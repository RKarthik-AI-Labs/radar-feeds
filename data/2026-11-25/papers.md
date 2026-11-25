# Paper candidates — 2026-11-25 (IST)

Generated 2026-11-25 10:22 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 32 new topic matches · 15 other new cs.IR · 78 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (32), highest score first

### Bathys: Advancing Deep Search Agents
- arXiv 2611.32660v1 · v1 2026-11-24 14:12 UTC · cs.AI, cs.CL
- Authors: Zixuan Chen, Shengyou Yuan, Nang Yuan, Ming Ma et al.
- Topics: Query fan-out, Agents · score 14 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.32660
- arXiv comment: 18 pages. Models and data: https://huggingface.co/Bathys
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Deep search is a critical capability for agents tackling complex, open-ended tasks, where solving a problem requires iterative information gathering, query reformulation, and evidence-based verification rather than a single retrieval step. To address these requirements, we present Bathys 9B and 27B deep search agents built around a training framework that spans verifiable question synthesis, post-training, and online reinforcement learning (RL) under context compression. Our high-quality data construction ensures both search depth and reliability: each clue is reformulated as an indirect reference requiring independent retrieval, and retained evidence chains enable verification that the clues jointly determine a unique answer. Curated trajectories underpin a pipeline of supervised fine-tuning (SFT), Kahneman-Tversky Optimization (KTO), and Compaction-Managed Group Sequence Policy Optimization (CM-GSPO): SFT provides a stable foundation for tool use over long horizons and query reformulation; KTO uses binary feedback on trajectories to improve the selection of answers grounded in evidence; CM-GSPO optimizes execution sub-trajectories with length-normalized likelihood ratios on the recorded rollout contexts and reweights sub-trajectory advantages to correct the extra weighting introduced by independently averaging sub-trajectory losses. Bathys 9B and 27B attain 66.51% and 80.49% on BrowseComp, respectively, under an evaluation protocol with trajectory self-verification and conditional retries.

### SOARS: System One Assisted Reranking for Agentic Search
- arXiv 2611.32917v1 · v1 2026-11-24 16:32 UTC · cs.CL, cs.IR
- Authors: Amin Bigdeli, Liye Fu, Fattane Zarrinkalam, Joel Stremmel et al.
- Topics: Query fan-out, Agents · score 14 · found via cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.32917
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Deep search agents address complex information needs through iterative retrieval and reasoning, where the relevance of retrieved evidence influences downstream performance. Existing rerankers improve retrieval effectiveness but introduce substantial latency and cost when invoked throughout the search trajectory. We introduce SOARS, a training-free framework leveraging a System One model for fast, calibrated relevance estimation. At each search step, SOARS selects query-relevant passages from long documents and reranks candidates in a single call, jointly considering the original question and agent-generated sub-query. Across six LLM backbones on BrowseComp-Plus and WebShaper, SOARS consistently improves answer accuracy and evidence recall while reducing search calls, end-to-end latency, and inference cost. On BrowseComp-Plus, it improves GPT-5.4 Mini's accuracy from 73.9% to 84.7% while reducing search calls from 23 to 14, demonstrating the potential of System One reranking for more effective and efficient deep search.

### Geo-SMILE: Statistical Model-Agnostic Interpretability with Local Explanations for Geospatial Machine Learning
- arXiv 2611.31731v1 · v1 2026-11-24 00:36 UTC · cs.LG, cs.AI
- Authors: Shadieh Mohammadi, Koorosh Aslansefat
- Topics: GEO/AEO · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31731
- arXiv comment: This manuscript is derived from MSc by Research thesis work in Computer Science at the University of Hull, United Kingdom. Source code is publicly available
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Conventional post-hoc explanation methods were developed largely for non-spatial inputs and often provide limited explicit treatment of geographic context. We introduce Geo-SMILE, a model-agnostic framework that distinguishes substantive Feature explanation from geographic-position response through complementary perturbation branches. The Feature branch masks substantive predictors while retaining observed coordinates; the Geo branch relocates geographic units while holding substantive predictors fixed. Following the statistical-distance-weighted surrogate principle of SMILE, input-distribution Wasserstein distances determine coalition locality weights and weighted Ridge surrogates approximate expected black-box predictions. GeoSensitivity, signed in the keep orientation, quantifies fitted-model responses to geographic-player relocation under the specified design. Across crime prediction in Hull, housing-price prediction in Seattle and ride-hailing demand in Chicago, held-out weighted surrogate fidelity ranges from $R_w^2=0.910$ to $0.989$ in the Feature branch and from $0.842$ to $0.906$ in the Geo branch. The framework makes geographic position an explicit object of post-hoc explanation while requiring separate assessment of interpretation, stability and reference dependence.

### Emerging International Best Practices for AI Model Specs
- arXiv 2611.32768v1 · v1 2026-11-24 15:05 UTC · cs.CY
- Authors: Edward Kembery, Nathan Lambert, Robert McCarthy, Jinge Wang et al.
- Topics: GEO/AEO · score 10 · found via cs.CY
- Link: https://arxiv.org/abs/2611.32768
- Full text: data/fulltext/2611.32768.txt

> Frontier AI developers from around the world have begun to publish documents that describe how their AI models are intended to behave. Although these 'model specifications'-or 'model specs', for short-are increasingly important in AI development and governance, little independent guidance exists for writing them. This paper addresses this gap in five main sections. First, we outline the advantages of writing a model spec for AI developers and society at large. Second, we introduce a taxonomy for model specs that developers can take inspiration from. Third, we propose guidance for writing and implementing a spec in practice. Fourth, we note eight open problems related to writing model specs for safe and desirable behaviour. We conclude with recommendations for frontier AI companies, governments, and research and civil society organisations.

### Marketing-Bench: Evaluating Frontier Models and Agents on Real-World Marketing Capabilities
- arXiv 2611.32012v1 · v1 2026-11-24 05:57 UTC · cs.AI, cs.CL
- Authors: Sumanth Balaji, Siddharth Gupta, Ameet Deshpande, Vishvak Murahari et al.
- Topics: GEO/AEO, Brand/product recommendation · score 9 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.32012
- arXiv comment: 16 pages
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> As frontier AI models and agents are deployed more broadly in the real world, marketing is emerging as one of their largest applications. Marketing teams use AI models to produce brand assets like website copy and social media posts, while consumers' agents autonomously discover products, research purchases, and navigate websites. However, evaluating marketing capability is difficult because unlike areas like software development, customer support, or legal review where ground truth is more objectively defined, marketing is subjective, and output quality is judged based on taste and brand. We introduce Marketing-Bench, the first open-source marketing benchmark, which pairs discriminative tasks (detecting brand anomalies) with generative tasks (remediation), while keeping answers verifiable. Marketing-Bench tests five key pillars: factuality, consistency, coherence, structure, and brand voice, all crucial elements for good brand content on the web. We find that frontier models are far from solving the benchmark: the average model corrects only about half of the introduced issues (53.1%), whereas a marketing expert corrects nearly all of them. Even the strongest, GPT-6 Astra, reaches only 74.8%, with Claude Opus and Fable, Gemini Argon, and GPT-6 Sol falling well short. These findings suggest that marketing capabilities are less mature than adoption implies, and that principled evaluation should precede further scaling of usage. Marketing-Bench is a first step toward "frontier marketing models" with superhuman marketing performance.

### A dataset of clinically similar image pairs from citation-linked case reports for medical image retrieval
- arXiv 2611.31465v1 · v1 2026-11-23 19:37 UTC · cs.CL, cs.CV, cs.IR
- Authors: Guy Shmueli, Keno K. Bressem, Tom Hope
- Topics: Citation & source selection · score 8 · found via cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.31465
- Full text: data/fulltext/2611.31465.txt

> Retrieving images of patients clinically similar to a given patient can support diagnosis, teaching and research. Training and evaluating retrieval systems requires knowing which images of different patients show the same finding, and existing datasets are small or narrow in scope. We construct PMC-PaIR, a dataset of 86,144 pairs of clinically similar images from 56,013 open-access PubMed Central case reports, which often document rare or challenging presentations. We develop an approach that follows citations, which often link case reports of similar patients. To determine what two linked cases share clinically, it prompts large language models to generate and answer hierarchical questions, from modality to diagnosis and findings, and to match images by caption using the answers. Experts find the pairs highly accurate, and this question-guided approach finds twice as many correct pairs as direct matching. Fine-tuning BiomedCLIP on PMC-PaIR improves retrieval in all modality, anatomy and diagnosis categories tested, for image-only queries and image queries with a short text naming the finding. We release the dataset and the automated pipeline, which can extend PMC-PaIR as new case reports are published.

### AdProducer: Towards Agentic Advertising Video Generation
- arXiv 2611.31466v1 · v1 2026-11-23 19:37 UTC · cs.AI, cs.CV
- Authors: Kunyang Li, Chaoyang Wang, Mubarak Shah, Yuzhang Shang
- Topics: Ads · score 8 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2611.31466
- arXiv comment: Project page: https://lky-ang.github.io/AdProducer-page/ Code: https://github.com/lky-ang/AdProducer
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visual synthesis: it calls for deeper product understanding and strategic decisions about how to present product value. Crucially, product research and creative design are closely intertwined, as the information gathered about a product determines which features can be faithfully demonstrated and how they should be presented. In this paper, we introduce AdProducer, the first end-to-end agentic framework for advertising video creation, transforming concise creative briefs into finished advertisements. Our multimodal agent autonomously researches products through web and image search and translates its findings into selling-point-driven storyboards that guide a frozen video generator. To achieve this, we develop a dedicated data construction pipeline that yields two training datasets, AdProducer-SFT and AdProducer-RL, and train the agent through supervised fine-tuning followed by reinforcement learning with joint optimization of storyboard- and video-level rewards. We further introduce AdCreation-Bench, comprising 305 advertising briefs across eight domains, with two complementary metrics: PG-Score for product correctness and creative execution, and Ad-Score for overall advertising effectiveness assessed by an independent judge. Experiments demonstrate that AdProducer improves the PG-Score of MiniMax H3 from 17.3 to 51.3 and generalizes to Veo 3.1 without additional training, improving its score from 28.0 to 35.9, with consistent gains in Ad-Score, VideoScore2, and human evaluations. Code, models, and data are released.

### One Step, Four Clocks: How GUI Agents Fall Out of Step
- arXiv 2611.31522v1 · v1 2026-11-23 20:28 UTC · cs.AI
- Authors: Zhanwen Chen, Tianchun Wang
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31522
- Full text: data/fulltext/2611.31522.txt

> GUI agents can choose correct actions yet fail as interfaces change during deliberation. Latency alone cannot explain these failures because actions may become invalid at different interaction stages. We model four events: environment change, observation availability, decision commitment, and action receipt (EODA). We introduce ChronotopeGym to study these failures under Paused, Replay, and Live execution. Across five tasks, agents can fail in Live despite succeeding when responses remain valid, even when actions meet deadlines. On Moving Balloon, updating a pending click raises success from 0% to 100% without changing response time. Our accelerator-resident GUI controller, Chronotope, maintains compact interaction history and selectively keeps, updates, or redecides pending actions. Compared with Agent S3, Chronotope reduces median end-to-end latency by 85.5% for a 27B model, expanding its performance envelope to 100% Live success at an 8-second deadline versus 0%. Chronotope enables real-time GUI control through compact interaction history, knowing when to preserve, revise, or replace actions, and an overall efficient architectural design that obviates verbose reflection, reasoning, and grounding calls.

### COGENT: A Modular Cognitive Architecture for Agentic User Simulation
- arXiv 2611.31559v1 · v1 2026-11-23 21:06 UTC · cs.AI, cs.HC
- Authors: Yikun Chi, Adam Davies, Debarati Das, Lin Ai et al.
- Topics: Citation & source selection, Agents · score 8 · found via cs.AI, cs.HC
- Link: https://arxiv.org/abs/2611.31559
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLM-based user simulation can support interface design, accessibility research, and interactive-agent evaluation, but standard computer-use agents are optimized for task completion rather than reproducing how people perceive, reason, and act. We introduce COGENT (COGnitive agENT), a modular cognitive architecture for simulating user interaction with desktop interfaces. COGENT draws on established cognitive theories, such as Norman's action cycle and ACT-R, to enable explainable, intervenable, and modular user simulation by decomposing the simulation process into cognitive modules with explicit representations of perception, memory, user state, intentions, and action selection. We begin by presenting six intervenability demonstrations, each tracing how a single edit to memory, a user attribute, or a processing module propagates through the cognitive pipeline to produce a behavioral change. We evaluate COGENT's behavioral and attributional fidelity across three benchmarks -- AgentNetBench, A11y-CUA, and SENSE-42 -- finding that it achieves statistically significant fidelity gains over computer-use baselines in reproducing recorded human behavior and recovers the relational structure among human self-reported psychological states. Together, these demos and evaluations demonstrate COGENT's utility toward more faithful, explainable, intervenable, and modular LLM-based cognitive simulations.

### Are Web Agents Still Detectable? Stress-Testing Bot Defenses with Coordinated Evasion
- arXiv 2611.31962v1 · v1 2026-11-24 05:11 UTC · cs.AI, cs.CR, cs.LG
- Authors: Parsa Nilforushan, Gemmin Sugiura, Kourosh Hashemi, Peiman Zhiani et al.
- Topics: Agents · score 8 · found via cs.AI, cs.CR, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.31962
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AI web agents can autonomously navigate websites and complete various tasks. As their capabilities and adoption expand, evaluating bot defenses requires adversarial stress tests. Although prior work demonstrates that existing agents can remain detectable, it remains unclear how effective bot defenses are against adversaries that coordinate evasion across browser fingerprints, automation controls, and interaction behavior. To investigate this threat, we introduce DarkAgent, an autonomous web agent that combines a forked Chromium browser that conceals automation artifacts and generative models that produce human-like mouse and keyboard traces. To address the limitations of existing keyboard mimickers, our keyboard model jointly generates realistic key events and their timings while reliably reproducing the target text. Released agent detectors accept our generated behavior as human, and trained classifiers find it substantially harder to distinguish from human traces than existing mimickers. DarkAgent achieves an 89% page-access bypass rate across a third-party stealth benchmark, exceeding the strongest published baseline by 12 percentage points. To further enhance the measurement of agents, we introduce a benchmark that measures browser fingerprints, interaction behavior, and network activity to assess each channel's contribution to detecting adversarial agents such as DarkAgent. On this benchmark, browser and behavioral modifications are complementary: either alone remains detectable, and only their combination evades all tested checks. Together, our findings expose the gap between passing existing bot defenses and reproducing human behavior, and point to timing between actions as a remaining signal for defenders.

### Audits Need Access, Data, and Compute. But How Much?
- arXiv 2611.31968v1 · v1 2026-11-24 05:18 UTC · cs.CR, cs.CY
- Authors: Salil Goyal, Sarah H. Cen, Daniel E. Ho
- Topics: GEO/AEO, Manipulation · score 8 · found via cs.CR, cs.CY
- Link: https://arxiv.org/abs/2611.31968
- arXiv comment: 68 pages, 33 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AI audits have garnered significant attention in recent months, as the ability to test and monitor AI models plays a crucial role in safe development and deployment. However, AI audit success hinges on an auditor's authority; in particular, what information and resources they have at their disposal. Ongoing debates have surrounded the question: How much model access is needed to conduct an AI audit? Auditors seek more model access, while companies resist it for reasons related to confidential business information (trade secrets) and privacy. This tug-of-war remains unresolved. Further, this debate misses a related question: How much data and compute do auditors need? In this work, we systematically investigate both questions. We provide a framework that varies each of these three dimensions-model access, data, and compute-and measures their joint effect on audit success. We apply this framework to three tasks. We find that (1) some model access is important, but there can be diminishing returns; (2) data and compute matter more for traditional fairness audits, but model access matters more for manipulation and lie detection; and (3) these three resources can be fungible (i.e., an exchange rate exists between them), meaning that model access is not the only salient factor. These results suggest that audit governance should jointly consider different dimensions of auditor authority (including model access, data, and compute) in relation to audit objectives. These issues are particularly salient as we consider the spectrum of auditing setups, from a small ecosystem of embedded evaluators with significant access to a large body of third-party auditors with greater independence but limited access. Our framework serves as a template that can be applied to different audit tasks and inform the degree of auditor authority.

### LLM Agent Authorization Across Context Compaction
- arXiv 2611.32194v1 · v1 2026-11-24 08:44 UTC · cs.AI, cs.CR
- Authors: Zeming Fei, Hongming Fei, Yi Xu, Xiaoyang Wang et al.
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.32194
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Request-derived authorizers such as Progent protect LLM agents from prompt injection by deriving what an agent may do from the user's request. Their guarantee rests on attribution: the request is taken to be what the user said. Compaction breaks it. At every automatic compaction we observed, Claude Code and Codex placed a model-written summary of earlier turns as a user message, so the compactor's quotation of the user, documents and injected text reads as the user speaking. Because a policy frozen at the first request lets the agent finish few later tasks, we let Progent derive its policy for each request, and find that what it grants then follows what the compactor wrote. Even a payee the user stated is not safe: when an attacker's notice states another account as plain data and the user asks to pay the rent, the policy derived from a frontier compactor's summary admits the notice's account in 91% of cases, and the one derived from the user's own words in none. The cause is general: we prove that an authorizer that cannot see who wrote which bytes cannot treat a forged record differently from the legitimate one it imitates by more than the two are distinguishable, and that the bound is tight. Frontier compactors bear this out: they mark injected instructions, which have no legitimate twin, but rarely injected data, which does. What a compactor keeps, and how it marks it, is a security parameter. The fix follows from attribution: the authorizer credits only what the user said, authenticated on arrival and carried verbatim across the boundary, while the agent still reads the summary. We prove that it then receives exactly that text or nothing, so an attacker can block the policy but cannot shape it, and adaptive attacks on our implementation confirm it. In 40 attacked AgentDojo episodes re-run with the fix, no attacker action completes while the agent reads the summary.

### When Successful Collaboration Becomes an Attack Surface: Insider Memory Poisoning in Multi-Agent Systems
- arXiv 2611.31307v1 · v1 2026-11-22 12:18 UTC · cs.AI, cs.CR, cs.MA
- Authors: Jihyung Ahn, Buru Chang
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.31307
- arXiv comment: 28 pages, 19 figures, 9 tables
- Full text: data/fulltext/2611.31307.txt

> Recent Multi-Agent Systems (MAS) increasingly use shared memory to store and reuse successful collaboration records, enabling teams to improve across tasks. However, this memory introduces a new attack surface for malicious insiders. Unlike existing insider attacks that inject misleading information directly into the current collaboration, misinformation stored in shared memory can later appear as successful team experience and gain greater credibility and influence. We propose MIMPA (Multi-Agent Insider Memory Poisoning Attack), which exploits this vulnerability using only normal participation privileges, without direct memory access. During an earlier task, the malicious agent embeds a target-specific payload while helping the team answer correctly, allowing the payload to be retained in a successful collaboration record. When retrieved for a later target task, this poisoned record can steer benign agents toward a designated wrong answer, further amplified by malicious triggering. Across three benchmarks and two LLM backbones, MIMPA substantially outperforms existing insider attacks and remains effective under hierarchical memory management, while auditing only partially mitigates it. These results reveal that shared memory intended to accumulate team experience can become a persistent channel for insider attacks. Our code is available at https://github.com/ahnji0520/MIMPA-code.

### Foresight Forcing: Learning Spatial Foresight for Robotic Manipulation
- arXiv 2611.30963 · v1 2026-11-23 00:00 UTC · 
- Authors: Mishuo Han, Zhixuan Liang, Zhaoyuan Wan, Wendi Chen et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.30963
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Robotic manipulation policies can improve action prediction by anticipating how objects move and how their spatial relationships change. World Action Models (WAMs) learn to predict future visual observations, but their training objectives typically leave the underlying 3D geometric transitions implicit. To alleviate this problem, we introduce Foresight Forcing (F^{2}), a WAM that learns a spatial transition representation from changes in a pretrained 3D feature space. During training, a frozen 3D foundation model extracts patch-wise feature differences from aligned current and future observations that provide dense supervision for geometry-aware feature transitions. We distill these targets into spatial transition queries, which are progressively refined from the current observation, language instruction, and proprioceptive state, and use them alongside current visual features to generate actions. At deployment, the policy predicts the queries without future observations or the 3D teacher. Experiments on LIBERO, LIBERO-Plus, and RoboTwin2.0 demonstrate strong manipulation performance and improved robustness, including 95.01% average success on RoboTwin2.0 Full. On six real-world manipulation tasks, F^{2} achieves a mean task score of 85.8%.

### Differential Proteomics to Symbolic Rules: An Audit of SHAP Guidance in Lung Adenocarcinoma
- arXiv 2611.29989v2 · v1 2026-11-23 03:51 UTC · cs.AI
- Authors: Surajit Das
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.29989
- Full text: data/fulltext/2611.29989.txt

> We tested whether SHAP improves protein-based Horn rules for distinguishing lung adenocarcinoma from adjacent-normal tissue. CPTAC supplied 213 samples (111 tumour, 102 adjacent-normal) from 111 patients, including 102 matched pairs. Per-protein effects and tests used the same complete pairs with Benjamini-Hochberg correction. Sparse logistic regression used five stratified patient-grouped outer folds, with preprocessing and tuning confined to training data and feature selection repeated within inner folds. A separate five-fold patient-grouped evaluation of inductive logic programming used training-derived evidence and discretisation. Of 9,518 proteins passing quality control, 378 differed in abundance (40 up, 338 down) at FDR below 0.05 and an absolute mean paired log-ratio difference of at least 1. Classifier ROC-AUC, average precision, accuracy and balanced accuracy were 0.9997, 0.9998, 0.9906 and 0.9906, respectively. On the original held-out rule splits, accuracy and F1 were 0.9765 and 0.9774, respectively. One clause appeared in two folds and the others appeared once. On common folds across all 111 patients, F1 was 0.9600 with SHAP, 0.9910 without SHAP and 0.9909 for L1 logistic regression. The inclusive SHAP cutoff retained all 100 ranked proteins per audited fold. Absolute logistic-regression coefficients reproduced the SHAP-guided candidate sets, clauses and held-out predictions in both the all-patient and paired-only analyses. A single-protein threshold reproduced full-rule predictions in the paired-only cohort. SHAP guidance did not improve held-out F1 on the common folds. Diagnostic utility, early detection, prognosis and generalisability beyond this cohort remain unestablished. Biomarker and clinical claims require independent validation, rule-stability testing under repeated resampling and further biological annotation.

### What People Choose Not to Say: A Multimodal Benchmark for Fine-Grained Information Manipulation in Conversations
- arXiv 2611.31346v1 · v1 2026-11-23 17:57 UTC · cs.AI, cs.CL
- Authors: Yuhan Bian, Zhaokai Liang, Jia Wang, Haoyu Liu et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.31346
- arXiv comment: ACM WSDM 2027 (Main Track), Our benchmark dataset is available at https://huggingface.co/datasets/xilinghuiye/RoomReader-Full
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recent advances in MLLMs have improved social understanding, enabling models to recognize emotions and distinguish truthful from deceptive behaviors. However, existing benchmarks largely focus on coarse-grained emotion recognition or binary truth-deception detection, overlooking the diverse ways people manipulate information in conversations, such as withholding, leakage, fabrication, evasion, and defensive counterclaim. Understanding these behaviors requires reasoning about underlying facts, participant knowledge, and conversational context, making them difficult to evaluate reliably. To address this gap, we introduce InfoCon, a multimodal benchmark for fine-grained information manipulation in conversations. InfoCon identifies six fine-grained strategies and derives a coarse consistency label from their factual and interactional relations. We develop an evidence-grounded multi-agent annotation framework to construct and verify reliable labels from rich contextual evidence. We benchmark representative multimodal models and systematically analyze their fine-grained information manipulation understanding, providing a testbed beyond binary truth-deception judgments.

### ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection
- arXiv 2611.31424v1 · v1 2026-11-23 19:11 UTC · cs.AI
- Authors: Yi Han, Zhen Sun, Zhijie Deng, Yini Huang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31424
- arXiv comment: 17 pages, 8 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> As LLMs become more capable, agents can perform more complex tasks with tools and maintain longer interactions with users. These benign conversations contain evidence on task results, user concerns, and operational constraints. The risk is that attackers who can observe benign conversations (evidence) may construct stronger indirect prompt injections without increasing the attackers' control over prior turns or the later injection. However, we still lack a clear study of how effectively attackers can select and use this evidence. To address this gap, we introduce ContextLure, a red-teaming framework in which an attacker silently observes an existing benign conversation, extracts evidence, and constructs an injection. The challenges are twofold: (a) selecting useful evidence and (b) presenting it as reasons for an unauthorized action, without changing the prior benign conversation. To efficiently exploit (a) the effect of evidence on attack success, our framework selects evidence across 2 dimensions: User/System Preferences with 3 selection policies. And to enhance (b) the process of turning the selected information into the malicious request, we introduce an Urgency/Priority matrix with 4 rewriting strategies. Across the evaluated conditions, we reach 67.4% ASR on AgentDojo and 87.3% on InjecAgent. These results show that attackers can use benign interaction evidence in later attacks without first poisoning the benign conversation.

### Frequency-Conditioned Privacy Auditing of Fine-Tuned Language Models
- arXiv 2611.31581v1 · v1 2026-11-23 21:22 UTC · cs.AI
- Authors: Aymen Noor, Ke Lyu, Honglu Jiang
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31581
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models are increasingly fine-tuned on sensitive data, where the same person's information may appear multiple times across records. This can cause models to memorize sensitive information, but memorization does not necessarily mean that the information can be recovered. A more serious privacy risk arises when the model begins to reproduce that information during generation. In this paper, we study how often sensitive information must appear in the fine-tuning data before it becomes recoverable. Across four language models, we vary the frequency of email addresses and phone numbers from $1\times$ to $50\times$ and compare standard fine-tuning, gradient clipping, and differentially private training. We find that the number of repetitions required before sensitive information becomes recoverable varies substantially across models. Gradient clipping can delay extraction, but it does not consistently prevent leakage at high repetition. DP-SGD at $\varepsilon=5$ produces zero observed extraction through $50\times$ repetition across all four models under the attacks we test, although the utility cost varies by model. These findings characterize how observed extraction varies across sensitive-data frequencies, model families, and training mechanisms, and highlight substantial differences in extraction behavior across models. Code and data are publicly available.

### FoveaWAM: Role-Aware 4D World-Action Modeling for Dynamic Manipulation
- arXiv 2611.31705v1 · v1 2026-11-23 23:50 UTC · cs.RO, cs.AI
- Authors: Jiaqi Yin, Baoyue Zhang, Jiyuan Zhang, Wenxuan Liu et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31705
- arXiv comment: 19 pages, 9 figures. Supplementary material included
- Full text: data/fulltext/2611.31705.txt

> To manipulate a moving object, a policy must predict the scene at the moment its action executes, yet every millisecond spent predicting pushes that moment further away. Scene-level forecasts are computationally expensive, whereas target-centric forecasts can omit nearby objects that affect contact. Our key insight is that what a policy must predict decouples by role: only the target's pose, which determines contact, requires millimeter precision, while the surroundings matter primarily through the clearance they leave and the motion they impart. We present FoveaWAM, a native 4D world-action model that allocates precision according to these roles. Specifically, it models the target's past and future motion as a metric SE(3) trajectory, the surroundings as sparse 3D flow, and relies on the current frame for everything static. This compact representation lets FoveaWAM act in 15.1 ms on one RTX 5090, about 10 times faster than video world-action baselines, leaving substantially less time for the scene to evolve before action execution. To evaluate each policy under its own latency, we introduce OnTimeBench, a dynamic manipulation benchmark in which the scene keeps moving while the policy computes. FoveaWAM reaches 82.1% success on OnTimeBench, 20.8 points above the strongest baseline, and also leads on DOMINO and real-robot tasks. Project page: https://foveawam.github.io/

### EffectWAM: Learning Action-Grounded Effects for Robot Manipulation
- arXiv 2611.32053v1 · v1 2026-11-24 06:36 UTC · cs.AI
- Authors: Yuan Zhang, Hao Cui, Jingfei Ni, Meiyi Wang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32053
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> World-action models connect visual prediction with executable robot control. We present EffectWAM, which develops this connection through three complementary components: Effect, camera positional encoding (CaPE), and Action Grounding. Effect represents visual change as the difference between independently encoded future observations and a shared current-observation anchor. CaPE conditions endpoint pooling on relative camera pose when reliable extrinsics are available, while sharing the same learned parameters with pose-free pooling for uncalibrated trajectories. Action Grounding trains the visual representation to retain measured changes in end-effector pose and gripper state. An exponential moving average of the observation encoder supplies Effect targets. A shared generation expert learns to jointly predict Effect and an executable action chunk through flow matching, and reuses the sampled pair to generate future video on demand. This allows the controller to execute actions without waiting for video synthesis. We train on more than 20,000 hours of heterogeneous embodied data, excluding unused chain-of-thought data, and accommodate dataset-specific joint, end-effector, and hand-pose representations. Our evaluation uses the Small (8B) configuration on all five benchmarks and additionally evaluates the Large (26B) configuration on RoboDojo. Experiments examine closed-loop manipulation across complementary benchmarks, and comparisons across multiple baseline policies show consistent improvements from Action Grounding.

### Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation
- arXiv 2611.32238v1 · v1 2026-11-24 09:15 UTC · cs.RO, cs.AI
- Authors: Kaipeng Fang, Yuhao Wang, Ji Zhang, Yunsong Zhou et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32238
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, while the agent may invoke it outside this region. We call this region the policy's handoff boundary. Existing whole-task policies typically have handoff boundaries that are narrow and difficult for an agent to characterize, making reliable coordination challenging. We propose Boundary-Aware Policy Learning, which explicitly shapes and then expands the handoff boundary of a visuomotor policy. First, Boundary-Explicit Training fine-tunes the policy on contact segments with diverse start poses, yielding a wide and well-defined boundary that can be communicated to the agent through a simple handoff protocol. Second, Boundary-Expanding Self-Improvement retrains the policy on curated successful system rollouts, extending the boundary toward earlier stages of each task and allowing the agent to hand over sooner with fewer language-model calls. Across RoboTwin 2.0 and RoboDojo, our system outperforms the strongest baseline by over 26 percentage points, reaching 98.4% success in randomized RoboTwin 2.0 scenes, while further reducing its API cost and execution time by 41.3% and 37.5%, respectively. These results suggest that the key to robust agent-policy orchestration lies not only in improving either component individually, but also in explicitly shaping the boundary between them.

### Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning
- arXiv 2611.32304v1 · v1 2026-11-24 10:00 UTC · cs.AI
- Authors: Simin Huang, Jiawei Chen, Shaolong Zhu, Qiwei Liang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32304
- arXiv comment: 15 pages, 7 figures, including supplementary material. Simin Huang and Jiawei Chen contributed equally. Code: https://github.com/vla-attack/Sparse_Poison_Strong_Hijack
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Vision-Language-Action (VLA) models advance robotic manipulation, but their reliance on demonstrations exposes them to backdoor threats. Among these threats, trajectory-level targeted backdoors are particularly challenging and may pose greater safety risks than behavior-disrupting attacks: rather than merely causing task failures or local action deviations, they must sustain closed-loop redirection to complete an attacker-specified multi-step task. To reliably induce such behaviors, existing methods typically rely on high poisoning rates to obtain sufficient target-trajectory supervision. However, high poisoning rates may compromise clean-task performance, whereas low rates leave target-trajectory supervision scarce and backdoor learning vulnerable to interference from dominant clean-task updates. To resolve this trade-off at low poisoning rates, we propose a two-stage co-optimization framework guided by vision, language, and action. Stage I freezes the policy and uses differentiable rendering and multimodal supervision to optimize a 3D trigger's texture, translation, and scale, strengthening trigger-target associations from limited poisoned demonstrations. Building on the optimized trigger, Stage II applies source-selective dual-LoRA adaptation to decouple clean and backdoor updates and mitigate their interference, followed by learned column-wise calibration and analytic fusion into a unified policy. Experiments on OpenVLA, OpenVLA-OFT, $π_0$, and $π_{0.5}$ across four LIBERO suites show consistent gains over all evaluated attack baselines. With only 1% poisoned data, our method achieves 86.4% target success and 95.2% clean-task success on OpenVLA-OFT in LIBERO-Spatial. Real-robot trials also demonstrate trajectory-level hijacking.

### Gamification in the age of AI: surveying player perceptions of motivation, manipulation, and data protection
- arXiv 2611.32464v1 · v1 2026-11-24 11:59 UTC · cs.AI, cs.CY, cs.NI
- Authors: Kurt Horvath, Tom Tucek
- Topics: Manipulation · score 6 · found via cs.AI, cs.CY
- Link: https://arxiv.org/abs/2611.32464
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Modern games and applications increasingly employ artificial intelligence (AI), user modeling, and gamification to influence user behavior, sustain engagement, and monetize attention. Although these mechanisms can enhance motivation and enjoyment, they also raise concerns about manipulation, personal data usage, and transparency. To examine how players perceive these dynamics, we conducted a survey with 28 adult participants. Respondents expressed strong concerns about the collection and exploitation of personal information in games and gamified applications, while also reporting low awareness and a limited sense of control over how their data is used. They evaluated progression features such as leveling systems and leaderboards as motivating. In contrast, they rated retention-focused mechanics such as daily login rewards and random reward reveals as highly manipulative. Participants reported that these systems can create fear of missing out or resemble gambling. Participants also expressed support for regulatory measures that limit exploitative design and protect vulnerable users. These findings reveal a clear gap between increasingly powerful engagement strategies and user trust, illustrating the need for more responsible and transparent gamification practices.

### Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation
- arXiv 2611.32533v1 · v1 2026-11-24 12:58 UTC · cs.RO, cs.AI
- Authors: Jiayi Liu, Ke Ye, Jiaming Zhou, Yufei Huang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32533
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> General-purpose robotic manipulation requires task reasoning, failure recovery, and precise control, yet limited manipulation data make these abilities difficult to obtain from a single policy. Recent multimodal agents show promise in task reasoning and recovery but lack reliable fine-grained control and incur high inference cost, whereas learned policies provide efficient fine-grained execution but struggle beyond their learned skills. Although their complementary strengths suggest combining the two, doing so requires repeatedly deciding which executor should act as task demands change. Instead of relying on the agent for each decision, we present Next-Manip, an on-demand agent--policy collaboration framework that decouples executor allocation from costly agent inference. We propose an Agent Invocation Controller (AIC) that allocates control between the policy and the agent through a lightweight classifier of current execution demands. We further introduce Task Dynamics Context (TDC), which packages informative manipulation changes from in-context examples into compact task references to support both agent reasoning and executor allocation. Across two simulation benchmarks and real-world experiments, Next-Manip achieves state-of-the-art performance while reducing agent inference costs.

### MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory
- arXiv 2611.32564v1 · v1 2026-11-24 13:12 UTC · cs.RO, cs.AI
- Authors: Jialong Peng, Shihao Zhou, Feng Yan, Wen Xiao et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32564
- arXiv comment: 17 pages, 8 figures, including supplementary material
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates. However, existing robotic ICL methods either rely on large-scale pretraining constrained by scarce, costly robot interaction data or require additional annotations yet struggle to generalize across tasks. To bridge this gap, we propose MXI-MemICL, a framework for memory-guided ICL in vision-language-action (VLA) models. By treating demonstrations as retrievable memory, MXI-MemICL enables in-context manipulation without additional large-scale pretraining or specialized annotations. Specifically, a visual-action causal encoder turns actions and their observed effects in demonstrations and completed interactions into reusable memory to guide execution. To retrieve experience suited to upcoming execution, an intention predictor forecasts the next stage's intent and uses it to query memory. The retrieved experience conditions the language backbone through experience-token prefixes and gated cross-attention, guiding action generation with a learned gate that regulates its influence. MXI-MemICL improves success over the baseline by +8.2% and +14.4% on RoboCasa365 and RoboTwin 2.0. Real-robot experiments show a +9.0% gain, with demonstrations adding +5.0% on seen and +16.7% on unseen tasks. The code will be made publicly available.

### When "Neutral" Means Irrelevant: A Construct-Validity Audit of NormAd-ETI
- arXiv 2611.32614v1 · v1 2026-11-24 13:45 UTC · cs.CL
- Authors: Aarav Singh, Animesh Pathak, Christian Hoang, Navyansh Singh et al.
- Topics: Clicks & measurement · score 6 · found via cs.CL
- Link: https://arxiv.org/abs/2611.32614
- arXiv comment: 19 pages, 4 figures
- Full text: data/fulltext/2611.32614.txt

> NormAd-ETI scores a model's judgment of everyday actions as acceptable, unacceptable, or neither as the cultural context shrinks from a specific rule to a country name. We audit what that three-way score measures. It combines two decisions: whether a supplied norm applies, and whether the action conforms to it. Separating them shows that when only a country is shown, applicability falls to near chance while conformity stays well above it, because the prompt withholds the rule a Neutral label depends on. Because one answer carries both decisions, the score follows the steadier conformity and hides the weaker applicability, and no single prompt recovers the two separately. Dedicated forced-choice probes separate them for frontier models but not for small open models, where the applicability judgment still tracks the hidden acceptability label. Adding a written rationale reduces that conflation without removing it. We recommend reporting the two results separately and measuring the conflation gap.

### ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning
- arXiv 2611.32639v1 · v1 2026-11-24 14:00 UTC · cs.AI, cs.CV, cs.RO
- Authors: Haoyuan Li, Wei Huang, Jiehong Lin, Shengrong Zhang et al.
- Topics: Manipulation · score 6 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2611.32639
- arXiv comment: 27 pages, 15 figures
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction. However, in long-horizon manipulation, sparse success/failure feedback provides little information about where policies encounter bottlenecks. Moreover, repeated full-task rollouts also leave these bottlenecks weakly analyzed and insufficiently practiced. To this end, we introduce ReFocus, a progress-guided multi-round RL framework that alternates between Global and Local RL to identify task-specific bottlenecks and allocate additional practice to them. Specifically, during Global RL, we decompose each task into a Directed Acyclic Graph (DAG) of subtasks. Then a DAG-based Progress Reward is leveraged for both policy training and bottleneck diagnosis. Based on the identified bottlenecks, ReFocus selects Adaptive Practice Windows, defining task segments from an entry stage to a target stage. It allocates additional interaction to these segments during Local RL while updating the entire policy. After that, it evaluates the policy to perform the full task for the next round of RL, forming an iteration between Global and Local RL. Experiments on LIBERO-Long and RoboCasa365 show that ReFocus achieves success rates of 97.8% and 51.3%, respectively, compared with 90.6% and 39.3% for the $π_{0.5}$ baseline. Furthermore, we evaluate a real-world adaptation on three long-horizon tasks. On BreadBaker, ReFocus achieves 95% success, compared with 30% for the $π_{0.5}$. Project page: https://refocus-robotics.github.io.

### DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation
- arXiv 2611.32654v1 · v1 2026-11-24 14:09 UTC · cs.RO, cs.AI
- Authors: Hongjia Liu, Dacheng Zhou, Minghao Fu, Chuanjun Guo et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32654
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success. Recent world-action models (WAMs) extend vision-language-action (VLA) models with the first signal by jointly predicting actions and future observations, yet this predictive ability serves only as an auxiliary loss for policy learning. Meanwhile, most policy improvement methods learn dynamics and values in separate models, increasing training overhead and limiting representation sharing between these complementary objectives. We introduce DexWAC, a unified world-actor-critic model that jointly learns an actor, an action-conditioned world model, and a bootstrapped critic in a single robot pretraining stage. Our key insight is that visual prediction encourages control-relevant features, while value supervision promotes task-relevant representations; together, they shape a representation suited to policy learning. Built on an image-editing backbone, DexWAC predicts, for each action chunk, the visual latent and proprioception at its endpoint together with its reward and continuation, so the world model alone efficiently yields complete imagined transitions without generating intermediate video frames. After adapting the world model and critic on real rollouts, we improve the pretrained actor through either PPO on imagined rollouts or critic-guided best-of-$N$ selection. DexWAC surpasses the large-scale pretrained VLA and WAM baselines in simulation and achieves 75% average success on two real-world tasks, compared with 45% for $π_{0.5}$. Its world model is more accurate and faster than video-based baselines, and ablations confirm that learning dynamics and value together improves the policy.

### MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation
- arXiv 2611.32803v1 · v1 2026-11-24 15:25 UTC · cs.RO, cs.AI, cs.MA
- Authors: Yanzhe Chen, Zhijun Cao, Ruihe An, Chang Gong et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.32803
- arXiv comment: Project website: https://showlab.github.io/MRBench/
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recent advances in multi-robot manipulation have shown how robots can collaborate to accomplish complex tasks. However, successful coordination does not reveal which robots are actually needed. The same task may require different teams as robot capabilities change, resources become unavailable, or objects replace robotic support. We argue that reliable multi-robot manipulation requires physical necessity reasoning: understanding what a task demands, which resources can fulfill those demands, and which are truly necessary. We introduce MRBench, a benchmark for physical necessity reasoning in heterogeneous multi-robot manipulation. It comprises eight tasks with distinct concurrency and reach constraints, each evaluated under five configurations that change the required resources while preserving the task goal. Our evaluation reveals that existing coordination agents perform well with reference teams but struggle when robot embodiments change or passive objects can replace robotic support. To address this gap, we propose MRScissors, which separates task requirements from measured physical capabilities and identifies minimal feasible teams through constrained search. Across two model backbones, MRScissors achieves 85.4% and 91.2% team-selection accuracy, outperforming the strongest baselines by 10.4 and 9.5 points, respectively. Together, these findings expose a critical gap between coordinating robots and understanding their physical necessity.

### Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance
- arXiv 2611.33098v1 · v1 2026-11-24 18:34 UTC · cs.AI, cs.IR
- Authors: Lingwei Gu, Jimmy Lin
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.33098
- arXiv comment: 11 pages, 2 figures, 5 tables
- Full text: data/fulltext/2611.33098.txt

> Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks to a small language model, or SLM, that runs on hardware one already owns. To test it, we build Delegent, a simple and effective agent harness built on Claude Code, in which the frontier model stays in charge of every task but hands focused subtasks, such as investigating code, running tests, and searching a corpus, to SLM subagents. Existing approaches such as cascades and model routers usually choose which model executes the entire task, whereas in Delegent, the frontier model always leads the execution and delegates easy subtasks to the SLM. No router or model is trained, so either model can be swapped freely. With the help of a 27B FP8 SLM, Delegent reduces the frontier cost of long-horizon coding by 67% and of agentic search by 59%, with no loss in task performance, and even a 2B SLM that fits on a laptop reduces the coding cost by 66%. The savings grow with the legwork that the frontier model would otherwise do itself, and a short instruction, which leaves the main coding tasks to the frontier model, accounts for most of the saving and keeps the 2B SLM from losing tasks. Code: https://github.com/castorini/delegent

### Towards Realistic Evaluation of Uncertainty Quantification for LLM-Based Recommender Systems
- arXiv 2611.33036v1 · v1 2026-11-24 17:48 UTC · cs.IR, cs.CL, cs.LG, stat.ML
- Authors: Hao Wu, Sipeng Chen, Weikai Li, Tianyi Chen et al.
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.33036
- arXiv comment: 27 pages, 5 figures. Published in Transactions on Machine Learning Research (TMLR), 11/2026. Reviewed on OpenReview: https://openreview.net/forum?id=GXDe6REdu3

> Large language models (LLMs) provide a flexible interface for recommendation systems. However, their issued rankings require reliable instance-level uncertainty monitoring. In this scenario, comparing uncertainty quantification (UQ) methods becomes challenging because LLM rankers lack a standard item-classification head. Their scores may depend on option labels, prompts, generation procedures, and the available user and item evidence. Existing methods derive uncertainty from different sources and apply it at different stages of the recommendation process. Some methods evaluate an issued ranking, whereas others use uncertainty to change the ranking itself, making direct comparison difficult. Here we introduce a fixed-ranking benchmark which evaluates eight heterogeneous UQ signals as record-level monitors under a shared output contract. We evaluate these signals across four recommendation datasets and two LLM backbones under a shared fixed-ranking protocol. From the results, we draw three main observations. First, UQ method ordering changes across backbones even on the same reference instances. Second, ranking-aligned Top10Mass provides the strongest scalar Error@10 detection in several evaluation conditions, reflecting effective cutoff-aligned monitoring, while its advantage narrows for popularity-tail targets. Third, scalar UQ signals are weak at identifying which control has the larger clipped NDCG@10 difference, whereas source-specific signals, including Perturbation Rank Instability and simple listwise distances, provide stronger paired-control agreement, reflecting their sensitivity to the two controlled evidence sources. These findings motivate us to evaluate ranking-failure detection, robustness across recommendation conditions, and responses to controlled evidence changes as distinct properties of UQ.

### Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounded Policy Assistant
- arXiv 2611.32266v1 · v1 2026-11-24 09:37 UTC · cs.CL, cs.CY, cs.IR
- Authors: Mark Farinas, Alesandra Garcia, Maria Reyes, Jethro Nueva et al.
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.32266
- arXiv comment: Extended version of a paper published in the proceedings of IEEE SmartEdu 2026 (2026 IEEE Smart World Congress), pp. 810-817. 12 pages, 4 figures, 7 tables. Benchmark and code: https://github.com/JAMNSoftware/jamn-rag-benchmark
- Journal ref: 2026 IEEE Smart World Congress (SWC), pp. 810-817

> In some educational institutions, workflows such as the exam deferral process can be slow, inconvenient, and inconsistent, which creates the need to implement novel digital systems. This paper presents Schedulater, a mobile app for managing university exam deferrals. JAMN Bot is a Large Language Model (LLM)-powered chatbot integrated into Schedulater that provides context-aware support to help users understand the deferral process. The system features a Retrieval-Augmented Generation (RAG) pipeline using Ollama (Llama 3.2 3B) for self-hosted inference which enables policy-grounded responses without sacrificing privacy. We evaluate the system using a 43-item benchmark spanning Exam Deferral, Privacy, Scheduling, Cross-Policy, and Adversarial & Out-of-Scope questions, and report inter-rater agreement among our human evaluators alongside retrieval hit-rate metrics. Subsequently, we utilize an LLM-as-a-judge approach with GPT-5.4, revealing slight-to-moderate alignment with our raters that improves with answer quality, and check the ranking against a panel including Gemini 3.5 Flash and Qwen3.5 397B. The results of our study display trade-offs between open-weight and frontier models, as well as LLM-human evaluation alignment with answer quality. Schedulater demonstrates the feasibility of integrating lightweight LLMs into university administrative workflows with structured retrieval.

## Other new cs.IR papers, title only (15)
- Query Obfuscation with Embedding-Optimized Noise (EON): A Representational Blindspot in Agentic Retrieval — https://arxiv.org/abs/2611.31344
- Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study — https://arxiv.org/abs/2611.31442
- ModernELECTRA: Replaced-Token Detection with Boundary-Window Reconstruction for Compact Encoders that Classify and Embed — https://arxiv.org/abs/2611.31495
- Provably Near-Optimal PQ in the Extended Zador Model — https://arxiv.org/abs/2611.31579
- Provenance Loss and Repair in Multilingual Compaction — https://arxiv.org/abs/2611.31668
- RELAY: Learning Compatible Representations One Encoder at a Time — https://arxiv.org/abs/2611.31882
- MELODI: Similarity-Identity Decoupling for Lightweight Ranking — https://arxiv.org/abs/2611.31940
- User-Adaptive Fusion of Multiple Foundation Models for Recommender Systems — https://arxiv.org/abs/2611.31951
- LARF: Learning-aligned Reasoning Framework for Search Relevance — https://arxiv.org/abs/2611.32125
- OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval — https://arxiv.org/abs/2611.32203
- See the Answer, Learn to Embed: Learning Universal Multimodal Embeddings from Hindsight — https://arxiv.org/abs/2611.32439
- LazUnirec: Unifying Retrieval and Ranking in Multi-scenario Industrial Recommendation — https://arxiv.org/abs/2611.32590
- A Text-to-SQL Benchmark for Official Statistics — https://arxiv.org/abs/2611.32646
- Speculative Decoding for Semantic-ID-Based Generative Recommendations — https://arxiv.org/abs/2611.32855
- SAG-Mem-1.0 Technical Report — https://arxiv.org/abs/2611.33124

## Already listed on an earlier day, still inside the look-back window (78)
- Fetch, Read, Reuse: How AI Search Agents Bend the Web's Rules — https://arxiv.org/abs/2611.30546 (score 28)
- DM-Lab at TREC 2026 RAG: Multi-Query Retrieval, Ensemble Judging, and Claim-Pack Generation — https://arxiv.org/abs/2611.28233 (score 16)
- Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection — https://arxiv.org/abs/2611.29268 (score 14)
- Can Search Agents Correct Their Own Errors? Evaluating Retrieval, Evidence Delivery, and Answer Completion — https://arxiv.org/abs/2611.30243 (score 14)
- Bug Bounty Programs in the AI Era: How Does Platform Anti-Spam Friction Affect Vendor Profitability? — https://arxiv.org/abs/2611.30615 (score 14)
- Leakage-Safe Auditing of Attribution-Driven Data Curation in Medical Imaging — https://arxiv.org/abs/2611.31096 (score 14)
- CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting — https://arxiv.org/abs/2611.31185 (score 14)
- Ask Again: Answer-List Instability in Generative Engines — https://arxiv.org/abs/2611.30819 (score 13)
- Adaptation or Poisoning? Security Risks of Conversational Test-Time Learning in Large Language Models — https://arxiv.org/abs/2611.29532 (score 11)
- Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation — https://arxiv.org/abs/2611.27689 (score 10)
- CompareDR: Benchmarking Deep Research Reports from Individual Quality to Comparative Merit — https://arxiv.org/abs/2611.29549 (score 10)
- SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health — https://arxiv.org/abs/2611.29988 (score 10)
- Disclosure Bias in AI Reviewers — https://arxiv.org/abs/2611.30410 (score 10)
- CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons? — https://arxiv.org/abs/2611.30727 (score 10)
- ComputeWise: Measuring and Fixing GPU Waste by AI Research Agents — https://arxiv.org/abs/2611.31027 (score 10)
- ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents — https://arxiv.org/abs/2611.31198 (score 10)
- PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search — https://arxiv.org/abs/2611.28645 (score 9)
- Can Cities Have Personalities? Introducing the SCD City Personality Assessment — https://arxiv.org/abs/2611.30733 (score 9)
- The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web Search — https://arxiv.org/abs/2611.27899 (score 8)
- Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents — https://arxiv.org/abs/2611.28947 (score 8)
- Elicitation format changes zero-shot classification accuracy in a medical vision-language model: a two-center evaluation on colorectal histopathology — https://arxiv.org/abs/2611.28997 (score 8)
- Automatic Construction of Persian E-Commerce Dialogue Datasets for Conversational Product Search — https://arxiv.org/abs/2611.29356 (score 8)
- Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents — https://arxiv.org/abs/2611.29613 (score 8)
- Reducing Authorship Attribution Risk in Student Texts Through Style-Conditioned Rewriting — https://arxiv.org/abs/2611.29642 (score 8)
- Sánchez, Feijóo, or Abascal? Speaker Attribution and Ideological Congruence in LLM Personas Reading Posts on X of the Leaders of the Three Main Parties of the 29N General Election in Spain — https://arxiv.org/abs/2611.29765 (score 8)
- MobileGrail: Learning Compact Guardrails for On-Device deployable Mobile GUI Agent Safety — https://arxiv.org/abs/2611.29847 (score 8)
- WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce — https://arxiv.org/abs/2611.30662 (score 8)
- Self-Evolving Evaluation Environments for Computer-Use Agents — https://arxiv.org/abs/2611.30962 (score 8)
- MedUIGym: Evaluating and Training GUI Agents for Clinical Workflows — https://arxiv.org/abs/2611.30983 (score 8)
- Poisoning Attacks and Collaborative Defense Framework for LightRAG-Based Construction Regulation Knowledge — https://arxiv.org/abs/2611.27460 (score 7)
- When Learned IDS Model Selection Collapses to a Static Choice: A Measurement Study at the Edge — https://arxiv.org/abs/2611.29968 (score 7)
- MomentMem: Memorizing Key Moments for Robot Manipulation — https://arxiv.org/abs/2611.26745 (score 6)
- Manipulation-resistant reputation for peer-to-peer scientific publishing: a combination-therapy approach — https://arxiv.org/abs/2611.27625 (score 6)
- Redesigning Neural Networks to Not be Confidently Wrong even to Strong Adversarial Attacks — https://arxiv.org/abs/2611.27811 (score 6)
- Targeted In-Context Poisoning of Tabular Foundation Models: An Empirical Study — https://arxiv.org/abs/2611.28396 (score 6)
- A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation — https://arxiv.org/abs/2611.29338 (score 6)
- More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation — https://arxiv.org/abs/2611.29339 (score 6)
- MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model — https://arxiv.org/abs/2611.29501 (score 6)
- Relativising Integrity and Robustness: Prompt Injection and Partitioned Enclaves — https://arxiv.org/abs/2611.29802 (score 6)
- HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation — https://arxiv.org/abs/2611.30813 (score 6)
- Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection — https://arxiv.org/abs/2611.29977 (score 6)
- Spiking World-Action Models for Robotic Manipulation — https://arxiv.org/abs/2611.30041 (score 6)
- A statistical measure of trust in generative AI — https://arxiv.org/abs/2611.30286 (score 6)
- Automated Call for Action: RAG-Based Environmental Law Enforcement Screening System — https://arxiv.org/abs/2611.30423 (score 6)
- JEPA-ICL: Progress-Aligned Latent Plans for In-Context Robotic Manipulation — https://arxiv.org/abs/2611.30516 (score 6)
- RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation — https://arxiv.org/abs/2611.30555 (score 6)
- How Many Parameters Does Forecasting Need? A Survey and Code-Level Audit of Lightweight Long-Term Time Series Forecasting — https://arxiv.org/abs/2611.30685 (score 6)
- Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression — https://arxiv.org/abs/2611.31089 (score 5)
- Pre-Crawl Prioritization and Seed Classification for Large-Scale Web Archiving — https://arxiv.org/abs/2611.27743 (score 4)
- Beyond Relevance: An Empirical Study of Multimodal LLMs for Diversity-Aware Recommendation Reranking — https://arxiv.org/abs/2611.28379 (score 4)
- ChatGPT Can't Sell (And That's Probably a Good Thing): Buyer-Aligned AI Advice, the Sales-Representative Gap, and Evidence from Commercial Conversations — https://arxiv.org/abs/2611.28946 (score 4)
- Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and Judgement in Evidence-Grounded Verification — https://arxiv.org/abs/2611.29697 (score 4)
- DataRecycle: Trustworthy Distillation of Structured Data from Scattered Web Evidence — https://arxiv.org/abs/2611.29206 (score 3)
- SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance — https://arxiv.org/abs/2611.30588 (score 2)
- GERF: A Token-Efficient Multimodal Retrieval Framework for Schema-Guided Scientific Information Extraction — https://arxiv.org/abs/2611.28295 (score 1)
- MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation — https://arxiv.org/abs/2611.28604 (score 1)
- LLM-Based Assistant for Dog Care Guidance — https://arxiv.org/abs/2611.29286 (score 1)
- Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees — https://arxiv.org/abs/2611.29966 (score 1)
