# Paper candidates — 2026-11-19 (IST)

Generated 2026-11-19 07:50 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 14 new topic matches · 9 other new cs.IR · 86 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (14), highest score first

### Dreaming Up Authors: Factual Prevalence and LLM Hallucinations in Academic Authorship Attribution
- arXiv 2611.23530v1 · v1 2026-11-17 21:37 UTC · cs.CL
- Authors: Sijia Zhong, Tamir Yirga, Yijia Ma, Thai Le et al.
- Topics: Citation & source selection, RAG (generic) · score 10 · found via cs.CL
- Link: https://arxiv.org/abs/2611.23530
- arXiv comment: Published in EMNLP 2026 (Main Conference). 37 pages. Code and data: https://github.com/quinnzhong1/dreaming-up-authors. Anthology: https://aclanthology.org/2026.emnlp-main.2372/
- Journal ref: Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026), pages 53827-53863, Budapest, Hungary
- Full text: data/fulltext/2611.23530.txt

> Large Language Models (LLMs) are widely used for question answering but are prone to hallucinations, yet the underlying causes, particularly the role of factual prevalence in training data, remain underexplored. In this work, we study this through academic authorship attribution, hypothesizing that hallucinations are more likely for less prevalent papers. Using citation count as a proxy for factual prevalence, we curate a dataset of 1.92 million papers across eight scientific disciplines with stratified samples by citation level. Experiments on three state-of-the-art LLMs confirm our hypothesis, revealing a robust inverse relationship between hallucination rate and citation count across all models and disciplines, with hallucination rates exceeding 98% for rarely cited papers and falling below 37% for highly cited ones. Our in-depth analysis further shows that these failures primarily reflect retrieval limitations rather than knowledge absence, and hidden-state probing of open-source models shows that factual prevalence is encoded in pre-generation representations, providing convergent mechanistic evidence for the prevalence-hallucination relationship. The code and data are available at https://github.com/quinnzhong1/dreaming-up-authors.

### X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- arXiv 2611.24283v1 · v1 2026-11-18 11:58 UTC · cs.IR
- Authors: Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov et al.
- Topics: Clicks & measurement, Ads · score 10 · found via cs.IR
- Link: https://arxiv.org/abs/2611.24283
- arXiv comment: Alexander Ploshkin, Nikita Stepanov and Alexey Pismenny contributed equally to this work
- Full text: data/fulltext/2611.24283.txt

> Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.

### Entropy-Regularized Integrated Gradients for Stable Feature Attribution
- arXiv 2611.23600v1 · v1 2026-11-17 22:53 UTC · cs.LG, cs.AI, cs.CV
- Authors: Rukmangadh Sai Myana, Sumit Kumar Jha, Yanzhao Wu
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.23600
- arXiv comment: 36 pages, 19 figures, 27 tables, including the appendix
- Full text: data/fulltext/2611.23600.txt

> Path-based attribution methods like Integrated Gradients (IG) are widely used to interpret neural networks, yet imperceptible input perturbations can drastically alter their attribution maps while leaving model predictions unchanged. We introduce Entropy-Regularized Integrated Gradients (ERIG), a path-based attribution method that intrinsically attenuates gradient irregularities along the integration path using maximum-entropy softmax weighting with temperature parameter $τ$. We quantify the effect of the entropy-regularized weighting on attribution stability by using the Lipschitz properties of the model and its gradients. We decompose the attribution change under an input perturbation into a model-response term, whose bound is $τ$-independent, and a weight-variation term, whose bound decreases at rate $\mathcal{O}(1/(2τ))$. Their ratio $R(τ)$ characterizes the trade-off between gradient information and attribution stability. We further add a new dimension to attribution evaluation by adapting classical noise estimators into two metrics, LINV-C and LINV-P, that quantify attribution noise. Across eleven CNN and Transformer backbones on ImageNet and Oxford-IIIT Pet datasets, our experiments show that, relative to the next-best method, ERIG remains comparable on ranking-based fidelity metrics while improving localization by approximately 24% and attribution stability by approximately 47-fold on average, reaching up to four orders of magnitude improvement over IG, all at negligible additional computational cost.

### IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents
- arXiv 2611.24102 · v1 2026-11-18 00:00 UTC · 
- Authors: Zhizhuo Kou, Sizai Hou, Jian Yang, Ge Sun et al.
- Topics: Agents · score 8 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.24102
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. However, existing sample-level detectors target image classifiers and CLIP-style encoders, leaving step-level backdoor detection for GUI agents unaddressed. On clean steps, the instruction drives the action; when an unreferenced screen region hijacks the step, the instruction loses control over the decision state or that region dictates it instead. We term this signature intent--evidence dominance inversion and propose IDEA (Intent-Dominance Evidence Audit) to detect backdoor activation at inference time for each step without trigger knowledge or attack data. Specifically, Intent Counterfactual Probing (ICP) measures how far redirected instructions move the decision state, and Region Causal Audit (RCA) quantifies how far ablating a candidate region moves it. A gated conformal score compares both displacements against clean steps at the same distance from the clean manifold, providing a finite-sample false-positive guarantee. Extensive experiments on Qwen2.5-VL-3B across five attack families show that IDEA consistently detects backdoor activation under a controlled false-positive rate and outperforms state-of-the-art detection methods, while localizing the trigger region for every alarm and adding only modest inference overhead.

### How Complete Must an Environment Be to Train a Capable GUI Agent?
- arXiv 2611.23946v1 · v1 2026-11-18 06:32 UTC · cs.CV, cs.AI, cs.LG
- Authors: Jingxing Wang, Teng Wang, Xingyu Lou, Zihan Guo et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.23946
- arXiv comment: 15pages, 6 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We describe these choices along three dimensions: reward coverage, the goal-reaching trajectories the verifier rewards; data coverage, the application data the agent is exposed to beyond what the task reads or writes; and feature coverage, the application features beyond what the task uses. Existing works set each dimension on engineering grounds, but they do not measure its effect on training. How complete must an environment be to train a capable agent, and along which dimensions? In MobileGym, we adjust each dimension separately, train Qwen3-VL-4B-Instruct, and evaluate every policy in the original full environment. A verifier that rewards only one reference path lowers success by 10.53 points, and removing unneeded records also lowers success. Pruning unneeded features instead raises success from 51.61% to 56.13%, entirely on tasks whose environments it left unchanged. The gain reverses when each episode is weighted equally and vanishes when only episodes on the pruned tasks are balanced. Without pruning, length weighting there reinforces long detour successes that erode skills on other tasks. Following these findings, we build MobileGym-Lite, which keeps reward and data coverage complete and prunes unneeded features. It outperforms Full in the full environment (55.48% versus 51.61% success) with lower construction cost.

### Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness
- arXiv 2611.23346v1 · v1 2026-11-17 10:36 UTC · cs.CR
- Authors: Deep Shah, Nehal Kathrotia
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.CR
- Link: https://arxiv.org/abs/2611.23346
- Full text: data/fulltext/2611.23346.txt

> Long-horizon LLM agents across codebases, web browsers, and enterprise infrastructure rely on an execution harness to move state between the working context, session history, persistent memory, and external environment. While conventional execution traces log model prompts and tool calls, critical security and reliability failures occur during state transfers: a transfer can admit unchecked content (indirect prompt injections, unverified memory writes), rewrite state lossily (context compaction dropping user constraints, memory consolidation stripping source authority), or restore state incompletely (workspace rollbacks leaving aborted KV state active on the inference server). Because current traces omit what crosses these boundaries, failure attribution and runtime monitors fail on multi-step trajectories. We present a state-transfer audit architecture for the agent harness. At each transfer boundary, we define an audit point specifying the minimal hash-chained record the harness emits, separating low-overhead deterministic checks from model-based semantic checks and binding internal context, memory, and inference-server cache state to external actions. We show that the same transfer records required for causal failure attribution supply the durable state needed by runtime security controls, including least-privilege capabilities, replay-resistant authorization outside the prompt, information flow control, obligation monitors, and transactional recovery across multi-agent and infrastructure pipelines. Finally, we analyze multimodal GUI adaptations and implement and evaluate a reference harness middleware across 240 multi-step fault-injection trajectories, showing that transfer records localize root causes and catch cross-transfer violations missed by lifecycle and tool-only logs at microsecond deterministic overhead.

### Data Poisoning Attacks to Locally Differentially Private Triangle Counting Protocols
- arXiv 2611.23701v1 · v1 2026-11-18 01:47 UTC · cs.CR
- Authors: Tingxuan Han, Wei Tong, Zijian Wang, Sheng Zhong
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.23701
- arXiv comment: Accepted by ICDE 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Local differential privacy (LDP) has become a crucial paradigm for privacy-preserving graph analytics, enabling graph analytics tasks such as subgraph counting without requiring a trusted curator. However, while LDP provides strong privacy guarantees, the integrity and robustness of LDP subgraph counting protocols in the presence of malicious participants remain poorly understood. In particular, since data are randomized locally before collection, it is inherently difficult to distinguish malicious users from honest ones based solely on their submitted reports, and small, protocol-compliant local manipulations can be systematically amplified through reconstruction and calibration into large global estimation bias. In this paper, we use LDP triangle counting as a representative task to characterize the vulnerability of LDP subgraph counting to data poisoning attacks. For both non-interactive and interactive LDP triangle counting protocols, we analyze their attack surfaces and develop a unified gain-driven framework that captures how adversarial users can manipulate calibrated subgraph count estimates, which we instantiate on representative protocols of both types. Extensive experiments on four real-world graph datasets demonstrate that these attacks can significantly distort triangle count estimates across different protocols and adversarial settings. Moreover, we show that existing and straightforward defenses are insufficient to mitigate these attacks, underscoring the need for robustness mechanisms tailored to LDP subgraph counting.

### What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents
- arXiv 2611.24231v1 · v1 2026-11-18 11:08 UTC · cs.AI, cs.CR
- Authors: Haoyang Liu, Yinong Xu, Zhe Lang, Zhenyu Guan et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.24231
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multimodal language models increasingly answer questions over external documents, exposing them to indirect prompt injection: commands planted in untrusted content to hijack the response. Rendering untrusted content as page images lowers attack success on average, leaving open which injected operations survive rendering, at what utility cost, and whether failed image attacks reflect unread commands or commands read but not followed. We pair text and page-image versions of 191 English question-answering sources across six models, measuring marker appending, answer formatting, and answer replacement alongside clean Question-Answering utility. Rendering reduces append and format execution for every model, yet Qwen3-VL-8B still executes image-borne replacement at 77.96\%. Protection also depends on target type, rendering settings, wording, and repetition, and a search over eight fixed attack candidates largely closes the image deficit in appending and formatting for Qwen and Gemini, though not for GPT-5-nano. Utility ratios on original questions range from 93.31\% to 101.61\%, but Qwen falls to 61.99\% when answers combine two evidence spans. Illegibility cannot explain all failed attacks: models often transcribe and identify image-borne commands they do not execute, and trusted user authorization raises execution on unchanged pages. Inside Qwen, patching early attack-region states induces all three operations, more weakly in images. Attention blocking suggests why: a text command acts through its own positions, whereas visual encoding spreads an image command and its target across the instruction page. Rendering thus offers conditional protection, motivating evaluations that report security by model, operation, and attack budget alongside utility.

### AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents
- arXiv 2611.24313v1 · v1 2026-11-18 12:20 UTC · cs.AI, cs.CR, cs.LG
- Authors: Stavros Damianakis, Konstantinos Psounis
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.24313
- arXiv comment: 18 pages, 8 figures, 5 tables. Project page at https://stevendamianakis.github.io/autopi-site/ and code at https://github.com/stevendamianakis/autopi
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to maximize attack success rate (ASR). Yet ASR counts how often a target breaks, not in how many different ways. A red teamer can achieve a high ASR by reusing a few techniques that work, leaving the others untested and absent from the attacks used to harden models. We present AutoPI, an adaptive red teamer designed to find many different ways to break a target, not just to break it often. AutoPI uses PIAtlas, a taxonomy of prompt-injection techniques, both to guide its search and to measure coverage. For each scenario, an attacker LLM writes an injection for every sub-technique in the taxonomy and then reworks the ones that fail using feedback from an LLM judge. The method is black-box and training-free, it plugs into existing benchmarks in place of their fixed attack templates, and it stays up to date as the taxonomy evolves. We evaluate AutoPI on AgentDojo and IPI Arena against open-weight and proprietary target models. Alongside ASR, we report technique coverage, the fraction of taxonomy classes, techniques, and sub-techniques that yield at least one successful injection. On AgentDojo, AutoPI finds a successful injection against Qwen3.6-35B in all six classes of the taxonomy and for more than 90% of its techniques. Against Claude Haiku 5.5, the most robust target we evaluate, it achieves between 20% and 50% higher ASR and between 25% and 400% higher class-level coverage than recent state-of-the-art adaptive red teamers, while requiring no training. We release our code and the generated attacks to support reproducible, coverage-aware evaluation.

### PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents
- arXiv 2611.24362v1 · v1 2026-11-18 12:56 UTC · cs.AI, cs.CR
- Authors: Lipeng He, Yihan Wang, Jiawen Zhang, N. Asokan
- Topics: Manipulation · score 6 · found via HF daily papers, cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.24362
- arXiv comment: 18 pages, 6 figures
- Full text: data/fulltext/2611.24362.txt

> Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement learning (RL) to generate attacks that achieve high attack success rates (ASR). Model developers use the attacks discovered during internal red-teaming to harden agents through adversarial training before deployment, a collaborative offensive-defensive process known in cybersecurity as purple-teaming. However, we show that achieving high ASR during red-teaming does not guarantee robustness gains from subsequent adversarial training. Specifically, we find that two state-of-the-art RL-based red-teaming methods, RL-Hammer and PISmith, suffer from mode collapse, repeatedly discovering similar attack strategies whose additional successes add no additional robustness improvements to adversarial training. To address this gap, we introduce PIPETTE, a unified prompt injection purple-teaming framework that effectively converts red-teaming discoveries into defender robustness improvements. PIPETTE employs a dictionary learning-based reward that encourages broader coverage of attack strategies during red-teaming. It also integrates an on-policy adversarial training pipeline tailored to IPI defense, enabling agents to resist attacks while completing legitimate user tasks. Extensive evaluations across agentic benchmarks (AgentDojo and ASB) demonstrate that PIPETTE produces defenders that achieve near-zero attack success rates on static attacks and can withstand strong adaptive attacks, while maintaining benign task utility close to that of the undefended baseline.

### SCR: Detecting Backdoor-Poisoned Samples through Clean-Reference Residuals
- arXiv 2611.24558v1 · v1 2026-11-18 14:57 UTC · cs.CV, cs.CR
- Authors: Yi Yang, Jinyang Huang, Feng-Qi Cui, Yu-Tong Guo et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.24558
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Deep neural networks are vulnerable to backdoor attacks, in which adversaries manipulate model predictions by injecting poisoned samples into training data. Detecting these samples remains challenging because legitimate semantic variation can obscure poisoning-related signals in learned representations. Consequently, class-level statistics used by existing detectors may flag benign feature deviations while overlooking poisoned samples that blend into the class distribution. In this paper, we propose Semantic Counterfactual Residualization (SCR), which uses a small set of clean reference samples to account for benign variation through sample-specific feature reconstruction. SCR identifies poisoned samples by detecting coherent deviations from these clean baselines, without requiring prior knowledge of the attacks. We evaluate SCR through experiments covering twelve dirty-label and clean-label attacks across CIFAR-10, CIFAR-100, and Tiny ImageNet. With a small clean-reference set, SCR achieves attack-averaged true positive rates above 99.5\% and false positive rates below 2\% on each dataset, outperforming eight representative detection baselines in macro-TPR.

### Gradient-Based Defensive Poisoning Against System Identification Attacks on Cyber-Physical Systems
- arXiv 2611.24662v1 · v1 2026-11-18 15:59 UTC · cs.CR, eess.SY
- Authors: Gonçalo Fernandes, José Cecílio, Victor Mattos, Daniel S. Menasché et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.24662
- arXiv comment: Presented at the 2026 IEEE International Workshop on Technologies for Defense and Security (TechDefense 2026), Torino, Italy, November 4-6, 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AI-driven attacks learn the models of cyber-physical systems (CPS) by passively observing controller and plant signals, then use this knowledge to act covertly. Because covertness depends on the accuracy of the identified model, degrading that accuracy is a viable countermeasure. This work applies Adversarial Machine Learning as a defense, injecting small perturbations into the measurements the attacker observes to degrade an artificial neural network (ANN)-based system identification (SI) attack. The perturbations are derived from input gradients of several independently trained identification models, aggregated into a generalized perturbation, and confined to the transient regimes that carry most of the dynamic information. A sparsity parameter further restricts them to the most influential samples, with negligible cost in effectiveness. On a simulated DC motor networked control system, the proposed perturbations induce larger prediction errors than stochastic poisoning of equal root-mean-square magnitude, and the advantage widens as the magnitude grows. This limits the defense's operating range, which is intended for decoy environments such as CPS honeynets. Additional results indicate that the designed poisoning signals can also degrade N4SID-based system identification, providing evidence of their transferability beyond the ANN-based models originally targeted.

### KnowMe Paper Radar: Lightweight Discovery of Promising Papers in the Age of Autoresearch
- arXiv 2611.23702v1 · v1 2026-11-18 01:47 UTC · cs.AI, cs.IR
- Authors: Zhuo Chen, Jian Wang, Jinjie Gu, Lijun Wu
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.23702
- arXiv comment: Ongoing work. 67 pages with 34 figures and 37 tables. Project website: https://hackerchenzhuo.github.io/knowme-research-ai/en/ GitHub: https://github.com/hackerchenzhuo/knowme-research-ai
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> The growing volume of topically similar papers makes it difficult to identify new work that can offer useful research insights or methodological guidance. We present KnowMe Paper Radar, a lightweight discovery tool that combines multiple sources of evidence into personalized reading priorities. Users specify topics, priorities, exclusions and dates; the system brings together topical relevance, recency, author research histories, collaboration paths and direction-specific institutional context. By exposing each score component and its supporting sources, KnowMe helps readers select promising papers for their current questions and discover relevant work beyond familiar authors. Automatic acquisition, version merging and graph-cache reuse keep this workflow convenient without large language model (LLM) inference during ordinary use. Experiments on 174,640 acquired records show more than threefold faster repeated context preparation, while cached abstracts improve normalized discounted cumulative gain at rank 10 (NDCG@10) from 0.412 to 0.598 on expert-judged retrieval tasks. Complementary analyses examine how the same accumulated records support semantic retrieval, research-history modeling and literature-grounded planning. A browser interface and a structured command-line interface (CLI) make these capabilities available to both researchers and research agents, positioning KnowMe as a practical upstream tool for literature-informed recursive self-improvement (RSI) workflows.

### MARS Technical Report
- arXiv 2611.24006v1 · v1 2026-11-18 07:56 UTC · cs.IR
- Authors: Tong Liu, Chaoqun Hou, Longxiang Xiong, Junhong Lou et al.
- Topics: Clicks & measurement · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.24006
- arXiv comment: 46 pages, 5 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario. This report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage predictions to full pipeline orchestration. A near-line agent built on fine-tuned Qwen3-0.6B generates per-user configurations--a seven-dimensional action covering pipeline mode, retrieval quotas, model selection, fusion weights, and reranker settings--from a constrained action space. Configurations are validated, cached, and consumed asynchronously; the cascade never waits for LLM inference. Schema checks, fallbacks, and a kill switch ensure serving safety. The policy is trained in three stages: Confidence-aware SFT distills schema-valid generation from a teacher model; Format-Anchored Preference Optimization (FAPO) learns action preferences via ActionMask with posterior weighting; Group Relative Policy Optimization (GRPO) refines the policy through Sandbox replay with a frozen reward model, without exposing exploratory actions to live traffic. Two-week A/B tests across five Taobao scenarios with over ten million daily users show positive gains on all key metrics. The largest reach +5.22% V2P and +7.34% GMV, with positive CTR lifts on both click surfaces. About 20% of requests use a lightweight Minimal mode, and deployment shows 12 ms lower mean serving latency versus production.

## Other new cs.IR papers, title only (9)
- Prioritize, Don't Decide: What We Learned Auditing a Deployed Human-in-the-Loop CV Sorter — https://arxiv.org/abs/2611.23359
- LusoClin: A Synthetic Clinical Note Dataset for Medical Information Retrieval in European Portuguese — https://arxiv.org/abs/2611.23454
- From Docket Minutes to Case Trajectories: Building Analysis-Ready Criminal Court Data — https://arxiv.org/abs/2611.23537
- VIBRA: Backward-Compatible Cross-Modal Retrieval with Consensus Barycenters — https://arxiv.org/abs/2611.23606
- CONCORD-Rec: Catalog-Conditioned Modality Utility for Semantic-ID Diffusion Recommendation — https://arxiv.org/abs/2611.23710
- ReflectRec: Cycle-Consistency Preference Verification for LLM-based Recommendation — https://arxiv.org/abs/2611.23969
- Task-Oriented Network Ranging via Joint Graph and Schedule Design — https://arxiv.org/abs/2611.24702
- Variance-Optimal Counterfactual Policy Design for Sample-Efficient Online A/B Testing — https://arxiv.org/abs/2611.24757
- Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling — https://arxiv.org/abs/2611.24849

## Already listed on an earlier day, still inside the look-back window (86)
- Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning — https://arxiv.org/abs/2611.20045 (score 23)
- User First Intelligence: Three Measurements of Search and AI-Answer Analytics (SEO and GEO/AEO), and a Knowledge-Graph Framework for Query Discovery Beyond Search Volume — https://arxiv.org/abs/2611.19655 (score 18)
- GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk — https://arxiv.org/abs/2611.22223 (score 15)
- How Web Research Agents Interpret User Priorities — https://arxiv.org/abs/2611.22989 (score 14)
- Data Attribution Should Steer Pretraining — https://arxiv.org/abs/2611.19698 (score 13)
- The Fragility of Reasoning-Importance Attribution for Pruning Language Models — https://arxiv.org/abs/2611.22234 (score 13)
- Explainable Federated Learning via Global-Local Attribution Alignment — https://arxiv.org/abs/2611.20445 (score 11)
- DetouR: Plugging Association Routes into Search Agents for Multi-hop Question Answering — https://arxiv.org/abs/2611.19967 (score 10)
- EchoSpec: Training Search Agents to Weigh Evidence Above Echoes — https://arxiv.org/abs/2611.20034 (score 10)
- TUSI: A Citation-Grounded Graph-Based Benchmark — https://arxiv.org/abs/2611.21823 (score 9)
- IntentGR: Enhancing Intent for End-to-End Personalized Generative Retrieval in Search — https://arxiv.org/abs/2611.22788 (score 9)
- Can Decision Models Replace LLMs in Real-World Contact Center Classification and Judging Tasks? — https://arxiv.org/abs/2611.22949 (score 9)
- On Representational and Functional Alignment of Training Data Attribution Methods for Language Models — https://arxiv.org/abs/2611.19286 (score 8)
- MathaMAGICal: Validating Trajectory Data Attribution During Capability Acquisition — https://arxiv.org/abs/2611.19692 (score 8)
- IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu — https://arxiv.org/abs/2611.20448 (score 8)
- EVIDENT: Evaluating Evidence Grounding in GUI Agents — https://arxiv.org/abs/2611.20488 (score 8)
- UIAnchor: Anchoring UI Perception and Action Execution for Reliable Service-Composed Mobile Task Automation with GUI Agents — https://arxiv.org/abs/2611.20753 (score 8)
- EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation — https://arxiv.org/abs/2611.20846 (score 8)
- MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory — https://arxiv.org/abs/2611.21019 (score 8)
- Portrait Fitness as a Pretext: Probing Implicit Demographic Bias in VLMs — https://arxiv.org/abs/2611.21403 (score 8)
- Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle — https://arxiv.org/abs/2611.21538 (score 8)
- ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises — https://arxiv.org/abs/2611.21579 (score 8)
- Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering — https://arxiv.org/abs/2611.21586 (score 8)
- Threat Landscape of Vibe Coding and the Road to Secure Autonomy — https://arxiv.org/abs/2611.21822 (score 8)
- Does the Model Use What It Cites? Counterfactual Tests of Grounded Reasoning Chains in Small Video-Language Models — https://arxiv.org/abs/2611.21940 (score 8)
- Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents — https://arxiv.org/abs/2611.22033 (score 8)
- Right Labels, Wrong Reasons: Signed Feature Attribution for Multi-Label Explainability — https://arxiv.org/abs/2611.22515 (score 8)
- PACT: Plan-Action Consistency Training by Preserving Correct Plans and Repairing Actions in GUI Agents — https://arxiv.org/abs/2611.22591 (score 8)
- SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway — https://arxiv.org/abs/2611.22971 (score 8)
- Hidden-State Similarity Predicts Re-Elicitation After Inoculation Prompting — https://arxiv.org/abs/2611.23096 (score 8)
- Attribution Through the Decoder: Prediction-Space Explanations for Structured Outputs — https://arxiv.org/abs/2611.23161 (score 8)
- What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution — https://arxiv.org/abs/2611.23218 (score 8)
- NI-ACT: A Neural Intent Interface for Brain-Embodied Manipulation — https://arxiv.org/abs/2611.19332 (score 6)
- VoiceGuard: An Audio-Native LLM-VLA Pipeline for Wheelchair-Mounted Assistive Manipulation — https://arxiv.org/abs/2611.19984 (score 6)
- Can AI Judge You? An Empirical Audit of Deployment Readiness in LLM-assisted Hiring Systems — https://arxiv.org/abs/2611.20140 (score 6)
- AsymEEF: Bimanual Manipulation with Asymmetric End Effectors — https://arxiv.org/abs/2611.20557 (score 6)
- Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models — https://arxiv.org/abs/2611.20901 (score 6)
- Language-model agents' beliefs can be manipulated via truthful evidence in open channel — https://arxiv.org/abs/2611.21235 (score 6)
- Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models — https://arxiv.org/abs/2611.21517 (score 6)
- ALOHA Lightning: Learning Fast and Precise Manipulation — https://arxiv.org/abs/2611.21919 (score 6)
- TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation — https://arxiv.org/abs/2611.23143 (score 6)
- RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't — https://arxiv.org/abs/2611.22179 (score 6)
- Where Does Hindsight Enter Clinical Agent Benchmarks? An Audit of Simulators and Case Construction — https://arxiv.org/abs/2611.22241 (score 6)
- A Full-Ledger Counterfactual Audit of Adaptive Reasoning — https://arxiv.org/abs/2611.22778 (score 6)
- Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate — https://arxiv.org/abs/2611.22904 (score 6)
- Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web — https://arxiv.org/abs/2611.19900 (score 5)
- From Relevance to Utility: Rubric Alignment in Yuanbao Search — https://arxiv.org/abs/2611.22503 (score 5)
- Reflection Is Not Always Worth It: Budgeted Reflection Allocation for Recommendation Agents — https://arxiv.org/abs/2611.19847 (score 4)
- How did data sharing evolve in the decade since the FAIR Principles? — https://arxiv.org/abs/2611.20319 (score 4)
- Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First — https://arxiv.org/abs/2611.20378 (score 4)
- What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially Private Item Counts — https://arxiv.org/abs/2611.20388 (score 4)
- Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates — https://arxiv.org/abs/2611.20837 (score 4)
- When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents — https://arxiv.org/abs/2611.21577 (score 4)
- Teaching Language Models to Narrow Boolean Patent Searches from Search Feedback — https://arxiv.org/abs/2611.22270 (score 4)
- MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval with Multi-Category Solutions — https://arxiv.org/abs/2611.22509 (score 4)
- Learning Cross-Domain Media Similarity from Amazon Reviews — https://arxiv.org/abs/2611.22756 (score 4)
- GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation — https://arxiv.org/abs/2611.22274 (score 3)
- NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval — https://arxiv.org/abs/2611.22353 (score 1)
