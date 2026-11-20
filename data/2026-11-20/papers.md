# Paper candidates — 2026-11-20 (IST)

Generated 2026-11-20 09:05 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 28 new topic matches · 13 other new cs.IR · 98 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (28), highest score first

### FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification
- arXiv 2611.25071v1 · v1 2026-11-18 19:13 UTC · cs.AI, cs.CL, cs.IR, cs.MA
- Authors: Meenakshi Rajpurohit, Anna Phan, Ravikumar Komandur Narayanan, Gunanidhi Ramakrishnan et al.
- Topics: Citation & source selection, Query fan-out · score 14 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.25071
- arXiv comment: 15 pages, 4 figures, 11 tables. Code: https://github.com/SJSU-CMPE259/AI-Stock-Research-and-Earnings-Assistant
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) write fluent financial analyses but miscompute ratios, recall stale prices, and route questions to the wrong tool with high confidence. We ask which component should do each job in a financial question-answering assistant, and study it with FinVeriQA, an open-source multi-agent research prototype over SEC filings and live market data: a compact typed-decision model (Laya) routes each question and screens out advice requests, Python computes every number, retrieval and tools fetch evidence, Mistral-7B writes a cited answer, a code validator checks that cited IDs exist and that numbers match computed notes, and a Model Context Protocol (MCP) server exposes the pipeline. In live experiments, Laya routed better than Mistral-7B (0.85 vs. 0.52; overall 0.86 vs. 0.68, McNemar p = 0.0003); a 12B Mistral decided no better, and DeepSeek-R1-8B decided better (0.79 vs. 0.68, p = 0.0192) but about 9.9 times more slowly. Mistral-7B computed 29% of 100 financial calculations correctly against 100% for Python, a live quote cut price error from 210% to 0.00%, and hybrid retrieval reached 76% Hit@5 on 50 filing questions. Yet in a live case study, both agent answers passed validation while describing AMD sample data under NVIDIA's and Alphabet's names. A controlled upper-bound study on the FinRank benchmark explains why: when one figure in the shared evidence is corrupted, self-consistency stays confident (agreement 0.55 to 0.59 while accuracy falls from 0.50 to 0.00), and a shared-evidence check (the kind our validator performs) catches 35% of the errors, whereas a check against the original passage catches 77% ($p = 5.96 \times 10^{-8}$); for DeepSeek-R1-8B, 68% vs. 90%. Verification must be independent of the evidence the writer saw.

### GEOHunter: Mapping a Generative Engine Optimization Network in the Wild
- arXiv 2611.26564v1 · v1 2026-11-19 18:33 UTC · cs.AI, cs.CR, cs.SI
- Authors: Sean Tang, Peiran Wang, Ying Li, Esha Shivakumar et al.
- Topics: GEO/AEO, Citation & source selection · score 14 · found via cs.AI, cs.CR, cs.SI, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2611.26564
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative engines synthesize retrieved web pages into answers, recommendations, and rankings. Generative engine optimization (GEO) services sell visibility in these answers by publishing promotional articles on user-generated-content (UGC) platforms for paying clients. Such promotion raises concerns in medical and financial domains, where misleading advice can cause harm. To study the severity of this problem, we measure one such paid-content operation across three major Chinese UGC platforms, uncovering 1,985 accounts associated with the network comprising 466,357 inferred promotional placements. We find that the network promotes products across diverse categories through a growing pool of accounts, conducting coordinated campaigns spanning months across multiple platforms while evolving its listicle content over time. Across nine generative engines from both the US and China, we find that 4.5% to 20% of retrievable cited pages are attributable to the network, depending on how strictly attribution is drawn. On eight of these engines, its clients are named in 52% of answers, against 68% for category leaders. Our work demonstrates the effectiveness of UGC GEO placement at influencing generative engine outcomes, and reveals content-level defenses as insufficient against coordinated UGC placements, where account-level and platform-level signals are necessary for proper defense.

### DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents
- arXiv 2611.25583v1 · v1 2026-11-19 06:26 UTC · cs.AI
- Authors: Licheng Pan, Yuzhou Chen, Zhixuan Chu, Yichen Sun et al.
- Topics: GEO/AEO, Citation & source selection · score 13 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25583
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attribution, as perplexity or retrieval relevance alone cannot determine which retrieved memory would change agent behavior if neutralized; (2) Counterfactual attribution is prohibitively expensive for online detection, as it requires replaying downstream agent and tool execution for each candidate memory, exceeding real-time serving budgets. To address these challenges, we propose DriftGuard, a two-stage framework that decouples offline causal supervision from online estimation. Specifically, DriftGuard first constructs causal supervision through repeated paired counterfactual replays, continuing the original and single-memory neutralized trajectory suffixes from a shared pre-action state. The resulting annotations are aggregated by component-wise majority voting into a memory drift score (MDS) that captures action change, attack removal, violation removal, and task recovery. Guided by this supervision, DriftGuard then learns an online risk model that estimates MDS from pre-action information and flags drift-inducing memories via its maximum component risk, without online counterfactual rollouts. Extensive experiments demonstrate that DriftGuard accurately identifies drift-inducing memories and enables efficient online defense. Code is available at https://anonymous.4open.science/r/DriftGuard-7F0B.

### Seer: Guiding Small Deep-Research Agents with Shared Decision Models
- arXiv 2611.26423v1 · v1 2026-11-19 17:03 UTC · cs.AI
- Authors: Yuhao Zhou, Yang Zhou, Yuanxi Li, Jindi Lv et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.26423
- arXiv comment: 24 pages
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Deep-research agents repeatedly decide what to search, read, and verify, often using large cloud-hosted language models for action proposal. However, privacy and local control motivate running agents on users' devices, where limited memory and compute favor smaller models and complicate on-device training. Yet inference-time guidance faces three obstacles: exploring alternatives through real execution adds tool calls, prompted self-evaluation is bounded by the agent's judgment, and model-specific guidance risks repeated adaptation costs. We introduce Seer, an inference-time framework providing local guidance that separates the agent's action proposal from learned consequence prediction and value estimation. From a shared corpus of real research trajectories, we train two models: a tool-response simulator on observed call--response pairs and a value estimator on histories labeled with discounted terminal correctness. The simulator and estimator are trained offline and reused across agents without further training. Moreover, Seer executes only the selected action and adds only real tool responses to the committed history, avoiding tool calls on discarded candidates at additional inference cost. Across multiple deep-research benchmarks, Seer substantially improves agent performance for different language models. For instance, GAIA accuracy rises from 13.6% to 41.7% for Qwen3.5-4B and from 22.3% to 50.5% for Qwen3.5-9B. Furthermore, our analyses suggest that broader candidate coverage can compensate for imperfect simulation, while prediction and scoring errors limit the benefits of wider imagined search. These findings highlight the potential of reusable models for prediction and evaluation to strengthen small research agents through extra local computation without the real execution of the discarded candidates.

### MambaLIFT: Reference-Based Mechanism-Aware Attribution for VMamba
- arXiv 2611.25644v1 · v1 2026-11-19 07:28 UTC · cs.AI, cs.CV, eess.IV
- Authors: Jintu Kakati, Niladri B. Puhan
- Topics: Citation & source selection, RAG (generic) · score 9 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25644
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Attributing predictions of visual state-space models remains challenging because input-dependent selective dynamics couple feature selection, recurrent state propagation, and shared computational pathways. We introduce MambaLIFT, a reference-based, multiplier-first attribution framework for VMamba that propagates contributions through its computational graph using interaction-aware rules for selective-scan injection, recurrent memory, LayerNorm, and shared pathways. MambaLIFT decomposes the reference-relative class-logit difference, \(f_c(x)-f_c(x^0)\), by spatial position, VSS block, scan direction, and computational mechanism. Experiments on ImageNet-1K evaluate VMamba-T and VMamba-B, with hyperparameters selected on a calibration set and faithfulness assessed on a disjoint held-out evaluation set. MambaLIFT achieves numerical conservation to floating-point precision across audited attribution interfaces in both configurations. Under mean-colour pixel flipping, it achieves significantly higher mean faithfulness scores than MambaLRP on both configurations and the highest scores among the evaluated methods, including Integrated Gradients with matched references. Under blurred replacement, MambaLIFT is non-inferior to MambaLRP on VMamba-T and equivalent on VMamba-B, indicating that its advantage depends on the replacement protocol. Ablations on VMamba-T show that interaction allocation, temporal propagation, and pathway composition affect attribution maps. Mechanism-level analyses further show that exact relevance conservation does not imply additive effects under finite interventions: the mechanism decomposition accounts for the reference-relative logit difference but does not estimate intervention effects or establish causal validity.

### LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature
- arXiv 2611.25845v1 · v1 2026-11-19 09:59 UTC · cs.AI, cs.IR
- Authors: Pangjing Wu, Xu Yuan, Wenqi Fan, Qing Li
- Topics: Citation & source selection, Query fan-out · score 9 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2611.25845
- Full text: data/fulltext/2611.25845.txt

> Current research agents are moving beyond academic search toward literature synthesis and experiment planning. These workflows increasingly rely on literature retrieval systems, which serve as standalone systems or as components of research agents. However, existing scientific literature retrieval benchmarks mainly evaluate these methods using topical relevance or citation links as supervision, which cannot capture which prior methods are used for empirical comparison. To address this gap, we introduce Lineage, a benchmark for empirical lineage retrieval in AI scientific literature. An empirical lineage relation links a prior paper to a source paper that explicitly uses its method as an empirical comparison baseline. These relations form lineage graphs whose multi-hop neighborhoods provide retrieval ground truth for structural evaluation. To construct these graphs at scale, we develop Lineage-Constructor, which converts heterogeneous paper records and full-paper empirical baseline evidence into calibrated lineage graphs. Built from 121,048 papers across 17 top AI venues from 2018 to 2025, Lineage contains 3,950 graph components, 67,502 paper nodes, 164,948 lineage edges, and 80,000 multi-facet retrieval queries. Experiments with 19 representative retrieval systems show that empirical lineage retrieval remains challenging. Performance drops sharply with lineage distance, while structural metrics reveal that isolated retrieval hits often fail to recover closely connected empirical comparison neighborhoods.

### CANDID: Candidate-Driven Intervention for Disciplined Execution in Local Computer-Use Agents
- arXiv 2611.24977v1 · v1 2026-11-17 15:39 UTC · cs.AI, cs.CL
- Authors: Woongkyu Lee, Jungwook Choi
- Topics: Agents · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.24977
- Full text: data/fulltext/2611.24977.txt

> We present CANDID (Candidate-Driven Intervention for Disciplined Execution), an execution-control framework designed to enhance the reliability of local computer-use agents (CUAs) in resource-constrained settings. While local CUAs feature robust baseline proficiency in single-step action prediction, they frequently fail at critical junctions due to rigid action loops or premature DONE decisions. Rather than imposing imprecise cognitive loads through textual reflection, CANDID repurposes parallel test-time scaling into a disciplined, execution-level intervention at sparse, failure-prone points. We introduce a loop-recovery mechanism to filter candidates away from repeated behaviors and a conservative, unanimous DONE gating policy that requires absolute consensus to terminate. Experiments on OSWorld demonstrate that CANDID's structural control significantly improves success rates, outperforming feedback-based alternatives with minimal execution overhead.

### RouterWeave: A Unified Observation Layer for Cross-Platform Activity Analysis via Home Routers
- arXiv 2611.26134v1 · v1 2026-11-19 13:53 UTC · cs.NI, cs.HC
- Authors: Chengeng Liu, Ronghua Li, Yan Long, Shinan Liu
- Topics: Citation & source selection, Brand/product recommendation · score 8 · found via cs.HC
- Link: https://arxiv.org/abs/2611.26134
- arXiv comment: 17 pages, 7 figures
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Smart homes bring together devices from different operating systems and vendor ecosystems, but each platform reports activity only for the devices and features it supports, leaving gaps in household-wide activity monitoring. Interoperability standards such as Matter and software integrations connect and control supported devices, yet vendor restrictions and licensing barriers limit access to their data, while hardware constraints hinder integration. Our key insight is that encrypted network traffic provides complementary evidence of activity across platform boundaries. Accordingly, we present RouterWeave, a router-side observation framework that combines cross-platform traffic collection, task-adaptive processing, and unified activity records. These records preserve activity meaning, temporal extent, and source-device attribution while distinguishing discrete operations from sustained activity intervals. We evaluate RouterWeave across four datasets, native execution on a commodity home router, and two novel case studies: cross-platform Screen Time monitoring and appliance energy estimation. RouterWeave achieves 94.41% macro-F1 on application activities and 97.46% on IoT operations, outperforming baselines by up to 20.99 percentage points, while using under 7 MB of router memory per task and supporting 54 concurrent devices within a 5-second update window. In end-to-end case studies, RouterWeave reconstructs 600 Screen Time timelines across Android, iOS, and Windows with 92.15% accuracy (24.84-second mean active-time error over 19-minute averages) and recovers 49 of 55 appliance operations over four days, tracking ON/OFF states with 92.84% agreement and estimating electricity use within a 4.28% error. Together, these results establish the commodity home router as practical infrastructure for whole-home activity sensing. The code is open sourced at https://github.com/naisslab/routerweave.

### Visual Attribution Limits and Graded Provenance Auditing in Commercial Video-Generation APIs
- arXiv 2611.26508v1 · v1 2026-11-19 17:56 UTC · cs.CR, cs.CV
- Authors: Haocheng Mei, Yuchuan Tian, Yingte Shu, Chao Xu et al.
- Topics: Citation & source selection · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.26508
- arXiv comment: 23 pages, 2 figures, 13 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Commercial video-generation APIs bill by model and tier, while intermediaries could substitute cheaper models, lower tiers, or cached clips. What can a delivered file establish about its origin? We combine measurements of passive attribution and cryptographic provenance into a graded audit. We test attribution probes and zero-shot detectors under re-encoding, downscaling, and frame-rate changes, and survey C2PA and GB 45438 metadata across 19 commercial endpoints. Only authenticated provenance supports accusations: tier contradictions or duplicate signed instances under fresh-generation contracts, excluding retries and idempotent returns. Unverifiable signed-endpoint deliveries trigger original-file demands under pass-through clauses; archive-reuse and delivery-parameter screens support review only. Six-model container and bitstream accuracy falls from 83.9% on raw files to 45.3% after uniform re-encoding, using different feature sets. Subsampling real references from 24 to 3 fps raises pooled D3 AUROC from 0.845 to 0.988. Only BytePlus authenticates tier claims under our pinned policy, including 187/187 audited deliveries across three Seedance tiers; tested remuxing and re-encoding leave processed Seedance files unverifiable. The audit identifies authenticated contradictions in 100/100 raw 720p signed tier-swap cases, with zero observed false flags on the tested honest pools.

### User Perceptions of Deceptive In-Vehicle Infotainment User Interfaces
- arXiv 2611.25195v1 · v1 2026-11-18 21:15 UTC · cs.CR
- Authors: Pedram MohajerAnsari, Iwinosa Aideyan, Anna Galeano, Arjun Arunasalam et al.
- Topics: Brand/product recommendation, Clicks & measurement · score 7 · found via cs.CR
- Link: https://arxiv.org/abs/2611.25195
- arXiv comment: Accepted to the Network and Distributed System Security (NDSS) Symposium 2027
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Modern vehicles collect extensive data about drivers, passengers, and vehicle use, with privacy and consent decisions increasingly mediated through infotainment software. Although dark patterns have been widely studied in web, mobile, and e-commerce interfaces, little is known about how they appear in automotive infotainment systems or how users perceive them. We study this problem through Android Automotive OS (AAOS), conducting a three-phase empirical analysis. First, 26 HCI and privacy annotators audit four OEM AAOS emulators (Honda, Volvo, GM, and Polestar), documenting 17 dark-pattern types across 65 observations. Second, a user study with 100 participants compares OEM-specific implementations of five dark patterns across GMC, Honda, and Volvo, finding that implementation choices affect user perceptions. Third, an independent study with 49 participants compares automotive and e-commerce dark-pattern clips before and after a brief tutorial, showing that automotive's initial rating advantage largely collapses after instruction. Together, the studies identify a sophistication paradox: subtler dark patterns are less likely to trigger user suspicion and may therefore be harder to identify. These findings indicate that oversight should evaluate not just the presence but also the specific implementation of dark patterns.

### Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)
- arXiv 2611.26553v1 · v1 2026-11-19 18:23 UTC · cs.AI, cs.CR, cs.MA
- Authors: Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena
- Topics: Brand/product recommendation, Manipulation · score 7 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.26553
- arXiv comment: 21 pages, 5 figures, 13 tables. Project page: https://rogue-ai.surge.sh
- Full text: data/fulltext/2611.26553.txt

> Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Our results suggest that ROGUE-AI is able to reproduce the reported harm in 89% of its 108 attempted replications. Agents built on five current GPT, Claude, Gemini and DeepSeek models made the reported mistake in 18% to 33% of runs, against at most 1% without the blamed cause. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site. Replications without an attacker caused more harm than replications of prompt injection for all five models. Defenses against prompt injection look for injected instructions, but these replications contain none. Further, a warning after each tool output that names the hazard and its consequence lowered harm for all five models, whereas a note of the same length that does not mention the hazard left most of the harm in place. Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendors can rerun before each new release.

### WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation
- arXiv 2611.24011 · v1 2026-11-18 00:00 UTC · 
- Authors: Junlin Long, Xu Deng, Yiran Wang, Yue Yang et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.24011
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Arm-free quadrupeds can perform loco-manipulation, walking on three legs while manipulating with a front leg, yet no existing policy for it follows language instructions. World action models (WAMs) have emerged as effective language-conditioned manipulation policies, but are pretrained for robot arms and sample slowly. WAM-Policy turns one WAM into a quadrupedal loco-manipulation policy via two stages. The first, Cross-Morphology Policy Adaptation and Acceleration, adapts the arm-centric WAM to quadrupeds and distills the transferred policy into a student with one video and two action steps by on-policy self-distillation (OPSD). This student, however, is bounded by its teacher, which only imitates demonstrations. The second stage, Task-Specific Improvement and Merging, therefore tunes the teacher by reinforcement learning (RL) and merges the slow specialists into one few-step student by multi-teacher on-policy distillation (M-OPD). On QLM-Bench, ten simulated tasks with 1,000 demonstrations synthesized without teleoperation, the transferred policy reaches 77.0%, and the OPSD student keeps 76.7% while sampling 14 times faster. Task-specific RL and M-OPD lift it to 85.0%. We also deploy the OPSD student on a real Unitree Go2 Air. WAM-Policy thus achieves a stronger quadrupedal policy at a fraction of the inference cost.

### On the Impact of Feature Reduction Techniques on Adversarial Attacks
- arXiv 2611.25004v1 · v1 2026-11-18 18:12 UTC · cs.LG, cs.AI
- Authors: Mohammad Meymani, Roozbeh Razavi-Far
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25004
- Full text: data/fulltext/2611.25004.txt

> Adversarial attacks have posed significant threats to machine learning models by exploiting their inherent vulnerabilities. Researchers have established an interdisciplinary field called adversarial machine learning to explore these vulnerabilities and develop corresponding defense strategies. Feature reduction strategies are used to decrease the dimensionality of the data in order to reduce training time, avoid the curse of dimensionality, prevent overfitting, and mitigate redundant features. However, their effect on adversarial robustness across different classifiers and attack scenarios remains insufficiently explored. This study aims to analyze the effect of feature reduction techniques on the adversarial robustness of a diverse set of machine learning models under poisoning, backdoor, and universal adversarial perturbation attacks on the APT dataset. These models include support vector machine, decision tree, random forest, multi-layer perceptron, and k-nearest neighbors. The attained results are compared with scenarios where different feature reduction techniques are applied, including principal component analysis, permutation importance ranking, recursive feature elimination, and univariate mutual information. Metrics such as accuracy, F1-score, and mitigation score are employed to evaluate the effect of these techniques on adversarial robustness. The results demonstrate that permutation importance ranking and univariate mutual information generally provide the most consistent robustness improvements, while other methods exhibit more variable effects depending on the classifier and attack scenario.

### MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation
- arXiv 2611.25105v1 · v1 2026-11-18 19:39 UTC · cs.RO, cs.AI, cs.CV
- Authors: Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25105
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the highest success on all three real-robot tasks (laundry-bag collection, bath-towel folding, and umbrella handover), with 67.8% mean success, 18.9 percentage points above MA-VLA trained on the same demonstrations and cameras. In simulation, MAWAM reaches 90.3% mean success on eight tasks with teams of up to four arms. Ablations show that cross-agent attention and team-stage future-video supervision both improve coordinated control: without attention, a four-arm relay falls from 95.0% to 39.0%, and without this supervision, Place Food falls from 78.0% to 47.0%.

### Demonstration-Free Skill Composition for Navigation and Manipulation
- arXiv 2611.25462v1 · v1 2026-11-19 03:47 UTC · cs.RO, cs.AI
- Authors: Madeleine Nouri, Gelareh Mohammadi, Francisco Cruz
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25462
- arXiv comment: 10 pages. Accepted at the Australasian Conference on Robotics and Automation (ACRA 2026). Project page: https://madeleinenouri.github.io/acra-skill-composition
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Hierarchical reinforcement learning enables sequential tasks to be represented as compositions of separately trained skills. This paper evaluates demonstration-free hierarchical pipelines for MiniGrid navigation and robotic manipulation, comparing their training requirements and task performance with flat reinforcement learning baselines. The evaluation concerns complete pipelines with task-specific observation, reward and control structures. In navigation, two parameterised skills are reused across unseen FourRooms layouts under manually specified high-level plans. In manipulation, reaching, grasp alignment and lifting are trained separately, with downstream skills initialised from states collected during predecessor rollouts. Across unseen navigation layouts, the hierarchical pipeline substantially outperforms the evaluated flat DQN baselines while requiring fewer training interactions. In manipulation, the hierarchical chain requires fewer training steps than flat SAC and exhibits lower observed variation across seeds. The frozen Pick and Lift skills are further reused for stacking by training an additional Place skill.

### Passing NPCR Without Diffusion: Exact Signatures, a Detection Benchmark and an Audit of Published Image Ciphers
- arXiv 2611.25561v1 · v1 2026-11-19 06:06 UTC · cs.CR, cs.MM, eess.IV
- Authors: Mua'ad Alfarajat
- Topics: Clicks & measurement · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.25561
- arXiv comment: Accepted for publication in the Journal of Information Security and Applications. This is the submitted version; the accepted manuscript will replace it once the article's DOI is available. 31 pages, 5 figures, 16 tables. Code and records: https://doi.org/10.5281/zenodo.22796547
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> NPCR, the share of ciphertext bytes changed by a one-pixel plaintext change, is reported for nearly every image cipher as evidence of diffusion, with 99.61% the target. Several mechanisms produce values near it, and the mean does not say which. We separate three regimes: no propagation, one round of forward and backward chaining linear over addition or XOR, and independent ciphertexts. For the second an exact count applies. After a least-significant-bit change its mean asymptotically matches the independent-ciphertext reference, while its spread without cancellation is about five to twenty times larger. In simulation, the one-sided NPCR test of Wu, Noonan and Agaian flags one-round additive, mixed and S-box chaining in 2-4% of papers; read in both directions, the same five values flag at least 99.9%. Two-sided testing does the detecting; the spread and the other signatures help diagnose the structure. We then audit twenty-one published schemes. The count matches a reimplementation of one published diffusion layer on every trial and accounts for its reported table, the signatures show two schemes whose printed specifications cannot produce their reported values, and find that three of our own report plain-versus-cipher values and fall to two chosen images; ten more change their encryption material with the plaintext or per encryption, so their NPCR mostly reflects that change. A released checker applies the signatures to published tables, showing what a table measures within stated assumptions; it does not certify security.

### Diagnosis is not a policy: a state-transition audit of caoability-conditioned test-time inference
- arXiv 2611.25566v1 · v1 2026-11-19 06:09 UTC · cs.AI
- Authors: Yuchong Hu, Zhao Zhang, Kainan Liu, Haoyu Wang et al.
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25566
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Test-time actions can satisfy retrieval, state-realization, program-consistency, or rendering objectives without correcting an answer. Test-time Error Response and Realizability Audit (TERRA) is an evaluation/auditing protocol, not a new inference algorithm. It uses a unified decomposition of intervention outcomes into applicability, target-state realization, endpoint translation, harm, and resource/inference cost. Paired comparisons fix the incoming state and evaluation conditions; cross-model analyses vary the receiving configuration. Executable financial reasoning experiments yield three findings: the same context expansion can harm one configuration and benefit another; sufficient evidence does not ensure correctness because configurations differ in evidence-to-answer translation; and diagnostic headroom---accuracy attainable with idealized diagnostic information over the measured baseline---plus local consistency does not ensure practical gains. Action value is $V(a\mid x,m)$, not diagnosis alone; diagnosis is not a deployable policy $π(a\mid x,m)$.

### MetaScanner: An Empirical Study and Proactive Defense against Deceptive UI Attacks in Social VR
- arXiv 2611.25608v1 · v1 2026-11-19 06:55 UTC · cs.CR, cs.HC
- Authors: Junhee Lee, Seungwon Woo, Minseok Kim, Jongseop Kim et al.
- Topics: Clicks & measurement, Manipulation · score 6 · found via cs.CR, cs.HC
- Link: https://arxiv.org/abs/2611.25608
- arXiv comment: 23 pages, 21 figures, 6 tables. Accepted to Computers & Security. This is the authors' accepted manuscript
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Social virtual reality (VR) platforms have surged in popularity but continue to face significant security challenges, including privacy invasion and user manipulation. Yet, the security risks posed by deceptive content remain largely unexplored. In this paper, we introduce four novel deceptive UI attacks that covertly manipulate social VR users into performing unintended actions without their awareness. We show how adversarial content creators can embed seemingly benign scripts and interactive elements within carefully designed virtual worlds, deceiving users into unknowingly carrying out harmful behaviors. We implemented these attacks on VRChat, a leading social VR platform, and an IRB-approved user study involving 30 participants confirmed their effectiveness. To mitigate these threats, we propose MetaScanner, a proactive analysis system that efficiently scans virtual world assets, including scripts and interactive objects, to identify suspicious or deceptive elements before users are exposed to them. We demonstrate that MetaScanner can successfully detect all threats in test worlds where the four attack scenarios were implemented. Additionally, MetaScanner shows its lightweight nature, with an average scanning time of 5 seconds across 38 real-world assets.

### DNA: Unlocking Depth Scaling in CTR Models
- arXiv 2611.25659v1 · v1 2026-11-19 07:40 UTC · cs.IR
- Authors: Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou et al.
- Topics: Clicks & measurement · score 6 · found via cs.IR
- Link: https://arxiv.org/abs/2611.25659
- arXiv comment: 10 pages, 5 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Long user behavior sequences are among the strongest signals for click-through rate (CTR) prediction. Cross-attention makes these sequences practical for industrial ranking by keeping compute linear in sequence length. Yet the gains from stacking cross-attention layers taper off: on Taobao search, growing a cross-attention stack from 16 to 28 layers adds only 0.02 percentage points (pt) of AUC. We argue that the key-value side is the bottleneck. Each layer projects the same behavior sequence into keys and values, so adding depth gives the model more reads of a fixed sequence. We propose DNA (Dual-stream Nexus Attention), which lets the sequence itself evolve with depth. At each layer, the request representation (the search query, user features and scene) first reads the sequence. Each behavior token then attends to the updated request representation and uses what it reads to update itself, so the next layer reads a sequence shaped by the current request. The update runs once per request, all candidates share the resulting sequence, and both the reads and the update keep linear complexity in sequence length. At comparable forward FLOPs, DNA improves AUC over cross-attention stacks by 0.08 to 0.26 pt and keeps improving in the depth range where those stacks level off. DNA-4 is deployed in Taobao search. In an online A/B test against the production model, it improves CTR by 0.8% and GMV by 0.5%.

### TipDex-VTLA: Learning When to Refine Actions with Touch for Dexterous Manipulation
- arXiv 2611.25683v1 · v1 2026-11-19 08:01 UTC · cs.RO, cs.AI
- Authors: Xudi Ge, Yepeng Liu, Haifeng Liu, Enze Shi et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25683
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Changes in illumination can induce action drift in dexterous manipulation even when the physical state remains unchanged. Although existing vision--tactile--language--action (VTLA) policies incorporate tactile feedback, when and how touch refines actions under changing visual conditions remains challenging. We introduce \textbf{TipDex-VTLA}, a VTLA policy that combines estimated visual action reliability and tactile forecast verification to regulate execution-time refinement. Specifically, Visual Action Sensitivity Estimation (VASE) learns visual reliability from a frozen reference policy's action sensitivity to illumination perturbations. Tactile Anticipation and Correction during Execution (TACE) compares predicted and measured touch at matched times and combines the resulting discrepancy with visual reliability to gate bounded feature corrections for unexecuted actions. This effectively helps to refine actions under challenging unseen visual conditions. We evaluate TipDex-VTLA on four real-world dexterous manipulation tasks and the UniVTAC simulation benchmark. TipDex-VTLA trained on data collected under normal visual conditions, achieves average full-task success rates of 87.5% (resp. 73.8%) under normal (resp. challenging unseen) lighting in real-world tasks, significantly outperforming some state-of-the-art methods. We will release the collected data and source code.

### When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards
- arXiv 2611.25793v1 · v1 2026-11-19 09:22 UTC · cs.AI
- Authors: Yingshuo Wang, Weixiang Zhao, Guancheng Li, Jiahe Guo et al.
- Topics: Citation & source selection, RAG (generic) · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.25793
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multimodal safety guards increasingly generate rationales alongside safety predictions, yet whether these rationales are reliable remains largely unexplored. We systematically study *rationale hallucination* from two perspectives: visual rationale hallucination, where rationales contain unsupported visual facts, and safety attribution hallucination, where grounded content is assigned an incorrect safety interpretation. Across rationale-generation methods, multiple vision-language backbones, and safety datasets, we find that rationale hallucination is widespread and does not consistently diminish with higher classification accuracy or increased model scale. Further analysis of the Think-with-Image paradigm shows that hallucination is concentrated in fine-grained attributes and relations, while visual tools are often invoked infrequently or without sufficient spatial focus. Based on these findings, we propose *Tool-Contrastive Grounding Reinforcement Learning* (TCG-RL), which rewards tool use only when it improves rationale grounding over a tool-free reference. TCG-RL substantially reduces rationale hallucination while maintaining competitive safety prediction performance. By revealing the gap between prediction correctness and rationale reliability, our study motivates a shift in multimodal safety guarding from outcome-only evaluation toward safety decisions that are both accurate and verifiably grounded.

### Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation
- arXiv 2611.26444v1 · v1 2026-11-19 17:15 UTC · cs.AI, cs.CV, cs.RO
- Authors: Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin et al.
- Topics: Manipulation · score 6 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2611.26444
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess them separately without their composition, so they reveal little about whether a failure comes from reasoning, execution, or their composition. We introduce Mind2Act World, a diagnostic benchmark of 30 simulated manipulation tasks from five real-world application domains. Each task has three difficulty levels and two scene settings (Clean and Random), yielding 180 configurations. The tasks form three views: Mind tests decisions based on past observations, Act tests precise and timely execution, and Mind2Act combines both in closed-loop tasks where action outcomes guide later decisions. Comparing the three views shows whether a system lacks a capability or fails to compose capabilities it already has. A diagnosis harness further attributes the failed episodes of three representative systems to Mind, Act, or their composition and summarizes each system in a profile card. Our evaluation of multimodal agents, vision-language-action models (VLAs), and world-action models (WAMs) shows that competence in a single view does not carry over to Mind2Act tasks. Even the strongest agent succeeds in 52.7% of Mind and 39.0% of Act episodes but in only 12.0% of Mind2Act episodes. The strongest agent retains task state but struggles with sustained contact, whereas end-to-end policies execute practiced motions but retain little task state. These findings point to composing reasoning and execution through environmental feedback as the main open problem.

### PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation
- arXiv 2611.26596v1 · v1 2026-11-19 18:52 UTC · cs.RO, cs.AI
- Authors: Kai Lu, Chenyang Ma, Ioannis Havoutis
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.26596
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free components, allowing the VLA to focus on stage-specific skill dynamics. PGX decomposes long-horizon loco-manipulation into three layers: (i) a predicate-based state machine governs task progression, using physical predicates to gate phase transitions, trigger recovery, and coordinate navigation and waiting. Shared predicate semantics connect offline demonstration segmentation, online execution, and stage-wise evaluation; (ii) VLA skills operate within active manipulation phases, with flat or stage-trained models concentrating on task-relevant actions; and (iii) world-coordinate locking (WCL) maintains spatial consistency through base station keeping, object-relative positioning, and world-anchored contact targets. We demonstrate the effectiveness of PGX with extensive experiments conducted on three simulated tasks and one real-world task using a Unitree G1 humanoid robot for long-horizon loco-manipulation, showing improvements in stage progression and task success rates. Project page is available at: https://kl-research.github.io/pgx

### Retrieving Patristic References and Modelling Topics in Bullinger's Reformation Correspondence
- arXiv 2611.25247v1 · v1 2026-11-18 22:31 UTC · cs.IR, cs.CL, cs.DL
- Authors: Lena Pickartz, Philipp Schaer, Phillip B. Ströbel
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.25247
- arXiv comment: Accepted for the Seventh Conference on Computational Humanities Research 2027. To be published in the Anthology of Computers and the Humanities
- Full text: data/fulltext/2611.25247.txt

> The correspondence of Heinrich Bullinger (1504-1575), Swiss Reformer and Antistes of Zurich, documents the political and religious debates of the Reformation, including extensive appeals to the Church Fathers as authoritative sources. Detecting such references computationally remains largely unexplored. We investigate dense and sparse retrieval for patristic reference detection, and metadata-informed topic modelling as a proxy for the topics and ideas discussed. Prior work on Latin intertextuality has fine-tuned dense retrievers for their respective target domain, and we test how well these models transfer to Bullinger's correspondence. We compare lexical (BM25), dense (bi-encoders), and hybrid methods on explicit and implicit references. A Latin encoder fine-tuned on biblical reuse performs best among the bi-encoders (82%, Recall@20 on explicit and 16% on implicit references), while BM25 outperforms dense approaches on explicit citations (94%, R@20). Because BM25 and dense retrieval recover disjoint sets of implicit references, fusing their rankings raises implicit R@20 to 22%, close to cross-encoder reranking of the same candidates (26%) but without its inference cost. For topic modelling, we extend FASTopic with a seed-guided loss function and editorial abstract embeddings. Measurable coherence gains over the baseline remain minimal, but qualitative and temporal analysis shows that some topics track documented historical events. However, dominant topic weights barely exceed a uniform distribution, making topics unusable to inform retrieval. A pilot application of LLM-based concept induction (LLooM) further points towards a more human-interpretable alternative. Together, these results present a first approach to retrieving patristic references and modelling fine-grained topics in Bullinger's correspondence.

### VideoTrail: Interactive Video Foraging Through Hierarchical Visualization
- arXiv 2611.25377v1 · v1 2026-11-19 02:16 UTC · cs.HC, cs.IR, cs.MM
- Authors: Catherine Yeh, Bryan Wang, Fernanda Viégas, Martin Wattenberg
- Topics: Clicks & measurement · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.25377
- arXiv comment: 19 pages, 13 figures
- Full text: data/fulltext/2611.25377.txt

> People often watch videos to find information, but locating relevant moments can be difficult and time-consuming. Existing strategies like scrubbing rely primarily on visual scanning and linear search, providing limited support for goal-directed navigation. We present VideoTrail, an AI-powered browser extension that supports information seeking in videos through a hierarchical visualization. Inspired by information foraging theory, VideoTrail surfaces semantic and structural cues as information scent, creating an explorable roadmap of segments. The system is multimodal and adaptive, prioritizing visual or textual scent based on the video's content. In a user study (N=16), VideoTrail helped participants efficiently locate key moments and enabled new navigation strategies compared to traditional timelines, highlighting how exposing an adaptive video structure can enhance goal-directed viewing.

### LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented Generation
- arXiv 2611.25229v1 · v1 2026-11-18 22:01 UTC · cs.IR
- Authors: Haochen Liu, Guanghui Min, Song Wang, Yada Zhu et al.
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.25229
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large Language Models (LLMs) have demonstrated strong capabilities in open-domain question answering, but often struggle with factual accuracy and multi-hop reasoning due to the incompleteness of the training corpora. A promising solution is Knowledge Graph Retrieval-Augmented Generation (KG-RAG), which supplements LLMs with structured knowledge retrieved from external knowledge graphs (KGs). However, existing KG-RAG methods either rely on large-scale language models (e.g., ChatGPT) to guide the retrieval process, which leads to high computational costs, or suffer from limited retrieval quality when using lightweight language models, particularly under multi-hop scenarios. We propose LSP-RAG (Latent Scoring Perspectives for Retrieval-Augmented Generation over Knowledge Graphs), a novel KG-RAG framework that enhances hop-wise KG knowledge retrieval through multi-perspective prompted scoring. Each latent scoring perspective is guided by a combination of two types of soft prompts: a perspective-specific soft prompt induces a distinct prompt-conditioned scoring function over candidate triplets, while a contextual soft prompt evolves with each reasoning hop by encoding the query and previously explored KG triplets, enabling the model to preserve consistency and relevance across multi-hop retrieval. Rather than assuming manually defined semantic roles, these latent perspectives are adaptively aggregated to capture heterogeneous relevance signals during retrieval. This design allows LSP-RAG to perform accurate and robust retrieval using lightweight language models. LSP-RAG achieves superior performance across multiple KG-based Question Answering benchmarks compared to existing retrieval systems, including those that rely on much larger language models, demonstrating its effectiveness under limited computational budgets.

### AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development
- arXiv 2611.25582v1 · v1 2026-11-19 06:26 UTC · cs.CL, cs.AI, cs.IR
- Authors: Hang Zhang, Yuzhi Pan, Ziyao Zhong, Chaokun Wang et al.
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.25582
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substantial engineering effort and iterative experimentation, as effective design choices vary across tasks and domains. With rapid advances in LLM agent capabilities, we ask how well these agents can autonomously build RAG systems and how effectively they can improve them through iteration. In this paper, we propose AutoRAGBench, the first benchmark to evaluate how well LLM agents develop RAG systems from scratch in an open code space. It comprises nine RAG system development tasks. For each task, agents build RAG systems from scratch without starter code or prescribed strategies, under a six-hour budget on a single H800 GPU. They analyze task data, implement RAG pipelines, and iteratively refine their designs based on experimental feedback. We evaluate nine agent configurations and analyze both the effectiveness of the resulting RAG systems and their development trajectories. GPT-6.1 Sol with Codex CLI achieves the highest average score of 56.1. The composite Human-SOTA baseline averages 44.4. These results show that LLM agents can automate effective RAG system development. When starting from a human-designed system on each of seven tasks, GPT-6.1 Sol with Codex CLI improves the score by 16.6 points on average.

### Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem
- arXiv 2611.26398v1 · v1 2026-11-19 16:49 UTC · cs.IR, cs.AI, cs.CL
- Authors: Oriol Alàs, Ian Palacín, Iván Cester, Edgar Rubión
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.26398
- arXiv comment: 8 pages, 2 figures. Accepted at WDSA/CCWI 2026. Proceedings publication pending
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> EU-funded projects produce extensive evidence in the form of deliverables, reports, and case studies. However, this knowledge is typically scattered across projects and document structures, making it difficult to locate relevant, contextual information when making decisions. This paper introduces an Agentic AI Ecosystem that consolidates heterogeneous project documentation into a domain-aware knowledge base and provides adaptive access through an agentic Retrieval-Augmented Generation pipeline. Documents from three EU-funded projects (IMPETUS, NATALIE, and InnWater) are reconstructed into hierarchical section trees and indexed with structured metadata. Retrieval is supported by two domain-specific embedding models fine-tuned on domain data (water and climate). On top of this knowledge base, a ReAct-style controller iteratively orchestrates retrieval actions by allocating retrieval budget across domain collections and accumulating evidence until a stopping criterion is met. In a retrieval benchmark over the corpus, the proposed approach improves Mean Reciprocal Rank by 26.7% (relative) compared to a single-domain embedding baseline, indicating more consistent retrieval of relevant evidence to support cross-project knowledge synthesis and climate-resilient decision-making.

## Other new cs.IR papers, title only (13)
- LQ-Rec: Late Quantization for Sequential Recommendation — https://arxiv.org/abs/2611.25256
- Learning Generative Ranking Policies for Whole-Page Optimization — https://arxiv.org/abs/2611.25527
- Generative News Recommendation Reproduces Popularity: A Memorization-Based Analysis — https://arxiv.org/abs/2611.25606
- Uncontrolled source titles: When Nature, Science, and PNAS meet Scopus — https://arxiv.org/abs/2611.25627
- Exploring Semantic Table Search in Data Lakes — https://arxiv.org/abs/2611.25691
- STARK: Moving towards Personalized Agents That Truly Learn and Remember — https://arxiv.org/abs/2611.25705
- Can LLMs Resolve Entity Conflicts in Domain Specific NLU Pipelines? — https://arxiv.org/abs/2611.25733
- CACO: Coverage-Aware Coordinated Optimization for Continuous Generative Retrieval — https://arxiv.org/abs/2611.25738
- A Task-Level Bias Taxonomy for Historical Image Retrieval — https://arxiv.org/abs/2611.26019
- From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation — https://arxiv.org/abs/2611.26096
- The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting — https://arxiv.org/abs/2611.26521
- Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models — https://arxiv.org/abs/2611.26531
- Variants of Beam Search for DiskANN — https://arxiv.org/abs/2611.26609

## Already listed on an earlier day, still inside the look-back window (98)
- Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning — https://arxiv.org/abs/2611.20045 (score 23)
- GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk — https://arxiv.org/abs/2611.22223 (score 15)
- How Web Research Agents Interpret User Priorities — https://arxiv.org/abs/2611.22989 (score 14)
- The Fragility of Reasoning-Importance Attribution for Pruning Language Models — https://arxiv.org/abs/2611.22234 (score 13)
- Explainable Federated Learning via Global-Local Attribution Alignment — https://arxiv.org/abs/2611.20445 (score 11)
- DetouR: Plugging Association Routes into Search Agents for Multi-hop Question Answering — https://arxiv.org/abs/2611.19967 (score 10)
- EchoSpec: Training Search Agents to Weigh Evidence Above Echoes — https://arxiv.org/abs/2611.20034 (score 10)
- Dreaming Up Authors: Factual Prevalence and LLM Hallucinations in Academic Authorship Attribution — https://arxiv.org/abs/2611.23530 (score 10)
- X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction — https://arxiv.org/abs/2611.24283 (score 10)
- TUSI: A Citation-Grounded Graph-Based Benchmark — https://arxiv.org/abs/2611.21823 (score 9)
- IntentGR: Enhancing Intent for End-to-End Personalized Generative Retrieval in Search — https://arxiv.org/abs/2611.22788 (score 9)
- Can Decision Models Replace LLMs in Real-World Contact Center Classification and Judging Tasks? — https://arxiv.org/abs/2611.22949 (score 9)
- MMIntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu — https://arxiv.org/abs/2611.20448 (score 8)
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
- Entropy-Regularized Integrated Gradients for Stable Feature Attribution — https://arxiv.org/abs/2611.23600 (score 8)
- IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents — https://arxiv.org/abs/2611.24102 (score 8)
- How Complete Must an Environment Be to Train a Capable GUI Agent? — https://arxiv.org/abs/2611.23946 (score 8)
- Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness — https://arxiv.org/abs/2611.23346 (score 7)
- VoiceGuard: An Audio-Native LLM-VLA Pipeline for Wheelchair-Mounted Assistive Manipulation — https://arxiv.org/abs/2611.19984 (score 6)
- Can AI Judge You? An Empirical Audit of Deployment Readiness in LLM-assisted Hiring Systems — https://arxiv.org/abs/2611.20140 (score 6)
- AsymEEF: Bimanual Manipulation with Asymmetric End Effectors — https://arxiv.org/abs/2611.20557 (score 6)
- Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models — https://arxiv.org/abs/2611.20901 (score 6)
- Language-model agents' beliefs can be manipulated via truthful evidence in open channel — https://arxiv.org/abs/2611.21235 (score 6)
- Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models — https://arxiv.org/abs/2611.21517 (score 6)
- ALOHA Lightning: Learning Fast and Precise Manipulation — https://arxiv.org/abs/2611.21919 (score 6)
- RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't — https://arxiv.org/abs/2611.22179 (score 6)
- Where Does Hindsight Enter Clinical Agent Benchmarks? An Audit of Simulators and Case Construction — https://arxiv.org/abs/2611.22241 (score 6)
- A Full-Ledger Counterfactual Audit of Adaptive Reasoning — https://arxiv.org/abs/2611.22778 (score 6)
- Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate — https://arxiv.org/abs/2611.22904 (score 6)
- Data Poisoning Attacks to Locally Differentially Private Triangle Counting Protocols — https://arxiv.org/abs/2611.23701 (score 6)
- What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents — https://arxiv.org/abs/2611.24231 (score 6)
- AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents — https://arxiv.org/abs/2611.24313 (score 6)
- PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents — https://arxiv.org/abs/2611.24362 (score 6)
- SCR: Detecting Backdoor-Poisoned Samples through Clean-Reference Residuals — https://arxiv.org/abs/2611.24558 (score 6)
- Gradient-Based Defensive Poisoning Against System Identification Attacks on Cyber-Physical Systems — https://arxiv.org/abs/2611.24662 (score 6)
- Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web — https://arxiv.org/abs/2611.19900 (score 5)
- From Relevance to Utility: Rubric Alignment in Yuanbao Search — https://arxiv.org/abs/2611.22503 (score 5)
- KnowMe Paper Radar: Lightweight Discovery of Promising Papers in the Age of Autoresearch — https://arxiv.org/abs/2611.23702 (score 5)
- How did data sharing evolve in the decade since the FAIR Principles? — https://arxiv.org/abs/2611.20319 (score 4)
- Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First — https://arxiv.org/abs/2611.20378 (score 4)
- What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially Private Item Counts — https://arxiv.org/abs/2611.20388 (score 4)
- Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates — https://arxiv.org/abs/2611.20837 (score 4)
- When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents — https://arxiv.org/abs/2611.21577 (score 4)
- Teaching Language Models to Narrow Boolean Patent Searches from Search Feedback — https://arxiv.org/abs/2611.22270 (score 4)
- MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval with Multi-Category Solutions — https://arxiv.org/abs/2611.22509 (score 4)
- Learning Cross-Domain Media Similarity from Amazon Reviews — https://arxiv.org/abs/2611.22756 (score 4)
- GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation — https://arxiv.org/abs/2611.22274 (score 3)
- MARS Technical Report — https://arxiv.org/abs/2611.24006 (score 3)
- NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval — https://arxiv.org/abs/2611.22353 (score 1)
