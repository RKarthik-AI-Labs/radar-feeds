# Paper candidates — 2026-11-02 (IST)

Generated 2026-11-02 06:55 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 27 new topic matches · 11 other new cs.IR · 46 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (27), highest score first

### Search When Needed, Proceed When Reliable: Metacognitive Reliability Supervision for Efficient Agentic Search
- arXiv 2610.41738v1 · v1 2026-10-30 13:44 UTC · cs.IR
- Authors: Minhao Sun, Zhijing Wu, Xian-Ling Mao
- Topics: Query fan-out, Clicks & measurement · score 13 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41738
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Efficient agentic search requires large language models (LLMs) to determine whether they can reliably proceed with their current knowledge or need additional external evidence. Supervision based on final-answer correctness or trajectory-level feedback evaluates realized trajectory performance. However, observed trajectory performance is jointly shaped by stochastic generation, retrieval quality, and downstream reasoning. Such signals therefore provide only indirect evidence of how reliable the current decision state was and how retrieved evidence changed its reliability. An effective reward should encourage search when external information is needed and favor searches that contribute to the answer. To this end, we propose a metacognitive framework for training LLMs to make search decisions based on the reliability of their intermediate reasoning states. Our framework estimates the reliability of local conclusions to distinguish whether the current information supports proceeding without search from how much retrieved evidence improves that reliability. The current-state reliability score assesses whether the model can proceed without search. The search-action score measures how retrieved evidence changes estimated reliability. Together, these scores define a reliability-aware process reward for Group Relative Policy Optimization (GRPO), providing finer-grained supervision for search and no-search behavior. Experiments across seven question-answering benchmarks demonstrate that our method achieves a better accuracy-efficiency trade-off than strong agentic-search baselines. Our code and model checkpoints will be open-sourced.

### AgentShield: Fortifying Web Applications Against AI Agents and Agentic Browsers
- arXiv 2610.41181v1 · v1 2026-10-30 03:00 UTC · cs.CR
- Authors: Moiz Ali, Nafis Karim, Rownak Islam, Jyotirmay Chauhan et al.
- Topics: Agents, Manipulation · score 11 · found via cs.CR
- Link: https://arxiv.org/abs/2610.41181
- arXiv comment: To appear in Proceedings of IEEE Symposium on Security and Privacy Oakland (IEEE S&P 2027)
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> LLM-powered browser agents are transforming web automation by autonomously interacting with websites and executing complex workflows. However, the effectiveness of existing anti-bot defenses against these systems remains unclear. We present a systematic empirical evaluation of modern agentic browsers against widely deployed anti-bot mechanisms, characterizing their capabilities, limitations, and behavioral differences from humans. Our results show that many defenses designed for traditional automation struggle to reliably detect autonomous AI-driven agents. Accordingly, we introduce AgentShield, a behavioral fingerprinting framework that targets the Perception-Reasoning-Action (PRA) loop underlying agentic user clients. By leveraging dynamic web forms that progressively reveal content and capture fine-grained interaction telemetry, AgentShield exposes behavioral artifacts that enable differentiation between human users and autonomous agents. We further demonstrate Extinction-induced Policy Drift (EPD), a novel attack in which repeated obstruction of task completion causes agents to relax their safeguards and engage in unsafe behaviors. Finally, we present defensive prompt injection techniques that exploit agent-specific weaknesses to mitigate emerging forms of autonomous web abuse that rely on content extraction. Our results highlight both the shortcomings of current web defenses against agentic user clients and the feasibility of practical detection mechanisms tailored to this new generation of web automation.

### WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search
- arXiv 2610.16927 · v1 2026-10-30 00:00 UTC · 
- Authors: Yingtao Ren, Aolin Li, Cheng Cheng, Huiyun Hu et al.
- Topics: Query fan-out · score 10 · found via HF daily papers
- Link: https://arxiv.org/abs/2610.16927
- Full text: data/fulltext/2610.16927.txt

> Short-video search needs compact query rewriters that recover users' personalized intent from ambiguous queries under strict latency constraints. Existing LLM-based methods have improved rewriting by using synthetic reasoning and subsequent consumption-behavioral feedback. However, overemphasizing subsequent consumption can favor engaging content over the user's immediate need, causing intent drift even when rewritten queries are grounded in behavioral history. We propose WeFair, Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in WeChat short-video search. WeFair uses human feedback according to how directly it reflects personalized intent, assigning feedback fidelity to a progression from demonstration to preference to verification. We first mine actual queries and user reformulations from search sessions, and then screen them for contextual support. In the demonstration stage, a supervised fine-tuning curriculum progresses from large-scale context-to-query learning to reasoning and direct prediction on human reformulation and preservation. In the preference stage, direct preference optimization learns relative preferences from subsequent consumption feedback. In the verification stage, group relative policy optimization rewards exact agreement with reformulation or preservation targets to constrain intent drift. Further analysis shows that broad supervision benefits the full curriculum supervised training, while strict verification achieves better performance than auxiliary rewards. In offline experiments, WeFair-2B outperforms strong rewriting baselines in overall accuracy and intent preservation. An online A/B test shows relative increases of 2.593% in effective video-view rate and a 2.350% relative reduction in query reformulation rate. WeFair-2B has been deployed in the WeChat short-video search system, which serves over 100 million queries per day.

### AI evaluators favor job applications written by certain AI models, independent of candidate quality
- arXiv 2610.41866v1 · v1 2026-10-30 15:18 UTC · cs.AI, cs.CY, cs.MA
- Authors: Nicolò Pagan, Michael Andreas Ebling, Stefania Ionescu, Anikó Hannák
- Topics: GEO/AEO · score 10 · found via cs.AI, cs.CY
- Link: https://arxiv.org/abs/2610.41866
- Full text: data/fulltext/2610.41866.txt

> Job applicants increasingly use large language models (LLMs) to write cover letters, while employers deploy LLMs to screen them. In this all-AI setting, we ask whether the \emph{choice of model} affects hiring outcomes independently of candidate qualifications. We introduce a multi-model auditing framework pairing eleven LLM writer agents with nine API-hosted evaluator agents across ten job descriptions and fifty candidates per job. Four findings emerge. First, we identify a generative preference hierarchy: a consistent global ranking of writer models by evaluator acceptance, in which locally hosted models are systematically disadvantaged regardless of their license, compounded by self-preference bias where evaluators favour their own outputs. Second, evaluator models differ substantially in how much bias they introduce based on applicants' tool choice, offering actionable guidance for fairer screening design. Third, this hierarchy has measurable competitive consequences: in the most adverse pairing, approximately two (1.8) out of twenty-five qualified candidates are filtered out purely due to model mismatch. Fourth, a common mechanism explains the patterns above: writer preference and self-preference trace to a combination of how much each writer leans on specific stylistic cues and how strongly evaluators, often unanimously, reward or penalise those same cues. A further check finds little evidence that an unmeasured "writer fingerprint" remains once these same features are accounted for. We discuss implications for algorithmic fairness in employment, regulation of AI-assisted screening, and the design of auditing frameworks that can be reapplied as the model landscape evolves.

### BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed?
- arXiv 2610.41435v1 · v1 2026-10-30 08:39 UTC · cs.AI, cs.CL
- Authors: Anirudh Phukan, Tanya Goyal, Danish Pruthi
- Topics: Query fan-out, Agents · score 9 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2610.41435
- arXiv comment: Preprint
- Full text: data/fulltext/2610.41435.txt

> Given that AI agents can search the web broadly and deeply in real time, it is tempting to conclude that their outputs account for recent world events. We show that this conclusion does not hold in practice. While agents can search and easily find recent changes, the correctness of their responses depends on whether they search and what they search for. Popular agentic search benchmarks like BrowseComp cannot expose failures wherein agents do not recognize their own assumptions that should be verified, since these benchmarks explicitly state what needs to be found. In contrast, many user requests state only the final information need (e.g., an itinerary for a trip), leaving the agent to discover relevant changes (e.g., the temporary closure of a museum) and account for their consequences. To highlight such gaps, we introduce BlindToChange, a benchmark that measures whether agents proactively discover recent events that affect their responses. Our benchmark comprises requests for recommendations where an obvious candidate is no longer applicable due to a recent real-world event. These events are drawn automatically from Wikidata, allowing BlindToChange to be periodically refreshed. Strikingly, we find a big gap -- as high as 27.5 points, even at high reasoning effort -- in systems' performance, when the recent event is not explicitly mentioned compared to when we ask about it directly. Analyzing search trajectories, we learn that more than half of the failures can be attributed to the fact that agents do not directly search to verify whether a relevant fact has changed. Our benchmark highlights, and tracks, a new axis of progress, wherein systems account for recent information that is not explicitly mentioned in the user request.

### Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses
- arXiv 2610.40747v1 · v1 2026-10-29 15:54 UTC · cs.CL, cs.LG
- Authors: Xiaoyi Zhang, Haoqing Wang, Xinjie Zhang, Xiang Ming et al.
- Topics: Agents · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.40747
- arXiv comment: Project page: https://microsoft.github.io/Mage
- Full text: data/fulltext/2610.40747.txt

> Effective computer-use agents (CUAs) should seamlessly combine visual GUI interaction with code and terminal execution within a single policy. We present Mage-VL-Cowork, a 4B hybrid CUA trained from a general multimodally aligned checkpoint through an end-to-end, progressive five-stage curriculum across midtraining, SFT, and RL. To power this curriculum at scale, Mage-CUA-Forge replaces per-task agent construction with reusable, skill-conditioned generation workflows and application-specific preparers, synthesizing 293,806 desktop and web tasks across 6,915 skills while reducing recurring per-task expenditure by 82.6%. Rather than directly distilling a default teacher, we evolve the teacher harness and instantiate specialized CUA harnesses to yield high-quality trajectories alongside stage-specific supervision. Mage-VL-Cowork-4B finally climbs to 66.0% on OSWorld-Verified through different training stages with more efficient reasoning cost, achieving state-of-the-art performance at its parameter size and pushing forward the frontier of on-device intelligence.

### Language Models Show Conformity Bias in RAG: When the Majority Endorses a Poisoned Claim
- arXiv 2610.41012v1 · v1 2026-10-29 21:45 UTC · cs.CL
- Authors: Mehrdad Ghassabi, Audrina Ebrahimi, Zahra Zojaji, Amin Milani Fard
- Topics: RAG (generic), Manipulation · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.41012
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Retrieval-augmented generation (RAG) can expose language models to misleading evidence in retrieved documents. We investigate whether increasing the number of mutually agreeing poisoned documents affects a model's ability to detect misinformation. We evaluate 200 randomly selected questions from SciFact (random seed 38), comparing contexts with one poisoned and six healthy documents against contexts with six mutually agreeing poisoned documents and one healthy document. For Gemma-3-12b, poison-detection rates decrease from 25% (50/200) in the minority condition to 10% (20/200) in the majority condition. Among the 38 questions with different outcomes across conditions, 34 change from detected to undetected, while only four change in the opposite direction (exact McNemar test, p = 6.04e-7). This pattern is consistent with a conformity-like response to a majority of mutually agreeing poisoned documents. Our results provide initial evidence of conformity bias in RAG-based misinformation detection: Gemma-3-12b is substantially less likely to detect poisoned claims when they dominate the retrieved evidence.

### ReplayRCA: Measuring Post-hoc Diagnosis and Live Oversight of Agent Failures by Counterfactual Replay
- arXiv 2610.41025v1 · v1 2026-10-29 22:11 UTC · cs.AI
- Authors: Jeremy Canale, Fabien Soulis
- Topics: Citation & source selection, Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.41025
- arXiv comment: 29 pages, 10 figures, 16 tables. Code: https://github.com/jeremy1392/RCAreplay
- Full text: data/fulltext/2610.41025.txt

> When a language-model agent fails a multi-step task, can another model find the decisive mistake and fix it with a single action? We introduce ReplayRCA, a benchmark that scores such diagnoses by intervention rather than by agreement with annotations: the environment is restored to the state preceding the chosen step, the proposed action replaces the agent's own, and the same agent continues. The score, causal repair, is the continuation success rate minus that of a paired placebo that replays the agent's original action through the same mechanism. Two tracks share this protocol: a post-hoc autopsy, where the diagnoser sees the whole failed run and is told that it failed, and live oversight, where a supervisor watches the run unfold and may intervene once, before an irreversible action, without knowing whether the run will fail. Tasks come from OpsWorld, a deterministic, procedurally generated back-office environment with six difficulty levels, the last of which is multimodal (QR codes, handwriting). On 62 calibrated systematic failures, the best of 13 frontier models (Grok 4.7) reaches a causal repair of +51.3 points; the top eight models are statistically indistinguishable, the flagship models of the two largest vendors rank 8th and 12th, and 5 items are repaired by no model. Forcing a strong model to intervene at the last step costs it 17.1 points, so the last-step shortcut of annotation-based attribution benchmarks does not transfer. On 87 runs, the two best live supervisors are statistically tied and one of them is a small open-weight model (DeepSeek V4.1 Flash); the supervisor that is among the best post-hoc diagnosers (GPT-6.1 Sol) is the weakest live one (-14.5 points on the same runs, p = 0.002), so post-hoc diagnostic performance can be a poor proxy for live oversight. The environment and the evaluation code are released at https://github.com/jeremy1392/RCAreplay.

### Language Models Show a "Women-Are-Wonderful" Effect in Blame Attribution That is Not Just Leniency
- arXiv 2610.41116v1 · v1 2026-10-30 01:17 UTC · cs.CL
- Authors: Anika Sharma, Snehalkumar 'Neil' S. Gaikwad, Snigdha Chaturvedi, Shashank Srivastava
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2610.41116
- Full text: data/fulltext/2610.41116.txt

> This paper investigates the Women-Are-Wonderful (WaW) effect in language-model blame attribution: a favorable bias in which women receive more positive evaluations than men. Using 11,270 interpersonal conflicts from r/AmItheAsshole, we construct matched counterfactuals that vary the gender of the person being judged (the original poster) and the person affected (the counter-party). Across four language models, gender changes a minority of verdicts, but those changes consistently favor women. The effect is strongly role-dependent. Making the original poster a woman reduces the odds of blame by 9--52%, while making the counter-party a woman multiplies them by 2.7--9.2X. Counter-party WaW also varies across conflict types, strengthening in communication and relationship conflicts and weakening in family conflicts. Exploratory probes suggest that counter-party gender can shift judgments of sympathy, reasonableness, harm and protection. WaW is therefore not just leniency toward women being judged: models also judge conduct more harshly when it affects a woman.

### ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents
- arXiv 2610.41272v1 · v1 2026-10-30 05:25 UTC · cs.AI, cs.CR
- Authors: Yini Huang, Aiwen LU, Zhen Sun, Yi Han et al.
- Topics: Agents · score 8 · found via cs.AI, cs.CR, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2610.41272
- Full text: data/fulltext/2610.41272.txt

> Web agents are increasingly deployed to complete tasks autonomously on real websites, where adversarially injected content can induce them to perform unauthorized actions. Existing evaluations primarily use fixed attacks or focus on a single attack type, and evaluate attacks at the text level rather than through real state changes, thus underestimating how vulnerable agents are to diverse attacks. To address the gap, we introduce REEF, a benchmark of red-teaming executable environments with faithful verification for measuring the security vulnerabilities of web agents. REEF covers 9 verifier-grounded websites spanning travel, commerce, productivity, media, and communication, and pairs every authentic benign task with a malicious objective delivered through 5 attack types at both the user and the environment level. REEF's state-based verifiers provide the execution feedback that drives ANGLER, an adaptive near-miss-guided lure evolution framework for red-teaming. Rather than evaluating a fixed attack set, ANGLER uses outcomes from prior rollouts to guide LLM-based attack mutation and candidate selection, prioritizing near-miss seeds during refinement. Across 8 VLM-based web agents, ANGLER achieves an end-to-end attack success rate (ASR) of 20.36%, compared with 15.24% for the non-adaptive setting. Compared with attack-free execution on the same benign tasks, attacks generated by ANGLER reduce benign task success rate (BSR) from 61.9% to 44.4%.

### Cross-Interface Authorization for AI Computer-Use Agents
- arXiv 2610.41397v1 · v1 2026-10-30 08:07 UTC · cs.AI
- Authors: Genliang Zhu, Chu Wang
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2610.41397
- arXiv comment: 31 pages, 2 figures, and 7 tables. Includes formal results, two reference runtime mappings, mutation tests, commit-time race probes, source-shaped adapter checks, and a frozen external-source audit. Guarantees bind the registered deployment profile and declared effect semantics
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Computer-use agents act through graphical interfaces, command lines, APIs, scripts, and Model Context Protocol servers. A policy decision can be interface-invariant while its executable authorization is not: another route can bypass mediation, alter a security-relevant default, or commit after the authorized state has changed. We present a profile-bounded protocol for a fixed, versioned computer-use deployment. It enumerates effect-bearing routes and durable sinks, checks a route-to-sink enforcement cut, normalizes each concrete request to a canonical effect, issues a route-bound prepare ticket, and verifies the route, effect, grant, trace, profile, inventory, and authoritative state again at commit. A committed result requires an agreeing sink receipt. Under explicit assumptions, we prove profile-bounded refinement, matched-effect decision invariance, resistance to alternate-route laundering and declared cross-surface recomposition, commit-time state safety, and receipt-grounded outcomes. The reference profile registers 12 effect families, five interfaces, and 60 routes. Two structurally distinct runtime mappings produce 3,464 traces over 1,732 scenarios each: 960 commits, 2,312 denials, and 192 commits after re-preparation. An independent checker accepts every retained trace and pair and rejects 26/26 semantic regressions; coverage and normalizer suites reject 24/24 and 720/720 mutants; and 168/168 commit probes match their declared outcomes. A frozen-source audit passes 52 checks over 12 files from two independent hybrid runtimes and one public authorization substrate. Source-shaped adapter refinements commit 48/48 instrumented calls and reject 15/15 unbound cases. The resulting guarantees bind the declared profile and its effect semantics.

### Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents
- arXiv 2610.41432v1 · v1 2026-10-30 08:38 UTC · cs.CL, cs.HC
- Authors: Haoqing Wang, Xiaoyi Zhang, Sicheng Fan, Zhexin Zhang et al.
- Topics: Agents · score 8 · found via cs.CL, cs.HC
- Link: https://arxiv.org/abs/2610.41432
- Full text: data/fulltext/2610.41432.txt

> Computer-use agents increasingly tackle tasks ranging from everyday desktop activities to long-horizon professional workflows. Yet interfaces centered on screenshots and mouse-and-keyboard actions can impose a human-interaction prior, requiring repeated screen interpretation while leaving the computer's semantic and programmatic capabilities underexposed. We argue for exposing these capabilities and letting models choose and combine them. We introduce Hybrid Computer Use (HCU), a unified interface for general agents that combines three complementary channels: programmatic interaction through code and command-line tools, semantic interaction through accessibility (AX), and visual interaction through graphical user interfaces (GUI). Our HCU supports efficient AX interaction and guards against stale-state actions during channel switching. A supplementary HCU skill guides agents in selecting and coordinating channels to use the unified interface effectively. Our designed AX tools return compact observations, execute actions in batches, and report their effects as AX diffs, so the model needs fewer round trips. On OSWorld 2.0, HCU achieves the highest Partial and Binary scores among the compared systems. Analyzing agent trajectories, we find that all evaluated models improve with HCU yet allocate work across the channels differently and consistently outperform compared baselines in terms of both efficiency and task success, highlighting the value of unified computer-use interfaces that allow flexible channel selection and combination.

### Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products
- arXiv 2610.42032v1 · v1 2026-10-30 16:59 UTC · cs.CR
- Authors: Tina Rezaei, Suzan Bayhan, Andrea Continella, Jeroen van der Ham-de Vos et al.
- Topics: Brand/product recommendation · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2610.42032
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> The Internet of Things (IoT) has expanded beyond consumer smart homes to sectors, such as industrial systems, healthcare, and smart cities, broadening the IoT attack surface. Prior empirical work has focused on studying aggregate IoT vulnerability characteristics or specific protocols, so patching is directed by aggregate security guidance. However, if dominant weaknesses differ substantially across sectors or products, such uniform guidance misdirects the remediation effort. To address this gap, we present a fine-grained, data-driven analysis of IoT vulnerabilities using a dataset of more than 15,000 IoT specific CVEs. We design a pipeline to enrich noisy CPE (Common Platform Enumeration) metadata, normalizing vendors and products, then assigning product type and sector labels using lexical matching, fuzzy clustering, and LLM-assisted classification. We find meaningful differences in the weakness profile of IoT sectors. For example, healthcare is dominated by authentication and credential weaknesses, while automotive faces memory issues. More importantly, we find that weakness profiles are more similar across different product types from the same vendor than across the same product type built by different vendors. This suggests vendor-level factors such as shared code and development practices dominate weakness inheritance, making a vendor's disclosure history informative about its other products. Our findings suggest weakness classes should be used to prioritize remediation efforts.

### Wizard: Manipulate Any World in Real Time via Agentic Control
- arXiv 2610.40339 · v1 2026-10-29 00:00 UTC · 
- Authors: Yuzhe Wu, Zijun Lin, Yeying Jin
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2610.40339
- Full text: data/fulltext/2610.40339.txt

> Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined motion patterns, generalize poorly to unseen environments and characters, and offer limited real-time interactivity. In this paper, we introduce Wizard, an agentic game world model that enables real-time, precise control over character motions while generalizing zero-shot across novel scenes, characters, and actions. To achieve this, we construct a diverse dataset spanning 750 scenes and 178 characters, incorporating skeleton and geometry information as structured representations. We leverage these representations as intermediate proxies to condition a video generation model, together with an adaptive masking mechanism that improves alignment between the conditioning signals and generated video rollouts. Furthermore, we introduce an agentic framework that explicitly maintains and updates game states, allowing players to freely configure their virtual worlds and exercise fine-grained control over character motions while preserving visual quality and gameplay consistency. By combining agentic control with structured proxy-based generation, our framework unlocks new possibilities for player-driven game creation with real-time, generalizable, and mechanically consistent world simulation.

### From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation
- arXiv 2610.40828v1 · v1 2026-10-29 18:07 UTC · cs.RO, cs.AI, cs.LG, eess.SY
- Authors: Ammar N. Abbas, Aayush Jain, Prashanth Viswanath, Nivesh Gadipudi et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2610.40828
- arXiv comment: Accepted at CoRL 2026 Workshop
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion. However, real-world performance remains difficult to predict, as conventional optimization signals such as validation loss show no consistent relationship with robot success. To identify the design choices that govern real-world performance, 281 imitation-learning policies spanning seven policy families were evaluated in approximately 1,700 real-robot trials of RJ45 connector grasping and insertion using a five-fingered robotic hand. Controlled ablations showed that observation and action representations dominated conventional optimizer and sampling choices. For point-cloud policies, region-of-interest cropping, representation in the robot-base frame, and normalization within the point encoder each improved success by 70-100 percentage points. For the vision-language-action policy, absolute rather than relative action prediction improved insertion success by up to 70 percentage points. Skill decomposition, multi-view perception, and recovery demonstrations were associated with the strongest-performing systems, although their effects were not independently isolated. Of 67 offline metrics evaluated, only five measures of predicted-motion smoothness and directness reliably correlated with insertion success (r = -0.70 to -0.80), and only within a single policy family. These results identify representation choices as key determinants of real-world imitation-learning performance and show that offline metrics can shortlist policies, but cannot replace real-robot evaluation.

### Real Computation or Merely Naming? A Pre-Registered Mechanism Audit of 25 Cognitive-Architecture Modules in an LLM-Based Agent System
- arXiv 2610.41604v1 · v1 2026-10-30 11:38 UTC · cs.AI
- Authors: Peter Chen, Ni Zhang, Ying Xu, Siyuan Zhang
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2610.41604
- arXiv comment: 40 pages. Static audit of 25 cognitive-architecture modules (18 carry no computed value to any production output), pre-registered interventions on 11 modules, 61 frozen criteria (53 confirmed / 5 falsified), two repair controls (0.028 -> 1.000 task success; -52% error). Artifact: https://doi.org/10.5281/zenodo.23433900
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Agent systems built on local large language models are increasingly marketed through the vocabulary of cognitive architecture: modules named global workspace, theory of mind, causal reasoning, or active inference are listed as features, and the presence of the name is taken as the presence of the mechanism. We ask the prior question -- does the named computation actually happen -- and contribute a transferable verification method for the claim-implementation gap: a four-question static audit protocol with line-number evidence and call-chain tracing, demonstrated on two systems. We audit a system claiming 25 cognitive mechanisms, pre-register falsifiable predictions for 11 modules and execute the interventions, replicate the protocol on the IIT-phi core of a second, independent system with its own pre-committed falsification criteria, and run two repair experiments as positive controls. In 18 of 25 modules the computed value never reaches any production output; three idle-wiring shapes new to the dead-code and code-smell literatures emerge (connected-but-never-called, called-but-inert, called-but-content-blind). Of 61 frozen criteria across 12 interventions, 53 were confirmed, two partially adjudicated, five falsified, one adjudication-ambiguous. Repairs raised planner task success from 0.028 to 1.000 and cut state-controller error by 52%. Module names and module computations must be audited as independent claims; the protocol and the five-class failure taxonomy are reusable for the claim-implementation gap at two-system, case-level depth.

### When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity
- arXiv 2610.41970v1 · v1 2026-10-30 16:21 UTC · cs.AI
- Authors: Jun Liu, Dajie Sun, Zhenglun Kong, Zhenjiang Fan et al.
- Topics: Clicks & measurement · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2610.41970
- Full text: data/fulltext/2610.41970.txt

> World-action models increasingly apply test-time scaling, spending extra inference computation on candidate selection and adaptive allocation to improve control. Such gains are credible only when candidates carry exploitable signal, nominal compute savings become real speedup, and evaluation stays reliable. We audit all three on Cosmos Policy and RoboCasa with a premise-first, pre-registered methodology. On clean data, a learned value selector is 1.66 pp worse than random; a hindsight oracle gains only 1.40 pp, with an episode-level interval spanning zero; and 82% of states show identical candidate outcomes, leaving little selection headroom. Token pruning cuts per-forward FLOPs by up to 47% but yields at most a measured 1.15$\times$ end-to-end speedup on the deployed path (1.25$\times$ on a decode-excluded path), short of a 1.5$\times$ target, and our adaptive-allocation experiment is inconclusive under a power gate. We further identify and fix a silent rendering corruption whose rate rises sharply along compute-heavy planning paths while leaving the official direct-policy result unaffected, and release a detector, fix, and scripts. These findings show why test-time scaling should be audited as a chain of premises (decision signal, realized efficiency, evaluationintegrity) rather than by success rate alone. Conclusions are scoped to the tested configuration.

### SecPO: Principled Adversarial Training for Prompt Injection Security
- arXiv 2610.41998v1 · v1 2026-10-30 16:43 UTC · cs.AI, cs.CR
- Authors: Sizhe Chen, Yibo Peng, Jaewon Chang, Chawin Sitawarin et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2610.41998
- Full text: data/fulltext/2610.41998.txt

> Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers from attack success rates (ASRs) approaching 100% under adaptive prompt injections. One reason is that DPO anchors the model around the undefended reference model, which is insecure. We show an idealized reference model---an injection-invariant, utility-preserving oracle---can nevertheless be approximated, as its output distribution in training is interestingly accessible. This new observation motivates a theoretically principled SecPO loss. Another Meta-SecAlign shortcoming is that it trains on weak simulated attacks. We implement an efficient adversarial training (AT) pipeline that synthesizes strong injected inputs (best@240), and train the model on them. Our AT reduces ASRs by 1.5-14.5$\times$ across three SoTA adaptive attacks, compared with Meta-SecAlign; the SecPO loss reduces them by a further 2.4-4.6$\times$ compared with using DPO loss. In agentic workflows, our SecPO + AT Qwen3.6-27B is much more secure than Meta-SecAlign: 8.8% vs. 78.8% AgentDojo ASR@800 under the AttackerMovesSecond attack. Moreover, our defended model shows no noticeable reduction in benign utility in nine benchmarks covering agentic tool calling, instruction following, science, and math. We release our $\href{//github.com/Sizhe-Chen/SecPO}{\text{code}}$, $\href{//huggingface.co/datasets/Sizhe-Chen/Qwen3.6-27B-Instruct-SecPO-trainset}{\text{training data}}$ (with optimized injections from AT), and $\href{//huggingface.co/Sizhe-Chen/Qwen3.6-27B-Instruct-SecPO}{\text{model}}$.

### Prevented is Not Protected: What Attack Success Rate Hides about RAG
- arXiv 2610.40742v1 · v1 2026-10-29 15:21 UTC · cs.CR, cs.CL, cs.IR
- Authors: Chahana Dahal, Zuobin Xiong
- Topics: RAG (generic), Manipulation · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2610.40742
- Full text: data/fulltext/2610.40742.txt

> Retrieval-Augmented Generation (RAG) is vulnerable to knowledge poisoning, where adversaries manipulate retrieved evidence to influence model outputs. Existing defenses are primarily evaluated using attack success rate (ASR), which obscures defense-induced failures and the mechanisms behind apparent attack prevention. To address this issue, this work introduces \textbf{Aligned RAG Evaluation}, a matched-query protocol that jointly examines clean and poisoned responses, with and without defense. By combining matched conditions analysis, LLM-judge endorsement, and retrieval dependence controls, the proposed framework distinguishes prevented from introduced failures, target mentions from LLM endorsement, and single-passage influence from evidence composition. Experiments on HotpotQA and Natural Questions reveal that existing defenses can introduce unexpected target-positive answers, although they can prevent some attacks, while evaluation criteria can also change defense rankings. Our findings expose critical blind spots in ASR-based evaluation and motivate a more comprehensive assessment of RAG poisoning defenses. The code and the evaluation artifact are available at https://github.com/chxhana/aligned-rag-eval.

### Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses
- arXiv 2610.41172v1 · v1 2026-10-30 02:48 UTC · cs.IR, cs.AI, cs.CL
- Authors: Zhichang Yu, Baining Cao, Sbaaoui Idriss, Qi Wang et al.
- Topics: RAG (generic), Agents · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41172
- arXiv comment: 13 pages, 2 figures
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Retrieval-augmented generation is becoming agentic. A search harness writes queries, reads results, reformulates, and decides when to stop. This largely solves accuracy: a harness with only BM25/grep and MiniMax M3 answers 85% of BrowseComp-Plus and 91% on multi-hop FRAMES in our runs, without compiled or vector indexes. It exposes a context problem: an undisciplined loop repeats queries, rereads documents, and fills the window with unused passages. The missing layer is knowledge compilation: a configurable ingestion pipeline where LLMs enrich documents with context no chunk contains alone--navigation hierarchies with claim-evidence leaves, entity graphs, timelines, mind maps, ontologies, wikis, and memory. Compilation is not a better retriever: under a competent harness, structural artifacts gave no detectable accuracy gain on FRAMES, and a PageIndex-style outline degraded at scale. It is a supply layer. A navigation tree whose leaves are claim-evidence pairs--the mechanism we measure--cuts query tokens by 91% when evidence suffices and adds 1.9% when it does not, a 38% average reduction; this implies a 2% break-even sufficiency rate and a measured rate near 43%. A decision gate cuts latency from 140 s to 30 s, though substitution's token saving is bought with retrieval rounds and carries its own latency cost. Other artifacts--ontology, graph, wiki, timeline, mind map, memory--pay off in deployment (governance, integration, onboarding, temporal orientation, continuity) where accuracy benchmarks cannot see them. We describe RAGFlow's pipeline and harness (open source at https://github.com/infiniflow/ragflow), which turns the loop into five disciplined stations and keeps the context entering the model the smallest sufficient set; together they form an agent-native database: a store that hands the agent compiled, governed context instead of a ranked list of passages.

### ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science
- arXiv 2610.41396v1 · v1 2026-10-30 08:06 UTC · cs.IR, cs.AI, cs.CL
- Authors: Wenliang Liang, Zhiyuan Ning, Haolin Chen, Yuanchun Zhou et al.
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41396
- arXiv comment: Accepted to NeurIPS 2026 (Evaluations and Datasets Track). 48 pages, 4 figures. Wenliang Liang and Zhiyuan Ning contributed equally. Code: https://github.com/kg4sci/ProSearch. Data: https://huggingface.co/datasets/kg4sci/ProSearch
- Full text: data/fulltext/2610.41396.txt

> In AI for Science scenarios, experimental design and method reproduction require retrieving protocols that satisfy multiple interdependent constraints, yet existing benchmarks lack systematic evaluation of this capability. To address this gap, we introduce ProSearch, a benchmark for multi-constraint protocol retrieval in experimental science. ProSearch has three key features: (1) realism, with queries grounded in real experimental records and expert-defined templates; (2) complexity, with 60 experimental fields and their dependencies; and (3) diagnosticity, with 3-5 explicit constraints per query, including numerical and negation constraints. We construct ProSearch through LLM-based extraction, data-driven constraint selection, controlled query generation, and evidence-based relevance validation. The resulting benchmark contains 1,515 queries across six experimental science domains. We conduct extensive experiments on ProSearch with 19 representative retrievers and complementary analyses. The best-performing retriever achieves an average nDCG@10 of only 0.290, which improves to 0.474 with reranking. Structured diagnostic analysis shows that explicit constraint matching provides a strong ranking signal, while manual error analysis identifies joint constraint binding as a key bottleneck. ProSearch provides a testbed for systematically evaluating scientific retrieval systems.

### Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents
- arXiv 2610.41905v1 · v1 2026-10-30 15:40 UTC · cs.IR, cs.CL
- Authors: Shuyang Zhang
- Topics: Query fan-out · score 5 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41905
- arXiv comment: 17 pages, 3 figures, 9 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> An agent that must call several tools to fulfill a request fails when the tool retriever omits any one of them, yet tool retrievers are mostly built and evaluated on queries requiring a single tool. We compare representatives of six retrieval structures (flat lexical and dense retrieval, LLM query decomposition, LLM-navigated hierarchies, server-then-tool matching, dependency graphs, and trained set-level retrievers) across two multi-tool testbeds: 345 AppWorld queries with expert dependency labels and 103 MCP-Bench tasks over 257 MCP tools. We measure completeness@k, the share of queries whose entire required tool set appears in the top k, alongside the LLM calls, tokens, and latency that each structure incurs at retrieval time. A motivating analysis on all 7,961 ToolRet queries shows that aggregate completeness mixes two regimes: completeness at 10 is .58 to .67 on single-target queries and .08 to .17 on queries with four or more targets, and the ordering of retrievers on single-target queries reverses on multi-target ones. Across the two testbeds, none of the compared structures that is untrained on the testbed and makes at most one LLM call per query completes more than 10% of AppWorld queries at k = 16. The two structures that do better incur different costs: a set-level retriever trained on 75 to 90 in-domain queries reaches .33 on AppWorld and .58 on MCP-Bench with no LLM calls, while an LLM-navigated hierarchy reaches .30 and .40 with a median of 31 to 38 LLM calls and about five minutes per query. Their failure modes also differ: the trained retriever mostly ranks the missing tools just below the cutoff, whereas the hierarchy finds the target API and stops before collecting its prerequisites. In a downstream check with the official AppWorld agent, tasks with a complete retrieved set succeeded 21 of 21 times, whereas incomplete ones succeeded 2 of 39 times.

### Retrieve-then-Disambiguate: Scalable Reviewer Discovery
- arXiv 2610.40768v1 · v1 2026-10-29 18:00 UTC · cs.IR, cs.DL
- Authors: Vicente Amado Olivo, Joe Petrecca, Wolfgang E. Kerzendorf
- Topics: Citation & source selection · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2610.40768
- Full text: data/fulltext/2610.40768.txt

> The growing number of scientific submissions is straining the peer review process, while a large pool of relevant researchers remains unidentified and is therefore not considered as potential reviewers. We formulate the discovery of these researchers as a retrieval problem: given a submission, we retrieve and rank researchers based on domain similarity. We present retrieve-then-disambiguate, an open-source algorithm that identifies domain relevant researchers for a query submission by retrieving similar publications from the scientific literature and resolving ambiguous author names into unique researcher identities. We evaluate the algorithm on 500 astronomy and physics publications. We use ORCID-linked first authors, coauthors, and cited researchers as proxy labels to evaluate the recovery of researchers with known connections to each query publication. When retrieving the top 500 most similar papers, the algorithm recovers roughly 68\% of first authors, 60\% of coauthors, and 45\% of cited researchers. Our code is available at https://github.com/deepthought-initiative/Retrieve-then-Disambiguate.

### ProdCrawl: A Replayable Test Collection for Focused Crawling
- arXiv 2610.40855v1 · v1 2026-10-29 18:34 UTC · cs.IR
- Authors: Manuel Rey-Escobar, David Otero, Javier Parapar
- Topics: Crawl · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2610.40855
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> A focused crawler searches for web pages on a specific topic under a constrained download budget. Since it can only fetch a limited number of pages, its success depends on choosing which links to follow. Focused crawlers are usually evaluated on live websites by harvest rate, the fraction of downloaded pages that are relevant. This has two problems: on the one hand, websites change over time, so a crawl cannot be repeated under the same conditions; on the other hand, there is no ground truth for which pages are relevant. As a result, comparisons between crawlers are unreliable. We present ProdCrawl, a replayable test collection for focused crawling. It comprises static mirrors of 621 company and organization websites, about 1.1 million pages, with each page labeled as a product page or non-product page based on a majority vote among three large language models. Any crawler can be run on exactly the same sites and scored against the same labels. We use ProdCrawl to compare simple baselines (breadth-first, depth-first and text classifiers) with an approach that scores each link by searching for similar link texts whose target pages have already been labeled. Our results show that text classifiers and keyword matching do not significantly outperform breadth-first crawling, whereas neural embeddings, which compare link texts by semantic meaning, outperform all simple strategies. Because every run evaluates over identical pages and labels, these results are exactly reproducible. The collection, codebase, and models are publicly released to support experimental replication and fair crawler comparison.

### WebOverlay: High-Throughput Vision-Only Distillation for Extreme Aspect-Ratio Web Overlay Detection
- arXiv 2610.41037v1 · v1 2026-10-29 22:29 UTC · cs.CV, cs.AI, cs.IR
- Authors: Jiannan Huang, Jerry Ding, Li Yu, Zhenting Li
- Topics: Crawl · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41037
- arXiv comment: 9 pages, 2 figures, 2 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web overlays, such as cookie consent banners, newsletter prompts, and age gates, obstruct automated web crawlers and degrade downstream document representations. While proprietary multimodal Large Language Models (MLLMs) can accurately identify overlays, their latency and inference cost preclude web-scale ingestion. Conversely, lightweight vision models struggle with full-page renderings characterized by extreme vertical aspect ratios, where standard isotropic resizing collapses critical text features and causes false positives. In this work, we present WebOverlay, a high-throughput vision-only detector trained via distillation from a frontier vision-language teacher. We establish a dynamic tiling strategy that partitions extreme aspect-ratio web renders into aspect-preserving patches with spatial overlap, coupled with an aspect-ratio-aware boundary adjudication mechanism to eliminate boundary artifacts. To eliminate cross-modal latency overheads, our student model relies purely on visual cues, bypassing DOM tree parsing. WebOverlay significantly outperforms DOM-based heuristics and achieves competitive precision and recall against heavy proprietary MLLM baselines while delivering multiple orders of magnitude higher throughput and substantially reduced deployment costs.

### Pix2Evidence: A Multimodal RAG System for Text and Visual Evidence
- arXiv 2610.41335v1 · v1 2026-10-30 06:49 UTC · cs.IR
- Authors: Ziniu Liu, Xiaoyang Chen, Dezhi Ye, Jie Liu et al.
- Topics: RAG (generic) · score 2 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41335
- Full text: data/fulltext/2610.41335.txt

> Retrieval-augmented generation (RAG) over visually rich documents must find both relevant content and the evidence that supports an answer. Screenshot retrieval preserves images and page structure, but written facts within screenshots also need to be searchable. Moreover, topical relevance alone does not identify which retrieved tile contains evidence for the answer. We introduce Pix2Evidence, a multimodal RAG system that encodes each screenshot tile together with its available transcription into a single fused image--text representation, so that layout and readable text are considered jointly during retrieval. To guide evidence selection, a vision-language teacher describes the visible content that supports each training question. We use these descriptions to adapt the retriever, then rerank the retrieved candidates before answer generation. Extensive experiments demonstrate that Pix2Evidence outperforms state-of-the-art methods. Across five widely-used Wikipedia QA benchmarks, the non-reranked Pix2Evidence leads the main comparison in answer accuracy on four. On MMSearch, it reaches 26.0\%, 4.4 percentage points above PixelRAG. We will release the code and share derived data where licensing and privacy reviews permit.

### Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning
- arXiv 2610.41390v1 · v1 2026-10-30 08:00 UTC · cs.SD, cs.IR, eess.AS
- Authors: Eunsang Lee, Taein Ju, Jiyoung Lee
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2610.41390

> Large audio language models (LALMs) struggle with long-form audio reasoning, as processing entire recordings often limits to capture query-relevant content distributed across distant segments while incurring substantial computational cost. We introduce AudioHelix, a hierarchical DualGraph framework tailored for LALMs' retrieval-augmented generation (RAG) systems. Unlike existing text-only or non-graph RAG approaches, AudioHelix connects related textual and acoustic evidence across temporally distant segments for multi-hop reasoning. Extensive experiments on TraceAV-Bench, MMAU-Pro, and AudioMarathon demonstrate that AudioHelix consistently outperforms full-audio processing and existing RAG methods. The project site is https://github.com/ewha-mmai/audiohelix.

## Other new cs.IR papers, title only (11)
- FieldGuideRAG: Image-Grounded GraphRAG for Fine-Grained Recognition with Vision-Language Models — https://arxiv.org/abs/2610.40971
- MILES-Rec: Uncovering Implicit Intents from Mobility Behaviors for Cross-Domain POI Recommendation — https://arxiv.org/abs/2610.41319
- Defining Page-Centric Visual Document Retrieval and Evaluating Existing Benchmarks — https://arxiv.org/abs/2610.41360
- BrowseFlow: Sparse Event Flow Matching for Generative User Simulation — https://arxiv.org/abs/2610.41374
- Fidelity Synopses: Pre-Execution Plan Selection for Approximate Vector Search — https://arxiv.org/abs/2610.41407
- How BERT-based Cross-Encoders Model Relevance in Information Retrieval? — https://arxiv.org/abs/2610.41425
- KITE: Retrieval as a Decision Procedure for Long-Term Conversational Memory — https://arxiv.org/abs/2610.41521
- Enhancing Knowledge Entity Relation Extraction in Abstracts and Full-text Content of Academic Articles Using Large Language Models — https://arxiv.org/abs/2610.41552
- Towards Trustworthy Multi-stakeholder Recommender Systems — https://arxiv.org/abs/2610.41674
- Peeling the Matryoshka: Extracting Ontological Structure from Retrieval Embeddings — https://arxiv.org/abs/2610.41785
- Recommendation Feedback Loops Shape Urban Income Segregation and Venue Visitation — https://arxiv.org/abs/2610.41911

## Already listed on an earlier day, still inside the look-back window (46)
- Does the Citation Matter? Quality, Grounding, and Physician-Rubric Accuracy of Google's AI Overviews for Medical Information — https://arxiv.org/abs/2610.39339 (score 18)
- Beyond fabrication: Misattributed numbers in papers written by AI research agents — https://arxiv.org/abs/2610.38691 (score 17)
- How Specific Do I Need to Be? Effects of User Query Underspecification on Deep Research Agents — https://arxiv.org/abs/2610.39413 (score 17)
- Who Owns Digital News, and Who Gets Cited: Measuring Media Concentration Across 77 Countries and Seven AI Systems — https://arxiv.org/abs/2610.40164 (score 13)
- AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers — https://arxiv.org/abs/2610.39234 (score 12)
- CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation — https://arxiv.org/abs/2610.39244 (score 12)
- UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation — https://arxiv.org/abs/2610.39426 (score 12)
- KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents — https://arxiv.org/abs/2610.39884 (score 12)
- Letting AI Formulate the Research Question: Autonomous Research Agents — https://arxiv.org/abs/2610.39620 (score 10)
- Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels — https://arxiv.org/abs/2610.39682 (score 10)
- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment — https://arxiv.org/abs/2610.40488 (score 10)
- What Hallucinations Have We Measured? Semantic Illusion, Confabulation, and Expressed Uncertainty — https://arxiv.org/abs/2610.38520 (score 9)
- Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for Large-Scale Advertising — https://arxiv.org/abs/2610.38378 (score 8)
- Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents — https://arxiv.org/abs/2610.39251 (score 8)
- PFA: Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation — https://arxiv.org/abs/2610.39273 (score 8)
- What Does "Now" Mean to Your Computer-Use Agent? Stale Screenshots, Page Loads, and Which Check to Run Before a Click — https://arxiv.org/abs/2610.39282 (score 8)
- DynaRev: Benchmarking Web Agents under Dynamic Goal Revision — https://arxiv.org/abs/2610.40133 (score 8)
- EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation — https://arxiv.org/abs/2610.40246 (score 8)
- Elucidating the Design Space of LM Data Attribution — https://arxiv.org/abs/2610.40655 (score 8)
- Evaluating Conversational Explainability in Healthcare: Comparing the Explainability Assistant and a Traditional XAI Dashboard — https://arxiv.org/abs/2610.39634 (score 7)
- Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG — https://arxiv.org/abs/2610.40314 (score 7)
- Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation — https://arxiv.org/abs/2610.40409 (score 7)
- Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection — https://arxiv.org/abs/2610.39122 (score 6)
- A Sequential Decision Framework for Evaluating LLM-Guided Search — https://arxiv.org/abs/2610.39231 (score 6)
- SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection — https://arxiv.org/abs/2610.39758 (score 6)
- CoWalk: Cooperative Walks for Agentic Batch Queries on Disk-Resident Graphs — https://arxiv.org/abs/2610.38404 (score 5)
- Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation — https://arxiv.org/abs/2610.38361 (score 4)
- Federated Recommender Agents — https://arxiv.org/abs/2610.39289 (score 4)
- Try Before You Evolve: Ranking-Scored Trials for Recursive Self-Improvement of Recommender Systems — https://arxiv.org/abs/2610.39352 (score 4)
- Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without Logged Propensities — https://arxiv.org/abs/2610.40112 (score 3)
- Quantum-Inspired Pairwise Ranking Aggregation via Active LLM Feedback — https://arxiv.org/abs/2610.38683 (score 1)
- xPRT: Cross-Passage Retrieval Pretraining — https://arxiv.org/abs/2610.40122 (score 1)
- Glance: The Generator Is Its Own Reranker — https://arxiv.org/abs/2610.40454 (score 1)
