# radar-feeds

Daily fetch layer for the **AI Radar** and **Paper Radar** scheduled digests.

The scheduled Claude runs can't reach arXiv, news sites or RSS feeds directly, and their web search has no date filter. This repo fills that gap: a GitHub Actions job with open internet access pulls papers and news every morning and commits plain files the digests read first.

## What runs when

| Time (IST) | Job |
|---|---|
| 06:07 | Fetch run 1 (arXiv EDT announcement + overnight news) |
| 06:47 | Fetch run 2 (arXiv EST announcement + anything run 1 missed) |
| 07:15 | Paper Radar reads `latest/papers.md` |
| 07:40 | AI Radar reads `latest/news.md` |

GitHub can delay scheduled jobs by 10–30 minutes under load. Check the "Generated" line at the top of each file.

## Files the digests read

All public, no login needed:

- `https://raw.githubusercontent.com/RKarthik-AI-Labs/radar-feeds/main/latest/papers.md`: new arXiv papers matching the topics, highest score first, with full abstracts. Other new cs.IR papers are listed as titles.
- `https://raw.githubusercontent.com/RKarthik-AI-Labs/radar-feeds/main/latest/news.md`: news from the last 3 days, grouped by priority topic (Fan-out, Agents, Crawl, Ads, Search, Labs, B2B, Mentions), then by source feed.
- `https://raw.githubusercontent.com/RKarthik-AI-Labs/radar-feeds/main/latest/status.md`: which sources worked and which failed this run.
- `https://raw.githubusercontent.com/RKarthik-AI-Labs/radar-feeds/main/data/fulltext/<arxiv id>.txt`: full text of the top new papers (arXiv HTML, falling back to PDF text).

`latest/*.json` holds the same data in structured form. `data/<date>/` keeps a dated copy for 21 days.

**NEW** means first seen since the previous fetch run, tracked in `state/seen.json`. It does not mean "published today".

## Changing what gets fetched

Edit `sources.yaml`. Pushing a change to it triggers a fresh run, so check `latest/status.md` a few minutes later.

- **topics:** keyword patterns that tag and score papers and news.
- **papers:** arXiv categories, extra arXiv searches, the score threshold, and how many full texts to save.
- **feeds:** RSS feeds, or pages to scrape for sites without a feed.
- **news_searches:** date-filtered Google News and Bing News queries per priority topic.

## Manual run

Go to Actions → "Fetch radar feeds" → Run workflow.
