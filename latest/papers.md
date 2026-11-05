# Paper candidates — 2026-11-05 (IST)

Generated 2026-11-05 07:27 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 21 new topic matches · 14 other new cs.IR · 125 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (21), highest score first

### WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution
- arXiv 2611.06777v1 · v1 2026-11-04 16:53 UTC · cs.IR
- Authors: Wenyi Xu, Renzhe Zhou, Songyang Li, Feiran Zhu et al.
- Topics: Citation & source selection, Ads · score 12 · found via cs.IR
- Link: https://arxiv.org/abs/2611.06777
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Algorithm-driven services, including search, recommendation, and advertising, rely on multi-stage model pipelines. While research prioritizes model optimization, post-deployment monitoring focuses on operational reliability. Yet operationally healthy systems may still produce poor-quality results, exposing a gap in existing evaluation and monitoring practices. However, a systematic problem formulation and benchmark for this task remain lacking. To bridge this gap, we formulate System Quality Diagnosis (SQD) for algorithm-driven services, a new task that extends quality evaluation beyond identifying poor outcomes to attributing their causes across system components. Focusing on industrial search, we propose WISE, an agentic framework for end-to-end quality diagnosis that discovers user-facing issues and traces their origins to underlying algorithmic components. To improve diagnostic reliability, we introduce ReTrace for constructing evidence-consistent trajectory supervision and Adaptive Harness-Policy Optimization (AHPO) for failure-guided optimization of the agent harness and model policy. To enable systematic evaluation, we construct WISE-BENCH, a real-world multimodal search benchmark that combines user-facing evidence, internal pipeline traces, and expert diagnosis annotations. Extensive experiments show consistent gains across model scales, with WISE achieving 75.20% end-to-end accuracy on Qwen3.5-35B-A3B. In production, WISE supports quality auditing, online quality assurance, and model optimization, reducing diagnosis costs and improving downstream relevance models.

### Securing Web Agents with the Compile-Then-Execute Paradigm
- arXiv 2611.06039v1 · v1 2026-11-04 06:42 UTC · cs.CR
- Authors: Annabella Chow, Jinhao Zhu, Sylvie Venuto, Abdulaziz Alharbi et al.
- Topics: Agents, Manipulation · score 11 · found via cs.CR, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.06039
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web agents commonly follow the ReAct paradigm, selecting each action from runtime observations that inherently mix trusted and untrusted content. This design makes their control flow vulnerable to prompt injections embedded in webpages. We introduce Baya, a compile-then-execute web agent designed to prevent prompt-injection-driven control-flow hijacking by design. Before accessing the live website, Baya compiles the user's request into an executable Python program that calls a Trusted Website API. The planning model does not observe live website content; only the compiled program processes it. Untrusted data may determine program values or select among branches defined during compilation, but it cannot redefine the user task or cause the model to synthesize new website operations at runtime. The Trusted Website API gives the compiler a unified view of the website's action space, enabling ahead-of-time planning without the stepwise action discovery required by reactive agents. Our evaluation across 581 valid WebArena Verified tasks shows that Baya achieves 77.8% aggregate utility, outperforming browser-only ReAct (55.1%) and API-enabled ReAct (66.7%). On WASP, a security benchmark for web agents, Baya achieves 0% attack success rate, compared with 16.2% for API-enabled ReAct and 25.5% for browser-only ReAct.

### Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification
- arXiv 2611.06662v1 · v1 2026-11-04 15:37 UTC · cs.AI
- Authors: Hyeseo Jeon, Seonho Yoo, Jay-Yoon Lee
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.06662
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Search-augmented reasoning systems can reach correct answers while making errors in intermediate steps. Reliable auditing must check whether evidence $D$ covers the question $Q$, reasoning $T$ addresses $Q$, and $T$ is grounded in $D$. We introduce GraphRail, which represents requirements, evidence, and reasoning as structured claims and compares them without a generative judge or gold answer. Across three multi-hop QA benchmarks and three reasoning frameworks, GraphRail improves error recall over generative verifiers while remaining stable under stochastic extraction. Its diagnoses can also guide online reasoning, providing a traceable way to detect and correct intermediate errors.

### LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks
- arXiv 2611.06687v1 · v1 2026-11-04 15:55 UTC · cs.AI
- Authors: Jenny Yang, Elizabeth Proehl, Anjan Bharadwaj, Emily Fan et al.
- Topics: GEO/AEO · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.06687
- arXiv comment: 16 pages, 6 figures
- Full text: data/fulltext/2611.06687.txt

> We introduce LifeVal, a benchmark evaluating AI model performance on personalized agentic consumer tasks. LifeVal covers the most valuable life tasks that a personalized digital superassistant could automate, representing over 1.7 trillion US dollars in annual willingness-to-pay across 148 consumer task categories (e.g., managing finances, moving apartments, searching for a job, finding childcare). To construct our activity distribution, we conducted a new survey of willingness-to-pay for a digital superassistant across a demographically representative sample of over 3,800 consumers, cross-referencing our results against the American Time Use Survey (Bureau of Labor Statistics, 2025) and the Multinational Time Use Study (Fisher et al., 2025). For the most valuable consumer activities, we recruited task creators to create AI evaluation tasks personalized using real ChatGPT conversations and memories, reference files, and personal context. Task creators had to pass our expertise threshold (including personally completing the task multiple times and seeing the results through in their real lives for over a year) and also write a rubric, ensuring that our evaluation measured the best personalized completion for that task. All tasks had to pass at least three rounds of human quality-control before acceptance into our final evaluation sets.

### CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines
- arXiv 2611.05862v1 · v1 2026-11-04 02:52 UTC · cs.CL
- Authors: Yuqin Dai, Zhanwei Zhang, Honghui Yang, Zhouheng Yao et al.
- Topics: Brand/product recommendation · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.05862
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language model (LLM) shopping assistants now recommend products in multi-turn conversations. However, reliable evaluation faces Data scarcity and Difficulty Standardizing Criteria. To address these obstacles, we introduce CARTBench for CART (Complex and Ambiguous Requests with Timelines). For Data scarcity, we curate cases from real commercial shopping needs across 17 retail domains, pairing timestamped dialogue with 1,603 product records. For Difficulty Standardizing Criteria, we develop case-specific rubrics guided by Ideal Response Principles, distilled from excellent replies manually selected from successfully completed orders. These principles also guide Principle-Guided CART Prompting, our structured recommendation strategy. The experimental benchmark contains 1,328 expert-annotated criteria across Core, Excellence, and Safety. To answer the CART question, we evaluate 7 flagship commercial API models, including GPT-6.1-Sol and Claude-Opus-5, and 35B+ parameters open-weight models. In the first full-suite evaluation under the frozen rubrics, 3 of 10 models exceed 90% on Core, while none exceeds 45% on Excellence. Therefore, we identify an understanding-to-execution gap between required behavior and high-quality purchase advice. To examine these limitations, we diagnose shared failures in product evidence and unresolved needs, linked to changing requirements and decisive unknowns. Code and data are available at https://github.com/Da1yuqin/CARTBench.

### Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline
- arXiv 2611.06000v1 · v1 2026-11-04 05:47 UTC · cs.CV, cs.AI
- Authors: Ashutosh Dayal, Mallika Garg, Debashis Sen
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.06000
- arXiv comment: Accepted at IEEE/CVF Winter Conference on Applications of Computer Vision(WACV 2027)
- Full text: data/fulltext/2611.06000.txt

> Designing systems that attribute a generated image to its source model has lately become a major area of AI research. Most existing datasets and systems related to image source attribution are targeted towards the detection of architectural signatures of the source models. Distinct from this, focusing on stable diffusion, we introduce a novel task, IntrAA-SD, Intra-Architecture source Attribution for Stable Diffusion, where the source models to be differentiated share the same architectural backbone and differ only due to fine-tuning. The proposed task aligns with the emergence of fine-tuned generators having the same architecture, like Juggernaut XL and RealVis XL, which are fine-tuned versions of Stable Diffusion XL (SDXL). We provide a first-of-its-kind $140$K-image benchmark dataset containing images generated from different fine-tunes of SDXL, along with in-domain and out-of-distribution prompts. We also provide a baseline framework for IntrAA-SD, which leverages a style-conditioned Mixture-of-Experts network. It uses a frozen CLIP backbone to capture the image style and gate the MoE, which processes fine-tuned trace features from a high-resolution LoRA-adapted DINOv2 network. The fine-tuned models used, the prompting strategies considered, and the formation details employed in the novel dataset are elaborated. Our baseline intra-architecture source attribution method is evaluated in terms of attribution accuracy on our dataset, and ablation studies are also performed. Code and dataset is available at https://github.com/mallikagarg/IntrAA-SD.

### Beyond Risk Cues: A Mechanism-Level Benchmark and Verifiable Debate for Scam Video Detection on the Web
- arXiv 2611.06110v1 · v1 2026-11-04 07:52 UTC · cs.AI
- Authors: Yifan Wang, Junyu Lu, Shun Zhang, Chaozhuo Li et al.
- Topics: Citation & source selection, Ads · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.06110
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Online scam videos pose significant threats to individuals and society. Existing studies primarily focus on binary classification, offering limited insights into how scams work and the reasoning behind detection decisions. Moreover, they often overlook the challenge of distinguishing scam videos from superficially similar non-scam content, such as advertisements, and the robustness of detection models against misleading arguments. These limitations hinder reliable scam video detection. To address these limitations, we introduce MechScam, a benchmark comprising 6,614 videos covering diverse scam mechanisms and non-scam categories. MechScam provides explanations supported by video evidence, annotations of potential scam elements and their context, and misleading arguments constructed from genuine evidence. Recognizing that genuine evidence can still be used to justify misleading conclusions, we further propose ScamCourt, a debate framework in which trained prosecution and defense debaters present opposing arguments, while a trained judge makes decisions based on a transcript with verified citations. Extensive experiments show that state-of-the-art MLLMs struggle to distinguish scam videos from similar non-scam content. ScamCourt outperforms larger MLLMs and same-backbone fine-tuned baselines, reducing false positives and showing stronger resistance to misleading arguments. Together, MechScam and ScamCourt contribute to more reliable and interpretable scam video detection. The dataset and code are available at https://github.com/SuperYFan/MechScam.

### Beyond the Landing Page: Website Blocking, Tracker Visibility, and Human Alignment in Automated Web Crawls
- arXiv 2611.06197v1 · v1 2026-11-04 09:12 UTC · cs.CR
- Authors: A H M Nazmus Sakib, Mahsin Bin Akram, Raveen Wijewickrama, Igor Bilogrevic et al.
- Topics: Crawl · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.06197
- Full text: data/fulltext/2611.06197.txt

> Web tracking studies largely rely on automated crawlers, yet their measurements can differ from what people encounter while browsing. Conventional crawlers follow predefined navigation rules, whereas LLM-driven agents decide how to navigate and interact with websites, potentially changing the tracking they encounter. We compare agentic and non-agentic crawlers to examine how websites respond to them, what tracking they record, and how closely their observations match human browsing. Across 2,000 popular websites, we evaluate different navigation strategies, automation frameworks, and stealth configurations, alongside browsing data from 26 participants. We find that website denials increase beyond landing pages for standard browser automation, while a detection-resistant automation framework largely prevents this escalation without increasing recorded tracking. On the same URLs, agentic crawlers record tracking activity from 1.5-1.7 times as many third-party organizations, particularly on consent-managed pages. Agentic crawlers recover 82-87% of tracker organizations observed by participants, compared with 58-68% for non-agentic crawlers, yet roughly half of their own observations are absent from human participant visits. These findings show that avoiding website interventions, increasing tracking visibility, and achieving closer agreement with human observations do not necessarily go hand in hand, highlighting the need to select and validate crawlers according to the measurement objective.

### Presentation Sensitivity in Typed Decision Models for Subjective Text Evaluation
- arXiv 2611.06384v1 · v1 2026-11-04 11:48 UTC · cs.CL
- Authors: Jatin Agrawal, Radhika Mamidi
- Topics: GEO/AEO, Clicks & measurement · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.06384
- arXiv comment: 27 pages, 1 figure, includes appendices
- Full text: data/fulltext/2611.06384.txt

> Typed decision models offer structured choices, scores, and probabilities for low-cost automated evaluation. We present a controlled audit of presentation sensitivity in Jev, Clef Flash, and Perplexity Decider across native choice and score interfaces. Across six datasets with 9,000 multiply annotated humor, helpfulness, and summarization items, we collect 702,000 judgments under interventions that vary positions, identifiers, authorship claims, endorsements, decision framing, and rating rubrics while preserving the evaluated texts. Jev's second-position probability advantage reaches 6.11 percentage points on summaries; reversing reader endorsements changes Perplexity's selected humor text on 40.40% of pairs; and rejection framing reduces Clef's summary agreement with human preferences by 23.36 points. Rating formats also shift score levels while often preserving rankings. Across these findings, repeatability, presentation robustness, and human alignment emerge as distinct properties of an evaluator. Reliable use therefore requires validating the decisions and score interpretations on which an evaluation pipeline depends.

### U.S. State Guidance on AI in K-12 Education: A Comparative Content and Citation Analysis
- arXiv 2611.06762v1 · v1 2026-11-04 16:40 UTC · cs.CY, cs.DL
- Authors: Shahan Ali Memon, Anna-Maria Gueorguieva, Anukriti Kumar, Lucy Lu Wang et al.
- Topics: Citation & source selection · score 8 · found via cs.CY
- Link: https://arxiv.org/abs/2611.06762
- arXiv comment: 29 pages, 8 figures, 8 tables, Under Review
- Full text: data/fulltext/2611.06762.txt

> In the years following the public release of ChatGPT in late 2022, more than half of U.S. states have published formal guidelines around AI usage in K-12 education, creating a record of largely independent state education departments responding to a shared technological disruption. In this work, we analyze publicly available AI usage guidance documents from 35 states in the U.S. and Puerto Rico. We compare the guidance in these documents across various dimensions, including pedagogy and instruction, audience, actionability, workforce and career readiness, responsible use and equity, and alignment with state-level demographics and administrative capacity. Finally, we investigate who authored these documents and their cited sources, identifying epistemic foundations underlying their claims. We find that guidance priorities converge on topics anchored in laws such as data privacy and academic integrity, each addressed in 97% of documents. While most documents mention equity of access (86%) and algorithmic bias (97%), fewer discuss specific marginalized populations. Across documents, there is a common framing of urgency around AI integration to prepare students for workforce readiness (86%) and promote loosely-defined personalized learning (86%), which is not matched by specific guidance for capacity-building, actionability, or accountability. State priorities show no relationship to state demographics, capacity, or partisanship. Instead, we identify notable interdependencies between states with shared citations to non-profit organizations like TeachAI and Code.org, with some states reproducing TeachAI's model guidance near-verbatim, and peer citations concentrating on a few early states such as Oregon and Washington. No state includes parents as contributors on these documents, and only five include students.

### LLM-based NPCs in Video Games: A Systematic Mapping Study
- arXiv 2611.05427v1 · v1 2026-11-02 23:03 UTC · cs.SE, cs.AI
- Authors: Dilan Mian, Jeremy Bradbury, Yann-Gaël Guéhéneuc, Fabio Petrillo et al.
- Topics: RAG (generic), Query fan-out · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.05427
- arXiv comment: 12 pages. Accepted manuscript. Published in IEEE Transactions on Games (Early Access)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> For decades, non-player characters (NPCs) have been driven by rule-based systems whose personalities and interactions are scripted before release. Large language models (LLMs) promise NPCs that converse openly, adapt to new situations, and behave in ways developers did not fully author, prompting a wave of research and commercial experimentation. Yet the field lacks a unified picture of what has been built, how well it works, and at what cost. We address this gap with a systematic mapping study of 377 papers from the academic literature, yielding 42 papers analysed against a main research question and ten sub-questions across four thematic axes. We provide the first quantitative characterisation of component adoption, latency, safety coverage, and reproducibility: short-term memory and world-state grounding are near-universal (60% and 69%), whereas long-term memory (31%), reflection (38%), and retrieval-augmented generation (14%) remain rare, and response times span 2.6 to 15 seconds. Finally, we identify six structural barriers to commercial adoption and offer evidence-based recommendations for developers and researchers.

### GRIDSHIELD: Verifiable Grid Feasibility and Manipulation Resistance in Privacy-Preserving Peer-to-Peer Energy Trading
- arXiv 2611.05816v1 · v1 2026-11-04 01:49 UTC · cs.CR
- Authors: Abdullahil Kafi, Md Zahidul Islam, Alvi Ataur Khalil
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.05816
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Blockchain-based peer-to-peer (P2P) energy markets let neighbors trade directly, but concentrate unchecked power in the clearing operator. Most prior work addresses only part of this: network-aware clearing respects grid constraints but operates on plaintext allocations, while privacy-preserving designs hide bids yet either drop the network constraint, enforce it only inside an unauditable computation, or recover it at the cost of a per-circuit trusted setup. Neither considers what happens if an adversary captures the operator's clearing privilege to reorder trades for profit or curtail a rival. We present GRIDSHIELD, a P2P energy-trading system that clears sealed bids with an order-independent batch program, removing the welfare a compromised operator can extract by reordering trades, and proves the result grid-feasible via an aggregated congestion-feasibility proof (ACFP). Exploiting the additive homomorphism of Pedersen commitments, ACFP reconstructs each grid constraint directly from per-bus commitments, reducing feeder-wide feasibility verification over any public grid constraints to a single aggregated range proof over the hidden allocation, with a reveal-and-recompute challenge that catches feasible yet unfair clearings. We introduce congestion-responsibility fairness (CRF), a metric scoring curtailment against each party's physical responsibility for congestion rather than consumption. We evaluate GRIDSHIELD against three prior P2P energy-trading designs across four feeders, including a 240-node Midwest feeder with real hourly loads, on a live Hyperledger Fabric network benchmarked with Hyperledger Caliper. GRIDSHIELD proves an entire round feasible with a few-kilobyte proof and no trusted setup, rejects infeasible allocations two of the three compared designs accept, and sustains $\approx$1064 tx/s.

### Risk Control Certifies Rates, Not Magnitudes: An Audit of Selective Fetal Biometry
- arXiv 2611.05851v1 · v1 2026-11-04 02:41 UTC · cs.AI, cs.CV
- Authors: Zhengshuai Yang, Linna Jiang, Changyun Li, Guihu Zhao
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.05851
- arXiv comment: 10 pages, 2 figures, 3 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Prenatal ultrasound biometry must return a head circumference (HC) and refuse when the image cannot support one. Selective prediction trades coverage against error, but its finite-sample guarantees bound the rate of gross errors, not their magnitude. We audit a tool-grounded biometry pipeline on two separately pre-registered four-way splits of the 999 labelled HC18 images, retraining the segmenter three times on each. Calibrating the contour-completeness threshold by exact Clopper-Pearson risk control returns a certificate indistinguishable from a hand-set floor, yet the pipeline still emits a 271.3 mm error: a small, geometrically complete ring fitted to an image whose true HC is 324.6 mm. The accepted candidate scores 0.94 completeness, so the score cannot see the failure, and one outlier among $\approx 150$ answers leaves the certified risk bound ($α= 0.10$) intact. A second, untouched split reproduces the mechanism on a different image (233.3 mm). Constraining the admissibility region---the anatomical range in which the measurand is defined---removes the family instead: raising the lower bound from 50 to 55 mm costs 0.4 coverage points and cuts the worst-case error on both splits to 11.4 and 11.1 mm, whereas suppressing it through the completeness threshold costs 19.0 and 12.1 points. At an anatomically defined 70 mm the frozen tests give 1.91 and 1.81 mm MAE.

### Information-Matched Auditing of Conversational Emotion-Shift Forecasting: A Leakage-Safe Evaluation Protocol
- arXiv 2611.05895v1 · v1 2026-11-04 03:36 UTC · cs.CL, cs.LG
- Authors: Bin Wen, Dai-Qiao Zhang, Tien-Ping Tan
- Topics: Clicks & measurement · score 6 · found via cs.CL
- Link: https://arxiv.org/abs/2611.05895
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Comparisons in conversational emotion-shift forecasting are easily distorted when a learned model receives rich features but its transition baseline is given a noisy or unavailable current-emotion label, when hyperparameter budgets differ, or when target-turn information enters the representation. We present an information-matched, leakage-safe auditing protocol that closes these gaps with an explicit commitment point, executable causality tests, equal four-configuration validation searches, and seed-dialogue-aware inference. Applying it to six causal model families on four text corpora and two feature-source sensitivity configurations shows that a deployable train-only current-emotion classifier feeding the transition baseline yields a different verdict than an oracle diagnostic where both sides receive gold current emotion. Under the deployable condition, learned models improve over the predicted-label baseline on all four primary corpora; DailyDialog gains are large and survive a 72-comparison Holm correction (best ROC-AUC gain = +0.167, adjusted p=.0144). Under matched gold information, the baseline remains competitive on IEMOCAP and stronger on MELD, while every model retains a large DailyDialog advantage. We additionally report precision-recall AUC, calibration, a strictly utterance-local feature control, same-person self-shift forecasting, and a future-access dose-response test. An eight-item leakage checklist accompanies the protocol. Code, raw seed predictions, and reporting artifacts are available from the corresponding author upon request.

### Do Saliency Maps Fail Dense Breasts? A Chance-Normalized, Confounder-Aware Audit of Explanation Fairness in Mammography
- arXiv 2611.05909v1 · v1 2026-11-04 04:01 UTC · cs.CV, cs.AI
- Authors: Ahmed Jaheen
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.05909
- Full text: data/fulltext/2611.05909.txt

> Saliency maps, offered as evidence that mammography classifiers use the cancer, are untested in dense breasts, which can hide cancers. We tested whether they locate cancers worse there, and why. On 1,345 malignant CBIS-DDSM views, we scored three CNNs' Grad-CAM, Integrated Gradients and occlusion maps by whether their peak hits the lesion and a chance-normalized lesion-to-background saliency ratio (bits; +1 doubles it). Unadjusted gaps were large: Grad-CAM peaks hit 44% of dense vs. 58% of non-dense lesions. Case mix, chiefly more calcifications in dense breasts, explained about half or more of each gap. Occlusion kept a significant average of -0.56 bit gap. Controls also implicate the classifiers: unadjusted gaps exceeded an image-only conspicuity map's, and models relied less on dense-breast lesions. We recommend reporting density gaps before and after case-mix adjustment, per classifier, with conspicuity and lesion-reliance controls.

### Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation
- arXiv 2611.06498v1 · v1 2026-11-04 13:32 UTC · cs.CR, cs.IR, cs.LG
- Authors: Georgios Feretzakis, Alexandros Papaspyridis
- Topics: RAG (generic), Clicks & measurement · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2611.06498
- arXiv comment: 20 pages, 2 figures, 7 tables. Code and data: https://github.com/securagenai/signed-but-steerable (DOI 10.5281/zenodo.23948839)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. We study this text-vector integrity gap. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls the vectors: the hijack rate equals the distribution of angular retrieval margins at the tolerance (the margin law). Margins are small in five corpora and two embedding models, so an idealised tolerance at the level of floating-point noise leaves up to 5.5% of queries exposed (at most 1.2% in any corpus once exact duplicate documents are excluded), and a threshold calibrated from our CPU INT8-FP32 comparison of a small embedding model (at the empirical 0.1% quantile of honest cosines) leaves 98-100% exposed; on a Raspberry Pi 5 running a local language model, such an attack lowers correct answers from 0.75 to 0.39. Integrity audits of compressed vector stores fare no better: on a FAISS product-quantisation index over 57,638 documents, tampered vectors that all pass the audit put the attacker's document first for 25% of targets. Verifying quantisation codes instead, with ambiguity decided by the verifier, a calibrated guard band and canonicalisation, accepted every honest vector in our samples on three platforms and left the publisher no choice. We also show that common floating-point and dynamic-INT8 inference pipelines are not bit-reproducible across batch sizes or architectures, and report pre-registered negative results on abstention, context pruning and semantic screening. We release code and data.

### SciToT: Multimodal Tip-of-the-Tongue Retrieval for Scientific Papers
- arXiv 2611.05829v1 · v1 2026-11-04 02:12 UTC · cs.IR
- Authors: Stan Fris, Sijie Tao, Makoto P. Kato, Maarten de Rijke
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.05829
- Full text: data/fulltext/2611.05829.txt

> Researchers frequently encounter difficulties re-finding scientific papers when they remember aspects of the content but cannot recall reliable identifiers, such as titles or author names. This type of re-finding task, known as tip-of-the-tongue (ToT) retrieval, is particularly challenging for scientific documents, where recollections may involve textual information and visual elements, including figures, diagrams, and plots. Existing ToT retrieval benchmarks do not address scientific search. We introduce a multimodal benchmark for scientific ToT retrieval, comprising 108,512 open-access scientific documents across five domains and 11,499 synthetically generated queries. To construct the benchmark, we propose a scalable query elicitation pipeline that independently extracts textual and visual memory cues from source documents and uses large language models to generate queries resembling incomplete human recollections. We characterize scientific ToT information needs through an empirical analysis of publicly available re-finding requests and use the outcomes to assess the generated queries using human annotations and automated quality control. The benchmark includes lexical, dense, late-interaction, and visually grounded retrieval baselines. We release the dataset, extracted document representations, generated memory cues, evaluation splits, and accompanying generation and retrieval pipelines under an MIT license to facilitate research on multimodal scientific paper re-finding.

### PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries
- arXiv 2611.06349v1 · v1 2026-11-04 11:10 UTC · cs.IR
- Authors: Xiaoyu Zhang, Yougang Lyu, Bin Wu, Sahan Bulathwela et al.
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.06349
- arXiv comment: 13 pages. Project page: https://pmrecbench.github.io/
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> On Web platforms for shopping and entertainment, recommendation agents under multimodal queries aim to deliver personalized recommendations that satisfy users' visually specified requirements and reflect preferences inferred from user histories. However, existing personalized recommendation benchmarks use text-only queries, while multimodal ones assess query matching without evaluating personalization based on real user histories. We introduce the Personalized Multimodal Recommendation Benchmark (PMRecBench), the first benchmark to evaluate the personalization of recommendation agents under multimodal queries. It pairs 510 quality-controlled image-text queries across clothing and movies with the corresponding users' real histories. PMRecBench features two key designs: (1) queries derived from consistent behavioral patterns in real user records, with reference images and targets linked to actual interactions; and (2) challenging diagnostic pools with candidate items rated highly by the user but violating requirements, and items satisfying requirements but never rated highly, testing requirement understanding and preference following, respectively. Extensive experiments on diagnostic pools reveal a personalization imbalance in recommendation agents: relative to personalization signals alone, adding multimodal queries weakens preference following, even though the additional information about query requirements improves overall ranking performance. Further analysis links this decline in preference following to image interpretation, where agents can prioritize resemblance to reference images over evidence from user histories, and stronger commercial backbones alone fail to resolve this imbalance. This personalization imbalance highlights a central challenge for recommendation agents: improving ranking performance while preserving preference following when responding to multimodal user queries

### Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized Retrieval-Augmented Generation
- arXiv 2611.05900v1 · v1 2026-11-04 03:48 UTC · cs.IR
- Authors: Linyao Zheng, Zhifang Mao, Xuhang Shi
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.05900
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Personalized retrieval-augmented generation requires extracting and applying user preferences from extended interaction histories. This task is challenging because preference evidence is scattered across past conversations and remains bound to specific temporal and situational contexts. Consequently, isolated fragments rarely provide complete support for a response, while preferences expressed under different conditions are easily conflated. To address these limitations, we propose Weaver, a framework that incrementally weaves memory-conditioned retrieval trajectories with compositional preference reasoning for personalized responses. Weaver operates on a Dual-Layer Retrieval and Reasoning Graph that couples an upper Intent Dependency Graph with a lower Memory-Conditioned Retrieval Trajectory Graph. Dependency Information Gap Tracking represents the information needed to answer the current request and its prerequisite dependencies in the upper graph. Memory-Conditioned Incremental Retrieval uses established premises and clues from retrieved conversations to locate missing evidence, recording the resulting retrieval trajectories in the lower graph. Scope-Aware Compositional Reasoning jointly interprets the accumulated evidence to determine which preferences apply to the request. It identifies complementary and alternative support and distinguishes conflicting claims within the same temporal and situational context. These conclusions iteratively update task premises and remaining information gaps, guiding subsequent retrieval to establish a coherent contextual basis for the final response. Experiments on personalized RAG benchmarks, particularly PersonaMem, demonstrate that Weaver outperforms leading baselines in both evidence completeness and answer quality.

### RAGCompass: Generalizable Retriever Routing via Reranking
- arXiv 2611.05596v1 · v1 2026-11-03 20:36 UTC · cs.CL, cs.IR
- Authors: Valentin Six, Mufei Li, Dongqi Fu, Yinglong Xia et al.
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.05596
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Different retrievers exist for retrieval-augmented generation, yet none performs best for all queries. Therefore, the key question is: given a query and retrieved passages from different retrievers, which one is most suited for that query? Existing routers usually make predictions from query-specific features and a fixed pool of retrievers; such routers have no output for an unseen retriever and are incapable by design on a new corpus. To fill these gaps, RAGCompass reads the retrieved passage sets themselves: passages from an unfamiliar retriever or corpus stay directly comparable to other passages, so routing stays well designed where a query-only map would fail. We contrastively fine-tune a reranker against the answer each evidence set produces, which accounts for most of the gain; a small comparison head adds a moderate improvement, and neither component has retriever-specific parameters. RAGCompass improves answer F1 by 28% relative to the best fixed retriever, and outperforms fusion baselines, three query-only routers, and a prompted 8B language model. Generalization experiments show that RAGCompass keeps most of its gain under an unseen corpus, retriever, or reader, while query-only baselines fall to the best fixed retriever or below.

### ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs
- arXiv 2611.06481v1 · v1 2026-11-04 13:20 UTC · cs.CL, cs.AI, cs.IR
- Authors: Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal, Bhaskarjit Sarmah et al.
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.06481
- arXiv comment: Preprint
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure their own construction pipeline produces, and whether they survive a change of construction is rarely tested. We study this cross-construction portability: whether one retrieval procedure, with no construction-specific schema, relation names, or retuning, stays effective when the graph is built differently. We introduce ArcRAG, which induces a query-local graph interface at inference time (the node labels, relation descriptors, and property keys reachable from the entities a question names), plans multi-hop traversals against it, and executes and repairs them as Cypher. We build each of the MuSiQue, HotpotQA, and TriviaQA corpora as a schema-guided graph (typed nodes, a closed relation set, source provenance) and as an open-information-extraction graph (untyped nodes, free-text relations), with the retriever's configuration fixed across them. We compare against a construction-agnostic Direct-Cypher agent, ablate each stage across retry and pass budgets on both graph families, and compare with results reported for prior GraphRAG systems, most of which design retrieval together with their own graph construction. Across the two constructions, we find that retrieval need not be co-designed with the graph: query-time interface induction keeps a construction-agnostic retriever effective when the construction changes, although construction still shapes absolute accuracy.

## Other new cs.IR papers, title only (14)
- LIBRA: Programmatic Induction of Executable Tool Libraries — https://arxiv.org/abs/2611.05445
- Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled Hyperparameter Scaling — https://arxiv.org/abs/2611.05643
- Combining Relevant Expert Knowledge Using Mixtures of Feedback Fuzzy Cognitive Maps — https://arxiv.org/abs/2611.05664
- Turbocharging PiPNN for Proximity and $k$-NN Graph Building — https://arxiv.org/abs/2611.05690
- Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex — https://arxiv.org/abs/2611.05753
- Item Representations Matter: Bridging Hard Semantic IDs and Soft Prototype Mixtures for Generative Retrieval — https://arxiv.org/abs/2611.05799
- Optimal Re-Ranking Depth — https://arxiv.org/abs/2611.05908
- One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation — https://arxiv.org/abs/2611.05952
- From Waste to Discovery: Recycling High-Scored Unexposed Candidates in Taobao Feed Recommendation — https://arxiv.org/abs/2611.05997
- Do Search-Augmented Recommenders Use the Latest Search Episode? — https://arxiv.org/abs/2611.06044
- Generative Retrieval under Real-Time Supply Constraints in Local Commerce — https://arxiv.org/abs/2611.06323
- Deliberate Latent Reasoning for Sequential Recommendation — https://arxiv.org/abs/2611.06521
- Alternatives to Shallow Autoencoders for Collaborative Filtering — https://arxiv.org/abs/2611.06610
- Balancing hierarchical representation and quantization: A performance trade-off in text embeddings — https://arxiv.org/abs/2611.06859

## Already listed on an earlier day, still inside the look-back window (125)
- Characterizing Adversarial GEO via Implicit Brand Injection — https://arxiv.org/abs/2611.04005 (score 21)
- IntentGEO: Intent-aware Generative Engine Optimization for Recommendation — https://arxiv.org/abs/2611.04225 (score 18)
- Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO — https://arxiv.org/abs/2611.01126 (score 15)
- Building Weighted PubMed Citation Graphs at Scale: A Pipeline and an Audit of Edge-Similarity Features — https://arxiv.org/abs/2611.01044 (score 14)
- From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents — https://arxiv.org/abs/2611.01527 (score 14)
- FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting — https://arxiv.org/abs/2611.01621 (score 14)
- When 200 OK Is Not an Answer: Silent Fetch Failures in Agentic Web Content Acquisition — https://arxiv.org/abs/2611.00884 (score 13)
- The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents — https://arxiv.org/abs/2611.03754 (score 13)
- AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising — https://arxiv.org/abs/2611.00822 (score 12)
- Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce Relevance — https://arxiv.org/abs/2611.02758 (score 12)
- $τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems — https://arxiv.org/abs/2611.04459 (score 12)
- ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud — https://arxiv.org/abs/2611.04879 (score 11)
- StreamDuo: A Live Commentator and a Research Agent for Unseen Games — https://arxiv.org/abs/2611.01120 (score 10)
- Designing Informative Actions: Action Construction for Long-Horizon Research Agents — https://arxiv.org/abs/2611.00773 (score 10)
- Measuring User Success in Randomized Search Experiments: Interpreting Good Abandonment in Generative AI Search — https://arxiv.org/abs/2611.01582 (score 10)
- EMBERS: Empirically Motivated Robustness Testing of Deep Research Systems via Defect-Guided Fuzzing — https://arxiv.org/abs/2611.03723 (score 10)
- Same Trajectory, Different Knowledge: Information-State-Aware On-Policy Distillation for Search Agents — https://arxiv.org/abs/2611.01987 (score 10)
- DR Pixel: Page-Native Deep Research with Vision-Language Models — https://arxiv.org/abs/2611.03097 (score 10)
- Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction — https://arxiv.org/abs/2611.03183 (score 10)
- Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents — https://arxiv.org/abs/2611.03384 (score 10)
- MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study — https://arxiv.org/abs/2611.03555 (score 10)
- Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions — https://arxiv.org/abs/2611.03052 (score 9)
- Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses — https://arxiv.org/abs/2610.40747 (score 8)
- Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents — https://arxiv.org/abs/2610.39251 (score 8)
- PhoneValue-Bench: A Multimodal Benchmark and Datasets for Consumer Smartphone Recommerce Valuation — https://arxiv.org/abs/2611.00791 (score 8)
- Similarity-Weighted Leiden-CPM Clustering of a 7.4-Million-Node Biomedical Citation Graph: Weight Alignment, Scale, and Sparsity — https://arxiv.org/abs/2611.01049 (score 8)
- Acceptance and Responsibility Attribution Toward Autonomous Ambulances Across Driving Conditions: A Preliminary Survey of Fire Service Personnel — https://arxiv.org/abs/2611.01132 (score 8)
- Are Fake Citations a Form of Reward Hacking? A Pre-Registered Study of Post-Training and Citation Cues — https://arxiv.org/abs/2611.01313 (score 8)
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
- SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use — https://arxiv.org/abs/2611.03982 (score 8)
- AdSteer: Native Advertising in Large Language Model Generation — https://arxiv.org/abs/2611.04147 (score 8)
- Reliability Stress Testing of RAG Retrieval under Query-Relevant Corpus Poisoning — https://arxiv.org/abs/2611.04264 (score 8)
- SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local Search — https://arxiv.org/abs/2611.04662 (score 8)
- Learning to Rank Explanations for Recommendation with Language Models — https://arxiv.org/abs/2611.04775 (score 8)
- PACT: Defending Recommendation against Promotional News Rewriting via Attack-Diverse Score Consistency — https://arxiv.org/abs/2611.00972 (score 7)
- Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction — https://arxiv.org/abs/2611.01087 (score 7)
- Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning — https://arxiv.org/abs/2611.01411 (score 7)
- RuntimeTickets: Source-Grounded Security Obligations for Agent Skills — https://arxiv.org/abs/2611.03772 (score 7)
- From Benchmarks to Behaviors: A Framework for Auditing AI Agents — https://arxiv.org/abs/2611.03939 (score 7)
- ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix Reuse — https://arxiv.org/abs/2611.04259 (score 7)
- Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents — https://arxiv.org/abs/2611.04393 (score 7)
- Collaborative Search Meets Large Language Models: An Empirical Study — https://arxiv.org/abs/2611.04619 (score 7)
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
- AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data — https://arxiv.org/abs/2611.03815 (score 6)
- Whose startup does the AI back? An algorithm audit of reputation and demographic signals in LLM-assisted crowdfunding — https://arxiv.org/abs/2611.03993 (score 6)
- The Devil is in the Context: Nine Dimensions of Prompt Injection Attacks — https://arxiv.org/abs/2611.04672 (score 6)
- Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning — https://arxiv.org/abs/2611.04673 (score 6)
- When Category Means Move: A Paired-Support Audit of Recommendation Logs with Random Insertions — https://arxiv.org/abs/2611.05006 (score 6)
- DuSE-Bench: Benchmarking Joint Reasoning over Evolving Dialogue and Documents — https://arxiv.org/abs/2611.00755 (score 4)
- Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights — https://arxiv.org/abs/2611.01280 (score 4)
- Dynamic Click Destinations: Personalizing Post Ad-Click Landing Experiences — https://arxiv.org/abs/2611.01287 (score 4)
- EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees — https://arxiv.org/abs/2611.01977 (score 4)
- Multi-criteria Rating and Review based Recommendation Model — https://arxiv.org/abs/2611.02019 (score 4)
- DualEvolve: Dual-Level Self-Evolution of Mechanism and Orchestration for Recommendation — https://arxiv.org/abs/2611.04439 (score 4)
- OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer — https://arxiv.org/abs/2611.04720 (score 4)
- Auditing Multi-Proxy Explanations of Web User Preferences: Identification Boundaries and Abstention — https://arxiv.org/abs/2611.04997 (score 4)
- JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks — https://arxiv.org/abs/2611.05263 (score 4)
- HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation — https://arxiv.org/abs/2611.05319 (score 4)
- HiPaper: A Human-AI Collaborative System for Academic Literature Triage and Scholarly Sensemaking — https://arxiv.org/abs/2611.00762 (score 3)
- CST: Lightweight Risk Triage with Source-Grounded Evidence for Web Discussions — https://arxiv.org/abs/2611.01710 (score 3)
- Adversarial Robustness of Retrieval-Based Fact-Checking: Detecting and Mitigating Evidence Contamination — https://arxiv.org/abs/2611.02139 (score 3)
- Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation — https://arxiv.org/abs/2611.03747 (score 2)
- Bridging Low-Level Image Fusion and High-Level Semantic Understanding — https://arxiv.org/abs/2611.02896 (score 1)
- Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo — https://arxiv.org/abs/2611.03927 (score 1)
- QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution — https://arxiv.org/abs/2611.04625 (score 1)
