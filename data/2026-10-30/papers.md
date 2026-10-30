# Paper candidates — 2026-10-30 (IST)

Generated 2026-10-30 06:21 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 35 new topic matches · 16 other new cs.IR · 110 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (35), highest score first

### Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a Distilled 4B Student on Ten Engines under Controlled Retrieval
- arXiv 2610.38090v1 · v1 2026-10-28 00:11 UTC · cs.AI, cs.IR
- Authors: Elisha Bajemon, Andre-Louis Rochet
- Topics: GEO/AEO, Citation & source selection · score 18 · found via cs.AI, cs.IR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2610.38090
- arXiv comment: 12 pages, 1 figure, 4 tables. Model: https://huggingface.co/citead/geo-citation-ranker-4b ; benchmark and code: https://huggingface.co/datasets/citead/geo-citation-benchmark
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative engine optimization needs a scorer that ranks candidate pages by the share of an answer they will receive as citations. We measure pretrained rerankers, a hosted typed decision model (Jev), eight open decision models and distilled students on GEO-Bench queries answered by ten engines that receive the same candidate sources in their prompt. Where several engines answer the same query, they agree with one another at a within-group Spearman correlation of 0.704. Jev and two open 27B decision models, used without training, are the strongest scorers at 0.575 to 0.578. A Qwen3-Reranker-4B fine-tuned with low-rank adapters on teacher labels for other GEO-Bench queries, released as GEO Citation Ranker 4B, reaches 0.542 to 0.549 across three seeds, and its differences with the 27B models and with Jev are not distinguishable from zero on 229 queries. Most of the remaining distance between the student and Jev disappears when Jev scores one passage at a time, as the student does. Students trained on teacher labels and on observed engine citations reach the same level, and labels from Jev alone match the two-teacher target at 0.6B. We release the model, the benchmark, the predictions of every reported scorer and the code.

### Does the Citation Matter? Quality, Grounding, and Physician-Rubric Accuracy of Google's AI Overviews for Medical Information
- arXiv 2610.39339v1 · v1 2026-10-29 04:31 UTC · cs.CL, cs.CY, cs.HC, cs.IR
- Authors: Sam Agnoli, Brigid Reilly, Lily Barna, Emőke-Ágnes Horvát
- Topics: GEO/AEO, Citation & source selection · score 18 · found via cs.CL, cs.CY, cs.HC, cs.IR, search abs:"AI overviews"
- Link: https://arxiv.org/abs/2610.39339
- arXiv comment: 12 pages, 5 figures, 10 tables. Code and data: https://github.com/SamAgnoli/AIOverviews
- Full text: data/fulltext/2610.39339.txt

> Google's AI Overviews (AIOs) are the first result users encounter when searching the web, shifting the work of selecting and evaluating sources from the user to Gemini. This may be especially consequential for health information, given that Google's traditional algorithm was designed to prioritize quality sources, and inaccurate information carries health risks. We evaluated 3,611 benchmark health questions, comparing each AIO against that question's top five traditional results on source selection and quality. We also evaluated the AIOs' statement grounding in their cited sources and how accurate AIOs were against physician-written rubrics. Overviews appeared for 96.4% of questions but drew on substantially different evidence than traditional search: only 44.4% of the top five results were cited by the corresponding AIO, which instead overrepresented commercial health publishers (e.g., WebMD, Healthline) at the expense of academic and government sources (e.g., Cleveland Clinic, National Health Service). AIO-cited pages scored lower than traditional results on four of six well-established credibility criteria. The grounding of AIO statements to their sources was poor: after correcting for classifier error, an estimated 56.7% of cited statements were supported by their cited page, and a further 20.8% of all statements were factual claims with no citation at all. When AIOs were graded against physicians' rubrics, they earned 38.2% of all available points (e.g., accuracy 54.2%, completeness 21.6%), and among the subset of AIOs whose physician rubric anticipated a specific inaccurate or potentially harmful claim, 22.2% of AIOs contained the harmful content. Notably, the accuracy of AIOs was unrelated to the grounding of their statements. We recommend AIO literacy interventions for users and holding AIOs at least to Google's own health-ranking standards.

### Beyond fabrication: Misattributed numbers in papers written by AI research agents
- arXiv 2610.38691v1 · v1 2026-10-28 18:57 UTC · cs.AI, cs.CL, cs.DL
- Authors: Mosab Alfaqeeh, Omar Hourani, Muath Hourani, Hashem Alfaqeeh
- Topics: Query fan-out, Brand/product recommendation, Clicks & measurement · score 17 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2610.38691
- arXiv comment: 42 pages, 5 figures, 13 tables. Code and data: https://github.com/mos3b-faqeeh/agent-integrity-analysis
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Verifying numerical claims in research written by AI agents is an important but challenging problem. Recent benchmarks show that many agent-written papers fail integrity checks, but such verdicts, often produced by a single LLM judge, identify failure without explaining its nature, and existing checks either test a paper for internal consistency or test whether a reported value appears somewhere in an agent's output. We re-analyze all 540 released judgments from a recent public benchmark of AI research agents (nine agents, fifteen open research problems) and manually label 256 numerical claims from 18 submissions. Failures concentrate on alignment between the paper and the underlying work rather than overt cheating, and about four in five unsupported claims correspond to values in the agent's own files that come from the wrong experiment, metric, or run. We introduce a deterministic claim-to-evidence checker that scores whether the surrounding context identifies the claimed result and calibrates each claim against numerical decoys. With its rules fixed before labeling, it certifies claims with over 90% precision against blinded annotators (78 of 85; Cohen's kappa = 0.89), while verifying only a subset of claims; most claims it cannot verify are nevertheless traceable, so failure to verify is not evidence of falsehood. An LLM verifier given the same evidence recovers more traceable claims but accepts about three times as many misattributed ones, so the two are best used together. Applied to 99 submissions, the checker reveals large differences in traceability across agents, and a second judge from a different vendor preserves the official agent ranking while passing twice as many papers. These findings motivate provenance-first auditing of AI-produced research.

### How Specific Do I Need to Be? Effects of User Query Underspecification on Deep Research Agents
- arXiv 2610.39413v1 · v1 2026-10-29 05:55 UTC · cs.CL
- Authors: Yi Wen, Xiangjue Dong, Bingxuan Li, Hangxiao Zhu et al.
- Topics: Citation & source selection, Query fan-out, Clicks & measurement · score 17 · found via cs.CL
- Link: https://arxiv.org/abs/2610.39413
- arXiv comment: 16 pages, 8 figures
- Full text: data/fulltext/2610.39413.txt

> Deep research agents (DRAs) conduct long-horizon reasoning, search, and literature synthesis to provide long-form answers to complex, domain-specific questions. These agents are typically trained and evaluated on fully specified user queries. However, real-world user queries can often be underspecified. We introduce UNDERSPEC-DR, a framework for systematically evaluating how underspecified queries affect agents' final answer quality and intermediate search behavior. Across three DRAs we evaluated, underspecification substantially reduces how well DRA's answers fulfill users' information needs, even though they remain grounded in cited evidence. Our analysis of intermediate search behavior suggests a possible explanation: DRAs conduct broader searches that draw less on the original user query but rely more on their learned prior during training, which can be misaligned with users' intent. Our findings reveal the vulnerability of current DRAs to underspecified user queries and inform future efforts to build DRAs that proactively recognize when additional user input is needed to reliably complete deep research tasks.

### Who Owns Digital News, and Who Gets Cited: Measuring Media Concentration Across 77 Countries and Seven AI Systems
- arXiv 2610.40164v1 · v1 2026-10-29 14:38 UTC · cs.CY
- Authors: Peter Carragher, Kathleen M. Carley
- Topics: GEO/AEO, Citation & source selection · score 13 · found via cs.CY, search abs:"AI overviews"
- Link: https://arxiv.org/abs/2610.40164
- Full text: data/fulltext/2610.40164.txt

> Digital news outlets compete for audience attention. Search engines equipped with generative AI systems such as Google's AI overviews increasingly decide where that attention goes, as well as the revenue it represents. Yet, the lack of a consistent data collection infrastructure between national-level regulatory bodies has hindered between-country comparative analysis of media concentration, and with it any assessment of how these intermediaries reshape digital news markets. To address this issue, we compile an ownership dataset for 9,761 digital news outlets drawn from Wikipedia and Wikidata, achieving high agreement with independently compiled US and UK news directories. Using this dataset, we derive traffic-weighted concentration indices for 77 countries. We find that journalists report more owner pressure in countries with higher concentration, and that outlet-level measures understate concentration, with owner-level indices a median 1.30x higher. Applying concentration measures to AI-mediated news discovery, we find that citation distributions from major AI systems are up to 2.08x more concentrated than traffic, and that if Google AI Overviews mediated all organic search, the resulting rise in US concentration would be several times that associated with highly regulated media mergers and acquisitions. Finally, our analyses indicate that AI systems preferentially cite state-controlled media outlets when prompted in that country's native language. Together, these findings raise concerns about the effect AI systems may have on digital media. We release the dataset to enable the monitoring of digital news globally, so that the impact of disruptive technologies on digital media markets can be tracked as they emerge.

### DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers
- arXiv 2610.37826v1 · v1 2026-10-27 18:40 UTC · cs.AI, cs.CL, cs.IR
- Authors: Dingyi Kang, Bingzhe Li
- Topics: RAG (generic), Query fan-out · score 12 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2610.37826
- arXiv comment: 12 pages, 2 figures, 7 tables. Code: https://github.com/Dingyi-Kang/DeFT-RAG
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop questions, which require chaining facts spread across several documents through intermediate entities that the question never mentions. Graph-based RAG methods retrieve once from the entities a question names and so rarely recover the full evidence chain. Iterative RAG methods recover it step by step, but their accuracy is limited by the many tasks they ask the LLM to perform, such as planning the sub-questions, deciding their dependencies, rewriting them as answers arrive, and keeping track of what is known. We propose DeFT-RAG, a RAG framework built on three components. First, DeFT-RAG generates one self-contained sub-question at a time from the original question and the sub-questions answered so far with their answers (QA pairs). Each sub-question names every entity it asks about, which removes the need to plan, track dependencies or rewrite, and lets the LLM focus on a single fine-grained task at a time. Second, DeFT-RAG moves the remaining LLM work outside the LLM: rule-based updates to a QA table that keeps track of what is known, and yes/no decisions made by a fine-tuned lightweight decision model. Third, DeFT-RAG caches the QA pairs and reuses an answer when a later question asks a sub-question with the same meaning. On MuSiQue, 2WikiMultiHopQA and HotpotQA, DeFT-RAG achieves the best accuracy among thirteen baselines with both gpt-4o-mini and Qwen3.6 as the backbone, while giving the LLM fewer input tokens than any other iterative method. With a QA cache shared across 1,000 MuSiQue questions, 23.1% of sub-questions are answered from the cache, which reduces LLM calls by 12.9% without lowering accuracy.

### AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers
- arXiv 2610.39234v1 · v1 2026-10-29 02:51 UTC · cs.CL, cs.CR
- Authors: Zhiyi Liu, Haohua Du, Haoqi Sun, Haisheng Tan
- Topics: Agents, Crawl · score 12 · found via cs.CL, cs.CR, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2610.39234
- arXiv comment: Code and Dataset are available at https://github.com/Lzzzzzzzzzzy/AgentHeal
- Full text: data/fulltext/2610.39234.txt

> Large language model (LLM) agents have demonstrated strong capabilities in automating complex information-seeking and transactional tasks across the open web. However, their real-world reliability remains limited by access barriers, such as dead links, authentication walls, rate limits, and anti-scraping defenses. These barriers block the primary execution path, causing agents to abort prematurely, loop indefinitely, or quietly compromise the user's original constraints. Existing evaluations either implicitly assume that target resources are freely accessible or focus on transient perturbations that simple retries can resolve, failing to capture scenarios where agents must actively reroute around impassable bottlenecks. To bridge this gap, this paper introduces AgentHeal, a comprehensive benchmark evaluating goal-preserving resource recovery, defined as the ability of web agents to detect non-transient access barriers, pivot to legitimate alternative sources, and fulfill the user's exact original objective. Spanning nine barrier families across a counterfactual sandbox and real-website replay, our experiments on leading LLM backbones show that average task success drops sharply from 89.4% to 43.7% under access barriers. Further analysis reveals that agents frequently fall for deceptive look-alikes, fail to escalate to users when necessary, violate access policies, or waste computation on futile retries, providing actionable diagnostics for developing resilient web agents.

### CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation
- arXiv 2610.39244v1 · v1 2026-10-29 02:59 UTC · cs.IR
- Authors: Minmao Wang, Huihuang Lin, Likang Wu, Hongke Zhao et al.
- Topics: Citation & source selection, Ads · score 12 · found via cs.IR, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2610.39244
- Full text: data/fulltext/2610.39244.txt

> Advertising platforms subsidize advertisers through billing discounts, and Advertiser Subsidy Allocation (ASA) chooses a subsidy level for every account to maximize total discounted revenue under a platform-wide subsidy-rate constraint. In practice, operators configure these subsidies from business rules, advertiser tiers and operating goals. Such configuration draws on rich business experience, yet as the advertiser base grows, tier-level policies can neither resolve how individual accounts respond across subsidy levels nor allocate a shared budget at the granularity of single accounts. We propose CASH, a Capability-Aware Subsidy Harness for ASA. CASH pairs a knowledge-guided large language model (LLM) with a data-driven numerical response model, learns from realized outcomes where each is locally reliable across accounts and subsidy levels, and turns this reliability into explicit capability licenses that govern source selection, agent review and budget allocation. Its Expected Policy Coverage Gain (EPCG) directs a limited feedback budget toward evidence expected to expand high-value reliable coverage, and the resulting feedback further improves the numerical model and updates capability estimates. In a one-month online experiment with CASH serving 60% of a large-scale advertising platform's traffic, CASH raises revenue per account by 15.35% and ADVV by 19.86% over Control at an essentially unchanged subsidy rate, with further gains in revenue quality, LTV and retention.

### UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation
- arXiv 2610.39426v1 · v1 2026-10-29 06:05 UTC · cs.IR
- Authors: Zonghe Shao, Huabin Chen, Sitong Lu, Fangmei Zhu et al.
- Topics: Brand/product recommendation, Ads · score 12 · found via cs.IR
- Link: https://arxiv.org/abs/2610.39426
- Full text: data/fulltext/2610.39426.txt

> List-wise ranking in e-commerce recommendation must balance user utility and commercial value across organic content, ads, and candidates from other businesses, while modeling candidate interactions and sequential dependencies. Existing generative ranking methods typically learn from logged exposure sequences and operate on truncated candidate sets from a single business. Exposure-sequence learning may not fully exploit post-exposure feedback signals. Meanwhile, generative ranking over heterogeneous, multi-business candidates remains less explored, particularly when recommendation scores and advertising value must be jointly modeled under generalized second-price (GSP) auctions. We propose Unified Generative Ranking (UGR), which performs generative ranking over the full request-level multi-business heterogeneous candidate set, typically comprising around a thousand candidates in production, and directly generates multi-business ranking lists through candidate-aware autoregressive decoding. To go beyond exposure-sequence imitation, UGR introduces complementary feedback supervision through weighted supervised fine-tuning and permutation preference optimization, which respectively leverage observed post-exposure feedback and feedback-derived preferences among permutations. UGR uses a training-time advertising debiasing tower to model historical ad exposure effects and incorporates current ad value during serving while preserving the existing allocation and GSP pricing rules. Multi-value sequence retrieval produces candidate ranking lists, and the existing downstream evaluator selects the final list for exposure. Offline experiments demonstrate consistent gains in ranking quality, while online A/B tests on Taobao's Guess You Like recommendation service yield improvements of 1.76% in Core IPV, 3.29% in Transaction Volume, and 2.10% in GMV over the production baseline.

### KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents
- arXiv 2610.39884v1 · v1 2026-10-29 11:59 UTC · cs.AI
- Authors: Xinhua Miao, Yuanzhen Rong, Weiru Zhang, Xiaoyi Zeng
- Topics: Brand/product recommendation, Ads · score 12 · found via cs.AI
- Link: https://arxiv.org/abs/2610.39884
- Full text: data/fulltext/2610.39884.txt

> Industrial advertising agents must continually adapt their decision knowledge to changing product offerings, traffic patterns, and operating policies. We present KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation), a training-free framework that evolves six typed knowledge modules while keeping model weights and executable harness code frozen. During our evolution, a deterministic Trace Verifier maps observed errors to candidate modules, and a Critic compares successful and failed trajectories to guide a tool-constrained Evolver. The Evolver applies atomic knowledge edits, which a fixed validation gate retains only when their measured gain reaches a threshold; otherwise, the previous knowledge state is restored. We evaluate KARMA with three LLM families on cases sampled from a corpus of approximately half a million real-world operation logs across six e-commerce domains. Across 18 domain--model settings, KARMA raises the average hold-out score from 30.19 to 39.15 (+8.96 points, +29.7%). Ablations show that removing either successful or failed trajectories more than halves the average hold-out gain. Evolved knowledge also transfers across domains without further adaptation, yielding an average hold-out gain of 8.54 points across all source--target pairs. By linking retained patches to their diagnostic evidence and validation outcomes, KARMA supports inspectable, reversible knowledge adaptation for agents in Web marketplaces.

### Letting AI Formulate the Research Question: Autonomous Research Agents
- arXiv 2610.39620v1 · v1 2026-10-29 08:48 UTC · cs.AI, cs.CY
- Authors: Ko Fujimura
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CY
- Link: https://arxiv.org/abs/2610.39620
- arXiv comment: 17 pages, 1 figure
- Full text: data/fulltext/2610.39620.txt

> Systems such as The AI Scientist have shown that AI agents can carry out and write up research, but in those demonstrations humans chose the research area and selected the outputs to show. We study letting the AI formulate the research question itself, and we report every run. Our system gives an off-the-shelf coding agent an instruction document and two skills: one for formulating the question, in which the agent diverges from recent technologies into problems of other fields, screens its candidates for known failure modes and obtains a critique from a different model; and one for peer review, in which a reviewer from another model family reruns the study from its records before the agent revises the paper. Over 13 development runs, changes to the one or two sentences that set the research area coincided with large shifts in what the candidate questions and the chosen papers were about, which led us to the area of a new technology applied to a societal problem. We froze the system after a pilot run and report five consecutive runs: the pilot, counted by a disclosed amendment to the pre-registration, and four pre-registered runs. All five runs went from question formulation to a revised, re-computable paper, with local computation on a laptop and no research input from humans, and external AI reviewers reading only the papers judged them at or near workshop level. We release the system, the five papers and the records needed to reproduce them.

### Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels
- arXiv 2610.39682v1 · v1 2026-10-29 09:28 UTC · cs.AI, cs.IR, cs.LG
- Authors: Qin-Wen Luo, Sheng Ren, Xiang Chen, Rui Liu et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2610.39682
- Full text: data/fulltext/2610.39682.txt

> Deep search agents extend language models by interleaving reasoning with external retrieval. However, effective search-agent training requires addressing two challenges beyond final-answer optimization. First, the capability frontier of agents is largely determined by training questions, whereas fixed or labeled task collections cannot adapt as agents improve. Second, outcome-only reinforcement learning treats all successful trajectories equally, even when some correct answers rely on redundant searches, creating an inherent tension between answer accuracy and tool efficiency. To address these issues, we introduce \textsc{ZEST-Search}, a zero-label and tool-efficient framework for search-agent training via heterogeneous co-evolution. Starting from unlabeled reference questions, \textsc{ZEST-Search} constructs validated search tasks online through an answer-first and evidence-path-guided generation process. A heterogeneous proposer adaptively constructs training tasks around the solver's evolving capability boundary, while the solver learns search-augmented reasoning through reinforcement learning. To jointly optimize task difficulty and search efficiency, \textsc{ZEST-Search} employs an intermediate-difficulty reward for the proposer and a task-local tool-aware reward for the solver, encouraging informative tasks and correct answers with fewer redundant searches. Experiments on seven general-domain and multi-hop question answering benchmarks demonstrate that \textsc{ZEST-Search} consistently improves search-agent performance while achieving higher tool efficiency without labeled search-training data or expert search trajectories. Further analyses show that heterogeneous generation, adaptive difficulty control, and tool-aware optimization enable more effective search-agent training.

### rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment
- arXiv 2610.40488v1 · v1 2026-10-29 17:15 UTC · cs.CL
- Authors: Art Kanke
- Topics: Query fan-out · score 10 · found via cs.CL
- Link: https://arxiv.org/abs/2610.40488
- arXiv comment: 27 pages, 1 figure, 9 tables. Code and data: https://github.com/ArtKanke/rTaste
- Full text: data/fulltext/2610.40488.txt

> Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a research agent alone or as a team, proposes minimum viable experiments (MVEs), forecasts whether each will pass a threshold it sets and ranks them. A separate executor then attempts every MVE, including those ranked last, and three model auditors judge the results. Of 415 MVEs, 194 are judged sound, valuable and new, but fewer than half of these (73) are also judged beyond the seed paper and non obvious. The agents' first choices match the auditors' most valued experiment more often than a random pick, but are not shown to improve on choosing the experiment written first. Their forecasts beat a base rate but are not measurably more accurate than those of a fresh instance of the same model given only the paper and registrations. Teams cost more without a clear overall improvement in proposal quality. The agents produce many worthwhile experiments, but the evidence that their rankings improve the choice of which to run remains limited. The evaluation harness and a dataset of all 415 MVEs, with their forecasts and audited outcomes, are available at https://github.com/ArtKanke/rTaste.

### Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis
- arXiv 2610.37830v1 · v1 2026-10-27 18:43 UTC · cs.AI, cs.HC, cs.IR, cs.MA, cs.SE
- Authors: Abhinav Goel, Agostino Capponi, Alfio Gliozzo, Chaitya Shah
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.AI, cs.HC, cs.IR
- Link: https://arxiv.org/abs/2610.37830
- arXiv comment: ACM TheWebConf2027 8 pages main content 4 pages appendix
- Full text: data/fulltext/2610.37830.txt

> AI agents can now write software from a plain-English description, but code that runs is not the same as code that does what was asked. This gap matters most for smart contracts, the programs behind Web3 applications that move money on a blockchain and cannot be fixed once deployed. We ask how to check whether an AI-written contract behaves as it should, and where the requested behavior gets lost. We design an evaluation built on execution rather than opinion. We replay the same transactions on an AI-written contract and on the original it should reproduce and measure how often they agree. We test every grading tool on planted mistakes, compare against an answer key written without the description, and audit our own scorer until known wrong answers cannot pass. Common methods, such as AI judges and standard analysis tools, miss obvious mistakes, and scoring choices matter too. Checking only the functions every system includes hid about half the difference between pipelines. We then propose an elicitation-first architecture. Before writing code, the agent asks the client a short checklist of questions, checks the contract against an independently written executable answer key, and returns disagreements to the client instead of silently rewriting code. Asking first matters far more than reviewing or patching afterwards, across three AI models, while automated security fixes often break requested behavior. A few well-chosen questions recover much of what a short description omits, and their value can be estimated without the original contract. To our knowledge, this is the first study in smart contract synthesis to gather missing requirements before generation and check the result against an independently written executable model. The lessons extend to any setting where AI agents turn requests into programs. We release our tools, 600 tasks and all results.

### What Hallucinations Have We Measured? Semantic Illusion, Confabulation, and Expressed Uncertainty
- arXiv 2610.38520v1 · v1 2026-10-28 09:32 UTC · cs.CL
- Authors: Hazel H. Kim, Jakub Binkowski, Ekaterina Fadeeva, Juan David Guerra et al.
- Topics: Citation & source selection, RAG (generic), Clicks & measurement · score 9 · found via cs.CL
- Link: https://arxiv.org/abs/2610.38520
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Hallucination remains one of the most critical challenges in deploying large language models (LLMs) reliably and safely. Yet the term is used inconsistently across the research community. We argue for a strict definition of hallucinations in LLMs. First, hallucinations should be confident incorrectness, kept separate from expressed uncertainty (UNK)1. UNK reveals that the model may be wrong, whereas a hallucination does not reveal it and is therefore more dangerous in practice. Conflating the two obscures their distinct behaviors and makes them hard to study. Second, hallucinations should be split by a simple re-elicitation test: does any semantically equivalent prompt recover the correct response? This test probes whether the relevant knowledge2 is accessible. If none does, the knowledge is likely absent or inaccessible, and the error type is a confabulation (CF) that likely requires external knowledge or retraining; if some does, the knowledge is accessible from the model but applied inconsistently, and the error type is a semantic illusion (SI) that simple prompt or decoding changes can mitigate3. Re-evaluating 14 recent hallucination methods under this taxonomy yields three findings. (1) Detection methods flag UNK more often than hallucinated responses (i.e., SI and CF). (2) Mitigation methods are far more effective for SI than for CF. (3) Latent signals are more informative than output-level signals for CF. An audit of recent hallucination papers shows that most conflate these categories. We recommend reporting CF, SI, and UNK separately, and introduce a practical labeling protocol that needs only a modest number of semantically equivalent prompts.

### PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas
- arXiv 2610.22990 · v1 2026-10-16 00:00 UTC · 
- Authors: Haoming Li, Defu Cao, Xu Hu, Yingtao Luo et al.
- Topics: Agents · score 8 · found via HF daily papers
- Link: https://arxiv.org/abs/2610.22990
- Full text: data/fulltext/2610.22990.txt

> Computer-use agents (CUAs) are commonly evaluated against fixed task specifications, but users may omit requirements, add constraints, or require approval before consequential actions. Completing the benchmark instruction does not guarantee serving the person who asked. We introduce PersonaCUABench, which holds 74 tasks across 11 domains fixed and varies only who asks. A persona agent, playing one of 44 personas in four groups, rewrites each instruction in that user's own words and answers the CUA's questions, while the CUA sees only the dialogue, never the profile or the original instruction. Across nine backbones (3,330 runs), mean task completion falls by 36% relative to the original requests. The losses have two sources: in 59.9% of cells that lose points, the agent engages with what the user asked for and still gets it wrong, and 11.2% are stops the user requested that the checker scores as failures. Even when a persona request is fully completed, the user gives the top satisfaction rating in only 62.7% of cells, against 84.1% for the original requests. CUAs should therefore be evaluated not only on task completion but also on whether they meet the requirements and constraints users express. Code: https://github.com/MatrAIx-ai/PersonaCUABench. Project page: https://matraix.ai/research/persona-cua.html

### Beyond Aggregate WER: In-domain Adaptation, Learner Speech, Code-Switching, and Speaker Attribution in Online Spanish Learning Classrooms
- arXiv 2610.38016v1 · v1 2026-10-27 22:13 UTC · cs.CL
- Authors: Olga Kellert, Samhitha Harish, Johnatan E Bonilla, Nemika Tyagi et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.38016
- arXiv comment: 15 pages, 9 Tables, 2 Figures
- Full text: data/fulltext/2610.38016.txt

> Automatic speech recognition (ASR) increasingly supplies transcripts for educational NLP, but aggregate word error rate (WER) can conceal errors concentrated in learner speech, multilingual turns, and speaker attribution. We compare platform-integrated, open-weight, adapted, and commercial ASR configurations on held-out sessions of online L2 Spanish interaction between L1 English learners and their instructors and tutors. Because English is the learner's shared first language, the interactions contain Spanish-only, English-only, and code-switched turns. Evaluation combines overall WER and character error rate (CER), WER disaggregated by speaker role and language context, and diarization error rate (DER). We also adapt Whisper large-v3 and MOSS-Transcribe-Diarize with LoRA using human-corrected in-domain classroom data. MOSS adaptation produced consistent improvements across speaker roles and language contexts, whereas Whisper showed smaller gains. Domain match proved more important than data volume: Larger out-of-domain bilingual and learner corpora did not outperform the smaller classroom corpus, where learner speech and code-switching are embedded in instructor--learner interaction. The open-weight MOSS adapter was competitive with commercial Muse Voice Transcribe on WER and CER and achieved lower system-provided DER on the recordings eligible for each system. Learner, English-only, and code-switched speech remained more difficult than instructor and Spanish-only speech. The findings demonstrate the value of condition-aware evaluation and interactionally matched data for bilingual educational ASR.

### Making Sense of Audience Change: Causal Attribution and Boundary Management on Xiaohongshu
- arXiv 2610.38026v1 · v1 2026-10-27 22:23 UTC · cs.AI, cs.CY, cs.HC
- Authors: Zhiyi Zhou, Kyrie Zhou
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CY, cs.HC
- Link: https://arxiv.org/abs/2610.38026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recommendation-driven platforms can reshape not only what users see, but also who becomes visible and how community boundaries are negotiated. We examine Xiaohongshu discussions surrounding a perceived World Cup-related audience influx to understand how users attributed community change and how those explanations related to boundary-management strategies. We analyzed 262 comments from eight high-engagement threads using researcher-led thematic analysis, structured coding, and permutation-based association analysis. Users described personalization as both social separation and a boundary that could fail, interpreted platform growth through audience acquisition and commercialization, and contested whether gender should define community membership. Among 70 comments with explicit attributions and strategies, attribution and strategy were strongly associated (Cramer's V = .583): algorithmic attributions concentrated in technical boundary management, while social-actor attributions more often aligned with social enforcement or normative socialization. These findings connect causal sensemaking with boundary management and show how audience restructuring can create governance consequences on recommendation-driven platforms.

### Vendster: An Evaluation Arena to Investigate How Forecasting Tool Quality Affects LLM Agent Behaviors in Buyer-Vendor Negotiation
- arXiv 2610.38292v1 · v1 2026-10-28 05:23 UTC · cs.GT, cs.AI
- Authors: Charin Polpanumas
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.38292
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Time-series forecasters are ranked almost entirely by accuracy metrics, but a forecast's decision value, its effect on the downstream decision, need not track accuracy and is rarely measured. This problem compounds as large language model (LLM) agents increasingly consume forecasters as tools, mediating them through stochastic, opaque policies. We present Vendster, an evaluation arena measuring how a forecaster's bias and prediction-interval width change the outcome of a buyer--vendor discount negotiation between two LLM agents. In the reference instance Vendster-M5, sampling base demand patterns from the M5 dataset, we evaluate two frontier-closed LLM families (Claude Opus 4.6 and GPT-5.6 Sol) and two open ones (DeepSeek-V3.2 and Qwen3-235B-A22B). Model-generated forecasts raise sales target attainment by up to +17 percentage points (p<0.001), yet standard forecast evaluation metrics such as relWQL and MASE do not predict negotiation outcomes at a statistically significant level. To isolate the causal structure, we substitute in synthetic forecasts with controlled bias and interval width. Under-prediction bias significantly improves outcomes for agents that react more to the forecasts---dose-response slopes -0.387 and -0.416 (p<0.001). Interval width has no statistically significant effect at zero bias. These findings indicate that the direction of forecast bias and agent forecast-reactivity are more strongly associated with downstream outcomes than forecast accuracy. Vendster is fully customizable and released under CC BY-NC 4.0 at https://github.com/amazon-science/Vendster.

### Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for Large-Scale Advertising
- arXiv 2610.38378v1 · v1 2026-10-28 07:17 UTC · cs.IR, cs.LG
- Authors: Yatong Xiao, Yibo Sheng, Lixiang Wang, Mingjie Sun et al.
- Topics: Ads · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2610.38378
- arXiv comment: 9 pages, 3 figures, under review
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative recommendation (GR) reformulates item retrieval as autoregressive generation of discrete semantic identifiers (SIDs), offering a unified paradigm for personalized recommendation. GR4AD, as an industrial generative recommendation framework, has greatly improved advertising revenue while enabling efficient real-time serving in Kuaishou.However, continued deployment has exposed three limitations: deterministic SID assignment remains sensitive to semantic boundaries; conventional backbone scaling provides diminishing revenue gains under strict serving constraints; and sequence-level value optimization provides limited credit assignment to intermediate SID decisions, causing likelihood-based beam search to prematurely prune potentially high-value candidates. We present GR4AD-X, which addresses these limitations through reliable SID construction, serving-efficient capacity scaling, and unified value alignment. Specifically, GR4AD-X improves SID reliability through Multi-Path assignment. It expands model capacity along multiple complementary dimensions rather than relying solely on wider or deeper backbones, achieving a better effectiveness-efficiency trade-off under strict serving constraints. Finally, Unified Value-Guided Generation and Discrimination (UniVGD) aligns generation with commercial value through prefix-level reward optimization, value-guided beam pruning, and discriminative reranking within a unified model. Large-scale online A/B tests on the Kuaishou advertising platform demonstrate that GR4AD-X achieves a cumulative revenue improvement of 3.07% over the deployed GR4AD baseline while satisfying strict latency and throughput constraints.

### Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents
- arXiv 2610.39251v1 · v1 2026-10-29 03:03 UTC · cs.AI
- Authors: Yuxiang Chai, Quyu Kong, Panrong Tong, Steven Hoi et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.39251
- Full text: data/fulltext/2610.39251.txt

> Trajectory-level GRPO is a common approach for training multi-step GUI agents, but repeatedly rolling out complete trajectories from the task root can be inefficient: task-level rewards provide coarse supervision over which intermediate decisions require improvement, while already-mastered prefixes are repeatedly re-executed before reaching difficult states. We introduce a two-stage adaptive training framework that jointly addresses where to learn and how far to roll out. We first construct reusable intermediate checkpoints from successful expert trajectories and select informative pivots using action disagreement, which measures uncertainty directly from sampled GUI actions. Stage I performs one-step RL at these pivots to improve uncertain local decisions. Stage II then progressively expands policy responsibility through adaptive Local, Suffix, and Root training according to task progress. Recoverable checkpoints enable repeated training from intermediate states without replaying the preceding trajectory. Across MobileGym and CUA-Gym-Hub, our method reduces environment interaction by 56-61% relative to Vanilla GRPO while improving task performance, demonstrating that jointly allocating training across states and rollout ranges can substantially improve GUI-agent RL efficiency.

### PFA: Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation
- arXiv 2610.39273v1 · v1 2026-10-29 03:25 UTC · cs.IR
- Authors: Pengjie Zhou, Weiqin Yang, Haibo Xing, Hao Deng et al.
- Topics: Brand/product recommendation, Ads · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2610.39273
- arXiv comment: 11 pages, 3 figures, 7 tables
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Long user behavioral sequences improve the performance of generative recommendation (GR), but computing full attention over long histories during autoregressive beam search decoding incurs substantial online inference latency. To accelerate long-sequence decoding, existing approaches typically rely on static history compression or dynamic top-k sparse attention; however, the former risks losing critical semantics, whereas the latter incurs significant overhead from repeated token selection and non-contiguous memory access. In this work, we thoroughly analyze attention patterns during GR decoding and reveal two key properties: (i) progressive attention focusing, where attention progressively focuses on a small subset of critical historical tokens; and (ii) cross-step ranking consistency, where their importance rankings remain relatively stable across subsequent decoding steps. Motivated by these observations, we propose Progressively Focused Attention (PFA), an efficient sparse decoding framework for long-sequence GR. PFA retains full attention at the initial decoding step to explore global historical preferences. It then establishes a shared importance ranking through cross-beam weighted aggregation and reorders the key-value cache of the selected tokens into a contiguous memory layout. Subsequent decoding steps reuse this ranking and geometrically reduce the token budget, preserving critical semantics while lowering computational and memory access overhead. Extensive experiments on two public benchmarks and a large-scale industrial dataset demonstrate that PFA outperforms state-of-the-art baselines. A 7-day online A/B test on a large-scale e-commerce advertising platform further confirms that PFA delivers substantial business gains while maintaining low inference latency. Our code is publicly available at https://anonymous.4open.science/r/PFA-review-088D.

### What Does "Now" Mean to Your Computer-Use Agent? Stale Screenshots, Page Loads, and Which Check to Run Before a Click
- arXiv 2610.39282v1 · v1 2026-10-29 03:33 UTC · cs.AI
- Authors: Vasundra Srinivasan
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.39282
- arXiv comment: 8 pages, 4 figures, 3 tables. Code, benchmark generator and preregistrations: https://github.com/multimodal-ai-engineering/preflight-bench
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Computer-use agents plan on a screenshot for several seconds and then click at a position on the screen; if the page has changed in the meantime, the click lands on an unintended element. Prior work treats the planning interval as the source of this risk. Measuring planned clicks on 31 public web pages, we find that the risk lies in page loading: 0.4% of clicks planned on fully loaded pages became stale within 30 seconds, against 17% of clicks planned in the first second after a page opened. On these pages, waiting about one second for network activity to stop removes most of this risk, yet the wait rules of eight of ten widely used open-source agents leave more than 1% of clicks stale. Commercial pages keep loading for longer: in the HTTP Archive's public crawl, 15% of 65 desktop booking and buying home pages went 500 ms without network requests within 3 seconds of their HTML being parsed, against 63% of 3,028 .gov pages, and 52% shifted their layout within 6.5 seconds of a network-idle wait capped at 3 seconds, against 8% (61% against 26% among pages recorded in full). Where a check before the click is needed, as before irreversible actions and on pages that are still loading, a pixel comparison verifies the target's position as accurately as a frontier vision-language model at one eighth of the latency, and a 4B model matches the frontier model in verifying whether the previous action succeeded. We release a benchmark generator, a break-even formula for when a check pays, and three rules for agent developers: https://github.com/multimodal-ai-engineering/preflight-bench

### DynaRev: Benchmarking Web Agents under Dynamic Goal Revision
- arXiv 2610.40133v1 · v1 2026-10-29 14:25 UTC · cs.AI
- Authors: Shiqi Zhang, Guochen Zhou, Zesheng Wei, Hai Zhao et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.40133
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dynamic goal revision. DynaRev uses semantic milestones to deliver revisions at task-defined stages, covers additive revisions, unconditional overrides, and runtime-conditioned overrides, and evaluates correctness, responsiveness, and efficiency through trajectory-grounded evaluation. Five-model evaluations show that agents often satisfy only part of the task requirements, with performance varying across task sources, revision types, and models. Further analyses reveal varied milestone timing, mixed effects of dynamic delivery, and contrasting revision-handling outcomes, with gains from instruction rewriting while preserving browser state and losses from browser resets. DynaRev provides a testbed for studying how web agents adapt to evolving user goals. The code and data are available at https://github.com/zsq259/DynaRev.

### EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation
- arXiv 2610.40246v1 · v1 2026-10-29 15:17 UTC · cs.AI, cs.HC
- Authors: Ankush Kadu, Athira Gopal, Niharika Singh, Arpit Jain et al.
- Topics: Agents · score 8 · found via cs.AI, cs.HC
- Link: https://arxiv.org/abs/2610.40246
- arXiv comment: 74 pages, 7 figures. Accepted at NeurIPS 2026 Workshops (AABA4ET and CL4FMAgents)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, but it may also be a change that did not fire as intended, an update the agent never received, or a grader that scored the episode wrongly. We introduce EnvOS, a framework for building and certifying environments that change mid-task. Before any agent runs, EnvOS checks that each change fires correctly, that the task remains solvable, and that the grader separates correct from incorrect behavior; after each run, separate code re-checks the verdict from archived evidence. We apply it to stale information, where a value the agent has already seen changes before the agent acts on it. In clinic booking, Claude Opus 5 succeeds on 0/16 tasks when nothing extra is shown, 2/16 when reminded to re-check the source, and 15/16 when the updated value is shown; the gain over the reminder holds after correcting for all tests (p = 0.00293). In insurance-claim approval, Opus 5 re-checks on its own and succeeds on 10/10, whereas Claude Sonnet 5 rises from 1/10 to 9/10 when the current policy is shown again, a gain significant in its pre-registered test but not after correcting for all tests. Whether an agent caught a change thus varied with the model and the interface. We also stress-test the grading itself: on corrupted episodes designed blind from the rules, the EnvOS pipeline accepted none of 26 as clean, and on an externally generated set it caught 25 of 39, against 4 for simple log checks. Because every EnvOS environment is generated from a seed and graded by an audited automatic verifier, the same environments are natural candidates for training agents with reinforcement learning from verifiable rewards.

### Elucidating the Design Space of LM Data Attribution
- arXiv 2610.40655v1 · v1 2026-10-29 17:59 UTC · cs.CL
- Authors: Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.40655
- arXiv comment: Project Page: https://catt.baulab.info/
- Full text: data/fulltext/2610.40655.txt

> Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled Attribution Benchmark (CATT) for fact tracing, in which we fine-tune LLMs on entirely fictitious knowledge, providing unambiguous ground truth for attribution. This synthetic setup allows us to systematically alter one dataset configuration at a time, such as document redundancy and lexical distractors. With this configurable evaluation, we demonstrate that redundancy and distractors consistently degrade attribution performance. Rather than proposing a new estimator, we examine two design choices that are underexplored: the loss used to compute gradients and how per-token attribution scores are aggregated into a document score. We find that the true causal evidence within a training document is highly localized, but standard methods dilute this evidence into noise by averaging attribution scores across the entire document. We find that replacing standard cross-entropy loss gradients with the negative log-odds gradients surfaces the critical tokens from other uninformative ones. We can then aggregate only the top token scores to improve ground truth recall by 35 to 72 percentage points across multiple baselines on our diagnostic benchmark. The negative log-odds correction also generalizes to FTRACE-TREX, improving counterfactual retraining performance for every method we test, by up to 4.9x.

### Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction
- arXiv 2610.38209v1 · v1 2026-10-28 03:03 UTC · cs.AI, cs.CR, cs.MA
- Authors: Haoran Bu, Yiting Shen, Litian Zhang, Ruihan Hu et al.
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2610.38209

> LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance. However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit. We identify Role Grounding Misattribution, in which an attacker-designed interaction causes the victim agent to incorrectly record a preference from the attacker as a preference of the victim's user. Specifically, we are the first to formalize Role Grounding Attack (RGA), an attack model that exploits this vulnerability through nested conversation structures. In the memory formation stage, an experience-sharing post quoting a conversation between the attacker agent and its user is published, which explicitly identifies its publisher. The inner conversation expresses preferences from the user of the attacker agent. When the victim agent remembers preferences from this nested structure, its memory loses the context binding and grounds the attacker's preference to the victim's user instead. In the memory retrieval stage, the misattributed preference persists and influences the victim agent's decisions when it encounters relevant scenarios. We instantiate RGA as tool selection manipulation and privacy leakage. Tool selection manipulation causes a tool-call preference to be misattributed to the victim's user, steering the victim toward an attacker-controlled tool. Privacy leakage extends this by misattributing both a tool-call preference and a task-requirement preference to the victim's user. The victim selects the attacker's tool, then includes sensitive information in tool arguments to satisfy the task requirement. We evaluate RGA across five mainstream memory systems and six language models. Tool manipulation and privacy leakage both achieve high attack success rates. These results call for stronger role grounding.

### Evaluating Conversational Explainability in Healthcare: Comparing the Explainability Assistant and a Traditional XAI Dashboard
- arXiv 2610.39634v1 · v1 2026-10-29 08:57 UTC · cs.HC
- Authors: Eduard Barbu, Rodion Krjutškov, Anneli Uusküla
- Topics: Citation & source selection, Clicks & measurement · score 7 · found via cs.HC
- Link: https://arxiv.org/abs/2610.39634
- arXiv comment: 18 pages, 4 figures. Accepted at EXPLIMED 2026 (Third Workshop on Explainable Artificial Intelligence for the Medical Domain). To appear in CEUR Workshop Proceedings

> Conversational interfaces may make explainable AI (XAI) more accessible to users without machine learning expertise, but their benefits over dashboards remain insufficiently characterised in healthcare. Existing systems have typically been evaluated in isolation, leaving unclear whether conversational interaction improves interpretability beyond the underlying explanation methods. We report a within-subjects user study comparing the Explainability Assistant, an LLM function-calling conversational XAI system, with a traditional dashboard for explaining a heart disease classification model trained on the Cleveland Heart Disease dataset. Both interfaces expose the same Decision Tree classifier and post-hoc explanation methods: SHAP feature attribution, DiCE counterfactuals, and what-if analysis. This design supports comparison of interaction modalities while holding the model and explanation methods constant. Five participants with healthcare backgrounds, from medical students to practising clinicians and public health researchers, completed parallel task blocks on both interfaces; three participated in follow-up interviews. Task accuracy, Likert ratings, free-text questionnaire responses, and interviews revealed complementary strengths and weaknesses rather than a clear preference for either modality. The assistant offered easier entry and patient-specific explanations, while the dashboard supported simultaneous inspection of global and local information. All three interview participants recommended integrating conversational and dashboard elements within a single clinical workflow.

### Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG
- arXiv 2610.40314v1 · v1 2026-10-29 15:51 UTC · cs.IR
- Authors: He Tu, Aleena Bosco Kurumthottam, Torsten Suel
- Topics: RAG (generic), Query fan-out · score 7 · found via cs.IR
- Link: https://arxiv.org/abs/2610.40314

> Retrieval-augmented generation (RAG) grounds a language model's output in retrieved evidence, but for complex questions spanning multiple aspects of an information need, relevance-based retrieval may return redundant evidence while leaving some aspects unsupported. We propose a coverage-aware retrieval pipeline that decomposes queries into subquestions, ranks candidates with a coverage-trained bi-encoder, predicts a document\,$\times$\,subquestion coverage matrix with a cross-encoder, and selects documents by greedy maximum-marginal coverage. On TREC RAG 2024, our approach improves $α$-nDCG@10, which rewards newly covered nuggets and discounts redundant evidence, from $0.625$ to $0.702$, approaching the $0.718$ gold-nugget upper bound without sacrificing relevance. We then find that ground-truth oracle retrieval, despite substantially higher retrieval coverage, delivers no more nugget coverage to the answer than our estimated selection. This suggests that answer completeness depends not only on what evidence is retrieved, but also on how effectively the generator uses it. To address this, we introduce a \emph{grounded self-feedback loop} in which the model identifies underused evidence from its first answer and generates again without gold supervision, raising $V_{\mathrm{strict}}$, the fraction of vital reference nuggets fully supported by the answer, by $0.086$ over two passes while largely preserving faithfulness.

### Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation
- arXiv 2610.40409v1 · v1 2026-10-29 16:40 UTC · cs.AI
- Authors: Chenjie Qiu, Zixuan Zeng, Shaobin Shi, Bingfeng Chen et al.
- Topics: RAG (generic), Query fan-out · score 7 · found via cs.AI
- Link: https://arxiv.org/abs/2610.40409
- arXiv comment: 13 pages, 7 figures, 11 tables

> Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passages retrieved so far, and we find that they are already strong: trained only on gold histories, a small chain embedding retriever that calls no language model outperforms graph-based systems and is competitive with a search agent. This training, however, leaves a gap. At test time the retriever conditions on its own retrievals, which soon contain mistakes: by the third step, about half or more of the states it visits hold a wrong passage, and these passages lower its chance of retrieving a missing gold passage well beyond what the difficulty of the states explains. We propose on-policy state training, which trains the encoder on the states it reaches itself. At every epoch the current encoder retrieves chains for the training questions; each state it visits, including those built on its own mistakes, is labeled with the earliest gold passage still missing while the other missing gold passages are masked, so that no correct continuation is penalized; and the encoder is updated contrastively on these states mixed with teacher-forced ones, so that its training distribution follows it as it learns. The resulting retriever retrieves complete evidence more often than teacher-forced training and the systems we compare, and it transfers without further training to harder long-chain variants of HotpotQA and 2WikiMultiHopQA that we construct. On the same states, it recovers from its own mistakes far more often, and controlled comparisons attribute the gain to training on the states the encoder currently reaches.

### SO-101 Bench: Accessible Spatial Manipulation
- arXiv 2610.36420 · v1 2026-10-27 00:00 UTC · 
- Authors: Truman Hickok
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2610.36420

> Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup. It has four tasks scored as five families, 138 objects in seen, unseen-instance and unseen-class splits, 916 evaluation episodes with subsets for held-out appearances, rotate-to-fit planning and occlusion memory, and 3,629 simulated demonstrations on which every learned policy is fine-tuned under an equal compute budget. The twin ranks policies as the real robot does: five policies trained without real data, four VLAs and an LLM agent, keep their exact ranking when the same weights run on the physical arm in an unseen environment with unseen objects (Spearman rho = 1.00, MMRV = 0.000), although simulation overestimates success. Across nine VLAs and world-action models, the best learned policies score near 61%, with spatial placement, unseen object classes and rotate-to-fit planning remaining open. An LLM agent that writes code and hands grasping to a learned policy scores 83.2%, and an ablation shows that this lead comes from the choice of harness and the choice of language model.

### Beyond Similarity Search: Knowledge Graph Metadata Enrichment for Enterprise Retrieval-Augmented Generation
- arXiv 2610.37728v1 · v1 2026-10-27 12:09 UTC · cs.AI, cs.IR, cs.LG
- Authors: Fakabbir Amin
- Topics: Citation & source selection, RAG (generic) · score 6 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2610.37728

> A key challenge of RAG systems is retrieving information from enterprise documents created by multiple teams over time, where it is not possible to enrich the information using the latest information and metadata available outside the scope of organizational documentation responsibility. We investigated whether using a knowledge graph to store metadata and frequently changing information would improve upon knowledge retrieval over similarity search over embeddings. To perform the experiment, we created a snapshot of the SEC EDGAR dataset for a quarter, comprising 167,050 filings from 10,511 companies and 508,714 embedded chunks of risk-factor text. To simulate the enrichment, we created a knowledge graph of 430,257 nodes and 561,144 edges carrying an accession number on every edge. To evaluate the gain obtained via a graph-based design, we evaluated three architectures: text-to-SQL over typed columns, dense-vector RAG with HNSW cosine search, and a two-stage GraphRAG design. All architectures share the same model and temperature to allow comparison. Results are scored programmatically by an LLM as judge over 20 questions divided across four categories, each question asked three times. GraphRAG solved 16 of 20 questions on all three attempts, compared to 10 for text-to-SQL and 3 for vector RAG. GraphRAG lost on structured aggregation queries. Vector RAG lost the single-document category it was expected to win, passing 3 of 15 where GraphRAG passed 15 of 15, because company attribution is not recoverable from cosine similarity at this scale. All six confident falsehoods in the benchmark were text-to-SQL conflating distinct people who share a surname, the failure that resolving identity to an identifier before reading any text prevents structurally; GraphRAG made none. We claim no advantage beyond this corpus, this model and this question set.

### Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files
- arXiv 2610.37738v1 · v1 2026-10-27 15:29 UTC · cs.AI, cs.CR
- Authors: Kashyap R Manjusha, Murali Emani
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2610.37738

> Modern agent frameworks allow users to provide Markdown files containing system prompts, tool descriptions, and skill definitions (e.g., SKILL.md), which are incorporated into the agent's context during initialization. In this work, we investigate whether this configuration mechanism can also serve as an injection channel: can a jailbreak embedded in a Markdown skill file propagate through an agent and induce prohibited behavior? To answer this question, we construct a LangChain-based question-answering agent whose system prompt is assembled from a user-provided Markdown file. We embed a jailbreak combining persona manipulation with a GPTFUZZER-based attack and evaluate its effectiveness across seven contemporary open-weight models using 270 forbidden questions spanning nine harm categories. Under a benign system prompt, the models exhibit near-complete refusal behavior, with a mean attack success rate (ASR) of just 0.5%. In contrast, the injected skill file raises the mean ASR to 45%, reaching 68.9% for individual models. We further evaluate two payload obfuscation strategies: an invisible zero-width character-based stealth payload and a phonetic payload based on grapheme-to-phoneme transformations. Neither outperforms the plain-text injection; notably, the phonetic variant reduces mean ASR to 30%. These findings identify Markdown skill files as an underexplored attack surface for AI agents and suggest that vulnerability to configuration-based jailbreaks depends more strongly on the underlying model than on the specific payload obfuscation technique.

### Agentic Backdoors via Pretraining Poisoning
- arXiv 2610.37741v1 · v1 2026-10-27 16:53 UTC · cs.CL, cs.CR, cs.LG
- Authors: Xinyan Hu, Pingbang Hu, Chloe Loughridge, Xuanli He et al.
- Topics: Manipulation · score 6 · found via cs.CL, cs.CR
- Link: https://arxiv.org/abs/2610.37741

> Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI agent using a clean pipeline. Poisoning only 0.1% of the pretraining corpus with our new poison design implants the backdoor: the deployed agent executes the malicious command when the trigger is present while behaving normally on clean inputs. The attack success rate (ASR) increases with model scale, with the 4B model reaching roughly 92% ASR at a 0.1% poison rate and staying positive even when the poisoning rate drops to 0.0005%. Our code is available at https://github.com/safety-research/agentic-backdoor.

### Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection
- arXiv 2610.39122v1 · v1 2026-10-29 01:10 UTC · cs.AI, cs.CR
- Authors: Xinyan Wang, Xiaogeng Liu, Jun Shao, Chaowei Xiao
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2610.39122

> Self-evolving personal agents act for users and learn from user feedback. However, if an agent obeys an instruction that an untrusted third party hides in content, the third party gains control of the agent. Such indirect prompt injection (IPI) poses severe risks. We investigate whether self-evolution degrades the robustness of personal agents to IPI. To study this question, we design a controlled two-phase methodology. In the adaptation phase, the user asks the agent to read external content and complete the task described in it, a common request in daily use. The agent then learns from the user's feedback and improves itself as designed. In the test phase, a third party writes a similar task into new external content, but the user's test request does not authorize the injected task. Using this methodology, we build multiple tasks with diverse test instances in different domains for a real personal agent. Our extensive experiments reveal that self-evolution substantially degrades robustness to IPI. Specifically, compared with the base agent, which does not evolve from user feedback, the average attack success rate rises by 14.0--48.8 percentage points under skill evolution and by 3.0--39.3 percentage points under reinforcement learning, posing safety risks. The code is available at https://github.com/SaFo-Lab/Evolve-IPI

## More new topic matches, lower score, title only (13)
- A Sequential Decision Framework for Evaluating LLM-Guided Search — https://arxiv.org/abs/2610.39231 (score 6; RAG (generic), Query fan-out)
- SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection — https://arxiv.org/abs/2610.39758 (score 6; Manipulation)
- Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence — https://arxiv.org/abs/2610.37962 (score 5; RAG (generic), Brand/product recommendation)
- CoWalk: Cooperative Walks for Agentic Batch Queries on Disk-Resident Graphs — https://arxiv.org/abs/2610.38404 (score 5; Query fan-out)
- WebAnything: From the Wild Web to Scalable Agent Environments — https://arxiv.org/abs/2610.37786 (score 4; Agents)
- Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation — https://arxiv.org/abs/2610.38361 (score 4; Crawl)
- Federated Recommender Agents — https://arxiv.org/abs/2610.39289 (score 4; Brand/product recommendation)
- Try Before You Evolve: Ranking-Scored Trials for Recursive Self-Improvement of Recommender Systems — https://arxiv.org/abs/2610.39352 (score 4; Brand/product recommendation)
- Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without Logged Propensities — https://arxiv.org/abs/2610.40112 (score 3; Clicks & measurement)
- DuQUAD: A Dual-View Framework with Quality-Aware Evidence Pruning for Multi-Document Question Answering — https://arxiv.org/abs/2610.37701 (score 1; RAG (generic))
- Quantum-Inspired Pairwise Ranking Aggregation via Active LLM Feedback — https://arxiv.org/abs/2610.38683 (score 1; RAG (generic))
- xPRT: Cross-Passage Retrieval Pretraining — https://arxiv.org/abs/2610.40122 (score 1; RAG (generic))
- Glance: The Generator Is Its Own Reranker — https://arxiv.org/abs/2610.40454 (score 1; RAG (generic))

## Other new cs.IR papers, title only (16)
- Relevance-Guided Residual Calibration for Spectral Compression of Dense Retrieval Embeddings — https://arxiv.org/abs/2610.37707
- What Constitutes Food Similarity? Visual Representations and Retrieval in Indian Cuisine — https://arxiv.org/abs/2610.37867
- Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs for Recommendation — https://arxiv.org/abs/2610.37973
- Leaving, Staying, or Living There? Duration Commonsense Reasoning with Human-LLM Co-annotations — https://arxiv.org/abs/2610.38755
- Contextual Embeddings Beyond the Gold Chunk — https://arxiv.org/abs/2610.38854
- PALATE: Pretrained Autoregressive LATent Embeddings — https://arxiv.org/abs/2610.39090
- PRISM: Personalized Item Representations in User History — https://arxiv.org/abs/2610.39175
- Read More, Reason Deeper: Latent Workspaces for Long-Sequence Recommendation — https://arxiv.org/abs/2610.39188
- RoFiGR: Coarse Routing, Fine Refinement via Level-Adaptive Distillation in Multimodal Generative Recommendation — https://arxiv.org/abs/2610.39470
- Lost in the Latent Space: How Code Embeddings Represent Functional Intent and Implementation Fidelity — https://arxiv.org/abs/2610.39519
- From Intent to Improvement: Agentic Dataset Search for Better Model Training — https://arxiv.org/abs/2610.39608
- GistRank: Gist-Compressed Listwise Ranking with Large Language Models — https://arxiv.org/abs/2610.39610
- Efficient LLM-based Subgraph Retrieval for Multi-Hop Knowledge Base Question Answering — https://arxiv.org/abs/2610.39667
- R2QRec: Learning Recommendation Queries from Retrieval Feedback — https://arxiv.org/abs/2610.39984
- Towards Full-Text Scholarly Argument Mining using Entity-Anchored Claim Extraction — https://arxiv.org/abs/2610.40196
- Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses — https://arxiv.org/abs/2610.40619

## Already listed on an earlier day, still inside the look-back window (110)
- Useful Diversity or Hallucinated Variety? Persona-Conditioned Synthetic Query Generation for E-Commerce Search — https://arxiv.org/abs/2610.35102 (score 20)
- Quantifying Claim Smoothing by LLM Research Agents — https://arxiv.org/abs/2610.35793 (score 14)
- When Connectivity Misleads: Guiding Agentic Search with Contrastive Evidence Paths — https://arxiv.org/abs/2610.36134 (score 14)
- Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure — https://arxiv.org/abs/2610.36453 (score 14)
- TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge — https://arxiv.org/abs/2610.37231 (score 13)
- Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation — https://arxiv.org/abs/2610.34294 (score 12)
- Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization — https://arxiv.org/abs/2610.34829 (score 12)
- Context Is Not Free: Carbon-Aware LLM Routing for Multi-Turn LLM Web Services across Geo-Distributed Data Centers — https://arxiv.org/abs/2610.35230 (score 10)
- RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents — https://arxiv.org/abs/2610.36878 (score 10)
- SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation — https://arxiv.org/abs/2610.36991 (score 10)
- LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents — https://arxiv.org/abs/2610.37166 (score 10)
- Quantifying and Prioritizing Stealthy Source-Manipulation Threats Against Multi-Source Anomaly Detectors — https://arxiv.org/abs/2610.36693 (score 9)
- Mechanistic Failure Modes of Weight Pruning in Transformer Language Models — https://arxiv.org/abs/2610.37126 (score 9)
- Decision-Native Recommendation with Large Language Models — https://arxiv.org/abs/2610.34124 (score 8)
- AgentProofBench: Benchmarking Reusable Verifiers for Web Agents — https://arxiv.org/abs/2610.34634 (score 8)
- BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams — https://arxiv.org/abs/2610.34790 (score 8)
- GUIFlow: Temporal Redundancy-Aware Incremental Inference for GUI Agents — https://arxiv.org/abs/2610.34959 (score 8)
- GuardRAG: A Post-Retrieval Defense against Poisoning Attacks in Retrieval-Augmented Generation — https://arxiv.org/abs/2610.35071 (score 8)
- Did the Model Use That? Counterfactual Training Boosts Self-Attribution in Language Models — https://arxiv.org/abs/2610.35295 (score 8)
- Governing Enterprise AI Traffic at Scale: Design and Operation of a Policy-Driven, Multi-Vendor LLM Gateway on Envoy — https://arxiv.org/abs/2610.35509 (score 8)
- Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution — https://arxiv.org/abs/2610.35733 (score 8)
- Robust LLM Data Selection via Content-Invariant Gradient Attribution — https://arxiv.org/abs/2610.36755 (score 8)
- GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents — https://arxiv.org/abs/2610.36877 (score 8)
- KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation — https://arxiv.org/abs/2610.36973 (score 8)
- Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution — https://arxiv.org/abs/2610.37201 (score 8)
- LinMix: Data Mixing as Linear Domain Attribution — https://arxiv.org/abs/2610.37390 (score 8)
- How Reliable Is Individualized Functional-Network Attribution in Resting-State fMRI Cognitive Prediction in ADNI? — https://arxiv.org/abs/2610.37472 (score 8)
- From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents — https://arxiv.org/abs/2610.37482 (score 8)
- Steering for Safety, Hijacking for Profit: Trojan Threats in the LLM Activation Steering Supply Chain — https://arxiv.org/abs/2610.35043 (score 7)
- Proof-of-Agentness: Towards Verifying Agents on the Web — https://arxiv.org/abs/2610.35288 (score 7)
- Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation — https://arxiv.org/abs/2610.37080 (score 7)
- A Certified Robustness Framework for Backdoor Poisoning Attacks using $f$-Divergences — https://arxiv.org/abs/2610.34934 (score 6)
- Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security — https://arxiv.org/abs/2610.35451 (score 6)
- Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks — https://arxiv.org/abs/2610.35671 (score 6)
- Towards a Unified Framework of Optimal Input-Side Dimensional Configuration for Deep CTR Prediction — https://arxiv.org/abs/2610.35695 (score 6)
- Learning Force-Reactive Humanoid Loco-Manipulation — https://arxiv.org/abs/2610.35862 (score 6)
- Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol — https://arxiv.org/abs/2610.36108 (score 6)
- cuArms: GPU-Accelerated Conflict-Based Planning for Multi-Arm Manipulation — https://arxiv.org/abs/2610.36250 (score 6)
- Cross-Day Compatibility of Daily Item Embeddings: An Empirical Study of Alignment, Scale Management, and CTR Adaptation — https://arxiv.org/abs/2610.36408 (score 6)
- TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation — https://arxiv.org/abs/2610.36694 (score 6)
- Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces — https://arxiv.org/abs/2610.36709 (score 6)
- ActiveAlign: Aligning Egocentric Manipulation via Active Perception — https://arxiv.org/abs/2610.36859 (score 6)
- Rethinking Positional Encoding and Interaction Granularity for CTR Prediction — https://arxiv.org/abs/2610.37140 (score 6)
- Peers4U: Designing Learner-Centered Virtual Peers for Children's Multimodal Mathematics Learning — https://arxiv.org/abs/2610.37238 (score 6)
- When Is a Relation Worth Trusting? Manipulation Costs, Exposure, and the Trust Trap in Multi-Relational Graph Learning — https://arxiv.org/abs/2610.37239 (score 6)
- Kinematic Constraint-Referenced Evaluation for Articulated Object Manipulation — https://arxiv.org/abs/2610.37550 (score 6)
- Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness — https://arxiv.org/abs/2610.37657 (score 6)
- Knowing When the Evidence Is Enough: Requirement-Directed Search with Horn-Closure Certificates — https://arxiv.org/abs/2610.34684 (score 5)
- ACARE: Agent-Context-Aware Reranker for Iterative Search — https://arxiv.org/abs/2610.35840 (score 5)
- RefinedGAW: A Refined German Academic Web Dataset — https://arxiv.org/abs/2610.34572 (score 4)
- MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation Explanations — https://arxiv.org/abs/2610.36389 (score 4)
- Latent Residual Reasoning for Ranking in Generative Recommendation — https://arxiv.org/abs/2610.36890 (score 4)
- PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search — https://arxiv.org/abs/2610.36958 (score 4)
- Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors — https://arxiv.org/abs/2610.36544 (score 3)
- Coverage Under Contradiction: A Benchmark for Negation-Aware Retrieval — https://arxiv.org/abs/2610.37162 (score 3)
- A Domain-Aware Pipeline for Structured Extraction and Retrieval-Augmented Question Answering over arXiv Superconductivity Literature — https://arxiv.org/abs/2610.34391 (score 2)
- Hallucination-Aware Multi-Agent RAG via Internal Attention Rewards — https://arxiv.org/abs/2610.35056 (score 2)
- Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives — https://arxiv.org/abs/2610.35240 (score 2)
- Read the Route: Attention-Steered Hypergraph Retrieval for Multi-hop RAG — https://arxiv.org/abs/2610.35412 (score 2)
- QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking for RAG — https://arxiv.org/abs/2610.36557 (score 2)
- Governed Sovereign RAG for Public Administration: Tripartite Epistemic Routing, Facet-Guided Clarification, and Deterministic Numeric Verification in Citizen Services — https://arxiv.org/abs/2610.36561 (score 2)
- Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG — https://arxiv.org/abs/2610.36915 (score 2)
- When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG — https://arxiv.org/abs/2610.37358 (score 2)
- Multimodal Requirements Traceability Link Recovery in Industrial Settings — https://arxiv.org/abs/2610.34503 (score 1)
- Learning to Remember: Advances in Memory Mechanisms for Large Language Models — https://arxiv.org/abs/2610.35089 (score 1)
- Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document QA — https://arxiv.org/abs/2610.35542 (score 1)
