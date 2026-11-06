# Paper candidates — 2026-11-06 (IST)

Generated 2026-11-06 08:27 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 21 new topic matches · 9 other new cs.IR · 124 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (21), highest score first

### The Popular Get More Popular: Auditing Brand Bias in Generative Search
- arXiv 2611.07614v1 · v1 2026-11-05 07:57 UTC · cs.AI, cs.CY, cs.SI
- Authors: Giorgio Monaco, Jacopo Lenti, Francesco Pierri
- Topics: GEO/AEO, Citation & source selection, Brand/product recommendation · score 22 · found via cs.AI, cs.CY, cs.SI
- Link: https://arxiv.org/abs/2611.07614
- Full text: data/fulltext/2611.07614.txt

> The shift from traditional to generative search has fundamentally transformed online product discovery. Because conversational recommendations synthesize choices into a few direct answers, subtle systemic preferences toward specific providers can exert profound commercial impacts. In this work, we audit this phenomenon through two distinct dimensions: (i) brand popularity bias, the systematic preference for market-dominant entities over long-tail alternatives, and (ii) brand familiarity bias, the ranking advantage an entity encoded in an LLM's parametric memory holds over an unfamiliar competitor. First, evaluating commercial queries across major engines, we observe persistent brand popularity bias: dominant brands in the top quintile are cited 1.4x to 2.8x more frequently than the average brand within a sample of 1,176 top market players, already present in parametric memory that external web retrieval fails to mitigate. Second, through controlled in-context experiments holding product attributes constant, we find that substituting authentic brand signatures with unfamiliar ones significantly degrades recommendation rank. Conversely, fact-preserving content rewrites yield negligible ranking gains. Taken together, our findings demonstrate that generative search engines reinforce a ``rich-get-richer'' dynamic by favoring established market leaders and imposing a parametric barrier to entry that standard content optimization cannot overcome.

### CORE: Coarse-to-Fine Search with Context Management for Deep Research
- arXiv 2611.07859v1 · v1 2026-11-05 11:36 UTC · cs.AI, cs.CL, cs.IR
- Authors: Hoang Tran Vuong, Ngoc Quan Pham, Hung Bui, Fatih Porikli et al.
- Topics: Query fan-out, Agents · score 14 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.07859
- arXiv comment: 24 pages
- Full text: data/fulltext/2611.07859.txt

> Deep research agents answer complex questions through repeated search. They rely on a harness that runs their tool calls and returns evidence to their context. This creates a trade-off: Search works best over long passages, which give enough context for reliable semantic matching. But the returned evidence should be short, because every observation stays in the agent's context for the rest of the trajectory. We introduce CORE, a training-free harness that combines coarse-to-fine search with context management. CORE retrieves passages with a dense retriever. It then reuses the token-level similarities from a late-interaction reranker to return only the most relevant snippet from each passage. Context management lets the agent expand the context around sources it has already retrieved and suppresses repeated snippets. In controlled closed-search comparisons with the Tongyi DeepResearch and OpenResearcher harnesses, CORE achieves state-of-the-art answer accuracy and evidence recall across three agent models and three benchmarks (BrowseComp-Plus, BrowseComp-Wikipedia and BrowseComp-Plus-CM), on corpora containing up to 553M documents.

### Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks
- arXiv 2611.07640v1 · v1 2026-11-05 08:25 UTC · cs.AI, cs.CR
- Authors: Rongting Zhang, Martin Bertran, Sandeep Avula, Chia-Jung Lee et al.
- Topics: Citation & source selection, Manipulation · score 10 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.07640
- arXiv comment: 34 pages, 6 figures. Code and data: https://github.com/amazon-science/task-tampering-prompt-injection
- Full text: data/fulltext/2611.07640.txt

> Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's dispute evidence can cite a false refund policy to inflate a refund without changing the task. We define IPI by authority rather than instruction-like wording: planted content constitutes an attack when it attempts to influence a decision that its source is not authorized to determine. We introduce a benchmark that makes this boundary explicit: in each of 90 validated cases across three tool-use environments, the user request specifies the source that resolves the targeted decision. Every attack tampers with a decision required by the benign task rather than replacing that task. Each case has attacks with the same harmful outcome that target up to six parts of the agent's decision making: its objective, decision rules, available actions, expected consequences, reading of observations, or beliefs about the current state. Without a defense, attacks on three of the five other targets (decision rules, available actions, and state) have higher mean success than objective attacks across five LLMs. A detection-and-removal defense reduces objective-targeting attacks to 2.4% success but leaves observation- and state-targeting attacks at 9.5% and 12.1%; this gap persists under detection-optimized rewrites. A tool-policy defense still allows 15.4% attack success, close to 17.0% without a defense, because these attacks generally retain expected tools and manipulate values obtained during execution. Evaluations whose attacks redirect the task or target only the agent's objective can therefore overestimate the coverage of these defenses. Code and data are available at https://github.com/amazon-science/task-tampering-prompt-injection.

### Consistent yet Contextual: Learning Author-Level Mixtures of Style for Authorship Attribution
- arXiv 2611.07111v1 · v1 2026-11-04 20:25 UTC · cs.CL
- Authors: Omkar Yadav, Michael Jiang, Kenan Alkiek, Jian Zhu et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.07111
- Full text: data/fulltext/2611.07111.txt

> Approaches to authorship verification or attribution typically model the style of a document, asking whether two documents were likely written by the same author. While recent approaches have been performant, such approaches largely ignore modeling the authors themselves and how varied their style is. Here, we introduce multiple alternatives for modeling the author and demonstrate that allowing an author's representation to capture multiple consistent but distinct writing styles yields significant performance improvements. Using our new authorship model, we then examine when an author writes in a way that is most idiomatic of their style across four scenarios: (i) variation in the size of their writing audiences, (ii) temporal distance from when the model was trained, (iii) the effect of preceding context, and (iv) the effect of genre norms on style. Across all four experiments, we demonstrate that authors vary substantially in how idiolectic their writing is. Our results have clear implications for both the modeling and data used for authorship verification and attribution, showing that authors need to be represented with their multiple styles and that some settings produce text that is much more informative about who wrote that text.

### Full Provenance on the COSS Causal Axis: An Event-Level Closure of Causal Attribution and Confused-Deputy Exclusion
- arXiv 2611.07164v1 · v1 2026-11-04 21:42 UTC · cs.CR, cs.DC
- Authors: Nicola Gallo
- Topics: Citation & source selection · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.07164
- arXiv comment: 19 pages
- Full text: data/fulltext/2611.07164.txt

> Provenance Identity Continuity (PIC) represents an authority-use event as an operation/resource behavior situated in a causal lineage, $(o,r,\ell)\in O\times R\times L$. We make the causal occurrence itself primitive: a represented security-relevant causal graph $(E,\to_c)$ in which each occurrence has a unique causal history, so the consistent event-lineage space is canonically isomorphic to $E$. The modeled execution has one causal partial order; distinct lineages are distinct causal histories inside it and may share a root while diverging into incomparable branches. PIC's $O\times R\times L$ is the authority-behavior projection of this space, and Causally Ordered Security-State (COSS) continuity generalizes it to an arbitrary behavior product over the same causal execution. On this semantics we prove an architecture-independent confused-deputy exclusion theorem. PIC continuation requires $C(e')\subseteq C(e)$ on every ordinary causal edge, so descendants are bounded by their ancestors; at an ordinary join, authority available on only one incoming branch cannot be resurrected, even when branches share a common root. Non-conservative combination must be an explicit authorized composition or relaxation event. With protected-effect mediation, an effect caused by request $q$ through an ordinary authority segment can exercise only authority in $C(q)$, so a confused-deputy state is contradictory. The result holds for any system whose protected request-to-effect causes are faithfully represented and whose ordinary authority transport satisfies PIC. We revisit Rajani, Garg, and Rezk: their value, control-flow, and initial-heap attacks are different witnesses of causal ancestry, so full provenance is an evidence mechanism for recovering edges of the causal graph, not the foundation of the PIC theorem. Finally we lift it to the COSS product of heterogeneous security-state coordinates.

### BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation
- arXiv 2611.07425v1 · v1 2026-11-05 04:20 UTC · cs.IR
- Authors: Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu et al.
- Topics: Brand/product recommendation, Ads · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.07425
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative recommendation retrieves items by autoregressively generating Semantic IDs(SIDs), where an RQ-VAE quantizes each item into a hierarchical SID sequence that the decoder generates level by level. We identify an overlooked bottleneck in this paradigm: the Semantic Quantization Gap(SQG). Quantization derives SIDs from rich continuous signals, including codebook centroids, local neighborhood geometry, and level-wise entropy. However, the decoder receives only discrete identifiers and loses the semantic structure that shaped them. This mismatch manifests in three ways: a grounding gap, where the decoder lacks semantic anchors when target-side information is limited; a neighborhood gap, where token-level supervision discards inter-item similarity and exacerbates exposure bias; and a difficulty gap, where computation is allocated uniformly despite generation difficulty diminishing with depth. To bridge the SQG, we propose BRIDGE. Codebook-grounded latent reasoning injects frozen quantizer centroids as semantic anchors before SID generation. Privileged EMA self-distillation transfers neighborhood-aware knowledge from a teacher to an on-policy student, preserving inter-item geometry while mitigating exposure bias. Effort-aware recurrence allocates more computation to the challenging early levels and progressively reduces it with depth. Across three Amazon benchmarks, BRIDGE improves Recall@10 and NDCG@10 by 10.9% and 9.7% on average over the strongest baseline (up to 12.6% and 10.7%). In a one-week online A/B experiment on a large-scale e-commerce advertising platform with 5% traffic, BRIDGE improves eCPM by 0.65%.

### ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality Hand Interaction by a Coding Agent
- arXiv 2611.08321v1 · v1 2026-11-05 17:18 UTC · cs.HC
- Authors: Bektur Ryskeldiev
- Topics: GEO/AEO, Clicks & measurement · score 8 · found via cs.HC
- Link: https://arxiv.org/abs/2611.08321
- arXiv comment: 10 pages, 2 figures, 1 table. Code: https://github.com/Apolotary/controlanything
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Connecting hand input in mixed reality (MR) to a nearby physical device typically requires an integration written in advance for that device, its transport and the mapping. ControlAnything defers this integration to the moment of use and assigns it to a coding agent. On a Meta Quest 3, the wearer selects an object outlined by SAM 3.1 and states what their hands should control. An agent built on Meta's Muse Spark model then writes a connector program on the wearer's laptop, tests it against the live device through hand-written MIDI, Bluetooth and key-press transports, and returns augmented-reality (AR) controls, a per-frame hand program, or both. These outputs are a form of generative UI, interfaces created by an AI model; here, the agent also generates and tests the code that binds the interface to a physical device. In a single-session technical evaluation with the author as the only wearer, nine of ten requests addressing five targets reached a ready state, and the wearer stopped one. The median time to ready was 32.5 s (range 24.9-57.8 s, excluding speech transcription); sequential model calls accounted for a median of 89.9% of this time, and 91.7% of input tokens came from the prompt cache. The system's evidence of success extends to transport acknowledgements but not to physical effects. These findings point to connector reuse and the observation of effects through the headset's own sensors as next steps for on-demand device integration in MR. A user study with first-time wearers is planned.

### Dynamic Watermarking and Action-Conditioned Latent Dynamics for Secure Vision-Based Controllers
- arXiv 2611.07403v1 · v1 2026-11-05 03:57 UTC · cs.RO, cs.CR, eess.SY
- Authors: Aditya Parameshwaran, Navid Aftabi, Abhishek Hanchate, Satish T. S. Bukkapatnam et al.
- Topics: Citation & source selection, Manipulation · score 7 · found via cs.CR
- Link: https://arxiv.org/abs/2611.07403
- arXiv comment: 8 pages, 3 figures, Submitted to ACC 2027 conference
- Full text: data/fulltext/2611.07403.txt

> Replay attacks are difficult to detect in vision-based control systems because previously recorded observations can remain plausible while the physical system follows a different trajectory. This paper develops an adaptive dynamic-watermarking framework for detecting replay attacks against vision-based controllers. A private Gaussian watermark is added to the nominal control input, and a control input-conditioned latent dynamics network (LDN) predicts the corresponding evolution in a compact latent space learned from image observations. Attack evidence is obtained from the discrepancy between the predicted latent response and the latent representation of the received image observation. A reinforcement learning policy adjusts the watermark covariance using the latent state and detector confidence, thereby balancing attack detectability, watermark energy, and control distortion. A Lagrangian penalty on task-specific safety costs is included during training to limit the adverse effect of the excitation. The framework is evaluated on a vision-guided UR5 manipulation task in which the robot reaches a target while avoiding a moving human arm under nominal and replay-attacked observations.

### SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection
- arXiv 2611.07222v1 · v1 2026-11-04 23:18 UTC · cs.AI, cs.CR
- Authors: Woosang Lim, Yeseul Chang, Jaewoo Lee
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.07222
- arXiv comment: An earlier version was accepted at the Third Workshop on Agents in the Wild: Safety, Security, and Beyond (NeurIPS 2026). 16 pages. Project page: https://saintmachines.github.io/spillway/ Code and per-cell results: https://github.com/saintmachines/spillway
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but need a model to plan or route each task first. Where an action goes can instead be read from the tools' typed returns: an email's sender or a payment's account arrives in a typed field, while injected instructions arrive as free text. SPILLWAY turns this observation into a deterministic floor with no per-task plan. The check admits a call when each target value that appears in tool output but not in the user's task was returned by a read-only tool in a typed field or is covered by a fixed delegation rule. A deterministic sanitizer removes instruction-like regions its fixed rules match before the model reads them and retains the removed spans as evidence, and a local judge may restore a refused call, never one whose target lies in the removed text. Across three backbones, and seven task suites on one of them, no standard templated injection redirects an action to an attacker's target under SPILLWAY, at the highest observed mean utility and composite scores (NRP, ERS) of the defenses we run under that attack. A forged chat template also produces a raw zero, and mean in-scope attack success under a released reinforcement-learning attacker is .007. SPILLWAY reaches this floor with no defense-triggered backbone re-run and almost no added model call. As personal AI agents act on users' email, files, and payments, SPILLWAY gives them an auditable refusal floor on where their actions go that keeps them useful and holds across backbones.

### VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations
- arXiv 2611.07272v1 · v1 2026-11-05 00:46 UTC · cs.RO, cs.HC
- Authors: Liuchuan Yu
- Topics: Manipulation · score 6 · found via cs.HC
- Link: https://arxiv.org/abs/2611.07272
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> VREgo trains manipulation policies from demonstrations recorded on consumer VR headsets; we instantiate it with EgoKit on one such headset, the PICO 4 Ultra. On-device head and hand tracking and stereo object localisation allow the operator to begin a demonstration at the table. We adapt HumanEgo's preprocessing to estimate grasp thresholds per recording, update object positions after release, and propagate segmentation masks between keyframes. We evaluate policies in simulation on two tabletop tasks recorded by one operator. For cube placement, we compare PICO and Project Aria recordings of the same 41 layouts. With 40 training demonstrations, the PICO policies placed the cube on the tray in 67, 74, and 60 of 100 evaluation layouts across three training seeds. The corresponding Aria results were 73, 78, and 0. For a two-stage stacking task recorded with the PICO alone, the baseline placed the block on the tray in 94 of 100 layouts and met the end-of-episode criterion for both placements in two. In one diagnostic episode, repeated replanning deferred release beyond the eight executed steps. Demonstration replays also showed that the open gripper could displace the cube before grasping it. After adapting the training trajectories and adding task-specific execution rules that use simulator object positions, the system met both placement criteria in 93.8% of episodes across four evaluation noise seeds. The same 100 layouts informed rule development and evaluation. VREgo is available at https://vrego.chuange.org/.

### Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model
- arXiv 2611.07513v1 · v1 2026-11-05 06:20 UTC · cs.CV, cs.AI, cs.RO
- Authors: Chengcheng Wang, Wei He, Wenhao Li, Hongguang Li et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.07513
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors bear no stable correspondence to physical displacements, or delegating continuous trajectory generation to a separate action expert whose gradients compete with or are blocked from updating the VLM backbone. We argue that manipulation and cognition should instead be embodied in the same model, shifting from a decoupled VLA to an Embodied Vision-Language Model (eVLM). We introduce Concertina, an eVLM that places continuous trajectory representation, blockwise generation, and physical-coordinate supervision directly on the computation and parameter path of a shared diffusion VLM backbone. Each control timestep is encoded as one continuous latent action token in the backbone hidden space, and the shared Transformer reconstructs temporally ordered action blocks via the same corrupt-and-reconstruct operator used for multimodal pretraining. Active action projections account for only 0.21% of parameters in the 4.46B model with zero separate action-generator layers, compared with 16.5%-35.1% dedicated action-expert capacity in representative continuous VLAs. Using our proposed Action Interface Audit, we confirm that cross-time trajectory coupling emerges in the middle and late layers of the shared backbone rather than at the action interfaces. On standard benchmarks, Concertina achieves 98.15% average success on regular LIBERO, 85.9% on the 10,030-task LIBERO-Plus benchmark, and 4.142 average completed chain length on CALVIN ABC-D. Code: https://github.com/lose4578/Concertina Hugging Face: https://huggingface.co/collections/Traly/concertina

### MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents
- arXiv 2611.07689v1 · v1 2026-11-05 09:14 UTC · cs.AI
- Authors: Yizhen Jiang, Haowei Guo, Tianyi Bai, Zengjie Hu et al.
- Topics: RAG (generic), Brand/product recommendation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.07689
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rather than building specific reasoning, execution, and memory failure risks into task construction. We introduce MCPHallu, a benchmark for diagnosing hallucination-prone agent failures in MCP environments along three axes: reasoning, execution, and memory. MCPHallu contains 358 tasks across five capability domains and runs on 36 production MCP servers in isolated containers. Each task is designed with a structural trigger that makes one of four subtypes the dominant failure risk: Branch Collapse, Unreachable Goal, Tool Misuse, or Context Forgetting. This design enables subtype-level analysis rather than aggregate task success alone. We evaluate fourteen frontier LLM agents from eight vendors on 5{,}012 trajectories. Current MCP agents remain vulnerable to hallucination-inducing tool environments, achieving an average score of 0.642 on a $[0,1]$ scale (higher is better). Failures concentrate on Unreachable Goal tasks, where the average score drops to 0.458 and 23.2\% of runs pass, indicating that agents often continue issuing tool calls or claim successful completion rather than recognizing infeasible goals. Subtype rankings diverge sharply: a model's rank shifts by 6.9 of 13 positions on average across subtypes, and Branch Collapse is uncorrelated with Unreachable Goal across models ($r = -0.12$). MCPHallu is released at https://github.com/J1zz/mcp_hallu.

### ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation
- arXiv 2611.07928v1 · v1 2026-11-05 12:33 UTC · cs.AI, cs.DC, cs.IR, cs.NI
- Authors: Petru Neague, Quinten Stokkink, Martijn de Vos, Rafael Pires et al.
- Topics: RAG (generic), Ads · score 6 · found via cs.AI, cs.IR, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.07928
- arXiv comment: 14 pages, 8 figures
- Full text: data/fulltext/2611.07928.txt

> Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG systems collect, index, and serve these documents from centralized stores. In practice, however, documents are owned by organizations, devices, and individuals who cannot or will not surrender custody of them to a central party, e.g., because of privacy, copyright or regulatory compliance. Existing modern decentralized retrieval techniques either reintroduce a coordinating authority, or rely on a global data structure that requires continuous network-wide coordination (e.g., DHTs). We present ZeroRAG, a decentralized routing layer for document retrieval in RAG that performs semantic query routing across an overlay of peers with- out global data structures or centralized orchestration. Documents remain with the peers that own them, and each peer keeps only lightweight local state: a bounded set of neighbor advertisements and a cache of recently routed queries. Using these, ZeroRAG steers each query through a best-first walk that progressively rewires the overlay toward semantically relevant neighbors, so recall improves over time as the network self-organizes. We evaluate ZeroRAG using three real-world workloads and two decentralized baselines. We find that ZeroRAG outperforms baselines in terms of recall and required network messages, approaches the recall and LLM answer accuracy of a centralized document store, self-heals after catastrophic peer failures, and scales to 100 000 peers.

### MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation
- arXiv 2611.08372v1 · v1 2026-11-05 17:50 UTC · cs.RO, cs.AI, cs.CV
- Authors: Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.08372
- arXiv comment: Project page: https://robin-lab.cs.utexas.edu/momasplat
- Full text: data/fulltext/2611.08372.txt

> Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view demonstration augmentation framework for mobile manipulation that synthesizes full manipulation trajectories from unseen robot base poses, including dynamic object interactions. Our key insight is that standard MoMa data collection naturally provides the multiview observations needed to reconstruct both the static scene and the manipulated object in 3D. MOMASPLAT combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to separately reconstruct the scene and manipulated object, render them from novel viewpoints, and generate geometrically consistent synthetic demonstrations paired with transformed actions. We evaluate MOMASPLAT on five real-world mobile manipulation tasks involving both rigid and articulated objects across three scenes, and validate the fidelity of its synthesized demonstrations against ground truth in simulation. MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

### What Gets Hacked in a Collaborative Reward for LLM Recommenders: The Part That Does Not Depend on the User
- arXiv 2611.07588v1 · v1 2026-11-05 07:39 UTC · cs.IR
- Authors: Zhuangsheng Li, Liang Dong, Yu Wu, Dailin Li et al.
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.07588
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Collaborative-filtering (CF) scores provide graded, personalized rewards for training large language model (LLM) recommenders through reinforcement learning. However, these rewards can cause exposure collapse: even though the CF model itself produces diverse top recommendations across users, an LLM optimized with its rewards concentrates on fewer items. We decompose each score into an item-mean component, the item's average CF score across user histories, and a residual component, the current user's score deviation from the average. Through controlled interventions, we identify the item-mean component as a contributor to exposure collapse. Accordingly, we propose two reward corrections: per-item centering removes each item's estimated mean score, while per-item standardization further rescales the residual using its estimated standard deviation. Experiments on two datasets with two identifier schemes show that both corrections substantially improve catalog coverage and exposure evenness. Compared with training on the uncorrected CF reward, our corrections increase the number of distinct items ranked first across users by up to $9.8\times$, while maintaining comparable ranking accuracy. Code is available at https://anonymous.4open.science/r/LLM4Rec-CF-Bias-27EF/.

### MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents
- arXiv 2611.07631v1 · v1 2026-11-05 08:17 UTC · cs.IR
- Authors: Mayank Anand, Subham Raj, Aman Vaibhav Jha, Sriparna Saha
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.07631
- Full text: data/fulltext/2611.07631.txt

> Long-horizon LLM agents require memory systems that preserve useful information across sessions and retrieve it when needed. Existing systems treat these as separate problems: memories are written prospectively with static importance scores that are never revised after use. This creates two coupled failure modes: consolidation can silently destroy evidence that future queries require, while retrieval continues to favor stale memories. We propose MEMOIR (Memory Evidence via Merge-certified, Online Importance Revision), a training-free memory lifecycle that unifies judge-gated consolidation with retrospective attribution. Before compressing memory, screening gates test whether answer-relevant evidence is preserved. After each query, attribution estimates which retrieved memories supported the answer and updates their retrieval priority. A UCB-style exploration bonus additionally encourages retrieval of under-exposed memories, reducing the risk that frequently retrieved memories crowd out useful but less-seen evidence. On 1,905 deduplicated LoCoMo QA pairs, the full retrieval stack improves evidence recall@5 by 11.92 percentage points over bare cosine, with confidence-gated feedback adding 1.50 points overall without reference answers or reranker training; a deployment-unavailable oracle adds 1.84 points overall and 8.05 points on multi-hop. Judge-gated merge changes the recall of text-based evidence from 58.82% to 59.08%, reduces the active store by 1.42%, and incurs 0 observed losses in 100 independently audited merges, with a one-sided 95% upper loss-rate bound of 2.95%. Together, these results outline a practical deployment path: no additional LLM call on the online write path, with merge screening confined to periodic offline consolidation. The lifecycle reduces to one principle: attribute usefulness after use, and screen for preservation before compression.

### What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays
- arXiv 2611.07650v1 · v1 2026-11-05 08:35 UTC · cs.SE, cs.AI
- Authors: Xiaodong Wu, Zhimin Zhao, Qi Li, Chaklam Cheong et al.
- Topics: Ads · score 4 · found via search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.07650
- Full text: data/fulltext/2611.07650.txt

> Third-party application programming interface (API) relays offer access to large language models (LLMs), often at lower prices. Users depend on these services for model quality, instruction compliance, and accurate billing. However, existing studies leave unclear whether relays meet these expectations together. We test 20 relays offering GPT-6 Astra and Claude Opus 5. First, we compare answers to knowledge questions with batch-matched official responses. In our first-round sample, the analysis flags 7/10 low-price and 2/10 same- or higher-price relays for behavioral differences. On retesting 35 pairs, seven gain or lose a flag under the original rules, and six under matched correction families. Because answer comparisons cannot reveal every delivery problem, we examine returned content and tool permissions. No injection is confirmed in 3,332 screened responses to a fixed, non-adversarial code and setup workload, yet four relays return tool calls despite instructions disabling them in the first round. Finally, to connect reported usage to actual costs, we compare input-token counts with official references and check balances. For identical requests, five relays report 4,200 to 60,000 more input tokens than the official API. Where balances are available (six services), charges follow reported usage at listed prices, including extra reported input tokens at one service. Our study shows that advertised models and prices are insufficient to judge relay reliability. It identifies unexplained billed token quantities and tool-permission violations as risks and shows why service evaluations need repeated measurements.

### Decision Models as Retrieval Gates Against Injection and Pollution
- arXiv 2611.08325v1 · v1 2026-11-05 17:19 UTC · cs.CR, cs.IR
- Authors: Mahdi Ghadamyari, Reza Habibi
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.08325
- arXiv comment: 5 pages, 3 figures
- Full text: data/fulltext/2611.08325.txt

> Retrieved web text can carry instructions aimed at the language model, or synthetic pages written to mislead. We test whether released open-weight decision models, which answer typed questions about a text without generating tokens, can screen retrieved passages against both threats. On a benchmark of 1,000 questions over forum-style web pages with hidden injected instructions, a Kev-4B gate reads each passage's HTML. Attack success, measured automatically, falls from 27.9% with no defence to 13.6% with the published mitigations (sanitisation, normalisation and citation prompting) and to 5.7% with the gate added. The gate takes 76 ms per passage and wrongly flags 4 of 186 benign pages with instructions for human readers. Responsiveness on clean queries stays within a point (85.6% to 86.2%). On a 200-query pollution testbed where two thirds of the candidate pages are fake, filtering the pool before the top ten are chosen keeps fake pages out of the answer (0.5% exposure) and holds accuracy at 83%, against 28% with no filter. Filtering only the top ten leaves the generator too few pages to answer. Large LLMs used as judges rank attacks better (AUROC 0.99 against 0.94) but cost ten times more. Gates catch more attacks when they read the page's HTML than when they read its plain text. Every model is open-weight.

### Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking
- arXiv 2611.07591v1 · v1 2026-11-05 07:41 UTC · cs.IR
- Authors: Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei et al.
- Topics: Clicks & measurement · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.07591
- Full text: data/fulltext/2611.07591.txt

> Re-ranking aims to present users with an ordered list that maximizes sequence-level utility. Industrial deployments widely adopt the Generator--Evaluator framework, where the generator proposes candidate sequences, and the evaluator scores them to select the best one for display. The fidelity of the evaluator's utility estimates thus directly governs recommendation quality. However, existing evaluators predominantly follow the \textbf{Independent Behavior Modeling (IBM)} paradigm, which simplifies the continuous user \emph{browsing journey} into independent per-item predictions (e.g., CTR). This oversimplification ignores two physical realities: (i) a click can occur only after the item has been reached and impressed, and (ii) items compete for finite user attention. As a result, IBM produces systematically biased evaluations and suboptimal sequence selection. To address this, we propose a \textbf{Joint Behavior Modeling (JBM)} perspective that explicitly models the \emph{display} $\rightarrow$ \emph{impression} $\rightarrow$ \emph{click} process to capture causal and competitive dependencies within a sequence. Building on JBM, we develop the \textbf{Impression-Click Evaluator (ICE)}, a plug-and-play framework that (i) predicts a browsing-depth distribution to estimate per-position impression probabilities, (ii) leverages predicted impressions to suppress spurious context from unexposed items during click modeling, and (iii) introduces a click distribution matching objective to capture intra-sequence dependencies. Extensive offline experiments across diverse backbones, together with a 14-day online A/B test in the Taobao App (+0.70\% clicks, +3.67\% revenue) and full-traffic deployment, validate the effectiveness and robustness of our approach.

### Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial Objects
- arXiv 2611.07851v1 · v1 2026-11-05 11:30 UTC · cs.HC, cs.IR
- Authors: DaEun Choi, Daniel Lee
- Topics: Manipulation · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.07851
- Journal ref: UIST 2026 Posters
- Full text: data/fulltext/2611.07851.txt

> Most recommender systems treat user preferences as a single signal to infer and optimize, yet human preferences are a mix of a stable preference and situational preferences that turn on and off depending on context. Through Tasteply, we externalize this preference structure as manipulable spatial objects. Tasteply represents each situational preference as an attractor and the stable preference as an underlying global field. Users can adjust their feed by moving around the space and adjusting the strength of the global field, turning the preference structure that remains latent within the model into something they can see and act on directly to steer the recommendation algorithm. Through an exploratory study (N=5), we found that this spatial control was effective, along with its limits and future direction as a means of manipulating preference-based recommendations.

### CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment
- arXiv 2611.07393v1 · v1 2026-11-05 03:43 UTC · cs.IR, cs.LG
- Authors: Vihan Lakshman, Peter Baile Chen, Zhuohan Gu, Michael Cafarella
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2611.07393
- arXiv comment: 5 pages. Third KEIR Workshop @ CIKM 2026. Work in progress
- Full text: data/fulltext/2611.07393.txt

> Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches. In this paper, we argue that such cache-to-cache translation can provide utility beyond the original motivating application of real-time agent communication and can instead be utilized for retrieval-augmented generation (RAG). Building on the Cache-to-Cache (C2C) fusion framework, our proposed system CacheGraft encodes each corpus passage offline into a fused KV cache representation between a larger sharer model (4B parameters in our experiments) and a smaller receiver model (0.6B parameters) such that this cache can be injected into the receiver at query time with no need for the larger model. Across five QA benchmarks and two independent locally-run judges, CacheGraft improves answer quality over the text-only receiver baseline in 29 out of 30 comparisons, of which 17 of the 30 are statistically significant. Notably, these gains are zero-shot with respect to the fuser, which was never trained on retrieval data. These initial results suggest that latent-space document enrichment may be a promising avenue for enhancing the performance of RAG systems, particularly in compute-constrained settings where it is only feasible to deploy a small model at inference time.

## Other new cs.IR papers, title only (9)
- MapHub: Daily Relevance Heatmaps of New arXiv Preprints for a Research Community — https://arxiv.org/abs/2611.07174
- Reducing Representational Interference in Retrieval Embeddings with Trainable Prefix Tokens — https://arxiv.org/abs/2611.07298
- MEvince: Knowledge-Constrained LLM Reasoning for Technique Identification from Malware Reports — https://arxiv.org/abs/2611.07486
- OptST: Optimizing Semantic Tokenization for LLM-Enhanced Recommendation — https://arxiv.org/abs/2611.07523
- Persistent Retrieval for Conversational Agents: A Study of Retrieval Efficiency — https://arxiv.org/abs/2611.07899
- ArcadeDB in Python: An In-Process Multi-Model Database — https://arxiv.org/abs/2611.07971
- Probabilistic Relevance Decisions for Semantic Retrieval — https://arxiv.org/abs/2611.08014
- Domain-specific information retrieval — https://arxiv.org/abs/2611.08228
- GINGER: Spicing Up Graph-Based Vector Search — https://arxiv.org/abs/2611.08306

## Already listed on an earlier day, still inside the look-back window (124)
- Characterizing Adversarial GEO via Implicit Brand Injection — https://arxiv.org/abs/2611.04005 (score 21)
- IntentGEO: Intent-aware Generative Engine Optimization for Recommendation — https://arxiv.org/abs/2611.04225 (score 18)
- The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents — https://arxiv.org/abs/2611.03754 (score 13)
- Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce Relevance — https://arxiv.org/abs/2611.02758 (score 12)
- $τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems — https://arxiv.org/abs/2611.04459 (score 12)
- WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution — https://arxiv.org/abs/2611.06777 (score 12)
- ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud — https://arxiv.org/abs/2611.04879 (score 11)
- Securing Web Agents with the Compile-Then-Execute Paradigm — https://arxiv.org/abs/2611.06039 (score 11)
- StreamDuo: A Live Commentator and a Research Agent for Unseen Games — https://arxiv.org/abs/2611.01120 (score 10)
- Same Trajectory, Different Knowledge: Information-State-Aware On-Policy Distillation for Search Agents — https://arxiv.org/abs/2611.01987 (score 10)
- DR Pixel: Page-Native Deep Research with Vision-Language Models — https://arxiv.org/abs/2611.03097 (score 10)
- Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction — https://arxiv.org/abs/2611.03183 (score 10)
- Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents — https://arxiv.org/abs/2611.03384 (score 10)
- MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study — https://arxiv.org/abs/2611.03555 (score 10)
- Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification — https://arxiv.org/abs/2611.06662 (score 10)
- LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks — https://arxiv.org/abs/2611.06687 (score 10)
- Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions — https://arxiv.org/abs/2611.03052 (score 9)
- Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents — https://arxiv.org/abs/2610.41432 (score 8)
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
- CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines — https://arxiv.org/abs/2611.05862 (score 8)
- Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline — https://arxiv.org/abs/2611.06000 (score 8)
- Beyond Risk Cues: A Mechanism-Level Benchmark and Verifiable Debate for Scam Video Detection on the Web — https://arxiv.org/abs/2611.06110 (score 8)
- Beyond the Landing Page: Website Blocking, Tracker Visibility, and Human Alignment in Automated Web Crawls — https://arxiv.org/abs/2611.06197 (score 8)
- Presentation Sensitivity in Typed Decision Models for Subjective Text Evaluation — https://arxiv.org/abs/2611.06384 (score 8)
- U.S. State Guidance on AI in K-12 Education: A Comparative Content and Citation Analysis — https://arxiv.org/abs/2611.06762 (score 8)
- RuntimeTickets: Source-Grounded Security Obligations for Agent Skills — https://arxiv.org/abs/2611.03772 (score 7)
- From Benchmarks to Behaviors: A Framework for Auditing AI Agents — https://arxiv.org/abs/2611.03939 (score 7)
- ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix Reuse — https://arxiv.org/abs/2611.04259 (score 7)
- Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents — https://arxiv.org/abs/2611.04393 (score 7)
- Collaborative Search Meets Large Language Models: An Empirical Study — https://arxiv.org/abs/2611.04619 (score 7)
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
- LLM-based NPCs in Video Games: A Systematic Mapping Study — https://arxiv.org/abs/2611.05427 (score 6)
- The Devil is in the Context: Nine Dimensions of Prompt Injection Attacks — https://arxiv.org/abs/2611.04672 (score 6)
- Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning — https://arxiv.org/abs/2611.04673 (score 6)
- When Category Means Move: A Paired-Support Audit of Recommendation Logs with Random Insertions — https://arxiv.org/abs/2611.05006 (score 6)
- GRIDSHIELD: Verifiable Grid Feasibility and Manipulation Resistance in Privacy-Preserving Peer-to-Peer Energy Trading — https://arxiv.org/abs/2611.05816 (score 6)
- Risk Control Certifies Rates, Not Magnitudes: An Audit of Selective Fetal Biometry — https://arxiv.org/abs/2611.05851 (score 6)
- Information-Matched Auditing of Conversational Emotion-Shift Forecasting: A Leakage-Safe Evaluation Protocol — https://arxiv.org/abs/2611.05895 (score 6)
- Do Saliency Maps Fail Dense Breasts? A Chance-Normalized, Confounder-Aware Audit of Explanation Fairness in Mammography — https://arxiv.org/abs/2611.05909 (score 6)
- Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation — https://arxiv.org/abs/2611.06498 (score 5)
- EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees — https://arxiv.org/abs/2611.01977 (score 4)
- Multi-criteria Rating and Review based Recommendation Model — https://arxiv.org/abs/2611.02019 (score 4)
- DualEvolve: Dual-Level Self-Evolution of Mechanism and Orchestration for Recommendation — https://arxiv.org/abs/2611.04439 (score 4)
- OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer — https://arxiv.org/abs/2611.04720 (score 4)
- Auditing Multi-Proxy Explanations of Web User Preferences: Identification Boundaries and Abstention — https://arxiv.org/abs/2611.04997 (score 4)
- JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks — https://arxiv.org/abs/2611.05263 (score 4)
- HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation — https://arxiv.org/abs/2611.05319 (score 4)
- SciToT: Multimodal Tip-of-the-Tongue Retrieval for Scientific Papers — https://arxiv.org/abs/2611.05829 (score 4)
- PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries — https://arxiv.org/abs/2611.06349 (score 4)
- CST: Lightweight Risk Triage with Source-Grounded Evidence for Web Discussions — https://arxiv.org/abs/2611.01710 (score 3)
- Adversarial Robustness of Retrieval-Based Fact-Checking: Detecting and Mitigating Evidence Contamination — https://arxiv.org/abs/2611.02139 (score 3)
- Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation — https://arxiv.org/abs/2611.03747 (score 2)
- Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized Retrieval-Augmented Generation — https://arxiv.org/abs/2611.05900 (score 2)
- Bridging Low-Level Image Fusion and High-Level Semantic Understanding — https://arxiv.org/abs/2611.02896 (score 1)
- Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo — https://arxiv.org/abs/2611.03927 (score 1)
- QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution — https://arxiv.org/abs/2611.04625 (score 1)
- RAGCompass: Generalizable Retriever Routing via Reranking — https://arxiv.org/abs/2611.05596 (score 1)
- ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs — https://arxiv.org/abs/2611.06481 (score 1)
