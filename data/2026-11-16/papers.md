# Paper candidates — 2026-11-16 (IST)

Generated 2026-11-16 07:22 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 19 new topic matches · 6 other new cs.IR · 46 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (19), highest score first

### Beyond Bot Labels: Retrospective Consequence-Grounded Ranking of Attributed Cache Harm in E-Commerce Logs
- arXiv 2611.18027v1 · v1 2026-11-13 10:53 UTC · cs.CR, cs.LG, cs.NI
- Authors: Jisoo Kim, Youngwoo Seo, Seonghoon Jeong
- Topics: Citation & source selection, Brand/product recommendation · score 12 · found via cs.CR
- Link: https://arxiv.org/abs/2611.18027
- arXiv comment: 11 pages, 4 figures, 7 tables. Accepted to appear in Proc. of the 2026 IEEE International Conference on Big Data (IEEE BigData 2026), Phoenix, AZ, USA. This is the author's accepted manuscript
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web caches reduce origin load and latency, but automated traffic can either warm them or evict objects shoppers reuse, lowering the cache hit ratio (CHR). Existing bot defenses generally infer automation from User-Agent (UA) strings or behavior rather than identify sessions that impose cross-session cache harm. We instead formulate the task as ranking sessions by eviction damage and propose consequence-grounded session ranking. A single chronological replay attributes each eviction-induced miss by a protected shopping session (a victim) to the session whose insertion last evicted the object. A behavioral model predicts the target from session behavior alone. Selected sessions bypass the cache but remain origin-served. In a controlled check of 539 non-victim sessions selected across harm levels, attribution order tracks victim-hit changes after removal (Spearman correlation 0.80). On a 12.7-million-request real trace, the top 1% of sessions carry 48.8% of attributed harm. Sessions without bot tags contribute 49.1% of this tier's harm. At the 20% request-volume target, the default conditional CHR difference reaches 93% of the UA baseline, which selects 47 times as many sessions. Six training seeds show little variation. This comparison conditions on the victims that remain, so we also report victim bypass. Local replay and retraining on a second store reproduce harm concentration and a top tier dominated by sessions without bot tags. These results establish attributed cross-session harm as an outcome-based target for retrospective cache audits and selective intervention design.

### Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent
- arXiv 2611.17939v1 · v1 2026-11-13 09:22 UTC · cs.AI, cs.CL
- Authors: Cosimo Galeone, Anna Ettorre, Ginevra Mariani, Minsu Park et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.17939
- arXiv comment: 9 pages. Accepted as an oral presentation at the AI4F workshop, ICAIF 2026, Milan
- Full text: data/fulltext/2611.17939.txt

> Can you trust a finance agent you did not build? We take the reference agent shipped with the Vals Finance Agent Benchmark v2, leave it untuned, and ask four questions a leaderboard score does not answer. Is the score stable? Seven identical runs on 18 questions pass between 105 and 123 of 149 rubric criteria, and the bill varies by up to 17%. When the agent fails, who owns the fix? We classify 20 failed trajectories, from three runs of nine held-out questions, by the layer whose owner would remedy them, under a taxonomy frozen in advance: 13 belong to the agent's instructions, 3 to its tools, 4 to the model, none to its data. Can that diagnosis be trusted? Four blind readers from three model families, given only the traces, name the same fault as our LLM analyzer in 94% of cases, the rate at which they agree with one another (93%). Can a change be trusted? An optimization loop reads the traces, makes one targeted change per round and keeps it only if it clears a fixed threshold. Under a cost objective its final configuration costs 0.34x the baseline on the held-out questions (95% CI [0.22, 0.58]) at accuracy within noise. Under an accuracy objective it gains 14 points on the development questions and 1.5 on the held-out ones (CI [-5.3, +7.2]). Judged against the measured run-to-run noise, under a rule written before the test was opened, the first is a real saving and the second is not. This is a case study of one agent and nine test questions, not a general result.

### AI-Voyager: A Public-Interest System for Human-AI Civic Reasoning to Contest and Shape the Rules That Govern AI
- arXiv 2611.17564v1 · v1 2026-11-12 22:38 UTC · cs.AI, cs.CL, cs.HC
- Authors: Snehalkumar `Neil' S. Gaikwad, Dhruv Dixit, Bryen Alvarez, Pratik Patekar et al.
- Topics: Citation & source selection, Query fan-out · score 9 · found via cs.AI, cs.CL, cs.HC
- Link: https://arxiv.org/abs/2611.17564
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Governments are writing rules for artificial intelligence that decide what counts as an automated decision or a harm, often before the people they affect have a chance to question them. We introduce AI-Voyager, a public-interest system for human-AI civic reasoning, in which people and AI work together to understand, contest and shape the rules that govern AI. A resident can find their city's rules on AI in hiring or upload their country's AI strategy, read it as an affected worker would, open the passage behind any answer, and draft a revision. Its architecture turns 3,653 governance documents from city, state, federal and national governments into passages that keep their page and edition, and retrieves evidence through bounded agentic search that verifies each statement. On 360 new questions that require finding the relevant documents, it reached 83.0% macro recall, against 80.5% for the strongest baseline, 73.7% without iterative search and 99.1% on a benchmark with fixed documents. In a study with 24 participants new to two AI bills, most proposed changes asked how provisions would apply. Participants chose lenses for the kind of explanation they wanted, and citations signaled grounding but rarely led them to check the source. By binding AI assistance to the exact text of public documents, this work introduces a grammar of operations and a design space that inform how such systems are designed and evaluated, and how people take part in governing AI.

### DOCKET: A Pluralistic Benchmark for Evaluating AI-Assisted Policy Feedback in U.S. Rulemaking
- arXiv 2611.17914v1 · v1 2026-11-13 08:55 UTC · cs.CY
- Authors: Alexander Spangher, Charlotte Peale, Sílvia Casacuberta, Victor Y. Wu et al.
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.CY
- Link: https://arxiv.org/abs/2611.17914
- Full text: data/fulltext/2611.17914.txt

> As AI models advance and impact deliberative democracies, there is a growing need to assess their support of pluralistic viewpoints. Most pluralism benchmarks are insufficient for this: they are not grounded in diversity (i.e., stakeholders across different frames, skills and needs), quality (i.e., rigorous and technical debates), and impact (i.e., invested deliberators and real-world outcomes). To address this, we first (i) curate DOCKET, the most comprehensive dataset of the U.S. Federal Notice & Comment process to date. DOCKET consists of 42.3M public comments on 22,400 regulations across 44 government agencies between 2016 and 2026 and contains millions of policy debates; we link public comments to particular policy items proposed by regulators to track the public's attention and the responsiveness of regulators to public input. (ii) Next, we demonstrate the pluralistic utility of DOCKET - we show that public commenters have a wide breadth of perspectives with significant depth in policy expertise and that regulators are often responsive. (iii) Finally, we present DOCKETBench, the first systematic evaluation of LLMs' ability to represent human policy perspectives in federal rulemaking. Only 18-30% of LLM-generated feedback aligns with real human comments. LLMs critique proposals broadly but generally, lacking the specific grounding, citations, and lived-experience arguments that humans bring to bear; in addition, most models we test systematically agree with government perspectives (overlapping with up to 68% of their claims) and agree least with labor unions (as little as 26% of their claims), demonstrating a fundamental skew in perspectives that even tools like persona modeling do not solve. Taken together, we reveal fundamental gaps in how language models navigate real policy issues, and DOCKETBench serves as a testbed for closing those gaps in a crucial real-world domain.

### Towards Explainable Sleep Stage Classification using Single-Channel Electroencephalogram
- arXiv 2611.18434v1 · v1 2026-11-13 17:13 UTC · cs.AI, eess.SP
- Authors: Gurinder Kaur Sandhu, Jude Koenig, Ankita Shukla, Shruti Kshirsagar
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.AI
- Link: https://arxiv.org/abs/2611.18434
- arXiv comment: 8 pages, 4 figures. Accepted at AgIA4BioHealth Workshop, IEEE BIBM 2026, Dallas, Texas, December 1-4, 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Automated sleep staging has achieved strong bench- mark accuracy; however, clinical adoption remains limited due to a lack of interpretability. In this work, we fill the research gap by extending the SleepXAI sleep staging framework to systematically compare five different XAI methods. Further, attribution fidelity is evaluated using Spearman rank correlation with AASM-defined EEG frequency bands, serving as clinically grounded reference signals. In this paper, we focus on single- channel Electroencephalogram (EEG), which is more amenable to practical clinical deployment compared to full polysomnography setups. Experiments are conducted on the Sleep-EDF benchmark dataset and the DREAMT dataset. In DREAMT, we stratified subjects based on OSA into four Apnea-Hypopnea Index (AHI) severity groups. We observed that the SleepXAI model achieves strong classification performance on both datasets. Among the evaluated methods, Integrated Gradients (IG) consistently achieves the highest mean attribution fidelity across all five sleep stages on Sleep-EDF and across all AHI groups on DREAMT, outperforming all other evaluated methods under the Spearman rank correlation metric. These findings highlight the importance of attribution method selection as a key factor for ensuring reliable and clinically interpretable automated sleep staging systems.

### Evaluating the Robustness of PRNU Source-Camera Attribution to the Fingerprint-Copy Attack: An Open Toolkit with Triangle-Test Detection
- arXiv 2611.17747v1 · v1 2026-11-13 05:03 UTC · cs.CR
- Authors: Zeno J. M. H. Geradts
- Topics: Citation & source selection · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.17747
- arXiv comment: 8 pages, 3 figures. Toolkit: https://github.com/geradts1/forensicsd
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Photo-Response Non-Uniformity (PRNU) is the de facto standard trace for sensor-level source-camera attribution, and a high Peak-to-Correlation-Energy (PCE) between a questioned image and a camera reference fingerprint is routinely treated as strong evidence of common origin. The fingerprint-copy attack of Goljan, Fridrich and Chen (2011) shows that this signal can be forged: an adversary who estimates a target camera's fingerprint from that camera's publicly available images can inject a scaled copy of it into an unrelated photograph, producing a forgery that clears a PCE decision threshold despite never having been taken by the target device. We present prnucf, an open, auditable toolkit that pairs a reference implementation of the (additive) fingerprint-copy attack with the triangle-test detector and a cohort-calibrated decision procedure, so that practitioners can quantify how fragile a PRNU attribution is against this attack on their own pipelines. On a controlled multi-camera Monte-Carlo benchmark the attack reaches an arbitrary target PCE at a mean PSNR of 59.2 dB (visually lossless), yet the triangle test separates forgeries from innocent images with an area under the ROC curve of 0.999, detecting every forgery at a cohort-calibrated 5% false-positive operating point. We discuss why a fixed significance cut-off is not safe in casework, the limitations of synthetic validation, and the open problem of extending explainable detection to the modern, GAN-based generation of fingerprint-transfer attacks. The toolkit is released under the MIT license with an explicit dual-use statement.

### Creative Product Design under Brand Image Constraints
- arXiv 2611.17762v1 · v1 2026-11-13 05:17 UTC · cs.CV, cs.AI, cs.GR
- Authors: Takeshi Onishi, Hiroya Makino, Takahiro Yamaguchi, Hiroyuki Sakai
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.17762
- Full text: data/fulltext/2611.17762.txt

> Industrial design requires creative visual exploration while satisfying constraints that are often product-specific and implicit. Existing text-to-image (T2I) approaches can generate creative designs through concept blending or multi-agent self-enhancement, but they provide limited mechanisms for ensuring that generated designs remain consistent with such constraints. We focus on brand image as a representative design constraint and propose a framework for brand-aware redesign generation. Given a product name, the framework constructs a brand image survey report that summarizes product and market information, derives a creative direction from the report, and integrates this direction into a self-enhancement loop in which generated images are critiqued and prompts are revised. We evaluate the framework on 50 redesign tasks across five product categories, comparing it with Naive T2I, IP-Adapter/IT-Blender, and unconstrained self-enhancement under the same T2I backbone. By a VLM-as-Judge protocol to measure creativity and brand identifiability, the proposed framework achieves a more favorable trade-off between the two objectives, with particularly clear gains in highly constrained categories such as automotive and motorcycle, where the plausible design space is relatively limited compared with that of other product categories. These results suggest that dynamically eliciting and textualizing brand image can guide creative product design generation under brand image constraints.

### G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands
- arXiv 2611.17814v1 · v1 2026-11-13 06:53 UTC · cs.AI, cs.CL
- Authors: Yuechun Yu, Wenzheng Kong, Xiaofeng Mao, Jin Zhang
- Topics: Brand/product recommendation · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.17814
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> With the rapid advancement of Large Language Models (LLMs), an increasing number of users are turning to LLM-powered agents for conversational shopping in e-commerce. However, the user needs continue to change as new product categories, procurement scenarios, and feature requests emerge. At the same time, the product's execution harness-including its tools, skills, and operating procedures-continues to evolve to support increasingly sophisticated interactions. These changes create two practical challenges: 1) Demand drift alters the distribution, intent, and complexity of user requests, causing a model trained once to fall behind; 2) Harness evolution requires the model to use newly introduced capabilities correctly without losing behavior that users already rely on. Periodic manual retraining is too delayed and labor-intensive for this setting. To address these challenges, we present G-CAST, a governed continual self-training system that converts daily production evidence under evolving demand and capability contracts into reward-routed, entropy-prioritized training data and governed reward evolution. Governed checkpoint transition under cumulative evaluation controls each model update, enabling the agent to learn newly introduced behaviors without sacrificing previously accepted capabilities. Experiments on a real production e-commerce agent show that G-CAST achieves stronger adaptation to newly introduced demand while better preserving previously accepted behavior compared with a strong autonomous post-training baseline. Ablations further show that both reward-routed, entropy-prioritized data orchestration and governed reward evolution are important to these gains. G-CAST is now deployed in Yuancai(http://cai.1688.com/), a B2B procurement agent on Alibaba's 1688 platform.

### WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents
- arXiv 2611.17955v1 · v1 2026-11-13 09:44 UTC · cs.AI, cs.CL, cs.LG
- Authors: Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù, Weijian Qi et al.
- Topics: Agents · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.17955
- arXiv comment: Accepted at NeurIPS 2026 E&D Track
- Full text: data/fulltext/2611.17955.txt

> Web agents powered by large language and vision-language models are increasingly applied to realistic browser work that spans heterogeneous applications, multimodal content, and stateful workflows. However, existing reproducible web-agent benchmarks cover only a small number of web applications drawn from a few software categories, and restrict modality to text and vision. Live benchmarks broaden site coverage but sacrifice reproducibility, since pages and data drift between runs. Moreover, existing benchmarks do not meaningfully evaluate whether agents can understand and use audio and video content embedded within web tasks. To address these gaps, we introduce WebArena-Pro, a benchmark comprising 300 tasks across 20 self-hosted web applications in six domain categories, spanning distinct interface conventions, workflows, and data models. Across the evaluated agents, the best performance is achieved by both Codex with GPT 6.1 Sol and Claude Code with Claude Opus 5.5 at 62.3%, followed by OpenCode with Kimi 3.1 Pro at 60.7%. The strongest GenericAgent configurations, Gemini 3.1 Pro omni and Gemma4 31B, both achieve 30.3%. Among reproducible, human-curated web agent benchmarks, WebArena-Pro provides the broadest application coverage and the most comprehensive multimodal support to date. The benchmark treats audio and video as core observations alongside text and vision, with dedicated actions for extracting information from each. WebArena-Pro runs each task in isolation and supports reproducible, parallel evaluation. Tasks are authored through a dedicated annotator interface, filtered by LLM-assisted triage, and finally validated by humans before release. Project page: https://webarena-pro.github.io

### From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States
- arXiv 2611.18272v1 · v1 2026-11-13 15:04 UTC · cs.AI, cs.CR
- Authors: Jonathan Pan, Yidi Yuan, Xin Wei Chia, Xinhui Su et al.
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.18272
- arXiv comment: 7 pages, 1 figure, 4 tables
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Existing memory forensics for machine learning systems typically targets static artifacts, such as model weights or prompt logs, rather than the transient computational states of a live inference process. This gap limits an examiner's ability to analyze the specific behavior of a running large language model (LLM) service that cannot be restarted or modified. We present a method for acquiring per-layer residual-stream activations from a live GPU process using a non-modifying debugger, without requiring prior knowledge of the model's architecture parameters or weights. The approach employs a general six-stage process with platform-specific adapters, utilizing either a PyTorch allocator clock or a kernel-launch clock to identify and read tensor allocations from video memory. We validate this acquisition on 33 open-source decoder-only models across nine architecture classes, demonstrating that the recovered bytes are byte-exact and usable for downstream analysis. As a use case, we apply linear probes trained on standard framework activations to the recovered states, successfully distinguishing refusal from compliance with an AUROC of 0.88 on held-out prompts. This work establishes that live, observational access to intermediate hidden states is feasible on named inference platforms, providing a new source of evidence for examining the operational behavior of deployed AI systems.

### RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG
- arXiv 2611.17788v1 · v1 2026-11-13 06:01 UTC · cs.CL
- Authors: Qigan Sun, Xudong Wang, Chaoning Zhang, Chenghao Li et al.
- Topics: RAG (generic), Query fan-out · score 7 · found via cs.CL
- Link: https://arxiv.org/abs/2611.17788
- arXiv comment: 12 pages, 6 figures, 8 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> In retrieval-augmented generation (RAG), query rewriting serves as a core interface that aligns user intent with external knowledge bases, and its effectiveness directly determines overall system performance. However, generative retrieval faces three critical challenges in real-world deployment: noisy retrieval feedback, the difficulty of jointly optimizing discrete prompt templates and continuous decoding-control parameters, and the limited generalization of static rewriting strategies under semantically complex scenarios. To address these issues, we propose RAG-FGO, a dynamic optimization framework for generative retrieval strategies. RAG-FGO formulates query rewriting as a non-differentiable black-box optimization problem in a mixed discrete-continuous space, and represents prompt templates and decoding parameters as adaptively optimizable query-rewriting agents. The framework performs global search to enable semantic jumps and structural reorganization that escape local optima, while applying local perturbations for fine-grained alignment and precise refinement. In addition, RAG-FGO introduces an elite-preserving memory pool that accumulates high-quality strategies across iterations, thereby mitigating the impact of stochasticity and noisy feedback on optimization stability. Experimental results on a diverse suite of benchmarks demonstrate the effectiveness and robustness of the proposed method, supporting its applicability to complex semantic retrieval tasks.

### Interactive deep-learning based interface for brain tumour segmentation
- arXiv 2611.17983v1 · v1 2026-11-13 10:09 UTC · cs.AI
- Authors: Enora Giffard, Pierre Jannin, John S H Baxter
- Topics: Brand/product recommendation, Clicks & measurement · score 7 · found via cs.AI
- Link: https://arxiv.org/abs/2611.17983
- Journal ref: SPIE Medical Imaging, Feb 2026, Vancouver, Canada. pp.17
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Brain tumour segmentation from MR images is an integral part of their treatment, either through surgical resection or radiotherapy. Both applications require a high degree of precision that can be difficult to ensure for all patients due to the high degree of variability in the size, shape, number, and location of these tumours. This leads to difficulties with their automatic segmentation via deep learning, which can display catastrophic segmentation errors when presented with images that differ, even subtly, in terms of the specific MR sequence used, which varies from vendor to vendor. This article presents a deep-learning-based interactive segmentation system that, while being fully automatic by default, has the capability of being easily corrected by human users, allowing them ensure sufficiently high brain tumour segmentation accuracy for all patients. This interface is evaluated both in terms of the accuracy of its automatic approach as well as its usability through a preliminary observational expert user study.

### Contagious Fingerprints: When LLMs Inherit Another Model's Identity
- arXiv 2611.18104v1 · v1 2026-11-13 12:32 UTC · cs.CL
- Authors: Zailong Tian
- Topics: Brand/product recommendation, Clicks & measurement · score 7 · found via cs.CL
- Link: https://arxiv.org/abs/2611.18104
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> The fingerprint by which a classifier recognizes the LLM behind a text is usually treated as a fixed property of the model. We show that it is contagious: a model that continues a conversation begun by another model inherits that model's fingerprint. This undermines audits of API relays, which can serve the first turns of a conversation with the model a customer pays for and silently hand the rest to a cheaper one. After such a handoff, detection of the substitute by a text classifier drops from 0.97 to 0.72 (DeepSeek replacing Claude Sonnet) and from 0.87 to 0.54 for a same-vendor downgrade (Haiku), and retraining on handoff data repairs only substitutes seen in training. Preregistered experiments trace the contagion to imitation of the history's style. History also moves a model away from its own fingerprint: active probes are not camouflaged, but when calibrated on fresh conversations they flag \emph{honest} models on long contexts at rates up to 1.00, and a standard MMD equality test rejects all nine models we test. Both failures come from comparing a history-dependent reply with a history-free reference. We propose \textsc{Lineup}, which samples references from the claimed model \emph{on the same history} and tests the audited reply by its rank among them. \textsc{Lineup} controls false positives by exchangeability and needs no fitted threshold or log-probabilities. With contemporaneous references on two closed models, its false-positive rate is 0.056 (preregistered bound 0.10), and it detects 0.81 of substitute sessions across six pairs after four audited turns.

### HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation
- arXiv 2611.16439 · v1 2026-11-12 00:00 UTC · 
- Authors: Shuai Yang, Fangyi Xu, Yishu Shen, Kecheng Zheng et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.16439
- Full text: data/fulltext/2611.16439.txt

> Learning whole-body mobile manipulation requires demonstrations that coordinate bimanual actions with locomotion across extended workspaces. However, existing interfaces trade off direct robot control, perception and action alignment, and natural operator mobility, making such demonstrations difficult to collect. We introduce HALO, a human-aligned data collection system for whole-body mobile manipulation. The system aligns the operator's perception and action space with the robot while preserving direct physical feedback and natural locomotion. Operators guide the robot end-effectors through kinesthetic teaching and move a low-resistance platform without the deployed mobile base while performing bimanual manipulation. This interface enables more natural whole-body demonstrations, but the close human-robot coupling introduces discrepancies between the demonstration and deployment settings. We address these discrepancies with deployment-aligned demonstration processing, which calibrates and temporally aligns platform motion with the deployed base response and masks and inpaints demonstrator hands in recorded observations. Compared with Mobile ALOHA and VR teleoperation, HALO enables up to 2.9x faster demonstration collection while maintaining comparable or higher success rates. Policies trained with HALO perform precise manipulation tasks, including zip-tie fastening, and achieve a 73.3% success rate on a six-stage long-horizon mobile manipulation task involving repeated coordinated base and arm motion. Project page: https://robbyant-research.github.io/Lingbot-ALOHA/

### An In-Silico Audit of Topographic Organization in a Multimodal Brain-Response Model
- arXiv 2611.18105v1 · v1 2026-11-13 12:32 UTC · q-bio.NC, cs.AI
- Authors: Jakub Strawa
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.18105
- arXiv comment: 12 pages, 5 figures, 4 tables. Code and stimuli: https://github.com/jakubstrawa1/audit-multimodal-brain-response
- Full text: data/fulltext/2611.18105.txt

> TRIBE v2 (d'Ascoli et al., 2026) predicts fMRI responses across the cortical surface from video, audio and text. Its authors validated it with category-selective localizers (faces, places, bodies, words) and language contrasts, but not with the classic topographic organization of sensory cortex: retinotopy, tonotopy, and motion selectivity in area MT+. There is a clear architectural reason to expect retinotopy to fail: TRIBE's video features are averaged over space before the response head, which should discard visual-field position. I present mapping stimuli, a fitting pipeline adapted from standard fMRI mapping analyses, and a stand-in model with known ground truth that serves as a positive and negative control, and apply them to TRIBE v2's predictions, comparing the fitted maps with human atlases using spin tests. TRIBE v2 shows a sharp split. There is no contralateral hemifield response and no polar-angle map, robustly across stimulus controls. There is no tonotopic gradient in primary auditory cortex: best frequencies span an interquartile range of only 0.14 octaves across core and belt, and the null persists with loudness-equalized tones. An eccentricity-like gradient appears only when the ring geometry changes, consistent with global image statistics rather than a positional code. In contrast, motion selectivity is strong and precisely localized: 22% of the 1% most motion-selective vertices fall in MT+, which covers 0.42% of cortex. In-silico experiments that depend on feature identity appear viable with TRIBE v2, while those that depend on visual-field or frequency position are not supported by the current model.

### Toward On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset: A Preliminary Study
- arXiv 2611.18438v1 · v1 2026-11-13 17:13 UTC · cs.CV, cs.HC
- Authors: Guangxi Feng, Philip Yasskin, Wei Yan
- Topics: Manipulation · score 6 · found via cs.HC
- Link: https://arxiv.org/abs/2611.18438
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AR-Classroom uses physical models and virtual overlays to help learners explore spatial transformations. To align these overlays on a standalone headset, we developed a markerless six-degree-of-freedom(6DoF) tracker for a LEGO airplane on the Meta Quest 3. A compact YOLO model trained on synthetic Unity renders predicts 20 keypoints from dynamic RGB crops resized to 128 by 128 pixels. A perspective-n-point solver estimates the airplane's pose from these predictions and the corresponding 3D landmarks. In a paired evaluation on 1,000 synthetic validation images, cropping guided by ground-truth boxes increased the detection rate on annotated images from 32.5 to 46.2 percent. Mean keypoint F1 increased from 42.9 to 44.6 percent, with lower keypoint precision in the cropped view. In preliminary headset tests, 2 Hz was the highest tested tracking target at which the application maintained approximately 72 frames per second. A headset demonstration illustrates virtual overlay alignment with the physical airplane before and after a manual rotation. Quantitative 6DoF pose accuracy on real headset footage will be measured in future work.

### Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination
- arXiv 2611.18514v1 · v1 2026-11-13 18:30 UTC · cs.AI, cs.CL
- Authors: Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao
- Topics: RAG (generic), Agents · score 6 · found via cs.AI, cs.CL, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.18514
- Full text: data/fulltext/2611.18514.txt

> Mechanistic Interpretability (MI) has made significant progress in explaining the internal computations of Large Language Models (LLMs); however, these advances have yet to demonstrate comparable success in explaining the decision-making processes of LLM-based agents. This paper examines the challenges MI tools face when applied to realistic agentic failures. We focus on one such failure: web agents hallucinating actions that are not available on a website. We apply a series of mechanistic analyzes to Qwen2.5-7B-Instruct as it interacts with live websites. We find that a linear probe trained on the last prompt token can predict hallucinations before generation begins (0.80 AUC) and steering along a probe direction corrects 85\% of hallucinations, but disrupts 7\% of valid actions. However, these results only provide a partial explanation of why the agent hallucinates. The probe direction is sensitive to prompt formatting, losing much of its steering effect after a minor change to how actions are represented. Additionally, circuit identification can be difficult as the computation is distributed across multiple components and positions, and the information the agent relies on varies across examples. We discuss how these observations challenge the assumptions underlying standard MI methods for circuit discovery and feature identification, and outline future directions for making these methods better suited to explain failures in LLM-based agents.

### Advancing Quantization for R&R Models with Microscaling Formats
- arXiv 2611.17501v1 · v1 2026-11-12 20:46 UTC · cs.AI
- Authors: Yavuz Yetim, Bor-Yiing Su, Zhe Wang, Arthur Liu et al.
- Topics: Ads · score 4 · found via search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.17501
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Recommendation and Ranking (R&R) models, particularly in digital advertising, require massive inference throughput but exhibit extreme sensitivity to precision loss. Unlike Large Language Models (LLMs) that frequently tolerate quantization-induced accuracy drops of 1% or more, production-grade R&R models enforce a stringent launch bar: model quality must remain within a 0.01% Normalized Entropy (NE) margin relative to the baseline, which commonly uses FP16 or FP32. This tight constraint has historically hindered the adoption of aggressive quantization in this domain. In this paper, we present an empirical evaluation of both MXFP8 and the 6-bit MXFP6 format for industrial-scale R&R inference on the AMD MI350X architecture. To the best of our knowledge, this is the first paper, across R&R and LLM domains, that reports significant speedups from native MXFP6 GEMMs, which quantize both weights and activations and compute directly on 6-bit elements, without sacrificing model quality. We demonstrate that we can selectively apply this 6-bit format to maximize overall QPS gain without breaching the strict NE parity threshold. We further show that MXFP8 is a viable alternative to row-wise FP8: the two formats have nearly the same accuracy on our models, so the faster kernel can be chosen for each GEMM shape. On two production ads ranking models, our implementation shows measured GEMM kernel speedups over FP16 of 1.33--1.55x for MXFP8 and 1.73--1.99x for MXFP6 across all supported linear layers, and up to 2.90x for MXFP6 on individual layers, alongside end-to-end (E2E) inference throughput gains from selective MXFP6 of 1.5--5.3% for Model A and 7.6--14.3% for Model B over their FP8 configurations.

### StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval
- arXiv 2611.18516v1 · v1 2026-11-13 18:35 UTC · cs.CV, cs.IR, cs.LG
- Authors: Dayoon Ko, Yichuan Wang, Soyeong Jeong, Joseph E. Gonzalez et al.
- Topics: Agents · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.18516
- Full text: data/fulltext/2611.18516.txt

> Screen history can serve as searchable visual memory for people and agents, but unlike an offline corpus, it must be encoded and indexed as each screenshot arrives. OCR-based indexing is fast but loses visual information; visual encoding takes over two seconds. Yet screens change incrementally: most pixels repeat within and across screenshots. This raises a question: do visual encoders need to recompute their representations from scratch for every new screenshot? We present StreamEmbed, a system for incremental visual embedding that exploits this redundancy. Guided solely by pixel differences, it combines spatial token pruning, which skips blocks that repeat a neighbor, with temporal KV reuse, which reuses cached keys and values for blocks unchanged across screenshots. A small learned adapter compensates for pruning and reuse to preserve fidelity to full-screenshot embeddings. On ScreenMemEval, our benchmark of 10,426 questions over 184 hours of screen histories from two humans and a computer-use agent, StreamEmbed sets a new accuracy-latency Pareto frontier on an M2 Pro GPU: it encodes up to 3.7x faster than full-screenshot encoding without sacrificing accuracy and improves accuracy over OCR-based indexing by up to 6.3 Recall@10 points at matched latency. A memory-efficient vector index stores a simulated year of screenshots in 0.13 GB of RAM. Together, these results make real-time indexing of screen history in its native visual form practical, laying a foundation for fully local visual assistants.

## Other new cs.IR papers, title only (6)
- Towards High-Performance Multimodal Discovery: Evaluating Retrieval Efficacy and Operational Scalability in Digital Libraries — https://arxiv.org/abs/2611.17726
- RecMem: Recurrent Memory Compression for Long-Sequence Generative Recommendation — https://arxiv.org/abs/2611.17921
- Who Counts as Exposed? Measurement Choices in an Open, Re-estimable Index of Occupational AI Exposure — https://arxiv.org/abs/2611.18168
- Explanations that Transfer: Interpreting Medical Retrieval with Sparse AutoEncoders — https://arxiv.org/abs/2611.18179
- RACE: Ranking-Uncertainty Aware Capacity-Adaptive Customization for Efficient Sequential Recommendation — https://arxiv.org/abs/2611.18244
- MeReader: An Offline, Privacy-Preserving, Progress-Aware AI Assistant for Narrative eBook Reading — https://arxiv.org/abs/2611.18513

## Already listed on an earlier day, still inside the look-back window (46)
- Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition — https://arxiv.org/abs/2611.15538 (score 20)
- Protocol-Aware Auditing of Domain-Blind Feature Attribution in Network Intrusion Detection — https://arxiv.org/abs/2611.16018 (score 14)
- Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents — https://arxiv.org/abs/2611.16744 (score 14)
- From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research — https://arxiv.org/abs/2611.17041 (score 14)
- RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication — https://arxiv.org/abs/2611.16425 (score 12)
- Loyalty Capture: Reporting Relationships and Structural Sycophancy in Frontier AI Models — https://arxiv.org/abs/2611.15475 (score 10)
- Lost in Delegation: Studying the Effectiveness of Task Orchestration in Generative Search — https://arxiv.org/abs/2611.16526 (score 10)
- Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation — https://arxiv.org/abs/2611.17161 (score 10)
- Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights — https://arxiv.org/abs/2611.15642 (score 9)
- RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback — https://arxiv.org/abs/2611.15802 (score 9)
- MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents — https://arxiv.org/abs/2611.15600 (score 8)
- Wayfinder: Adaptive Resource Routing from Agent Citations — https://arxiv.org/abs/2611.16053 (score 8)
- Trained on What Screen Readers Cannot Read: Accessibility Debt in the GUI Corpora Behind Computer-Use Agents — https://arxiv.org/abs/2611.16107 (score 8)
- ReliaGuard: Reconstruction-Aware Watermarking for Source Attribution and Blind Edit Localization — https://arxiv.org/abs/2611.16368 (score 8)
- MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection — https://arxiv.org/abs/2611.16693 (score 8)
- Sketching Language Models for Context Attribution — https://arxiv.org/abs/2611.17313 (score 8)
- Right Answers, Inconsistent Evidence: Source-Level Counterfactual Auditing of Large Audio-Language Models — https://arxiv.org/abs/2611.15463 (score 6)
- Temporal Context-Aware Spam Detection Using Transformer-Based NLP Models — https://arxiv.org/abs/2611.16139 (score 6)
- EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming — https://arxiv.org/abs/2611.16728 (score 6)
- A Code-Level Audit of X — https://arxiv.org/abs/2611.16800 (score 6)
- SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction — https://arxiv.org/abs/2611.15426 (score 5)
- HyperPage: Learned Page Layouts for Disk-Resident Graph Vector Indexes — https://arxiv.org/abs/2611.16149 (score 5)
- CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented Generation using Decision Models — https://arxiv.org/abs/2611.16366 (score 2)
- Calibrated Early Termination with Bounded Optimality Gaps for Constrained Vector Search — https://arxiv.org/abs/2611.16148 (score 1)
