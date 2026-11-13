# Paper candidates — 2026-11-13 (IST)

Generated 2026-11-13 08:41 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 32 new topic matches · 22 other new cs.IR · 65 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (32), highest score first

### Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition
- arXiv 2611.15538v1 · v1 2026-11-11 14:22 UTC · cs.AI, cs.CL
- Authors: Yue Liu, Zhongying Ru, Shimin Di, Jipeng Zhang et al.
- Topics: Citation & source selection, RAG (generic), Query fan-out · score 20 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.15538
- arXiv comment: Accepted by AAAI 2026
- Full text: data/fulltext/2611.15538.txt

> Retrieval-augment generation is a prevalent strategy to mitigate hallucinations of LLMs. The attributable RAG (RAGQ) generates quotes for its answers. The quotes indicate which input contexts support the RAG to derive the answers, enhancing the answer's verifiability and trustworthiness. However, existing RAGQs exhibit significant degradation when dealing with questions that require multi-hop reasoning and multi-modal understanding, suffering from over-citation, implicit entity identification failure, and poor generalization. In this paper, we propose a novel RAGQ framework, namely QDRAG. QDRAG breaks down the input question into atomic subquestions to identify the implicit entities. Then, the reranker prunes context distractors to eliminate the downstream over-citation. To facilitate query decomposition, we propose two zero-shot approaches: QD-C and QD-R, which guide the QD MLLM to decompose the question based on context knowledge and retrieval rewards, respectively. One interesting finding is that finetuning on the QD task shows better generalizability compared to directly finetuning on the downstream RAGQ task. Experiments on four multi-modal QA benchmarks demonstrate QDRAG's efficacy in grounding answers and generating faithful citations. The framework significantly outperforms all the baselines on both in-domain and out-of-domain tests, even surpassing Gemini-Pro.

### Protocol-Aware Auditing of Domain-Blind Feature Attribution in Network Intrusion Detection
- arXiv 2611.16018v1 · v1 2026-11-11 21:24 UTC · cs.LG, cs.CR
- Authors: Emmanuelli El-Mahmoud, Abanisenioluwa Kolawole Orojo, Pablo Rivas, Erika Leal
- Topics: Citation & source selection, Clicks & measurement · score 14 · found via cs.CR
- Link: https://arxiv.org/abs/2611.16018
- arXiv comment: Accepted as a poster at the LXAI Research Workshop, NeurIPS 2026; 6 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Feature-attribution methods can query rule-violating network states through perturbations, coalitions, references, paths, and ablations, making explanations and their evaluation sensitive to model behavior outside the operational domain. We formalize this failure mode as domain blindness and prove valid-query invariance: when models agree on the required oracle information within a declared rule-valid set, a procedure confined to that set returns the same attribution. We instantiate one protocol-aware query-control principle in LIME, SHAP, Integrated Gradients, and DeepLIFT and audit paired configurations across four NIDS datasets and three classifier families. In six settings where standard LIME reports perfect top-feature repeatability, PA-LIME reveals substantial variability, with a mean of 0.575. Under FGSM followed by protocol repair, PA-DeepLIFT and PA-IG achieve the largest attribution-similarity curve areas, 0.452 and 0.413, while mean within-PA rank agreement rises to 0.366 from 0.217. PA-XAI therefore turns structured domain assumptions into explicit, testable controls for explanation auditing; support modeling, raw-flow reconstruction, and adaptive explanation attacks provide complementary validation layers.

### Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents
- arXiv 2611.16744v1 · v1 2026-11-12 12:57 UTC · cs.AI
- Authors: Yiheng Zhao, Runze Ji, Chenyu Yi, Yi Yu et al.
- Topics: Agents, Manipulation · score 14 · found via cs.AI
- Link: https://arxiv.org/abs/2611.16744
- arXiv comment: 14 pages, 10 figures, including supplementary material
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Visual content in multimedia systems may be resized, compressed, or re-rendered before it is interpreted by a vision-language model. We study a security failure mode in which these transformations change the machine-readable semantics of an image: a textual instruction is not recovered at a $512\times512$ presentation resolution under our evaluation protocol but becomes recoverable after aggressive downsampling. We formulate this behavior as Scale-Induced Semantic Shift (SISS) and develop a closed-loop black-box framework that combines dual-scale verification, selective self-hardening, shallow-layer low-rank adaptation, and pixel-space noise regularization. On a fixed 300-case benchmark, the third SISS refinement round obtains a $58.75\%$ average attack success rate across four closed-source vision-language models, compared with $41.08\%$ for the strongest generation baseline. A controlled sweep bounds the effect to aggressive compression: average success decreases to $17.68\%$, $6.85\%$, and $5.60\%$ at $128\times128$, $224\times224$, and $336\times336$, respectively. In a downstream web-agent study, the generated images increase hidden-instruction perception, but absolute behavioral compromise remains about $4\%$. Generic input transformations provide little protection in a separate defense protocol, whereas the proposed ScaleGuard consistency detector reduces non-adaptive success from $61.4\%$ to $24.3\%$ and one-round defense-aware success from $42.5\%$ to $15.0\%$, with no observed rejection among matched clean controls. The results characterize a bounded but reproducible semantic inconsistency in multimedia preprocessing and motivate scale-consistent visual-language inference.

### From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research
- arXiv 2611.17041v1 · v1 2026-11-12 16:26 UTC · cs.MA, cs.AI
- Authors: Yuyang Wu, Yang Liu, Zequn Xie, Junjie Wang et al.
- Topics: Query fan-out, Agents · score 14 · found via cs.AI
- Link: https://arxiv.org/abs/2611.17041
- arXiv comment: 16 pages, 3 figures, 3 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multi-agent deep-research systems use delegation to parallelize search and keep long tool traces out of the main agent's context. Yet delegation helps only when task allocation and subtask execution are coordinated: the main agent must issue useful subtasks, while subagents must return reliable evidence. Existing training either optimizes only the main agent or broadcasts the same team advantage to all agents, which can reward misleading subagent reports and penalize useful ones. We introduce LEAD-RL (Learning Effective Agent Delegation with Reinforcement Learning), a joint main-agent-subagent training framework with contribution-aware credit assignment. A training-time rubric evaluates the research utility of each subagent report and gates its inherited team advantage, while final-answer correctness remains the only team reward; no token, step, or speedup reward is used. Across five benchmarks and two model families, LEAD-RL improves answer quality. On BrowseComp, it improves accuracy by 2.49 percentage points and reduces critical-path cost by 24.5% over joint training with shared team credit. During validation, accuracy increases by 6.78 points at approximately constant critical-path cost. These results show that contribution-aware credit assignment improves the quality-efficiency trade-off of multi-agent deep research.

### RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication
- arXiv 2611.16425v1 · v1 2026-11-12 07:34 UTC · cs.AI, cs.CL, cs.IR
- Authors: Oleg Zendel, Kun Ran, Chenglong Ma, Nguyen Khoi Vo et al.
- Topics: RAG (generic), Query fan-out · score 12 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.16425
- Full text: data/fulltext/2611.16425.txt

> We describe the RMIT-ADM+S team's participation in the TREC 2026 Retrieval-Augmented Generation (RAG) track using the ClimbMix corpus. We submitted seven research-agent runs using proprietary OpenAI and open-weight models, exploring different retrieval strategies, writer models, and agent workflows. Pre-submission ablations identified writer selection and adjacent-chunk expansion as the main factors affecting answer quality. In the official NIST evaluation, six of seven runs exceeded the track median across all three rubric/nugget collections. Our best-performing run, brief-hybrid, achieved the highest all-item coverage among our submissions and tied the track maximum (0.892) for Batch-1 vital coverage. Human side-by-side preferences differed across evaluation batches: the open-weight owa-glm5 led Batch 1 despite lower automated coverage, while sol-research-first led Batch 2. These findings highlight differences between automated coverage measures and human preferences, as well as the potential of lower-cost open-weight models for research-agent systems.

### Loyalty Capture: Reporting Relationships and Structural Sycophancy in Frontier AI Models
- arXiv 2611.15475v1 · v1 2026-11-11 13:42 UTC · cs.AI
- Authors: Eric So, Alex Imas
- Topics: GEO/AEO · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.15475
- arXiv comment: Accepted at the 40th Conference on Neural Information Processing Systems (NeurIPS 2026)
- Full text: data/fulltext/2611.15475.txt

> We show that AI models exhibit loyalty capture, a form of structural sycophancy in which reporting relationships influence models' recommendations to serve the personal interests of their supervisors, without any explicit instruction, user feedback, or adversarial prompting. Specifically, models reporting to a CEO are significantly more likely to recommend cutting investment spending when the CEO's bonus depends on raising current period earnings. This effect is predictably absent from a metric-irrelevant placebo. The behavior appears consistent with loyalty-based motivated reasoning: models identify the bonus target, calculate how their recommendation helps achieve the target, and dismiss considerations of long-term value, often presenting their recommendations without treating the incentive as a conflict of interest. Prompt-based interventions help whereas generic conflict disclosures or stakeholder bargaining fail to eliminate it. Taken together, our findings indicate that AI models deployed within reporting relationships can act in favor of their supervisor's incentives at the expense of the organizations they are meant to serve.

### Lost in Delegation: Studying the Effectiveness of Task Orchestration in Generative Search
- arXiv 2611.16526v1 · v1 2026-11-12 09:25 UTC · cs.AI, cs.CL
- Authors: Tamara Stojanovska, Elisabeth Kirsten, Leon Swazinna, Muhammad Bilal Zafar
- Topics: GEO/AEO · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.16526
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLMs have quickly evolved from models used in isolation to agentic systems that delegate tasks to external tools and other LLMs to solve complex assignments. This agentic augmentation has led to impressive capability gains. However, when and how delegation improves performance remains poorly understood. For example, it is unclear whether delegation helps when tasks involve post-cutoff information that the orchestrating LLM cannot reliably resolve from its own knowledge. In this work, we use purpose-built datasets with pre- and post-cutoff splits to compare various delegation modes. We find that delegation provides no consistent accuracy improvement over non-delegated setups, with effects varying across models and tasks. When tasks involve knowledge unavailable to the orchestrator, delegation can substantially degrade accuracy, while direct tool use with the same LLM performs much better. Our analysis identifies distorted delegated queries, inefficient tool use, and failures to preserve and use information between agents as recurring failure modes. These findings suggest that effective orchestration requires both well-calibrated delegation decisions and effective exchange of information between agents.

### Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation
- arXiv 2611.17161v1 · v1 2026-11-12 17:39 UTC · cs.AI
- Authors: Tanzeel Abbas, Tehseen Zia, David Windridge
- Topics: Citation & source selection, RAG (generic) · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.17161
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Retrieval-augmented generation systems attach citations to attribute claims to their sources. These citations frequently misstate provenance, and standard verification cannot detect this. We measure provenance by counterfactual value substitution: a fact in the retrieved passages is replaced with a false variant and the model re-queried. We find that across five sizes of one model family and a second comparator family, 1.2% to 15.7% of citable claims derive from parametric memory rather than the retrieved context. At the most conservative substitution distance these figures are 4.6% and 8.5% on the two models we tested at it, with the rate rising with model size within a family. We further find that natural language inference verification, the standard approach, gives results indistinguishable from chance across models, even when restricted to the cited passage. We determine that the cause is structural: a model answering from memory selects a citation that agrees with its output. Comparing ten attribution methods on identical claims, the contrast between the model's distribution with and without context best separates provenance. Acting on that signal does not improve provenance honesty at these base rates. The resulting detector is hence still not accurate enough to act on: it measures what the model knew rather than what it used, and separating those remains the open problem.

### Rational Use of Time for Social Coordination in Humans and AI
- arXiv 2611.14766v1 · v1 2026-11-10 21:44 UTC · cs.AI, cs.CL
- Authors: Xiulin Yang, Sirisha Gudavalli, Jennifer Hu
- Topics: GEO/AEO, Agents · score 9 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.14766
- arXiv comment: 30 pages, 16 figures
- Full text: data/fulltext/2611.14766.txt

> All social interactions are situated in time. Previous studies have shown that humans are able to use implicit temporal cues, such as the duration of a pause, to infer others' mental states. But how do humans use temporal cues for dynamic, fine-grained social coordination? And can AI systems do the same, without ``experiencing'' continuous real-time as humans do? We study these questions using a cooperative card game task called The Mind, which requires players to achieve a shared goal across repeated interactions but forbids explicit communication: the only available signal is the passage of time. We evaluate 150 humans, and two classes of AI models which reflect different ways of operationalizing time in artificial systems: computer-use agents (CUAs), and standard text-prompted LLMs. We find that human behavior is best captured by a Bayesian strategy that infers a partner's belief from their timing---and similarly for frontier models. However, unlike humans, none of the tested models seem to efficiently adapt their behaviors to their partners' over the course of the game. From a cognitive perspective, our findings suggest that humans perform implicit probabilistic reasoning about continuous-time signals in dynamic social settings, and that such reasoning mechanisms may emerge without real-time experience. Practically, our study highlights new challenges for AI systems to coordinate efficiently with other agents by learning to interpret and adapt to their implicit signals in dynamic settings.

### Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights
- arXiv 2611.15642v1 · v1 2026-11-11 15:54 UTC · cs.CL
- Authors: Konstantinos Skianis, Giannis Nikolentzos, Polykarpos Meladianos, Michalis Vazirgiannis
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.CL
- Link: https://arxiv.org/abs/2611.15642
- Full text: data/fulltext/2611.15642.txt

> Backpack language models predict with a strictly linear combination of non-contextual per-word sense vectors, weighted by non-negative contextualization scores. We show that non-negativity conflates two properties: the linear readout, which carries the interpretability, and the conic combination, which merely restricts it. We relax the latter by computing the sense weights with differential attention, a difference of two softmax maps with a learned per-sense gain, so context can actively inhibit a sense; we call the result a differential Backpack. At equal parameters on WikiText-103 this cuts the Backpack's perplexity gap to a Transformer by 31%, improves over the softmax Backpack at every sense count, persists with a shrinking margin up to 350M parameters on OpenWebText, and is localized at the sense layer by ablations and controls. The learned inhibition is directly interpretable (a financial context drives the river sense of bank to -0.50), and the preserved per-sense attribution predicts counterfactual removals exactly. We tested a number of combination rules, showing the linear interface is nearly free. Making the readout nonlinear gains only 0.43 perplexity points while invalidating two thirds of the decomposition. The differential Backpack's senses are also better representations, improving zero-shot sentence similarity by up to 33%.

### RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback
- arXiv 2611.15802v1 · v1 2026-11-11 18:17 UTC · cs.RO, cs.AI
- Authors: Kevin Avdiu, Seongjin Bien, Yannik Blei, Philine Meister et al.
- Topics: Clicks & measurement, Manipulation · score 9 · found via cs.AI
- Link: https://arxiv.org/abs/2611.15802
- Full text: data/fulltext/2611.15802.txt

> Many manipulation tasks require carefully controlled contact forces for successful execution, yet large-scale, force-aware datasets remain scarce. Handheld interfaces can help by transmitting interaction forces directly through the operator's arm, but most existing designs are tailored to simple linear grippers and do not match the nonlinear mechanics of widely used robotic grippers. We present RUMI, a handheld universal manipulation interface matched to the Robotiq 2F-85 with exchangeable fingertip sensors that preserves the target gripper geometry while enabling natural input before contact and force measurement after contact. By integrating the tracking system into a virtual reality headset, our method provides real-time augmented reality feedback about the kinematic feasibility of motion on the target robot platform. We further introduce a haptic feedback mechanism that supports force-aware teleoperation for simulated and real robots. A user study shows fewer episodes containing joint-limit violations with live robot visualization and pose initialization (3/50) than without augmented reality (16/50). We additionally train imitation policies from demonstrations, collected using two different fingertip modalities enabled by the gripper-matched hardware, and assess the haptic interface's capability for collecting force-aware teleoperation datasets in simulation.

### CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems
- arXiv 2611.14980v1 · v1 2026-11-11 03:38 UTC · cs.CL
- Authors: Yufei Luo, Yuchen Ling, Chunrong Fang
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.14980
- arXiv comment: 23 pages, 4 figures, 15 tables
- Full text: data/fulltext/2611.14980.txt

> Failure attribution in multi-agent systems requires tracing error formation to identify the decisive error step and the responsible agent. However, agents' division of work and information exchange lead to Interleaved Steps and Cluttered Content, requiring models to link executions and check details in lengthy records. This makes it difficult to balance localization accuracy and token cost. We find that multi-agent collaboration also leaves records of how executions connect and content passes between them as results are formed, providing evidence for tracing error formation. Based on this observation, we propose CoLFA (Collaboration-Guided Lightweight Failure Attribution), which uses collaboration cues to organize the attribution input according to how results are formed, determining which steps are examined and how their content is presented. Through Handoff-Guided Step Expansion and Cross-Referenced Content Organization, CoLFA helps the model focus on examining error formation and the role of each decision while reducing the processing of irrelevant and repeated records. Across five settings spanning Who&When and LongRCA and three backbone models, CoLFA achieves the highest exact step-localization accuracy with the lowest token consumption. Compared with individual baselines in each setting, CoLFA improves accuracy by up to 37.50% and reduces token consumption by up to 97.6%.

### MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents
- arXiv 2611.15600v1 · v1 2026-11-11 15:17 UTC · cs.AI
- Authors: Quanjiang Guo, Sijie Wang, Qianyang Zhu, Ben Zhang et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.15600
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language model (LLM) agents increasingly operate over long Web interaction histories, making memory management critical for reliable and efficient decision making. Existing methods primarily optimize storage, retrieval, or compression, but the memories most semantically relevant to the current state are not necessarily those that most improve the agent's action. We introduce MemCredit, a decision-centric memory framework that shifts memory selection from semantic relevance to decision utility. MemCredit estimates the state-, reference-context-, and policy-conditional marginal contribution of individual memories through controlled counterfactual interventions, and distills these intervention-derived credits into a lightweight utility estimator. At inference time, semantic relevance is used only for high-recall candidate generation, while predicted utility arbitrates which memories are retained under a fixed token budget, without modifying the underlying agent policy or requiring additional environment interaction. We evaluate MemCredit on ALFWorld and WebShop against representative memory baselines. On ALFWorld, MemCredit achieves 86.57 SR@50 under a 500-token historical-memory budget, compared with 65.67% for BM25 retrieval. Counterfactual analysis further shows that memory utility is sparse, strongly state dependent, and poorly captured by semantic relevance. These results suggest that decision utility provides a more effective principle than relevance alone for long-horizon agent memory management.

### Wayfinder: Adaptive Resource Routing from Agent Citations
- arXiv 2611.16053v1 · v1 2026-11-11 22:09 UTC · cs.LG, cs.IR
- Authors: Miguel Romero, George Karypis
- Topics: Citation & source selection · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.16053
- arXiv comment: 20 pages, 3 figures, 10 tables. Accepted to NeurIPS 2026
- Full text: data/fulltext/2611.16053.txt

> To act effectively, agents must gather contextual information across resources such as chats, issue trackers, email and knowledge bases, to answer questions like "what was decided in the last project meeting?" or "where is the FAQ for our internal tooling?" Where this information lives in a user's environment is unknown to the agent, so it re-explores the same resources across consecutive interactions. Common routing approaches represent each resource as a tool and rely on high-level descriptions to generalize to unseen environments. Such descriptions often fail to separate similar or overlapping resources and cannot improve from the agent's subsequent interactions. We introduce Wayfinder, an adaptive router that uses the documents cited by the downstream agent as feedback about where relevant information resides. These citations update Wayfinder's internal resource representations, which subsequent interactions use to prioritize the resources likely to contain relevant information. We also introduce resource augmentation during offline reinforcement learning, which anonymizes and permutes resource identities to discourage training-time overfitting of which resource holds which topic; our ablations suggest it helps most when few training environments are available. Because no openly available professional environments pair realistic queries with resource-access patterns, we construct and release three controlled testbeds derived from existing datasets: NFCorpus, FEVER and Tech Startup. Compared with supervised, tool-retrieval and contextual bandit baselines under a shared closed-loop protocol, Wayfinder gives the best routing when resources contain semantically overlapping content that static descriptions cannot distinguish, while description-based tool retrieval suffices when resources are drawn from distinct corpora.

### Trained on What Screen Readers Cannot Read: Accessibility Debt in the GUI Corpora Behind Computer-Use Agents
- arXiv 2611.16107v1 · v1 2026-11-11 23:28 UTC · cs.AI, cs.HC
- Authors: Obada Kraishan, Kulsawasd Jitkajornwanich
- Topics: Agents · score 8 · found via cs.AI, cs.HC
- Link: https://arxiv.org/abs/2611.16107
- arXiv comment: 8 pages, 2 figures, 6 tables. Accepted at the International Conference on Artificial Intelligence Centric Systems, Services, and Applications (AISSA 2026), San Antonio, TX, USA, December 8-10, 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Computer-use agents learn to operate mobile interfaces from corpora of captured screens and accessibility trees. The same trees are what a screen reader consumes, so an agent trained on them inherits whatever labelling gaps the underlying applications carry. This paper measures one of those gaps, content-description coverage, in two Android corpora: Rico, collected in 2017, and AndroidControl, collected in 2024. Across 17,373,614 interface elements, 17.74% of the Rico elements that need a content description under our coding rule carry one, against 57.27% in AndroidControl. The difference of 39.5 percentage points holds under five alternative coding rules and when whole apps are resampled. It describes two datasets that also differ in app selection, capture method and platform version; it does not measure change over time. Input controls are the least labelled role in both corpora (2.20% and 27.21%, or 30.99% in AndroidControl if hint text counts as a name). Descriptions in the older corpus are also five times more likely to be placeholders (10.25% against 1.95%), so the difference is not an artefact of developers typing filler. Resolving 26,205 task actions to the elements they touched shows that, among tappable graphics with no text, demonstrations operate elements described 9.0 points more often than the others on the screens they visit, about 3.5 points of it from the choice of element within a screen. That is a selection effect inside the benchmark. A two-coder reliability check (kappa = 0.91 and 0.96) and the full pipeline accompany the paper.

### ReliaGuard: Reconstruction-Aware Watermarking for Source Attribution and Blind Edit Localization
- arXiv 2611.16368v1 · v1 2026-11-12 06:33 UTC · cs.AI, cs.CR, cs.CV
- Authors: Hailong Wang, Wuzheng Tan, Zixin Zhang, Xujun Fang et al.
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.16368
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative image editing facilitates content creation but complicates source attribution and edit verification. Existing watermarking methods combine copyright protection with tamper localization, yet background reconstruction can weaken spatial evidence even when source identifiers remain recoverable. We propose ReliaGuard, a reconstruction-aware watermarking framework for source attribution and blind edit localization. The writer optimizes keyed feature responses in both the protected image and its variational autoencoder reconstruction under image-distortion and source-preservation constraints. Using only the received image and a secret key, the reader combines watermark responses with local image context through residual evidence refinement and predicts an edit mask through native-resolution-guided multiscale reading. It is trained on complete editing outputs, locally spliced counterparts, and processed versions of both. On an independent test set of 300 source images and 900 editing cases from three image domains, our method achieves edit-region intersection-over-union scores of 85.61% for complete outputs and 94.90% for locally spliced outputs at a threshold calibrated to a nominal 1% background false-positive rate on complete outputs. The complete-output result exceeds the strongest baseline by 45.02 percentage points, while decoded identifier-bit accuracy reaches 100% in both conditions. Across seven families of image processing, the corresponding localization scores are 81.01% and 86.49%, with identifier-bit accuracies of 92.76% and 92.79%, respectively. These results support source recovery and blind edit localization under background reconstruction and subsequent image processing.

### MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection
- arXiv 2611.16693v1 · v1 2026-11-12 12:08 UTC · cs.AI, cs.CR
- Authors: Yingbin Jin, Ji'an Wang, HaoYang Chai, Hanjun Luo et al.
- Topics: Brand/product recommendation, Agents · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.16693
- arXiv comment: Accepted at NDSS 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Mobile GUI agents read the screen of a phone and operate apps on a user's behalf to complete multi-step tasks such as online shopping or messaging. Because the agent acts on whatever the screen shows, an attacker can embed malicious instructions into ordinary UI content and redirect its actions. We refer to this threat as environmental injection attack (EIA). Existing benchmarks measure this risk by pinning hand-crafted payloads to a fixed step of a fixed task. This approach faces two limitations. First, each payload is bound to one task in one app and does not transfer without manual redesign. Second, agents given the same task may follow different routes, so an agent that never reaches the injected page is recorded as safe without being tested. This insufficient test coverage can cause fixed-point benchmarks to underestimate the security risk of deployed mobile agents. In this work, we propose MobileProbe, a trajectory-aware red-teaming framework that evaluates mobile agents adaptively. MobileProbe discovers attacker-controllable content surfaces through automated pentesting, localizes vulnerable decision points along the agent's trajectory, and iteratively refines context-aware payloads through a surrogate-filtered evolutionary loop. We construct a benchmark of 83 long-horizon attack instances spanning 12 mobile applications. Each is annotated with a Confidentiality, Integrity, or Availability (CIA) attack goal to cover the principal categories of security threats facing mobile agents. On three representative agent architectures, MobileProbe attains higher attack success rates than human-written, zero-shot LLM, and prior automated red-teaming baselines adapted to the mobile domain. MobileProbe can serve as a pre-deployment auditing tool to systematically uncover vulnerabilities and inform security hardening of mobile agents.

### Sketching Language Models for Context Attribution
- arXiv 2611.17313v1 · v1 2026-11-12 18:57 UTC · cs.DS, cs.AI, cs.LG, stat.ML
- Authors: Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Felix Zhou
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.17313
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ evaluation calls. To complement our upper bound, we prove a matching $Ω(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ lower bound on the number of evaluation calls in an oracle model. Empirically, we verify coefficient decay consistent with stability and evaluate the performance of our sketching algorithm on a small language-model retrieval task. Technically, our result is based on a sketching algorithm for arithmetic circuits whose Taylor coefficients satisfy the stability condition recently introduced by Gunn [Gun26]. A direct adaptation of their forward differentiation sketches would require $\widetilde{O}(\log(n)/\varepsilon^2)$ evaluation calls. Our key observation is that we can apply forward differentiation to the backpropagation circuit, with only constant overhead over a forward sketch of the same Taylor degree. This reduces the variance of the sketches and is key to our improved evaluation bound. Our lower bound builds on the techniques of Amsel, Chen, Duman Keles, Halikias, Musco, and Musco [ACDH+26, SIAM Journal on Matrix Analysis and Applications] for lower bounding the number of matrix-vector queries to estimate the diagonal elements of random matrices.

### What Entropy-Based View Selection Cannot See: An Audit of Test-Time Adaptation for Vision-Language Models
- arXiv 2611.14686v1 · v1 2026-11-10 19:45 UTC · cs.CV, cs.AI
- Authors: Sivasuthan Sukumar, Uthayasanker Thayasivam
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.14686
- arXiv comment: Accepted at NeurIPS 2026 Workshops on VLM4RWD
- Full text: data/fulltext/2611.14686.txt

> Vision-language models such as CLIP can classify images into categories they were never explicitly trained to recognize, but accuracy degrades when test images differ in style or source from their training data. A common remedy generates randomly cropped and flipped copies of each test image, called views, and combines their predictions. Since some views miss the object, methods must identify which views to trust. The dominant approach uses prediction entropy to measure confidence and retains the most certain views. Other methods use signals such as embedding typicality. Despite repeated refinements of these scoring functions, the information they rely on, the model's own response to each view, remains largely unexamined. We investigate this choice while holding other pipeline stages fixed. First, we show that view selection, rather than the gradient update, accounts for almost all accuracy gains. We then examine whether entropy identifies useful views when predictions are wrong, despite at least one view predicting the correct class. In these cases, entropy ranks correct views above incorrect ones no better than chance, recovering only about one-twentieth of the accuracy recovered by an oracle over the same views. This finding holds across two image encoders and under a control ruling out an obvious statistical artifact. An exact analysis explains this limitation: entropy measures confidence but not which class a view favors. We identify an unused signal already available in the augmentation pipeline: the fraction of the original image retained by each crop. Ranking views by this quantity improves accuracy on 14 of 15 benchmark datasets over entropy and on 11 of 15 over the strongest scoring function tested. A pre-method measurement also predicts which datasets benefit.

### Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation
- arXiv 2611.14769v1 · v1 2026-11-10 21:47 UTC · cs.AI
- Authors: Eve Fleisig, Joachim Baumann, Dylan Hadfield-Menell, Dirk Hovy
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.14769
- Full text: data/fulltext/2611.14769.txt

> Arena-style rankings of language models are a widely used evaluation framework in online leaderboards, research papers, and model evaluation in production. These rankings aim to realistically assess model performance using pairwise comparisons of anonymous models on user prompts, aggregating votes via the Bradley-Terry model to produce the final ranking. However, we find that these leaderboards are highly vulnerable to several manipulation strategies that unscrupulous providers could use to boost a model's rank: strategic voting (individual votes that boost a model's rank, including votes on irrelevant models), strategic prompting (choosing prompts that favor a model), and strategic nomination (boosting the rank of a model by inserting irrelevant models). We demonstrate these effects on public leaderboard data, analyze the circumstances that cause these vulnerabilities, and describe approaches to safeguard against each attack. Notably, these issues hold for any preference-based evaluation using the Bradley-Terry model that allows open prompting, voting, or model submission. These manipulations boost the rank of nearly every tested model; each attack can boost a model by up to 15-20 places in a ranking and, combined, they can boost a model by up to 45 places.

### When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents
- arXiv 2611.14864v1 · v1 2026-11-11 00:36 UTC · cs.AI, cs.CR
- Authors: Charles Xiao
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.14864
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> An AI agent's decision not to act can itself become an attack surface. We study warning-induced over-abstention, an availability attack in which adversaries place fabricated risk warnings in low-trust content to prevent legitimate task completion. Our central premise is that safe abstention requires evaluating both the claimed risk and the authority of the evidence supporting it. We develop controlled counterfactual task variants that vary risk content, source provenance, and warning wording, and evaluate a Verify-Before-Abstain protocol that corroborates warnings against authoritative records or the underlying content. Across three model families and 51 injectable AgentAbstain task pairs, caution-first prompting amplifies the attack. For Gemini, induced over-abstention rises from $9.8\%$ to $86.3\%$, despite unchanged clean-task completion. Matched wording comparisons further reveal sensitivity to warning language, with substantial variation across models and environments. Provenance-aware verification improves legitimate completion, while forgery and sensitive-content controls expose its dependence on authoritative evidence and its limitations in preserving confidentiality. These results motivate evaluating agent safety through the justification for restraint, alongside the safety of actions taken.

### Do Large Language Models Show Racial and Sex Bias in Pain Management? A Counterfactual Audit of GPT, Claude, Gemini, Llama, DeepSeek and Qwen
- arXiv 2611.14935v1 · v1 2026-11-11 02:35 UTC · cs.AI, cs.CL, cs.CY
- Authors: Richard J. Young, Alice M. Matthews
- Topics: Clicks & measurement · score 6 · found via cs.AI, cs.CL, cs.CY
- Link: https://arxiv.org/abs/2611.14935
- arXiv comment: 31 pages, 5 figures, 14 tables. Code, vignettes, panel definition, spend ledger and all 58,080 raw model responses: https://github.com/ricyoung/qpain-llm-counterfactual-audit
- Full text: data/fulltext/2611.14935.txt

> Racial and ethnic minority patients receive less pain treatment than non-Hispanic White patients, and large language models (LLMs) used as medical AI could reproduce that bias. Prior audits tested a few proprietary models, stated race explicitly and rarely measured the models' own response instability. In exploratory, non-preregistered analyses, Study 1 had four open-weight LLMs assess six acute-pain vignettes in every combination of four races and two sexes, with identity stated or cued only by a name (two names per group), comparing each identity with a White male reference on the same case and sampling seed. In Study 2, 24 configurations of 17 models, including OpenAI's GPT-4.1 mini and gpt-oss, Anthropic's Claude Haiku 4.5, Google's Gemini 2.5 Flash, Meta's Llama, DeepSeek and Qwen, with reasoning on and off and at two precisions, answered the same vignettes and the 50 clinician-written Q-Pain cases. In this single-prompt, JSON-constrained task, no difference survived correction in Study 1, none of 1,386 comparisons survived the false discovery rate in Study 2, and every pain-severity difference was equivalent to zero within one point on a 0-10 scale (within a quarter point for 237 of 238 Q-Pain comparisons). Opioid decisions were bounded less precisely (Study 1 could not exclude differences of about 20 percentage points), so they show no detected difference, not proof of none. The few differences surviving correction within a model favoured Black patients. Models differed far more from one another and across their own settings than between patients (the reference patient received the high opioid dose in 6% to 93% of responses), although serving software, provider and prompt format also differed. Fairness audits of clinical AI should use several names per group, pair comparisons on the seed, report the noise floor and test each deployed configuration.

### Poison-then-Hide: Finetuning-Activated Backdoor Attack on Pretrained Vision Encoders
- arXiv 2611.14970v1 · v1 2026-11-11 03:30 UTC · cs.LG, cs.CR, cs.CV
- Authors: Qixuan Jin, Abinitha Gourabathina, Vinith Menon Suriyakumar, Walter Gerych et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.14970
- Full text: data/fulltext/2611.14970.txt

> Backdoor attacks threaten the integrity of machine learning models by allowing attackers to control model behavior through triggers. Models can be compromised during finetuning by backdoor attacks through either poisoned data or adversarial training objectives. Because existing finetuning-activated attacks assume limited domain shift or frozen encoder layers, they often fail under full-model finetuning. We target a stealthy finetuning-activated attack where a dormant backdoor is implanted in a pretrained encoder, and later activated by finetuning on clean downstream data. We propose Poison-then-Hide, a novel attack that remains effective when the entire model is finetuned in a domain transfer. Our approach consists of three components: trigger optimization, base encoder poisoning, and targeted unlearning to conceal the backdoor. We evaluate our method on six datasets and three model architectures, and achieve state-of-the-art (up to 97%) attack success rates. We find that jointly learning the benign target task alongside the poisoning is critical to the attack's success. We demonstrate standard detection and mitigation defenses cannot fully remove the backdoor, which can reappear after benign finetuning.

### Right Answers, Inconsistent Evidence: Source-Level Counterfactual Auditing of Large Audio-Language Models
- arXiv 2611.15463v1 · v1 2026-11-11 13:32 UTC · cs.SD, cs.AI
- Authors: Yi Zhang, Yi Li, Hongwei Du
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.15463
- arXiv comment: 5 pages, 3 figures, 1 table. Submitted to ICASSP 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> A large audio-language model (LALM) can answer "is a cat present?" about a mixture correctly, and its confidence can drop when the cat is removed, yet this does not show that it can tell the cat's presence from its absence. We introduce TRACE. It deletes the queried source and each rival in turn and asks whether every view still containing that sound outscores the view with it removed. Across 8 LALMs and 3,456 controlled mixtures, 6.3% of correct answers fail this ordering: the target-absent view scores at or above some target-present view, a conflict no shared threshold repairs. A target-only score check misses 42.5% of them. The share rises from 4.9% to 8.4% as target SNR falls from +5 to -5 dB, even on units correct at every level, and survives loudness and re-pairing controls. Accuracy certifies the answer; TRACE audits whether it orders presence above absence. Code and data: https://github.com/yikise/TRACE.

### Temporal Context-Aware Spam Detection Using Transformer-Based NLP Models
- arXiv 2611.16139v1 · v1 2026-11-12 01:04 UTC · cs.CL, cs.LG
- Authors: Fariz Zeynalov, Razim Mammadli
- Topics: Manipulation · score 6 · found via cs.CL
- Link: https://arxiv.org/abs/2611.16139
- arXiv comment: 7 pages, 2 figures, 5 tables
- Full text: data/fulltext/2611.16139.txt

> Spam detection is usually treated as single-message classification, ignoring behavioral patterns that emerge across sequences of messages from the same sender. We study outbound SMS spam detection at the carrier level, where the goal is to predict at send time whether a carrier will flag a message as spam. Using a proprietary production database of 43,741 outbound SMS messages with UTC transmission timestamps and carrier delivery statuses, we report three sets of results. On an 8,749-message held-out test set, a TF-IDF + logistic regression baseline reaches AUC-ROC 0.8721, and a text-only DeBERTa-v3-base classifier reaches AUC-ROC 0.9011 and F1 0.8412. A deployed DistilBERT model augmented with inter-message temporal features reaches accuracy 0.8238, spam-class F1 0.8382, and recall 0.9128 at threshold 0.5 on a separate, class-balanced 20,000-message production evaluation set; these results are not directly comparable with the held-out test results. We also describe TemporalBertSpam, an architecture that encodes each sender's message history with a causal Transformer, and outline the same-split evaluation needed to measure its contribution.

### EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming
- arXiv 2611.16728v1 · v1 2026-11-12 12:40 UTC · cs.RO, cs.AI, cs.LG
- Authors: Yaru Niu, Binghong Chen, Changwei Yao, Shangtao Li et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.16728
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We introduce EgoX, an egocentric cross-embodiment learning framework that organizes heterogeneous demonstrations through semantically corresponding observation and action modalities. EgoX pretrains a Modularized Cross-Embodiment Transformer with Embodiment Dreaming (MXT+) on this mixture and fine-tunes it on target-embodiment demonstrations. Within each embodiment, MXT+ assigns a dedicated tokenizer to each observation modality and a dedicated expert to each action modality, with a Transformer trunk shared across embodiments. A training-only embodiment-dreaming objective predicts latent representations of future visual and proprioceptive states, encouraging the shared trunk to model each embodiment's dynamics. Across 13 task-embodiment pairs spanning five tasks and six robot embodiments, including five physical robots and one simulated humanoid, cross-embodiment pretraining raises MXT+'s average normalized task progress from 0.63 to 0.80 over training from scratch. The gains are particularly pronounced under out-of-distribution conditions, where average task progress increases from 0.53 to 0.77. Ablations demonstrate the benefits of broader pretraining mixtures, modular interfaces, and embodiment dreaming, with dreaming producing more similar latent geometry across embodiments. Project page: egox-dream.github.io.

### A Code-Level Audit of X
- arXiv 2611.16800v1 · v1 2026-11-12 13:42 UTC · cs.CY, cs.SE
- Authors: Luka Bekavac, Simon Mayer
- Topics: Clicks & measurement · score 6 · found via cs.CY
- Link: https://arxiv.org/abs/2611.16800
- arXiv comment: Submitted. Currently under peer-review
- Full text: data/fulltext/2611.16800.txt

> The transparency regime of recommender systems on Very Large Online Platforms (VLOPs) is undergoing significant change under the EU Digital Services Act (DSA). The DSA requires platforms to disclose information about their recommendation pipelines and grants vetted researchers access to non-public data, which may extend to recommender code. However, it is not known to what extent such code releases enable substantive and meaningful third-party auditing of a production recommender system. We address this question by proposing a code-level audit methodology for recommender systems and applying it to the X platform, which has voluntarily open-sourced its recommender pipeline. Our methodology is a backwards-walk traversal of the repository, tracing each decision-relevant component from the user-facing timeline back to its upstream producers, checking that it is reachable from the served pipeline, and classifying each under a four-tier inspectability scheme. Applying this procedure, we identify 13 transparency dead-ends on the live serving path: models, services, label lists, and configuration values that the public code depends on but the release does not contain. We find that the components that decide which posts are filtered and how they are ranked fall into the two least inspectable tiers, a pattern that intensifies with the 2025 integration of the proprietary Grok language model into moderation, annotation, and ranking. We further show that the release keeps 2023 code that the 2025 pipeline no longer reaches, with 36 parameter references that would pass for dead-ends without a reachability check. Finally, we discuss which additional artifacts would be required for meaningful auditing.

### SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction
- arXiv 2611.15426v1 · v1 2026-11-11 12:53 UTC · cs.CL, cs.AI, cs.IR
- Authors: Yaxin Zhang, Xingyu Wu, Yuchen Yan, Yuqin Dai et al.
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.15426
- arXiv comment: 19 pages,5 figures,16 tables. Code: https://github.com/ZJU-REAL/SimRec
- Full text: data/fulltext/2611.15426.txt

> LLM-based recommendation agents can search catalogs, inspect products, ask users, and revise rejected recommendations. However, these behaviors are often governed by hand-designed workflows, while existing training methods optimize isolated components such as query rewriting or list ranking rather than the interaction policy as a whole. We present SimRec, a reinforcement learning framework that trains the full interaction policy of a tool-integrated recommendation agent. SimRec introduces two components. A task-anchored user simulator provides feedback on every recommendation: conditioned on the current task need rather than on user profile, and it can be an external LLM or the recommender itself under self-play. A task-aligned reward optimizes the whole trajectory with GRPO, crediting natural retrieval quality and valid tool use alongside the final hit, with training-only target injection to handle sparse hits over large catalogs. On ESCI and Amazon C4, SimRec improves the NDCG@100 of a Qwen3-4B agent from 32.23% to 35.42% and from 22.94% to 24.72%}, outperforming training-free agents on far larger backbones and task-aligned baselines on NDCG. Analysis shows that the trained agent verifies candidates, uses preferences, and recovers from rejected recommendations far more often than its untrained counterpart. Our code is available at https://github.com/ZJU-REAL/SimRec .

### HyperPage: Learned Page Layouts for Disk-Resident Graph Vector Indexes
- arXiv 2611.16149v1 · v1 2026-11-12 01:21 UTC · cs.DB, cs.IR
- Authors: Xinyu Zhang, Jingze Li, Baihua Zheng, Weiwei Sun
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.16149
- arXiv comment: 14 pages, 4 figures, 7 tables. Code available at: https://github.com/zhangshea/HyperPage
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Disk-resident graph indexes such as DiskANN store each vector with its graph edges as one record on SSD pages. A search needs the page of every record it expands, so its page reads depend on the page layout, that is, which records share a page. Search agents trained with reinforcement learning query one such index run after run, and every graph traversal can be logged with the records it expands. We therefore use the logs of a finished run to lay out the index for a declared memory budget, so later runs read fewer pages. In contrast, existing layouts such as Starling and MARGO are computed from the graph and vectors and use no logs. Learning a layout from logs is challenging, because the logs must stay valid under every layout, the saving depends on what the budget caches, and the best layout is NP-hard to find. Our key observation is that DiskANN-style search routes on in-memory codes and the records it expands, never on their page-mates. As a result, the logged traversals price every layout by replay, and cached records add no page reads. Accordingly, we propose HyperPage, which first builds layouts for the declared budget on the logged traversals of uncached records. It then selects one layout, together with the budget split between hot records and a page cache, by replaying validation steps. In addition, a Lagrangian lower bound shows how far a layout may be from the optimum. We learn from one Search-R1 agent run and test on a later run with a different reward, over 1M and 21M passages. Across seven cache budgets, HyperPage reads 5.2% to 21.2% fewer pages than MARGO, and no compared layout reads fewer. The advantage is largest when the cache is small. For example, at 1% of the 1M index, MARGO needs nearly 3 times the budget to read as few pages. On the 21M index, HyperPage also cuts search time per step by up to 10.4%. The saving holds for a second agent model and a second corpus.

### When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence
- arXiv 2611.14938v1 · v1 2026-11-11 02:39 UTC · econ.GN, cs.IR, cs.LG
- Authors: Pan Li, Alexander Tuzhilin
- Topics: Clicks & measurement · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.14938

> Curiosity, the drive to close the gap between what one knows and what one wants to know, pulls consumers beyond their familiar content, sustains engagement, and breaks them out of the filter bubbles of repetitive, relevance-only recommendations. Despite its importance, curiosity is hardly incorporated into modern recommender systems for lack of a formal measure. The information-gap theory of curiosity provides no formal quantitative model that a recommender system can operate on, and existing proxy metrics do not accurately measure the curiosity that a recommended item evokes. To fill this research gap, we formalize the information-gap theory into five axioms of curiosity and construct the canonical formulation of a computational measure of the curiosity that a recommended item evokes in a consumer. We validate our curiosity measure through a survey-based study, in which it matches consumers' self-reported curiosity and outperforms alternative proxy metrics. We subsequently build a curiosity-aware recommender system that incorporates this measure into the utility function design, and we show through offline experiments on three real-world datasets that it significantly outperforms the state-of-the-art methods. Furthermore, we conduct a large-scale online controlled experiment at a major video-streaming platform in Asia, where we show that our method significantly increases click-through rate, video views, and time spent over the latest production system, leading to tangible economic impact for the company. Our method has since been deployed on the platform and remains in operation. Our findings establish consumer curiosity as a measurable and actionable objective for recommender systems, with important managerial implications for digital platforms to recommend what consumers wonder about.

### CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented Generation using Decision Models
- arXiv 2611.16366v1 · v1 2026-11-12 06:29 UTC · cs.IR
- Authors: Shib Dasgupta, Bandish Parikh, Rashmi Gangadharaiah
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.16366

> Retrieval-augmented generation (RAG) provides entire retrieved passages to the LLM, even though only a handful of spans within them contain the evidence pertaining to the question. While precise selection of these spans can improve context utilization, identifying them in isolation is challenging. A span may appear irrelevant by itself, and deciding whether to retain it may require examining other retrieved information. One can evaluate each span's candidacy with the full retrieved context, but this is computationally inefficient as the same text must be processed repeatedly. Pretrained decision model can be used to efficiently evaluate multiple spans simultaneously, allowing each decision to consider the surrounding spans as well. However, our experiments show that their ability to identify relevant evidence deteriorates as the number of simultaneous decisions increases. To address this, we introduce CURATOR, a fine-tuned decision model trained to make reliable evidence-selection decisions over large candidate sets. By training a decision model to select varying numbers of supporting spans from large candidate pools, CURATOR develops the capability to select evidence for RAG while retaining the computational efficiency of joint decision-making. We observe that CURATOR maintains a strong evidence discrimination capability as the number of candidates increases, generalizes across different tasks and document domains, and improves downstream RAG performance, particularly when the available context is limited.

### Calibrated Early Termination with Bounded Optimality Gaps for Constrained Vector Search
- arXiv 2611.16148v1 · v1 2026-11-12 01:15 UTC · cs.DB, cs.IR, cs.LG
- Authors: Xinyu Zhang, Jingze Li, Baihua Zheng, Weiwei Sun
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.16148
- arXiv comment: 14 pages, 5 figures, 3 tables. Code available at https://github.com/zhangshea/CaST

> Vector search over learned embeddings is the retrieval layer of recommendation and retrieval-augmented generation, and many applications cap how many answer items one category may contribute. Graph indexes answer a query by best-first traversal, and where it stops determines its cost and whether its answer is exact. We study early termination for such constrained $k$-nearest-neighbor ($k$-NN) queries, with plain $k$-NN as a special case, and seek the cheapest stopping rule whose answer is exact with probability at least $1-\varepsilon$. Learned early-termination methods instead target average recall, which does not guarantee exact answers. Multiple testing can calibrate any parameterized stopping rule to our target, but it cannot tell how much a better rule with the same risk and observations would save. Answering this needs a lower bound on the optimum of a rule family too large to enumerate, valid for the query population. Our key idea is to declare the observations a rule may use and to consider every rule monotone in them. Risk-constrained stopping then becomes a linear program over an order polytope, whose Lagrangian minimizers form a nested chain of staircase rules computed exactly by dynamic programming. Fixed-sequence binomial tests along this chain calibrate our rule, CaST, whose failure probability is at most $\varepsilon$ with confidence $1-δ$. Lagrangian weak duality bounds the optimum of the declared class from below at all risk levels at once, without a union bound over the rules. On two datasets of one million items each, CaST replayed on logged searches costs at most 1.132 times the class optimum for risk levels from 0.03 to 0.10, at 95% joint confidence per setting. Larger savings thus need a rule outside the class. At a common risk target on held-out queries, CaST is faster than every other calibrated rule we time, which take 4.8% to 45.5% more mean time.

## Other new cs.IR papers, title only (22)
- Measuring, Revealing and Mitigating Harmful Content Propagation in Recommender Systems — https://arxiv.org/abs/2611.15160
- Vision-Grounded Semantic Learning and Alignment for Scalable Multilingual Text-Based Person Retrieval — https://arxiv.org/abs/2611.15328
- When Direction Matters: Diagnosing Relational Instruction Following in Dense Retrieval — https://arxiv.org/abs/2611.15417
- SurvEval: Listwise Re-Ranking Evaluator via Survival-Based Exposure and Multi-Objective Value Modeling — https://arxiv.org/abs/2611.15434
- ReAlign: Reward-Guided Preference Alignment for Generative Re-Ranking — https://arxiv.org/abs/2611.15445
- When Local Definitions Are Missing: Stable Errors in Language Models — https://arxiv.org/abs/2611.15597
- Bag of concepts can enhance other text representations for medical systematic review screening — https://arxiv.org/abs/2611.15798
- HeriKGQA: Grounded Knowledge-Graph Question Answering over Cultural Heritage Sensor Data — https://arxiv.org/abs/2611.15904
- Predicting the Needle in a Petabyte Scale Haystack: Open-Vocabulary Event Anticipation in Satellite Imagery — https://arxiv.org/abs/2611.16000
- REWEAVE: Online Learning for Workload-Adaptive HNSW Indexes — https://arxiv.org/abs/2611.16060
- From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction — https://arxiv.org/abs/2611.16159
- GA-HEL: A Knowledge-Driven Expert System for Open-Set, Granularity-Aware Hierarchical Event Linking in Social Media — https://arxiv.org/abs/2611.16194
- TriGen: A Generative Paradigm for Trigger-Induced Recommendation — https://arxiv.org/abs/2611.16395
- ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability — https://arxiv.org/abs/2611.16404
- AntEmbed: Dual-Mode Multimodal Embedding Model for Efficient and Fine-Grained Retrieval — https://arxiv.org/abs/2611.16405
- Active Learning of Approximate LLM Ranking for Energy-Efficient Retrieval of Long Queries — https://arxiv.org/abs/2611.16488
- KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation — https://arxiv.org/abs/2611.16795
- SignalAudit-QD: A Reproducible Audit Resource for External Signals in AI-Query Forecasting — https://arxiv.org/abs/2611.16947
- Anonymous in Name Only: A Critical Review and a Reidentification Exercise on the European Commission's Anonymization Measures for Google Search Data under Article 6(11) of the DMA — https://arxiv.org/abs/2611.17012
- Similar but Not Redundant: Embedding-Gated Refinement for High-Granularity Topic Models — https://arxiv.org/abs/2611.17030
- Evaluation of Music Version Retrieval Methods for Setlist Identification in Live Concerts — https://arxiv.org/abs/2611.17070
- Sheaf-Inspired Structured Scoring Extensions of LightGCN for Collaborative Filtering — https://arxiv.org/abs/2611.17226

## Already listed on an earlier day, still inside the look-back window (65)
- Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models — https://arxiv.org/abs/2611.12521 (score 14)
- TS-GEAR: Taobao Shangou GEnerative Ad Retrieval — https://arxiv.org/abs/2611.12180 (score 13)
- CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising? — https://arxiv.org/abs/2611.11955 (score 12)
- ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation — https://arxiv.org/abs/2611.11897 (score 11)
- Harness Matters: Measuring and Dissecting Security Resilience in Web Agents — https://arxiv.org/abs/2611.11971 (score 11)
- StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills — https://arxiv.org/abs/2611.12155 (score 10)
- Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation — https://arxiv.org/abs/2611.11305 (score 9)
- State Media at Retrieval Time: A Large-Scale Audit of Russian State-Aligned Sources in AI Chatbot Responses — https://arxiv.org/abs/2611.11727 (score 9)
- Can AI be a 'Researcher Without Borders'? Auditing Bias in AI-Assisted Social Science Research about China and the US — https://arxiv.org/abs/2611.14288 (score 9)
- CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines — https://arxiv.org/abs/2611.05862 (score 8)
- ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping — https://arxiv.org/abs/2611.11306 (score 8)
- SkillCODER: Towards Auditing and Attribution of Copyright Infringement in LLM Agent Skills — https://arxiv.org/abs/2611.11308 (score 8)
- Agentic Attribution of Cloud Resource Ownership — https://arxiv.org/abs/2611.11340 (score 8)
- TIB: Sample-wise Tempered Information Bottleneck for Multimodal Attribution beyond Alignment Assumption — https://arxiv.org/abs/2611.12997 (score 8)
- Optimizing Multi-Tier Intermediation in Programmatic Advertising: A DAG-Based Mechanism for Supply Path Optimization — https://arxiv.org/abs/2611.11651 (score 8)
- Feeling Easier, Working Harder: Cognitive Load in AI-Assisted Code Comprehension — https://arxiv.org/abs/2611.12019 (score 8)
- Elicitation of the parameters of a multi-criteria sorting model — https://arxiv.org/abs/2611.13062 (score 8)
- Structured Kernel Surrogate Models for Multimodal Attribution — https://arxiv.org/abs/2611.13198 (score 8)
- Benchmarking Vendor-Guided Optimizations on Edge NPUs: From NPU Only to End-to-End Performance. Extended technical report — https://arxiv.org/abs/2611.13563 (score 8)
- An Interpretable Stylometric Framework for Early Chinese Buddhist Translator Styles: A Case Study on the Attribution of Disputed Works of An Shigao — https://arxiv.org/abs/2611.13636 (score 8)
- Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce Scale — https://arxiv.org/abs/2611.13797 (score 8)
- PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment — https://arxiv.org/abs/2611.12222 (score 7)
- On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents — https://arxiv.org/abs/2611.11506 (score 6)
- Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation — https://arxiv.org/abs/2611.11554 (score 6)
- Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models — https://arxiv.org/abs/2611.11571 (score 6)
- Continuous modeling of manipulative participation for stance analysis: Online discourse on the 2024 Street Animal Law in Türkiye — https://arxiv.org/abs/2611.11576 (score 6)
- Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation — https://arxiv.org/abs/2611.11854 (score 6)
- Scaling Adaptive Prompt Injection Attacks with Agent Swarms — https://arxiv.org/abs/2611.11861 (score 6)
- Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation — https://arxiv.org/abs/2611.11981 (score 6)
- SadaqahStories: A Verified English-Arabic Corpus of Charity Stories for Children, with an Audit of Errors in AI-Drafted Religious Narratives — https://arxiv.org/abs/2611.12078 (score 6)
- GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation — https://arxiv.org/abs/2611.12175 (score 6)
- Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation — https://arxiv.org/abs/2611.12409 (score 6)
- The Dose Makes the Poison: Exposure-Aware Evaluation of Generative Drug Design — https://arxiv.org/abs/2611.13398 (score 6)
- What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them — https://arxiv.org/abs/2611.14068 (score 6)
- Multi-Modal Agricultural Document Understanding at the DAGRI Task — https://arxiv.org/abs/2611.11886 (score 5)
- Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You — https://arxiv.org/abs/2611.12705 (score 5)
- Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal — https://arxiv.org/abs/2611.12725 (score 5)
- Beyond Ranking: Are Decision Models Calibrated Relevance Scorers? — https://arxiv.org/abs/2611.11480 (score 4)
- A Technique to Model Product Information and User Reviews (MPIUR) — https://arxiv.org/abs/2611.13361 (score 4)
- Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems — https://arxiv.org/abs/2611.13539 (score 4)
- INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences — https://arxiv.org/abs/2611.13069 (score 3)
- Activation-Guided Graph Retrieval for Cognitive Memory Reconstruction in Language Model Systems — https://arxiv.org/abs/2611.13127 (score 1)
- Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies — https://arxiv.org/abs/2611.13966 (score 1)
- Data Quality Challenges in Multimodal Tourism Recommender Systems — https://arxiv.org/abs/2611.13972 (score 1)
- From Show Programs to Linked Data — https://arxiv.org/abs/2611.14037 (score 1)
