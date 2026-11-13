# Paper candidates — 2026-11-13 (IST)

Generated 2026-11-13 08:04 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 14 new topic matches · 0 other new cs.IR · 19 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (14), highest score first

### Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition
- arXiv 2611.15538v1 · v1 2026-11-11 14:22 UTC · cs.CL, cs.AI
- Authors: Yue Liu, Zhongying Ru, Shimin Di, Jipeng Zhang et al.
- Topics: Citation & source selection, RAG (generic), Query fan-out · score 20 · found via cs.CL
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

### RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication
- arXiv 2611.16425v1 · v1 2026-11-12 07:34 UTC · cs.IR, cs.AI, cs.CL
- Authors: Oleg Zendel, Kun Ran, Chenglong Ma, Nguyen Khoi Vo et al.
- Topics: RAG (generic), Query fan-out · score 12 · found via cs.CL
- Link: https://arxiv.org/abs/2611.16425
- Full text: data/fulltext/2611.16425.txt

> We describe the RMIT-ADM+S team's participation in the TREC 2026 Retrieval-Augmented Generation (RAG) track using the ClimbMix corpus. We submitted seven research-agent runs using proprietary OpenAI and open-weight models, exploring different retrieval strategies, writer models, and agent workflows. Pre-submission ablations identified writer selection and adjacent-chunk expansion as the main factors affecting answer quality. In the official NIST evaluation, six of seven runs exceeded the track median across all three rubric/nugget collections. Our best-performing run, brief-hybrid, achieved the highest all-item coverage among our submissions and tied the track maximum (0.892) for Batch-1 vital coverage. Human side-by-side preferences differed across evaluation batches: the open-weight owa-glm5 led Batch 1 despite lower automated coverage, while sol-research-first led Batch 2. These findings highlight differences between automated coverage measures and human preferences, as well as the potential of lower-cost open-weight models for research-agent systems.

### Lost in Delegation: Studying the Effectiveness of Task Orchestration in Generative Search
- arXiv 2611.16526v1 · v1 2026-11-12 09:25 UTC · cs.AI, cs.CL
- Authors: Tamara Stojanovska, Elisabeth Kirsten, Leon Swazinna, Muhammad Bilal Zafar
- Topics: GEO/AEO · score 10 · found via cs.CL
- Link: https://arxiv.org/abs/2611.16526
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLMs have quickly evolved from models used in isolation to agentic systems that delegate tasks to external tools and other LLMs to solve complex assignments. This agentic augmentation has led to impressive capability gains. However, when and how delegation improves performance remains poorly understood. For example, it is unclear whether delegation helps when tasks involve post-cutoff information that the orchestrating LLM cannot reliably resolve from its own knowledge. In this work, we use purpose-built datasets with pre- and post-cutoff splits to compare various delegation modes. We find that delegation provides no consistent accuracy improvement over non-delegated setups, with effects varying across models and tasks. When tasks involve knowledge unavailable to the orchestrator, delegation can substantially degrade accuracy, while direct tool use with the same LLM performs much better. Our analysis identifies distorted delegated queries, inefficient tool use, and failures to preserve and use information between agents as recurring failure modes. These findings suggest that effective orchestration requires both well-calibrated delegation decisions and effective exchange of information between agents.

### Rational Use of Time for Social Coordination in Humans and AI
- arXiv 2611.14766v1 · v1 2026-11-10 21:44 UTC · cs.AI, cs.CL
- Authors: Xiulin Yang, Sirisha Gudavalli, Jennifer Hu
- Topics: GEO/AEO, Agents · score 9 · found via cs.CL
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

### CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems
- arXiv 2611.14980v1 · v1 2026-11-11 03:38 UTC · cs.CL
- Authors: Yufei Luo, Yuchen Ling, Chunrong Fang
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.14980
- arXiv comment: 23 pages, 4 figures, 15 tables
- Full text: data/fulltext/2611.14980.txt

> Failure attribution in multi-agent systems requires tracing error formation to identify the decisive error step and the responsible agent. However, agents' division of work and information exchange lead to Interleaved Steps and Cluttered Content, requiring models to link executions and check details in lengthy records. This makes it difficult to balance localization accuracy and token cost. We find that multi-agent collaboration also leaves records of how executions connect and content passes between them as results are formed, providing evidence for tracing error formation. Based on this observation, we propose CoLFA (Collaboration-Guided Lightweight Failure Attribution), which uses collaboration cues to organize the attribution input according to how results are formed, determining which steps are examined and how their content is presented. Through Handoff-Guided Step Expansion and Cross-Referenced Content Organization, CoLFA helps the model focus on examining error formation and the role of each decision while reducing the processing of irrelevant and repeated records. Across five settings spanning Who&When and LongRCA and three backbone models, CoLFA achieves the highest exact step-localization accuracy with the lowest token consumption. Compared with individual baselines in each setting, CoLFA improves accuracy by up to 37.50% and reduces token consumption by up to 97.6%.

### ReliaGuard: Reconstruction-Aware Watermarking for Source Attribution and Blind Edit Localization
- arXiv 2611.16368v1 · v1 2026-11-12 06:33 UTC · cs.CV, cs.AI, cs.CR
- Authors: Hailong Wang, Wuzheng Tan, Zixin Zhang, Xujun Fang et al.
- Topics: Citation & source selection · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.16368
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative image editing facilitates content creation but complicates source attribution and edit verification. Existing watermarking methods combine copyright protection with tamper localization, yet background reconstruction can weaken spatial evidence even when source identifiers remain recoverable. We propose ReliaGuard, a reconstruction-aware watermarking framework for source attribution and blind edit localization. The writer optimizes keyed feature responses in both the protected image and its variational autoencoder reconstruction under image-distortion and source-preservation constraints. Using only the received image and a secret key, the reader combines watermark responses with local image context through residual evidence refinement and predicts an edit mask through native-resolution-guided multiscale reading. It is trained on complete editing outputs, locally spliced counterparts, and processed versions of both. On an independent test set of 300 source images and 900 editing cases from three image domains, our method achieves edit-region intersection-over-union scores of 85.61% for complete outputs and 94.90% for locally spliced outputs at a threshold calibrated to a nominal 1% background false-positive rate on complete outputs. The complete-output result exceeds the strongest baseline by 45.02 percentage points, while decoded identifier-bit accuracy reaches 100% in both conditions. Across seven families of image processing, the corresponding localization scores are 81.01% and 86.49%, with identifier-bit accuracies of 92.76% and 92.79%, respectively. These results support source recovery and blind edit localization under background reconstruction and subsequent image processing.

### MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection
- arXiv 2611.16693v1 · v1 2026-11-12 12:08 UTC · cs.CR, cs.AI
- Authors: Yingbin Jin, Ji'an Wang, HaoYang Chai, Hanjun Luo et al.
- Topics: Brand/product recommendation, Agents · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.16693
- arXiv comment: Accepted at NDSS 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Mobile GUI agents read the screen of a phone and operate apps on a user's behalf to complete multi-step tasks such as online shopping or messaging. Because the agent acts on whatever the screen shows, an attacker can embed malicious instructions into ordinary UI content and redirect its actions. We refer to this threat as environmental injection attack (EIA). Existing benchmarks measure this risk by pinning hand-crafted payloads to a fixed step of a fixed task. This approach faces two limitations. First, each payload is bound to one task in one app and does not transfer without manual redesign. Second, agents given the same task may follow different routes, so an agent that never reaches the injected page is recorded as safe without being tested. This insufficient test coverage can cause fixed-point benchmarks to underestimate the security risk of deployed mobile agents. In this work, we propose MobileProbe, a trajectory-aware red-teaming framework that evaluates mobile agents adaptively. MobileProbe discovers attacker-controllable content surfaces through automated pentesting, localizes vulnerable decision points along the agent's trajectory, and iteratively refines context-aware payloads through a surrogate-filtered evolutionary loop. We construct a benchmark of 83 long-horizon attack instances spanning 12 mobile applications. Each is annotated with a Confidentiality, Integrity, or Availability (CIA) attack goal to cover the principal categories of security threats facing mobile agents. On three representative agent architectures, MobileProbe attains higher attack success rates than human-written, zero-shot LLM, and prior automated red-teaming baselines adapted to the mobile domain. MobileProbe can serve as a pre-deployment auditing tool to systematically uncover vulnerabilities and inform security hardening of mobile agents.

### When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents
- arXiv 2611.14864v1 · v1 2026-11-11 00:36 UTC · cs.CR, cs.AI
- Authors: Charles Xiao
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.14864
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> An AI agent's decision not to act can itself become an attack surface. We study warning-induced over-abstention, an availability attack in which adversaries place fabricated risk warnings in low-trust content to prevent legitimate task completion. Our central premise is that safe abstention requires evaluating both the claimed risk and the authority of the evidence supporting it. We develop controlled counterfactual task variants that vary risk content, source provenance, and warning wording, and evaluate a Verify-Before-Abstain protocol that corroborates warnings against authoritative records or the underlying content. Across three model families and 51 injectable AgentAbstain task pairs, caution-first prompting amplifies the attack. For Gemini, induced over-abstention rises from $9.8\%$ to $86.3\%$, despite unchanged clean-task completion. Matched wording comparisons further reveal sensitivity to warning language, with substantial variation across models and environments. Provenance-aware verification improves legitimate completion, while forgery and sensitive-content controls expose its dependence on authoritative evidence and its limitations in preserving confidentiality. These results motivate evaluating agent safety through the justification for restraint, alongside the safety of actions taken.

### Do Large Language Models Show Racial and Sex Bias in Pain Management? A Counterfactual Audit of GPT, Claude, Gemini, Llama, DeepSeek and Qwen
- arXiv 2611.14935v1 · v1 2026-11-11 02:35 UTC · cs.AI, cs.CL, cs.CY
- Authors: Richard J. Young, Alice M. Matthews
- Topics: Clicks & measurement · score 6 · found via cs.CL, cs.CY
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

### Temporal Context-Aware Spam Detection Using Transformer-Based NLP Models
- arXiv 2611.16139v1 · v1 2026-11-12 01:04 UTC · cs.CL, cs.LG
- Authors: Fariz Zeynalov, Razim Mammadli
- Topics: Manipulation · score 6 · found via cs.CL
- Link: https://arxiv.org/abs/2611.16139
- arXiv comment: 7 pages, 2 figures, 5 tables
- Full text: data/fulltext/2611.16139.txt

> Spam detection is usually treated as single-message classification, ignoring behavioral patterns that emerge across sequences of messages from the same sender. We study outbound SMS spam detection at the carrier level, where the goal is to predict at send time whether a carrier will flag a message as spam. Using a proprietary production database of 43,741 outbound SMS messages with UTC transmission timestamps and carrier delivery statuses, we report three sets of results. On an 8,749-message held-out test set, a TF-IDF + logistic regression baseline reaches AUC-ROC 0.8721, and a text-only DeBERTa-v3-base classifier reaches AUC-ROC 0.9011 and F1 0.8412. A deployed DistilBERT model augmented with inter-message temporal features reaches accuracy 0.8238, spam-class F1 0.8382, and recall 0.9128 at threshold 0.5 on a separate, class-balanced 20,000-message production evaluation set; these results are not directly comparable with the held-out test results. We also describe TemporalBertSpam, an architecture that encodes each sender's message history with a causal Transformer, and outline the same-split evaluation needed to measure its contribution.

### A Code-Level Audit of X
- arXiv 2611.16800v1 · v1 2026-11-12 13:42 UTC · cs.CY, cs.SE
- Authors: Luka Bekavac, Simon Mayer
- Topics: Clicks & measurement · score 6 · found via cs.CY
- Link: https://arxiv.org/abs/2611.16800
- arXiv comment: Submitted. Currently under peer-review
- Full text: data/fulltext/2611.16800.txt

> The transparency regime of recommender systems on Very Large Online Platforms (VLOPs) is undergoing significant change under the EU Digital Services Act (DSA). The DSA requires platforms to disclose information about their recommendation pipelines and grants vetted researchers access to non-public data, which may extend to recommender code. However, it is not known to what extent such code releases enable substantive and meaningful third-party auditing of a production recommender system. We address this question by proposing a code-level audit methodology for recommender systems and applying it to the X platform, which has voluntarily open-sourced its recommender pipeline. Our methodology is a backwards-walk traversal of the repository, tracing each decision-relevant component from the user-facing timeline back to its upstream producers, checking that it is reachable from the served pipeline, and classifying each under a four-tier inspectability scheme. Applying this procedure, we identify 13 transparency dead-ends on the live serving path: models, services, label lists, and configuration values that the public code depends on but the release does not contain. We find that the components that decide which posts are filtered and how they are ranked fall into the two least inspectable tiers, a pattern that intensifies with the 2025 integration of the proprietary Grok language model into moderation, annotation, and ranking. We further show that the release keeps 2023 code that the 2025 pipeline no longer reaches, with 36 parameter references that would pass for dead-ends without a reachability check. Finally, we discuss which additional artifacts would be required for meaningful auditing.

## Other new cs.IR papers, title only (0)

## Already listed on an earlier day, still inside the look-back window (19)
- Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models — https://arxiv.org/abs/2611.12521 (score 14)
- TS-GEAR: Taobao Shangou GEnerative Ad Retrieval — https://arxiv.org/abs/2611.12180 (score 13)
- CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising? — https://arxiv.org/abs/2611.11955 (score 12)
- ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation — https://arxiv.org/abs/2611.11897 (score 11)
- Harness Matters: Measuring and Dissecting Security Resilience in Web Agents — https://arxiv.org/abs/2611.11971 (score 11)
- StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills — https://arxiv.org/abs/2611.12155 (score 10)
- Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation — https://arxiv.org/abs/2611.11305 (score 9)
- Can AI be a 'Researcher Without Borders'? Auditing Bias in AI-Assisted Social Science Research about China and the US — https://arxiv.org/abs/2611.14288 (score 9)
- CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines — https://arxiv.org/abs/2611.05862 (score 8)
- ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping — https://arxiv.org/abs/2611.11306 (score 8)
- SkillCODER: Towards Auditing and Attribution of Copyright Infringement in LLM Agent Skills — https://arxiv.org/abs/2611.11308 (score 8)
- Agentic Attribution of Cloud Resource Ownership — https://arxiv.org/abs/2611.11340 (score 8)
- An Interpretable Stylometric Framework for Early Chinese Buddhist Translator Styles: A Case Study on the Attribution of Disputed Works of An Shigao — https://arxiv.org/abs/2611.13636 (score 8)
- On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents — https://arxiv.org/abs/2611.11506 (score 6)
- Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models — https://arxiv.org/abs/2611.11571 (score 6)
- Continuous modeling of manipulative participation for stance analysis: Online discourse on the 2024 Street Animal Law in Türkiye — https://arxiv.org/abs/2611.11576 (score 6)
- Scaling Adaptive Prompt Injection Attacks with Agent Swarms — https://arxiv.org/abs/2611.11861 (score 6)
- SadaqahStories: A Verified English-Arabic Corpus of Charity Stories for Children, with an Audit of Errors in AI-Drafted Religious Narratives — https://arxiv.org/abs/2611.12078 (score 6)
- What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them — https://arxiv.org/abs/2611.14068 (score 6)
