# Paper candidates — 2026-11-17 (IST)

Generated 2026-11-17 09:41 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 34 new topic matches · 20 other new cs.IR · 39 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (34), highest score first

### Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning
- arXiv 2611.20045v1 · v1 2026-11-15 14:44 UTC · cs.AI, cs.CR
- Authors: Yang Luo, Guangpu Chen, Yichen Liu, Zhaoyu Chen et al.
- Topics: GEO/AEO, Citation & source selection, RAG (generic), Query fan-out, Manipulation · score 23 · found via cs.AI, cs.CR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2611.20045
- arXiv comment: 31 pages, 5 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Deep research and agentic search agents autonomously retrieve content from the open web and generate reports with citations, and their outputs are often taken directly as research conclusions. This paper systematizes security research in this area along four stages, namely retrieval, planning, evidence integration, and report generation. We present a unified threat model, a taxonomy of attacks and defenses, and a review of evaluation benchmarks, and we align the area dimension by dimension with retrieval-augmented generation (RAG) poisoning, prompt injection, and generative engine optimization (GEO). Coding 34 primary studies shows that only 26.5% of them involve the planning stage, and none performs an end-to-end poisoning evaluation on commercial products. To address this gap, we propose the agenda seeding attack, in which the attacker writes no instructions and only introduces a fictitious evaluation metric. Across 3,520 sandboxed research runs under the same budget, GEO and prompt injection are nearly ineffective, whereas agenda seeding makes the attacker's target the top pick in 16% to 28% of reports. Injection detection and query anchoring fail against it, verification prompting hurts utility, and our proposed provenance tagging preserves utility but can be bypassed by multi-site bait. Finally, we propose eight research directions.

### User First Intelligence: Three Measurements of Search and AI-Answer Analytics (SEO and GEO/AEO), and a Knowledge-Graph Framework for Query Discovery Beyond Search Volume
- arXiv 2611.19655v1 · v1 2026-11-14 22:51 UTC · cs.IR
- Authors: Venkata Pagadala
- Topics: GEO/AEO, Citation & source selection, Brand/product recommendation · score 18 · found via cs.IR, search abs:"AI overviews"
- Link: https://arxiv.org/abs/2611.19655
- arXiv comment: 43 pages, 10 figures. Preprint, not peer reviewed. Data and scripts in the ancillary files; implementation at https://github.com/VenkataPagadalaGIT/ufi
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> People say what they want to know in many places besides a search box, and the tools that search and AI-answer optimization (SEO and GEO/AEO) rely on see only part of that demand, through models reported as counts. This paper reports three measurements of such instruments and a framework. On the area-code section of a large US telecom provider's site, two commercial analytics platforms differed on estimated monthly visits by 7.5x to 27.1x (8.6x to 29.9x worldwide); across twelve sections of the domain the ratio ran from 0.20x to 7.24x with no detectable relation to section age, while they agreed on which section is larger in 60 of 66 pairs. On 37,193 reviews of 378 telecom stores linked to a 42,994-node keyword taxonomy, review demand and search volume agreed on branches to a varying degree (Spearman 0.47 to 0.75; 0.91 post hoc) and barely on topics (0.18), on links two blind AI annotators judged two-thirds correct; on the 372 area codes, a public count of Wikipedia requests for each code and vendor volume agreed roughly on ranking (0.45 over 240 articles, gone once keywords matched per code are held constant) and not on magnitudes, predictions fixed first. In one vendor's index of AI answers naming or citing the largest companies of each S&P 500 sector, of four predictions written first, one held, one in direction only and two failed; video and community sites took a median 21% of citation incidences on Google's AI Overviews and AI Mode against 0.6% to 9.2% on four other surfaces, in every sector, and in education answers in each of 13 countries read later. Estimates and sources need measuring per instrument and surface. User First Intelligence (UFI), built on that premise, collects what people ask beyond the website, links it to an industry ontology and scores where an organization does not answer; an open implementation is released, its score not evaluated. No causal claim is made.

### Data Attribution Should Steer Pretraining
- arXiv 2611.19698v1 · v1 2026-11-15 01:03 UTC · cs.AI, cs.CL, cs.LG
- Authors: Glenn Matlin, Chandreyi Chakraborty, Mohammed Rehan Parwani, Saehee Eom et al.
- Topics: GEO/AEO, Citation & source selection · score 13 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.19698
- arXiv comment: Accepted to the 3rd Workshop on Attributing Model Behavior at Scale: Data Attribution and Provenance (ATTRIB 2026) at NeurIPS 2026, Idea Track. 4 pages main text, 13 pages total, 1 figure, 2 tables
- Full text: data/fulltext/2611.19698.txt

> Pretraining data curation decides what a model learns from, yet what makes a document worth learning from depends on what the model already knows. Influence-driven selectors already rank documents to improve one run; we argue that training-data attribution should steer pretraining by identifying testable data properties that become reusable curation criteria, evaluated on new data against cheaper selectors at matched total cost, discovery included. A document ranking is consumed by the run it was computed for, whereas an explained data property can be tested across corpora and checkpoints, especially where familiar quality signals diverge from measured usefulness. Because historical contribution, an understandable explanation, and future data value require distinct evidence, we specify a feedback loop that interprets attributed sources, tests candidate data changes, and states for five claim types what evidence each requires and what none establishes. We close with a falsifiable comparison against perplexity, classifier, and mixing baselines at equal total compute.

### Explainable Federated Learning via Global-Local Attribution Alignment
- arXiv 2611.20445v1 · v1 2026-11-16 03:15 UTC · cs.LG, cs.AI
- Authors: Dawood Wasif, Terrence J. Moore, Chang-Tien Lu, Jin-Hee Cho
- Topics: Citation & source selection, Manipulation · score 11 · found via cs.AI
- Link: https://arxiv.org/abs/2611.20445
- arXiv comment: 26 pages, 2 figures, 9 tables. Published in Proceedings of the 43rd International Conference on Machine Learning (ICML 2026)
- Journal ref: Proceedings of Machine Learning Research, 306:133305-133330, 2026
- Full text: data/fulltext/2611.20445.txt

> Federated learning enables on-device training without centralizing data, yet existing systems still struggle to provide explanations that are both locally faithful and globally consistent under strict privacy and bandwidth constraints. Prior approaches either keep explanations siloed across clients, transmit heavy or sensitive artifacts, or replace expressive task models with interpretable surrogates that sacrifice accuracy. We propose xFedAlign, a model-agnostic framework that decouples task optimization in parameter space from explanation coordination in a compact group space. Each client distills a lightweight surrogate to produce private, per-class top-k attribution artifacts, which are robustly aggregated by the server into a Global Explanation Prior that softly aligns client explanations without constraining task learning. Across image, text, and tabular benchmarks with IID and non-IID partitions, xFedAlign matches FedAvg accuracy while consistently reducing explanation drift and improving deletion and insertion AUC relative to Local-XAI, FedAttr-Agg, and Fed-XAI, with only a few kilobytes of additional communication per round. Privacy and robustness evaluations further demonstrate reduced membership inference advantage and increased resistance to attribution poisoning, enabling consistent and trustworthy explanations in federated learning.

### DetouR: Plugging Association Routes into Search Agents for Multi-hop Question Answering
- arXiv 2611.19967v1 · v1 2026-11-15 12:21 UTC · cs.IR
- Authors: Tingwei Chen, Yunxiao Shi, Zhendong Chu, Zhiying Deng et al.
- Topics: Query fan-out · score 10 · found via cs.IR
- Link: https://arxiv.org/abs/2611.19967
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Search agents answer multi-hop questions by interleaving reasoning with retrieval, deciding at each step what to search next. Existing agents follow semantic routes: they infer what is missing and phrase it as a query, reaching only what the model can name. Yet the decisive page is often one the question never names, frequently just one hyperlink away from evidence already retrieved. Following such association routes reaches more gold pages than semantic search under the same budget. Exploiting them raises two challenges: obtaining the association structure without costly offline graph construction, and keeping linked evidence in the reader's limited context, where relevance- and fusion-based selection discards it. We propose DetouR, a plug-in that reuses the links arriving with retrieved pages and adds no search or LLM call. Link Rerouting replaces near-repeat queries with routes to linked pages, chosen by a lightweight learned scorer; Chain-aware Context Selection runs personalized PageRank over these links so that evidence chains reach the reader intact. Across four agents, DetouR improves EM by 4.0 points on 2Wiki and 1.4 on HotpotQA on average. We also find that heavier LLM models struggle with this non-semantic evidence, adding little over these simple selectors or even falling behind. In summary, our work reveals association routes as a cheap complement to semantic routes that current search agents overlook: added as a plug-in, they improve every agent we test, in replay and in live runs, at no extra search or LLM cost.

### EchoSpec: Training Search Agents to Weigh Evidence Above Echoes
- arXiv 2611.20034v1 · v1 2026-11-15 14:25 UTC · cs.IR
- Authors: Shihao Yang, Can Zeng, Xinzhe Li
- Topics: Query fan-out · score 10 · found via cs.IR
- Link: https://arxiv.org/abs/2611.20034
- arXiv comment: 24 pages, 5 figures, 15 tables. Code: https://github.com/unihsy/EchoSpec
- Full text: data/fulltext/2611.20034.txt

> Search agents trained with reinforcement learning decide what to retrieve, when to search again, and when to answer. In real corpora, one claim is copied and paraphrased across many pages while the primary source settling a question appears once. We show that reinforcement-learned search agents grant echoes the credence of independent sources and lose their ability to abstain. Across five base models from 3B to 32B and seven released RL agents on multi-hop Wikipedia questions with primary evidence intact, eight paraphrased false-claim echoes overturn 58-73% of previously correct answers, while exact-match RL drives deleted-evidence abstention below 15%. Conditioning on retrieval localizes the failure to evidence acquisition: once primary evidence enters context, agents overrule eight echoes as reliably as one, whereas echoes fill top ranks and halt search early, so larger budgets, forced search turns, or passive passage filtering alone fail to recover displaced evidence. We introduce EchoSpec, specifying reliability across five corpus transformations with known target answers and training in two stages. Verification warm-start teaches multi-hop bridge-entity recovery past echoes, after which group RL optimizes an evidence-gated $λ$-reward with an outcome-independent acquisition bonus and scale-preserving advantages retaining the optimal rule $λ/(1+λ)$. Across Qwen2.5-3B, Qwen2.5-7B, and Llama-3.1-8B backbones on nine evaluation suites, EchoSpec cuts eight-echo deference by 30-44 points on Qwen2.5-7B down to 29-31%, nearly quadruples eight-echo reach to 26-27% with zero-shot transfer to unseen BGE and BM25 retrievers, and raises standalone QA precision to 47-55%. Code is publicly available at https://github.com/unihsy/EchoSpec.

### On Representational and Functional Alignment of Training Data Attribution Methods for Language Models
- arXiv 2611.19286v1 · v1 2026-11-14 09:30 UTC · cs.CL
- Authors: Loris Schoenegger, Benjamin Roth
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.19286
- arXiv comment: EACL 2027. 9 pages
- Full text: data/fulltext/2611.19286.txt

> Existing approaches to training data attribution derive influence estimates from different sources of information, including gradients, model-internal states, and surface-level similarity. However, comparisons between attribution methods remain incomplete, often relying on indirect evaluations through downstream task performance. In this work, we introduce a framework for directly comparing methods along three dimensions: functional alignment, which measures correlation between full attribution vectors; representational alignment, which captures structural similarity of the representations underlying attribution; and cross-method predictability, which evaluates agreement on local pairwise ranking decisions. We observe strong representational and moderate functional alignment within paradigms. Alignment across paradigms is low and task-dependent, yet stable across models. Our results suggest that the similar downstream performance observed across paradigms in prior work can be attributed to agreement on the relative importance of documents, rather than to agreement on rankings of the full training data.

### MathaMAGICal: Validating Trajectory Data Attribution During Capability Acquisition
- arXiv 2611.19692v1 · v1 2026-11-15 00:51 UTC · cs.AI, cs.CL, cs.LG
- Authors: Jason Lee, Dikshanta Pokhrel, Phonn Nay Khant, Victor Lee et al.
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.19692
- Full text: data/fulltext/2611.19692.txt

> Influence-function-based methods like MAGIC provide exact first-order scores for trajectory data attribution, yet only retraining indicates whether those scores accurately predict data removal. We evaluate MAGIC on $86$M- and $152$M-parameter GPT-2-style models learning multistep arithmetic from scratch on filtered web text and four synthetic math families. Full-run attribution at $86$M suffers from numerical overflow, and even with metagradient clipping, scores correlate near chance with retraining (linear datamodeling score, LDS, $0.17$--$0.22$). In contrast, short checkpoint windows yield stable, accurate predictions at both scales (LDS $0.86$--$0.99$ across four $100$-step windows at $152$M), whereas a single-checkpoint gradient-dot baseline shows near-zero correlation. Rankings of individual training blocks predict retraining only within that single run and do not transfer across seeds or hyperparameters ($ρ\le 0.09$), whereas format-level patterns replicate across runs. Two data families, worked examples and primitive facts, occupy $2.1$--$2.6\times$ their corpus share in both the helpful and harmful $5\%$ score tails, reflecting strong bidirectional local sensitivity distinct from net benefit under multi-epoch family deletion. These results show that trajectory attribution is reliable within short, validated windows and yields family-level insights that generalize across runs.

### IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu
- arXiv 2611.20448v1 · v1 2026-11-16 03:17 UTC · cs.IR
- Authors: Dongjia Zhao, Yuchen Ma, Chunsheng Shi, Ziqiu Gui et al.
- Topics: Query fan-out, Clicks & measurement · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.20448
- arXiv comment: 29 pages, 7 figures. Technical report
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multimodal search with image-text queries helps users find notes in user-generated content (UGC) communities and serves as a key search tool for multimodal search agents. For such queries, query-note relevance depends on the user's retrieval intent and cannot be determined by visual or topical similarity alone. Simply reranking visual search results cannot fully address this challenge, as notes relevant to the user's intent may be missing from the initial candidate set. This motivates explicit intent modeling to align candidate retrieval and reranking under consistent relevance criteria. We present IntentFlow, an intent-driven real-time multimodal search system deployed at Xiaohongshu over an index on the order of ten billion entries. IntentFlow represents retrieval objectives with a hierarchical intent taxonomy and uses intent-specific relevance criteria to guide data construction, representation learning, and reranking. An offline agentic data workflow acquires candidates and verifies their relevance under these criteria to produce training supervision. The embedding model combines intent-aware contrastive learning, graded ranking, and distribution distillation, while a compact reranker assesses query-candidate evidence conditioned on predicted hierarchical intents. Evaluations demonstrate that IntentFlow delivers substantial gains in search engagement while supporting real-time search at industrial scale. In a user-level A/B test on the Xiaohongshu platform, IntentFlow outperforms the existing production system based on visual search followed by reranking, achieving relative gains of 28.17% in Top-4 query click-through rate, 18.96% in query click-through rate, and 12.56% in average time spent on search results pages per user. Production monitoring records an end-to-end P50 latency of 1.07 s.

### EVIDENT: Evaluating Evidence Grounding in GUI Agents
- arXiv 2611.20488v1 · v1 2026-11-16 03:56 UTC · cs.AI, cs.HC
- Authors: Yerin Nam, Minkyung Cho, MinKyu Kim, SeungWoo Song et al.
- Topics: Agents · score 8 · found via cs.AI, cs.HC
- Link: https://arxiv.org/abs/2611.20488
- arXiv comment: Accepted to EACL 2027 Findings. 36 pages
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> GUI agents are increasingly evaluated by whether they complete web tasks, but surface success can hide a critical failure: the final answer may not be supported by evidence observed during navigation. We introduce EVIDENT, an evidence-driven benchmark for evaluating whether GUI agents ground their decisions in observable web evidence. EVIDENT contains 220 real-world English and Korean tasks spanning semantic grounding, contextual inference, and visual grounding, each paired with human-curated evidence metadata specifying what must be verified. We further separate surface task completion from evidence-grounded success using three metrics: TSR, ESR, and GSR, which respectively measure outcome success, required evidence observation, and claim-level evidence support. Experiments on commercial and open-source GUI agents reveal substantial gaps between surface success and evidence-grounded success, especially in contextual and visual tasks. These results show that current evaluations can overestimate agent reliability and highlight the need to assess not only whether agents answer, but whether they verify.

### UIAnchor: Anchoring UI Perception and Action Execution for Reliable Service-Composed Mobile Task Automation with GUI Agents
- arXiv 2611.20753v1 · v1 2026-11-16 09:01 UTC · cs.HC
- Authors: Wentao Zhou, Sicong Liu, Zimu Zhou, Yimeng Duan et al.
- Topics: Agents · score 8 · found via cs.HC
- Link: https://arxiv.org/abs/2611.20753
- Journal ref: Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 10, Issue 3, Article 197 (2026), Pages 1-30
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Mobile task automation aims to streamline multi-step, cross-app interactions on smartphones and in-vehicle systems. Recent LLM-based GUI agents have advanced rapidly, yet reliability remains limited because modern mobile workflows are increasingly service-composed (app switching, forms, pop-ups/permissions, copy-paste), requiring fine-grained operations on dense, dynamic, and heterogeneous UIs, often in distraction-sensitive contexts (e.g., hands-busy or attention-limited use). Through an in-the-wild failure analysis of deployable GUI agents, we identify two dominant bottlenecks: agents often miss or misread actionable UI elements, and they execute actions without verifying target correctness or outcomes. We present UIAnchor, a modular multi-agent system that improves mobile GUI automation by anchoring both perception and execution. UIAnchor combines a two-stage UI parser for high-recall element capture and context-aware semantics with a meta-controller that performs pre-action verification, post-action outcome perception, per-step state tracking, and targeted recovery. We further introduce an L1-L5 task taxonomy based on step length, cross-app scope, and UI granularity, showing that L5 remains beyond today's practical frontier. On the hardest practical tier, L4 tasks (20-30 steps, multi-app, targets < 100 x 100 px, ~5 mm on typical phones), UIAnchor improves success by 31.5% over GPT-4o and 16.6% over Mobile-Agent-v3. With edge/cloud assistance, UIAnchor runs at ~2 s per step, comparable to human operation, while reducing per-step latency by up to 75.5% and energy by 52.4%. It also generalizes to unseen apps and cross-platform GUIs.

### EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation
- arXiv 2611.20846v1 · v1 2026-11-16 10:22 UTC · cs.AI, cs.CL
- Authors: Zixuan Wang, Gregory Kang Ruey Lau, Xiao Tian, Jue Fan et al.
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.20846
- Full text: data/fulltext/2611.20846.txt

> Disentangling writing style from semantic content is a fundamental challenge in literary text modeling. Style-content entanglement causes models to rely on semantic content for authorship attribution (AA) tasks and memorize author-specific content for style imitation (SI) tasks. We propose EDITORS (EditingLoRA Subspaces), a diagnose-then-deflate framework that adapts pretrained large language models and prioritizes stylistic features, making it effective for both AA and SI tasks. EDITORS first trains a diagnostic LoRA adapter using style-neutral statements derived from the training corpus to identify a content-oriented subspace. It then trains the final style adapter under activation-space deflation that projects input activations away from the identified content-oriented directions. We empirically demonstrate that EDITORS is effective. On three AA benchmarks spanning literature, social media, and news, EDITORS achieves state-of-the-art accuracy, outperforming the strongest existing baseline by up to 29%. On SI, EDITORS generates stylistically faithful and diverse passages, outperforming baselines in achieving style similarity while adhering to content specifications.

### MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory
- arXiv 2611.21019v1 · v1 2026-11-16 12:38 UTC · cs.CL
- Authors: Ruiyang Jiang, Xinyang Liao, Weikai Huang, Yuqi Niu et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.21019
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown. When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, and the answer alone does not say where. We formalize multimodal memory as four stages, Write, Update, Retrieve and Answer, and define nine error types across them. A stage-resolved analysis on Mem-Gallery traces most failures to a source stage, and most of those lie before the answer. Injecting known errors against fact-preserving control edits, we then follow each tainted record downstream. Early errors survive to the answer as apparent evidence, and hurt most when no other record holds the fact. A diagnosis that trusts the quoted evidence therefore blames the stage where the error surfaces, not the one where it began. We propose MemDoctor, in which the MLLM that built the memory diagnoses its own failures. It traces each needed fact backward through the four stages, accepts a diagnosis only when the cited evidence is found in memory, and repairs that stage before answering again. On a 4B backbone, MemDoctor improves accuracy on both Mem-Gallery and MemLens, outperforming all evaluated 8B baselines, and the same loop also improves MuRAG and A-Mem.

### Portrait Fitness as a Pretext: Probing Implicit Demographic Bias in VLMs
- arXiv 2611.21403v1 · v1 2026-11-16 16:55 UTC · cs.CV, cs.CY
- Authors: Alexandre Fournier-Montgieux, Akram Elbouanani, Aboubacar Tuo, Adrian Popescu et al.
- Topics: Brand/product recommendation, Ads · score 8 · found via cs.CY
- Link: https://arxiv.org/abs/2611.21403
- arXiv comment: Accepted at WACV 2027
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> We audit face-related bias in VLMs using BALPORTRAITS, a new balanced dataset of 9,000 fictional portraits across ethnicity, gender, and age segments. Sixteen VLMs estimate portrait fitness scores for occupations, brands, activities, and banking or insurance products within an advertising-casting framework designed to avoid direct inference of protected attributes. Item-level estimations are aggregated with scenario-specific prestige scores to compare rankings across demographic groups. While the magnitude and direction of these biases vary across scenarios, model families, and demographic dimensions, with age, ethnicity, and gender contributing differently depending on the task, we find demographic dispersion across all evaluated models, with a majority of pairwise segment differences reaching statistical significance. This study introduces a controlled protocol to assess implicit face-related associations and demonstrates that single-scenario or single-attribute audits are insufficient.

### Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle
- arXiv 2611.21538v1 · v1 2026-11-16 18:25 UTC · cs.AI, cs.CL, cs.LG
- Authors: Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R., Arun Prakash et al.
- Topics: RAG (generic), Brand/product recommendation, Clicks & measurement · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.21538
- arXiv comment: 30 pages. A shorter version, "The Verifier Gap", appears at the NeurIPS 2026 Workshop on Meta-Agents (non-archival)
- Full text: data/fulltext/2611.21538.txt

> Reinforcement learning from verifiable rewards inherits whatever its verifier gets wrong. Outside mathematics and code the verifier is a proxy, a rubric, a learned judge or a hand-written checker, and its distance from the true objective is never measured, so a rising reward cannot be told apart from a hack. We build a setting where the true reward is exactly computable at the process level: executable authorization policies over 124,416 contexts admit an oracle that lists every minimal sufficient reason for every decision. We compile these policies into exact process rewards, degrade the verifier along seven realistic axes (outcome-only, sufficiency, recall-only, extraction noise, coarse taxonomy, stale policy, LLM judge), and train against each while the exact verifier scores every rollout. Four phenotypes appear. Optimistic verifiers are hacked by padding: the sufficiency proxy ends at 0.940 while true faithfulness falls from 0.731 to 0.667 on 96 held-out episodes. Outcome-only verifiers saturate and stop teaching, noise dilutes, and ranking-preserving gaps do no harm. A model-free audit of the verifier, its selection error and gap sign, together with a short saturation pilot, anticipates which phenotype a run will produce. Across nine configurations spanning two frameworks, two model vendors, two adapter sizes, three precisions, two initialisations and two seeds, the phenotypes recur, sufficiency damage is positive in all 10 replication cells and beyond two standard errors in 7, and optimistic gaps remain the steeper branch. The damage magnitude does not replicate, and five pre-registered attempts to explain it are reported as they fell. We release the testbed, the training instrumentation, and 14 real public policies (Cedar, OPA, Gatekeeper) ported to executable oracles.

### ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises
- arXiv 2611.21579v1 · v1 2026-11-16 18:49 UTC · cs.AI, cs.CR
- Authors: Jaime C. Acosta, Anantaa Kotal, Aritran Piplai
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.21579
- Full text: data/fulltext/2611.21579.txt

> Cyber-range and capture-the-flag scenario construction remains labor-intensive because authors must coordinate infrastructure, vulnerable services, attack paths, artifacts, and success conditions. LLMs can propose detailed exercises, but plausible descriptions do not guarantee deployable software or verifiable objectives. We present ScenarioForge, which turns high-level requirements into resource-grounded topologies, services, traffic, segmentation, and challenge chains, then instantiates and validates them in the Common Open Research Emulator (CORE). The ScenarioForge Execution Dataset contains 226 materialized scenarios covering 294 Vulhub images and all 85 custom-built challenge-resource generators developed with our AI-assisted scaffolding. All 226 passed construction, preview, sequencing, deployment, strict runtime validation, and live artifact checks; their 867 steps, each an individually verifiable challenge objective, comprise 457 vulnerability-backed and 410 generated-resource-backed instances. In a separate 50-prompt matched benchmark, ScenarioForge+Qwen3.8 and ScenarioForge+GPT5.6 each achieved 50/50 (100%) topology/build success and 160/160 intent fields; direct frontier generation reached 41/50 builds and 147/160 fields only with the full cumulative scaffold: structure, vocabulary, policy, and container-image guidance. The test still omitted ScenarioForge's downstream challenge-resource generation, dependency/flag sequencing, deployment, and live validation. The artifacts support operationally rich, reproducible exercises for training and evaluation.

### Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering
- arXiv 2611.21586v1 · v1 2026-11-16 18:54 UTC · cs.CL
- Authors: Yisong Cao, Leah Kim, Brian Wright, Ali Rivera
- Topics: Ads · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.21586
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Job titles and job descriptions alone provide limited insight into how technical roles differ in a changing job market. To assess how such roles differ in their work and industry applications, we design and compare two methods based on deep learning and transformer representations using 36,081 early-career job postings collected from LinkedIn in the United States between December 2025 and October 2026. We first apply PERC, short for Preprocessing (P), Embedding (E), Dimensionality Reduction (R) and Clustering (C). We employ GPT-6 Luna to classify job description passages into Team context, Role task and Qualifications. We then create combinations of these sections and examine whether embedding and clustering the segmented passages produce meaningful semantic clusters about different job roles. We use Maximum Mean Discrepancy (MMD) to rank observed differences between embedding distributions and employ a pretrained sparse autoencoder (SAE) to extract features from layer-19 representations of Llama-3.1-8B-Instruct. Lastly, we employ GPT-6 Luna to come up with hypotheses about job roles' feature patterns, and GPT-6.1 Terra to investigate whether those patterns exist in held-out job descriptions from unseen companies. Some example findings include Data Scientist advertisements placing more emphasis on machine learning model development, Data Analyst advertisements on reporting business performance, and Machine Learning Engineer advertisements on applying developed models in real-world settings. We also observe differences in the applications described by Data Analyst and Business Analyst advertisements across selected months, although our dataset's scale and uneven coverage limit their interpretation. Overall, we present a realistic application of SAEs and PERC to unstructured textual data and examine how automated insight extraction could support manual analysis of job descriptions.

### Label-Free Detection of Structural Bias in LLM-Based Recommender Systems via Randomized Paraphrasing: The Case of Verbosity
- arXiv 2611.18878v1 · v1 2026-11-13 19:33 UTC · cs.AI, cs.IR
- Authors: Carlos Peláez-González, David Herrera-Poyatos, Francisco Herrera, Andrés Herrera-Poyatos
- Topics: Brand/product recommendation, Clicks & measurement · score 7 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2611.18878
- arXiv comment: 24 pages, 5 figures
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) are increasingly deployed as recommenders in e-commerce and conversational shopping systems, where they select a product from a set of retrieved candidates described in natural language. Their decisions should depend on relevance to the user query, but may also be influenced by surface-level properties of the descriptions, such as their length. Detecting such structural biases is difficult because relevance labels are rarely available. We propose a label-free framework to audit LLM-based recommender systems for structural bias. Candidate descriptions are rewritten by randomly assigned paraphrasing models and presented in random order. We prove that, if the recommender's choice is invariant to these rewritings, every paraphraser is selected with equal probability, yielding a statistical test that requires no relevance labels. A four-step statistical pipeline tests this property and quantifies the contribution of each description feature while controlling for query-product relevance. We apply the framework to verbosity bias on 20{,}000 product queries and nine recommender LLMs from five model families. After controlling for the measured relevance signals, description length has a positive effect on selection in all nine models, increasing the odds of selection by up to 38% per standard deviation of length. Relevance remains the primary driver of recommendations, while verbosity acts as a consistent secondary signal whose strength depends on the model family. Since the framework needs only black-box access and no annotations, it can be run as a routine audit of deployed shopping assistants, and we provide an auditing protocol with cost and sample-size guidance.

### NI-ACT: A Neural Intent Interface for Brain-Embodied Manipulation
- arXiv 2611.19332v1 · v1 2026-11-14 10:57 UTC · cs.AI
- Authors: Yinghao Li, WeiHsien Lee, Zeyu Zhang, Canyang Zhao et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.19332
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Intracortical brain-computer interfaces can drive robotic arms, but they keep the user inside the fast sensorimotor loop: every approach, correction, and grasp must be neurally specified. Whether intracortical population activity can instead serve as a task-level condition for a learned embodied policy, without symbolic commands or hand-designed skill libraries, remains unknown. NI-ACT addresses this question with a hierarchical brain-embodied framework: a brief motor-cortical signal is read once as a persistent intent, and a visuomotor policy then closes the perception-action loop from vision and proprioception. In a counterfactual grasping task where the scene cannot specify the target, the neural intent alone determined which object the robot grasped; replacing the intent changed the behavior accordingly. Passing the full population latent as a dedicated intent token, rather than a one-hot decoded direction, raised grasp completion from 69% to 81% over 132 held-out scenes, whereas a continuous direction alone did not improve on a one-hot label. Where the signal was read also mattered: in one dual-array session, with the readout window matched, premotor (PMd) intent completed more grasps than primary motor (M1) intent (77% vs. 53%), and the conventional post-cue M1 readout reached 42%. Preparatory activity was itself sufficient: in a center-out task, intent read only from PMd before the go cue (that is, before any movement) drove complete grasps, and in one recording it completed more grasps than the same animal's post-cue readout. These results show that how a neural signal is represented, and where and when it is read, jointly determine how effectively it conveys movement goals to an embodied agent.

### VoiceGuard: An Audio-Native LLM-VLA Pipeline for Wheelchair-Mounted Assistive Manipulation
- arXiv 2611.19984v1 · v1 2026-11-15 12:46 UTC · cs.HC
- Authors: Bang Xiao, Rodolfo Cossovich
- Topics: Manipulation · score 6 · found via cs.HC
- Link: https://arxiv.org/abs/2611.19984
- Full text: data/fulltext/2611.19984.txt

> Wheelchair-mounted robotic arms can help people with limited upper-limb mobility reach and manipulate everyday objects, but operating them typically requires stepwise joystick control and frequent mode switching. Natural-language interfaces could let users express task-level goals, yet they must handle ambiguous requests, distinguish commands from nearby conversation, and support interruption. We present VoiceGuard, a voice interface that separates spoken intent from robot execution through structured request validation and a local stop mechanism. On-device detectors handle the wake phrase and stop commands, an audio-native large language model (LLM) routes each request into a structured function packet, a rule-based ToolDispatcher accepts, rejects, or clarifies the packet, and a SmolVLA vision-language-action (VLA) policy executes accepted tasks on a low-cost SO-101 arm. Preliminary tests showed that the system correctly handled 55 of 60 voice commands, including ambiguous and non-directed utterances, completed 16 of 20 deliveries, and stopped the arm on all 20 stop commands with a median latency of 210 ms. We demonstrate the feasibility of combining flexible spoken input with constrained task execution and local interruption for wheelchair-mounted assistive manipulation.

### Can AI Judge You? An Empirical Audit of Deployment Readiness in LLM-assisted Hiring Systems
- arXiv 2611.20140v1 · v1 2026-11-15 17:16 UTC · cs.AI, cs.CL, cs.CY
- Authors: Spandan Roy, Subhabrata Majumdar, Soudeep Deb
- Topics: Clicks & measurement · score 6 · found via cs.AI, cs.CL, cs.CY
- Link: https://arxiv.org/abs/2611.20140
- arXiv comment: 46 pages, 11 figures
- Full text: data/fulltext/2611.20140.txt

> Delegating resume screening to large language models (LLMs) requires organizations to establish whether they can distinguish candidates by relevant qualifications while allowing only authorized users to change screening rules or approve exceptions. To this end, we develop a system architecture that separates candidate evidence, evaluation, permission controls, and assessment record, and empirically examine two complementary dimensions of its deployment readiness. First, we assess its operational readiness on four LLMs using a controlled experiment on 210 resumes across 14 job roles and six decision interfaces. Second, we assess its compliance readiness by testing how it handles unauthorized user requests and instructions embedded in resumes. We find that operational performance depends on the choice of evaluation interface: scalar scores generally distinguish qualification changes better than simple pass/fail judgments, while comparative judgments are sensitive to presentation order. Explicit permission rules and separation of resume content from instructions reduce unauthorized compliance, to a varying degree of effectiveness across LLMs and usage contexts. Finally, we find that LLM evaluators often diverge between their decisions and offered justifications. Going beyond simply evaluating LLMs for hiring tasks, our framework supports an audit of a fully configured resume evaluation system to enable its deployment decision.

### AsymEEF: Bimanual Manipulation with Asymmetric End Effectors
- arXiv 2611.20557v1 · v1 2026-11-16 05:36 UTC · cs.RO, cs.AI, cs.CV, cs.LG
- Authors: Xiaokang Sun, Ningyue Wang, Kunqi Xu, Guangqi Jiang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.20557
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Teleoperated demonstrations are costly to collect and rarely reusable across end-effectors with different kinematics and action spaces. This burden grows in bimanual manipulation, where each end-effector pair may require new data. We present AsymEEF, a framework for executable cross-end-effector demonstration generation and unified bimanual policy learning. Given a small source dataset, AsymEEF transfers demonstrations to heterogeneous combinations of two-, three-, and five-fingered end-effectors without additional teleoperation. Kinematic teacher anchors provide geometric supervision, while sparse real-world X-Calib anchors correct discrepancies in grasp execution. A shared encoder maps wrist poses and actuator states to a morphology-agnostic latent space, and a morphology-conditioned decoder reconstructs target commands. Generated trajectories undergo replay filtering for task-level executability. The representation also supports a unified bimanual visuomotor policy trained across multiple pairs. Across four simulated and six real-world tasks, AsymEEF improves replay success over adapted transfer baselines, achieves a mean replay-valid expansion gain of 16.6 times in simulation, and is evaluated through downstream policy training on real robots. Project website: https://asymeef.vercel.app/.

### Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models
- arXiv 2611.20901v1 · v1 2026-11-16 11:10 UTC · cs.AI, cs.CY
- Authors: Mika Facchini
- Topics: Clicks & measurement · score 6 · found via cs.AI, cs.CY
- Link: https://arxiv.org/abs/2611.20901
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Organizations increasingly use large language models (LLMs) for decisions about people, such as hiring, investment and employee evaluation, and rely on them over long periods of time. Fairness audits of such systems, however, are conducted only once. We examine how the biases of LLMs change over time. In a venture screening setting, models from five providers decided whether and how much to invest in startups whose founders differed only in gender, origin and university. We repeated this audit three times over 13 months (248,400 API calls). Study 1 shows that the same model, called under the same identifier one year later, displayed a significantly different bias pattern. Study 2 shows that the successors of retired models carried the same bias as their predecessors, but in a significantly different size and form. Study 3 shows that the bias does not depend on the industry of the startup. A document analysis further shows that providers change and retire models at their discretion, with notice periods of zero to six months. Drawing on these findings, we develop a theory of evidence anchoring. We theorize that bias resides in the model class and persists, whereas audit evidence is anchored to a single model and expires when the provider decides. We derive policy advice for organizations and regulators, namely audits of model classes instead of single models, a version record for every model response, and re-audits triggered by model changes.

### Language-model agents' beliefs can be manipulated via truthful evidence in open channel
- arXiv 2611.21235v1 · v1 2026-11-16 15:20 UTC · cs.AI, cs.CL, cs.MA, cs.SI
- Authors: Jinwei Hu, Qisong He, Xinmiao Huang, Youcheng Sun et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CL, cs.SI
- Link: https://arxiv.org/abs/2611.21235
- arXiv comment: Under Review
- Full text: data/fulltext/2611.21235.txt

> Language-model agents' beliefs can be manipulated through open channels such as social media, even when the information they receive is truthful. When agents fill gaps between fragments with self-induced relationships, they may accept those relationships as established facts and pass the resulting rumours to others. Drawing on cognitive theory of narrative understanding and film theory of montage, we introduce Generative Montage to operationalize this failure, termed narrative overfitting, by coordinating agents to arrange truthful fragments into misleading narratives. Across 1,090 rumour targets from six Twitter events, agents often accepted rumours overconfidently, with overall acceptance exceeding 65 percent in twelve of fourteen models. Acceptance remained above 50 percent after majority voting or review of the same evidence, showing how errors can reach downstream decisions. To explain this susceptibility, fragment interventions identify posts that influence belief within complete narratives. Synthetic controls then show that similar response patterns arise from valid evidence, separating belief influence from evidential support. This distinction motivates Grounded Monitor, a proof-of-concept neuro-symbolic runtime monitor that checks direct evidential support to guide agents' judgements, improving decision accuracy by 5.6 to 29.0 percentage points across original and anonymized settings. These findings expose a cognitive route to rumour amplification and support monitoring inferred relationships before agent-generated conclusions guide public decisions.

### Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models
- arXiv 2611.21517v1 · v1 2026-11-16 18:10 UTC · cs.RO, cs.AI
- Authors: Itamar Mishani, Mukund Krishnakumar, Oren Salzman, Maxim Likhachev
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.21517
- arXiv comment: Under review
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Long-horizon manipulation tasks require a robot to perform a sequence of physical interactions with its environment, typically combining several different skills. Planning such behaviors efficiently is challenging: given a library of parameterized skills, solutions lie in a vast hybrid space of skill sequences and their parameters, and evaluating each candidate skill's feasibility and effect with a high-fidelity world model such as a physics simulator is computationally expensive. MOSAIC, a recent skill-centric approach, lets the skills guide a non-sequential search toward the regions of this space where they are likely to succeed; however, it pays the full cost of simulation for every parameterized skill it considers. In this work, we introduce Lazy-MOSAIC, a lazy planning framework that instead searches over hypothesized skill outcomes. A cheap learned skill-effect world model predicts, in a fraction of a millisecond, a skill's feasibility and the world state it produces. Lazy-MOSAIC then uses these predictions to focus expensive simulation on promising candidate skills and, when a hypothesis is invalidated, repairs only the affected part of the search, while ensuring that every skill in a returned plan is validated in simulation. We evaluate Lazy-MOSAIC on cluttered-shelf retrieval tasks of increasing difficulty and demonstrate it on a physical robot, showing that it plans substantially faster than baselines with fewer simulator queries, while matching or exceeding their success rate in every setting. Visit skill-mosaic.github.io.

### Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web
- arXiv 2611.19900v1 · v1 2026-11-15 09:29 UTC · cs.CL, cs.IR
- Authors: Bakary Gibba, Muhammad Abba Mandara, Karim Ismail Abd-Ellah Mohamed
- Topics: Citation & source selection, RAG (generic) · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.19900
- arXiv comment: 8 pages, 3 figures, 4 tables
- Full text: data/fulltext/2611.19900.txt

> Retrieval-augmented systems that research companies are judged by how much they find, yet in markets where public evidence is sparse, a confident answer without support costs more than no answer. We introduce AfriBizClaims, a benchmark of 150 company-research queries across six African markets in English, French and Portuguese, including queries about fictitious companies that a correct system must decline. Each claim a system makes is judged against the page it cites by an AI judge, checked against a second AI judge from another model family and against two human annotators, and abstentions are scored against answerability labels. We compare BM25 over a pooled corpus, standard web retrieval-augmented generation, and a multi-step agent pipeline (Konexium V1), all using the same language model. The two simple baselines are well attributed: 98% of their judged claims are supported by the page they cite, and they decline every field of every fictitious company. Counting claims about a company other than the one asked about as errors, the agent pipeline's per-query precision is 68%, and it never answers a question about a named company correctly: it substitutes other firms, including for 5 of the 24 fictitious names, and it is the least stable between runs and the most expensive. In the pipeline we evaluated, more steps between the query and the evidence did not buy more grounded answers. We will release the queries, system outputs, labels and short evidence excerpts.

### TokenFormer V2: Breaking the Resolution-Complexity Dilemma in Unified Recommendation
- arXiv 2611.19074v1 · v1 2026-11-14 01:24 UTC · cs.IR, cs.LG
- Authors: Kaihui Wu, Guoming Li, Liang Guo, Yifeng Zhou et al.
- Topics: Ads · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.19074
- arXiv comment: Technical Preprint. 12 pages, 5 figures

> Industrial recommendation faces a resolution--complexity dilemma: dense interactions make detailed modeling of long behavior histories expensive, while compact history summaries restrict the evidence available to prediction. A unified backbone must preserve rich behavioral details within strict serving budgets. We introduce \textbf{TokenFormer V2}, a unified architecture that explicitly decouples \emph{representation resolution} from \emph{interaction density}. Its group-wise token layout jointly encodes behavior segments with non-sequential context, expands interaction ranges via hierarchical group merging, and coordinates distributed groups through \emph{NS Fusion} and \emph{Global Sync} modules. Through this \emph{local--global decomposition} paradigm, computation is concentrated on structured interactions while preserving fine-grained evidence, ensuring that every encoded event remains directly accessible to the \emph{Full-Resolution Readout} module. On the Tencent Advertising Algorithm Competition 2026 (TAAC 2026) benchmark, TokenFormer V2 achieves top-ranking accuracy among unified recommendation baselines while using \textbf{5.1$\times$ fewer FLOPs} than leading baselines, sustaining its advantage across long histories and imbalanced behavior domains. Furthermore, in billion-parameter evaluations on WeChat Channels advertising, it consistently outperforms state-of-the-art industrial baselines, yielding up to a \textbf{+0.07 pp} overall AUC gain. In live online A/B testing against the production model, TokenFormer V2 delivers a statistically significant \textbf{2.33\% increase in GMV}. These results establish TokenFormer V2 as a battle-tested blueprint for scalable, full-resolution behavior modeling in industrial recommendation.

### CLEAR: Legible and Steerable Recommendation via Grounded Natural-Language Interests
- arXiv 2611.19110v1 · v1 2026-11-14 02:44 UTC · cs.AI, cs.IR
- Authors: Qi Guo, Reza Mirghaderi, Iordanis Fostiropoulos, David Fan et al.
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.19110
- arXiv comment: 18 pages, 6 figures

> Modern recommenders keep learned preferences in representations people cannot inspect or change. We present CLEAR (Controllable and Legible End-to-end Architecture for Recommendation), an end-to-end system deployed at Meta and built around an editable natural-language interest layer. CLEAR makes a ranked subset of inferred interests readable and stores accepted additions and suppressions as authoritative preference state. Behavioral grounding maps each inferred interest back to supporting events in the user's own history. The resulting interest object is also a serving address: its label and profile-conditioned rewrites drive lexical retrieval, its supporting events seed behavioral retrieval, its projection queries an embedding index, and its stable identity supports ranking, attribution, and exposure control. A fresh user declaration may precede behavioral support, so it enters through the same serving identity and initially draws candidates from topical retrieval. Ranking makes those candidates competitive, while a delivery controller observes attributable exposure and replenishes underexposed interests. Direct user review found that users rated about 88.5% of displayed interests accurate. In an offline benchmark using a shared evaluation protocol, the Specialized 3B generator reached 0.3967 mean-user F1@10, compared with 0.3633 for Gemini 2.5 Pro and 0.1911 for the prior generator. For a newly declared interest, a user-randomized cumulative ablation measured same-day delivery losses of 8.7 percentage points for added-interest ranking terms, 11.1 for reserved top-slot insertion, and 13.7 for interest-conditioned candidate sourcing, conditional on the tested removal sequence. CLEAR components have operated in production for over one year; the system spans four surfaces on Instagram and Facebook, with an interest layer people can inspect, correct, and use to direct recommendations.

### Reflection Is Not Always Worth It: Budgeted Reflection Allocation for Recommendation Agents
- arXiv 2611.19847v1 · v1 2026-11-15 07:11 UTC · cs.IR
- Authors: Jinfeng Xu, Zheyu Chen, Ziyue Peng, Jianheng Tang et al.
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.19847
- arXiv comment: Accepted by WSDM 2027

> This work aims to make recommendation agents more efficient by reducing unnecessary LLM reflection while preserving full-catalog ranking and inference reranking. Since BRAVE changes only how training-time reflection is allocated, it does not introduce new user data requirements or additional LLM exposure beyond the base agent protocol. The main potential risk is that a poorly calibrated allocator may assign less reflection to users whose preferences are sparse, niche, or under-represented, which could weaken personalization for those users or indirectly affect item exposure. This risk can be mitigated through deployment-time auditing and conservative allocation design. In practice, reflection budgets should be evaluated not only by aggregate Recall or NDCG, but also across user-history lengths, item popularity groups, and application-relevant cohorts when such analysis is permitted. The allocator should rely on task-side ranking evidence rather than sensitive attributes, and fallback policies can reserve a small portion of the budget for random or fairness-aware coverage when subgroup robustness is important. Privacy risks can be controlled with the same protections required by the base recommendation agent: minimizing user text sent to the LLM controller, anonymizing user identifiers, retaining only necessary interaction evidence, and applying standard access-control and logging policies. Overall, BRAVE is designed as a cost-aware allocation layer, and its ethical deployment depends on validating that the saved computation does not come at the expense of vulnerable users or responsible exposure.

### How did data sharing evolve in the decade since the FAIR Principles?
- arXiv 2611.20319v1 · v1 2026-11-15 23:29 UTC · cs.IR, cs.DL
- Authors: Sheeba Samuel, Daniel Mietchen
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.20319
- Full text: data/fulltext/2611.20319.txt

> A decade after the publication of the FAIR Guiding Principles, what have we learned about data sharing, and what do data availability statements (DAS) and other materials accrued over that period tell us about how data-sharing practices, attitudes, and infrastructures evolved? Here, we present a large-scale longitudinal analysis of over 6.8 million biomedical articles from the PMC Open Access Subset, spanning 2011 to 2025. Using an automated pipeline, we extracted and classified DAS, repository links, accession numbers, and supplementary materials, assigning each article a data-sharing score and independently FAIR-assessing a subset of cited dataset URLs. We find that explicit DAS adoption rose from ~2% in 2011 to 68% in 2025, while "available on request" statements grew in parallel from near zero to over 19%. The corpus growth amplifies both patterns: articles with a DAS containing an explicit repository mention rose from 132 in 2011 to 94,697 in 2025, while "available on request" articles rose from 77 to 173,474 over this span. Structural biology and genomics consistently achieved the highest data-sharing scores, while clinical research and public health ranked lowest. Gold Open Access journals showed a small advantage over subscription journals, while Diamond Open Access journals outperformed both. Internationally collaborative articles scored higher than domestic ones. A gender gap emerged: female first-authored articles' scores declined more than male first-authored ones. The analysis further covered additional dimensions, from compliance with funder/journal mandates and JATS XML tagging standards to computational reproducibility signals and the co-occurrence of DAS with ethics statements. A decade on, the gap between declaring data availability and actually sharing machine-readable, reusable data persists across fields, infrastructures and demographics.

### Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First
- arXiv 2611.20378v1 · v1 2026-11-16 01:10 UTC · cs.IR, cs.CY, cs.HC
- Authors: Michael Iannelli, Alan Ai
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.20378
- arXiv comment: 5 pages, 3 figures
- Full text: data/fulltext/2611.20378.txt

> When people ask an AI assistant what to buy, what happens next at the store? We link the same people's assistant conversations to their later browsing at twenty large online retailers. People go to the product the assistant named: among shoppers who had not visited the store in the past week, visits to the named product within a day rise from 0.02 to 2.07 per 100 answers (+2.0 points [1.7, 2.4]), and on days with a product-page visit at the store, 44% show a product from their own answer, against 1.5% for a matched answer given to someone else. The result replicates in a separate five-month period. Few arrive through the assistant's link: 89% of visits carry no sign of it, and 54% follow a web search, the same share as their usual visits. When a search comes just before the first visit, it names the answer's product 28% of the time (1% in earlier weeks), as if the search box were an address bar. The chat names the product; the store logs a search. Once there, shoppers keep browsing. We propose product follow-through, the share of answers followed by a visit to the product they named, as a way to evaluate shopping assistants and agents by what people do next: it needs no referral data or provider logs and can be computed for each assistant.

### What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially Private Item Counts
- arXiv 2611.20388v1 · v1 2026-11-16 01:32 UTC · cs.IR
- Authors: Chang Xu, Hao Wang, Gedi Zhou
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.20388
- arXiv comment: 10 pages, 4 figures. Accepted for publication in the Privacy and Security of Big Data special session at IEEE BigData 2026. Code available at https://github.com/AnthonyXu109/psbd26-artifact
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Privacy controls can prevent an evaluator from linking purchases to the recommendations users received, while a merchant can still release complete item-level purchase counts for the evaluation cohort. We ask when these counts identify which recommender performs better. The counts constrain who could have bought each item. We bound the performance difference over all assignments consistent with the counts. A reduced transportation network handles full catalogs and can certify attainable endpoints. If the interval excludes zero, it identifies the better recommender for that cohort. With differentially private counts, one confidence guarantee applies jointly to all comparisons from the same release. In two e-commerce cohorts of about 20,000 and 100,000 users, exact counts narrowed every interval compared with bounds that ignored the counts. Most decisions involved a recommender that favors popular items. For NDCG@10, which rewards ranking purchased items higher, each setting combined one of three personalized pairs with a pattern and rate of missing links. Exact counts settled 14 of 168 settings in the smaller cohort and none of 81 in the larger cohort. In the smaller cohort, exact counts broken down by user group settled two personalized pairs when 90% of users remained linked, at the cost of revealing more about individual purchases. Whole-cohort private releases with one count per item retained much of the narrowing but settled no personalized pair in either cohort. Grouping less popular items into bins let private counts settle one personalized pair in the smaller cohort.

### Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates
- arXiv 2611.20837v1 · v1 2026-11-16 10:16 UTC · cs.IR, cs.AI
- Authors: Yuchong Hu, Zhao Zhang, Ziyao Zhao, Haoyu Wang et al.
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.20837
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> When several candidates have graph support, does it matter which candidate receives which supporter and path counts? We study how LLM rankers use collaborative evidence on Amazon Books and MovieTV. Swapping user-level evidence degrades ranking, while matched item substitutions have little effect. On fixed clean-trained checkpoints, unrelated catalog text lowers Hit@1 from 44.77% to 38.70%, with 99.9% of rankings still valid. Across all three paired seeds, the NDCG@5 difference between count and path prompts was larger after count training than after path training. Degree matching preserves target paths while giving more rivals support. Across the full degree-matched development pools, adding candidate-level graph records to history improves NDCG@5 by 2.28 points on Books and 2.54 on MovieTV. When the target and a rival both have support, path- and count-trained rankers benefit from retaining counts. On these development queries, adding counts numerically to history scores outperforms presenting them as text. For count-trained rankers, exchanging intact count pairs among supported candidates preserves support and token length, yet lowers NDCG@5 by 4.06 points on 141 Books queries and 3.26 on 104 MovieTV queries. A frozen evaluation on 274 previously unused Books users with supported targets and rivals confirms the attribution effect: correct assignment improves pairwise accuracy by 6.07 percentage points (95% CI [4.18, 8.00]).

### When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents
- arXiv 2611.21577v1 · v1 2026-11-16 18:49 UTC · cs.CR, cs.AI
- Authors: Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani
- Topics: Ads · score 4 · found via search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.21577

> Large language model (LLM) applications increasingly act as agents that select and invoke external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing clients to compose tools advertised by multiple servers. However, tool metadata used for discovery and selection is not, by itself, necessarily bound to a verified provider identity. This paper studies this gap as tool-provider misbinding: a failure in which a request intended for a legitimate provider is instead resolved to an attacker-controlled tool. The attacker does not compromise the host, LLM, legitimate server, or network channel; it only operates another MCP server that advertises tools with chosen metadata. We formulate tool provider misbinding as an attacker-controlled tool-selection optimization problem and evaluate it in a controlled MCP environment across five LLM-based clients. The results show that interactions drive misbinding. The strongest failures occur when exact-name collision, task-aligned description, and compatible schema reinforce one another, but authority-enhanced descriptions with compatible schema can also cause wrong-provider execution or unresolved provider ambiguity without name collision. Different models expose the same provider-binding weakness differently, including attacker-controlled provider selection, clarification requests, and unstable or inconsistent provider resolution.

## Other new cs.IR papers, title only (20)
- LMEG-Doc: Layout-Grounded Multi-View Evidence Graphs for Multimodal Long-Document Retrieval — https://arxiv.org/abs/2611.18901
- Knowledge-Guided Local-to-Global Anomaly Learning for Longitudinal Medication Trajectories — https://arxiv.org/abs/2611.19106
- LABEL: Literature Asymmetry between Efficacy and Limits in Drug Knowledge and Language Models — https://arxiv.org/abs/2611.19166
- Revisiting What Makes a Good Context Subset: A Sparse Latent Basis Perspective — https://arxiv.org/abs/2611.19220
- Keep it Simple! A Multiple-Choice Task can Benefit Generative Recommendation — https://arxiv.org/abs/2611.19320
- StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix — https://arxiv.org/abs/2611.19752
- Exact Sparse Assignment with Costly Target Embeddings: Fixed-Realization Certificates and an Empirical Audit — https://arxiv.org/abs/2611.19770
- NoLBERT-Calls: Reading Earnings Calls Without Hindsight — https://arxiv.org/abs/2611.19849
- A Demonstration System for Faithful Temporal Question Answering — https://arxiv.org/abs/2611.19926
- Take a Step Back: A Dual-Granularity Raw Feature Empowered Intermediate Fusion Graph Convolutional Network for Multimodal Recommendation — https://arxiv.org/abs/2611.19974
- Overview of the Plagiarism Detection Task at PAN 2026 — https://arxiv.org/abs/2611.20443
- MAGE: Meta-path Adaptive Graph Evidence for Transferable Multimodal Graph Learning — https://arxiv.org/abs/2611.20449
- When the Bill Falls: Reusing the Old Index Defers,Never Avoids, Re-encoding in Complete Embedding-Model Migration — https://arxiv.org/abs/2611.20702
- CARE: Contrastive-Anchored Residual Encoding with Listwise Reconstruction for Retrieval-Oriented Semantic IDs — https://arxiv.org/abs/2611.20721
- UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval — https://arxiv.org/abs/2611.20758
- Living Context Graphs: Continual Semantic Learning for Enterprise Data Reasoning — https://arxiv.org/abs/2611.20976
- Adaptive-Elbow Graph Traversal for Schema Retrieval in Text-to-SQL — https://arxiv.org/abs/2611.20979
- EE-Motion: An EEG-based Web Architecture for Live Affective Music Recommendation — https://arxiv.org/abs/2611.21032
- Leveraging Binary Hashing for Scalable Index Assignment in Semantic Communications — https://arxiv.org/abs/2611.21260
- ExRel: Learning Directed Reuse Relevance between Rich-Text K-12 Question Images with Executable Relation Contracts — https://arxiv.org/abs/2611.21461

## Already listed on an earlier day, still inside the look-back window (39)
- Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents — https://arxiv.org/abs/2611.16744 (score 14)
- From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research — https://arxiv.org/abs/2611.17041 (score 14)
- Beyond Bot Labels: Retrospective Consequence-Grounded Ranking of Attributed Cache Harm in E-Commerce Logs — https://arxiv.org/abs/2611.18027 (score 12)
- Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation — https://arxiv.org/abs/2611.17161 (score 10)
- Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent — https://arxiv.org/abs/2611.17939 (score 10)
- AI-Voyager: A Public-Interest System for Human-AI Civic Reasoning to Contest and Shape the Rules That Govern AI — https://arxiv.org/abs/2611.17564 (score 9)
- DOCKET: A Pluralistic Benchmark for Evaluating AI-Assisted Policy Feedback in U.S. Rulemaking — https://arxiv.org/abs/2611.17914 (score 9)
- Towards Explainable Sleep Stage Classification using Single-Channel Electroencephalogram — https://arxiv.org/abs/2611.18434 (score 9)
- MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection — https://arxiv.org/abs/2611.16693 (score 8)
- Sketching Language Models for Context Attribution — https://arxiv.org/abs/2611.17313 (score 8)
- Evaluating the Robustness of PRNU Source-Camera Attribution to the Fingerprint-Copy Attack: An Open Toolkit with Triangle-Test Detection — https://arxiv.org/abs/2611.17747 (score 8)
- Creative Product Design under Brand Image Constraints — https://arxiv.org/abs/2611.17762 (score 8)
- G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands — https://arxiv.org/abs/2611.17814 (score 8)
- WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents — https://arxiv.org/abs/2611.17955 (score 8)
- From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States — https://arxiv.org/abs/2611.18272 (score 8)
- RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG — https://arxiv.org/abs/2611.17788 (score 7)
- Interactive deep-learning based interface for brain tumour segmentation — https://arxiv.org/abs/2611.17983 (score 7)
- Contagious Fingerprints: When LLMs Inherit Another Model's Identity — https://arxiv.org/abs/2611.18104 (score 7)
- SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection — https://arxiv.org/abs/2611.07222 (score 6)
- HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation — https://arxiv.org/abs/2611.16439 (score 6)
- EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming — https://arxiv.org/abs/2611.16728 (score 6)
- A Code-Level Audit of X — https://arxiv.org/abs/2611.16800 (score 6)
- An In-Silico Audit of Topographic Organization in a Multimodal Brain-Response Model — https://arxiv.org/abs/2611.18105 (score 6)
- Toward On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset: A Preliminary Study — https://arxiv.org/abs/2611.18438 (score 6)
- Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination — https://arxiv.org/abs/2611.18514 (score 6)
- Advancing Quantization for R&R Models with Microscaling Formats — https://arxiv.org/abs/2611.17501 (score 4)
- StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval — https://arxiv.org/abs/2611.18516 (score 4)
