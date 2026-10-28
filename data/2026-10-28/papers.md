# Paper candidates — 2026-10-28 (IST)

Generated 2026-10-28 05:40 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 35 new topic matches · 54 other new cs.IR · 0 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (35), highest score first

### Useful Diversity or Hallucinated Variety? Persona-Conditioned Synthetic Query Generation for E-Commerce Search
- arXiv 2610.35102v1 · v1 2026-10-26 09:43 UTC · cs.CL, cs.IR
- Authors: Filippos Ventirozos, Tom Armitage, Mahmoud Oshagh, Peter A. Appleby et al.
- Topics: RAG (generic), Query fan-out, Brand/product recommendation · score 20 · found via cs.CL, cs.IR
- Link: https://arxiv.org/abs/2610.35102
- arXiv comment: Accepted at IJCNLP-AACL 2026 (Findings). 20 pages, 2 figures, 16 tables
- Full text: data/fulltext/2610.35102.txt

> Synthetic supervision can bootstrap semantic parsers in new search domains, but prompt-induced diversity is useful only when generations are faithful to the structured intent. We explore this for cold-start e-commerce search: 118,098 synthetic pairs produced by 6 LLMs with 9 persona-conditioned prompt families on a 47-field UK automotive schema, against 1,214 human-annotated and 15,304 production queries. We show that the IPIP personality bundle improves parser F1 in all four matched contrasts (Holm-corrected $p<.001$), and all three bundles have a positive main effect over the complete $2^3$ grid. Syntax conditioning is the axis that moves generations towards real traffic. It also induces lexical diversity. Alignment sKL, the divergence between von Mises-Fisher distributions fitted to synthetic and human-annotated queries, is an unlabelled proxy for parser F1 ($ρ=-0.917$ against human queries written for simulated shopper scenarios, lower is closer). An LLM committee, checked against a blinded author pass, triages the 927 queries missed by every parser and labels 37% as hallucinated. Dropped constraints dominate. The four syntax-bearing families have the largest hallucinated shares, 38 to 42%, while IPIP alone has the lowest at 28%.

### Quantifying Claim Smoothing by LLM Research Agents
- arXiv 2610.35793v1 · v1 2026-10-26 17:29 UTC · cs.CL
- Authors: Tiasa Singha Roy, Manya Wadhwa, Greg Durrett
- Topics: Citation & source selection, Query fan-out · score 14 · found via cs.CL
- Link: https://arxiv.org/abs/2610.35793
- arXiv comment: Code and data present at: https://github.com/tiasa2/SmoothScore
- Full text: data/fulltext/2610.35793.txt

> Deep research, or any use of large language models (LLMs) to read a large document collection and produce insights, requires synthesizing information from different sources. In this work, we find that LLMs produce long-form research reports that read as confident syntheses but which fail to accurately reflect the underlying documents. We call this failure smoothing. In collapsing diverse and potentially conflicting sources into a single narrative, the model discards the evidential "jaggedness" of its corpus and asserts conclusions more decisive than the citations can support. We introduce a claim level scoring pipeline, SmoothScore, to quantify this effect. Our pipeline extracts key conclusive claims from model generated reports, then finds evidence relevant to each claim and clusters that evidence along high level aspects. Finally, each claim is scored with respect to the evidence to quantify the degree of smoothing done by the agent. Across 7 systems and 4 datasets, we find that agents consistently produce stronger claims than warranted.

### When Connectivity Misleads: Guiding Agentic Search with Contrastive Evidence Paths
- arXiv 2610.36134v1 · v1 2026-10-26 18:45 UTC · cs.AI, cs.IR
- Authors: Junchen Li, Liang Xu, Rongzheng Wang, Qizhi Chen et al.
- Topics: Query fan-out, Agents · score 14 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2610.36134
- Full text: data/fulltext/2610.36134.txt

> Search agents can use cross-document graphs to discover sources through multi-hop connections and choose subsequent actions based on candidate rankings and relationships within a limited observation window. However, documents may rank highly because their numerous connections make them easier to reach, without necessarily providing more valuable evidence. Graph diffusion methods such as Personalized PageRank (PPR) aggregate propagation contributions from multiple sources, allowing highly connected distractor nodes to crowd the observation window. Flat node scores also obscure cross-document evidence trails, limiting continued exploration. We propose Contrastive Evidence Paths (CEP), which scores candidates by their strongest individual paths on a query-conditioned document graph and calibrates these scores against the same graph's background visitation distribution to mitigate structural bias. CEP ranks candidates by the calibrated scores and retains the corresponding source paths. Building on CEP, we develop Structured Corpus Interaction (SCI), which organizes candidates and their connecting paths into a structured Map, enabling agents to verify source documents and pursue missing information through expansion from anchor documents. Experiments on BrowseComp-Plus and TREC-COVID show that SCI achieves state-of-the-art answer accuracy and nDCG@10 with the lowest generation cost. Compared with the strongest baselines by task performance, maximum reductions in tool calls and total generation costs exceed 50% and 40%, respectively. Further analysis confirms that SCI with CEP suppresses ranking inflation induced by structural connections and improves gold recall and exploration efficiency.

### Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure
- arXiv 2610.36453v1 · v1 2026-10-27 00:59 UTC · cs.AI
- Authors: Nardine Basta, Venus Haghighi, Dali Kaafar, Amin Beheshti
- Topics: Citation & source selection, Brand/product recommendation, Manipulation · score 14 · found via cs.AI
- Link: https://arxiv.org/abs/2610.36453
- arXiv comment: 20 pages, 7 figures, 11 tables. 8-page main paper with supplementary material included as an appendix. Under review
- Full text: data/fulltext/2610.36453.txt

> LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users, yet it remains unclear whether they distinguish correction from manipulation or merely differ in their propensity to concede. We examine this question across seven LLMs from four vendors in two studies, one on the answers agents give and one on the actions they take as customer-support agents whose policy permits account changes only for verified users. Simulated users push toward correct and incorrect answers with graded pressure. Following research on epistemic vigilance, the pressure either appeals to the source, such as claimed authority, or offers content the agent cannot verify, namely a cited source. Drawing on signal detection theory, we measure on a set of benchmark questions how much more readily each agent concedes to correction than to manipulation, separately from its overall propensity to concede. Citations made five of seven models readier to concede and four worse at discriminating, while stronger wording added little. In the agentic study, five models never violated the verification policy, including models that readily abandoned correct answers, so concession on answers did not predict violations of policy. Ministral 3B violated the policy mainly under claimed authority, and Ministral 8B reported changes it had not made. An instruction to revise only on verifiable evidence chiefly shifted propensity to concede rather than improving discrimination. Concession rates alone are therefore misleading, and agents should be evaluated on both their discrimination and the actions they take.

### TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge
- arXiv 2610.37231v1 · v1 2026-10-27 13:38 UTC · cs.IR
- Authors: Zhiheng Fu, Yupeng Hu, Zixu Li, Zhiwei Chen et al.
- Topics: Query fan-out, Brand/product recommendation · score 13 · found via cs.IR
- Link: https://arxiv.org/abs/2610.37231
- arXiv comment: Technical Report on the First-Place Solution for eCommerce Challenge @ SIGIR 2026 eCom Workshop
- Full text: data/fulltext/2610.37231.txt

> The SIGIR 2026 eCommerce Challenge Query Reformulation Task evaluates the reformulation of task-oriented queries into expressions suitable for product retrieval, followed by BM25-based retrieval. These queries often imply product needs through activity-level semantics, creating a lexical gap with catalog descriptions. Systems must preserve task intent while adapting the number of reformulations to the Automatic and Interactive protocols. We propose TaskBridge, a catalog-anchored framework comprising Catalog Semantic Anchoring, Unified Five-Candidate Rewriting, and Protocol-Aware Selection. It grounds queries in catalog vocabulary, generates five complementary reformulations, and selects one query for Automatic retrieval or up to four for Interactive retrieval using BM25 scores, query-product reranking, and weighted Jaccard overlap. The selected queries are independently executed using BM25 to produce results in the required six-column format. Experiments demonstrate improved retrieval effectiveness, with multiple complementary queries providing additional gains in the Interactive setting. TaskBridge achieved first place in the SIGIR 2026 eCommerce Challenge.

### AdShot: Benchmarking Multimodal Large Language Models for Video Advertisement Clipping
- arXiv 2610.33377v1 · v1 2026-10-24 00:14 UTC · cs.MM, cs.CV
- Authors: Wen Xie, Om Rastogi, Sai Siddhartha Vivek Dhir Rangoju, Gijs Overgoor et al.
- Topics: Brand/product recommendation, Ads · score 12 · found via search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2610.33377
- Full text: data/fulltext/2610.33377.txt

> Advertisers routinely create multiple duration variants of ads to meet marketing budgets and viewer preferences, a labor-intensive and costly process. While multimodal large language models (MLLMs) excel at general video understanding, their ability to perform specialized editorial tasks remains unexplored. We introduce AdShot, a benchmark for evaluating MLLMs on shot selection for ad clipping. It contains 823 professionally edited ad pairs (30-sec sources and 15-sec edits) across 194 brands and 17 industries, annotated with shot-level boundaries and content features (action, emotion, information, imagery). We evaluate 13 state-of-the-art video-only MLLMs and 2 audio-visual MLLMs (7B-72B parameters) on shot selection accuracy (Precision, Recall, F1), duration constraints (15s), and content preservation, including an audio ablation. We find: (1) model architecture matters more than scale, with smaller models often matching or exceeding larger ones; performance is strongest for target ads with 6-10 shots; (2) models exhibit a mean absolute duration error of 5.39s, with most tending to overshoot the 15s target, though they can still substantially reduce human editing effort; (3) all models exhibit systematic content biases, favoring information-rich and emotion-focused shots while under-selecting action and imagery. We publicly release our benchmark to facilitate research at the intersection of multimodal AI and computational advertising.

### Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation
- arXiv 2610.34294v1 · v1 2026-10-25 13:50 UTC · cs.CL, cs.CR, cs.IR
- Authors: Puyuan Yang, Shaoxuan Dong, Liujie Wu, Xiaochun Cheng et al.
- Topics: RAG (generic), Brand/product recommendation, Manipulation · score 12 · found via cs.CL, cs.CR, cs.IR
- Link: https://arxiv.org/abs/2610.34294
- arXiv comment: 29 pages, 4 figures, 20 tables
- Full text: data/fulltext/2610.34294.txt

> The stance expressed in responses from retrieval-augmented generation systems is significantly influenced by the stance distribution of the retrieved materials. Existing research on knowledge poisoning has primarily targeted factual errors. In contrast, this study focuses on injection attacks in which the facts are correct but the stance on a controversial issue is one-sided. At a mean topic-level poisoning share of 18.9% within the post-injection ProCon documents, all four generation models from different vendors exhibited stance shifts aligned with the poisoning direction; across four concentration levels, the shifts increased monotonically. This paper proposes a Stance-Balancing Middleware positioned between the retriever and the generator. It consists of stance detection, fixed balancing (2 supporting + 2 opposing + 1 neutral), and a debiasing prompt, without introducing additional large language model calls. Across all eight concentration-direction settings, the complete method reduced the magnitude of stance deviation by an estimated 0.106 to 0.350; the six settings at poisoning shares of 11.9%-18.9% remained significant after Holm adjustment (adjusted p <= 0.009). In the cross-model experiment, all eight model-direction combinations moved along the stance axis in the corrective direction, and seven of eight showed a clearly detected reduction in absolute distance from 0. In the concentration sweep, the post-defense intervals included 0 in all eight settings, while the cross-model pro-poisoning results retained small positive residual point estimates of +0.045 to +0.063. For 20 candidate documents, stance detection took approximately 1.5% of the median generation time on a single GPU and approximately 16% on CPU.

### Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization
- arXiv 2610.34829v1 · v1 2026-10-26 04:23 UTC · cs.AI
- Authors: Hangyi Zhao, Bonan Zhang, Fusen Guo, Jiaheng Wei et al.
- Topics: Citation & source selection, RAG (generic), Manipulation · score 12 · found via cs.AI
- Link: https://arxiv.org/abs/2610.34829
- arXiv comment: 22 pages, 3 figures, 14 tables
- Full text: data/fulltext/2610.34829.txt

> Single-document corpus poisoning under black-box access poses a severe threat to Retrieval-Augmented Generation (RAG). However, existing attacks predominantly rely on explicit factual refutations or imperative instruction overrides. Modern aligned LLMs often arbitrate such conflicts conservatively, rejecting overt contradictions in favor of parametric memory or clean retrieved context while triggering input guardrails. We propose MONOLOGUE, a single-document poisoning framework based on Logic Hijacking without explicit refutation. Rather than disputing the ground truth, our method concedes it as an authoritative historical baseline before introducing the update, weaving a grounded record-correction narrative (e.g., dated institutional reattributions) that presents the counterfactual target as the most recent update. To prevent suspicious live writes, payloads are refined entirely offline via local multi-dimensional gated optimization, coupling automated text quality audits with surrogate behavioral verification. Evaluations across three benchmarks, three retrieval backends, and four open-weight generator regimes show that our method achieves the strongest overall attack efficacy among the evaluated single-document poisoning attacks.

### SkillQR: Agentic Skill Discovery for Reason-Intensive Query Rewriting
- arXiv 2610.33768v1 · v1 2026-10-24 16:19 UTC · cs.IR
- Authors: Kenan Jiang, Meixiu Long, Zihao Zhang, Ran Xu et al.
- Topics: RAG (generic), Query fan-out · score 11 · found via cs.IR
- Link: https://arxiv.org/abs/2610.33768
- Full text: data/fulltext/2610.33768.txt

> Dense retrievers provide grounded evidence that mitigates hallucinations in outputs from Large Language Models (LLMs). Real-world queries are often verbose, ambiguously framed, or require multi-step reasoning, introducing irrelevant details that weaken semantic matching for dense retrievers. Query rewriting is a widely adopted pre-retrieval technique that leverages LLMs to reformulate queries and bridge the semantic gap between such queries and the retrieval target. Existing rewriting approaches either rely on expensive proprietary models, substantial training data, or iterative retrieval and rewriting, while largely applying a uniform rewriting strategy regardless of the retrieval corpus. We observe that effective query rewriting instructions are not universal: the optimal strategy depends on the retrieval target, rather than the model alone. We introduce SkillQR, a query rewriting framework that automatically discovers reasoning strategy sets from the retrieval target and dynamically routes a query to the appropriate rewriting strategy at inference time. Without relying on training data, SkillQR achieves competitive performance compared to fine-tuned rewriting models on the BRIGHT and R2MED benchmarks, while also providing lower inference latency than iterative rewriting approaches.

### Assessing the CAD Capabilities of General-Purpose AI Models: A Case Study of GPT-6 Astra
- arXiv 2610.24451 · v1 2026-10-17 00:00 UTC · 
- Authors: Qiang Zou, Jiajun Shen, Zhijie Yang, Yuhao Wang et al.
- Topics: GEO/AEO · score 10 · found via HF daily papers
- Link: https://arxiv.org/abs/2610.24451
- Full text: data/fulltext/2610.24451.txt

> Recent advances in general-purpose AI models and agentic systems have enabled them to perform some CAD tasks. A systematic assessment is now needed to establish what these systems can accomplish and how well their outputs meet engineering requirements. This paper presents an empirical study of GPT-6 Astra, a SOTA general-purpose AI model, across four basic CAD tasks: model understanding, generation, editing, and evaluation. We design test cases spanning different levels of complexity and engineering requirements. The results show that GPT-6 Astra can support multiple stages of CAD workflows, with successful outcomes in cases involving nontrivial geometric complexity. This suggests that general-purpose AI is beginning to offer practical value in almost all steps in CAD workflow. However, gaps remain between generating visually plausible geometry and producing valid, functional, and editable CAD models. Recurring errors in freeform geometry, parameter dependencies, and mating relationships between parts limit engineering usefulness. Agentic iterative refinement can improve results but does not consistently resolve critical errors; long completion times further constrain practical use.

### Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players
- arXiv 2610.33845v1 · v1 2026-10-24 18:33 UTC · cs.AI, cs.LG, cs.MA
- Authors: Changlian Ma, Limin Wang
- Topics: Query fan-out · score 10 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2610.33845
- arXiv comment: 20 pages, 8 figures, 15 tables. Code and benchmark: https://github.com/MCG-NJU/AutoTavern
- Full text: data/fulltext/2610.33845.txt

> Can LLM agents carry a hard real-world problem from raw data to a system that holds its own against people? We study this in Hearthstone Battlegrounds, an eight-player auto-battler with stochastic shops and battles, hidden information and nearly a thousand interacting cards. We present AutoTavern, a self-improving research system: specialised LLM research agents share a typed research memory, every claim passes verification gates, and live games close the loop, so the agents improve the simulator, opponents and policy and, from the same feedback, their own research process; a human sets goals and rules on ambiguous mechanics. In 20 days AutoTavern built TavernGym, the first faithful, full-content reproduction of the live game, and delivered 23 versions of TavernAgent, trained with PPO against opponents calibrated to real games. TavernAgent plays complete games on the live ladder by itself: its rating rose from 6,000 to about 15,000 and, on the public leaderboard's measure, its last 20 records average a placement of 1.60 with 80% first places, better than the server's ten highest-rated players on every statistic (2.34, 59%). TavernBench, 960 tasks in 40 scenarios, shows that the system the agents built is the strongest player: TavernAgent answers 91% of the play tasks against at most 63% for frontier LLMs, and decides in 0.03 s where they need up to 26 s; within the second a live turn allows, it keeps 90% and no LLM more than 26%. LLM agents build far better than they play. We will open-source TavernBench and TavernGym at https://github.com/MCG-NJU/AutoTavern.

### Context Is Not Free: Carbon-Aware LLM Routing for Multi-Turn LLM Web Services across Geo-Distributed Data Centers
- arXiv 2610.35230v1 · v1 2026-10-26 11:20 UTC · cs.AI, cs.CY, cs.DC
- Authors: Xiaoyang Zhang, Yuejun Yan, Qingang Zhang, Yonggang Wen
- Topics: GEO/AEO · score 10 · found via cs.AI, cs.CY
- Link: https://arxiv.org/abs/2610.35230
- Full text: data/fulltext/2610.35230.txt

> The sustainability of the Web has drawn growing attention, as large language model (LLM)-based web services leave a substantial carbon footprint. These services typically run in geo-distributed data centers whose grid carbon intensity varies across regions and over time, so routing each query to a cleaner region or a smaller model can reduce emissions. A conversation, however, is a stateful web session: each turn reuses the key--value (KV) cache of its history, which resides only where earlier turns were served. Serving a turn on another deployment requires recomputing this history, whose carbon cost grows with the conversation and can outweigh the saving of the move. Existing carbon-aware LLM routers treat a conversation's queries as independent and ignore this cost. We present CarbonRouter, an online framework that jointly selects the model, GPU type, and region for each query to minimize carbon emissions. CarbonRouter introduces a cache-aware carbon cost model, which charges history recomputation to every candidate deployment using cached-token counts from the serving backends, and uses a lightweight gate that keeps a session on its cached deployment when it would likely move back at the next turn and rebuild its history again. We evaluate CarbonRouter in trace-driven experiments on two real-world conversation datasets with five LLMs, three GPU types, and four regions, where it achieves the lowest carbon of all policies. CarbonRouter reduces CO$_2$ by 16.1\% on average relative to FairCarbon, a state-of-the-art carbon-aware router with the same action space, while also improving predicted answer quality and estimated latency. Moreover, the saving rises further to 23.1\% for sessions longer than 30 turns.

### RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents
- arXiv 2610.36878v1 · v1 2026-10-27 09:18 UTC · cs.AI, cs.CL
- Authors: Delin Wang, Sinuo Wang, Rui Sun, Beidi Luan et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2610.36878
- Full text: data/fulltext/2610.36878.txt

> Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirements explicit, but task-level checklists may leave the overall analytical structure underexamined. We introduce RubricAtlas, which derives type-level analytical requirements from expert reports on different objects within the same research type and organises detailed checks around recurring analytical questions. The requirements give related tasks a shared standard for what to analyse, without prescribing their answers. Our framework links binary checkpoints to report passages and evaluates completeness separately from argument validity. Built from 3,079 Chinese financial research reports, RubricAtlas covers 99 research types. Reference-report selection experiments show that individual reports cover only about half of their type's analytical questions, and that selecting requirements from different reports changes evaluation scores and agent rankings. Across ten agents, two judge pipelines achieve checkpoint agreement of $κ$ = 0.71 and agent-ranking agreement of Kendall $τ$ = 0.87. Controlled deletions reduce scores on the affected analyses, while padding produces no detectable increase. These findings support type-level rubrics for comparing the analytical completeness of Web deep research outputs, with individual decisions traceable to report evidence.

### SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation
- arXiv 2610.36991v1 · v1 2026-10-27 10:38 UTC · cs.AI, cs.CL, cs.IR
- Authors: Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler, Cahit Berkay Kazangirler
- Topics: Citation & source selection, RAG (generic), Brand/product recommendation · score 10 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2610.36991
- arXiv comment: 26 pages, 5 figures, 10 tables. This work is intended for submission to an IEEE journal
- Full text: data/fulltext/2610.36991.txt

> Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redundant passages, miss cross-chunk dependencies, and provide incomplete evidence for multi-hop reasoning. We propose SpectRAG, a spectral graph-augmented retrieval framework that combines hybrid candidate seeding, weighted chunk graph construction, graph-based expansion, spectral relevance propagation, and token-budgeted context selection. Document chunks are represented by dense semantic embeddings and graph-spectral coordinates derived from a weighted chunk graph whose edges encode semantic similarity, document adjacency, section hierarchy, shared entities, citation links, and similarity between LLM-generated utility questions. At query time, SpectRAG builds a high-recall seed set using exact inner-product search and hybrid relevance signals, expands it over the chunk graph, re-scores candidates using graph proximity and spectral information, and assembles the final context under a fixed token budget. The goal is not merely to retrieve individually similar chunks, but to construct a context that is relevant, diverse, structurally connected, and sufficient for grounded reasoning. Experiments on MultiHopRAG, UltraDomain, and long-document question-answering settings show that SpectRAG improves broad evidence recovery and achieves competitive generation quality against dense, hybrid, HyDE, LightRAG, and NaiveRAG baselines. The results further indicate that graph-spectral structure is particularly useful for inference-oriented and cross-document retrieval, while highlighting trade-offs in early precision, computational cost, and domain-dependent performance.

### LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents
- arXiv 2610.37166v1 · v1 2026-10-27 12:55 UTC · cs.AI
- Authors: Sinuo Wang, Wentao Zhao, Jiacheng Lu, Rui Sun et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2610.37166
- Full text: data/fulltext/2610.37166.txt

> In finance, the answer that matters is usually the current one: prices, rates, and disclosures hold only as of a given day, so retrieving up-to-date facts is a core capability of a financial agent. Yet most financial benchmarks overlook timeliness. They fix each answer at annotation time, so the gold goes stale as markets move and, once leaked into training data, rewards recall rather than search and analysis. We introduce LiveSearch, a live benchmark that stores each question as executable verifier code: a typed program of calls to a professional financial data service, followed by a declarative extractor. The question is frozen, while its gold answer is determined by executing the program against professional financial data at evaluation time, and a daily job re-executes it with no human or language model in the loop. A memorized answer is thus likely outdated, and a model must reach the current one through tools and analysis. Construction is equally automatic: a language model only verbalizes programs enumerated from real tool responses and never chooses an answer. Under general web search, six contemporary tool-calling models reach 70.9% to 76.7% answer accuracy. Over three consecutive days, 70% of served questions change their gold value, and even under tolerance-aware matching, a literally reused earlier snapshot fails on a majority of questions within a single day. Per-question tracking uncovers dynamic shifts in correctness masked by aggregate accuracy.

### Quantifying and Prioritizing Stealthy Source-Manipulation Threats Against Multi-Source Anomaly Detectors
- arXiv 2610.36693v1 · v1 2026-10-27 06:09 UTC · cs.CR, cs.LG
- Authors: Indraveni Chebolu, Seema Panghal, Arnab Mallick, Ch A S Murty
- Topics: Clicks & measurement, Manipulation · score 9 · found via cs.CR
- Link: https://arxiv.org/abs/2610.36693
- arXiv comment: To be appeared at Workshop on AI for Cyber Threat Intelligence (WAITI) 2026 @ ACSAC 2026

> Security pipelines often fuse several data sources and protect a downstream model with a cross-source anomaly detector. Such detectors are usually judged by their clean false-positive rate and by how well they catch random corruption. Neither metric captures an adversary who controls some sources and targets a specific downstream decision. We propose a threat-quantification score, the \emph{task-conditioned visibility margin}, defined as the least detector evidence a manipulation must reveal per unit of harm to the downstream task. The margin has a closed form, takes about $85\,μ$s per certificate, yields a minimum-evidence attack, and identifies task-relevant directions the detector cannot see. On a 17-channel industrial telemetry benchmark, a detector that flags 82.8\% of random single-channel corruptions is first-order blind on 64.7\% of task/subset pairs in an audit of one- to four-channel subsets. Task-conditioned manipulations cause more than twice as many falsely reassuring errors as generic stealthy ones, and more of them evade the alarm on four of five splits, mainly at small budgets. Used to prioritize audits on held-out subsets, the margin finds a median of four verified failures in ten checks, compared with none for random order and two for alarm-based ranking, and performs comparably to the task-gradient baseline. It also ranks vulnerable configurations of the learned GDN and TranAD detectors and of a five-source crop-yield panel.

### Mechanistic Failure Modes of Weight Pruning in Transformer Language Models
- arXiv 2610.37126v1 · v1 2026-10-27 12:25 UTC · cs.LG, cs.CL
- Authors: Nabeelah Faumi, Deshan Sumanathilaka
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.CL
- Link: https://arxiv.org/abs/2610.37126
- arXiv comment: 12 pages, 10 Tables

> Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation. We test this assumption with a factorial pruning study on GPT-2, crossing two importance criteria (magnitude, random), two component types (attention heads, MLP neurons) and three sparsity levels (3%, 50%, 70%). Using the fully characterised indirect object identification (IOI) circuit as ground truth, we measure circuit integrity with activation patching, path patching and direct logit attribution. We find two qualitatively distinct failure modes. Magnitude head pruning >= zeroes the circuit: output-facing heads are removed, and the model falls to near-chance. Magnitude neuron pruning at 30% inverts it: all 26 circuit heads remain intact, but Name Mover contributions flip sign, and the model systematically prefers the wrong name (17.7% accuracy). Perplexity ranks it as less damaged than random head pruning (74.6 vs 140.1). A replication of the Greater-Than circuit shows that the critical component type depends on the circuit's architecture. These results show that output metrics and structural checks can both miss mechanistic damage, motivating circuit-level causal analysis as a complementary evaluation of compressed language models.

### Correct Answers, Closed Gates: SolveBind for GUI Agents at the Verification Barrier
- arXiv 2610.32223v1 · v1 2026-10-23 06:27 UTC · cs.AI
- Authors: Xinhao Song, Haoxuan Peng, Su Su, Hongliang Wu et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.32223
- arXiv comment: 41 pages, 16 figures

> Websites and applications deploy CAPTCHAs and anti-automation mechanisms that use behavioral signals such as interaction trajectories and timing, not outcomes alone, to distinguish humans from automated agents. We call these protected GUI environments, where correctly solving a verification task is insufficient for end-to-end task completion. Agents must turn solver outputs into accepted interactions and adapt execution to runtime feedback under time constraints. We introduce SolveBind, a GUI-agent framework combining hierarchical solving with runtime supervision. A hierarchical solving tree decomposes verification into interdependent Perceive, Ground, Solve, Act, and Verify capabilities. A runtime supervisor grounds action commitments in tool-derived evidence, revises them as evidence arrives, and mediates execution under explicit recovery budgets. Across nine CAPTCHA task families and nine backbone models, SolveBind achieves the highest success rate on eight backbones, outperforming the strongest baseline by 13.3-34.5 percentage points. It achieves the highest success rate on all six AndroidWorld backbones. In a paired GPT-5.5 analysis, MobileAgent produces correct answers but fails dynamic verification on 13 of 90 tasks; SolveBind succeeds on seven of these tasks. With automatic submission, removing binding reduces success from 82.22% to 71.56% and increases latency and token usage. Recovery caps reduce execution cost with a small observed success trade-off: removing them raises success from 82.22% to 83.56%, while increasing latency and token usage to 3.7x and 2.4x their full-supervision values, respectively. These results support evidence-grounded execution control while identifying a success-cost trade-off in recovery and failure boundaries of heuristic submission rules.

### Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution
- arXiv 2610.32285v1 · v1 2026-10-23 07:43 UTC · cs.AI
- Authors: Zhiyong Cao, Hengjie Zhu, Yongxin Wang, Xuchen Li et al.
- Topics: Citation & source selection · score 8 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2610.32285

> LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited attention to the evaluation of agent harnesses. To address this gap, we introduce TraceTrial-Bench, which organizes harness reliability into seven components covering context, execution, governance, lifecycle, observability, tools, and verification. We construct 95 expert-level, mechanism-oriented tasks with executable or state-based ground truth to support semantically equivalent comparisons while preserving the native behavior of each harness. We design a Trajectory Tracing (TT) module to capture agent execution traces and introduce a two-layer evaluation framework that separately assesses agent performance and harness reliability. In addition, we design a Multi-source Evidence Acquisition (MEA) module to provide evidence from the agent context, harness, and execution environment for LLM-based evaluation, and develop a Failure Attribution (FA) module that uses explicit mechanism chains to support attribution at the run level. Across 4 harnesses, 9 models, and 95 tasks, our evaluation of 3,420 runs yields macro-averaged harness scores ranging from 59.8% to 72.0%, while 31.1% of runs achieve task success despite failing at least one harness criterion. TraceTrial-Bench provides an auditable and reproducible foundation for comparing agent harnesses, diagnosing their failures, and studying how harness design interacts with model behavior.

### Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms
- arXiv 2610.32945v1 · v1 2026-10-23 17:39 UTC · cs.AI, econ.TH
- Authors: Yuhang Ji, Fasheng Xu, Tianjun Feng
- Topics: Ads · score 8 · found via cs.AI, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2610.32945

> Large language model (LLM) platforms introducing advertising must decide how much capability ad revenue should fund and what consumers should pay to avoid ads. We study a monopolistic platform that jointly chooses costly response quality, advertising intensity, and subscription prices when advertising reduces user value but better service raises advertising returns. Three findings follow. First, when partly ad-supported and ad-free plans coexist, advertising can finance useful service for consumers who receive none under pure subscription. Lower effective quality in middle plans weakens the alternatives available to premium users, allowing higher prices for unchanged ad-free service. Some fully ad-supported users gain utility, while partly ad-supported and ad-free users lose: broader access can coexist with utility polarization. Second, an intermediate advertising cap can maximize consumer surplus by preserving some revenue that finances service while limiting degradation. Third, cheaper compute can raise quality and reduce ad intensity, yet sufficiently large cost reductions can increase aggregate advertising revenue above its initial level because better service raises the value of the remaining advertised interactions. An extension shows how advertising-funded upgrades can bring plans to the same maximum capability and advertising exposure, eliminating the basis for different prices. These results make menu design central to evaluating LLM advertising: the consequences extend beyond users who see ads to the alternatives and prices faced by those who do not.

### Deletion, Substitution, Repair and Transplant: Component Attribution in BARBICAN, a Layered Prompt-Injection Gateway for MCP
- arXiv 2610.33198v1 · v1 2026-10-23 18:47 UTC · cs.CR
- Authors: İpek Abasıkeleş Turgut, Edip Gümüş
- Topics: Citation & source selection · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2610.33198
- arXiv comment: 24 pages, 13 tables. Reproduction artifacts (per-request traces, detector scores, verification script): https://doi.org/10.5281/zenodo.23590822

> A neural classifier can fail completely inside a layered defense without any end-to-end number moving. We demonstrate this on BARBICAN, a fail-closed gateway for language-model tool mediation whose arbitration stage spent an entire recorded evaluation receiving text mangled by a misconfigured tokenizer. Correcting the misconfiguration lifts that stage's corpus-wide area under the ROC curve (AUC) from 0.392 to 0.855 and pushes system recall down, from 80.67% to 80.34%; a stub that answers "malicious" scores 80.77%, higher than either. The reason emerges once the stage's input distribution is examined: upstream routing hands it a band that is 96.82% malicious, and the enforcement design lets an incriminating verdict block while an exculpating one releases an input only through one narrow branch. Yet deleting it costs 673 detections. Substituting its verdict with a constant instead moves between 12 and 140 of 25,000 decisions. Transplanted into the arbitration stage, an off-the-shelf classifier that separates the band's inputs at an AUC of 0.916 changes 16 of 25,000 decisions. Measured against such detectors with operating points chosen away from the test data, the gateway leads on its own benchmark distribution and falls behind once that distribution changes. In our earlier gateway, the review model's band is 92.94% malicious and a constant verdict is as accurate as the review model. We argue that an ablation figure for any routed stage is unreadable without the class balance of the band that stage receives, and that deletion experiments need substitution experiments beside them.

### Two Uncertainties Are Not One: Disagreement versus Decision-Risk in Cheap Structured Content Moderation
- arXiv 2610.33258v1 · v1 2026-10-23 20:08 UTC · cs.CL, cs.CE, cs.LO
- Authors: Karan Yadav
- Topics: Query fan-out, Clicks & measurement · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.33258
- arXiv comment: 11 pages, 6 figures, 5 tables

> Content moderation compresses a graded, contested human judgment into a binary act (leave up / take down) over billions of items, at a scale where running a frontier LLM on every post is uneconomical. A new class of frozen "System One" models returns typed, calibrated decisions instead of text at ~USD 0.000025 per call and ~100 ms. We run the first independent audit of one such model on 142,658 human-labeled comments, and benchmark it against 14 frontier reasoning models (the GPT-5.x, Claude, Gemini 3, and Grok families) on a shared probe set. Two findings stand out. First, the cheap model is accuracy-competitive: its zero-shot classification AUROC (0.83) is not statistically separable (paired bootstrap, n=56; a failure to reject parity, not proof of equivalence) from 13 of the 14 frontier systems while costing 1-3 orders of magnitude less, and it is no worse calibrated than several of them. Second, "confidence" conflates two uncertainties that come apart: human disagreement (where annotators split on satire and coded language) and decision risk (where the automatic action is costly-wrong). Under an asymmetric moderation loss these call for opposite escalation signals, so no single confidence number serves both. Because the model prices extra questions at nearly zero, decomposing the judgment into parallel sub-questions and reading their spread recovers a human-disagreement signal that the model's native confidence misses -- but this remedy is specific: it helps the weakest, disagreement-blind models and only when the decomposition aligns with the sources of disagreement; a specialist toxicity model and the strongest LLMs do not need it, and the effect is distribution-sensitive. We will release the instrument, the cached runs, and the analysis.

### SkillShift-Bench: Benchmarking Skill Learning under Environment Evolution for Web Agents
- arXiv 2610.33528v1 · v1 2026-10-24 08:09 UTC · cs.AI, cs.CL
- Authors: Bo-Yu Chen, Zhi Zhou, Yu-Feng Li
- Topics: Agents · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2610.33528
- arXiv comment: 70 pages, 8 figures. Accepted to EMNLP 2026 (Main Conference)

> Skill learning enables web agents to reuse prior experience for long-horizon interactive tasks. However, learned skills are typically evaluated in closed environments, overlooking the fact that real-world web deployment involves continuous shifts in invocation context, perceptual grounding, and execution feasibility. To this end, we introduce SkillShift-Bench, the first benchmark for evaluating skill learning with controlled open-environment shifts. SkillShift-Bench simulates Contextual Shift, Perceptual Shift, and Execution Shift across three self-hosted web systems, and evaluates agents with diagnostics covering task success, interaction cost, skill use, and skill failure. Comprehensive experiments reveal systematic robustness degradation under controlled shifts, characterized by lower success rates, higher interaction costs, and more frequent skill failures, with Execution Shift exerting the strongest pressure. We further formulate shifted skill execution as a nonstationary local executability problem and provide both a dynamic-regret analysis and a practical test-time adaptation method, demonstrating the feasibility of improving learned-skill execution without relearning the skill library. Code, tasks, environments, documentation, and the leaderboard are available at https://skillshift-bench.github.io/.

### Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation
- arXiv 2610.33728v1 · v1 2026-10-24 15:18 UTC · cs.GT, cs.AI
- Authors: Jinhao Zhou, Zhaohan Zhang, Xijian Xu, Jun Wu
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.33728
- arXiv comment: 22 pages, 12 figures, including appendices

> In large language model (LLM)-based multi-agent systems, reported confidence increasingly determines the allocation of scarce downstream attention, computation, and decision influence. This makes reporting strategic: an agent may overstate the relevance of its contribution even when its underlying belief is well calibrated. Existing calibration methods largely assume passive reporting and therefore do not address strategic incentives created when confidence determines downstream allocation. We formulate strategic calibration as a reporting-layer incentive problem and propose the Audited Pivot Scoring Mechanism (APSM). APSM offsets platform-controlled allocation benefits, uses inverse-propensity-weighted sparse audits, charges the Clarke pivot externality, and applies a strictly proper score. Under the stated model assumptions, truthful reporting is the unique expected-utility best response. We also characterize approximate execution and the audit-variance trade-off. Calculator-free experiments show that LLM agents inflate confidence under Top-$K$ incentives. With a shared agent-local utility interface, LLM agents reduce distortion under both Compensated Proper Scoring (CPS) and APSM. CPS achieves higher exact allocation match, whereas APSM yields lower Brier loss and numerically fewer cutoff crossings. Experiments further show that APSM enlarges the utility margin against allocation-changing deviations by $1.93\times$ and improves robustness under approximate execution. These results support incentive-aware elicitation as a distinct layer for reliable multi-agent coordination.

### Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses
- arXiv 2610.33849v1 · v1 2026-10-24 18:40 UTC · cs.CL, cs.CR, cs.LG
- Authors: Pushkal Kumar, Arvin Sahaym
- Topics: RAG (generic), Manipulation · score 8 · found via cs.CL, cs.CR
- Link: https://arxiv.org/abs/2610.33849
- arXiv comment: 26 pages, 7 figures, 14 tables

> Query-time filters that screen each retrieved document before it reaches the generator are the dominant published defense against retrieval-augmented generation poisoning, and they report near-perfect detection on domain benchmarks. We show that this performance is predicted by how the poison set was built rather than by what the filter reads: removing a single construction cue destroys the deployed decision before it destroys the ranking. Two label-free statistics of a poison set and its clean corpus profile the cue: containment, how often the target question appears verbatim in the poison, and length overlap. PoisonedRAG's released code prepends the target question to every inserted passage. Of the 21 published defense evaluations we survey, 8 verifiably run poison built this way and 5 substitute a length cue; separately, 12 report no false-positive rate at the operating point they deploy. Deleting only that prefix from the attack authors' own passages (0.93 still retrieved for their target) takes RAGuard, a published content filter we re-implement, from AUROC 0.953 to 0.758 and its miss rate from 0.191 to 0.763. Across four corpora, four attack families and ten per-document defenses on one shared candidate set, the profile predicts where detection saturates. Padding medical poison to clean length with word-shuffled filler that carries no content takes TrustRAG's set-level stage from a miss rate of 0.000 to 0.827, and one learned scorer of ours from 0.000 to 0.986 (0.321 at a matched 5% false-positive rate) while its AUROC holds at 0.953. The ranking survives; the decision does not. A defense-aware attacker defeats our own scorer, so we claim no defense. A detection result is evidence only when it is reported with its poison set's construction profile and the false-positive rate at the threshold actually deployed; we release the script that computes the profile.

### Decision-Native Recommendation with Large Language Models
- arXiv 2610.34124v1 · v1 2026-10-25 07:46 UTC · cs.IR
- Authors: Daoxuan Liu, Jiayi Liao, Jiancan Wu, An Zhang et al.
- Topics: Brand/product recommendation · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2610.34124
- arXiv comment: 12 pages, 6 figures

> Large language models (LLMs) bring world knowledge to user preference modeling in sequential recommendation, but generation-based recommenders express next-item predictions indirectly as text. Generated outputs may fail to identify a unique candidate item, depend on candidate presentation order in the prompt, and lack explicit confidence in the recommendation. Recent studies explore Jev, a model for fast option selection with explicit confidence. Inspired by Jev, we introduce decision-native recommendation, a new paradigm that jointly models item choice and recommendation confidence using LLM representations. It requires valid candidate selection, consistency under candidate reordering, and confidence that reflects recommendation accuracy. We propose Direct Item Choice Estimation (DICE), which learns a personalized next-item distribution over supplied candidates from user interaction history and recommends the highest-scoring item with calibrated confidence. Tree-structured attention shares history computation across isolated candidate branches for order-consistent candidate scoring in a single forward pass. On three recommendation datasets, DICE achieves higher top-one accuracy than all evaluated baselines. Separate evaluations show unchanged item choices under tested candidate reorderings and end-to-end speedups of up to approximately $6\times$ over the evaluated generation-based methods. Its confidence estimates support selective recommendation by identifying more reliable predictions and guide additional computation for low-confidence examples in offline routing.

### AgentProofBench: Benchmarking Reusable Verifiers for Web Agents
- arXiv 2610.34634v1 · v1 2026-10-25 23:20 UTC · cs.AI, cs.MA, cs.SE
- Authors: Jingjie Ning, Xueqi Li, Yi Lu, Yibo Kong
- Topics: Agents · score 8 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2610.34634

> Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 families, and four Web services. Experiments with DeepSeek Flash/Pro establish two linked measurements. Across 48 families, complete-panel and decision-replay tests retain 82/96 Flash and 79/96 Pro source programs; paired reuse-rebuild BA intervals are [-5.47, 1.57] and [-10.16, 0.00] percentage points. Across 22 execution families, deployment-state panel correctness separates program assignments whose two saved openings are both delivered correctly: 32/33 assignments with error-free panels, versus 1/11 with panel errors. All reference-defined program-gate regressions and withheld deliveries occur in the latter group. Neutral continuation attains the highest correct delivery under the tested generic feedback, providing a concrete baseline for measuring the value added by a gate. Released instructions, states, programs, reference rules, and trajectories connect each test failure to its execution consequences. AgentProofBench makes reusable verification assessable at both the requirement and policy levels.

### BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams
- arXiv 2610.34790v1 · v1 2026-10-26 03:32 UTC · cs.CL
- Authors: Sizhe Wang, Xinghao Fang, Rui Qiu, Zhenjia Ma et al.
- Topics: Brand/product recommendation · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.34790

> User memory helps personalized systems build on their understanding of users over time. In e-commerce, users convey their preferences and needs through both explicit language and implicit interactions with products. We study memory built from logs of these interactions, examining how it can \emph{remember} concrete evidence and established interests, and use that evidence to \emph{infer} underlying needs and preferences that inform judgments beyond well-observed product domains. Existing memory methods primarily target language-based interactions, and evaluations offer limited real behavioral data and limited separation of these capabilities. This leaves open how to jointly support and separately evaluate remembering and inference from behavioral logs. We formulate the problem of continual behavioral user memory around these joint requirements and develop a dedicated evaluation framework and memory method to address them. \textbf{BehaviorMemBench} is a benchmark built from real e-commerce logs covering 1{,}194 users and 17{,}462 behavioral batches over more than three years, with automatic future-behavior labels and a task-independent memory interface to separately evaluate remembering and inference under a common protocol. \textbf{BehaviorMem} is a memory design that organizes explicit behavioral facts and inferred user characteristics across long-term and short-term scopes in a two-axis state, with evidence-grounded formation, continual maintenance, and query-independent readout. Experiments across two builders and two task readers show that BehaviorMem leads the evaluated agentic memories on remember and infer, and reveal different method rankings across the two capabilities and competitive statistical baselines. Validation on a public dataset further supports its usefulness for downstream tasks based on behavioral histories.

### GUIFlow: Temporal Redundancy-Aware Incremental Inference for GUI Agents
- arXiv 2610.34959v1 · v1 2026-10-26 07:25 UTC · cs.CV, cs.AI
- Authors: Ye Li, Haoran Ding, Huanan Liu, Yuan Meng et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.34959

> GUI agents built on vision-language models interact with continuously evolving interfaces, yet conventional inference repeatedly recomputes representations of largely overlapping observations and histories. This mismatch makes multi-step interaction costly, while changes in context, interface content, and action arguments prevent straightforward cache reuse. We introduce GUIFlow, a framework for full-pipeline incremental inference in multi-image GUI interaction. Our central insight is that advancing a decision need not require rebuilding all supporting representations: each interaction step can instead selectively update computational states maintained across the trajectory. To support new decisions as the context evolves, GUIFlow adapts how past computation is reused: historical KV states are position-aligned and injected into the current context; change signals guide selective updates of current-observation states in the vision encoder and language model; and earlier action responses serve as speculative drafts verified by the target model. Together, these mechanisms enable cross-step reuse throughout visual encoding, prefill, and decoding without additional training, a separate draft model, or changes to the model-visible inputs and action interface. Experiments demonstrate up to 3.39x geometric-mean speedup across offline multi-image benchmarks and up to 3.49x in online, closed-loop interaction on OSWorld, while maintaining task performance broadly comparable to the dense baseline.

### GuardRAG: A Post-Retrieval Defense against Poisoning Attacks in Retrieval-Augmented Generation
- arXiv 2610.35071v1 · v1 2026-10-26 09:17 UTC · cs.CR
- Authors: Linghui Jiao, Kang Wei, Fushuo Huo, Ruijie Zhao et al.
- Topics: RAG (generic), Manipulation · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2610.35071
- arXiv comment: 8 figures

> Retrieval-Augmented Generation (RAG) enhances the factual grounding of Large Language Models (LLMs) by incorporating external evidence, but also exposes them to corpus poisoning attacks. In particular, coordinated attacks can introduce multiple mutually reinforcing poisoned documents into retrieved contexts, making reliable evidence filtering challenging. To address this problem, we propose GuardRAG, a training-free and plug-and-play post-retrieval defense that exploits the semantic structure of retrieved evidence to identify suspicious document groups. Specifically, GuardRAG first expands the retrieval range and removes near-duplicate candidates, then partitions the retained documents using Hierarchical Agglomerative Clustering (HAC) with a query-adaptive threshold. Finally, it scores and prunes suspicious clusters based on query relevance, cluster size, and semantic compactness. Experiments across three question-answering datasets, multiple poisoning attacks, and six LLMs demonstrate that GuardRAG substantially reduces attack success rates while maintaining answer utility under clean retrieval.

### Did the Model Use That? Counterfactual Training Boosts Self-Attribution in Language Models
- arXiv 2610.35295v1 · v1 2026-10-26 12:03 UTC · cs.AI, cs.CL
- Authors: Zikai Zhou, Jiacheng Sang, Yilin Xu, Yufei Jin et al.
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2610.35295
- arXiv comment: 29 pages, 5 figures, 20 tables. Code: https://github.com/stanford-oval/CREDIT

> A fundamental challenge for explainable and accountable language models is revealing how external information influences their answers. This paper examines whether models are self-attributive: that is, whether they indicate when -- and only when -- their responses to questions are influenced by information provided alongside the question. Furthermore, we explore how self-attribution can be improved through counterfactual training, which explicitly teaches models to distinguish between answers that do and do not depend on supplied information. We found that most of the eleven frontier models rarely attribute influential information in their answers, and the rest attribute non-influential information. Training acknowledgment into reasoning does not fix this: the acknowledgment does not reach the final answer. We introduce CREDIT, which directly supervises final-answer self-attribution with counterfactual labels, without the need for human annotation. CREDIT substantially improves attribution in four open models, including two distilled reasoning models, and outperforms reasoning-level fine-tuning and prompting baselines. Among answers that agree with a user's suggestion, CREDIT distinguishes those changed by the suggestion from those the model would have given anyway. Gains transfer partly to unseen information types and prompts containing sources that support conflicting answers.

### Governing Enterprise AI Traffic at Scale: Design and Operation of a Policy-Driven, Multi-Vendor LLM Gateway on Envoy
- arXiv 2610.35509v1 · v1 2026-10-26 14:33 UTC · cs.DC, cs.AI, cs.SE
- Authors: Mithun Sasidharan, Srinivasan Manoharan, Rupesh Thakur, Abhinav TK et al.
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.35509
- arXiv comment: 17 pages, 6 figures, 6 tables. Industry case study

> Large organizations consume large language models (LLMs) from several vendors at once, each with its own API dialect, credential model, streaming protocol and pricing. Integrated directly, this heterogeneity yields credential sprawl, format lock-in, unbounded spend and inconsistent governance. We present the design and production operation of the Cosmos LLM Gateway, the governed entry point for enterprise LLM traffic at PayPal. Built on Envoy, it splits work by latency profile: I/O-bound control decisions (authentication, credential brokering, policy and budget evaluation) run in an out-of-process external-processing service, while wire-format translation, token metering and prompt-cache shaping run in-proxy as a Rust WebAssembly filter, so that, by default, streamed response body chunks never wait on an out-of-process call. Models, providers and prices are largely validated data rather than code. Governance is declarative policy evaluated by Open Policy Agent and managed through a control plane with role-scoped authoring, approvals, pilots, shadow-mode rollout, usage notifications and versioned policy bundles. For use cases that require it, a data-loss-prevention layer can block, redact or pseudonymize detected sensitive content before it reaches a provider. Spend scopes are views over per-model usage counters, so a new budget applies to spend already recorded in its window without migration. As of September 2026, the gateway serves more than 12,000 developers and hundreds of business use cases, handling roughly 200 billion tokens per day across more than 100 models at 99.999% availability to business. In a benchmark of the core request path against a synthetic upstream, it adds a median of 4 ms and a p99 of 11 ms of overhead at more than 2,200 requests per second on two 4-vCPU instances. We report the architecture, policy model, evaluation and lessons learned.

### Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution
- arXiv 2610.35733v1 · v1 2026-10-26 16:52 UTC · cs.LG, cs.AI, cs.MA, cs.RO, stat.ML
- Authors: Zhenshuo Zhang, Ruoxuan Xiong, Hongyang R. Zhang
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.35733
- arXiv comment: 30 pages. To appear at NeurIPS 2026 (extended version)

> Multi-objective reinforcement learning is a fundamental problem for modern AI, with applications spanning post-training, reasoning models, and robotic control. A central challenge is to learn policies that balance competing objectives, such as helpfulness versus honesty in safety and alignment, or speed versus energy in robotics. The optimal policy can vary sharply with objective-weighting combinations, and the extent of this variation depends crucially on the degree of conflict among objectives, making per-preference policy learning sample-inefficient. In this paper, we introduce objective-conflict coefficients and derive near-optimal regret bounds for online settings using this measure, thereby quantifying the impact of misalignment on learning efficiency. Then, we design routed ensemble policy learning, an algorithm that maintains a small set of basis policies and dynamically routes trajectories to the policy with the highest potential reward. Finally, we consider trajectory selection as another approach to mitigate objective conflict, and design a kernel surrogate trajectory attribution algorithm that estimates how feedback signals from a set of trajectories influence policy learning on other trajectories. The kernel can capture nonlinear interactions such as synergy and antagonism between trajectories. We evaluate our approach across diverse environments and benchmarks: routed ensembles improve average performance by 4.3% over baselines for online environments from Meta-World and MO-Gymnasium, and kernel surrogate attribution improves correlation with leave-one-out analysis over existing baselines by 50%. When applied to trajectory selection, kernel-based attribution yields a 27% improvement in reward over baseline attribution methods.

### Robust LLM Data Selection via Content-Invariant Gradient Attribution
- arXiv 2610.36755v1 · v1 2026-10-27 07:12 UTC · cs.LG, cs.AI
- Authors: Jia Gu, Liang Pang, Huawei Shen
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.36755
- arXiv comment: 16 pages, 8 figures

> Gradient-based data attribution has become an important tool for high-quality data selection in the instruction fine-tuning of large language models (LLMs), as it estimates the contribution of training examples through their influence on model optimization. However, we find that existing global gradient attribution methods suffer from surface-form bias: minor changes to semantically irrelevant details, such as wording or formatting, can produce highly inconsistent attribution scores even when the underlying content remains unchanged. To address this issue, we propose Content-Invariant Gradient Attribution (CIGA), a robust framework for instruction data selection. CIGA first identifies layers whose gradients are both influential for attribution and stable under semantics-preserving surface-form perturbations, thereby reducing formatting noise in gradient features. It then dynamically fuses these attribution signals with semantic representations of the input, combining optimization-level influence with content-level information. Extensive experiments across multiple benchmarks show that CIGA produces more stable rankings under surface-form perturbations while preserving downstream capabilities and improving average performance. CIGA also reduces attribution cost, offering a robust and efficient approach to data selection for LLM instruction tuning.

### GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents
- arXiv 2610.36877v1 · v1 2026-10-27 09:17 UTC · cs.AI, cs.CL, cs.CV
- Authors: Bingchao Wang, Yongcheng Jing, Shunyu Liu, Chengyu Wang et al.
- Topics: Agents · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2610.36877
- arXiv comment: 26 pages, 11 figures, 16 tables

> Mobile GUI agents are typically fine-tuned 7B-scale vision-language models (VLMs) that generate each action as text. However, these VLMs decode every action token by token, and even agents that score candidate actions keep a large language model or VLM in the loop, making them slow and memory-hungry. To address these issues, we propose GUI-JEPA, to our knowledge the first decoder-free GUI agent policy built on a Joint-Embedding Predictive Architecture (JEPA), which selects actions in the latent space of a JEPA encoder pretrained on unlabelled GUI screenshots. Its action- and region-conditioned latent predictor turns the screen latent into one latent per candidate action, letting lightweight heads score all candidates against the instruction in a single batched pass, without decoding a token. We further show that the scorer relies on this latent pathway and that the predictor is trained for the decision itself: a randomly initialised predictor does just as well as one pretrained on screen dynamics. On AndroidControl, GUI-JEPA is 2.8-4.0x faster on the same GPU than a Qwen2.5-VL-7B agent we fine-tune with the same inputs, while reaching 86-92% of its in-distribution accuracy with 6% of its parameters. Code is available at https://github.com/bcwang-sjtu/GUI-JEPA

## More new topic matches, lower score, title only (56)
- KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation — https://arxiv.org/abs/2610.36973 (score 8; Brand/product recommendation, Ads)
- Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution — https://arxiv.org/abs/2610.37201 (score 8; Citation & source selection)
- LinMix: Data Mixing as Linear Domain Attribution — https://arxiv.org/abs/2610.37390 (score 8; Citation & source selection)
- How Reliable Is Individualized Functional-Network Attribution in Resting-State fMRI Cognitive Prediction in ADNI? — https://arxiv.org/abs/2610.37472 (score 8; Citation & source selection)
- From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents — https://arxiv.org/abs/2610.37482 (score 8; Agents)
- Steering for Safety, Hijacking for Profit: Trojan Threats in the LLM Activation Steering Supply Chain — https://arxiv.org/abs/2610.35043 (score 7; Brand/product recommendation, Manipulation)
- Proof-of-Agentness: Towards Verifying Agents on the Web — https://arxiv.org/abs/2610.35288 (score 7; Clicks & measurement, Crawl)
- Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation — https://arxiv.org/abs/2610.37080 (score 7; RAG (generic), Query fan-out)
- On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection — https://arxiv.org/abs/2610.32531 (score 6; Manipulation)
- Clean-label Poisoning Attack and Defense Game for Federated Learning in Vehicular Networks — https://arxiv.org/abs/2610.32765 (score 6; Manipulation)
- STROKE: Simple Sparse Structural Occlusions for Black-Box Adversarial Attacks — https://arxiv.org/abs/2610.32932 (score 6; Manipulation)
- How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration — https://arxiv.org/abs/2610.33168 (score 6; Clicks & measurement)
- Spoofing the Toolbox: Optimizing Tool Descriptions to Deceive LLM Agents — https://arxiv.org/abs/2610.33182 (score 6; Clicks & measurement, Manipulation)
- AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos — https://arxiv.org/abs/2610.33413 (score 6; Manipulation)
- RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions — https://arxiv.org/abs/2610.34356 (score 6; Manipulation)
- A Certified Robustness Framework for Backdoor Poisoning Attacks using $f$-Divergences — https://arxiv.org/abs/2610.34934 (score 6; Manipulation)
- Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security — https://arxiv.org/abs/2610.35451 (score 6; Manipulation)
- Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks — https://arxiv.org/abs/2610.35671 (score 6; Manipulation)
- Towards a Unified Framework of Optimal Input-Side Dimensional Configuration for Deep CTR Prediction — https://arxiv.org/abs/2610.35695 (score 6; Clicks & measurement)
- Learning Force-Reactive Humanoid Loco-Manipulation — https://arxiv.org/abs/2610.35862 (score 6; Manipulation)
- Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol — https://arxiv.org/abs/2610.36108 (score 6; Manipulation)
- cuArms: GPU-Accelerated Conflict-Based Planning for Multi-Arm Manipulation — https://arxiv.org/abs/2610.36250 (score 6; Manipulation)
- Cross-Day Compatibility of Daily Item Embeddings: An Empirical Study of Alignment, Scale Management, and CTR Adaptation — https://arxiv.org/abs/2610.36408 (score 6; Clicks & measurement)
- TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation — https://arxiv.org/abs/2610.36694 (score 6; Manipulation)
- Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces — https://arxiv.org/abs/2610.36709 (score 6; Clicks & measurement)
- ActiveAlign: Aligning Egocentric Manipulation via Active Perception — https://arxiv.org/abs/2610.36859 (score 6; Manipulation)
- Rethinking Positional Encoding and Interaction Granularity for CTR Prediction — https://arxiv.org/abs/2610.37140 (score 6; Clicks & measurement)
- Peers4U: Designing Learner-Centered Virtual Peers for Children's Multimodal Mathematics Learning — https://arxiv.org/abs/2610.37238 (score 6; Clicks & measurement, Manipulation)
- When Is a Relation Worth Trusting? Manipulation Costs, Exposure, and the Trust Trap in Multi-Relational Graph Learning — https://arxiv.org/abs/2610.37239 (score 6; Manipulation)
- Kinematic Constraint-Referenced Evaluation for Articulated Object Manipulation — https://arxiv.org/abs/2610.37550 (score 6; Manipulation)
- Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness — https://arxiv.org/abs/2610.37657 (score 6; Manipulation)
- Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination — https://arxiv.org/abs/2610.33503 (score 5; Query fan-out)
- Knowing When the Evidence Is Enough: Requirement-Directed Search with Horn-Closure Certificates — https://arxiv.org/abs/2610.34684 (score 5; Query fan-out)
- ACARE: Agent-Context-Aware Reranker for Iterative Search — https://arxiv.org/abs/2610.35840 (score 5; Query fan-out)
- Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking and Item-Level Conversion — https://arxiv.org/abs/2610.32420 (score 4; Brand/product recommendation)
- Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare Software Adoption with Language-Model Agents — https://arxiv.org/abs/2610.32781 (score 4; Brand/product recommendation)
- Separating Thinking from Spelling for Efficient Generative Recommendation — https://arxiv.org/abs/2610.32980 (score 4; Brand/product recommendation)
- Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest — https://arxiv.org/abs/2610.33248 (score 4; Ads)
- RefinedGAW: A Refined German Academic Web Dataset — https://arxiv.org/abs/2610.34572 (score 4; Crawl)
- MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation Explanations — https://arxiv.org/abs/2610.36389 (score 4; Brand/product recommendation)
- Latent Residual Reasoning for Ranking in Generative Recommendation — https://arxiv.org/abs/2610.36890 (score 4; Brand/product recommendation)
- PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search — https://arxiv.org/abs/2610.36958 (score 4; Brand/product recommendation)
- Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors — https://arxiv.org/abs/2610.36544 (score 3; Clicks & measurement)
- Coverage Under Contradiction: A Benchmark for Negation-Aware Retrieval — https://arxiv.org/abs/2610.37162 (score 3; Clicks & measurement)
- TriageRAG: Failure-Aware Self-Training for Adapting Retrieval-Augmented Language Models to Specialized Domains — https://arxiv.org/abs/2610.33776 (score 2; RAG (generic))
- A Domain-Aware Pipeline for Structured Extraction and Retrieval-Augmented Question Answering over arXiv Superconductivity Literature — https://arxiv.org/abs/2610.34391 (score 2; RAG (generic))
- Hallucination-Aware Multi-Agent RAG via Internal Attention Rewards — https://arxiv.org/abs/2610.35056 (score 2; RAG (generic))
- Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives — https://arxiv.org/abs/2610.35240 (score 2; RAG (generic))
- Read the Route: Attention-Steered Hypergraph Retrieval for Multi-hop RAG — https://arxiv.org/abs/2610.35412 (score 2; RAG (generic))
- QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking for RAG — https://arxiv.org/abs/2610.36557 (score 2; RAG (generic))
- Governed Sovereign RAG for Public Administration: Tripartite Epistemic Routing, Facet-Guided Clarification, and Deterministic Numeric Verification in Citizen Services — https://arxiv.org/abs/2610.36561 (score 2; RAG (generic))
- Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG — https://arxiv.org/abs/2610.36915 (score 2; RAG (generic))
- When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG — https://arxiv.org/abs/2610.37358 (score 2; RAG (generic))
- Multimodal Requirements Traceability Link Recovery in Industrial Settings — https://arxiv.org/abs/2610.34503 (score 1; RAG (generic))
- Learning to Remember: Advances in Memory Mechanisms for Large Language Models — https://arxiv.org/abs/2610.35089 (score 1; RAG (generic))
- Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document QA — https://arxiv.org/abs/2610.35542 (score 1; RAG (generic))

## Other new cs.IR papers, title only (54)
- System One models Are Not Better Rerankers — https://arxiv.org/abs/2610.32318
- SkillRep: Characterizing and Understanding the Representation Design Space of Agent Skill Retrieval — https://arxiv.org/abs/2610.32336
- Agentic Memory Management Is the Next Frontier of Information Retrieval — https://arxiv.org/abs/2610.32464
- UAE GovTrust Scope Filtering Gains and Routing Failures in Bilingual Public Service Retrieval — https://arxiv.org/abs/2610.32608
- From archive to resource: bringing legacy data back to life at scale with large language models — https://arxiv.org/abs/2610.32616
- Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation — https://arxiv.org/abs/2610.32943
- Holo-NN: Holographic Nearest Neighbor Search via Compressive Sensing — https://arxiv.org/abs/2610.33224
- PinGER: Token-Efficient Generative Retrieval with Semantic IDs — https://arxiv.org/abs/2610.33435
- DyHist: Query-Aware Historical Dynamics Modeling for Temporal Knowledge Graph Extrapolation — https://arxiv.org/abs/2610.33473
- Bridging Search Intent and Tabular Data in Dataset Search — https://arxiv.org/abs/2610.33936
- LoopGR: Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth — https://arxiv.org/abs/2610.34157
- MIDA: Multi-Interest Decoding with Adaptive Aggregation for Session-based Recommendation — https://arxiv.org/abs/2610.34192
- $Δτ$-Bench: Pushing Agents Toward a Moving Capability — https://arxiv.org/abs/2610.34238
- Recovering Business Rules as Cascade Lookups for Enterprise Field Prediction — https://arxiv.org/abs/2610.34258
- Cross-Lingual Information Retrieval in Tetun for Ad-Hoc Search — https://arxiv.org/abs/2610.34362
- Theoretically Sound Item Similarity Measures for Recommender Systems — https://arxiv.org/abs/2610.34402
- The Price of Scale in Proactive Memory Recall — https://arxiv.org/abs/2610.34507
- HARP-LoRA: Hierarchy-Conditioned Rank Projection for Low-Rank Adaptation in Scientific Table Understanding — https://arxiv.org/abs/2610.34589
- Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents — https://arxiv.org/abs/2610.34673
- DPE-Rec: Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction — https://arxiv.org/abs/2610.34700
- Discovering Topics from Linear Autoencoders — https://arxiv.org/abs/2610.34739
- SLIDE: Search-to-List Item Distillation for Single-Rollout Generative Retrieval — https://arxiv.org/abs/2610.34764
- CA-HNM: Constraint-Aware Hard Negative Mining for Dense Retrieval with Structured Domain Models — https://arxiv.org/abs/2610.35045
- Reading the Registers of Honorius III without Manual Line Transcription: Forced-Aligned HTR, End to End, Modular or Hybrid — https://arxiv.org/abs/2610.35085
- When Fusion Order Matters: Insights on Progressive Multimodal Representation Learning for Cross-modal Retrieval — https://arxiv.org/abs/2610.35125
- Octen-WebGR: Scaling Generative Retrieval to 200 Million Web Pages — https://arxiv.org/abs/2610.35256
- Unified Heterogeneous Feature Interaction via Effective-Rank Scaling for Recommender Systems — https://arxiv.org/abs/2610.35318
- CRIM: Composable and Reusable Item Memory for Efficient Personalized Retrieval — https://arxiv.org/abs/2610.35323
- Agreement Between Reconstructed and Native GDELT GKG Records: A Field-Level Baseline — https://arxiv.org/abs/2610.35358
- RELAY: One Query, Two Roles for Sequential Recommendation — https://arxiv.org/abs/2610.36000
- Beyond "[at]": A Large-Scale Measurement of Email Address Presentation on Computer Science Scholars' Homepages — https://arxiv.org/abs/2610.35499
- Tiny Suffix Arrays — https://arxiv.org/abs/2610.35543
- Cross-Domain Sequential Recommendation with Representation-Level User Transfer — https://arxiv.org/abs/2610.35550
- Do Similarity Measures Measure Similarity? How User Activity Creates Phantom Correlation in Recommender Systems — https://arxiv.org/abs/2610.35765
- Is the education gap in generative AI use smaller than the internet's was at a similar level of use? Evidence from 16 European countries — https://arxiv.org/abs/2610.36181
- Counterfactual Profile Perturbations for Recommendation Explanations: A Reproducibility Study — https://arxiv.org/abs/2610.36208
- BehaveRec: When Does Long-Term Behavioral History Help Sequential Recommendation? A Study with Session, History, and Community Signals — https://arxiv.org/abs/2610.36239
- Preserving rare-item recall under a storage budget: quantization, distillation, and the limits of teacher fidelity — https://arxiv.org/abs/2610.36267
- From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn — https://arxiv.org/abs/2610.36383
- ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction — https://arxiv.org/abs/2610.36500
- CCP-DP: Cross-cluster context-guided phase dynamic programming for DNA storage sequence reconstruction — https://arxiv.org/abs/2610.36559
- Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift — https://arxiv.org/abs/2610.36585
- The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation — https://arxiv.org/abs/2610.36763
- DuTri: Dual-Branch Modeling with Triadic Factorization for Multimodal Multi-Scenario Recommendation — https://arxiv.org/abs/2610.36836
- When Diffusion Recommenders Stop Sampling: Preserving Generative Diversity — https://arxiv.org/abs/2610.36954
- Compote: Collapse-Resistant Multiple Hypothesis Learning For Sequential Recommendation — https://arxiv.org/abs/2610.37005
- Lossless Compression of Proximity Graph Indexes for Efficient Approximate Nearest Neighbors Search — https://arxiv.org/abs/2610.37176
- AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems — https://arxiv.org/abs/2610.37228
- GradCO: Behavior-Aware Gradient-Conflict Offloading for Text-Based Person Anomaly Search — https://arxiv.org/abs/2610.37267
- Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven Recommendation — https://arxiv.org/abs/2610.37280
- LESSRec: Level-Specific History Modeling for Semantic ID-Based Recommendation — https://arxiv.org/abs/2610.37286
- Can Complementary Signals Bridge Similarity Islands? Manifold-Augmented Graph Embedding for Multimodal Recommendation — https://arxiv.org/abs/2610.37409
- LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation — https://arxiv.org/abs/2610.37570
- REGER: Modeling inter-item Relations with Semantic IDs for Generative Recommendation — https://arxiv.org/abs/2610.37584

## Already listed on an earlier day, still inside the look-back window (0)
