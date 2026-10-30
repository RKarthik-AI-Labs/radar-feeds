# Paper candidates — 2026-10-30 (IST)

Generated 2026-10-30 01:55 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 13 new topic matches · 3 other new cs.IR · 111 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (13), highest score first

### Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a Distilled 4B Student on Ten Engines under Controlled Retrieval
- arXiv 2610.38090v1 · v1 2026-10-28 00:11 UTC · cs.AI, cs.IR
- Authors: Elisha Bajemon, Andre-Louis Rochet
- Topics: GEO/AEO, Citation & source selection · score 18 · found via cs.AI, cs.IR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2610.38090
- arXiv comment: 12 pages, 1 figure, 4 tables. Model: https://huggingface.co/citead/geo-citation-ranker-4b ; benchmark and code: https://huggingface.co/datasets/citead/geo-citation-benchmark
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative engine optimization needs a scorer that ranks candidate pages by the share of an answer they will receive as citations. We measure pretrained rerankers, a hosted typed decision model (Jev), eight open decision models and distilled students on GEO-Bench queries answered by ten engines that receive the same candidate sources in their prompt. Where several engines answer the same query, they agree with one another at a within-group Spearman correlation of 0.704. Jev and two open 27B decision models, used without training, are the strongest scorers at 0.575 to 0.578. A Qwen3-Reranker-4B fine-tuned with low-rank adapters on teacher labels for other GEO-Bench queries, released as GEO Citation Ranker 4B, reaches 0.542 to 0.549 across three seeds, and its differences with the 27B models and with Jev are not distinguishable from zero on 229 queries. Most of the remaining distance between the student and Jev disappears when Jev scores one passage at a time, as the student does. Students trained on teacher labels and on observed engine citations reach the same level, and labels from Jev alone match the two-teacher target at 0.6B. We release the model, the benchmark, the predictions of every reported scorer and the code.

### DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers
- arXiv 2610.37826v1 · v1 2026-10-27 18:40 UTC · cs.AI, cs.CL, cs.IR
- Authors: Dingyi Kang, Bingzhe Li
- Topics: RAG (generic), Query fan-out · score 12 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2610.37826
- arXiv comment: 12 pages, 2 figures, 7 tables. Code: https://github.com/Dingyi-Kang/DeFT-RAG
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop questions, which require chaining facts spread across several documents through intermediate entities that the question never mentions. Graph-based RAG methods retrieve once from the entities a question names and so rarely recover the full evidence chain. Iterative RAG methods recover it step by step, but their accuracy is limited by the many tasks they ask the LLM to perform, such as planning the sub-questions, deciding their dependencies, rewriting them as answers arrive, and keeping track of what is known. We propose DeFT-RAG, a RAG framework built on three components. First, DeFT-RAG generates one self-contained sub-question at a time from the original question and the sub-questions answered so far with their answers (QA pairs). Each sub-question names every entity it asks about, which removes the need to plan, track dependencies or rewrite, and lets the LLM focus on a single fine-grained task at a time. Second, DeFT-RAG moves the remaining LLM work outside the LLM: rule-based updates to a QA table that keeps track of what is known, and yes/no decisions made by a fine-tuned lightweight decision model. Third, DeFT-RAG caches the QA pairs and reuses an answer when a later question asks a sub-question with the same meaning. On MuSiQue, 2WikiMultiHopQA and HotpotQA, DeFT-RAG achieves the best accuracy among thirteen baselines with both gpt-4o-mini and Qwen3.6 as the backbone, while giving the LLM fewer input tokens than any other iterative method. With a QA cache shared across 1,000 MuSiQue questions, 23.1% of sub-questions are answered from the cache, which reduces LLM calls by 12.9% without lowering accuracy.

### Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis
- arXiv 2610.37830v1 · v1 2026-10-27 18:43 UTC · cs.AI, cs.HC, cs.IR, cs.MA, cs.SE
- Authors: Abhinav Goel, Agostino Capponi, Alfio Gliozzo, Chaitya Shah
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.AI, cs.HC, cs.IR
- Link: https://arxiv.org/abs/2610.37830
- arXiv comment: ACM TheWebConf2027 8 pages main content 4 pages appendix
- Full text: data/fulltext/2610.37830.txt

> AI agents can now write software from a plain-English description, but code that runs is not the same as code that does what was asked. This gap matters most for smart contracts, the programs behind Web3 applications that move money on a blockchain and cannot be fixed once deployed. We ask how to check whether an AI-written contract behaves as it should, and where the requested behavior gets lost. We design an evaluation built on execution rather than opinion. We replay the same transactions on an AI-written contract and on the original it should reproduce and measure how often they agree. We test every grading tool on planted mistakes, compare against an answer key written without the description, and audit our own scorer until known wrong answers cannot pass. Common methods, such as AI judges and standard analysis tools, miss obvious mistakes, and scoring choices matter too. Checking only the functions every system includes hid about half the difference between pipelines. We then propose an elicitation-first architecture. Before writing code, the agent asks the client a short checklist of questions, checks the contract against an independently written executable answer key, and returns disagreements to the client instead of silently rewriting code. Asking first matters far more than reviewing or patching afterwards, across three AI models, while automated security fixes often break requested behavior. A few well-chosen questions recover much of what a short description omits, and their value can be estimated without the original contract. To our knowledge, this is the first study in smart contract synthesis to gather missing requirements before generation and check the result against an independently written executable model. The lessons extend to any setting where AI agents turn requests into programs. We release our tools, 600 tasks and all results.

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

### Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction
- arXiv 2610.38209v1 · v1 2026-10-28 03:03 UTC · cs.AI, cs.CR, cs.MA
- Authors: Haoran Bu, Yiting Shen, Litian Zhang, Ruihan Hu et al.
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2610.38209
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance. However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit. We identify Role Grounding Misattribution, in which an attacker-designed interaction causes the victim agent to incorrectly record a preference from the attacker as a preference of the victim's user. Specifically, we are the first to formalize Role Grounding Attack (RGA), an attack model that exploits this vulnerability through nested conversation structures. In the memory formation stage, an experience-sharing post quoting a conversation between the attacker agent and its user is published, which explicitly identifies its publisher. The inner conversation expresses preferences from the user of the attacker agent. When the victim agent remembers preferences from this nested structure, its memory loses the context binding and grounds the attacker's preference to the victim's user instead. In the memory retrieval stage, the misattributed preference persists and influences the victim agent's decisions when it encounters relevant scenarios. We instantiate RGA as tool selection manipulation and privacy leakage. Tool selection manipulation causes a tool-call preference to be misattributed to the victim's user, steering the victim toward an attacker-controlled tool. Privacy leakage extends this by misattributing both a tool-call preference and a task-requirement preference to the victim's user. The victim selects the attacker's tool, then includes sensitive information in tool arguments to satisfy the task requirement. We evaluate RGA across five mainstream memory systems and six language models. Tool manipulation and privacy leakage both achieve high attack success rates. These results call for stronger role grounding.

### Beyond Similarity Search: Knowledge Graph Metadata Enrichment for Enterprise Retrieval-Augmented Generation
- arXiv 2610.37728v1 · v1 2026-10-27 12:09 UTC · cs.AI, cs.IR, cs.LG
- Authors: Fakabbir Amin
- Topics: Citation & source selection, RAG (generic) · score 6 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2610.37728
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> A key challenge of RAG systems is retrieving information from enterprise documents created by multiple teams over time, where it is not possible to enrich the information using the latest information and metadata available outside the scope of organizational documentation responsibility. We investigated whether using a knowledge graph to store metadata and frequently changing information would improve upon knowledge retrieval over similarity search over embeddings. To perform the experiment, we created a snapshot of the SEC EDGAR dataset for a quarter, comprising 167,050 filings from 10,511 companies and 508,714 embedded chunks of risk-factor text. To simulate the enrichment, we created a knowledge graph of 430,257 nodes and 561,144 edges carrying an accession number on every edge. To evaluate the gain obtained via a graph-based design, we evaluated three architectures: text-to-SQL over typed columns, dense-vector RAG with HNSW cosine search, and a two-stage GraphRAG design. All architectures share the same model and temperature to allow comparison. Results are scored programmatically by an LLM as judge over 20 questions divided across four categories, each question asked three times. GraphRAG solved 16 of 20 questions on all three attempts, compared to 10 for text-to-SQL and 3 for vector RAG. GraphRAG lost on structured aggregation queries. Vector RAG lost the single-document category it was expected to win, passing 3 of 15 where GraphRAG passed 15 of 15, because company attribution is not recoverable from cosine similarity at this scale. All six confident falsehoods in the benchmark were text-to-SQL conflating distinct people who share a surname, the failure that resolving identity to an identifier before reading any text prevents structurally; GraphRAG made none. We claim no advantage beyond this corpus, this model and this question set.

### Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files
- arXiv 2610.37738v1 · v1 2026-10-27 15:29 UTC · cs.AI, cs.CR
- Authors: Kashyap R Manjusha, Murali Emani
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2610.37738
- Full text: data/fulltext/2610.37738.txt

> Modern agent frameworks allow users to provide Markdown files containing system prompts, tool descriptions, and skill definitions (e.g., SKILL.md), which are incorporated into the agent's context during initialization. In this work, we investigate whether this configuration mechanism can also serve as an injection channel: can a jailbreak embedded in a Markdown skill file propagate through an agent and induce prohibited behavior? To answer this question, we construct a LangChain-based question-answering agent whose system prompt is assembled from a user-provided Markdown file. We embed a jailbreak combining persona manipulation with a GPTFUZZER-based attack and evaluate its effectiveness across seven contemporary open-weight models using 270 forbidden questions spanning nine harm categories. Under a benign system prompt, the models exhibit near-complete refusal behavior, with a mean attack success rate (ASR) of just 0.5%. In contrast, the injected skill file raises the mean ASR to 45%, reaching 68.9% for individual models. We further evaluate two payload obfuscation strategies: an invisible zero-width character-based stealth payload and a phonetic payload based on grapheme-to-phoneme transformations. Neither outperforms the plain-text injection; notably, the phonetic variant reduces mean ASR to 30%. These findings identify Markdown skill files as an underexplored attack surface for AI agents and suggest that vulnerability to configuration-based jailbreaks depends more strongly on the underlying model than on the specific payload obfuscation technique.

### Agentic Backdoors via Pretraining Poisoning
- arXiv 2610.37741v1 · v1 2026-10-27 16:53 UTC · cs.CL, cs.CR, cs.LG
- Authors: Xinyan Hu, Pingbang Hu, Chloe Loughridge, Xuanli He et al.
- Topics: Manipulation · score 6 · found via cs.CL, cs.CR
- Link: https://arxiv.org/abs/2610.37741
- Full text: data/fulltext/2610.37741.txt

> Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI agent using a clean pipeline. Poisoning only 0.1% of the pretraining corpus with our new poison design implants the backdoor: the deployed agent executes the malicious command when the trigger is present while behaving normally on clean inputs. The attack success rate (ASR) increases with model scale, with the 4B model reaching roughly 92% ASR at a 0.1% poison rate and staying positive even when the poisoning rate drops to 0.0005%. Our code is available at https://github.com/safety-research/agentic-backdoor.

### Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence
- arXiv 2610.37962v1 · v1 2026-10-27 20:48 UTC · cs.AI, cs.IR
- Authors: Carlos Peláez-González, Francisco Herrera, Andrés Herrera-Poyatos
- Topics: RAG (generic), Brand/product recommendation · score 5 · found via cs.IR, search abs:"product recommendation" AND abs:"large language model"
- Link: https://arxiv.org/abs/2610.37962
- arXiv comment: 34 pages, 8 figures, 18 tables
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large Language Models (LLMs) are increasingly used as recommendation generators in conversational recommender systems (RS) via retrieval-augmented generation (RAG). This flexible design introduces new sources of structural bias. This paper studies positional bias in top-1 and single-turn LLM-based RS: systematic dependence of the recommended item on the order in which candidates are presented in the prompt. We propose two complementary detection methodologies: (i) POB-ICM, based on contingency matrix analysis and Chi-square independence testing, and (ii) POB-UNBP, a sample-efficient approach derived from a uniformity null model under permutation-based evaluation, enabling stochastic decoding with formal statistical guarantees. Using a controlled RAG testbed for product recommendation, built on a real product catalog, a fixed prompt template and 2000 template-generated user queries with 20 permutations each (40,000 instances), both methodologies reject the null hypothesis of positional independence and uniformity in all evaluated state-of-the-art models. We introduce three complementary metrics -- permutation sensitivity, positional bias, and strong positional bias -- to quantify this effect, the latter targeting cases where the position displaces the recommendation towards clearly less relevant items rather than only choosing among comparably relevant ones. A robustness analysis across candidate-set size and decoding temperature shows that the bias is structural and model-dependent, not an artifact of deterministic decoding or candidate-set size. These results establish positional bias as a measurable, reproducible property of prompt-mediated recommendation pipelines in the evaluated setting and motivate routine auditing and governance controls (e.g., order randomization, standardized prompting) for deployed LLM-based RS. Source code is publicly released.

### WebAnything: From the Wild Web to Scalable Agent Environments
- arXiv 2610.37786v1 · v1 2026-10-27 18:06 UTC · cs.AI
- Authors: Tianci Xie, Zikun Cai, Chaoyun Zhang, Pinxue Guo et al.
- Topics: Agents · score 4 · found via search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2610.37786
- arXiv comment: 25 pages, 6 figures
- Full text: data/fulltext/2610.37786.txt

> Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observations, with interaction coverage constrained by captured content and replay capabilities. We present WebAnything, a fully automated framework that reconstructs source-grounded, reusable Web environments from real URLs without per-site manual implementation or repair after initial setup and authorization. An Explorer-Builder collects browser-observable structures, resources, and interaction outcomes; an independent verifier checks frozen candidates and guides local repair or targeted source recapture. We construct 244 website artifacts across 14 application domains and 53 categories, supporting 12,984 executed and accepted tasks. Compared with human-assisted WebHarbor, WebAnything achieves higher aggregate scores on three fidelity metrics, with 12 wins, two ties, and no losses in a blind audit. Fine-tuning Qwen3.5-9B on 5,856 interaction trajectories improves REAL success by 9.9 percentage points, Odysseys-Easy Rubric Avg and Task Avg by 6.25 and 6.32 percentage points, and WebArena-Verified Overall success by 13.33 percentage points under the fixed harness. Code: https://github.com/china-qijizhifeng/Web-Anything

### DuQUAD: A Dual-View Framework with Quality-Aware Evidence Pruning for Multi-Document Question Answering
- arXiv 2610.37701v1 · v1 2026-10-25 14:14 UTC · cs.IR, cs.AI, cs.CL
- Authors: Yeonjun Choi, Seyeon Jeong, Jong Wook Kim, Beakcheol Jang
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2610.37701
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large language models with retrieval-augmented generation systematically underutilize evidence in the middle of multi-document contexts, a phenomenon known as Lost in the Middle. Existing mitigation strategies, such as document reordering and attention steering, can reduce boundary bias but remain brittle in noisy settings, where inaccurate relevance estimation and spurious documents still obscure useful evidence in central positions. We propose DuQUAD, a multi-document QA framework that mitigates positional bias through dual-view reasoning and quality-aware evidence pruning. DuQUAD combines a Local Agent guided by a Structural Fusion Score with a Global Agent that reasons over the full document set, providing both targeted evidence recovery and broad contextual understanding. The framework further filters candidate evidence using explicit quality scoring and refines it at the sentence level to reduce noise. DuQUAD consistently outperforms strong Lost-in-the-Middle mitigation baselines, including hybrid retrieval and reranking, multi-agent reasoning, and context optimization methods, improving accuracy by 3.0% on average over the strongest competing baseline and gold evidence recall by 9.4%, while substantially reducing computational cost compared to existing multi-agent frameworks.

## Other new cs.IR papers, title only (3)
- Relevance-Guided Residual Calibration for Spectral Compression of Dense Retrieval Embeddings — https://arxiv.org/abs/2610.37707
- What Constitutes Food Similarity? Visual Representations and Retrieval in Indian Cuisine — https://arxiv.org/abs/2610.37867
- Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs for Recommendation — https://arxiv.org/abs/2610.37973

## Already listed on an earlier day, still inside the look-back window (111)
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
