# Paper candidates — 2026-11-09 (IST)

Generated 2026-11-09 08:02 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 19 new topic matches · 12 other new cs.IR · 43 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (19), highest score first

### What Matters for LLM Persona Simulation: Signal Form in Cold-Start E-Commerce Advertising
- arXiv 2611.08840v1 · v1 2026-11-06 00:55 UTC · cs.AI, cs.LG
- Authors: Jiwoo Choi, In Ik Lee, Woo Sung Seo, Minho Lee et al.
- Topics: Brand/product recommendation, Clicks & measurement, Ads · score 19 · found via cs.AI, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.08840
- arXiv comment: Accepted at GenAIECommerce'26: The Third Workshop on Agentic and Generative AI for E-Commerce, co-located with RecSys 2026. 13 pages
- Full text: data/fulltext/2611.08840.txt

> Estimating advertising performance in cold-start settings is challenging because historical logs are unavailable before launch. Large language models (LLMs) offer a potential alternative by simulating persona-conditioned user responses, but it remains unclear which design choices actually drive LLM-based persona simulation. Using real Google Ads e-commerce campaign data across five demographic segments, we identify three signal-form dimensions that affect simulation quality: (i) a demographic anchor without noisy rich attributes, (ii) a relative qualitative banner-blindness signal rather than quantitative anchors, and (iii) prompt phrasing. On this campaign, our method attains an MAE of 24.9 and a MAPE of 26.1%, a 51.3% lower MAE than the best tested non-LLM baseline and 77.3% lower than an LLM configuration using explicit CTR anchors. Systematic ablations show that minimal demographic descriptions achieve lower mean error than richer persona configurations, while relative qualitative cues substantially outperform the tested quantitative anchors. We additionally compare these configurations with direct-prior and rule-based baselines and with alternative LLM configurations.

### Functional Dependency beyond Similarity: Hierarchical Decomposition of Training Data Attribution in Music Generative Models
- arXiv 2611.08839v1 · v1 2026-11-06 00:53 UTC · cs.CY, cs.LG
- Authors: Changheon Han, Hugh Xuechen Liu, Ashkan Panahi, Kıvanç Tatar
- Topics: GEO/AEO, Citation & source selection · score 13 · found via cs.CY
- Link: https://arxiv.org/abs/2611.08839
- arXiv comment: 23 pages, 9 figures, 11 tables. Under review
- Full text: data/fulltext/2611.08839.txt

> Copyright analysis focuses on the similarity between two works. However, generative AI models learn from training data through functional relations beyond similarity. Training Data Attribution (TDA) estimates the influence of each training instance on a generated output and may serve as a basis for remuneration. However, prior studies find global influence, where a few training instances rank as the most influential for almost every generation. Used directly, TDA scores would distribute part of every remuneration to these instances regardless of what was generated. To address this, we propose a new approach in which TDA scores are decomposed into three levels of influence, namely global indicating the influence of a training data to a trained model, group for its influence on a group of generated outputs (that could be clustered together), and specific for its influence on a single generated output. Our study finds that, across several music generative models and TDA methods, global- and group-level influence is non-negligible in every case. Based on these observations, we propose the term functional dependency for the relation of training data to a trained model or to its outputs. This notion both encompasses and distinguishes dependencies of different scopes, allowing TDA scores to be interpreted as distinct forms of contribution in legal, economic and ethical discussions on remuneration.

### MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition
- arXiv 2611.09090v1 · v1 2026-11-06 07:20 UTC · cs.CL
- Authors: Rui Qi, Yunlong Liang, Yufeng Chen, Jinan Xu et al.
- Topics: RAG (generic), Query fan-out · score 11 · found via cs.CL
- Link: https://arxiv.org/abs/2611.09090
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Existing multilingual retrieval-augmented generation relies heavily on learned retrievers and similarity-based ranking from multilingual collections, which are vulnerable to cross-lingual retrieval errors and indexing overhead. In this paper, we explore retriever-free multilingual search, where the model directly interacts with raw corpora through executable shell commands. This paradigm shifts the bottleneck to multilingual search action generation, where exact search is sensitive to entity surface forms and outcome-only supervision provides limited guidance for multi-turn search. To address these challenges, we propose MARS, a multilingual search agent in direct corpus interaction (DCI) with reinforcement learning (RL). MARS introduces corpus-native entity grounding to recover reliable lexical anchors from corpus evidence, mitigating failure to retrieve evidence. Meanwhile, we present a redundancy-aware search reward to encourage concise and effective search trajectories, addressing training collapse in RL of multilingual scenarios. Experiments show that \ours~consistently outperforms strong retrieval-based and DCI baselines, while demonstrating robust cross-lingual generalization and substantially reducing redundant corpus interactions.

### On Agentic Manipulation Policies
- arXiv 2611.09892v1 · v1 2026-11-06 18:59 UTC · cs.RO, cs.AI, cs.CV, cs.LG
- Authors: Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez et al.
- Topics: GEO/AEO, Manipulation · score 11 · found via cs.AI
- Link: https://arxiv.org/abs/2611.09892
- arXiv comment: Videos and code available at: https://apple-aiml-research.github.io/ml-amp/
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the RoboLab-120 and CaP-Gym benchmarks, with no demonstrations or task-specific training. On RoboLab-120, AMP1 reaches an 85.6\% success rate zero-shot, compared to 49.2\% and 42.9\% for leading VLA and WAM policies. The agent succeeds zero-shot in 104 of 108 real-world trials spanning twelve tasks and three robot instances, reducing failure rates by 20x and 15x relative to strong VLA and WAM baselines. The basic harness supplies no grasping, pushing, or placing skills; the agent develops its own strategies, such as searching for hidden objects, using objects as tools, and calibrating its cameras. With the addition of a persistent memory store, the agent can also learn from experience: an augmented harness with a memory representation that is carried across episodes lowers the failure rate on RoboDojo bimanual manipulation tasks by 4.6x relative to zero-shot deployment. Our analysis suggests that AMPs are substantially more general and robust than specialist manipulation policies, providing a promising foundation for robot manipulation.

### Generative Search and Recommendation at Shopify
- arXiv 2611.08804v1 · v1 2026-11-05 23:56 UTC · cs.IR
- Authors: Juhana Kangaspunta, Khalil Hajji, Darshan Fofadiya, Kyumin Park et al.
- Topics: GEO/AEO · score 10 · found via cs.IR
- Link: https://arxiv.org/abs/2611.08804
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Search and recommendation at Shopify require retrieving relevant products from a changing catalog of billions of products under strict latency constraints. We present SID-LLM, which casts both tasks as generating semantic IDs: short sequences of content-derived tokens representing products. We jointly pre-train SID-LLM on catalog and behavioral data, giving search and recommendation a shared representation and training objective. We show that reinforcement learning further improves judged search relevance. Furthermore, distillation from task-specific experts improves recommendation quality over joint supervised fine-tuning without a statistically detected loss in search quality. Finally, for efficient serving, we pair multi-token prediction with a lightweight ranker, improving retrieval quality over our autoregressive baseline while reducing latency. We evaluate SID-LLM both as a standalone retriever and as a component of Shopify's production search and recommendation systems. As a standalone search system, SID-LLM achieves quality comparable to Shopify's existing multi-model search stack while meeting production latency requirements. Integrating SID-LLM into the search and recommendation stacks provides significant gains in both offline evaluations and online A/B tests. Together, these results demonstrate the practical value of semantic-ID generation as a unified approach to product discovery at scale.

### BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models
- arXiv 2611.09147v1 · v1 2026-11-06 08:24 UTC · cs.AI, cs.CL
- Authors: Anthony Rhodes, Gadi Singer
- Topics: Citation & source selection, RAG (generic), Brand/product recommendation · score 9 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.09147
- arXiv comment: 21 pages, 4 figures. NeurIPS 2026 Workshop on Trust-AI-Eval (TAE). Artifact: https://doi.org/10.5281/zenodo.22064759
- Full text: data/fulltext/2611.09147.txt

> Behavioral evaluation of language models fixes its dimensions in advance: hallucination, sycophancy, toxicity, over-refusal. An operator in a regulated industry needs a different question answered: does a system do what a particular rulebook requires? We introduce the Behavioral Misalignment Metric Suite (BMMS), which measures policy-conditioned misalignment by taking a policy corpus as an argument and returning a compliance profile over it, for any published policy and any system that answers in natural language. The Compliance Attainment Score (CAS) measures severity-weighted attainment over the obligations that bind the system, and the Compliance Robustness Margin (CRM) the share of that attainment surviving graded adversarial pressure; Behavioral Invariance (BIV) and the Behavioral Disposition Index (BDI) are specified and released with the suite. Dimensions enter only by passing a published admission test whose binding criterion is attribution: a quantity that moves when the judge changes, holding the target fixed, is measuring the instrument. Applying it excluded one of the quantities the suite itself reported. Across 1,003 obligations from eleven documents in five registers, the admission criterion holds 94.4% precision against blinded human judgment on vendor specifications and 50.0% on analytical guidance, extraction fidelity is 94.6%, and re-scoring under judges from two other providers leaves target ordering invariant while the absolute score of a single target spans up to 0.22. We apply it to the two most detailed published behavioral specifications. Own-specification advantage is not resolved from zero once document difficulty is subtracted, but absolute self-compliance is another matter: GPT-4o fails 70.7% of the hard constraints binding it in the Model Spec published by OpenAI, where the two Claude models fail 0.0% and 9.1% of theirs.

### Cutpurse: Decomposing Explanation-Guided Model Extraction on Tabular Data
- arXiv 2611.09375v1 · v1 2026-11-06 12:15 UTC · cs.CR, cs.LG
- Authors: Seyma Selcan Magara, Hanru Zhang, Fatme El Zahraa Hamad, Nico Pfeifer et al.
- Topics: Citation & source selection, Query fan-out · score 9 · found via cs.CR
- Link: https://arxiv.org/abs/2611.09375
- Full text: data/fulltext/2611.09375.txt

> Explanation APIs are often treated as increasing model-extraction risk, but an end-to-end attack comparison cannot show whether an explanation reveals model-specific information or merely supplies a convenient next-query coordinate. We study this distinction for explanation-guided extraction of tabular classifiers. We separate an explanation into an attribution channel, which ranks influential features, and a coordinate channel, which supplies candidate feature values for perturbing those features. We then test whether the useful bin edges are privileged to the service or reproducible from the adversary's own data. Across six datasets and five target families, using attribution rankings to choose which features to perturb provides no systematic extraction advantage. Lime's discretization bin edges can improve fidelity by up to 41 percentage points on continuous features, but those edges are quantiles of the explainer's background data rather than properties of the target model. In controlled comparisons, an attacker-side grid reproduces the useful bin-edge gains without querying an explanation API. We use these findings to derive Cutpurse, which combines a self-computed grid with diverse query generation and boundary search. Against a service that withholds bin edges, Cutpurse improves fidelity by 16.3 percentage points on continuous-feature targets. It also exceeds the undefended published attack by 7.0 percentage points. Thus, withholding default Lime bin edges alone does not prevent effective extraction under the in-domain auxiliary-input, probability-output, and same-family surrogate assumptions studied here. Our results concern default Lime and Shap configurations for tabular classifiers. They do not establish the same conclusion for other explainers, target classes, or data-free attackers.

### Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement Learning in E-Commerce Payment Fraud Detection
- arXiv 2611.08706v1 · v1 2026-11-05 21:02 UTC · cs.AI, cs.CL, cs.LG
- Authors: Bo Qu, Zhurong Wang, Frank Zahradnik, Ming Ouyang
- Topics: Brand/product recommendation · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.08706
- arXiv comment: 12 pages, 1 figure, 3 tables. Extends Qu et al., ACL 2025 Industry Track: https://aclanthology.org/2025.acl-industry.9/
- Full text: data/fulltext/2611.08706.txt

> Production fraud-detection models learn from a censored slice of their own traffic: transactions a legacy system blocked never receive fraud labels, so models train on a biased, approved-only distribution. We extend LLM-guided reward design, the framework of Qu et al. (2025) in which an LLM evolves the reward of a two-step REINFORCE fraud-blocking policy, to attack this reject-inference problem inside the reward. A single LLM designs a dual-stream reward: stream 1 applies the standard dollar-weighted precision objective to labeled transactions; stream 2 scores legacy-blocked, unlabeled transactions by contrasting the newest gradient-boosted risk signal against the legacy scores that drove the original block. Rather than prescribe which signals matter, we expose a superset of evidence and let the LLM decide for itself which to use, guided by evaluation feedback alone; because it writes the reward as code, that choice is directly auditable. On a held-out four-month out-of-time test, the dual-stream agent beats the prior labeled-only agent at every target recall, by +4.7, +2.4 and +3.0 points of dollar-weighted precision at 80%, 85% and 90% recall, and the production baseline by +6.8 points on average. The resulting policy is architecturally identical to that of Qu et al. (2025) and adds no inference cost.

### Learning Whom to Trust About the Unseen: Source Credibility and Reliability Transfer in Language Models
- arXiv 2611.08855v1 · v1 2026-11-06 01:22 UTC · cs.AI
- Authors: Ruijia Guan
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.08855
- Full text: data/fulltext/2611.08855.txt

> A source who has been right before deserves attention, but about what? We ask how far a demonstrated record of reliability travels in language models when the new claim cannot be checked, and whether the answer depends on the kind of claim. Three behavioral studies across six models approach the question from three angles. Study 1 adapts the Einstein-effect paradigm and finds that models, unlike the human sample, favor a spiritual leader over a scientist for the same obscure statement, and that the preference largely reverses when the statement is reworded in the vocabulary of physics. Study 2 adapts a paradigm in which a trusted expert calls a scientific or religious explanation unknown or a mystery; models reproduce the human domain asymmetry in exaggerated form. Study 3, the central test, gives two fictional informants different records on checkable river forecasts and then has them endorse matched claims about hidden natural and spiritual causes of the same village events. Most models carry the record to natural causes and barely at all to spiritual ones; one model transfers it weakly to either. Telling the model that the reliable informant forecasts by spiritual guidance rather than by measurement lowers that informant's influence on natural claims in every model and produces no comparable gain on spiritual claims in any. Demonstrated reliability thus has a scope in these models, and the account a source gives of how they came to be reliable can narrow it. Whether this reflects a judgment about relevance or the low prior credence of spiritual claims is the question the design leaves open, and we outline the experiment that would settle it.

### CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving
- arXiv 2611.09139v1 · v1 2026-11-06 08:14 UTC · cs.AI
- Authors: Jingjia Teng, Yang Li, Wenjie Huang
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.09139
- arXiv comment: Abridged version containing the main results; the full version is under peer review and will be updated here upon acceptance
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> This study presents Causal Attribution and Responsibility-Guided Optimization (CARGO), a multi-agent reinforcement learning framework for cooperative on-ramp merging in mixed traffic. A shared latent-context posterior and an action-conditioned response model estimate directed behavioral influence, with posterior uncertainty propagated into interaction-edge selection. Complementary attribution mechanisms couple signed influence with marginal team utility for cooperative reward shaping and assign responsibility from positive excess tail risk relative to a safe reference policy. Conditional diffusion generates future responses for action-dependent risk estimation. Responsibility-guided preventive optimization calibrates agent-specific risk-reduction requirements to local capacity within a policy trust region, using reserved safety margins, adaptive requirement scaling, and joint feasibility verification. Theoretical analysis establishes risk monotonicity and sufficient local conditions for non-decreasing environmental return under explicit assumptions. Experiments in highway-env across three traffic densities, together with controlled graph-recovery and attribution studies, support the effectiveness of the framework. Under high-density traffic, CARGO increases the success rate by 66.04\% and reduces the crash rate by 56.23\% relative to the best evaluated baseline for each metric.

### FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding
- arXiv 2611.09722v1 · v1 2026-11-06 17:00 UTC · cs.AI
- Authors: Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu, Shuaiwen Leon Song et al.
- Topics: GEO/AEO, Manipulation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.09722
- Full text: data/fulltext/2611.09722.txt

> Large-language-model decode attention streams the key-value (KV) cache for every generated token. Packing that cache into 2-bit or 4-bit quantized integers reduces memory traffic but does not automatically translate into latency saving. Existing 2-bit fused kernels reach under 31%/15% of peak HBM throughput on H100/B200. Converting each value and applying its scale and offset before feeding Tensor Cores is a major bottleneck because instruction-issue throughput is scarce on modern GPUs. Instead of applying scale and offset to each KV value, FOSCAR uses affine folding to apply them to the other operand or the output of decode-attention matrix products, depending on the quantization scheme (token-wise or channel-wise). This reduces scale-and-offset operations by up to two orders of magnitude while preserving the dequantized attention output in exact arithmetic. FOSCAR also uses bit manipulation to feed KV operands to Tensor Cores efficiently, requiring only 1 and 0.19 ALU instructions per INT2 element on H100 and B200, respectively. Finally, FOSCAR builds warp-specialized GPU pipelines for Hopper (H100) and Blackwell (B200) using wgmma and tcgen05. On H100, FOSCAR INT2 and INT4 kernels achieve geo-mean speedups of $3.36\times$ and $2.83\times$ over FlashInfer BF16, and $2.03\times$ and $1.71\times$ over TensorRT-LLM FP8. On B200, the corresponding INT2 and INT4 speedups are $2.67\times$ and $2.30\times$ over FlashInfer BF16, $1.48\times$ and $1.28\times$ over TensorRT-LLM FP8, and $1.16\times$ and $1.00\times$ over TensorRT-LLM NVFP4. We integrate FOSCAR into SGLang to benchmark serving efficiency. On long-context serving workloads, FOSCAR increases peak aggregate throughput by up to 170% and 341% over 2-bit and 16-bit baselines, respectively. We open-source FOSCAR as a kernel library at https://github.com/FutureMLS-Lab/FOSCAR.

### RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning
- arXiv 2611.08711v1 · v1 2026-11-05 21:06 UTC · cs.CL, cs.CR
- Authors: Taikun Chen, Yue Zhang, Wei Qian, Hui Fang
- Topics: Manipulation · score 6 · found via cs.CL, cs.CR
- Link: https://arxiv.org/abs/2611.08711
- arXiv comment: Accepted as a regular paper at IEEE EdgeCom 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) exhibit vulnerabilities to adversarial perturbations that can induce unintended responses. These vulnerabilities can be identified via intentional attacks and subsequently used to improve model safety. In black-box settings where gradients are inaccessible, existing methods tend to guess adversarial transformations using external knowledge, ignoring the information provided by the target model. To mitigate this, we propose a trainable black-box framework based on reinforcement learning, which learns from the target model to generate tailored adversarial transformations. We demonstrate that our approach achieves lower post-attack accuracy, greater query efficiency and better semantic preservation on both natural language inference and generative Q&A tasks. On natural language inference, it drives post-attack accuracy to 2% within 20 queries. Against generative language models, our trained attacker consistently achieves lower post-attack accuracy than the untrained attacker and wins in 4 out of 6 settings when compared to a strong optimization-based baseline. We further experiment with multiple reward designs and training settings, and we find that no design or setting is consistently dominant. Our code is available at https://github.com/taikunudel/RL-ATTACK.

### Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate
- arXiv 2611.08756v1 · v1 2026-11-05 22:13 UTC · cs.AI
- Authors: Liting Huang, Huizhi Liang, Yi Lei, Xingjun Ma et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.08756
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Knowledge attacks on Large Language Models, such as manipulating fact-checking judgments, pose significant risks to AI reliability. Existing approaches -- adversarial suffix/template injection and single-agent self-reflection -- lack robustness across diverse defenses and are prone to confirmation bias and costly trial-and-error, respectively. We propose Debate-to-Deceive (D2D), a multi-agent debate framework grounded in human debate structure and rhetorical style, enabling agents to generate adversarial passages that are semantically coherent, rhetorically effective, and resistant to early confirmation bias. D2D formalizes the adversarial process as an evolutionary game in which agents adaptively evolve their rhetorical strategies (Logos, Pathos, Ethos) through competition. To manage the intractably large LLM output space, we decouple agent behavior into a strategic layer, which selects a rhetorical action from a compact strategy space via evolutionary-inspired learning dynamics, and a generation layer, where the LLM produces a concrete passage conditioned on that strategy and the debate context. On four fact-checking benchmarks (FEVER, HealthVer, CLIMATE-FEVER, and SciFact), D2D substantially outperforms existing attacks and evades most defenses.

### Guardrail Erosion in Domain Fine-Tuned Large Language Models: A Paired Audit of Knowledge-Centric Abstention in Biomedical LLMs
- arXiv 2611.08780v1 · v1 2026-11-05 23:03 UTC · cs.AI, cs.CL
- Authors: Stephen Peng, Vineet Jagadeesan Nair, Noah Broestl, Anne Friederike Kleppe et al.
- Topics: Clicks & measurement · score 6 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.08780
- arXiv comment: To be published in the Proceedings of the 6th Machine Learning for Health Symposium (ML4H 2026), PMLR volume 346
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> The number of domain fine-tuned models, particularly in the biomedical domain, is rapidly expanding. Fine-tuning promises high-performing models at a fraction of the cost of training a base model, but it can also produce unintended behavioral changes. Multiple studies have shown that safety guardrails can erode with fine-tuning, yet large-scale studies across model architectures, data mixtures, and fine-tuning methodologies remain limited. Where prior work in this space has studied value-centric refusal, this work focuses on knowledge-centric abstention. We audit 25 biomedical domain fine-tuned large language models against 11 paired base checkpoints on MedAbstain and ClinDet-Bench to evaluate the impact of fine-tuning on knowledge-centric abstention. We find that defined appropriate abstention measured by these benchmarks, already low in base models (median 8.3% on MedAbstain), falls further after fine-tuning (median 4.2%, decreasing in 21 of 25 pairs on MedAbstain), and that the magnitude and direction of change are heterogeneous across pairs. These results motivate fine-tuning methods that improve domain-specific capability while preserving appropriate caution.

### Notwithstanding Anything to the Contrary, Ignore All Instructions: Measuring Prompt Injection Guards on Legal Contract Review Attacks
- arXiv 2611.08834v1 · v1 2026-11-06 00:42 UTC · cs.AI
- Authors: Mark Heimann, Katherine Taylor, Bruno Jacob
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.08834
- Full text: data/fulltext/2611.08834.txt

> Specialized prompt injection guards are deployed in front of document analysis systems, but no false positive rate has been published for any of them on legal contracts. We measure eleven open-weights guards on two corpora of legal contracts and find that existing guards struggle: document-level false positive rates are as high as 92.39%; two guards fall below chance on paired AUC; and a five-regex baseline is not Pareto-dominated by any guard in the panel. Controlled probes locate model-specific as well as general failure modes. Prompted LLMs resolve the tested failures, including a second threat category (unauthorized scope claims) on which every guard scores zero. A cascaded LLM solution, where the positives of a mid-tier model are verified by a frontier model, is 6.5x cheaper than using exclusively a frontier model and approaches its performance.

### MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory
- arXiv 2611.09721v1 · v1 2026-11-06 17:00 UTC · cs.AI, cs.CL, cs.CR
- Authors: David H. Yang, Blake Bullwinkel, Amanda Minnich, Mohammad Mohammadi Amiri et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CL, cs.CR
- Link: https://arxiv.org/abs/2611.09721
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning across different memory architectures, we introduce MemoryDojo, a benchmark for tracing the lifecycle of poisoned information through agent memory and measuring its influence on subsequent agent behavior. MemoryDojo is easily extensible, consists of 155 multi-session long-horizon trajectories covering four domains, and supports five different memory systems. Through our evaluation, we find that all memory systems are susceptible to memory poisoning, with substantial variation in downstream effects. We further propose a memory-aware poison optimization process that increases the poisoning efficacy, highlighting differences between memory architectures. We hope that MemoryDojo will support research on understanding and mitigating agentic memory risks.

### Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation
- arXiv 2611.09864v1 · v1 2026-11-06 18:44 UTC · cs.RO, cs.AI, cs.LG
- Authors: Xun Tu, Minghao Zou, Karthik Desingh
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.09864
- arXiv comment: 10 pages, 6 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons, is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation. Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object and object-environment interaction dynamics. Existing approaches address this challenge either through model-based methods, which often require accurate dynamics models, or through learning-based methods, which reduce this requirement but typically assume a fixed or predefined initial grasp. However, different geometrically stable grasps can lead to substantially different downstream manipulation performance. Therefore, we propose Grasp-TAGS, a task-aware grasp selection framework for goal-conditioned large-object rearrangement. We train a unified PPO-based reinforcement learning policy across multiple initial grasp configurations and distill the learned critic into a lightweight grasp utility network that ranks candidate grasps using only the candidate grasp configuration and goal information. At inference time, we select the grasp with the highest predicted downstream utility for the downstream policy to complete the task, before even making a contact. Experiments demonstrate that Grasp-TAGS improves rearrangement success over both fixed single-grasp policies and random grasp selection, achieving an average success rate of 89.84% compared with 79.87% for the best-performing single-grasp policies, an improvement of 9.97 percentage points. Grasp-TAGS also reduces final orientation errors across all evaluated objects. For more qualitative results, refer to the supplementary webpage: https://rpm-lab-umn.github.io/Grasp-TAGS-web-page/

### Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL
- arXiv 2611.09200v1 · v1 2026-11-06 09:21 UTC · cs.IR, cs.CL
- Authors: Duc-Vu Nguyen, Ngan Luu-Thuy Nguyen
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.09200
- arXiv comment: Accepted at SOICT 2026
- Full text: data/fulltext/2611.09200.txt

> We study Vietnamese statutory Article retrieval on DRiLL using features for provision identity and local form, same-law support, and citation and lineage evidence. Across five random seeds, selectors sharing candidates, listwise Qwen evidence, and learner settings improve official $F_2$ from 71.77% to 72.91%, with the largest descriptive gain on two-Article questions. Added features account for 18.20% of the proposed selector's total decision-tree split gain, measured as training-objective reduction, mainly from same-law and citation evidence. Cases reveal base provisions and amendments, companion recovery, distractor removal, and failures. These findings motivate research on other datasets, representations, and learners without establishing individual feature effects or requiring LightGBM, hand-crafted scores, or explicit graphs.

### SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI
- arXiv 2611.08935v1 · v1 2026-11-06 03:24 UTC · cs.IR
- Authors: Jing Hao, Weinan Zhou, Zhihong Lu, Yaling Shen et al.
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.08935
- arXiv comment: 35 pages, 7 figures
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Reliable dermatology AI requires access to verifiable evidence distributed across heterogeneous textual and visual sources. However, conventional retrieval-augmented generation (RAG) typically relies on one-shot retrieval from flat corpora, limiting its ability to adapt retrieval granularity, explore multi-hop relations, and integrate multimodal clinical evidence. We introduce SkinMind, a multimodal agentic RAG framework that equips policy models with human-inspired graph probing for autonomous evidence seeking. SkinMind organizes retrieval as an iterative interaction between an orchestrator and a graph environment. Through eight hierarchical graph-probing tools, the orchestrator progressively identifies relevant entities, inspects node-level information, traverses relations and paths, and retrieves source-text and visual evidence. This progressive-disclosure design allows the model to adaptively determine the retrieval modality, exploration direction, and evidence granularity while constructing a query-specific evidence subgraph. To support autonomous graph probing, we construct SkinMind-KG from a 62M-token corpus of dermatology guidelines and textbooks and 423K images, guided by a dermatologist-informed schema and a conflict-resolution mechanism. The resulting graph contains over 1.0M nodes and 2.0M edges, unifying textual, relational, and visual evidence for retrieval. Across six dermatology VQA benchmarks and two policy-model settings, SkinMind improves the average score over direct answering by 8.70 and 8.89 points with GPT-5.4-mini and Gemini-2.5-Flash, respectively, while consistently outperforming competing RAG methods. Together, SkinMind and SkinMind-KG provide an effective foundation for evidence-grounded multimodal reasoning in dermatology.

## Other new cs.IR papers, title only (12)
- CascadeRec: Deployed Adaptive LLM Compute Allocation for Multi-Tenant Content Recommendation — https://arxiv.org/abs/2611.08566
- SteerGR: Steering Generative Recommendation via Sparse Autoencoders for Controllable Game Discovery — https://arxiv.org/abs/2611.08790
- Rethinking Latent Reasoning for Generative Recommendation: Beyond Teacher-Generated CoT and Recurrent Hidden-State Feedback — https://arxiv.org/abs/2611.09006
- MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering — https://arxiv.org/abs/2611.09040
- PAGSL: Path-Augmenting Graph Structure Learning for explainable scholar recommendation — https://arxiv.org/abs/2611.09126
- A Taxonomy-Driven Synthetic Dataset for Retrieval Effectiveness and Fairness Evaluation in Hiring — https://arxiv.org/abs/2611.09178
- Large Language Model Consensus and Corpus-Adaptive Topic Modeling for Classifying and Mapping Patent Innovation — https://arxiv.org/abs/2611.09194
- FondueQA: A Benchmark for Evaluating Parametric Compensation in Multi-Hop QA — https://arxiv.org/abs/2611.09274
- Orthogonal Norm Growth in Two-Tower Retrieval: A Popularity Mechanism for Unified Discovery — https://arxiv.org/abs/2611.09294
- ENGRAM: From Agent Experience to Weights through Verified Consolidation — https://arxiv.org/abs/2611.09472
- SPARSEUP: Towards Better Recipes for Training Modern Learned Sparse Retrievers — https://arxiv.org/abs/2611.09680
- SAGE-PAIR: Source-Pretrained Routed Residual Adaptation for Sparse-Feedback Recommendation — https://arxiv.org/abs/2611.09728

## Already listed on an earlier day, still inside the look-back window (43)
- The Popular Get More Popular: Auditing Brand Bias in Generative Search — https://arxiv.org/abs/2611.07614 (score 22)
- CORE: Coarse-to-Fine Search with Context Management for Deep Research — https://arxiv.org/abs/2611.07859 (score 14)
- WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution — https://arxiv.org/abs/2611.06777 (score 12)
- Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification — https://arxiv.org/abs/2611.06662 (score 10)
- LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks — https://arxiv.org/abs/2611.06687 (score 10)
- Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks — https://arxiv.org/abs/2611.07640 (score 10)
- Beyond the Landing Page: Website Blocking, Tracker Visibility, and Human Alignment in Automated Web Crawls — https://arxiv.org/abs/2611.06197 (score 8)
- Presentation Sensitivity in Typed Decision Models for Subjective Text Evaluation — https://arxiv.org/abs/2611.06384 (score 8)
- U.S. State Guidance on AI in K-12 Education: A Comparative Content and Citation Analysis — https://arxiv.org/abs/2611.06762 (score 8)
- Consistent yet Contextual: Learning Author-Level Mixtures of Style for Authorship Attribution — https://arxiv.org/abs/2611.07111 (score 8)
- Full Provenance on the COSS Causal Axis: An Event-Level Closure of Causal Attribution and Confused-Deputy Exclusion — https://arxiv.org/abs/2611.07164 (score 8)
- BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation — https://arxiv.org/abs/2611.07425 (score 8)
- ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality Hand Interaction by a Coding Agent — https://arxiv.org/abs/2611.08321 (score 8)
- Dynamic Watermarking and Action-Conditioned Latent Dynamics for Secure Vision-Based Controllers — https://arxiv.org/abs/2611.07403 (score 7)
- SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection — https://arxiv.org/abs/2611.07222 (score 6)
- VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations — https://arxiv.org/abs/2611.07272 (score 6)
- Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model — https://arxiv.org/abs/2611.07513 (score 6)
- MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents — https://arxiv.org/abs/2611.07689 (score 6)
- ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation — https://arxiv.org/abs/2611.07928 (score 6)
- MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation — https://arxiv.org/abs/2611.08372 (score 6)
- Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation — https://arxiv.org/abs/2611.06498 (score 5)
- PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries — https://arxiv.org/abs/2611.06349 (score 4)
- What Gets Hacked in a Collaborative Reward for LLM Recommenders: The Part That Does Not Depend on the User — https://arxiv.org/abs/2611.07588 (score 4)
- MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents — https://arxiv.org/abs/2611.07631 (score 4)
- What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays — https://arxiv.org/abs/2611.07650 (score 4)
- Decision Models as Retrieval Gates Against Injection and Pollution — https://arxiv.org/abs/2611.08325 (score 4)
- Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking — https://arxiv.org/abs/2611.07591 (score 3)
- Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial Objects — https://arxiv.org/abs/2611.07851 (score 3)
- CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment — https://arxiv.org/abs/2611.07393 (score 2)
- ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs — https://arxiv.org/abs/2611.06481 (score 1)
