# Paper candidates — 2026-11-26 (IST)

Generated 2026-11-26 08:50 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 28 new topic matches · 9 other new cs.IR · 103 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (28), highest score first

### Real Package, Wrong Controller: Static Auditing of Vendor--Protocol Mismatches in LLM-Generated PLC Code
- arXiv 2611.33227v1 · v1 2026-11-24 08:53 UTC · cs.CR, cs.LG, cs.SE, eess.SY
- Authors: S M Zia Ur Rashid, Sazidul Islam Hira, Suman Rath
- Topics: Brand/product recommendation, Clicks & measurement · score 14 · found via cs.CR
- Link: https://arxiv.org/abs/2611.33227
- Full text: data/fulltext/2611.33227.txt

> Language models can generate Python that drives industrial protocols on programmable logic controllers, yet existing code-grounding checks ask whether an imported package or symbol exists rather than whether it suits the declared industrial target. We define \emph{metadata-conditioned, import-level vendor--protocol incompatibility} and build \textsc{Proteus-OT}, a label-free static verifier over a version-pinned graph of documented bindings. Across 883 generated scripts, 180 carry an import-level mismatch against the declared target (20.4\%); restricting to single-vendor targets gives 16.3\%, and additionally requiring the offending library to reach a protocol communication call gives 14.2\%, which we read as conditional on the corpus metadata rather than on verified intent. None of the 28 adjudicable human control files carries one, a sample too small to estimate a prevalence. Within the balanced subset, 96.6\% of mismatching scripts import packages and call methods that exist, so an existence baseline does not represent them, and every positive ships with an inspectable witness. We also audit machine-versus-human classification on the same corpus, where character $n$-grams reach macro-F1 1.000 under task, model and vendor-disjoint partitions and survive comment removal, an AST round trip and identifier anonymisation. The trailing newline present in 95.2\% of human files and in none of the generated ones separates the classes on its own. Vendor--protocol consistency is a useful static audit target, whereas provenance classification on repository-labelled corpora is not authorship detection.

### Brand Recall and Category Accuracy in Language Models: An Audit of 1,000 B2B SaaS Brands
- arXiv 2611.33322v1 · v1 2026-11-24 19:08 UTC · cs.AI
- Authors: Ben Moore
- Topics: Brand/product recommendation, Clicks & measurement · score 14 · found via cs.AI
- Link: https://arxiv.org/abs/2611.33322
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> A language model can name a brand without classifying it correctly. This study measures these outcomes separately for 1,000 B2B SaaS brands across 333 product categories. On Gemma 4 12B, with no external retrieval, category prompts elicit 510 brands (51.0%). A separate five-candidate category probe ranks the reference label first for 787 brands, a distractor first for 194, and yields little separation for 19. Among the 981 separated rankings, the error rate is 19.8%. It falls to 3.5% for the 547 brands with a winner-to-runner-up log-probability margin above 0.6. These are within-cohort measurements, not calibrated confidence estimates. Exploratory regressions associate technical coverage with recall and an owned-properties composite with category accuracy, but the composites use different adjustment sets and do not establish causal effects. Across four Gemma generations, measured recall is 39.8%, 44.3%, 51.1% and 51.0%. A separate representation-based sentiment measure has little linear association with customer ratings (r=0.03, n=921). The findings support reporting recall and category accuracy separately. Failure to elicit a brand does not establish its absence from model parameters or training data.

### DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents
- arXiv 2611.34852v1 · v1 2026-11-25 18:25 UTC · cs.AI, cs.CL
- Authors: Han Huang, Yuchen Yan, Xingyu Wu, Yijun Li et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.34852
- arXiv comment: Project Page: https://zjureal.com/DRBenchPro/ Code: https://github.com/ZJU-REAL/DRBenchPro
- Full text: data/fulltext/2611.34852.txt

> Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a report covers and how deeply it explores them. We introduce DRBench Pro, a benchmark that makes structured knowledge coverage the primary evaluation target. Our automated pipeline builds local knowledge trees from Wikipedia and uses sampled subgraphs to generate research queries and evidence-grounded rubrics. Each rubric corresponds to a relation in the tree, preserving the structure of the knowledge being evaluated. Agents receive only the research query. This structure allows us to measure breadth across major research directions and depth along related knowledge chains, with their geometric mean giving overall coverage. The benchmark includes 144 cases across 24 domains and 44,102 rubrics. Evaluating 16 deep research agents reveals different strengths in breadth and depth, with the best-performing agent reaching 57.04% overall coverage. Rubric judgments agree closely with human annotations, and agent rankings remain stable across the tested metric configurations.

### Welfare-Enhancing Mechanism Design for Agent Ecosystems
- arXiv 2611.33627v1 · v1 2026-11-25 01:57 UTC · cs.GT, cs.IR, cs.MA
- Authors: Zitian Guo, Chen Xu, Beibei Li, Chenyan Xiong
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.IR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2611.33627
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> The emerging Agentic Web forms a multi-agent ecosystem: a decentralized service market where the user agent selects which content agents to query from their submitted profiles, before seeing any documents. Profiles therefore become a new target of optimization. Existing Generative Engine Optimization studies how a single supplier rewrites documents the engine can already retrieve, to improve their citation. In the Agentic Web, multiple content agents optimize profiles to compete for limited opportunities to deliver documents. To study this repeated interaction, we build WildRegistry, a simulation framework and benchmark based on a real agentic-search request stream, and model it as a dynamic game under private monitoring. Long-horizon experiments show that this competition lowers website-selection quality and settles at a harmful stable point, which our empirical criterion identifies as an approximate rewriting equilibrium. We therefore design a welfare-enhancing mechanism, DEC (Delivery-Evidence Credit), a platform-side policy that uses recorded delivery outcomes to reallocate later opportunities and reduce information asymmetry. DEC improves this endpoint, raising website-selection quality while preserving most of providers' exposure gains, for a Welfare Gain of +2.01 points and a healthier long-horizon outcome. More broadly, our findings highlight the importance of mechanism design in agent ecosystems: turning recorded delivery outcomes into evidence that endogenously shapes later user-agent selection and content-agent adaptation can steer long-horizon adaptation toward delivered capabilities.

### When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL
- arXiv 2611.34777v1 · v1 2026-11-25 17:38 UTC · cs.AI, cs.CL, cs.LG
- Authors: Haowen Hou, Yicheng Liu, Zhen Huang, Jiaqi Wang
- Topics: Query fan-out, Agents · score 9 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.34777
- arXiv comment: 16 pages
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Group-based reinforcement learning with verifiable rewards often yields all-fail groups on long-horizon agent tasks: every sampled trajectory receives zero reward, leaving group-relative methods without a reward-based policy gradient. A common remedy supplies complete solutions from a stronger model, but full trajectories are expensive and expose the learner to long off-policy histories. We introduce SPLICE, which constructs local training targets from failed current-policy trajectories online. For each all-fail group, a proposal model selects a splice point in a current-policy trajectory and generates several bounded options from that point. We estimate each option's value using repeated current-policy continuations, convert positive estimates into a return-weighted local target, and fit the current policy on the options. We evaluate SPLICE across two policy families on two long-horizon agent tasks, Software Engineering with SWE-bench Verified and Deep Research with BrowseComp-Plus. SPLICE outperforms GRPO and full-trajectory guidance baselines in all four settings, improving over GRPO by 2.8--9.8 percentage points. On initially failed SWE tasks, it raises GRPO's graduation rate by 10.8 percentage points. Further experiments show that SPLICE improves performance while reducing costly proposal-model computation.

### Learning the Platform, Not the Learner: Sequencing Shortcuts in the Offline Evaluation of Educational Recommender Systems and LLM Rankers
- arXiv 2611.33240v1 · v1 2026-11-24 13:48 UTC · cs.CY, cs.IR, cs.LG
- Authors: Youssef Jdidou
- Topics: Brand/product recommendation · score 8 · found via cs.CY, cs.IR
- Link: https://arxiv.org/abs/2611.33240
- arXiv comment: 27 pages, 6 figures, 17 tables. Code: https://github.com/jdidou/beat-the-syllabus (doi:10.5281/zenodo.24443552); code and per-case results also in the ancillary files
- Full text: data/fulltext/2611.33240.txt

> Educational recommenders are usually compared offline, by how well they predict the next activity in logs of tutoring systems, learning applications and MOOCs, where the next activity is largely decided by the platform: teachers assign problem sets, tutors draw problems until mastery, engines select questions. On eight public datasets from five platforms, we compare four structural predictors, which use nothing about the learner beyond the last activity, with ten personalised recommenders and with open-weight LLM rankers from 0.5 to 7 billion parameters, under two protocols. The structural predictors reach between 0.81 and 1.00 of the best accuracy of any method (median 0.95), mostly through population transitions rather than the course order; the best personalised recommender is significantly better on five datasets, by 0.007 to 0.102 NDCG@10, and on Eedi in three of four training runs. Every method is far less accurate on steps along transitions never seen in training and on steps chosen by learners. LLM rankers look competent with random negatives but are never much better than a word-matching baseline, and with negatives that are plausible under the course structure they stay close to random or well behind the transition heuristic, whatever their size. In a simulation with known learner needs, the structural share tracks the share of steps decided by the platform, and offline accuracy ranks an oracle of the learners' needs below imitators of the platform. Weighting test steps by how unlikely the structure makes them restores much of the link with usefulness and, on the real data, reveals a significant personalisation signal on seven of the eight datasets. We propose a syllabus-aware evaluation checklist and release a Python package that reports the lift of any recommender over the structure.

### Onnx2TEE: Automated Graph-Aware Model Partitioning for TEE-based Edge AI Protection
- arXiv 2611.33262v1 · v1 2026-11-24 18:11 UTC · cs.AI, cs.CR, cs.ET
- Authors: Daniela M. Vela Hernandez, Samuel Hildebrand, Sean Oesch, Brian Weber et al.
- Topics: GEO/AEO, Manipulation · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.33262
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> AI models are increasingly being deployed at the edge. Since these models often require significant research and development to produce, are often deployed in potentially hostile environments, and downstream systems often rely on accurate data; protecting them from theft or manipulation is worthy of serious consideration. Trusted Execution Environments (TEEs), which provide hardware-enforced separation of software execution, can protect model weights but impose strict resource constraints, making full-model execution impractical for large neural networks. We present Onnx2TEE, an automated, model-independent pipeline that partitions ONNX models across rich, trusted execution environments for non-sequential feed-forward networks using graph-aware segmentation to preserve computational dependencies while minimizing boundary communication and reducing TEE-induced inference latency. Evaluation on an NVIDIA Jetson AGX Orin using an Arm TrustZone TEE demonstrates that model parameters can be highly concentrated in individual segments, supporting selective protection of parameter-dense model components. The evaluation further shows that the generated trusted app's memory requirements depend on both computation and intermediate tensor sizes.

### OneQuery: Unified Sequence-to-Structure Generation for Multilingual E-commerce Query Understanding
- arXiv 2611.33653v1 · v1 2026-11-25 02:19 UTC · cs.IR
- Authors: Mingyu Zhang, Jiejie Qin, Jianhui Ji, Rong Xiao et al.
- Topics: Brand/product recommendation · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.33653
- arXiv comment: Accepted by WSDM 2027 (Findings)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multilingual e-commerce search requires robust query understanding to convert cross-lingual user queries with varied linguistic patterns into standardized semantic representations that support retrieval and ranking. However, traditional Query Understanding systems suffer from error accumulation, separately optimized subtasks that ignore their mutual correlations, and high maintenance costs. To address these issues, this paper proposes OneQuery, a unified generative framework for multilingual query understanding based on domain-specific large language models in e-commerce. We reformulate four subtasks, namely Language Recognition, Spelling Correction, Translation, and Query Tagging, into a unified Sequenceto-Structure autoregressive generation process constrained by predefined schemas, and design a three-stage progressive training pipeline with multi-task reinforcement learning alignment. OneQuery demonstrates consistent gains over baselines across all tasks and remains effective across different backbone sizes, and online experiments in the AliExpress e-commerce search scenario further confirm its practical value for industrial deployment.

### Is Sara Omar the true author of Dødevaskeren (The Dead Washer)? Authorship attribution in Danish literature
- arXiv 2611.34131v1 · v1 2026-11-25 10:30 UTC · cs.CL, cs.CY, cs.DL
- Authors: Jacques Savoy
- Topics: Citation & source selection · score 8 · found via cs.CL, cs.CY
- Link: https://arxiv.org/abs/2611.34131
- arXiv comment: 23 pages, 4 figures, 10 tables
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> The bestseller Dødevaskeren (The Dead Washer) was published in 2017 under the name Sara Omar. A Danish colleague has suggested that the novel may have been written by another author, possibly Mads Peder Nordbo. To investigate this authorship question, four authorship attribution methods were applied, namely Delta, intertextual distance, Nearest Shrunken Centroids (NSC), and naïve Bayes. Using various parameter settings, these approaches consistently identify Nordbo's writing style in the doubtful novel, although the results do not provide conclusive evidence that he authored the novel in its entirety. In a second step, the novel was divided into non-overlapping segments of 5,000 tokens. Once again, Nordbo's style was identified in the majority of the segments. However, a small number of passages do not clearly support this conclusion and instead suggest the possible involvement of another, as yet unidentified, author, possibly Sara Omar herself.

### EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts
- arXiv 2611.34466v1 · v1 2026-11-25 14:36 UTC · cs.AI
- Authors: Yurun Chen, Biao Yi, Qihang Yu, Keting Yin et al.
- Topics: Agents · score 8 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2611.34466
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AI wearables, such as smart glasses, extend the context available to agents beyond digital environments to users' physical surroundings. With these devices, computer tasks can originate from users' ongoing activities rather than solely from explicit instructions. Through first-person observations, agents can identify objects and activities relevant to user requests and ground digital tasks in the surrounding context. We call this interaction paradigm Ego Use. However, first-person observations are limited by the wearer's viewpoint and may provide incomplete or ambiguous evidence of ongoing activities. As new observations arrive, agents may need to revise their understanding of the physical context and user intent, and reassess whether prior digital actions remain valid. Whether current agents can reliably handle these changes remains insufficiently evaluated. We introduce EgoUseBench, a benchmark for evaluating Ego Use across three interaction settings with different levels of first-person context. Computer-Use relies on explicit instructions, Offline Ego Use provides prerecorded first-person context before execution, and Online Ego Use provides continuous observations as user intent evolves. Based on over 74 hours of real-world first-person recordings, we construct 693 tasks across the three interaction settings. To capture task evolution, we track first-person observations, user requirements, and website state separately. We further group tasks by how information changes during execution, resulting in three types: Graft (revised user requirements), Refresh (new first-person observations), and Clarify (agent-initiated information seeking). We evaluate advanced models and find that average success rates in Online Ego Use are 26.3% lower than in Computer-Use. This result reveals the difficulty of keeping task execution aligned with evolving first-person context and user intent.

### Anti-AI in the Wild: From Toxic Discourse to Action
- arXiv 2611.33254v1 · v1 2026-11-24 16:55 UTC · cs.AI, cs.CR, cs.SI
- Authors: Yage Zhang, Yukun Jiang, Ziqing Yang, Yihan Ma et al.
- Topics: Crawl, Manipulation · score 7 · found via cs.AI, cs.CR, cs.SI
- Link: https://arxiv.org/abs/2611.33254
- Full text: data/fulltext/2611.33254.txt

> Online discussion of generative AI has become increasingly contentious, and communities devoted to supporting, opposing, or debating AI have emerged on social media. Some of these communities take anti-AI actions, such as deploying crawler tarpits and data-poisoning services to interfere with data collection and model training. Yet, the scope of these actions and their relationship to online discourse remain poorly understood. In this paper, we present the first measurement study of online conflict over generative AI, from toxic discourse to anti-AI actions. We collect 931,640 posts from 25 Reddit communities, label them with a large language model detector validated against human labels, identify 3,312 anti-AI actions, and trace the output of three deployed anti-AI tools. Our analysis reveals that 30.0% of posts in communities devoted to this conflict are toxic, compared to 4.4% in general AI communities. Anti-AI actions in these communities mainly target AI crawling or model training data, such as image cloaking and data poisoning. We further examine the implications of these anti-AI actions for AI training, by analyzing the text and code generated from deployed tools. Notably, 66.5% of the code samples generated by a data-poisoning service contain fabricated facts, misused APIs, or broken logic, yet 93.6% passes a public code-curation pipeline, close to the rate for real source code (95.0%). For crawler tarpit output, adding a period to the end of each paragraph increases the curation survival rate from 16.4% to 91.9%. We also find that crawler tarpit and data-poisoning output has already entered Common Crawl, a widely used public web archive, and that crawler tarpit output has also entered FineWeb, a released pretraining dataset. We hope our study can facilitate a better understanding of online conflict over generative AI and its implications for content moderation and AI training.

### Mitigating Overgeneralization in RND via Spectral Target Design
- arXiv 2611.33850v1 · v1 2026-11-25 06:24 UTC · cs.LG, cs.AI
- Authors: Minseok Jeong, Yechan Lee, Hyewon Choi, Jeongyong Yang et al.
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.AI
- Link: https://arxiv.org/abs/2611.33850
- arXiv comment: Accepted to NeurIPS2026
- Journal ref: https://neurips.cc/virtual/2026/loc/sydney/poster/148343
- Full text: data/fulltext/2611.33850.txt

> Random Network Distillation (RND) is a scalable novelty signal for RL based on a fixed random target network and a trained predictor. However, it can overgeneralize: the predictor extrapolates the random target off the data manifold, causing novelty scores to collapse on unfamiliar inputs. This paper analyzes this failure through a kernel-theoretic lens. Under a GP target model and an NTK-regime predictor, we show that the RND novelty score is a cross-kernel residual variance: it is governed jointly by the target covariance kernel and the predictor NTK, rather than by either one alone. This identifies overgeneralization as spectral under-excitation. Motivated by this view, we formulate spectral target design as a principle for shaping RND novelty geometry. As a concrete instance, we replace the implicit random-network target with a bandwidth-controlled Random Fourier Feature (RFF) target, redistributing residual signal toward modes less attenuated by the predictor. Experiments on offline D4RL, online Atari, and Fetch manipulation benchmarks show improved novelty discrimination and downstream RL performance. The code for the RL implementation is available at https://github.com/tuuktuc86/RFF-RND.

### MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance
- arXiv 2611.34188v1 · v1 2026-11-25 11:16 UTC · cs.AI, cs.CL
- Authors: Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen
- Topics: RAG (generic), Manipulation · score 7 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.34188
- arXiv comment: To appear in Proceedings of EACL 2027 (Main conference paper)
- Full text: data/fulltext/2611.34188.txt

> Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack style. We propose a different paradigm: defend by maximizing relevance, not by detecting attacks. Our method, MINE, is training-free and attack-agnostic, and it also serves as a query-conditioned reranker. To evaluate defenses under realistic conditions, we introduce LC-Inj-SQuAD, a long-context benchmark with an average of 4,032 words per context. We evaluate on four datasets spanning short-context QA (Inj-SQuAD, Inj-TriviaQA), long-context QA (LC-Inj-SQuAD), and agent tool-call injection (InjecAgent). Across all four, MINE achieves the best accuracy--security trade-off among training-free defenses. It is also the only defense that stays usable against a fully adaptive attacker, generalizes to agent tool-call injection, and achieves the lowest inference latency on long contexts.

### SoK: When FL Clients Cannot Train -- Delegated Federated Learning for IoT
- arXiv 2611.34876v1 · v1 2026-11-25 18:37 UTC · cs.CR
- Authors: Hamed Mohammed Alkharsh, Aydin Abadi, Jakub Szelag, Suleiman Muhammad Sabo et al.
- Topics: Citation & source selection, Clicks & measurement · score 7 · found via cs.CR
- Link: https://arxiv.org/abs/2611.34876
- arXiv comment: 30 pages, including appendices
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Federated learning (FL) assumes that a client can perform the computation required to produce its own contribution. This assumption is often unrealistic for resource-constrained Internet of Things (IoT) devices, motivating designs that delegate some or all client-side training to more capable parties. We systematize this setting as delegated federated learning (Delegated FL), where data ownership and execution of owner-attributed learning are separated. We develop a framework that examines three dimensions over the same delegated transition: delegate-view privacy, delegated attribution, and constrained-owner feasibility. Our audit of 29 systems reveals a recurring composition gap. Privacy mechanisms protect selected artifacts without necessarily characterizing the accumulated view. Attribution mechanisms establish individual execution relations without necessarily binding the complete delegated transition. Furthermore, computational offloading does not establish whether the remaining workload fits the owner's resource budget. Two controlled studies on Raspberry Pi devices illustrate these gaps. We show that encrypted inputs can coexist with information leakage through an exposed residual and that locally retained labels remain inferable from split-learning gradients. We also show that message authentication can reject tampering without establishing that the executor performed the prescribed computation. Our findings demonstrate why individually established guarantees do not necessarily support the same end-to-end claim and motivate evaluating privacy, attribution, and residual owner cost over the same delegated transition.

### PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents
- arXiv 2611.33144 · v1 2026-11-24 00:00 UTC · 
- Authors: Feixiang Ruan, Guodong Lv, Kewei Zhang, Wenbo Huang et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.33144
- Full text: data/fulltext/2611.33144.txt

> Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explore in parallel for task skills and ways to compose them, and a distilling agent condenses the successful attempts into a task library and one program. During refinement, this program is improved through randomized layouts for enhanced robustness and execution efficiency. In simulated environments, PyRUA-Dex achieves SOTA on Bench2Dex with a score of 72.9 and reaches 81.0% success on DexJoCo under full randomization, ahead of every trained policy on both benchmarks. In real world experiments on a bimanual platform with two 22-DoF hands, PyRUA-Dex learns to play piano, write calligraphy, and other tasks efficiently: learning a new piece from sheet music takes as little as 30 minutes. These results suggest that PyRUA-Dex is an effective framework for developing dexterous manipulation policies with coding agents in the absence of high quality dexterous manipulation demonstrations.

### A comprehensive survey of deep face verification systems adversarial attacks and defense strategies
- arXiv 2611.33231v1 · v1 2026-11-24 10:38 UTC · cs.CV, cs.CR
- Authors: Sohair Kilany, Ahmed Mahfouz
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.33231
- Full text: data/fulltext/2611.33231.txt

> Face Verification (FV) systems have exhibited remarkable performance in verification tasks and have consequently garnered extensive adoption across various applications, from identity duplication to authentication in mobile payments. However, the surge in popularity of face verification has raised concerns about potential vulnerabilities in the face of adversarial attacks. These concerns originate from the fact that advanced FV systems, which rely on deep neural networks, have recently demonstrated susceptibility to crafted input samples known as adversarial examples. Although imperceptible to human observers, adversarial examples can deceive deep neural networks during the testing and deployment phases. These vulnerabilities raised significant concerns about the deployment of deep neural networks in safety-critical contexts, prompting extensive investigations into adversarial attacks and corresponding defense strategies. This comprehensive survey provides a comprehensive overview of recent advances in deep face verification, encompassing a broad spectrum of topics such as algorithmic designs, database utilization, protocols, and application scenarios. Furthermore, we conduct an in-depth examination of state-of-the-art algorithms to generate adversarial examples and the defense mechanisms devised to mitigate such adversarial threats.

### RegionAlign: Manipulating Parameter Layouts for Localized Fault Injection on LLMs and VLMs
- arXiv 2611.33370v1 · v1 2026-11-24 20:02 UTC · cs.CR
- Authors: Xiaomeng Wang, Peter Horvath, Zhengyu Zhao, Martha Larson et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.33370
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Physical fault injection can flip stored weight bits, degrading LLMs and VLMs. Existing work largely overlooks how supply-chain manipulation affects fault vulnerability. We introduce RegionAlign, which allows a malicious provider to manipulate only the parameter layout before deployment, using bit-sensitivity search and channel permutations to concentrate vulnerable bits in one memory region while preserving weight values and clean performance. Under matched budgets, software experiments show greater degradation from search-selected in-region flips with RegionAlign than with original or random layouts. EMFI feasibility study confirms weight corruption. RegionAlign reveals a stealthy supply-chain threat that layout manipulation weakens physical fault resilience.

### Poisoning Self-Evolving Security Policies in LLM Agents
- arXiv 2611.33385v1 · v1 2026-11-24 20:10 UTC · cs.AI, cs.CR
- Authors: Aymen Noor, Honglu Jiang
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.33385
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Self-evolving defenses improve LLM-agent security by learning reusable policies from observed attacks. However, we demonstrate that this learning process itself can become an attack surface. Using SED (Self-Evolving Defense) in the AgentDojo benchmark, we construct a single prompt-injection episode that causes the defense to learn an over-broad policy and subsequently refuse legitimate requests. Across 10 Nemotron runs, every poisoned run over-refuses at least one legitimate task, while unrelated-task performance remains unchanged and the original prompt-injection defense remains effective. The attack also transfers to gpt-oss-120b; however, its poisoning mechanism depends on a successful initial prompt injection and therefore fails to activate when the target agent resists the underlying injection. In contrast, integrity-oriented attacks targeting SED's judge, policy synthesis, retrieval, and organization mechanisms fail in our evaluated settings, identifying over-refusal as the primary exploitable failure mode observed in our experiments. We further identify self-poisoning from false-positive harm judgments without an attacker. Finally, contrastive policy synthesis and an automatic broadness-check gate substantially reduce, but do not eliminate over-refusal, without compromising security in our evaluated settings.

### RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints
- arXiv 2611.33390v1 · v1 2026-11-24 20:14 UTC · cs.RO, cs.AI
- Authors: Qineng Wang, Jianwen Lyu, Pingyue Zhang, Reuben Tan et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.33390
- arXiv comment: 72 pages, 28 figures, 30 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts. These motions depend on the exact geometry of each scene, so demonstrations and skills recorded elsewhere rarely transfer. We therefore ask: when manipulation hinges on spatial constraints, can robots reason out the right motions? We introduce RoboARC, a benchmark of 90 tasks in six constraint types over rigid and soft materials, on three robots in MuJoCo. Every task is a frozen scene with a physics-based grader and a verified reference solution that replays bit-identically. Each task comes in a Privileged regime, with the full simulator state and resets, and a Standard regime with real-sensor inputs (camera images and proprioception) and a single attempt without resets. We evaluate seven coding agents and four VLA policies, none trained on these tasks. The strongest agent, GPT-6 Astra in Codex, solves 86% of the tasks in the Privileged regime and 43% in the Standard regime, and the four VLA policies, run zero-shot, solve none of their 18 one-arm puzzles. On 15 puzzles that GPT-6 Astra solved in the Privileged regime and failed in the Standard regime, object poses add 4 points and part geometry 13, but both together add 36, from 24% to 60%. Only 7% of the coding agents' failed runs pass more than half of a task, and 53% of the failed runs in the Standard regime are stuck on a single step. Frontier coding agents already reason out the right motions for many of these tasks once they know where the parts are and what shape they have. From their own sensors, in a single attempt, the strongest solves fewer than half of the tasks. The website can be found at https://roboarc.embodied-first-exam.ai

### SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation
- arXiv 2611.33915 · v1 2026-11-25 00:00 UTC · 
- Authors: Zeyang Guan, Qihao Zhao, Rui Gong, Zhang Haitian et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.33915
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working context. Once the task ends, it loses this execution knowledge, such as how to carry a bowl between two grippers. On the next attempt at the task, the robot may take just as long and repeat the same mistakes. To avoid this repetition, robots must retain execution knowledge across attempts. Yet replaying past actions is insufficient, because their effects depend on the current conditions. Procedures that determine actions from the current scene address this, but when they meet conditions that earlier attempts did not cover, revising them requires the measured effects of earlier actions. We therefore propose SEEK, an agentic framework that retains both, enabling robots to improve across attempts while keeping the underlying model fixed. To adapt retained knowledge to the current scene, SEEK adopts a Self-Evolving Programmatic Policy (SEPP) that encodes manipulation as executable procedures and determines each action from current observations. As the robot executes these procedures, SEEK records the measured effects of its actions, including those from failed attempts, in a Persistent Action-Effect Bank (PAEB). Where a retained procedure applies, it acts without a model request; where it meets a condition it does not cover, this evidence guides its revision. On RoboDojo, knowledge retained over ten attempts raises SEEK's average task score from 27.0 to 54.4 and its success rate from 19.7% to 48.0% across all 42 tasks. On 34 of these tasks with GPT-6.2 Astra, SEEK reaches 80.1 after five attempts, against 49.6 for the same model acting directly, and uses 77.6% fewer model requests. https://zeyangguan.github.io/SEEK-Agentic-Robot-Manipulation/

### SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator
- arXiv 2611.34750 · v1 2026-11-25 00:00 UTC · 
- Authors: Xiang Li, Hongyu Zhou, Ya-Li Li, Tao Li et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.34750
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result, and writes the next, while a motion planner interpolates between them. The agent decides the number and spacing of keyposes for both fast long-range motion and fine-grained manipulation. This granularity matches the sparsity of teleoperated manipulation: most demonstrations in DROID can be compressed into a few keyposes instead of dense actions. SOLVE grounds keyposes with sparse depth queries answered by noisy sources, such as multi-view triangulation, stereo, or monocular depth, and copes with that noise itself. It also improves from execution feedback, reflecting on its own rollouts and distilling a few rules per task. SOLVE reaches state-of-the-art performance of 74.5% on RoboDojo and 84.5% on RoboLab, with only $1.7 per episode on average, 12x less than previous dense-control agent policies. On a real robot, the same agent achieves an 88% success rate (75 of 85 episodes) over 16 challenging zero-shot tasks. Our project page is at https://serenos.github.io/solve-website.

### WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation
- arXiv 2611.33745v1 · v1 2026-11-25 04:06 UTC · cs.AI
- Authors: Xu Yang, Kailai Sun, Qianchuan Zhao
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.33745
- Full text: data/fulltext/2611.33745.txt

> World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation. Factual transitions alone determine action-wise marginal futures and average effects, but not individual effects or the probability that switching actions causes harm. We introduce WhatIf, a counterfactual world model for manipulation that couples candidate futures through shared latent physics and transition noise inferred from factual history. Each candidate action induces a sparse object-factor causal graph describing the physical pathways it activates. Rolling out these graphs under the shared situation anchors predictions to observed outcomes and confines action contrasts to the objects each action reaches. Shared type-conditioned functions support varying numbers of objects, while a round-trip loss enforces action-invariant abduction without counterfactual labels. We show that replacing an individual effect with its conditional mean incurs mean-squared error equal to its conditional variance, motivating comparisons between coupled futures. Building on these comparisons, Counterfactual Advantage Planning (CAP) ranks plans by their advantage over an incumbent within shared situations and constrains the probability of harm. Paired advantages reduce estimator variance by a factor of $1-ρ$, where $ρ$ is the correlation between branch outcomes, and cancel model errors shared by both branches. Each executed transition provides hindsight advantages to update the physics posterior, the next plan, and an amortized policy without a learned critic. We further establish when observational transitions identify interventional dynamics. Paired simulator interventions evaluate counterfactual accuracy, graph recovery, compositional generalization, and decision quality.

### Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation
- arXiv 2611.33993v1 · v1 2026-11-25 08:46 UTC · cs.RO, cs.AI
- Authors: Lennox Wei, Jiaqi Yao, Shixin Sun, Yuanzheng Zhang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.33993
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution. Although future prediction can inform action correction, an accurate forecast does not establish whether modifying an existing action would be beneficial. We present Aegis-VLA, a world-model-guided vision-language-action (VLA) framework that generates predictive action corrections and separately determines whether and how strongly to apply them. A Trajectory World Model combines kinematic extrapolation with learned residual dynamics to predict object motion and estimate positional uncertainty. Discrepancy-Guided Action Refinement uses differences between history-only and base-action-conditioned end-effector forecasts to propose bounded arm corrections. A Reliability Gate learns when to admit corrections based on demonstration-relative improvements over base actions, and regulates their application during inference using predictive uncertainty and anticipated object--end-effector proximity. Rejected corrections preserve the corresponding base actions. Aegis-VLA introduces only approximately 2.45M trainable parameters. On the simulated Dynamic Object Manipulation (DOM) benchmark, Aegis-VLA achieves 56.72\% success over 1,800 evaluation trials, exceeding our reproduced DynamicVLA baseline of 45.44\% by 11.28 percentage points.

### Hijacking 3D Generation: Targeted Adversarial Attacks against Image-to-3D Models via Prefix Trajectory Alignment
- arXiv 2611.34075v1 · v1 2026-11-25 09:45 UTC · cs.CV, cs.AI
- Authors: Yilong Yang, Jiale Teng, Yule Liu, Yang Liu et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.34075
- arXiv comment: 18 pages, 10 figures
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Online services that deploy Image-to-3D models enable users to generate high-quality 3D assets from a single image. However, the generated 3D geometry can violate content policies and cause broader security risks. To prevent such content, these services typically use policy-restricted inspectors to examine uploaded images before generation. Since the inspector examines only the visible content of the input, a visually benign image can still induce the generation of policy-restricted 3D geometry. However, turning this vulnerability into an effective attack is non-trivial in the black-box setting: global backpropagation through the long DiT generation trajectory is difficult to fit, while different image preprocessing pipelines across services can substantially reduce transferability. In this paper, we present PTA3D, a targeted adversarial attack against Image-to-3D models that addresses these challenges through Prefix Trajectory Alignment (PTA) and Preprocessing Aware Optimization (PAO). PTA progressively aligns the prefix DiT outputs of the adversarial trajectory with those of the target trajectory, where the core geometric structure is formed, allowing the final geometry to be controlled without optimizing through the complete generation trajectory. PAO exposes adversarial optimization to diverse image transformations rather than a single preprocessing pipeline, reducing sensitivity to the mismatch between surrogate and target services. We establish a prefix-to-output bound and a preprocessing-aware transfer bound to theoretically characterize the effectiveness of the two designs. Experiments on three open-source Image-to-3D models and three online services show that PTA3D achieves 41.5%-88.5% ASR on online services and 90.8%-94.6% ASR in white box settings, substantially outperforming existing attacks.

### Poisoning Attacks to Local Differential Privacy Protocols for Dynamic Graphs
- arXiv 2611.34340v1 · v1 2026-11-25 13:14 UTC · cs.CR
- Authors: Shang Liu, Yuhan Bao, Hongbin Zhao, Yanmei Zhang et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.34340
- arXiv comment: 13 pages, 5 figures, submitted to conference. Code available at https://github.com/spiralfood/GraphPoison-LDP
- Full text: data/fulltext/2611.34340.txt

> With the increasing adoption of privacy-preserving techniques in dynamic graph analysis, local differential privacy (LDP) has become a fundamental paradigm for protecting user data in decentralized environments. However, despite its strong privacy guarantees, LDP-based dynamic graph protocols remain vulnerable to data poisoning attacks through malicious data injection. In this paper, we present the first systematic study of data poisoning attacks against privacy-preserving dynamic graphs under the LDP framework. Considering the temporal evolution of dynamic graphs, we identify key challenges in attack design and evaluation, including how to schedule attack resources across time and how to measure cumulative attack impact. To address these challenges, we introduce an absolute gain metric to quantify the overall deviation of graph statistical metrics before and after attacks across time. Based on this metric, we further propose a unified poisoning attack framework for dynamic graphs, which consists of target node selection, dynamic fake node scale scheduling, and fake edge injection. Within this framework, we design a temporal enhanced attack (TEA) strategy that dynamically schedules attack resources to maximize attack effectiveness, along with two baseline strategies, equal-scale attack (ESA) and random-scale attack (RSA), for comparison. Extensive experiments on real-world and synthetic datasets demonstrate that the proposed attacks can significantly degrade the accuracy of graph metric estimation for target nodes.

### VisualMontage: Manipulating the Beliefs of Vision-Language Agents with Authentic Image Sequences
- arXiv 2611.34603v1 · v1 2026-11-25 15:57 UTC · cs.AI, cs.CV, cs.MA, cs.SI
- Authors: Jinwei Hu, Lai Wei, Zhuoyun Li, Youcheng Sun et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.SI
- Link: https://arxiv.org/abs/2611.34603
- arXiv comment: Under Review
- Full text: data/fulltext/2611.34603.txt

> As agents based on vision-language models (VLMs) increasingly interpret social-media content, errors in their analysis may lend credibility to rumors and amplify their spread. In this paper, we study the problem of visual cognitive collusion, in which coordinated posts combine authentic images and locally faithful captions to induce VLM agents to infer and accept attacker-chosen target claims through their own reasoning. To enable systematic evaluation of this cognitive threat, we introduce a new benchmark comprising 544 target cases and 33.2K candidate images across eight application domains. We further propose VisualMontage, a multi-agent framework for simulating such attacks through narrative planning, image selection and ordering, and caption assignment under iterative review. We evaluate this threat through extensive experiments across 12 vision-language models, examining modality effects, production-team components, and downstream defenses. Using identical attack feeds across models without victim-specific optimization, we demonstrate cross-model transferability, achieving mean attack success rates of 61.93% for proprietary models and 68.71% for open-weight models. Moreover, 92.65% of generated feeds pass independent model-based validity auditing. Even after downstream review, residual attack success rates range from 35.3% to 76.7% across the evaluated configurations. Our additional controlled comparisons further reveal that captions can improve model-rated posting naturalness while reducing attack success. Together, these findings reveal a novel cognitive threat in social-media interpretation and motivate safeguards that assess how authentic posts jointly shape agents' reasoning and conclusions.

### CA-RAG: Constraint-Aligned Retrieval for Structurally Faithful Long-Form Generation
- arXiv 2611.33497v1 · v1 2026-11-24 22:18 UTC · cs.AI, cs.CL, cs.IR
- Authors: Vimal Kumar Kumar, Meghana Kshirsagar, Conor Ryan
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.33497
- arXiv comment: 18 pages (including appendix), 5 figures
- Full text: data/fulltext/2611.33497.txt

> Retrieval-augmented generation (RAG) typically optimises evidence selection for semantic relevance, whereas compliance-sensitive long-form generation also requires evidence supporting explicit structural obligations. Semantically relevant retrieval may therefore omit information needed for mandatory downstream clauses. We propose Constraint-Aligned RAG (CA-RAG), a retrieval-conditioning framework that augments section-specific queries with ontology-derived structural constraints and policy-grounded knowledge-graph relations before evidence selection. Retrieval-only evaluation with manually annotated evidence shows consistent improvements across retrieval budgets. At $k=6$, CA-RAG increases Precision@$k$ from $0.5268$ to $0.5692$, pooled Recall@$k$ from $0.5402$ to $0.5950$, and F1@$k$ from $0.5389$ to $0.5672$ over standard RAG. Generation experiments further show improvements in compliance and reliability in several model--domain settings, while generation-only constraints achieve higher clause coverage but lower overall compliance and reliability. These results indicate that structurally aligned retrieval can improve evidence sufficiency in compliance-sensitive long-form generation.

### Privacy-Aware Adaptive Client Selection for Federated Retrieval-Augmented Generation
- arXiv 2611.33890v1 · v1 2026-11-25 07:05 UTC · cs.IR, cs.DC
- Authors: Ali Shams Saryazd, Abolfazl Gandomi
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.33890
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Federated retrieval-augmented generation retrieves evidence from distributed corpora. However, broadcasting queries to all clients increases the retrieval burden and query exposure. We present Privacy-Aware Adaptive Client Selection for Federated Retrieval-Augmented Generation (PACS-FedRAG), an online selector that takes into account perturbed semantic profiles along with evidence feedback, latency, payload cost, and exploration. In a ten-client setting where three clients are chosen, the archived end-to-end benchmark reports an evidence overlap of 0.372 and an answer accuracy of 0.287. The retrieval-only evaluation, on the other hand, reuses a full-broadcast baseline with a different fusion tie-breaking policy. Rank fusion across disjoint client corpora imposes an overlap ceiling of 0.375, limiting its interpretation as a relevance measure. Answer accuracy is below the fixed-label diagnostic of 0.645, and raw generator responses are unavailable for parser verification. Corrected baselines and a new answer-level evaluation are needed to assess whether quality is preserved. Selecting three clients reduces the number of query recipients by 70%. Profile perturbation does not provide confidentiality of queries or passages.

## Other new cs.IR papers, title only (9)
- Community Notes Across Platforms: Evaluating the Feasibility of Re-using Crowd-sourced Context Notes — https://arxiv.org/abs/2611.33546
- Multi-Modal Causal Disentanglement for Multi-Domain Sequential Audio Recommendation — https://arxiv.org/abs/2611.33628
- Structure-Aware Multimodal Retrieval Under Data Scarcity, Privacy Constraints and Out-of-Domain Content — https://arxiv.org/abs/2611.33649
- MulCLIP: A Multi-level Alignment Framework for Enhancing Fine-grained Long-context CLIP — https://arxiv.org/abs/2611.34083
- RecField: Embedding Recommendations into Spatial Movie Organization as Affordances for Serendipitous Encounters — https://arxiv.org/abs/2611.34330
- ConTra: A Training Framework for Effective Contextual Retrieval via Prefix Generation — https://arxiv.org/abs/2611.34366
- Agentic Waterfall: An Intent-Driven Information Discovery Framework for Reclaiming User Control in the Attention Economy — https://arxiv.org/abs/2611.34407
- Grounding User Preferences in Shared Multimodal Concepts for Recommendation — https://arxiv.org/abs/2611.34436
- Procedure Inference as Memory: Learning Recruiter Decision Procedures from OKF-Structured Episodes in Multi-Session Hiring Assistants — https://arxiv.org/abs/2611.34576

## Already listed on an earlier day, still inside the look-back window (103)
- Fetch, Read, Reuse: How AI Search Agents Bend the Web's Rules — https://arxiv.org/abs/2611.30546 (score 28)
- Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection — https://arxiv.org/abs/2611.29268 (score 14)
- Can Search Agents Correct Their Own Errors? Evaluating Retrieval, Evidence Delivery, and Answer Completion — https://arxiv.org/abs/2611.30243 (score 14)
- Bug Bounty Programs in the AI Era: How Does Platform Anti-Spam Friction Affect Vendor Profitability? — https://arxiv.org/abs/2611.30615 (score 14)
- Leakage-Safe Auditing of Attribution-Driven Data Curation in Medical Imaging — https://arxiv.org/abs/2611.31096 (score 14)
- CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting — https://arxiv.org/abs/2611.31185 (score 14)
- Bathys: Advancing Deep Search Agents — https://arxiv.org/abs/2611.32660 (score 14)
- SOARS: System One Assisted Reranking for Agentic Search — https://arxiv.org/abs/2611.32917 (score 14)
- Ask Again: Answer-List Instability in Generative Engines — https://arxiv.org/abs/2611.30819 (score 13)
- Adaptation or Poisoning? Security Risks of Conversational Test-Time Learning in Large Language Models — https://arxiv.org/abs/2611.29532 (score 11)
- CompareDR: Benchmarking Deep Research Reports from Individual Quality to Comparative Merit — https://arxiv.org/abs/2611.29549 (score 10)
- SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health — https://arxiv.org/abs/2611.29988 (score 10)
- Disclosure Bias in AI Reviewers — https://arxiv.org/abs/2611.30410 (score 10)
- CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons? — https://arxiv.org/abs/2611.30727 (score 10)
- ComputeWise: Measuring and Fixing GPU Waste by AI Research Agents — https://arxiv.org/abs/2611.31027 (score 10)
- ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents — https://arxiv.org/abs/2611.31198 (score 10)
- Geo-SMILE: Statistical Model-Agnostic Interpretability with Local Explanations for Geospatial Machine Learning — https://arxiv.org/abs/2611.31731 (score 10)
- Emerging International Best Practices for AI Model Specs — https://arxiv.org/abs/2611.32768 (score 10)
- Can Cities Have Personalities? Introducing the SCD City Personality Assessment — https://arxiv.org/abs/2611.30733 (score 9)
- Marketing-Bench: Evaluating Frontier Models and Agents on Real-World Marketing Capabilities — https://arxiv.org/abs/2611.32012 (score 9)
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
- A dataset of clinically similar image pairs from citation-linked case reports for medical image retrieval — https://arxiv.org/abs/2611.31465 (score 8)
- AdProducer: Towards Agentic Advertising Video Generation — https://arxiv.org/abs/2611.31466 (score 8)
- One Step, Four Clocks: How GUI Agents Fall Out of Step — https://arxiv.org/abs/2611.31522 (score 8)
- COGENT: A Modular Cognitive Architecture for Agentic User Simulation — https://arxiv.org/abs/2611.31559 (score 8)
- Are Web Agents Still Detectable? Stress-Testing Bot Defenses with Coordinated Evasion — https://arxiv.org/abs/2611.31962 (score 8)
- Audits Need Access, Data, and Compute. But How Much? — https://arxiv.org/abs/2611.31968 (score 8)
- When Learned IDS Model Selection Collapses to a Static Choice: A Measurement Study at the Edge — https://arxiv.org/abs/2611.29968 (score 7)
- LLM Agent Authorization Across Context Compaction — https://arxiv.org/abs/2611.32194 (score 7)
- More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation — https://arxiv.org/abs/2611.29339 (score 6)
- When Successful Collaboration Becomes an Attack Surface: Insider Memory Poisoning in Multi-Agent Systems — https://arxiv.org/abs/2611.31307 (score 6)
- MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model — https://arxiv.org/abs/2611.29501 (score 6)
- Relativising Integrity and Robustness: Prompt Injection and Partitioned Enclaves — https://arxiv.org/abs/2611.29802 (score 6)
- Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection — https://arxiv.org/abs/2611.29977 (score 6)
- Differential Proteomics to Symbolic Rules: An Audit of SHAP Guidance in Lung Adenocarcinoma — https://arxiv.org/abs/2611.29989 (score 6)
- Spiking World-Action Models for Robotic Manipulation — https://arxiv.org/abs/2611.30041 (score 6)
- A statistical measure of trust in generative AI — https://arxiv.org/abs/2611.30286 (score 6)
- Automated Call for Action: RAG-Based Environmental Law Enforcement Screening System — https://arxiv.org/abs/2611.30423 (score 6)
- JEPA-ICL: Progress-Aligned Latent Plans for In-Context Robotic Manipulation — https://arxiv.org/abs/2611.30516 (score 6)
- RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation — https://arxiv.org/abs/2611.30555 (score 6)
- How Many Parameters Does Forecasting Need? A Survey and Code-Level Audit of Lightweight Long-Term Time Series Forecasting — https://arxiv.org/abs/2611.30685 (score 6)
- What People Choose Not to Say: A Multimodal Benchmark for Fine-Grained Information Manipulation in Conversations — https://arxiv.org/abs/2611.31346 (score 6)
- ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection — https://arxiv.org/abs/2611.31424 (score 6)
- Frequency-Conditioned Privacy Auditing of Fine-Tuned Language Models — https://arxiv.org/abs/2611.31581 (score 6)
- FoveaWAM: Role-Aware 4D World-Action Modeling for Dynamic Manipulation — https://arxiv.org/abs/2611.31705 (score 6)
- EffectWAM: Learning Action-Grounded Effects for Robot Manipulation — https://arxiv.org/abs/2611.32053 (score 6)
- Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation — https://arxiv.org/abs/2611.32238 (score 6)
- Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning — https://arxiv.org/abs/2611.32304 (score 6)
- Gamification in the age of AI: surveying player perceptions of motivation, manipulation, and data protection — https://arxiv.org/abs/2611.32464 (score 6)
- Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation — https://arxiv.org/abs/2611.32533 (score 6)
- MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory — https://arxiv.org/abs/2611.32564 (score 6)
- When "Neutral" Means Irrelevant: A Construct-Validity Audit of NormAd-ETI — https://arxiv.org/abs/2611.32614 (score 6)
- ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning — https://arxiv.org/abs/2611.32639 (score 6)
- DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation — https://arxiv.org/abs/2611.32654 (score 6)
- MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation — https://arxiv.org/abs/2611.32803 (score 6)
- Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression — https://arxiv.org/abs/2611.31089 (score 5)
- Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance — https://arxiv.org/abs/2611.33098 (score 5)
- ChatGPT Can't Sell (And That's Probably a Good Thing): Buyer-Aligned AI Advice, the Sales-Representative Gap, and Evidence from Commercial Conversations — https://arxiv.org/abs/2611.28946 (score 4)
- Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and Judgement in Evidence-Grounded Verification — https://arxiv.org/abs/2611.29697 (score 4)
- Towards Realistic Evaluation of Uncertainty Quantification for LLM-Based Recommender Systems — https://arxiv.org/abs/2611.33036 (score 4)
- DataRecycle: Trustworthy Distillation of Structured Data from Scattered Web Evidence — https://arxiv.org/abs/2611.29206 (score 3)
- SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance — https://arxiv.org/abs/2611.30588 (score 2)
- Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounded Policy Assistant — https://arxiv.org/abs/2611.32266 (score 2)
- LLM-Based Assistant for Dog Care Guidance — https://arxiv.org/abs/2611.29286 (score 1)
- Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees — https://arxiv.org/abs/2611.29966 (score 1)
