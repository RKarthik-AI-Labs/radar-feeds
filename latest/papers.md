# Paper candidates — 2026-11-04 (IST)

Generated 2026-11-04 06:56 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 30 new topic matches · 11 other new cs.IR · 123 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (30), highest score first

### Characterizing Adversarial GEO via Implicit Brand Injection
- arXiv 2611.04005v1 · v1 2026-11-02 21:49 UTC · cs.AI, cs.IR
- Authors: Shobhnik Kriplani, Haohan Wang
- Topics: GEO/AEO, Brand/product recommendation, Manipulation · score 21 · found via cs.AI, cs.IR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2611.04005
- arXiv comment: Preprint. Under Review
- Full text: data/fulltext/2611.04005.txt

> Generative search engines increasingly shape how users discover products, services, and commercial entities by generating answers from retrieved web content. This creates an opportunity to influence which brands appear in these answers by modifying the content available to the retrieval system. In this work, we study an adversarial generative engine optimization (GEO) setting in which a predefined brand is added to an article through a single contextually integrated mention. The challenge is to make the mention fit the surrounding article without making the content overtly promotional, while keeping it relevant enough to be retrieved and to influence the generated answer. To study this, we introduce Implicit Brand Injection (IBI), a multi-agent framework that identifies insertion locations, rewrites the selected sentence, verifies the edit, and selects the final candidate. To evaluate IBI at scale, we construct IBIBench, which contains 1,000 web articles and 60 synthetic brands across 12 diverse domains, with both endemic and non-endemic brand placements. We compare IBI with Direct Prompting and Best-of-N with ranking under an equivalent budget, evaluating insertion quality, target-chunk retrieval, and downstream brand propagation. Compared with the baselines, IBI produces insertions that better preserve semantics and disrupt perplexity less, while improving Hit@k across all evaluated cutoffs, query regimes, and placement settings. IBI achieves up to 82.2% Hit@10 and 0.74 MRR@10, while Brand Mention Rate (BMR) and Conditional Propagation (CP) reach up to 62.7% and 75.9%, respectively. These results show that a single brand mention can increase both retrieval exposure and brand visibility in generated responses, highlighting the need for defenses against implicit content manipulation in generative search.

### IntentGEO: Intent-aware Generative Engine Optimization for Recommendation
- arXiv 2611.04225v1 · v1 2026-11-03 03:04 UTC · cs.AI, cs.IR
- Authors: Runlin Lei, Shiqi Zhang, Xiaokui Xiao, Zhewei Wei
- Topics: GEO/AEO, Citation & source selection, Brand/product recommendation · score 18 · found via cs.AI, cs.IR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2611.04225
- arXiv comment: 12 pages, 3 figures
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) increasingly shape recommendations across chatbots, e-commerce, and user-generated content (UGC) platforms, creating demand for Generative Engine Optimization (GEO) to improve item visibility in generated responses. Existing GEO studies are mainly content-centric, optimizing visibility under general-purpose queries. However, a shared item description usually serves users with different needs and decision goals, resulting in its visibility gains being dependent on the request. To investigate how changing intent affects visibility, we formulate IntentGEO to evaluate shared rewrites across need specificity and decision progression. We revisit existing GEO methods and find that their visibility gains vary across user intents. More critically, learning-based prompt optimization can underperform its handwritten seed on average. Tracing these updates reveals prompt drift from explicit recommendation instructions toward generic promotional tactics. To address this drift, we propose AMO (Anchored Meta-Optimization), which preserves recommendation instructions in a fixed core while learning appended strategies from citation feedback. Across four domains and ten intent states, AMO improves average citation-rank gain by 35% over the strongest prior learning-based baseline and leads on nine states. Ablations show that learned additions improve on the fixed core alone and that AMO outperforms full-prompt optimization initialized from that core. It also achieves the highest gains in an agentic recommendation pipeline and, after separate adaptation, on Doubao, a commercially deployed, closed-source online assistant. These findings highlight user intent as a key dimension of GEO evaluation and support anchored adaptation across recommendation needs and decision stages.

### The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents
- arXiv 2611.03754v1 · v1 2026-11-02 11:06 UTC · cs.AI, cs.CR
- Authors: Geyuan Wang, Shunyu Liu, Siyuan Liang, Chenyang Lyu et al.
- Topics: Query fan-out, Manipulation · score 13 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.03754
- arXiv comment: Accepted at NeurIPS 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large Language Models (LLMs) have shown promise for empowering search agents to tackle complex information-seeking tasks. However, since acquiring external information necessitates web search, these agents are highly susceptible to various adversarial attacks (e.g., malicious information injection or stealthy context manipulation). Existing attack strategies inevitably rely on static and human-crafted templates, failing to emulate the dynamic and complex nature of real-world threats. In this paper, we propose an adversarial self-evolution framework that integrates bi-level optimization between the attacker's strategy evolution and the defender's adaptive mitigation, to expose the vulnerabilities of search agents. Specifically, we introduce the Contrastive Rollout Evolutionary Optimization (CREO) method to drive the directional evolution of the attack strategy population via contrastive evolutionary signals. To provide a stable environment for this continuous evolution, we further construct a controlled sandbox and design fine-grained metrics to quantify internal vulnerabilities. Extensive experiments across various multi-hop QA benchmarks and frontier LLMs demonstrate that the proposed framework yields attack efficacy superior to static baselines, underscoring the urgent need to develop more robust defense frameworks.

### $τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems
- arXiv 2611.04459v1 · v1 2026-11-03 07:47 UTC · cs.AI, cs.CL, cs.IR
- Authors: Bharath Sivaram Narasimhan, Karthik R. Narasimhan
- Topics: Citation & source selection, Brand/product recommendation · score 12 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.04459
- arXiv comment: 16 pages, 3 figures, 4 tables. Submitted to ECIR 2027 (Resource Track)
- Full text: data/fulltext/2611.04459.txt

> While conversational recommendation systems provide a more natural user interface, they face the challenge of progressively discovering a user's needs before they can recommend an item that satisfies them. To evaluate the ability of AI agents at this elicitation process, we introduce $τ$-Rec-Books, a benchmark that holds each user request fixed while varying only when the user reveals their requirements: all at the start (volunteer), one at the start and the rest when asked (mixed), or some never (hidden). A hidden requirement can be found only by proposing books and inferring it from the user's accept or reject verdicts. We generate 450 tasks over a catalog of 20,000 books from Wikidata, develop a rule-based simulated user to answer the agent, and score recommendations against catalog metadata without an LLM judge. Across four agents and two search interfaces, success rates fall for every agent and interface, on average from 0.975 (volunteer) to 0.756 (mixed) and 0.283 (hidden). Mixed tasks fail mainly because agents do not ask, and when told to ask, every agent reaches at least 0.931. On hidden tasks, most failures come from agents recommending a book they never proposed to the user. When told to propose first, agents only match a simple baseline that proposes popular books, and stay well below one that uses rejection to rule out possible requirements. We release the catalog pipeline, task generator, simulated user, validators, reference agents, and all agent traces at https://github.com/nbharaths/tau-rec/tree/main/data/tracks/books-wikidata-v2.

### ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud
- arXiv 2611.04879v1 · v1 2026-11-03 13:31 UTC · cs.AI
- Authors: Yutao Wu, Xiao Liu, Ming Wen, Hanxun Huang et al.
- Topics: Agents, Manipulation · score 11 · found via cs.AI, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.04879
- arXiv comment: 15 pages, 17 figures, 7 tables. Code: https://github.com/wuyoscar/scamworld-bench
- Full text: data/fulltext/2611.04879.txt

> Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter online fraud designed to deceive humans, including fraudulent online stores, fake investment platforms, and advance-fee schemes. How web agents respond to such fraud during task execution remains underexplored, in part because scam websites are short-lived, making systematic evaluation difficult. To address this gap, we introduce ScamWorld, an interactive environment that reconstructs reported scam websites across diverse scenarios, fraud mechanisms, and languages. Each reconstructed website reproduces documented fraud mechanisms, making relevant signs of fraud observable before the agent's final action and enabling controlled, repeatable evaluation. Through an extensive study of web agents powered by six frontier LLMs, we find that baseline deception rates range from 11% to 35% across models. Agents proceed more readily with payments than with requests for credentials or wallet information. A closer analysis of agent trajectories shows that some agents acknowledge suspicious conditions yet proceed, at times treating the user's instructions as authorisation to accept additional terms imposed by the website. ScamWorld provides a reusable testbed for systematically evaluating and stress-testing web agents against real-world online fraud.

### StreamDuo: A Live Commentator and a Research Agent for Unseen Games
- arXiv 2611.01120 · v1 2026-10-31 00:00 UTC · 
- Authors: Zixian Gao, Penghao Luo, Xiangcheng Cao, Lixin Xiu et al.
- Topics: Query fan-out · score 10 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.01120
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowledge of the game world. We propose StreamDuo, which pairs a trainable commentator with a frozen research agent that reads the wiki of the game being played. When the commentator sees something it cannot name, it sends the current frames, and the research agent returns a few wiki entries two seconds later while the stream continues. We train only the commentator, on a single game, in two stages. Information-gain labels teach it to ask only where an answer would help it say what the human caster said, and on-policy self-distillation from a copy of itself that sees the ideal answer teaches it to use noisy answers. Trained on Baldur's Gate 3 and tested on ten unseen games, StreamDuo raises entity recall from 0.082 to 0.116 over Proact-VL trained on the same data, cuts source-game leakage from 9.9% to 1.0%, and achieves the best timing and the highest judged liveliness and overall quality among streaming models.

### EMBERS: Empirically Motivated Robustness Testing of Deep Research Systems via Defect-Guided Fuzzing
- arXiv 2611.03723v1 · v1 2026-11-01 06:27 UTC · cs.AI, cs.LG
- Authors: Shuochuan Li, Zan Wang, Dong Wang, Yuhang Jiang et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.03723
- Full text: data/fulltext/2611.03723.txt

> Deep Research (DR) systems extend large language models into autonomous agents that decompose complex information needs, iteratively search the web, and synthesize evidence to answer challenging questions. However, their multi-stage execution may introduce robustness risks, as variations in user questions or intermediate search inputs may propagate across research stages and lead to incorrect answers. Existing evaluations focus on task-solving capabilities or robustness against external evidence disturbances, leaving intrinsic weaknesses in DR execution insufficiently explored. Thus, we conduct an empirical study of 1,932 execution trajectories from three representative DR systems and identify nine recurring defect categories across subquestion formulation, online search, and final reasoning. Guided by these findings, we propose EMBERS, an empirically motivated, defect-guided fuzzing framework for robustness testing of DR systems. Starting from correctly answered seed questions, EMBERS generates stage-targeted test inputs using defect-guided mutation, web-search-assisted fidelity assurance, and diversity-aware seed maintenance. Experiments across 16 framework--model--dataset settings show that EMBERS achieves 3.21 times the failure-discovery throughput of the strongest baseline under identical testing budgets. Human and LLM-assisted evaluations demonstrate that most generated inputs preserve the original information need and necessary contextual constraints. Moreover, model fine-tuning experiments show consistent-answer performance improvement, highlighting their value for robustness testing and model improvement.

### SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use
- arXiv 2611.03982v1 · v1 2026-11-02 21:22 UTC · cs.AI, cs.CL
- Authors: Rongzhe Wei, Ge Shi, Min Cheng, Sarthak Ghosh et al.
- Topics: Brand/product recommendation · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.03982
- arXiv comment: 20 pages, 13 figures, 6 tables. Camera-ready version for the NeurIPS 2026 Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks (AABA4ET). Project page: https://geshijoker.github.io/slate/
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Enterprises increasingly want LLM agents to automate standard operating procedures over their software stacks -- mapping each step of a procedure to the right call among thousands of internal APIs, without hand-authored step-to-API mappings. The core difficulty is API selection at scale: choosing and composing the correct tools over a long horizon, judged only by whether the overall task succeeds. Current tool-use benchmarks do not test this regime -- they expose only a handful of tools, evaluate single-step invocation, or grade multi-step behavior with subjective LLM-as-a-judge scores that penalize valid alternative trajectories. We introduce SLATE (Synthetic Large-scale API Toolkit for E-commerce), a large-scale benchmark that tests large-toolset, long-horizon API selection in a realistic enterprise domain. SLATE couples (i) queries decomposed into hierarchical, tool-grounded procedures over a ~1,000-tool e-commerce library, (ii) a deterministic, context-aware simulator that returns recorded outputs for matching calls and default responses otherwise, and (iii) an end-to-end task-success metric -- a task succeeds when it reaches every reference outcome -- that credits diverse-but-valid trajectories while remaining fully automatic and reproducible. Experiments with six open decision models and the language models they are built on, from 3B to 12B parameters, show that even the best model completes only 5.0% of the tasks, establishing SLATE as a challenging testbed for reliable enterprise tool use. We release SLATE, its simulator, and the evaluation harness at https://geshijoker.github.io/slate/

### AdSteer: Native Advertising in Large Language Model Generation
- arXiv 2611.04147v1 · v1 2026-11-03 01:40 UTC · cs.CL
- Authors: Shuhang Lin, Chuhao Zhou, Zhenyu Wang, Xiao Lin et al.
- Topics: Ads · score 8 · found via cs.CL, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.04147
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language model (LLM) services face rapidly rising serving costs. To sustain free or affordable access for a broad user base, alternative monetization mechanisms are needed. Native advertising offers a promising approach, as it creates economic value by aligning user intent with merchant offerings. Yet how to integrate sponsored content naturally into LLM responses remains largely underexplored. Existing approaches primarily rely on prompt-level injection, multi-pass rewriting, or fine-tuning, which can compromise response quality or introduce additional computational costs. We propose AdSteer, a lightweight decoding-time advertising framework that adaptively adjusts token probabilities to integrate contextually appropriate advertisement into responses. AdSteer calibrates the strength and duration of advertising influence, making sponsored content a natural part of the response. Experiments on GEM-Bench across three application scenarios show that AdSteer achieves an average improvement of 14.1% in overall score over the strongest baselines and 22.5% fewer total tokens on average than rewrite-based methods. These results demonstrate that AdSteer provides an effective and practical solution for native advertising in LLMs.

### Reliability Stress Testing of RAG Retrieval under Query-Relevant Corpus Poisoning
- arXiv 2611.04264v1 · v1 2026-11-03 03:52 UTC · cs.AI
- Authors: Janet Sung, Kainan Zhou, Gangzhen Qian, Hang Xiao et al.
- Topics: RAG (generic), Manipulation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.04264
- Full text: data/fulltext/2611.04264.txt

> External text can affect a retrieval-augmented generation (RAG) system only after the retriever admits it to the model context. We stress this admission step while varying document content, attacker query information, per-target poison budget, and contamination scope. Across 623 Benchmarking Information Retrieval (BEIR) queries from SciFact and NFCorpus, five query-targeted documents per query reduce classical-retriever nDCG@10 by 40.2-61.5% in isolated-target stress. Full-query anchoring explains most Best Matching 25 (BM25) degradation, whereas appended text also shifts latent semantic analysis (LSA) and Hybrid rankings. A pretrained BGE-small validation reaches 100% target exposure for query-only P=5 on both datasets; adding the injection payload changes SciFact nDCG only from 0.269 to 0.271 and lowers NFCorpus exposure slightly to 98.8%, indicating that query anchoring remains the dominant retrieval-side factor for this dense model. Query length materially changes the interpretation of partial-information attacks: on 162 long SciFact queries, two random terms cover 19.9% of eligible terms and still yield 39.5% Hybrid target exposure. Multi-target contamination adds cross-target interference. Overlap-based admission can remove full-query poisons but may sharply reduce clean retrieval utility, and maximal marginal relevance (MMR) leaves exposure unchanged under the tested configuration. The study measures retrieval-layer failures, not downstream instruction following.

### SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local Search
- arXiv 2611.04662v1 · v1 2026-11-03 10:50 UTC · cs.IR
- Authors: Chenxu Wang, Wenxuan Yang, Yueqi Mou, Shuxian Bi et al.
- Topics: Query fan-out, Clicks & measurement · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04662
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Proactive query recommendation aims to suggest relevant search queries to users on the homepage of local service apps. Unlike conventional recommendation over a fixed item set, this requires open-set generation from a vocabulary of millions, where outputs must simultaneously align with user preference, match fine-grained spatiotemporal context, cover long-tail intents, and provide diverse alternatives within a few candidate slots. Existing approaches address these axes in isolation: standard tokenization suppresses long-tail queries, coarse location encoding misses fine-grained geographic demand, generic preference optimization fails to align with production impression-click distributions, and standard beam search collapses to near-duplicate outputs. We present SPADE (Spatiotemporal Preference Alignment and Diversity Enhancement), an end-to-end generative framework that jointly optimizes the generation space, contextual representation, preference distribution, and output slate quality through four components: Objective-Aligned BPE (OA-BPE) aligns subword merging with business value signals to boost long-tail query generation probability; Spatio-Temporal Adaptive Representation (STAR) replaces coarse location tokens with continuous multi-scale encodings and soft gating for precise spatiotemporal grounding; MARS-DPO (Multi-dimensional Adaptive Reward Sampling DPO) combines cross-domain pre-training with preference alignment on production impression-click data via composite rewards and adaptive hard negative sampling; and Sigmoid Diversity Beam Search (SDBS) improves intent coverage without sacrificing recall. Offline experiments on large-scale production data show that SPADE outperforms the strongest generative baseline by +5.6% HR@5, -40.3% GeoC@5, and +1.9% Exec@5. A one-week online A/B test confirms production impact: +1.88% Module CTR, +0.177% Search Volume, and +0.105% Search DAU.

### Learning to Rank Explanations for Recommendation with Language Models
- arXiv 2611.04775v1 · v1 2026-11-03 12:15 UTC · cs.IR
- Authors: Ben Kabongo, Vincent Guigue
- Topics: Brand/product recommendation · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04775
- arXiv comment: 12 pages, 5 figures, 7 tables
- Full text: data/fulltext/2611.04775.txt

> Recommender systems are ubiquitous on the Web, making understandable explanations essential for users. Although large language models (LLMs) increasingly generate natural-language justifications, evaluating their factual grounding and personalized relevance remains challenging. Statement-level ranking offers an alternative by selecting concise, review-derived explanations, enabling fine-grained and reproducible evaluation using established ranking metrics. However, existing statement ranking methods largely rely on collaborative representations, while semantic enhancements often fail to outperform simple user-history popularity baselines. Moreover, directly adapting language models for personalized statement ranking remains largely unexplored. In this work, we introduce LMStaR (Language Models for Statement Ranking), a fully text-based framework that formulates personalized explanation ranking as dense retrieval. A query encoder represents the user's interaction history and target-item metadata, while a statement encoder maps candidate explanations into a shared embedding space. Both encoders are jointly adapted through multi-positive contrastive learning to learn personalized relevance. Experiments on Amazon Beauty, Amazon Toys, and Yelp show that LMStaR achieves the highest NDCG@1 across all three domains, outperforming CLER by 1.06--8.25 points (+11.8--65.9%). It also leads top-five ranking on both Amazon datasets, although CLER remains stronger on Yelp. Task-specific adaptation improves all five evaluated backbones and transfers across domains without target-domain fine-tuning. Counterfactual analyses further reveal the importance of user-specific histories. These findings highlight the potential of task-adapted language models for personalized explanation ranking.

### RuntimeTickets: Source-Grounded Security Obligations for Agent Skills
- arXiv 2611.03772v1 · v1 2026-11-02 17:31 UTC · cs.AI, cs.CR
- Authors: Kuiyi Gao, Xue Liu, Bowei He
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.03772
- arXiv comment: 27 Pages, Submitted to ICLR 2027 (Under review)
- Full text: data/fulltext/2611.03772.txt

> Third-party Agent Skills extend what an autonomous agent can do, but a malicious Skill can hide data exposure or output manipulation inside a legitimate workflow. Neither reading a Skill's description nor granting it tool permissions tells whether its execution meets the user's security requirements. We introduce RuntimeTickets, a protocol that enforces and audits these requirements while a Skill runs. From released malicious-Skill datasets we derive a risk model and build adversarial-benign Skill pairs. From the task's delivery contract, a language model proposes security obligations for that task. Each obligation cites the Skill lines it answers, and the ticket tightens the host's approvals into fine-grained allowed actions but never loosens them. A runtime gate checks the recipient, object and amount of every outbound send before forwarding it, and trusted monitors record the effects within their observation scope. The ticket links these checks and observations to the approved obligations of each Skill run, and a deterministic decoder turns the ticket's status into governable data flows and verifies each obligation. Neither enforcement nor decoding involves a language model, so text injected by a Skill can change the proposal but never the rule that decides a send. We evaluate RuntimeTickets at the network egress boundary of three unmodified agent frameworks against production Skill scanners and runtime baselines, among them an AgentBound-derived allow-list and SkillGuard. RuntimeTickets eliminated both failure modes of current Skill defenses, overlook (malicious Skills let through) and overkill (benign Skills blocked): its overlook rate was 0.0% and its overkill rate 0.0%, while the scanners erred on both sides. RuntimeTickets ties approved requirements to verifiable execution evidence and offers a common foundation for the safe and auditable deployment of third-party Skills.

### From Benchmarks to Behaviors: A Framework for Auditing AI Agents
- arXiv 2611.03939v1 · v1 2026-11-02 20:41 UTC · cs.HC
- Authors: Nick Hagar
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.HC
- Link: https://arxiv.org/abs/2611.03939
- arXiv comment: 39 pages, 4 figures
- Full text: data/fulltext/2611.03939.txt

> Generative AI systems increasingly mediate access to information. Their behavior depends on tools, instructions, and user memories that are often difficult for researchers to observe or control. Here, I introduce TRACE (Transparent Research on Agent Contexts and Environments), a framework for systematically auditing how these components shape AI agent behavior. Built on an open-source agent harness, TRACE enables controlled manipulation of system components. It also records inputs, outputs, and task execution for downstream analysis. I demonstrate this framework through an experiment examining how user memories influence source selection when agents answer questions about the 2026 U.S. midterm elections. I find that memories expressing explicit preference for a publisher increase its inclusion among the first three cited sources in a response by 33-39 percentage points. Memories identifying the user as a Republican or expressing distrust of mainstream media shift citations rightward. That same media distrust memory also increases citation of sources expressing misinformation or conspiracy theories by 6.3 percentage points, with substantial variation across models. These findings demonstrate that concise user memories can alter source selection in consequential settings, even when questions and search results remain fixed. TRACE extends algorithm auditing to agent harnesses, providing a transparent way to study agent behaviors that benchmarks or commercial interfaces may struggle to isolate.

### ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix Reuse
- arXiv 2611.04259v1 · v1 2026-11-03 03:51 UTC · cs.IR
- Authors: Xujing Wang, Yufeng Chen, Boxuan Zhang, Chao Wei et al.
- Topics: Clicks & measurement, Ads · score 7 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04259
- Full text: data/fulltext/2611.04259.txt

> Larger generative retrieval models can improve retrieval quality, but their decoding cost makes low-latency serving difficult. When different users submit the same query, generating complete Semantic IDs (SIDs) for every request repeats computation, while their interaction histories call for different results. The challenge is to reuse large-model computation across requests while keeping retrieval personalized. We propose \textbf{ReuseGR}, which separates query-level candidate planning from request-level personalized completion. A 7B offline planner generates SID prefix sets shared across requests with the same query. A 0.5B online model uses each request's history to select prefixes and generate the remaining tokens. ReuseCut chooses a cache depth for each query based on historical coverage, balancing computation reuse and candidate coverage. To strengthen online completion, we transfer 7B suffix-scoring knowledge to 0.5B through path-level knowledge distillation (Path KD). BudgetCut then selects scored branches to improve final top-100 recall under a fixed branch budget. Its selection policy is initialized by on-policy distillation (OPD) and refined through group-relative policy optimization (GRPO). On an industrial search-advertising dataset with approximately 2M query--item records and 3.38M catalog items, ReuseGR improves query-level HR@100 by 3.83 percentage points and reduces mean online latency by 38.9\% relative to an all-online 0.5B baseline when prefixes are prepared. It achieves HR@100 comparable to an all-online 7B baseline with 57.7\% lower online latency. A 14-day user-level online A/B test against the 0.5B baseline shows relative gains of 0.93\% in click-through rate and 1.05\% in revenue per thousand requests.

### Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents
- arXiv 2611.04393v1 · v1 2026-11-03 06:26 UTC · cs.AI, cs.CL, cs.CR, cs.LG
- Authors: Ilan Zendel, Matan Levy, Stav Cohen, Avi Mendelson et al.
- Topics: Agents, Manipulation · score 7 · found via cs.AI, cs.CL, cs.CR
- Link: https://arxiv.org/abs/2611.04393
- arXiv comment: Accepted at NeurIPS 2026 (Main Track). 17 pages, 7 figures, 8 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLM agents increasingly act on information retrieved from public sources they treat as credible, which turns a manipulated recommendation into a transaction, a dependency, or a decision with physical consequences. The security literature models this threat as instruction injection, in which an adversary writes a command into retrieved content and deployed defenses learn to recognize command syntax. We show that an attacker can instead steer an agent through the agent's own harm-avoidance. A single fabricated hazard, written as an ordinary review, leads the agent to disqualify the legitimate options and select the attacker's target by its own reasoning, with no command for a detector to recognize. We call this voluntary servitude. These payloads steer agents about as often as instruction injection (60.4% vs. 66.0%), and deployed injection detectors score them as benign, so behind a filter they are 1.7-4.4x more effective. We measure this at the generation stage across six models and ten consumer-service domains, for three attack families, and show that it transfers to production browser agents, outperforming instruction injection, and to a retrieval pipeline (1.0-57.0% end-to-end success, depending on the retriever). We then show that a corroboration requirement added to the agent's instructions removes roughly 95% of the exposure against a non-adaptive attacker without retraining. With the requirement in place, the agent still reads the planted hazard and no longer acts on it.

### Collaborative Search Meets Large Language Models: An Empirical Study
- arXiv 2611.04619v1 · v1 2026-11-03 10:08 UTC · cs.IR
- Authors: Peiyuan Gong, Jiamian Li, Erhan Zhang, Fengming Liang et al.
- Topics: Citation & source selection, Clicks & measurement · score 7 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04619
- arXiv comment: Accepted by SIGIR-AP 2026
- Full text: data/fulltext/2611.04619.txt

> Collaborative search enables users to address complex information needs jointly. Advances in large language models (LLMs) enable autonomous agents to support collaborative information seeking within shared communication spaces. However, little is known about how these agents shape search experiences, behaviors, and outcomes compared with conventional search tools. We conduct a user study with 80 students working in 40 pairs. Each pair completes four collaborative search tasks under four scenarios: QAAgent, which answers queries using an LLM's parametric knowledge; CoSearchAgent, which uses multi-user conversational context to reformulate queries, retrieve web information, and generate source-grounded answers, while asking clarifying questions when needed; an in-chat search plugin that returns result lists; and manual Google Search. After each task, participants complete several questionnaires assessing their search experience and independently write a report; after all tasks, they participate in individual interviews. Results show that LLM-based agents reduce perceived workload, support collaboration, and reshape communication and evidence-use practices. They also encourage more independent paraphrasing, albeit at the cost of report richness. To the best of our knowledge, this is the first systematic empirical comparison of LLM-based agents and conventional tools for collaborative search across search experience, user behavior, and collaborative outcomes.

### AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data
- arXiv 2611.03815v1 · v1 2026-11-02 19:00 UTC · cs.RO, cs.AI, cs.LG
- Authors: Yueh-Hua Wu, Kei Ota, Hanlong Li, Hayata Yuasa et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.03815
- arXiv comment: 18 pages. Project page: https://a-0.airoa.io
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single instruction, A-0 sorts more than a dozen small parts into their numbered cells and changes the mop pads and brush of a robot vacuum; among other tasks, it unzips a pencil case and folds a towel. It performs these tasks using only a camera on each wrist, with no head or scene camera, at a site where none of its training data was recorded. Across the ten tasks of our evaluation, it averages a success rate of 78%, against 27% for the strongest of four other vision-language-action models post-trained on the same task demonstrations. We collect no teleoperation data and use no reinforcement learning or on-robot corrections, and the robot appears only at test time. The system learns which regions of each wrist view matter for the task, predicts the stage the task has reached, and decodes actions as a continuous stream. A-0 is embodiment-agnostic: it runs on robots that mount the YUBI gripper, such as a bimanual Franka, TX-G2, OpenArm and UR. We are releasing the dataset, to our knowledge the largest open dataset of handheld-gripper demonstrations with task and subtask instructions, together with the pre-trained weights and the post-training recipe. Videos of A-0 on every task are on the project page, https://a-0.airoa.io. Anyone can build the gripper, record a task of their own and post-train the model on it in under four hours on a single node of eight H200 GPUs.

### Whose startup does the AI back? An algorithm audit of reputation and demographic signals in LLM-assisted crowdfunding
- arXiv 2611.03993v1 · v1 2026-11-02 21:31 UTC · cs.AI, cs.CL, cs.CY, cs.ET
- Authors: Mirza Samad Ahmed Baig, Syeda Anshrah Gillani
- Topics: Clicks & measurement · score 6 · found via cs.AI, cs.CL, cs.CY
- Link: https://arxiv.org/abs/2611.03993
- arXiv comment: 36 pages, 4 figures, 3 tables; includes online appendix. Accepted manuscript of the article published in Journal of Business Venturing Insights 26 (2026) e00682. Data, design files and code: https://github.com/Mirza-Samad-Ahmed-Baig/Whose-startup-does-the-AI-back-
- Journal ref: Journal of Business Venturing Insights 26 (2026) e00682
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large language model (LLM) assistants increasingly advise backers on which crowdfunding campaigns to support. LLMs have known race and gender problems, and it is unsettled whether they reproduce, erase, or reverse the discrimination documented in entrepreneurial finance. We ask when, and through which decision process, LLM assistants use founders' gender and ethnicity. In a pre-specified choice-based conjoint experiment, seven LLMs chose among five synthetic campaigns with independently randomized quality signals and founder names, under three backer personas and a persona-free control (40,248 responses). By default, founder names barely matter: under budget-conscious and delivery-focused personas, gender and Black-name effects are statistically equivalent to zero. When the backer wants to support underrepresented creators, the models favor Black-signaled (+8.1 percentage points; positive in all seven models) and female-signaled (+5.1) founders. They do so most strongly among near-tied campaigns and for the founder who alone carries the signal, and they almost never name gender or ethnicity in their reasons. The results fit an agency account of algorithmic discrimination: an aligned assistant takes its demographic preferences from its user rather than from its training data.

### The Devil is in the Context: Nine Dimensions of Prompt Injection Attacks
- arXiv 2611.04672v1 · v1 2026-11-03 10:56 UTC · cs.CR
- Authors: Jiamin Chang, Kristina Nikolić, Rishi Sharma, Giovanni Cherubin et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.04672
- arXiv comment: 19 pages, 9 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Prompt injection is usually discussed and evaluated as a single, homogeneous type of attack. However, vulnerabilities reported in real-world systems show that prompt injections vary widely. Moreover, the same instruction can be a prompt injection in one context and a legitimate request in another, depending on the user's intent and the system's policies. Ignoring this variation leaves gaps in how defenses are evaluated, and can give a false sense of security against real-world attacks. We identify nine dimensions along which prompt injection attacks differ. Together, they form a taxonomy that describes the injected instruction itself, its relation to the user's task, and how it manifests in the target system. Each dimension affects which defenses can detect or prevent an attack. We first use the taxonomy to characterize six real-world prompt injection vulnerabilities, showing how much these attacks differ. We then apply it to nine prompt injection benchmarks and find that most cover only a small region of this space. Combining benchmarks helps, but 13% of pairwise category combinations remain untested, mostly among the less commonly represented categories. Finally, we show that the taxonomy supports automated annotation of benchmarks and targeted generation of new test cases to fill these gaps. The taxonomy is also useful beyond benchmarks. Defense authors can use it to state which types of prompt injection they evaluated against, and system operators can use it to identify which attacks apply to their system and choose defenses to match.

### Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning
- arXiv 2611.04673v1 · v1 2026-11-03 10:57 UTC · cs.CR
- Authors: Yao Wang, Zehua Ma, Weiming Zhang, Han Fang
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.04673
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Indirect Prompt Injection (IPI) poses a critical threat to LLM agents. Existing defenses largely focus on whether an injection induces a new tool invocation or unintended action. In this paper, we study a different attack surface, parameter poisoning, where the attacker preserves the intended action but manipulates one or more tool arguments, such as a recipient or other task-critical value. Such attacks are difficult to detect because no new action is introduced, while parameter changes themselves are often legitimate parts of the user's request. Our key insight is that the legitimacy of a parameter change should be determined by the trust of the information flow that produces it under the user query. The query induces a task-specific trust hierarchy over available information fields: some are trusted to determine particular parameters, while others should have little or no influence. Based on this insight, we propose AuthorityFlow, a three-stage parameter-level defense. First, it interprets the user query to construct a task-specific trust hierarchy over the information fields available to the agent. Second, for each tool argument, it traces the information flow that produces its current value and attributes the value to its supporting field. Finally, it accepts the value only when that field is trusted to determine the parameter under the current task, allowing high-trust changes while flagging low-trust influence as potential parameter poisoning. We further introduce FactAuthBench for evaluating parameter poisoning in LLM agents. Without defense, the attack success rate reaches 93.06%. AuthorityFlow reduces it to 9.03%, while retaining 82.64% benign task utility compared with 90.28% without defense. Our results show that effective IPI defense requires reasoning not only about what action an agent takes, but also about which information is trusted to determine its parameters.

### When Category Means Move: A Paired-Support Audit of Recommendation Logs with Random Insertions
- arXiv 2611.05006v1 · v1 2026-11-03 14:53 UTC · cs.IR
- Authors: Yu Zhang, Zhihan Wang, Yuhang Lu, Shuai Li
- Topics: Clicks & measurement · score 6 · found via cs.IR
- Link: https://arxiv.org/abs/2611.05006
- arXiv comment: 10 pages, 6 figures. Accepted at WSDM 2027 (Main Track)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Content-category dashboards summarize production recommendation logs, although the serving policy selects the users, items, and contexts behind each mean. Using KuaiRand random-insertion impressions, we audit these summaries on the same 12,472 users and 5,486 videos in both logs. Standard means have absolute/centered mean absolute error (MAE) 0.1935/0.0491 and rank correlation 0.7833. User demeaning plus a random grand-mean anchor reduces absolute MAE by 80.0%, but centered MAE by only 21.0%, without reliably improving rank. A complete-support ledger allocates weighted squared error mainly to within-video residual (72.41%) and video mix (23.90%), with 3.65% from random support. In a frozen later test, early category calibration reaches MAE 0.0251 versus 0.0531 for scalar calibration; their direct difference is -0.0280 [-0.0296, -0.0172]. Decision evidence is cutoff-specific: the nominal top-10 regret change for row-weighted demeaning versus naive is -0.0062 [-0.0084, -0.0003], while top-5 and top-20 intervals include zero. The six-contrast family-wise top-10 interval [-0.0136, 0.0013] includes zero. An outcome-free disjoint randomized-reference split also leaves all six nominal contrasts covering zero. A known-truth stress test shows incomplete improvement under a mean-additive positive control and failure under item mix and weak overlap. All decompositions are descriptive and each result is conditional on its overlap cohort. KuaiRand intervals quantify user-cluster variation conditional on the realized catalog and calendar; we claim neither intrinsic category effects nor a universally valid correction.

### DualEvolve: Dual-Level Self-Evolution of Mechanism and Orchestration for Recommendation
- arXiv 2611.04439v1 · v1 2026-11-03 07:32 UTC · cs.IR
- Authors: Tianqi Gao, Chenxu Wang, Wenxuan Yang, Yueqi Mou et al.
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04439
- arXiv comment: 12 pages, 4 figures, 15 tables. Tianqi Gao and Chenxu Wang contributed equally. Code: https://github.com/ToAdventure/dualevolve
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recommender systems are widely used in e-commerce and content platforms, where improvement requires repeated model design, training optimization, and experimental validation. Large language model (LLM) agents increasingly automate this development cycle. Sustained autonomous improvement requires agents to improve both recommendation models and their development workflows. However, task-performance-driven approaches select updates mainly by candidates' final scores, without a separate optimization signal for experimentation quality. We therefore present DualEvolve, a dual-level framework that co-evolves recommendation mechanisms and agent orchestration toward recursive self-improvement. Inner evolution revises model and training code using task feedback to improve recommendation performance. Outer evolution scores the inner-loop experimental process, updates harness and skill rules using these scores and execution traces, and adjusts orchestration choices based on next-round scores to improve the quality of subsequent experiments. Experiments on MovieLens-1M and three Amazon Reviews 2023 subsets cover four recommendation methods and 16 settings. DualEvolve achieves higher test means than Base, OpenEvolve, and DeepEvolve in all 64 setting-metric comparisons, with macro-averaged relative gains over DeepEvolve of 7.6% (HR@5) and 9.0% (NDCG@5).

### OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer
- arXiv 2611.04720v1 · v1 2026-11-03 11:42 UTC · cs.IR
- Authors: Feng Cheng, Yu-Hsuan Huang, Fengyi Wang, Chaofan Zhou et al.
- Topics: Ads · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04720
- arXiv comment: 26 pages, 6 figures, 11 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Industrial recommender systems allocate substantial computation to pointwise candidate scoring, yet separate reranking and mix-ranking stages still assemble the final exposure slate using hand-crafted rules and specialized low-capacity models. Mix-ranking combines product cards, short videos, livestreams, and advertising cards supplied by distinct upstream business channels. Although these rules and models encode valuable domain knowledge, they are inherently limited in leveraging additional data and computation. They constrain the combinatorial space of candidate slates and determine objective trade-offs through manual tuning. To enable scalable and effective slate generation, we reformulate reranking and mix-ranking as a unified learning problem whose performance can improve with computation. Specifically, we instantiate this formulation across the reranking and mix-ranking stages and propose OneTrans-GSR, a single decoder-only policy that extends our deployed OneTrans backbone to generate the exposure slate end-to-end. During training, a reward model evaluates complete slates and guides reinforcement learning toward slate-level and long-term objectives. During decoding, business constraints are explicitly enforced. Offline evaluation shows that slate quality consistently improves as reward-model and policy compute increase. Deployed in a large-scale industrial recommendation system, OneTrans-GSR mixes heterogeneous content types within a unified slate. In online A/B tests, it improves GMV/u by 2.63%, advertiser value by 2.06%, and repurchase rate by 2.03%, while reducing end-to-end latency across the reranking and mix-ranking stages by 13%. These results mark a paradigm shift in slate generation: moving beyond human-engineered heuristics toward a general learned policy creates a scalable path for further algorithmic optimization and compute-driven improvement.

### Auditing Multi-Proxy Explanations of Web User Preferences: Identification Boundaries and Abstention
- arXiv 2611.04997v1 · v1 2026-11-03 14:48 UTC · cs.LG, cs.IR
- Authors: Yu Zhang, Zhihan Wang, Yuhang Lu, Shuai Li
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04997
- arXiv comment: 11 pages, 1 figure. Accepted at WSDM 2027 (Main Track)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web systems infer user preferences from behavior, ratings, text, and LLM-generated profiles, yet explaining a proxy may reveal its measurement process rather than the preference of interest. We develop an audit framework distinguishing point identification, partial identification, and abstention relative to an explicit reference distribution. Under feature-dependent, arbitrarily signed proxy bias, a strict majority of uncontaminated proxy attributions lets the coordinatewise median recover latent-attribution support and direction and, with externally justified positive scales, magnitude. We prove this threshold sharp using response-valid indistinguishable worlds, characterize sharp minimax error and exact compatible-target sets under approximate cleanliness and scale uncertainty, and propagate clean-proxy attribution error. A frozen known-truth benchmark spans two response families, four proxy counts, all contamination counts, three bias strengths, and eleven methods, with a focal comparison confirmed on twenty unseen seeds. Under correct budgets, a direct attribution-tensor audit achieved 100% coverage, 95.40%-97.05% active-driver sign decisions, and no false signs. In a temporally separated Amazon study, median aggregation reduced comparator-relative conditional sign error for all four targets; six of eight prespecified target-metric contrasts had Bonferroni intervals excluding zero. A controlled real-covariate perturbation favored the median on the prespecified focal metric for all four targets. Compatible sets showed that the current proxy configuration rarely licensed strict-sign conclusions. Weak comparator calibration limits the Amazon evidence to fitted-surface alignment rather than latent-preference recovery.

### JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks
- arXiv 2611.05263v1 · v1 2026-11-03 17:49 UTC · cs.AI
- Authors: Shanka Subhra Mondal, Jiayun Wang
- Topics: Agents · score 4 · found via search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.05263
- Full text: data/fulltext/2611.05263.txt

> Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through intermediate states, track progress over extended interaction histories, and execute visually grounded actions. Although prior work has explored modular multi-agent systems with a separate planner, the planner is typically not updated jointly with the actor. We investigate whether explicitly separating and jointly training planning and execution provides a stronger inductive bias for long-horizon web navigation. We introduce JHiMA-WebRL, a joint hierarchical multi-agent reinforcement learning framework for web agents that couples a task decomposer with an actor. To train the decomposer, we use a strong teacher model to construct structured subtask supervision from multimodal GUI trajectories, and use these annotations to fine-tune both the decomposer and the subtask-conditioned actor. We then extend Group Relative Policy Optimization (GRPO) to jointly optimize the decomposer and actor in the interactive WebArena environment through hierarchical rollout grouping and role-specific advantages. On WebArena-Lite-v2, JHiMA-WebRL-14B, consisting of a 7B actor and a 7B decomposer, achieves an average success rate of 37.2%, compared with 24% for a ScaleCUA-32B agent that we fine-tune with RL on the same training tasks and evaluate under the same protocol. Ablations show that jointly updating the decomposer during RL outperforms updating the actor alone. These results suggest that jointly learned role factorization with smaller models can be a competitive alternative to scaling monolithic agents for long-horizon web tasks.

### HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation
- arXiv 2611.05319v1 · v1 2026-11-03 18:24 UTC · cs.IR, cs.AI
- Authors: Zhen Tao, Xun Zhou, Xuhui Chen, Ziyue Qiao et al.
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.05319
- arXiv comment: Accepted by NeurIPS 2026
- Full text: data/fulltext/2611.05319.txt

> In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone. Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup. We recast LLM-based recommendation as an agentic-communication process in four stages: BUILD a self-description, TRANSMIT it along the collaborative graph, UNDERSTAND the other side, and SYNC it from the next interaction. This formulation reveals three unresolved communication challenges: the item side never produces a comparable self-description (one-sided BUILD); profile-level signals enter only the bandwidth-limited reranker prompt rather than retrieval, where they would not compete for context tokens (prompt-trapped UNDERSTAND); and the user's description is frozen after warmup with no principled update rule (absent SYNC). We instantiate the missing stages as HARP (Homophily-aware Agentic Recommendation via dual Profiles), a training-free, three-operator addition to a frozen LLM backbone: a rule-extracted symmetric item profile (zero extra LLM calls), a channel-decomposable profile-level homophily H(phi_u, phi_i) consumed at retrieval time rather than inside the reranker prompt, and a single-pass reflective update realising in-context profile evolution without any gradient step. On four public benchmarks (Yelp, Books, MovieTV, Goodreads), HARP lifts Hit@1 over the strongest published baseline by 6.9%-24.0%, with family-wise Holm-corrected p < 1e-9 on every dataset. Ablations and a per-case attribution study show that the operators contribute complementary gains, with the retrieval-side gate as the main source; we also report the trade-off introduced by the reflective pass. We formulate agentic communication and provide a training-free instantiation. Code is available at https://github.com/Jove-Zhen/HARP.

### Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation
- arXiv 2611.03747v1 · v1 2026-11-02 05:49 UTC · cs.AI, cs.IR
- Authors: Huan Phong Thai, Thu Anh Ngoc Le, Nhu Huynh Thi Le, Nhan Huu Tran et al.
- Topics: RAG (generic) · score 2 · found via HF daily papers, cs.IR
- Link: https://arxiv.org/abs/2611.03747
- Full text: data/fulltext/2611.03747.txt

> Natural Language Processing (NLP) has been widely applied in financial domains, enabling automated analysis and retrieval of stock market information. However, traditional NLP-based systems often struggle with maintaining contextual accuracy and generating relevant responses in dynamic financial environments. To address these challenges, Retrieval-Augmented Generation (RAG) models have emerged as a powerful solution, combining retrieval-based methods with generative capabilities to enhance response quality. In this study, we present a Retrieval-Augmented Generation (RAG) system designed to generate responses related to stock market information. The system integrates retrieval-based and generative approaches to enhance the accuracy and relevance of financial text generation. To evaluate its effectiveness, we employ the ROUGE metric, specifically ROUGE-1, ROUGE-2, and ROUGE-L, to measure lexical and structural similarity between generated and reference texts. Experimental results on a dataset of 100 stock market-related queries demonstrate high ROUGE scores, indicating strong alignment with reference documents. Additionally, we assess latency to evaluate the system responsiveness, achieving an average response time of 1.16 seconds. These findings confirm that our RAG model is capable of providing accurate and timely stock market insights, making it a promising approach for financial information retrieval.

### Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo
- arXiv 2611.03927v1 · v1 2026-11-02 20:30 UTC · cs.IR, cs.DB
- Authors: Silvio Martinico, Franco Maria Nardini, Cosimo Rulli, Rossano Venturini
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.03927
- arXiv comment: 39 pages, 11 figures, 17 tables. Submitted to Information Systems. Code and data: https://github.com/TusKANNy/papers_reproducibility/tree/main/information-systems-vectorium-kannolo
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Approximate Nearest Neighbors (ANN) search over neural embeddings powers modern retrieval systems such as Retrieval-Augmented Generation. Embeddings come in three representations (dense, sparse and multi-vector), and efficient search combines an index structure, a similarity function and a quantization scheme. Existing libraries fix one combination, hard-code each one separately, or factor only one side of the problem, and none covers all three representations. We present Vectorium and kANNolo, two open-source Rust libraries that split this design space into a data-management layer and an indexing layer. Vectorium abstracts the vector, the distance function, the quantizer and the dataset independently, and provides 11 encoders, from 32-bit floats to sub-bit codes. On top of it, kANNolo implements Hierarchical Navigable Small-World (HNSW) graph and Inverted Vector File (IVF) indexes that are generic over representation, encoder and metric, and a two-stage index that composes any first-stage index with any rescoring dataset. Since every combination is specialized at compile time, this modularity adds no run-time overhead, and the resulting indexes reach state-of-the-art performance: our Product Quantization matches Faiss in accuracy at competitive speed, our RaBitQ and HNSW match or outperform their reference implementations, and our IVF outperforms Faiss. Against six dense and five sparse systems on seven public collections, our indexes give the best memory-throughput trade-off on dense data in 9 of 12 collection-accuracy pairs and perform well on out-of-distribution queries. On sparse data, the systems built on Vectorium lead on all three collections, with Seismic and SeismicWave the fastest and kANNolo's indexes the most compact.

### QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution
- arXiv 2611.04625v1 · v1 2026-11-03 10:14 UTC · cs.IR, cs.AI
- Authors: Manzong Huang, Chenyang Bu, Yi He, Jiapu Wang et al.
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.04625
- Full text: data/fulltext/2611.04625.txt

> Multi-hop retrieval-augmented generation (RAG) supports Web information seeking and fact verification by recovering complementary evidence across related pages within a limited retrieval budget. Scoring evidence independently against the original question can miss supporting units whose relevance emerges through intermediate facts. Iterative retrieval incorporates these facts into subsequent queries, while graph retrieval explicitly models relations among evidence units. Yet fixed-query graph retrievers update entity representations without adapting the query condition to accumulated relational context. We view multi-hop evidence recovery as the coupled evolution of evidence representations and query conditions, with accumulated context informing both what the retriever represents and how it searches for complementary evidence. QueryFlow realizes this perspective by recurrently integrating query-conditioned summaries of graph context into a shared query state, which controls boundary inputs and relation features for subsequent propagation. Across four representative multi-hop question answering (QA) datasets, QueryFlow achieves macro Recall@10 (R@10), Full Recall@10 (FR@10), and LLM-Acc gains of 4.98, 8.40, and 8.0 percentage points over representative baselines, respectively.

## Other new cs.IR papers, title only (11)
- DualClusterNet: Personalized Pattern-Space Composition for Next-POI Recommendation — https://arxiv.org/abs/2611.03726
- EvoMemState: Evolving Memory State for Personal Agents — https://arxiv.org/abs/2611.03743
- Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication — https://arxiv.org/abs/2611.03826
- IDs That Mean Something: A Hands-On Tutorial on Semantic IDs for Recommender Systems — https://arxiv.org/abs/2611.04140
- OSGR: Observation-Support Graph Reasoning for Earth Observation Question Answering — https://arxiv.org/abs/2611.04301
- Do Retrieval Ranking Models Capture Event Order? A Study of Timeline-Constrained Retrieval — https://arxiv.org/abs/2611.04343
- SourceFlow: Collaborative Source Coupling for Flow-Based Recommendation — https://arxiv.org/abs/2611.04455
- ZeroGR: Filtering-First Constrained Decoding for Generative Recommendation — https://arxiv.org/abs/2611.04715
- Scaling Laws For Data-Constrained Dense Retrieval — https://arxiv.org/abs/2611.04979
- Dataset Recommendation for Heterogeneous and Dynamic Scholarly Graphs via Multimodal Representation Learning — https://arxiv.org/abs/2611.05071
- Factorized MLLM Embeddings for Composed Image Retrieval — https://arxiv.org/abs/2611.05193

## Already listed on an earlier day, still inside the look-back window (123)
- Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO — https://arxiv.org/abs/2611.01126 (score 15)
- Building Weighted PubMed Citation Graphs at Scale: A Pipeline and an Audit of Edge-Similarity Features — https://arxiv.org/abs/2611.01044 (score 14)
- From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents — https://arxiv.org/abs/2611.01527 (score 14)
- FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting — https://arxiv.org/abs/2611.01621 (score 14)
- Search When Needed, Proceed When Reliable: Metacognitive Reliability Supervision for Efficient Agentic Search — https://arxiv.org/abs/2610.41738 (score 13)
- When 200 OK Is Not an Answer: Silent Fetch Failures in Agentic Web Content Acquisition — https://arxiv.org/abs/2611.00884 (score 13)
- DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers — https://arxiv.org/abs/2610.37826 (score 12)
- AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising — https://arxiv.org/abs/2611.00822 (score 12)
- Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce Relevance — https://arxiv.org/abs/2611.02758 (score 12)
- AI evaluators favor job applications written by certain AI models, independent of candidate quality — https://arxiv.org/abs/2610.41866 (score 10)
- Designing Informative Actions: Action Construction for Long-Horizon Research Agents — https://arxiv.org/abs/2611.00773 (score 10)
- Measuring User Success in Randomized Search Experiments: Interpreting Good Abandonment in Generative AI Search — https://arxiv.org/abs/2611.01582 (score 10)
- Same Trajectory, Different Knowledge: Information-State-Aware On-Policy Distillation for Search Agents — https://arxiv.org/abs/2611.01987 (score 10)
- DR Pixel: Page-Native Deep Research with Vision-Language Models — https://arxiv.org/abs/2611.03097 (score 10)
- Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction — https://arxiv.org/abs/2611.03183 (score 10)
- Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents — https://arxiv.org/abs/2611.03384 (score 10)
- MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study — https://arxiv.org/abs/2611.03555 (score 10)
- BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed? — https://arxiv.org/abs/2610.41435 (score 9)
- Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions — https://arxiv.org/abs/2611.03052 (score 9)
- Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay — https://arxiv.org/abs/2610.27954 (score 8)
- Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses — https://arxiv.org/abs/2610.40747 (score 8)
- Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents — https://arxiv.org/abs/2610.39251 (score 8)
- Cross-Interface Authorization for AI Computer-Use Agents — https://arxiv.org/abs/2610.41397 (score 8)
- Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents — https://arxiv.org/abs/2610.41432 (score 8)
- Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products — https://arxiv.org/abs/2610.42032 (score 8)
- MemU-Bench: Benchmarking GUI Agents on Long-Horizon User Interactions — https://arxiv.org/abs/2611.00191 (score 8)
- Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries — https://arxiv.org/abs/2611.00420 (score 8)
- Multi-Estimate Elicitation Does Not Uniformly Debias Language Model Judgments — https://arxiv.org/abs/2611.00597 (score 8)
- Sparse Autoencoder Attribution Graphs Are Decided at the Margin — https://arxiv.org/abs/2611.00606 (score 8)
- PhoneValue-Bench: A Multimodal Benchmark and Datasets for Consumer Smartphone Recommerce Valuation — https://arxiv.org/abs/2611.00791 (score 8)
- Similarity-Weighted Leiden-CPM Clustering of a 7.4-Million-Node Biomedical Citation Graph: Weight Alignment, Scale, and Sparsity — https://arxiv.org/abs/2611.01049 (score 8)
- Acceptance and Responsibility Attribution Toward Autonomous Ambulances Across Driving Conditions: A Preliminary Survey of Fire Service Personnel — https://arxiv.org/abs/2611.01132 (score 8)
- Are Fake Citations a Form of Reward Hacking? A Pre-Registered Study of Post-Training and Citation Cues — https://arxiv.org/abs/2611.01313 (score 8)
- NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale — https://arxiv.org/abs/2611.02102 (score 8)
- Don't Guess, Ask Wisely: Benchmarking and Training Proactive Elicitation in Open-Domain LLM Conversations — https://arxiv.org/abs/2611.01878 (score 8)
- Interface Quilt: Modifying Applications with Computer Use Agents and Generative UI — https://arxiv.org/abs/2611.01891 (score 8)
- One String to Rule Them All: Measuring Consent Under the IAB Global Privacy Platform — https://arxiv.org/abs/2611.02014 (score 8)
- RecGroupMemory: Feedback-Aware Cohort Memory for E-Commerce Recommendation — https://arxiv.org/abs/2611.02453 (score 8)
- ICJ-Graph: A Citation Graph and a Layered Document Corpus of the International Court of Justice — https://arxiv.org/abs/2611.02630 (score 8)
- E-GenRM: Generative Reward Modeling for Open-Ended E-Commerce Shopping Agents — https://arxiv.org/abs/2611.03008 (score 8)
- From Local Skills to Long-Horizon Web Tasks: Progressive Skill Exploration for LLM Web Agents — https://arxiv.org/abs/2611.03116 (score 8)
- CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements — https://arxiv.org/abs/2611.03126 (score 8)
- ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents — https://arxiv.org/abs/2611.03238 (score 8)
- IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning — https://arxiv.org/abs/2611.03431 (score 8)
- WebHarbor: Docking Real Websites for Evolving GUI Agent Environments — https://arxiv.org/abs/2611.03634 (score 8)
- PACT: Defending Recommendation against Promotional News Rewriting via Attack-Diverse Score Consistency — https://arxiv.org/abs/2611.00972 (score 7)
- Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction — https://arxiv.org/abs/2611.01087 (score 7)
- Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning — https://arxiv.org/abs/2611.01411 (score 7)
- TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents — https://arxiv.org/abs/2610.41216 (score 6)
- Real Computation or Merely Naming? A Pre-Registered Mechanism Audit of 25 Cognitive-Architecture Modules in an LLM-Based Agent System — https://arxiv.org/abs/2610.41604 (score 6)
- Early Stopping in Large Reasoning Models: A Survey and Empirical Audit of Efficiency and Reliability — https://arxiv.org/abs/2611.00166 (score 6)
- AuroraWorld: Structured 4D World Modeling for Exo-to-Ego Video Generation in Robot Manipulation — https://arxiv.org/abs/2611.00177 (score 6)
- When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity — https://arxiv.org/abs/2610.41970 (score 6)
- SecPO: Principled Adversarial Training for Prompt Injection Security — https://arxiv.org/abs/2610.41998 (score 6)
- RE-SciVQA: Improving Scientific VQA With Context-Relevant Retrieval and Lightweight MLLM Adaptation — https://arxiv.org/abs/2611.00242 (score 6)
- Queering the Audits: Community-Based Auditing of AI Harms to Queer Communities — https://arxiv.org/abs/2611.00345 (score 6)
- Price is Only the Symptom: Understanding and Analyzing Economic-State Manipulation Vulnerabilities in DeFi — https://arxiv.org/abs/2611.00587 (score 6)
- Conversational Interaction for LLM-Based Clinical Text-to-SQL: A User Study with Healthcare Professionals — https://arxiv.org/abs/2611.00605 (score 6)
- Reading Between the Chapters: A Graph-Free RAG Rebuilt With AI and Human Feedback — https://arxiv.org/abs/2611.00752 (score 6)
- Numerical Embeddings for CTR Prediction: A Taxonomy, Unified Benchmark, and Open-Source FuxiCTR Extension — https://arxiv.org/abs/2611.01090 (score 6)
- Pop Goes the Verifier: Phoneme-Targeted Data Poisoning of Voice Liveness Detection — https://arxiv.org/abs/2611.01095 (score 6)
- Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation — https://arxiv.org/abs/2611.01112 (score 6)
- MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents — https://arxiv.org/abs/2611.01700 (score 6)
- Reddit Community Signals as a Supplementary Domain-Reputation Feature in Spam Classification: A Conservative Controlled Evaluation — https://arxiv.org/abs/2611.01813 (score 6)
- EAGR: Evidence-Guided Adaptive Graph Retrieval — https://arxiv.org/abs/2611.01910 (score 6)
- Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security — https://arxiv.org/abs/2611.01976 (score 6)
- Testing concept-level audits of melanoma classifiers with diffusion counterfactuals and matched positive controls — https://arxiv.org/abs/2611.02119 (score 6)
- Conditional Calibration Contracts under Coupled Load: A Branch-Aware Audit of Switched Inference — https://arxiv.org/abs/2611.02121 (score 6)
- Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting — https://arxiv.org/abs/2611.02310 (score 6)
- From Language to Country to Valence: A Multilingual Audit of Stereotype Bias Across LLMs — https://arxiv.org/abs/2611.02585 (score 6)
- SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search — https://arxiv.org/abs/2611.02643 (score 6)
- The Customer Never Sees the Goal: Measuring and Detecting Vulnerability-Targeted Manipulation in LLM Assistants — https://arxiv.org/abs/2611.02689 (score 6)
- PanoTac: A Dense Three-Axis Tactile Sensor for Robust Touch-Centric Manipulation — https://arxiv.org/abs/2611.03520 (score 6)
- Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations — https://arxiv.org/abs/2611.03647 (score 6)
- Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation — https://arxiv.org/abs/2611.03648 (score 6)
- ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science — https://arxiv.org/abs/2610.41396 (score 5)
- Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents — https://arxiv.org/abs/2610.41905 (score 5)
- PatchScout: Thematic Web Data Collection via Information Foraging — https://arxiv.org/abs/2611.00169 (score 4)
- DuSE-Bench: Benchmarking Joint Reasoning over Evolving Dialogue and Documents — https://arxiv.org/abs/2611.00755 (score 4)
- Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights — https://arxiv.org/abs/2611.01280 (score 4)
- Dynamic Click Destinations: Personalizing Post Ad-Click Landing Experiences — https://arxiv.org/abs/2611.01287 (score 4)
- EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees — https://arxiv.org/abs/2611.01977 (score 4)
- Multi-criteria Rating and Review based Recommendation Model — https://arxiv.org/abs/2611.02019 (score 4)
- WeSearch: A Unified Model-Centric Retrieval Framework for WeChat Search — https://arxiv.org/abs/2611.00530 (score 3)
- HiPaper: A Human-AI Collaborative System for Academic Literature Triage and Scholarly Sensemaking — https://arxiv.org/abs/2611.00762 (score 3)
- CST: Lightweight Risk Triage with Source-Grounded Evidence for Web Discussions — https://arxiv.org/abs/2611.01710 (score 3)
- Adversarial Robustness of Retrieval-Based Fact-Checking: Detecting and Mitigating Evidence Contamination — https://arxiv.org/abs/2611.02139 (score 3)
- Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning — https://arxiv.org/abs/2610.41390 (score 1)
- ElectroChemLLM: A Multimodal LLM Pipeline for High-Fidelity Electrochemical Informatics — https://arxiv.org/abs/2611.00638 (score 1)
- Bridging Low-Level Image Fusion and High-Level Semantic Understanding — https://arxiv.org/abs/2611.02896 (score 1)
