#!/usr/bin/env python3
"""radar-feeds: daily fetch layer for the AI Radar and Paper Radar digests.

Runs on GitHub Actions (open internet), pulls papers and news that the
scheduled Claude runs cannot reach directly, and writes:

  latest/papers.md   latest/papers.json
  latest/news.md     latest/news.json
  latest/status.md   (per-source success/failure)
  data/<IST date>/   dated copy of the above
  data/fulltext/<arxiv id>.txt   full text of top new papers
  state/seen.json    first-seen ledger, so "NEW" means new since the last run

Design rule: no single source may break the run. Every fetch is wrapped,
logged in status, and the script always exits 0 after writing outputs.
"""
import datetime as dt
import io
import json
import os
import re
import shutil
import sys
import time
import traceback
import urllib.parse
import warnings

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

ROOT = os.path.dirname(os.path.abspath(__file__))
UA = "radar-feeds/1.0 (+https://github.com/RKarthik-AI-Labs/radar-feeds)"
BROWSER_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
NOW = dt.datetime.now(dt.timezone.utc)
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
TODAY_IST = NOW.astimezone(IST).date().isoformat()
ARXIV_DELAY = 3.5  # arXiv asks for >= 3 s between API calls

STATUS = []  # one dict per source attempt


# ---------------------------------------------------------------- helpers
def log(msg):
    print(f"[{dt.datetime.now(dt.timezone.utc):%H:%M:%S}] {msg}", flush=True)


def record(source, kind, ok, items=0, note="", seconds=0.0):
    STATUS.append({"source": source, "kind": kind, "ok": ok, "items": items,
                   "note": note[:300], "seconds": round(seconds, 1)})


def http_get(url, timeout=45, browser=False, tries=3):
    headers = {"User-Agent": BROWSER_UA if browser else UA,
               "Accept-Language": "en-US,en;q=0.9"}
    last = None
    for i in range(tries):
        try:
            r = requests.get(url, headers=headers, timeout=timeout)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
            if r.status_code in (403, 404, 410):
                break  # retrying won't help
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(3 * (i + 1))
    raise RuntimeError(last or "unknown error")


def iso(struct_time):
    if not struct_time:
        return None
    try:
        return dt.datetime(*struct_time[:6], tzinfo=dt.timezone.utc).isoformat()
    except Exception:  # noqa: BLE001
        return None


def parse_iso(s):
    if not s:
        return None
    try:
        d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    except Exception:  # noqa: BLE001
        return None


def clean(text, limit=None):
    if not text:
        return ""
    text = BeautifulSoup(text, "html.parser").get_text(" ")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit] if limit else text


def norm_title(t):
    t = re.sub(r"\s+-\s+[^-]{2,60}$", "", t or "")  # drop " - Source" suffix
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def fmt_date(s):
    d = parse_iso(s)
    return d.strftime("%Y-%m-%d %H:%M UTC") if d else "date unknown"


# ---------------------------------------------------------------- scoring
class Scorer:
    def __init__(self, topics):
        self.topics = {}
        for key, t in topics.items():
            self.topics[key] = {
                "label": t["label"], "weight": t["weight"],
                "res": [re.compile(p, re.I) for p in t["patterns"]],
            }

    def score(self, title, body=""):
        total, tags = 0, []
        for key, t in self.topics.items():
            in_title = any(r.search(title or "") for r in t["res"])
            in_body = any(r.search(body or "") for r in t["res"])
            if in_title or in_body:
                tags.append(key)
                total += t["weight"] * (2 if in_title else 1)
        return total, tags

    def label(self, key):
        return self.topics.get(key, {}).get("label", key)


# ---------------------------------------------------------------- ledger
def load_seen():
    path = os.path.join(ROOT, "state", "seen.json")
    if os.path.exists(path):
        try:
            with open(path) as f:
                data = json.load(f)
            data.setdefault("arxiv", {})
            data.setdefault("news", {})
            data.setdefault("sources", {})
            return data
        except Exception:  # noqa: BLE001
            pass
    return {"arxiv": {}, "news": {}, "sources": {}}


def save_seen(seen, keep_days=60):
    cutoff = (NOW - dt.timedelta(days=keep_days)).isoformat()
    for k in ("arxiv", "news"):
        seen[k] = {key: v for key, v in seen[k].items() if v >= cutoff}
    os.makedirs(os.path.join(ROOT, "state"), exist_ok=True)
    with open(os.path.join(ROOT, "state", "seen.json"), "w") as f:
        json.dump(seen, f, indent=0, sort_keys=True)


# ---------------------------------------------------------------- papers
def arxiv_query(search_query, max_results, cutoff, label):
    """Page through the arXiv API, newest submissions first, until cutoff."""
    out, start, page = [], 0, 500
    t0 = time.time()
    try:
        while start < max_results:
            n = min(page, max_results - start)
            url = ("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
                "search_query": search_query, "sortBy": "submittedDate",
                "sortOrder": "descending", "start": start, "max_results": n}))
            r = http_get(url, timeout=90)
            feed = feedparser.parse(r.content)
            entries = feed.entries
            time.sleep(ARXIV_DELAY)
            if not entries:
                break
            oldest = None
            for e in entries:
                pub = parse_iso(e.get("published"))
                oldest = pub if (oldest is None or (pub and pub < oldest)) else oldest
                m = re.search(r"abs/([^v\s]+)(v\d+)?$", e.get("id", ""))
                if not m:
                    continue
                out.append({
                    "id": m.group(1),
                    "version": (m.group(2) or "v1"),
                    "title": clean(e.get("title")),
                    "abstract": clean(e.get("summary")),
                    "authors": [a.get("name") for a in e.get("authors", [])],
                    "published": pub.isoformat() if pub else None,
                    "updated": e.get("updated"),
                    "categories": [t.get("term") for t in e.get("tags", [])],
                    "primary": e.get("arxiv_primary_category", {}).get("term"),
                    "comment": clean(e.get("arxiv_comment")),
                    "journal_ref": clean(e.get("arxiv_journal_ref")),
                    "doi": e.get("arxiv_doi"),
                    "abs_url": f"https://arxiv.org/abs/{m.group(1)}",
                    "found_via": [label],
                })
            start += len(entries)
            # stop once the newest-first listing has passed the cutoff; judge by the
            # last entry, not the single oldest one (one odd cross-list would stop early)
            last = parse_iso(entries[-1].get("published"))
            if last and last < cutoff:
                break
        kept = [p for p in out if p["published"] and parse_iso(p["published"]) >= cutoff]
        record(f"arXiv {label}", "papers", True, len(kept),
               f"{len(out)} fetched, {len(kept)} with v1 inside window", time.time() - t0)
        return kept
    except Exception as e:  # noqa: BLE001
        record(f"arXiv {label}", "papers", False, 0, str(e), time.time() - t0)
        return []


def hf_daily(cutoff):
    out = []
    for day in {NOW.date(), (NOW - dt.timedelta(days=1)).date()}:
        t0 = time.time()
        try:
            r = http_get(f"https://huggingface.co/api/daily_papers?date={day.isoformat()}")
            data = r.json()
            for row in data:
                p = row.get("paper", row)
                pid = p.get("id")
                if not pid:
                    continue
                out.append({
                    "id": pid, "version": "", "title": clean(p.get("title")),
                    "abstract": clean(p.get("summary")),
                    "authors": [a.get("name") for a in p.get("authors", [])],
                    "published": p.get("publishedAt"), "categories": [],
                    "primary": None, "comment": "", "journal_ref": "", "doi": None,
                    "abs_url": f"https://arxiv.org/abs/{pid}",
                    "found_via": ["HF daily papers"],
                    "hf_upvotes": row.get("paper", {}).get("upvotes"),
                })
            record(f"Hugging Face daily papers {day}", "papers", True, len(data), "", time.time() - t0)
        except Exception as e:  # noqa: BLE001
            record(f"Hugging Face daily papers {day}", "papers", False, 0, str(e), time.time() - t0)
    return out


def fulltext(paper, max_chars):
    """Try arXiv HTML, then PDF. Returns (text, how) or (None, reason)."""
    pid = paper["id"]
    try:
        r = http_get(f"https://arxiv.org/html/{pid}", timeout=60, tries=2)
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer", "math"]):
            tag.decompose()
        node = soup.find("article") or soup.body
        text = re.sub(r"\n{3,}", "\n\n", node.get_text("\n")) if node else ""
        if len(text) > 3000:
            return text[:max_chars], "html"
    except Exception:  # noqa: BLE001
        pass
    time.sleep(ARXIV_DELAY)
    try:
        from pypdf import PdfReader
        r = http_get(f"https://arxiv.org/pdf/{pid}", timeout=90, tries=2)
        reader = PdfReader(io.BytesIO(r.content))
        text = "\n".join((pg.extract_text() or "") for pg in reader.pages)
        if len(text) > 3000:
            return text[:max_chars], "pdf"
        return None, "pdf had no extractable text"
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def collect_papers(cfg, scorer, seen):
    pc = cfg["papers"]
    cutoff = NOW - dt.timedelta(days=pc["lookback_days"])
    by_id = {}

    def merge(p, core):
        s, tags = scorer.score(p["title"], p["abstract"])
        p["score"], p["topics"] = s, tags
        p["core"] = core
        if p["id"] in by_id:
            old = by_id[p["id"]]
            old["found_via"] = sorted(set(old["found_via"]) | set(p["found_via"]))
            old["core"] = old["core"] or core
            for k in ("categories",):
                old[k] = sorted(set(old[k]) | set(p[k]))
            if p.get("hf_upvotes") is not None:
                old["hf_upvotes"] = p["hf_upvotes"]
            return
        by_id[p["id"]] = p

    for c in pc["arxiv_categories"]:
        for p in arxiv_query(f"cat:{c['cat']}", c["max_results"], cutoff, c["cat"]):
            if c["keep_all"]:
                merge(p, True)
            else:
                s, _ = scorer.score(p["title"], p["abstract"])
                if s >= pc["min_score_non_core"]:
                    merge(p, False)
    for q in pc.get("arxiv_queries", []):
        for p in arxiv_query(q, 100, cutoff, f"search {q}"):
            merge(p, False)
    if pc.get("huggingface_daily_papers"):
        for p in hf_daily(cutoff):
            s, _ = scorer.score(p["title"], p["abstract"])
            if s >= pc["min_score_non_core"] or p["id"] in by_id:
                merge(p, False)

    papers = list(by_id.values())
    for p in papers:
        first = seen["arxiv"].get(p["id"])
        p["is_new"] = first is None
        p["first_seen"] = first or NOW.isoformat()
        seen["arxiv"][p["id"]] = p["first_seen"]

    # full text for the highest-scoring new papers
    ft_dir = os.path.join(ROOT, "data", "fulltext")
    os.makedirs(ft_dir, exist_ok=True)
    targets = sorted([p for p in papers if p["is_new"] and p["score"] > 0],
                     key=lambda p: -p["score"])[: pc["fulltext_top_n"]]
    t0, got = time.time(), 0
    for p in targets:
        path = os.path.join(ft_dir, f"{p['id']}.txt")
        if os.path.exists(path):
            p["fulltext"] = f"data/fulltext/{p['id']}.txt"
            got += 1
            continue
        text, how = fulltext(p, pc["fulltext_max_chars"])
        time.sleep(ARXIV_DELAY)
        if text:
            with open(path, "w") as f:
                f.write(f"{p['title']}\n{p['abs_url']}\n(source: arXiv {how})\n\n{text}")
            p["fulltext"] = f"data/fulltext/{p['id']}.txt"
            got += 1
        else:
            p["fulltext_error"] = how
    record("arXiv full text", "papers", got > 0 or not targets, got,
           f"{got}/{len(targets)} top new papers saved", time.time() - t0)
    papers.sort(key=lambda p: (-int(p["is_new"]), -p["score"], p["published"] or ""))
    return papers


# ---------------------------------------------------------------- news
def parse_feed_entries(content, source, bucket, scorer):
    feed = feedparser.parse(content)
    items = []
    for e in feed.entries:
        title = clean(e.get("title"))
        if not title:
            continue
        summary = clean(e.get("summary"), 500)
        s, tags = scorer.score(title, summary)
        items.append({
            "title": title, "url": e.get("link"), "source": source, "bucket": bucket,
            "published": iso(e.get("published_parsed") or e.get("updated_parsed")),
            "summary": summary, "topics": tags, "score": s, "via": "feed",
        })
    return items


def autodiscover(site):
    r = http_get(site, browser=True)
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all("link", rel=lambda v: v and "alternate" in v):
        if "rss" in (link.get("type") or "") or "atom" in (link.get("type") or ""):
            return urllib.parse.urljoin(site, link.get("href"))
    return None


def fetch_rss(src, scorer):
    t0 = time.time()
    errors = []
    for attempt in ("url", "discover"):
        url = src.get("url") if attempt == "url" else None
        try:
            if attempt == "discover":
                if not src.get("site"):
                    break
                url = autodiscover(src["site"])
                if not url:
                    errors.append("autodiscovery found no feed link")
                    break
            if not url:
                continue
            r = http_get(url, browser=True)
            items = parse_feed_entries(r.content, src["name"], src["bucket"], scorer)
            if items:
                note = "" if attempt == "url" else f"configured URL failed ({'; '.join(errors)}); used discovered feed {url}"
                record(src["name"], "feed", True, len(items), note, time.time() - t0)
                return items
            errors.append(f"{url}: 0 entries")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{url or 'autodiscovery on ' + str(src.get('site'))}: {e}")
    record(src["name"], "feed", False, 0, " | ".join(errors), time.time() - t0)
    return []


def fetch_html(src, scorer):
    t0 = time.time()
    try:
        r = http_get(src["site"], browser=True)
        soup = BeautifulSoup(r.text, "html.parser")
        pat = re.compile(src["link_pattern"])
        items, seen_urls = [], set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            path = urllib.parse.urlparse(href).path if href.startswith("http") else href.split("?")[0]
            if not pat.search(path):
                continue
            url = urllib.parse.urljoin(src["site"], href)
            if url in seen_urls:
                continue
            seen_urls.add(url)
            title = re.sub(r"\s+", " ", a.get_text(" ")).strip()
            if len(title) < 8:
                h = a.find(["h1", "h2", "h3", "h4"])
                title = h.get_text(" ", strip=True) if h else title
            if len(title) < 8:
                continue
            published = None
            t = a.find("time") or (a.parent.find("time") if a.parent else None)
            if t and t.get("datetime"):
                d = parse_iso(t["datetime"])
                published = d.isoformat() if d else None
            s, tags = scorer.score(title)
            items.append({"title": title[:220], "url": url, "source": src["name"],
                          "bucket": src["bucket"], "published": published, "summary": "",
                          "topics": tags, "score": s, "via": "page"})
        ok = len(items) > 0
        record(src["name"], "page", ok, len(items),
               "" if ok else "page loaded but no links matched (JS-rendered or pattern wrong)",
               time.time() - t0)
        return items
    except Exception as e:  # noqa: BLE001
        record(src["name"], "page", False, 0, str(e), time.time() - t0)
        return []


def bing_real_url(link):
    try:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)
        return q.get("url", [link])[0]
    except Exception:  # noqa: BLE001
        return link


STOPWORDS = {"or", "and", "launches", "launch", "releases", "release", "introduces", "model",
             "new", "survey", "search", "ai", "tool", "agent", "the", "for", "with"}


def relevance_terms(query):
    """What a hit's headline/snippet must contain to count as on-topic.
    - quoted phrases: all of them if the query has no OR, else any one
    - bare words (minus stopwords): at least one, if the query has any
    Returns None for site: queries (everything from that site is relevant)."""
    if "site:" in query:
        return None
    phrases = [p.lower() for p in re.findall(r'"([^"]+)"', query)]
    rest = re.sub(r'"[^"]*"', " ", query)
    words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9.\-]+", rest)
             if w.lower() not in STOPWORDS and len(w) >= 3]
    return {"phrases": phrases, "words": words, "any_phrase": " OR " in query}


def _norm(s):
    return " " + re.sub(r"[^a-z0-9.]+", " ", s.lower()) + " "


def is_relevant(text, terms):
    if terms is None:
        return True
    t = _norm(text)
    ph = [_norm(p) for p in terms["phrases"]]
    if ph:
        hit = any(p in t for p in ph) if terms["any_phrase"] else all(p in t for p in ph)
        if not hit:
            return False
    if terms["words"]:
        return any(f" {w} " in t or f" {w}s " in t for w in terms["words"])
    return True


def news_search(engine, query, window, group, scorer, max_items=10):
    t0 = time.time()
    name = f"{'Google News' if engine == 'google_news' else 'Bing News'}: {query}"
    try:
        if engine == "google_news":
            url = ("https://news.google.com/rss/search?" + urllib.parse.urlencode(
                {"q": f"{query} when:{window}", "hl": "en-US", "gl": "US", "ceid": "US:en"}))
        else:
            url = ("https://www.bing.com/news/search?" + urllib.parse.urlencode(
                {"q": query, "format": "rss", "qft": 'interval="8"'}))
        r = http_get(url, browser=True, tries=2)
        feed = feedparser.parse(r.content)
        items, dropped = [], 0
        terms = relevance_terms(query)
        for e in feed.entries:
            if len(items) >= max_items:  # engines return most relevant first
                break
            title = clean(e.get("title"))
            text = f"{title} {clean(e.get('summary'))}"
            # Google News matches on article bodies, so a headline that hits one of
            # the topic patterns is kept too. Bing results must match the query itself.
            topic_hit = engine == "google_news" and group in scorer.topics and \
                group in scorer.score(title)[1]
            if not (is_relevant(text, terms) or topic_hit):
                dropped += 1
                continue
            source = (e.get("source") or {}).get("title") if engine == "google_news" else None
            link = e.get("link")
            if engine == "bing_news":
                link = bing_real_url(link)
                source = e.get("news_source") or urllib.parse.urlparse(link).netloc
            s, tags = scorer.score(title, clean(e.get("summary"), 400))
            if source and title.endswith(f" - {source}"):
                title = title[: -len(source) - 3]
            items.append({"title": title, "url": link, "source": source or "unknown",
                          "bucket": f"search:{group}", "groups": [group],
                          "query": query, "engine": engine,
                          "published": iso(e.get("published_parsed")),
                          "summary": clean(e.get("summary"), 400) if engine == "bing_news" else "",
                          "topics": sorted(set(tags) | ({group} if group in scorer.topics else set())),
                          "score": s, "via": engine})
        record(name, "news search", True, len(items),
               f"{dropped} off-topic hits dropped" if dropped else "", time.time() - t0)
        return items
    except Exception as e:  # noqa: BLE001
        record(name, "news search", False, 0, str(e), time.time() - t0)
        return []


def collect_news(cfg, scorer, seen):
    items = []
    for src in cfg.get("feeds", []):
        items += fetch_rss(src, scorer) if src["type"] == "rss" else fetch_html(src, scorer)
    ns = cfg.get("news_searches", {})
    for group, queries in ns.get("queries", {}).items():
        engines = ns.get("engines_override", {}).get(group, ns.get("engines", ["google_news"]))
        for q in queries:
            for engine in engines:
                items += news_search(engine, q, ns.get("window", "2d"), group, scorer,
                                     ns.get("max_per_query", 10))
                time.sleep(1.0)

    window_days = 3
    cutoff = NOW - dt.timedelta(days=window_days)
    merged = {}
    for it in items:
        d = parse_iso(it["published"])
        if d and d < cutoff:
            continue
        key = norm_title(it["title"])
        if not key:
            continue
        if key in merged:
            m = merged[key]
            m.setdefault("also_in", [])
            label = it.get("query") and f"{it['via']}: {it['query']}" or it["source"]
            if label not in m["also_in"]:
                m["also_in"].append(label)
            m["topics"] = sorted(set(m["topics"]) | set(it["topics"]))
            m["groups"] = sorted(set(m.get("groups", [])) | set(it.get("groups", [])))
            # prefer a direct publisher URL over a Google News redirect
            if "news.google.com" in (m["url"] or "") and "news.google.com" not in (it["url"] or ""):
                m["url"] = it["url"]
            if not m["published"] and it["published"]:
                m["published"] = it["published"]
            continue
        merged[key] = dict(it)

    out = []
    for key, it in merged.items():
        src_first = seen["sources"].get(it["source"])
        first = seen["news"].get(key)
        it["is_new"] = first is None
        # first time we ever see an undated page source: treat as baseline, not news
        if it["is_new"] and not it["published"] and it["via"] == "page" and src_first is None:
            it["is_new"] = False
            it["baseline"] = True
        it["first_seen"] = first or NOW.isoformat()
        seen["news"][key] = it["first_seen"]
        if it["via"] == "page" and it["published"] is None and not it["is_new"]:
            continue  # undated page links seen before (or on the first visit) are not news
        out.append(it)
    for src in cfg.get("feeds", []):
        seen["sources"].setdefault(src["name"], NOW.isoformat())
    out.sort(key=lambda i: i["published"] or "", reverse=True)
    return out


# ---------------------------------------------------------------- writers
def write_papers_md(papers, scorer, path, max_with_abstract=60):
    all_hits = [p for p in papers if p["is_new"] and p["score"] > 0]
    new_hits, overflow = all_hits[:max_with_abstract], all_hits[max_with_abstract:]
    new_core_rest = [p for p in papers if p["is_new"] and p["score"] == 0 and p["core"]]
    older = [p for p in papers if not p["is_new"]]
    L = [f"# Paper candidates — {TODAY_IST} (IST)",
         "",
         f"Generated {NOW:%Y-%m-%d %H:%M} UTC. NEW = first seen in this run (i.e. since the previous run).",
         f"Totals: {len(new_hits)} new topic matches · {len(new_core_rest)} other new cs.IR · {len(older)} seen in earlier runs.",
         "Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.",
         ""]
    L.append(f"## New papers matching your topics ({len(new_hits)}), highest score first")
    for p in new_hits:
        topics = ", ".join(scorer.label(t) for t in p["topics"])
        authors = ", ".join(p["authors"][:4]) + (" et al." if len(p["authors"]) > 4 else "")
        L += ["",
              f"### {p['title']}",
              f"- arXiv {p['id']}{p.get('version') or ''} · v1 {fmt_date(p['published'])} · {', '.join(p['categories'][:5])}",
              f"- Authors: {authors}",
              f"- Topics: {topics} · score {p['score']} · found via {', '.join(p['found_via'])}",
              f"- Link: {p['abs_url']}"]
        if p.get("comment"):
            L.append(f"- arXiv comment: {p['comment']}")
        if p.get("journal_ref"):
            L.append(f"- Journal ref: {p['journal_ref']}")
        if p.get("fulltext"):
            L.append(f"- Full text: {p['fulltext']}")
        elif p.get("fulltext_error"):
            L.append(f"- Full text: not saved ({p['fulltext_error']})")
        L += ["", f"> {p['abstract']}"]
    if overflow:
        L += ["", f"## More new topic matches, lower score, title only ({len(overflow)})"]
        for p in overflow:
            L.append(f"- {p['title']} — {p['abs_url']} (score {p['score']}; "
                     f"{', '.join(scorer.label(t) for t in p['topics'])})")
    L += ["", f"## Other new cs.IR papers, title only ({len(new_core_rest)})"]
    for p in new_core_rest:
        L.append(f"- {p['title']} — {p['abs_url']}")
    L += ["", f"## Seen in earlier runs, still inside the look-back window ({len(older)})"]
    for p in older:
        if p["score"] > 0:
            L.append(f"- {p['title']} — {p['abs_url']} (score {p['score']})")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


def write_news_md(news, scorer, path, fresh_hours=30):
    """Compact digest input: each item appears once, in its first matching section.
    Shows items that are NEW since the previous run or published in the last
    `fresh_hours`. news.json keeps the full 3-day window with summaries."""
    groups = ["mentions", "fanout", "agents", "crawl", "ads", "search", "labs", "b2b", "sitewatch"]
    names = {"fanout": "Fan-out", "agents": "Agents", "crawl": "Crawl", "ads": "Ads",
             "search": "Search / AEO / GEO", "labs": "Model & lab launches (news search)",
             "b2b": "B2B buyer AI / adoption", "mentions": "Mentions of you",
             "sitewatch": "Sites with no usable feed (via Google News site: search)"}
    bucket_names = {"labs": "Labs (official feeds + trackers)", "search": "Search engines (official)",
                    "seo_press": "SEO / search press", "agents_crawl": "Agents & crawler access",
                    "tools": "Tools", "b2b": "B2B research"}
    fresh_cut = NOW - dt.timedelta(hours=fresh_hours)
    shown = [i for i in news if i["is_new"] or (parse_iso(i["published"]) or NOW) >= fresh_cut
             and i["published"]]
    hidden = len(news) - len(shown)

    def line(it):
        url = it["url"] or ""
        if "news.google.com" in url:
            url = "(Google News link; search the headline)"
        tags = ", ".join(scorer.label(t) for t in it["topics"] if t != "rag")
        s = f"- [{fmt_date(it['published'])}] {it['title']} — {it['source']} — {url}"
        if not it["is_new"]:
            s += " · (seen in an earlier run)"
        if tags:
            s += f" · {tags}"
        if it.get("also_in"):
            s += f" · +{len(it['also_in'])} other hits"
        return s

    L = [f"# News candidates — {TODAY_IST} (IST)", "",
         f"Generated {NOW:%Y-%m-%d %H:%M} UTC. Showing {len(shown)} items that are new since the "
         f"previous fetch run or published in the last {fresh_hours} h; {hidden} older items from the "
         "3-day window are only in news.json.",
         "Each item appears once, in the first section it matches. Dates are as reported by the source "
         "(\"date unknown\" = page with no date).", ""]
    used = set()
    L.append("## By priority topic")
    for g in groups:
        rows = [i for i in shown if id(i) not in used
                and (g in i.get("groups", []) or g in i["topics"])]
        used.update(id(i) for i in rows)
        if rows or g in ("fanout", "agents", "crawl", "ads", "mentions"):
            L += ["", f"### {names[g]} ({len(rows)})"]
            L += [line(i) for i in rows] or ["- nothing new"]
    L += ["", "## Other items from source feeds"]
    for b, label in bucket_names.items():
        rows = [i for i in shown if id(i) not in used and i["bucket"] == b]
        used.update(id(i) for i in rows)
        if rows:
            L += ["", f"### {label} ({len(rows)})"] + [line(i) for i in rows]
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


def write_status_md(path, started):
    ok = [s for s in STATUS if s["ok"]]
    bad = [s for s in STATUS if not s["ok"]]
    L = [f"# Run status — {TODAY_IST} (IST)", "",
         f"Started {started:%Y-%m-%d %H:%M:%S} UTC, took {time.time() - started.timestamp():.0f} s.",
         f"Sources OK: {len(ok)} · failed: {len(bad)}", ""]
    if bad:
        L += ["## Failed", "", "| Source | Kind | Error |", "|---|---|---|"]
        L += [f"| {s['source']} | {s['kind']} | {s['note'].replace('|', '/')} |" for s in bad]
        L.append("")
    L += ["## OK", "", "| Source | Kind | Items | Note |", "|---|---|---|---|"]
    L += [f"| {s['source']} | {s['kind']} | {s['items']} | {s['note'].replace('|', '/')} |" for s in ok]
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


def prune(retention_days, seen):
    data = os.path.join(ROOT, "data")
    if not os.path.isdir(data):
        return
    cutoff = (NOW.astimezone(IST) - dt.timedelta(days=retention_days)).date().isoformat()
    for name in os.listdir(data):
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", name) and name < cutoff:
            shutil.rmtree(os.path.join(data, name), ignore_errors=True)
    ft = os.path.join(data, "fulltext")
    if os.path.isdir(ft):
        old = (NOW - dt.timedelta(days=retention_days)).isoformat()
        for fn in os.listdir(ft):
            pid = fn[:-4]
            if seen["arxiv"].get(pid, NOW.isoformat()) < old:
                os.remove(os.path.join(ft, fn))


# ---------------------------------------------------------------- main
def main():
    started = dt.datetime.now(dt.timezone.utc)
    with open(os.path.join(ROOT, "sources.yaml")) as f:
        cfg = yaml.safe_load(f)
    scorer = Scorer(cfg["topics"])
    seen = load_seen()
    only = sys.argv[1] if len(sys.argv) > 1 else "all"

    latest = os.path.join(ROOT, "latest")
    dated = os.path.join(ROOT, "data", TODAY_IST)
    os.makedirs(latest, exist_ok=True)
    os.makedirs(dated, exist_ok=True)

    if only in ("all", "papers"):
        try:
            papers = collect_papers(cfg, scorer, seen)
            with open(os.path.join(latest, "papers.json"), "w") as f:
                json.dump({"generated_utc": NOW.isoformat(), "papers": papers}, f, indent=1)
            write_papers_md(papers, scorer, os.path.join(latest, "papers.md"),
                            cfg["papers"].get("max_with_abstract", 60))
        except Exception:  # noqa: BLE001
            record("papers pipeline", "internal", False, 0, traceback.format_exc()[-300:])
    if only in ("all", "news"):
        try:
            news = collect_news(cfg, scorer, seen)
            with open(os.path.join(latest, "news.json"), "w") as f:
                json.dump({"generated_utc": NOW.isoformat(), "items": news}, f, indent=1)
            write_news_md(news, scorer, os.path.join(latest, "news.md"),
                          cfg.get("news_searches", {}).get("fresh_hours", 30))
        except Exception:  # noqa: BLE001
            record("news pipeline", "internal", False, 0, traceback.format_exc()[-300:])

    write_status_md(os.path.join(latest, "status.md"), started)
    for fn in ("papers.md", "papers.json", "news.md", "news.json", "status.md"):
        src = os.path.join(latest, fn)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(dated, fn))
    save_seen(seen)
    prune(cfg.get("retention_days", 21), seen)
    log(f"done: {sum(s['ok'] for s in STATUS)} sources ok, "
        f"{sum(not s['ok'] for s in STATUS)} failed")


if __name__ == "__main__":
    main()
