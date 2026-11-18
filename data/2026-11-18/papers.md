# Paper candidates — 2026-11-18 (IST)

Generated 2026-11-18 07:52 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 27 new topic matches · 12 other new cs.IR · 72 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (27), highest score first

### GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk
- arXiv 2611.22223v1 · v1 2026-11-17 05:06 UTC · cs.CR
- Authors: Chaklam Cheong, Tiancong Cao, Qi Li, Zelin Zhang et al.
- Topics: Brand/product recommendation, Agents, Manipulation · score 15 · found via cs.CR, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.22223
- arXiv comment: Accepted for publication in Proceedings on Privacy Enhancing Technologies (PoPETs), 2027, Issue 2 Abstract shortened for arXiv character limit
- Full text: data/fulltext/2611.22223.txt

> Large Language Model (LLM)-based web agents rely on data minimization and least privilege to protect user privacy. We show that these principles are necessary but insufficient: they constrain authorized sources, but not higher-sensitivity sources that remain reachable. A website can request a field unavailable from authorized sources, creating an information gap. To complete the task, a goal-driven agent may escalate to reachable but unauthorized sources and disclose accumulated sensitive information. We formalize this vulnerability as GapLeak, where an adversary exploits a legitimate web form without prompt injection or other malicious instructions. We evaluate GapLeak on three web-agent frameworks and six LLMs from Anthropic, Google, and OpenAI across recruitment, e-commerce, travel, and healthcare. GapLeak induces an average unauthorized disclosure of approximately 37%. The information gap is the primary driver: eliminating it reduces disclosure by more than 50%. Existing instruction-level defenses based on least privilege partially mitigate the vulnerability but often reduce task success. We propose submission-time verification, which filters unauthorized content before form submission, eliminating over 96% of unauthorized disclosures while preserving task success.

### How Web Research Agents Interpret User Priorities
- arXiv 2611.22989v1 · v1 2026-11-17 16:07 UTC · cs.AI, cs.HC
- Authors: Robin Sharma, Parisa Suchdev
- Topics: Citation & source selection, Query fan-out · score 14 · found via cs.AI, cs.HC
- Link: https://arxiv.org/abs/2611.22989
- Full text: data/fulltext/2611.22989.txt

> Web research agents gather information online and write cited reports, including financial analysis. Users can state a priority to guide this research, but a priority may not say how to judge the options, leaving the agent to choose the criteria. We examine how two such agents, built on OpenAI and Anthropic models, interpret a stated priority. In 36 runs, the agents compared Microsoft and Alphabet as businesses. Prompts asked for special attention to growth or resilience, or gave no priority. We analyzed reports, searches, returned sources and cited sources. Of the 24 reports given a priority, 21 focused on it, but their criteria varied. Under the growth priority, OpenAI reports that ranked the companies accounted for risk or predictability and favored Microsoft, while the Anthropic ones judged growth by its pace and favored Alphabet. Under the resilience priority, reports used partly different criteria, and most named Microsoft as the more resilient company. Of the search and source measures tested, only the Anthropic agent's search wording differed detectably by condition. These findings suggest evaluations should examine the criteria behind a report's judgements, not only its focus or accuracy. Interfaces could let users see and adjust those criteria.

### The Fragility of Reasoning-Importance Attribution for Pruning Language Models
- arXiv 2611.22234v1 · v1 2026-11-17 05:36 UTC · cs.AI
- Authors: Himanshu Mishra
- Topics: GEO/AEO, Citation & source selection · score 13 · found via cs.AI
- Link: https://arxiv.org/abs/2611.22234
- Full text: data/fulltext/2611.22234.txt

> Attribution-guided pruning scores components by their causal contribution and protects the important ones, and it is increasingly applied to compress reasoning language models without destroying their chain of thought. Its reliability rests on an unexamined assumption: that reasoning importance can be faithfully measured. Across four small reasoning models, we show this measurement is fragile in three ways, each of which changes pruning decisions. First, scoring final-answer tokens, the natural choice, saturates in every chain-of-thought model we test (answer-token negative log-likelihood, NLL, of $10^{-4}$--$10^{-3}$) because the model states its answer inside its own reasoning; guiding head pruning with this target costs 27.6 and 32.2 accuracy points relative to scoring reasoning tokens on the two models we power with five seeds, while perplexity barely moves and even reverses sign at 7B. Second, causal importance is not localizable to single units: single-neuron effects sit at the measurement floor, their cross-split ranking is noise, and they cancel: a group's ablation effect disagrees in sign with the summed effects of its members in 90\% of groups. Reproducible importance emerges only at groups of $\sim 100$ neurons. Third, contrastively isolated ``reasoning-specific'' importance is not separable from generic importance, and protecting it is worse than protecting raw importance. We additionally pre-registered the hypothesis that distillation-induced concentration of importance predicts the pruning cost; it is not supported, and since our grid confounds concentration with scale, we report it as unresolved rather than reversed. The result is a short set of measurement rules: score reasoning tokens, attribute at coarse granularity, and evaluate with accuracy rather than perplexity.

### TUSI: A Citation-Grounded Graph-Based Benchmark
- arXiv 2611.21823v1 · v1 2026-11-16 19:38 UTC · cs.AI, cs.CL
- Authors: Marzieh Karimi, Mehran Safayani, Alireza Basiri
- Topics: Citation & source selection, RAG (generic) · score 9 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.21823
- arXiv comment: 28 pages, 11 figures, including appendix
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Evaluating retrieval-augmented generation (RAG) systems in Persian law remains challenging because benchmarks lack realism, grounding, and coverage of legal reasoning. Existing resources are either synthetically generated from statutory texts, lacking natural information needs, or derived from informal legal question--answer sources without explicit linkage to authoritative legal documents, making them unsuitable for rigorous evaluation of grounded legal reasoning. To address this gap, we introduce TUSI-Bench, a structured Persian legal benchmark designed for the evaluation of RAG-based systems. TUSI-Bench is built upon a multi-layered legal knowledge framework containing 7,261 legal articles and integrating codified statutes, legal commentaries, doctrinal writings, and Supreme Court unification rulings. We also construct a legal knowledge graph linking articles and concepts for structure-aware retrieval. Based on this foundation, TUSI-Bench provides two complementary evaluation tasks: (i) TUSI-QA, an open-ended question answering benchmark containing 1,999 questions that requires grounded responses with explicit legal citations, and (ii) TUSI-Bar, a multiple-choice benchmark containing approximately 500 four-option questions derived from Iranian Bar examination questions. Furthermore, we propose a graph-based retrieval baseline that leverages relational structure within the legal knowledge graph. Experimental results demonstrate that incorporating graph-based relations improves retrieval recall by up to 8 percentage points compared to standard baselines, highlighting the importance of structured legal representations for RAG systems. The proposed benchmark provides a standardized resource for evaluating grounded legal reasoning in Persian and enables future research on structured legal intelligence.

### IntentGR: Enhancing Intent for End-to-End Personalized Generative Retrieval in Search
- arXiv 2611.22788v1 · v1 2026-11-17 13:51 UTC · cs.IR
- Authors: Gefan Ye, Yanjing Wu, Yinfu Feng, Zhiqiang Wang et al.
- Topics: GEO/AEO, Brand/product recommendation · score 9 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22788
- arXiv comment: 11 pages, 3 figures; Accepted by WSDM 2027 Findings
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Personalized generative retrieval in search should jointly satisfy the user's immediate search intent and long-term preference. Recent end-to-end approaches, primarily explored in recommendation, unify item tokenization and sequence generation within a single model, allowing semantic identifiers (SIDs) to be optimized toward the downstream generation objective. However, these methods often treat the query merely as an input feature, without explicitly leveraging it to guide either identifier learning or sequence generation. This leaves intent guidance weak in both the tokenization and the generation stage, causing generated semantic identifiers to drift toward high-frequency token patterns rather than the current search intent. In this work, we find that incorporating additional query-related evidence into the framework of end-to-end generative retrieval is important. Based on this finding, we propose IntentGR, an intent-enhanced end-to-end framework that strengthens query semantics at four complementary stages of the retrieval pipeline. Query-Aware Semantic Behavior Representation (QBR) introduces query-level behavioral evidence as a new input signal; Query-Semantic Alignment (QSA), Long-Tail Query Enrichment (LQE), and Query-conditioned Attention Modulation (QAM) then serve as integration mechanisms at the optimization, training-distribution, and decoding stages to fully exploit this evidence. Experiments on the public AOL4PS benchmark and AE, a large-scale industrial e-commerce dataset, show that IntentGR improves Recall@10 by 8.11% and 11.96% over the strongest baseline, with strong gains on long-tail queries. These results suggest that enriched query-related input evidence, together with effective integration mechanisms, is beneficial for building intent-aware end-to-end generative search systems.

### Can Decision Models Replace LLMs in Real-World Contact Center Classification and Judging Tasks?
- arXiv 2611.22949v1 · v1 2026-11-17 15:39 UTC · cs.CL
- Authors: Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.CL
- Link: https://arxiv.org/abs/2611.22949
- Full text: data/fulltext/2611.22949.txt

> Contact center systems often need to make bounded decisions, such as identifying a caller's intent, retrieving the knowledge-base article that answers a query, assessing agent compliance, or judging the output of AI models used in production. Decision models return a typed answer and its probability directly, making them a promising cost-effective alternative to generative Large Language Models (LLMs) in such bounded conversational tasks. However, their effectiveness in real-world contact center applications remains unclear. In this paper, we compare nine decision models against thirteen generative LLMs in zero-shot settings across eight contact center use cases: six classification tasks and two judging tasks. Our experiments demonstrate that many decision models can match the performance of frontier LLMs on contact center classification, and API-based closed decision models achieve this at the lowest per-request cost among the API models we evaluate. We further observe that their confident predictions are more accurate, enabling selective routing in real-world production scenarios. Across classification tasks, the main weakness of most decision models is abstention: they rarely choose the no-answer option, which accounts for most of their gap to the strongest LLMs (although Gemini-Decision-1 is the notable exception in this regard). We also find that the judging quality of decision models drops sharply for smaller models, and they are also more prone to position bias. In short, our findings provide practical guidance for selecting decision models based on abstention behavior, confidence, and deployment cost, rather than overall accuracy alone.

### Threat Landscape of Vibe Coding and the Road to Secure Autonomy
- arXiv 2611.21822v1 · v1 2026-11-16 19:38 UTC · cs.CR, cs.ET
- Authors: Devki Nandan Jha, Shubh Anand, Karthick Keeranagere Krishnaiah, Roman Ahearn et al.
- Topics: GEO/AEO, Manipulation · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.21822
- arXiv comment: 35 pages, 6 figures, 5 tables, Submitted to ACM Computing Surveys
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Vibe coding is reshaping software development, enabling faster implementation and allowing individuals with limited programming experience to describe requirements in natural language while AI agents write, test, and deploy the code. As these agents evolve into autonomous systems that execute commands, manage dependencies, access cloud resources, and interact with other agents, their security risks extend beyond incorrect code to actions with direct consequences for software systems. Although research on these risks is expanding, it remains fragmented across areas including prompt injection, insecure code generation, supply-chain attacks, and human factors, with limited consensus on terminology, threat assumptions, and evaluation. This paper consolidates emerging research through the lens of the vibe coding workflow. We establish a reference architecture, characterise six levels of agent autonomy, and develop a threat model centred on five trust boundaries spanning developers, AI models, tools, cloud infrastructure, and the wider software ecosystem. Building on this foundation, we propose a taxonomy of twenty-one threats across nine classes. For each threat, we review the available evidence, assess proposed defences, and identify limitations. Our analysis highlights that risks increase with agents' operational authority, while most defences rely on model judgement and address isolated threats. Finally, we identify eleven research challenges, including enforceable limits on agent authority and shared benchmarks and methodologies for assessing vibe coding security.

### Does the Model Use What It Cites? Counterfactual Tests of Grounded Reasoning Chains in Small Video-Language Models
- arXiv 2611.21940v1 · v1 2026-11-16 22:03 UTC · cs.CV, cs.AI, cs.LG
- Authors: Jugal Gajjar, Kamalasankari Subramaniakuppusamy
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.21940
- arXiv comment: 24 pages, 4 figures, 27 tables. Code: https://github.com/JugalGajjar/CausalSight
- Full text: data/fulltext/2611.21940.txt

> A grounded reasoning chain cites a frame span and a box for every step, so a reader can check where the model looked. Whether the answer depends on the cited region is a different question. We test it by intervention: the regions a model cited in its own chain are blacked out, and the share of correct answers that flip is compared with blacking out boxes of the same size elsewhere on the same frames. The paired difference, the cite gap, needs no annotation. We apply it to 2-3B video-language models trained on exact CLEVRER chains and on pseudo-labelled NExT-QA chains. With the same weights, the cite gap is 0.089 on CLEVRER and 0.003 on NExT-QA. Pooled over models, masking the cited boxes flips 2.2 times as many correct answers as the control on CLEVRER and 1.1 times as many on NExT-QA, also among the answers that depend on the video at all, while the boxes pass a grounding check on both. Masking the cited entity on every frame, instead of the cited box, flips 1.9 times as many answers as its control. The NExT-QA chains were supervised to cite two frames of entities that stay visible on most frames, so this outcome is what the supervision predicts; the point is that the usual check on grounded chains cannot see it. A citation can be verifiable and relevant without the answer depending on it, and a test of grounded reasoning should remove what a chain names, not only where it points.

### Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents
- arXiv 2611.22033v1 · v1 2026-11-17 00:55 UTC · cs.AI, cs.CL, cs.CY, cs.HC, econ.GN
- Authors: Adi Krishnamoorthy, X. Y. Han
- Topics: Brand/product recommendation · score 8 · found via cs.AI, cs.CL, cs.CY, cs.HC
- Link: https://arxiv.org/abs/2611.22033
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) are increasingly deployed as autonomous shopping agents that process multimodal product listings (consisting of visual and text data) and recommend purchases on behalf of consumers. Naturally, one might assume that models with more thinking power would make higher-quality purchasing decisions. To test this belief, we ask two questions about such agents: does asking a model to think harder make it choose better products, and does the confidence it reports tell us the likelihood it may be wrong? We benchmark ten frontier models on three product-choice benchmarks built from WebShop, Amazon's SQID and Wayfair's WANDS platforms to see if LLMs with more thinking power actually make better-quality product purchase decisions. Across all three benchmarks, we found that increasing the thinking effort does not increase decision quality in a statistically meaningful way. The same change in thinking effort raises stated confidence at a statistically significant level, so extra thinking buys confidence rather than correctness. We also measure the calibration of these models (how well their reported confidence percentage matches their true correctness percentage) in these tasks and show that most models are not well-calibrated at every effort level. We also find that errors are strongly shared: when one model errs in a task, several others tend to err on that same task. Furthermore, on tasks where several models all err, a large number of them pick the same wrong product.

### Right Labels, Wrong Reasons: Signed Feature Attribution for Multi-Label Explainability
- arXiv 2611.22515v1 · v1 2026-11-17 10:07 UTC · cs.LG, cs.AI
- Authors: Kenton White
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.22515
- arXiv comment: 7 pages, 1 figure, 5 tables. Accepted at the 2027 IEEE Symposium Series on Computational Intelligence (IEEE SSCI 2027), Gold Coast, Australia, February 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> When a multi-label classifier assigns the right labels, it may do so for the wrong reasons. Diffuse feature combinations may vary across classifier families and lack a dominant feature. This paper proposes FLEX (Fisher LDA Explainer), a global surrogate that fits a single direct multi-label Fisher LDA over the full binary label matrix, producing signed feature attribution lists for each label in a single coherent coordinate system. Across the evaluated benchmarks and classifier families, FLEX reproduces the black box's predictions with consistently high fidelity. Pooling covariance across labels outperforms a per-label alternative on most datasets, with the advantage growing largest where labels are numerous and positive examples are scarce. FLEX's fidelity-complexity Pareto curve is monotonically increasing, giving practitioners a predictable path to higher-fidelity explanations as more features are used, and its in-sample fidelity matches or leads Binary Relevance alternatives once a modest feature budget is allowed. The magnitude of each discriminant weight vector bounds its label's separability, flagging labels that may be predicted correctly for the wrong reasons. The evaluated classifiers largely agree on which predictions to make, but reach those decisions through different feature subsets when no single feature dominates.

### PACT: Plan-Action Consistency Training by Preserving Correct Plans and Repairing Actions in GUI Agents
- arXiv 2611.22591v1 · v1 2026-11-17 11:14 UTC · cs.AI, cs.CV, cs.LG
- Authors: Zhuohan Cai, Zhangxuan Gu, Runze Li, Beitong Zhou et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.22591
- arXiv comment: 21 pages, 11 figures, including supplementary material
- Full text: data/fulltext/2611.22591.txt

> GUI agents can formulate a correct immediate plan in their reasoning yet emit an action that fails to execute it, creating an execution gap. This recurring mismatch undermines reliable task completion, as a single execution error can derail a multi-step workflow. In outcome-supervised reinforcement learning, broadcasting a negative response-level advantage across all generated tokens risks penalizing valid planning together with erroneous execution. To address this credit-assignment conflict, we introduce PACT (Plan-Action Consistency Training), a training framework that combines reference-aligned plan protection and plan-aligned action repair without altering the original scalar action reward. Using annotated reference actions to identify execution gaps, PACT protects the verified plan by masking negative policy-gradient contributions across its token span. Keeping the generated reasoning unchanged as context, it then favors the reference action over the emitted erroneous action through a preference surrogate with stop-gradient pair weights. Compared with the outcome-only baseline, PACT raises AndroidWorld task success from 60.34% to 68.97% (+8.63 pp), while improving rule-based plan-action consistency on AndroidControl High from 83.71% to 89.74% (+6.03 pp). Adapting PACT to desktop agents also improves task success from 40.92% to 44.17% (+3.25 pp) on the full 369-task OSWorld benchmark. Together, these results establish PACT as an effective credit-assignment framework for bridging execution gaps and improving task completion across mobile and desktop GUI environments.

### SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway
- arXiv 2611.22971v1 · v1 2026-11-17 15:53 UTC · cs.AI, cs.CR
- Authors: Yuxuan Zhou, Chen Xiong, Haitong Liu, Kuofeng Gao et al.
- Topics: Agents · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.22971
- arXiv comment: 30 pages, 14 figures, 29 tables
- Full text: data/fulltext/2611.22971.txt

> Safety benchmarks for computer-use agents (CUAs) place the harm either in the intent of the task or on a single screen: a malicious instruction, an injected command, a phishing page. An agent that checks the task and each screen in isolation can pass them, so they do not test whether it combines facts seen on different screens. Yet in delegated work, harm often arises exactly this way: a fact about a person on one screen, a fact about an item on another, and a legitimate task that binds them. We introduce SEAM (Safety Execution Across Multiple screens), a benchmark of such cross-screen compositional harm: 600 multi-step, cross-application OSWorld tasks in which the instruction and every single observation are benign and only their combination is harmful. Minimal-pair variants that differ in one place, scored from the server log rather than by an LLM judge, locate where an agent fails. General-purpose open-weight and flagship agents carry out the harm in up to 92% of runs, yet decline when the user states it in one sentence. Agents open the decisive pages, so exposure is not the primary bottleneck. Asked about those pages, they flag the harm, and with thinking they often write the conflict into their reasoning and confirm anyway. Safety recognition thus does not reliably translate into safe execution, and the translation depends on the information channel: the same warning stops agents far more often in the user's instruction than on screen. Proprietary models are markedly more cautious. We release SEAM with its generator and quality gates at https://yuxuan2003.github.io/SEAM/ .

### Hidden-State Similarity Predicts Re-Elicitation After Inoculation Prompting
- arXiv 2611.23096v1 · v1 2026-11-17 17:20 UTC · cs.AI
- Authors: Rose N. Kwon, Samy Mammeri, Sabyasachi Sahoo, Christian Gagné et al.
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.23096
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Fine-tuning on narrow harmful tasks can cause emergent misalignment, where models generalize harmful behavior beyond the training distribution. Inoculation prompting can reduce this effect by explicitly eliciting the undesired behavior during training, but recent work shows that the behavior can reappear when evaluation prompts contain cues from the training context. We study what makes such prompts effective triggers. We find that, surprisingly, textual similarity to the inoculation prompt is an incomplete predictor. Instead, prompts are more likely to re-elicit suppressed behavior when they induce activation states similar to those produced by the inoculation context. These findings advance our understanding of how inoculation prompting modulates conditional misalignment, and suggest that activation space analysis can help identify when suppressed behaviors remain accessible under eval-time prompts.

### Attribution Through the Decoder: Prediction-Space Explanations for Structured Outputs
- arXiv 2611.23161v1 · v1 2026-11-17 18:13 UTC · cs.CV, cs.AI
- Authors: Zaer Bin Zaqy, Brinnae Bent
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.23161
- arXiv comment: Under review
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Networks that predict angles, gaze directions, and rotations do not output these quantities directly: they emit raw coordinates that a fixed decoder, such as normalization, maps to the final prediction. Attribution methods are usually applied to the raw coordinates, so they can credit inputs for changes the decoder discards, such as rescaling a vector when only its direction matters. The resulting explanation can highlight inputs that have no effect on the prediction. We instead attribute through the decoder differential, which for normalization decoders reduces to a scaled tangent projection. We characterize invariance to output rescaling, show that every fixed smooth scalar target on a sphere has points of zero tangential sensitivity, and show that an endpoint-projected variant of Integrated Gradients can still attribute to scale-only inputs, whereas direct angular Integrated Gradients cannot. On synthetic tasks with analytically known relevance, ambient attribution assigns up to 72% of its mass to an irrelevant region. On MPIIGaze validation data, tangent Grad-CAM produces 44% greater prediction displacement under 10% pixel deletion. On PASCAL3D+ with a 6D rotation decoder, the full differential improves mean deletion displacement by 14.1 degrees over the ambient coordinate sum and by 13.8 degrees over a decoder-invariant scalar. Results for a two-polarity tangent LayerCAM variant are mixed: it exceeds ambient-sum LayerCAM on circular regression but no difference is detected on quaternion pose. These results separate two failure sources, radial contamination and scalarization loss. The approach uses existing attribution methods with decoder-aware targets, although some variants also require changes to attribution aggregation. An invariant attribution can still miss inputs that drive the prediction, so invariance and deletion performance should each be checked.

### What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution
- arXiv 2611.23218v1 · v1 2026-11-17 18:57 UTC · cs.CL, cs.LG
- Authors: S. M Seefat Alam
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.23218
- arXiv comment: 18 pages, 13 tables. Under review at ACL Rolling Review (October 2026 cycle)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Methods that localise social bias in large language models to individual attention heads and remove it by ablation are validated by their effect on a fairness metric, never by evidence that the statistic selecting the heads measures bias. We audit this on Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct. The head map correlates at $ρ= -0.950$ and $-0.768$ with a label-blind response-length map, apparently identifying a surface confound. An intervention that breaks the length-label coupling rejects this reading: with the prompt held fixed, response length explains 1% of the statistic's variance. What does explain it is prompt identity, at 64% of variance, in an ordering that is not monotonic in length. Within any fixed prompt the fairness label, response length and the presence of a protected-group token are collinear at $φ= 0.95$, partly by definition of the labelling rule, so no observational analysis can attribute the map to any of them, and no method in this family performs an experiment that could. The substantive claims fail independently: bias selectivity is not late-layer-concentrated on either model under either reference reading, and no head set we tested reduces the unfairness rate when ablated. Its complement, scored on the opposite label, reliably destroys refusal behaviour ($p = 2.7\times10^{-5}$), demonstrating that the pipeline detects effects at this scale.

### ALOHA Lightning: Learning Fast and Precise Manipulation
- arXiv 2611.21919v1 · v1 2026-11-16 21:31 UTC · cs.RO, cs.AI, cs.LG, eess.SY
- Authors: John Hua Yao. Qi Wu, Yihuai Gao, Chelsea Finn, Zipeng Fu
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.21919
- arXiv comment: Project website: https://flash-aloha.github.io/
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Learning from human demonstrations has enabled robots to acquire a wide range of manipulation skills, but learned policies typically execute far slower than ordinary humans. This speed gap is mainly due to lack of an interface for collecting demonstration data at high speed, and the difficulty in training policies that can robustly execute high-speed motions. In this paper, we present ALOHA Lightning (Flash ALOHA), a system for learning fast and precise robotic manipulation. Our system uses kinesthetic teaching to intuitively collect near-human-speed demonstrations on a backdrivable bimanual platform, yielding natural and fast trajectories. We also present a learning pipeline that enables smooth high-speed execution through test-time action smoothing and aligns the visual data distribution between data collection and deployment with masking. Given 50 demonstrations for each task, ALOHA Lightning autonomously completes bimanual tasks such as ball tossing and catching, folding shorts, battery insertion, and bussing tables for over 80% success rates while close to human speed. Project website: https://flash-aloha.github.io/

### TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation
- arXiv 2611.23143 · v1 2026-11-17 00:00 UTC · 
- Authors: Haosong Peng, Xiangyang Liu, Zhengshen Zhang, Yunfeng Fan et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.23143
- Full text: data/fulltext/2611.23143.txt

> Robot manipulation videos provide a rich visual experience, yet recovering robot action and gripper-state annotations from RGB observations still remains challenging. Using the embodiment-agnostic tool-center-point (TCP) pose as the action space, we present TCP4D, a unified model in which a shared 4D scene representation both tracks observed TCP motion and generates future TCP trajectories. Given a monocular video and initial 2D TCP queries, the tracker directly recovers metric TCP poses in SE(3) and gripper states alongside scene geometry and camera parameters. The generator samples local features from the same 4D representation along the recovered TCP tracks, then combines them with robot observations and language instructions to predict future TCP states. Our new cross-embodiment augmentation pipeline converts existing RGB videos into demonstrations for alternative embodiments by retargeting the recovered motion and synthesizing the corresponding observations, without recorded source-robot states. Experiments show that the tracker achieves absolute trajectory errors of 7.60 and 16.07 mm on DROID and RoboLab and adapts to a new embodiment with only ten demonstrations. The generator achieves 69.19% mean success on RoboTwin and outperforms well-established policy models on two real-world tasks, while joint training on source and augmented demonstrations improves target-robot success by 41.5% over augmented-only training.

### RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't
- arXiv 2611.22179v1 · v1 2026-11-17 04:16 UTC · cs.AI
- Authors: Jingyu Liu, Zongze Li, Zach Xu, Zhanhui Zhou et al.
- Topics: RAG (generic), Brand/product recommendation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.22179
- arXiv comment: 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Main Conference
- Full text: data/fulltext/2611.22179.txt

> Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a deliberately minimal RAG memory with chained observation notes, hybrid BM25 with cosine retrieval, and chronological rendering, which reaches parity within bootstrap CI with the prior SOTA on LongMemEval-S and BEAM, and beats the best memory baseline on EverMemBench by 5.7-6.3 points at matched reader. It runs at ~5-7K reader-prompt tokens per query, using a single LLM call for each ingestion or query. We argue that this parity is itself the result: standard benchmarks score what memory retrieves, not what memory enables when the agent acts. To test the latter, we introduce five adversarial probes (Rule Application +-, Pattern Induction Style / Procedural, Dynamic Multiturn) judged at generation time by a cross vendor verification chain, where each query can only be solved by applying a remembered rule or pattern it never mentions. Across 5 probes x 20 scenarios, no architecture wins universally: atomic fact extractors (LangMem) win rule application, while BRIDGE's block-summary memory wins pattern induction. This result holds across four domains, three graders, and three reader families. Each design fails where the other wins, for reasons a recall benchmark cannot see: atomic-fact extractors discard the form a demonstrated pattern takes, while block-summary memory retrieves the rule but the reader does not act on it, a gap that presenting the rule more prominently largely closes. What separates memory designs is not what they retrieve but what they enable an agent to do, and that is what agentic memory should be evaluated on.

### Where Does Hindsight Enter Clinical Agent Benchmarks? An Audit of Simulators and Case Construction
- arXiv 2611.22241v1 · v1 2026-11-17 05:43 UTC · cs.CL
- Authors: Meilu Zhu, Xiaohan Li, Axiu Mao
- Topics: Clicks & measurement · score 6 · found via cs.CL
- Link: https://arxiv.org/abs/2611.22241
- arXiv comment: 8 pages main text, 20 pages in total, 6 figures, 11 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Benchmarks for LLM diagnostic agents are built from retrospective records: the case an agent reads is rewritten from discharge summaries, and unrecorded test results are generated by a simulator that often sees the final diagnosis. HindAudit separates three hindsight channels (the diagnosis given to the simulator, the retrospective context it conditions on, and the agent-facing case text) and measures each with judges trained only on real data. On 27,489 emergency admissions from MIMIC-IV, five registered tests found no leakage into simulated laboratory results: providing the diagnosis to five simulators had a negligible effect, and prompted gatekeepers diluted the diagnostic signal, although exploratory results suggest they can raise agent scores. The largest effect lay in the case text. Against a presentation-time reconstruction from triage records, benchmark-style summaries raised the zero-shot accuracy of four LLMs from 25.4% to 39.7% and discharge histories to 45.3%, and raised six interactive agents' scores while barely changing their ranking. The exploratory gap was reproduced in a registered replication on held-out patients. Masking diagnosis names left it unchanged. Because MIMIC lacks a contemporaneous bedside history, the gap is an upper bound on hindsight. We report all registered outcomes and recommend construction practices.

### A Full-Ledger Counterfactual Audit of Adaptive Reasoning
- arXiv 2611.22778v1 · v1 2026-11-17 13:44 UTC · cs.AI, cs.CL
- Authors: Xiaopeng Chu, Wenzheng Kong, Wei Liu, Wenyi Zhang
- Topics: Clicks & measurement · score 6 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.22778
- arXiv comment: Accepted to EACL 2027 (Main Conference)
- Full text: data/fulltext/2611.22778.txt

> Adaptive reasoning must decide whether to answer now or spend more compute. Predicting that the current answer is wrong does not establish whether further reasoning will improve it. We introduce the Full-Ledger Counterfactual Value Audit (FLCVA), which compares an immediate answer with four fixed-length continuations from the same frozen prefix under one answer procedure and accounts for the cost of every signal used by a policy. On GSM8K and MATH-500, a random 256-token continuation recovers a wrong answer in 26.6% of Qwen3-8B cases and 18.9% of DeepSeek-R1-Distill-Qwen-7B cases, while damaging a correct answer in 1.4% and 1.9%. Correctness labels from independently sampled continuations predict a separate continuation's outcome in both primary models. In offline replay, using these labels to allocate compute improves performance on DeepSeek; the Qwen3 gain remains inconclusive. Under full cost accounting, the tested lightweight, myopic controllers mainly recognize current errors and add little continuation-specific value beyond that shortcut. A Llama-8B replication and action/cost ablations examine the robustness of these findings. FLCVA separates measuring local continuation value, predicting it from observable signals, and using those predictions to allocate computation.

### Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate
- arXiv 2611.22904v1 · v1 2026-11-17 15:08 UTC · cs.LG, cs.CR
- Authors: Adnan Malkani
- Topics: Clicks & measurement, Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.22904
- arXiv comment: 12 pages, 7 figures, 6 tables. Code: https://github.com/adnanmalkani/byzantine-fl-bench
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Clinical federated learning (FL) collaborations typically connect only three to six hospitals, yet Byzantine-robust aggregation rules are designed and benchmarked on synthetic partitions across dozens of equal-sized clients. We conduct an empirical audit of eight standard aggregation rules: FedAvg, coordinate-wise median, trimmed mean, Krum, Multi-Krum, Bulyan, geometric median (GeoMed), and Centered Clipping (CC). We evaluate both unweighted and sample-size-weighted variants across three cross-silo medical datasets from the FLamby benchmark: Fed-Heart-Disease ($n = 4$ hospitals), Fed-TCGA-BRCA ($n = 6$ regions), and Fed-ISIC2019 ($n = 6$ centres). We execute 54,214 training runs across enumerated attacker coalitions ($f \in \{1, 2\}$) paired with exact-twin leave-out controls that decompose performance drops into honest data loss versus adversarial attack damage. We report three findings. First, client-count validity checks fail to capture breakdown in skewed medical consortia: while $n = 6, f = 1$ satisfies every count condition except Bulyan's, assigning sample-size weights turns median and GeoMed into a clean-model dictatorship whenever a single hospital holds more than half the training data, and causes weighted median, GeoMed, and CC to collapse when that dominant centre attacks. Second, exact-twin leave-out controls reveal that when the largest hospital attacks, the apparent failure of count-based robust rules is predominantly caused by the loss of honest training data (7.5 to 10.4 points on ISIC) rather than adversarial perturbation (2.3 to 3.8 points on ISIC). Conversely, weight-dependent rules suffer large true attack damage (16.1 to 25.1 points on ISIC). Third, unweighted robust rules consistently discount whichever institution generates the most atypical parameter updates, penalizing the smallest hospital on Heart but penalizing larger institutions on TCGA and ISIC.

### From Relevance to Utility: Rubric Alignment in Yuanbao Search
- arXiv 2611.22503v1 · v1 2026-11-17 10:00 UTC · cs.IR
- Authors: Yu Lu, Lixin Zou, Yangqi Chen, Hui Xu et al.
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22503
- arXiv comment: 10 pages, 5 figures, 5 tables, accepted at KDD 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Agentic search demands that a search engine move beyond per document relevance ranking to assemble document sets optimized for downstream LLM reasoning. Prior work addresses this either by improving individual pipeline stages in isolation or by applying RL based selection on top of relevance trained upstream modules, leaving the full stack unaligned to utility for reasoning. We propose rubric aligned search, a framework that unifies the traditional search pipeline under a single supervision surface. For each query, we derive a rubric from coarse to fine, specifying weighted positive criteria that the document set must satisfy and negative criteria that it must avoid. From this rubric we derive two training signals. First, a lightweight labeler distills rubric grounded judgments into per document utility labels, which supervise a contrastive dual encoder for retrieval and a multi task ranker trained with four rubric aligned scoring heads. Second, a rubric conditioned evaluator produces a set level reward that drives a dual branch RL selector, combining GRPO with best rollout distillation to resolve credit assignment in subset optimization. Deployed in Yuanbao Search, the pipeline improves end to end answer quality by 8.52% over the online production baseline.

### Teaching Language Models to Narrow Boolean Patent Searches from Search Feedback
- arXiv 2611.22270v1 · v1 2026-11-17 06:17 UTC · cs.IR, cs.AI, cs.CL
- Authors: Seiya Kawano, Koji Marusaki, Hirofumi Nonaka, Koichiro Yoshino
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22270
- arXiv comment: 13 pages, 3 figures, 3 tables. Accepted at NLPIR 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Patent prior-art searchers issue Boolean queries line by line, broadening to find relevant documents and narrowing until candidates can be screened. We distill 38,397 Japan Patent Office search reports into executable expert strategies, re-execute them, and evaluate generated strategies by citation recall and the smallest set containing each citation. Prompted models write valid, high-recall strategies but leave citations in sets too large to screen. We adapt a generator offline from scored rollouts in two forms: strategy-level learning from a screening-aware strategy score, and line-level learning from citation-preserving narrowing credit, which upweights the query lines keeping a found citation in a smaller set. On shared rollouts, line-level credit outperforms strategy-level scores on screening measures; iterated, it cuts the median citation-containing set from 768 to under 50 and places more citations in sets under 100 documents than experts, at lower recall. Strategy-level preference learning reaches near-complete recall; the two forms are complementary.

### MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval with Multi-Category Solutions
- arXiv 2611.22509v1 · v1 2026-11-17 10:05 UTC · cs.IR
- Authors: Qiang Li, Xuan Lu, Jian Ruan, Manxi Lin et al.
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22509
- arXiv comment: 14 pages, 8 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Real-world e-commerce queries often express user intent without naming a target product, and a single intent may be fulfilled by products from multiple categories. However, existing multimodal retrieval benchmarks typically assume a relatively well-defined target, leaving retrieval for intents with multi-category solutions less explored. To fill this gap, we introduce MIPR, a benchmark for Multimodal Intent-to-Product Retrieval comprising 3,522 multimodal queries and a shared corpus of 30,731 products. MIPR features reasoning-intensive retrieval, multi-category solutions, and fine-grained relevance labels. Experiments show that the best embedding-based retriever achieves 49.23% nDCG@10 on the full query set, and 55.86% solution-category recall@10 on queries with multiple solution categories. Reranking improves these scores to 60.11% and 67.00%, respectively, yet substantial gaps to the candidate-pool oracle remain. These results establish MIPR as a challenging and diagnostic benchmark for evaluating multimodal intent-to-product retrieval. The data and code are publicly available at https://huggingface.co/datasets/leequeue/MIPR.

### Learning Cross-Domain Media Similarity from Amazon Reviews
- arXiv 2611.22756v1 · v1 2026-11-17 13:24 UTC · cs.IR
- Authors: Gabrielly Xavier dos Santos, Lucas Dias Cler, Luciana Fujii Pontello, Olga Goussevskaia
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22756
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Collaborative filtering is a basic foundation of many recommendation algorithms. It works by analyzing a user's history and then suggesting items similar to those in that history. This method typically relies on user data to compute item similarity, data that is widely available to commercial systems but is usually sparse or inaccessible for independent systems and research, especially across multiple media domains. In this work, we propose a method to generalize similarity information between items using supervised learning. As input to our model, we use semantic and temporal features extracted from Amazon product reviews, which are publicly available. As the training target, we use item (product) co-occurrence in the reviewing history of Amazon customers. We evaluate the quality of the predicted similarities across two media domains: books and movies. Experimental results demonstrate the robustness of our methodology, yielding positive outcomes in zero-shot cross-domain transfer tasks. Furthermore, feature attribution analysis reveals a structural shift in how feature groups are utilized across setups: intra-domain models rely heavily on linguistic semantics, whereas cross-domain environments pivot toward behavioral popularity cues. Incorporating even limited target-domain context during training bridges this domain sparsity gap, significantly enhancing framework generalization.

### GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation
- arXiv 2611.22274v1 · v1 2026-11-17 06:20 UTC · cs.IR, cs.CR
- Authors: Shiyi Yang, Xinshu Li, Chen Wang, Xiwei Xu et al.
- Topics: Manipulation · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22274
- arXiv comment: Accepted by WSDM 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning. In contrast, in LLM-based RSs, textual information becomes the primary medium for recommendation generation through semantic understanding and reasoning. This shift fundamentally changes the attack surface, making promotion-driven manipulations more feasible, effective, and harder to detect. However, effectively detecting such attacks remains largely unexplored. To fill this gap, we present the first systematic study on detecting promotion-driven attacks against LLM-based RSs, aiming to safeguard next-generation recommendation platforms. Specifically, we propose GuardAgent, a novel LLM-powered agentic detection framework that operates through a loop of Perception, Action, Reflection and Memory. In contrast to conventional LLM-based detectors that function in a static, one-off, and opaque fashion, GuardAgent continually learns and self-evolves to adapt to unseen threat patterns while generating explainable reasoning traces and outcomes. Extensive experiments on real-world datasets demonstrate that GuardAgent achieves state-of-the-art generalization performance, laying the foundation for robust and trustworthy recommendation in practical settings.

### NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval
- arXiv 2611.22353v1 · v1 2026-11-17 08:04 UTC · cs.IR, cs.CL
- Authors: Ankit Gupta
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.22353
- arXiv comment: Accepted to EACL 2027 (Main Conference). 15 pages
- Full text: data/fulltext/2611.22353.txt

> Dense retrieval is central to modern search, question answering, and retrieval-augmented generation, where high similarity is often treated as evidence of semantic relevance. We examine how far this assumption can be stressed. NONSENSE is a black-box sparse-edit probe that constructs visibly non-semantic strings while forbidding query-term copying, optimizing only the dense similarity between a query and the string. Across five BEIR-style datasets and three popular single-vector retrievers, these strings frequently outscore the retriever's own best judged query-relevant passage (QRP), and often rank first in the full corpus. The result indicates a semanticity gap in the evaluated dense retrievers: nearest-neighbor status can be separated from passage-like meaning. These findings highlight the importance of evaluating dense retrievers not only by whether they retrieve relevant documents, but also by how reliably their similarity scores reflect semantic evidence.

## Other new cs.IR papers, title only (12)
- Urban Representation Learning for Identifying Potential Disparities in Crime Reporting — https://arxiv.org/abs/2611.21825
- Complexity and precision in quantum associative retrieval — https://arxiv.org/abs/2611.21941
- Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual LLM Inference on NVIDIA Blackwell — https://arxiv.org/abs/2611.21974
- SIMQ: A Single Graph-based Index for Multi-Vector Query — https://arxiv.org/abs/2611.22079
- Cluster-Guided Decoding with Trust-Region Constraints for Personalized Recommendation — https://arxiv.org/abs/2611.22163
- RICoT: Recurrent Interleaved Chain-of-Thought for Page Stream Segmentation — https://arxiv.org/abs/2611.22382
- Deal With It: On Better Schedules for Listwise Reranking — https://arxiv.org/abs/2611.22392
- More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation — https://arxiv.org/abs/2611.22410
- Better Rankers, Worse Retrievers: The Hidden Cost of RL Post-Training in Generative Recommendation — https://arxiv.org/abs/2611.22838
- Music Similarity Learning in Sparse Latin Scenarios — https://arxiv.org/abs/2611.22846
- When the tail is earned by its companions: measuring label dependence in long-tailed multi-label classification — https://arxiv.org/abs/2611.22859
- CARE: Conversational Affective Response Retrieval for Internet Memes — https://arxiv.org/abs/2611.23005

## Already listed on an earlier day, still inside the look-back window (72)
- Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning — https://arxiv.org/abs/2611.20045 (score 23)
- User First Intelligence: Three Measurements of Search and AI-Answer Analytics (SEO and GEO/AEO), and a Knowledge-Graph Framework for Query Discovery Beyond Search Volume — https://arxiv.org/abs/2611.19655 (score 18)
- Data Attribution Should Steer Pretraining — https://arxiv.org/abs/2611.19698 (score 13)
- Beyond Bot Labels: Retrospective Consequence-Grounded Ranking of Attributed Cache Harm in E-Commerce Logs — https://arxiv.org/abs/2611.18027 (score 12)
- Explainable Federated Learning via Global-Local Attribution Alignment — https://arxiv.org/abs/2611.20445 (score 11)
- Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent — https://arxiv.org/abs/2611.17939 (score 10)
- DetouR: Plugging Association Routes into Search Agents for Multi-hop Question Answering — https://arxiv.org/abs/2611.19967 (score 10)
- EchoSpec: Training Search Agents to Weigh Evidence Above Echoes — https://arxiv.org/abs/2611.20034 (score 10)
- DOCKET: A Pluralistic Benchmark for Evaluating AI-Assisted Policy Feedback in U.S. Rulemaking — https://arxiv.org/abs/2611.17914 (score 9)
- Towards Explainable Sleep Stage Classification using Single-Channel Electroencephalogram — https://arxiv.org/abs/2611.18434 (score 9)
- WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents — https://arxiv.org/abs/2611.17955 (score 8)
- From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States — https://arxiv.org/abs/2611.18272 (score 8)
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
- Interactive deep-learning based interface for brain tumour segmentation — https://arxiv.org/abs/2611.17983 (score 7)
- Contagious Fingerprints: When LLMs Inherit Another Model's Identity — https://arxiv.org/abs/2611.18104 (score 7)
- Label-Free Detection of Structural Bias in LLM-Based Recommender Systems via Randomized Paraphrasing: The Case of Verbosity — https://arxiv.org/abs/2611.18878 (score 7)
- SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection — https://arxiv.org/abs/2611.07222 (score 6)
- An In-Silico Audit of Topographic Organization in a Multimodal Brain-Response Model — https://arxiv.org/abs/2611.18105 (score 6)
- Toward On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset: A Preliminary Study — https://arxiv.org/abs/2611.18438 (score 6)
- Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination — https://arxiv.org/abs/2611.18514 (score 6)
- NI-ACT: A Neural Intent Interface for Brain-Embodied Manipulation — https://arxiv.org/abs/2611.19332 (score 6)
- VoiceGuard: An Audio-Native LLM-VLA Pipeline for Wheelchair-Mounted Assistive Manipulation — https://arxiv.org/abs/2611.19984 (score 6)
- Can AI Judge You? An Empirical Audit of Deployment Readiness in LLM-assisted Hiring Systems — https://arxiv.org/abs/2611.20140 (score 6)
- AsymEEF: Bimanual Manipulation with Asymmetric End Effectors — https://arxiv.org/abs/2611.20557 (score 6)
- Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models — https://arxiv.org/abs/2611.20901 (score 6)
- Language-model agents' beliefs can be manipulated via truthful evidence in open channel — https://arxiv.org/abs/2611.21235 (score 6)
- Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models — https://arxiv.org/abs/2611.21517 (score 6)
- Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web — https://arxiv.org/abs/2611.19900 (score 5)
- StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval — https://arxiv.org/abs/2611.18516 (score 4)
- TokenFormer V2: Breaking the Resolution-Complexity Dilemma in Unified Recommendation — https://arxiv.org/abs/2611.19074 (score 4)
- CLEAR: Legible and Steerable Recommendation via Grounded Natural-Language Interests — https://arxiv.org/abs/2611.19110 (score 4)
- Reflection Is Not Always Worth It: Budgeted Reflection Allocation for Recommendation Agents — https://arxiv.org/abs/2611.19847 (score 4)
- How did data sharing evolve in the decade since the FAIR Principles? — https://arxiv.org/abs/2611.20319 (score 4)
- Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First — https://arxiv.org/abs/2611.20378 (score 4)
- What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially Private Item Counts — https://arxiv.org/abs/2611.20388 (score 4)
- Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates — https://arxiv.org/abs/2611.20837 (score 4)
- When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents — https://arxiv.org/abs/2611.21577 (score 4)
