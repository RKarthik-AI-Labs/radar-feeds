# Paper candidates — 2026-11-23 (IST)

Generated 2026-11-23 08:06 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 14 new topic matches · 6 other new cs.IR · 48 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (14), highest score first

### When Do LLM-Elicited Priors Help? A Controlled Audit of Language Models as Priors for Small-Sample Bayesian Regression
- arXiv 2611.27075v1 · v1 2026-11-20 03:39 UTC · cs.CL
- Authors: Ran Zou, Yang Liu
- Topics: Brand/product recommendation, Clicks & measurement · score 10 · found via cs.CL
- Link: https://arxiv.org/abs/2611.27075
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) are increasingly asked where to center the coefficients of a small-sample Bayesian regression, but the evidence is unclear: benchmarks are often built to match the prior and models may remember them. We audit this practice with one frontier and one flash-tier model, using hidden feature names, post-cutoff housing data and a pre-specified test that gives features the wrong descriptions. First, the models share their errors (correlation $0.92$--$0.99$ across draws, vendors and paraphrases): averaging $20$ draws is no more accurate than one, and treating draws as independent creates overconfidence. Much of this error comes from reporting each feature's effect alone, not with the others held fixed. Second, against the best classical prior, the LLM center helps clearly on one of four benchmarks (RMSE $-5.8\%$), marginally on two, and hurts mean RMSE on the fourth. Third, the LLM's stated uncertainty is unreliable; letting the data set the prior scale cuts the harm of a wrong center four-fold against a unit-variance prior. A pre-specified external test returned the verdict \textsc{partial}: on $18$ rule-selected problems the center helps on six and hurts on four, and a hard trust gate trusts a harmful prior while an evidence-weighted mixture is safer.

### Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation
- arXiv 2611.27689v1 · v1 2026-11-20 14:55 UTC · cs.RO, cs.AI, cs.CV, cs.MA
- Authors: Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang et al.
- Topics: Citation & source selection, Manipulation · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.27689
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a robot-control interface, while the Reflector converts execution evidence into reusable operational guidance. Hierarchical Memory Architecture maintains short-term execution context and long-term experiential knowledge to support execution and reflection. Evidence-based Experience Reflection grounds failure diagnosis in observed interactions, while Recursive Harness Self-Improvement refines operational guidance across successive attempts. Experiments on RoboTwin 2.0, RoboSPA, and RMBench demonstrate the effectiveness of Embodied-Harness in generalization under environmental variations, spatial reasoning, long-horizon planning, and memory-dependent manipulation. Our method achieves success rates of 82.4%, 76.7%, and 94.4% on the three benchmarks, respectively. Real-world evaluation further yields an average success rate of 96.7% across three manipulation tasks. These results highlight the potential of Embodied-Harness to improve robotic manipulation through experience-driven harness self-improvement.

### Modeling Attributional Style at Scale: A Dataset and Analysis for Psychological Attribution Assessment and Reframing
- arXiv 2611.26900v1 · v1 2026-11-19 23:24 UTC · cs.AI, cs.CL, cs.CY
- Authors: Qiang Zhou, Hanzhen Zhu, Pan Wang, Rui Tu et al.
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL, cs.CY
- Link: https://arxiv.org/abs/2611.26900
- arXiv comment: Accepted to ICML 2026. 26 pages, 9 figures, 9 tables. Proceedings version: https://proceedings.mlr.press/v306/zhou26bw.html. Code and data: https://github.com/qzhou711/ASTD
- Journal ref: Proceedings of the 43rd International Conference on Machine Learning (ICML 2026), PMLR 306:166662-166687, 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> According to the reformulated Learned Helplessness theory, repeated exposure to uncontrollable negative events can foster a depressogenic attributional style, increasing susceptibility to depression yet remaining a tractable target for cognitive therapy. Computational research on attributional cognition, however, is hampered by the lack of large-scale datasets and robust evaluation protocols. In this work, we introduce the Attributional Style Transfer Dataset (ASTD) along with dedicated evaluation metrics, the first benchmark designed to model, assess, and reframe attributional explanations at scale. Constructed via a Prevent-Filter-Validate pipeline that integrates LLM-based generation with specialist validation, ASTD contains 42,000 real-world events paired with psychologically grounded attributions spanning seven styles. Using this dataset, we address two key challenges: (1) scalable assessment of attributional style via both supervised classifiers and zero/few-shot LLMs; and (2) attributional reframing and evaluation, where we propose automatic evaluation metrics to quantify psychological validity. Furthermore, we leverage our proposed metrics to construct a preference dataset, fine-tuning LLMs with Direct Preference Optimization (DPO) and achieving substantial gains in reframing quality. Together, our dataset, metrics, and methodology offer a new paradigm for understanding and modeling attributional style, with direct implications for scalable and adaptive mental health interventions. Code and data: https://github.com/qzhou711/ASTD

### EcomWriteBench: A Real-World Benchmark for E-commerce Writing Tasks
- arXiv 2611.27349v1 · v1 2026-11-20 09:22 UTC · cs.AI
- Authors: Kaicheng Liang, Jingyi Cui, Hongwei Wen, Feng Wang et al.
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.27349
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) are increasingly used throughout e-commerce workflows to generate content that informs purchasing decisions and supports customer interactions. Evaluating these systems requires accounting for user needs, product evidence, structural constraints, and business requirements that are not fully captured by general-purpose writing benchmarks. We introduce EcomWriteBench, a real-world benchmark containing 3,861 queries from 69 e-commerce writing tasks across 13 categories and five languages. Through task-level extraction, cross-task consolidation, and refinement guided by human feedback, EcomWriteBench constructs a shared pool of 37 abilities and identifies the subset applicable to each task. Ability-wise scoring enables us to compare state-of-the-art LLMs on EcomWriteBench and characterize their relative strengths and weaknesses across fine-grained e-commerce writing abilities. We further propose a preference-calibrated weight-learning framework that converts human pairwise preferences into interpretable scoring rubrics through global, category-level, and task-level aggregation weights. This framework provides a reusable approach for translating human preferences into automated evaluation by combining ability discovery, ability-wise scoring, and preference-calibrated aggregation, and can potentially be applied to a broad range of benchmarks beyond EcomWriteBench. On held-out queries, our scoring framework achieves 88.96% agreement with human preferences, compared with 78.54% for conventional LLM-as-a-judge scoring.

### Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification
- arXiv 2611.27410v1 · v1 2026-11-20 10:15 UTC · cs.AI, cs.CR
- Authors: Ali Yousefi, Nikos Komninos, Hafizul Asad
- Topics: RAG (generic), Manipulation · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.27410
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> A retrieval-augmented generation (RAG) system answers questions using passages it retrieves from a knowledge base, so users must trust that knowledge base. We study an attacker who quietly edits existing passages by swapping words for synonyms (PWWS, TextFooler) in a cybersecurity RAG system built from MITRE ATT&CK and CAPEC. Using a reviewed 44-question benchmark, repeated paired runs and a control corpus in which only the layout changes, we find that poisoning lowers judged answer correctness from 0.714 to 0.555. The damage comes mostly from lost evidence and refusals, not from false statements. To find the edited passages, we use relative entropy. Comparing a whole passage with normal text is a weak signal. Still, one term of the relative entropy, the log-ratio between a word and its most probable synonym, works well: with a small language model as the reference, it reaches an AUROC of 0.95 and stays near chance on the control. Used as a retrieval filter, it halves how often edited text reaches the generator, and an attacker who must keep each passage as probable under the language model fails on all 57 sections it tries. Filtering does not restore correctness, because the edited passage is usually the one that held the answer. We therefore add a runtime monitor that checks each answer against trusted MITRE STIX data and remembers the passages it rejects. On its own, it reduces exposure to edited text from 0.41 to 0.26; when it may add the trusted MITRE entry as a source, correctness rises to 0.786. We report the costs and failure cases of every defence alongside its gains.

### The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web Search
- arXiv 2611.27899v1 · v1 2026-11-20 17:38 UTC · cs.AI, cs.LG
- Authors: Yi Ding, Gaurav Kumar, Rui Min, Isabella Ye et al.
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.27899
- arXiv comment: 8 pages, 3 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Sustaining user experience (UX) quality in large-scale web search requires scalable evaluation. Traditional surveys are slow and bottleneck rapid A/B testing, while automated metrics often lack the granularity to diagnose visual-spatial UX anomalies. To address this, we introduce the Dual-Tier Sentiment Framework, a novel industrial architecture for automated UX attribution. Tier 1 (Macro System) acts as a scalable user sentiment regression detector, utilizing a fine-tuned encoder-decoder LLM (based on Gemini XS) on telemetry features. Through multi-task regularization and contextual feature engineering, this tier achieves a +9.8% PR-AUC gain on over 500,000 held-out records, matching baseline recall on all validated regressions with $\sim$20% relative precision gain among the 12 held-out experiments. In production, it reduces measurement latency from weeks to hours and cuts survey overhead by over 40%. Tier 2 (Micro System) provides granular diagnostics by employing a Multimodal LLM (Gemini 3.0 Pro) to natively assess visual renderings and spatial layout of web result blocks, quantifying "User Toil" as the estimated effort required to reach a satisfactory result. Enhanced by RL-based automated prompt optimization and an AI judge for win/loss patterns, the MLLM yields a $>$6.5% F1 score improvement, offering deep insights into content quality and layout friction. Ultimately, this framework enables scalable, accurate, and diagnostic UX attribution, processing O(100k) live experiment queries daily.

### Poisoning Attacks and Collaborative Defense Framework for LightRAG-Based Construction Regulation Knowledge
- arXiv 2611.27460v1 · v1 2026-11-20 11:08 UTC · cs.CR
- Authors: Yingyan He
- Topics: RAG (generic), Manipulation · score 7 · found via cs.CR
- Link: https://arxiv.org/abs/2611.27460
- arXiv comment: Master's thesis, SWISS UMEF, November 2026. 60 pages, 35 tables, 10 figures
- Full text: data/fulltext/2611.27460.txt

> Retrieval-augmented generation (RAG) is widely used in construction, yet the security of building-regulation knowledge bases has received little study. This thesis reports a pre-registered experiment on one fully instrumented LightRAG system built on the UK Approved Documents. Using a 150-item benchmark labeled with safety consequences and tampering directions, it evaluates four attacks (text layer, graph layer, fabricated amendment narrative and a defense-aware adaptive attacker) together with a three-layer retrieval-graph-generation defense in a full factorial design. Text-level poisoning succeeded, with success rising with the budget; graph-level poisoning was less effective, contrary to the registered hypothesis. The full defense met the registered criterion and six of the seven configurations met its threshold, but those containing the generation layer did so by refusing 69-80 percent of poisoned queries, costing up to 74 points of clean accuracy, whereas provenance-based retrieval filtering cost no measurable clean accuracy in the configuration used. A second experimental batch showed that excluding a legitimate unregistered amendment caused no measurable loss of accuracy either, as its wording reached the generator through the graph's entity and relationship descriptions, the route the poison took, which no layer inspects. Interactions were strong, so no layer's contribution can be isolated. A reported zero attack success rate is not evidence of detection unless the refusal rate is reported with it: zero arises either because provenance filtering removes every document outside the manifest without judging its content, or because the system refuses. Layered defenses must therefore be evaluated factorially, and regulatory RAG assistants require corpus admission control and version-aware verification before they can support safety-critical decisions.

### MomentMem: Memorizing Key Moments for Robot Manipulation
- arXiv 2611.26745v1 · v1 2026-11-19 19:42 UTC · cs.RO, cs.AI
- Authors: Guangyu Zhao, Yongchang Zhang, Ruizhang Jiang, Zhihong Yu et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.26745
- Full text: data/fulltext/2611.26745.txt

> Robotic manipulation often requires remembering visual information that is no longer observable, such as the original location of an object. Existing approaches typically rely on full observation histories, which become redundant over long horizons, or text summaries, which may omit precise visual details. We study visual moment memory, the ability to retain such details from key moments for subsequent manipulation. To support this study, we introduce VMBench, a suite of long-horizon manipulation tasks requiring memory of spatial locations, visual appearances, and their associations. We further propose MomentMem, a hierarchical architecture in which a VLM-based memorizer selects keyframes and an executor predicts actions conditioned on the selected memories. This separation enables us to evaluate memory selection alongside closed-loop task success and to study memorizer generalization independently of the executor. On VMBench, MomentMem achieves 49.9% average success, outperforming the strongest evaluated baseline by 31.7 percentage points. Moreover, we find that the memorizer transfers well to unseen appearances zero-shot. It can also adapt to an unseen task with only a few memory annotations, reaching 43.7% success, close to the 44.3% obtained with full memory supervision. Further experiments show competitive performance on RMBench and improvements in real-robot manipulation. These results highlight the value of retaining sparse visual evidence for memory-dependent manipulation. Our code is available at https://github.com/PKU-VaLuE-Lab/MomentMem.

### Same Facts, Different Decision: Fact-Invariant Manipulation and Provenance-Based Defense in Typed Decision Models
- arXiv 2611.27016v1 · v1 2026-11-20 02:46 UTC · cs.AI
- Authors: Yujie Wang, Haotian Chi, Shunrong Jiang
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.27016
- arXiv comment: 15 pages, 7 figures, 14 tables
- Full text: data/fulltext/2611.27016.txt

> Typed decision models such as TypeSafe's Jev answer only with a probability, an option, or a score, so software can act on them directly. Their inputs, however, often include text from outsiders. Prior attacks test this risk poorly. Injected instructions rarely work on these models, and added facts can make a changed decision correct. We show that outside comments can persuade these models to make a wrong decision without adding any fact. We propose LEVER, an attack that writes such comments with four levers from argumentation theory, uses a separate verifier to discard any comment that adds a fact, and searches for effective comments guided by the model's output probabilities. We further propose the Provenance Gate, a defense that accepts a changed decision only if the model reaches it again without the outside comments. On three benchmarks, LEVER flips about a third of Jev's correct decisions, 2.8 times as many as the strongest prior attack under the same limit on facts, and more on five other models. The gate blocks all of these attacks with at most one extra query and still accepts trusted updates.

### Subverting Tool Arguments: Defense-Evading Metadata Poisoning in LLM Agents
- arXiv 2611.27041v1 · v1 2026-11-20 03:13 UTC · cs.CR
- Authors: Shih-Chieh Dai, Xinyu Sun, Haichuan Zhang, Zhiyuan Zhong et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.27041
- Full text: data/fulltext/2611.27041.txt

> Conventional indirect prompt injection (IPI) attacks hijack an LLM agent's workflow through malicious instructions embedded in retrieved external content. The growing adoption of the Model Context Protocol (MCP) exposes another attack surface: tool descriptions supplied by third-party MCP servers. Attackers can manipulate this metadata to induce malicious argument generation during tool calls. The challenge is to ensure that the modified descriptions still appear benign to both LLMs and users. Existing IPI attacks, however, struggle to achieve both high attack success and low detectability in this setting. To address this challenge, we propose GRAFT, an LLM-based optimization method for crafting adversarial tool descriptions. Specifically, GRAFT uses a masking mechanism to identify argument-relevant token positions for targeted injection. It then iteratively refines candidate descriptions using dynamic mutation strategies proposed by an LLM, guided by the agent's tool choices and generated arguments. We evaluate GRAFT on three public datasets against several attack baselines. The results show that GRAFT achieves higher attack success while maintaining low detection rates across five filter-based defenses. It also bypasses several existing IPI defenses. Even under an adaptive defense trained on GRAFT-generated injections, GRAFT remains more effective than the baselines.

### Manipulation-resistant reputation for peer-to-peer scientific publishing: a combination-therapy approach
- arXiv 2611.27625v1 · v1 2026-11-20 13:50 UTC · cs.CR
- Authors: Frédéric Prost
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.27625
- Full text: data/fulltext/2611.27625.txt

> In open peer-to-peer networks, where publishing is nearly free and identities are cheap, reputation systems decide what deserves attention, and their metrics become targets for manipulation. We study how to choose and combine reputation signals so that manipulation does not pay while genuine contribution does. Inspired by combination therapies in medicine, we describe each gaming action by its effects on all signals. For aggregation by the minimum of the signals, we prove that, in a global linear model, either some mix of gaming actions raises every signal by more than it costs, or the net gain of gaming is bounded by the imbalance of the attacker's honest profile; locally, gaming brings no first-order gain exactly when an admissible weighting is supported on the attacker's weakest signals. We then specify, without implementing it, MagMell, a two-tier system for peer-to-peer scientific publication: a protocol that orders signed events by Byzantine fault-tolerant consensus, enforces budgets and settles staked assessments, and open reputation algorithms that any node can run. Simulations on synthetic data show that minimum aggregation makes networks of fake identities, collusion rings and floods of generated papers lose rank beyond small intensities, at the price of a lower correlation between rank and quality for honest accounts. They also show that criticism is rarely settled, because the evidence needed is seldom available. The replicated log should grow by about 26 kilobytes per identity and year (analytic estimate), and a full recomputation of reputations takes 1.0 to 1.6 seconds for 100,000 identities (measured).

### Redesigning Neural Networks to Not be Confidently Wrong even to Strong Adversarial Attacks
- arXiv 2611.27811v1 · v1 2026-11-20 16:38 UTC · cs.CV, cs.AI, cs.LG
- Authors: Michael W. Spratling, Heiko H. Schütt
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.27811
- arXiv comment: Code: https://codeberg.org/mwspratling/STEAL/
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Early deep learning models attempted to simulate visual perception using a neural hierarchy that alternated between two types of layer: one modelled on cortical simple cells (that was designed to increase selectivity), and one modelled on cortical complex cells (that aimed to increase tolerance). We show that such a neural network (NN) architecture, when implemented with novel components that are better able to learn selective and tolerant representations, is capable of accurate and robust image classification and improved alignment between the behaviour of the model and the perceptual abilities of humans. Firstly, the proposed models are shallow, fewer than ten layer-pairs, which is more consistent with the rapid feedforward object categorisation performed by the biological visual system. Secondly, they are far less prone to producing classification predictions with high confidence for samples from unknown classes or for image consisting of pure noise, and hence, like humans are not easily fooled into perceiving objects that are not present in the image. Thirdly, for the proposed NNs adversarial samples cause predictions with low confidence, enabling them to be accurately identified. In contrast to humans, our networks still do not correctly classify adversarial samples. However, the behaviour of our networks is a significant step towards human-like behaviour compared to standard DNNs that produce highly confident, but incorrect, classification predictions for adversarial samples. The increased robustness to adversarial and unknown samples is achieved while maintaining competitive performance in terms of generalisation to novel samples from the training categories. This enables models of this type to be competitive with state-of-the-art DNNs across multiple different evaluation metrics and benchmark tasks.

### Pre-Crawl Prioritization and Seed Classification for Large-Scale Web Archiving
- arXiv 2611.27743v1 · v1 2026-11-20 15:37 UTC · cs.DL, cs.IR
- Authors: Akshith Garapati, Sawood Alam
- Topics: Crawl · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.27743
- arXiv comment: 4 pages, 4 figures, 1 table. Published in the 2025 ACM/IEEE Joint Conference on Digital Libraries (JCDL)
- Journal ref: 2025 ACM/IEEE Joint Conference on Digital Libraries (JCDL), pp. 273-276
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Pre-crawl prioritization systems decide which pages to fetch first before indexing, aiming to improve crawl efficiency and coverage. Existing approaches based on page popularity and relevance are unsuited to web-archival crawlers that prioritize comprehensive coverage over selective retrieval. We explore prioritization techniques tailored to web archival operations using URL lexical analysis, dynamic domain reputation systems, and HTTP response analysis to inform crawl scheduling decisions. By incorporating predictive models that estimate content change and disappearance probabilities, we improve crawl completeness while reducing redundant visits to stable resources. Through large-scale experiments, we demonstrate that our methods improve archival effectiveness and resource utilization compared to undirected crawling.

### Explicit Style Extraction for Personalized Long-Form Text Generation
- arXiv 2611.27211v1 · v1 2026-11-20 06:52 UTC · cs.AI, cs.CL, cs.IR
- Authors: Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam, Anisa Dye et al.
- Topics: RAG (generic) · score 1 · found via HF daily papers, cs.IR
- Link: https://arxiv.org/abs/2611.27211
- arXiv comment: 21 pages, 8 figures, 11 tables
- Full text: data/fulltext/2611.27211.txt

> Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an explicit step: the model first fills StylePrism with the user's patterns, quoted evidence, and habits to avoid, then drafts from the user's samples and revises the draft twice against this profile, guided by its own style scores. On the three long-form tasks of LongLaMP with three LLMs, SP-Refine outperforms LongLaMP's retrieval-augmented baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average and by up to 35.8%. Annotating users' own texts with the extracted profiles shows that StylePrism captures concrete, checkable habits, from the order of rhetorical moves to a reviewer's sign-off. Ablations show that the profile helps as revision guidance, not as a replacement for the samples: writing from the profile alone is worse in all 27 comparisons, while a single implicit-inference call is a cheaper alternative that comes close. Oracle variants that let the reviser see the reference, together with reference-free controls, show that larger refinement gains require information unavailable at inference time.

## Other new cs.IR papers, title only (6)
- ERA: Embed, Route, Adapt for Cold-Start Cross-Model Latent Retrieval — https://arxiv.org/abs/2611.26919
- Leader Finding: A New Variation of Expert Finding in Community Question Answering — https://arxiv.org/abs/2611.26921
- Which Dwarf Is This? Doppeldwarf-306 and Near-Identical Instance Retrieval — https://arxiv.org/abs/2611.27490
- Deep Cross-Division Network for Product-and-Ratio Feature Interactions in Industrial Ranking — https://arxiv.org/abs/2611.27514
- Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search — https://arxiv.org/abs/2611.27910
- DiTraR: Diverse Scorers and Transcript-Guided Re-ranking for Video Corpus Moment Retrieval — https://arxiv.org/abs/2611.27931

## Already listed on an earlier day, still inside the look-back window (48)
- FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification — https://arxiv.org/abs/2611.25071 (score 14)
- GEOHunter: Mapping a Generative Engine Optimization Network in the Wild — https://arxiv.org/abs/2611.26564 (score 14)
- DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents — https://arxiv.org/abs/2611.25583 (score 13)
- X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction — https://arxiv.org/abs/2611.24283 (score 10)
- Seer: Guiding Small Deep-Research Agents with Shared Decision Models — https://arxiv.org/abs/2611.26423 (score 10)
- MambaLIFT: Reference-Based Mechanism-Aware Attribution for VMamba — https://arxiv.org/abs/2611.25644 (score 9)
- LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature — https://arxiv.org/abs/2611.25845 (score 9)
- RouterWeave: A Unified Observation Layer for Cross-Platform Activity Analysis via Home Routers — https://arxiv.org/abs/2611.26134 (score 8)
- Visual Attribution Limits and Graded Provenance Auditing in Commercial Video-Generation APIs — https://arxiv.org/abs/2611.26508 (score 8)
- User Perceptions of Deceptive In-Vehicle Infotainment User Interfaces — https://arxiv.org/abs/2611.25195 (score 7)
- Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI) — https://arxiv.org/abs/2611.26553 (score 7)
- What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents — https://arxiv.org/abs/2611.24231 (score 6)
- AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents — https://arxiv.org/abs/2611.24313 (score 6)
- PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents — https://arxiv.org/abs/2611.24362 (score 6)
- SCR: Detecting Backdoor-Poisoned Samples through Clean-Reference Residuals — https://arxiv.org/abs/2611.24558 (score 6)
- Gradient-Based Defensive Poisoning Against System Identification Attacks on Cyber-Physical Systems — https://arxiv.org/abs/2611.24662 (score 6)
- On the Impact of Feature Reduction Techniques on Adversarial Attacks — https://arxiv.org/abs/2611.25004 (score 6)
- MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation — https://arxiv.org/abs/2611.25105 (score 6)
- Demonstration-Free Skill Composition for Navigation and Manipulation — https://arxiv.org/abs/2611.25462 (score 6)
- Passing NPCR Without Diffusion: Exact Signatures, a Detection Benchmark and an Audit of Published Image Ciphers — https://arxiv.org/abs/2611.25561 (score 6)
- Diagnosis is not a policy: a state-transition audit of caoability-conditioned test-time inference — https://arxiv.org/abs/2611.25566 (score 6)
- MetaScanner: An Empirical Study and Proactive Defense against Deceptive UI Attacks in Social VR — https://arxiv.org/abs/2611.25608 (score 6)
- DNA: Unlocking Depth Scaling in CTR Models — https://arxiv.org/abs/2611.25659 (score 6)
- TipDex-VTLA: Learning When to Refine Actions with Touch for Dexterous Manipulation — https://arxiv.org/abs/2611.25683 (score 6)
- When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards — https://arxiv.org/abs/2611.25793 (score 6)
- Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation — https://arxiv.org/abs/2611.26444 (score 6)
- PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation — https://arxiv.org/abs/2611.26596 (score 6)
- Retrieving Patristic References and Modelling Topics in Bullinger's Reformation Correspondence — https://arxiv.org/abs/2611.25247 (score 4)
- VideoTrail: Interactive Video Foraging Through Hierarchical Visualization — https://arxiv.org/abs/2611.25377 (score 3)
- LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented Generation — https://arxiv.org/abs/2611.25229 (score 2)
- AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development — https://arxiv.org/abs/2611.25582 (score 2)
- Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem — https://arxiv.org/abs/2611.26398 (score 1)
