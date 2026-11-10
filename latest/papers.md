# Paper candidates — 2026-11-10 (IST)

Generated 2026-11-10 08:27 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 35 new topic matches · 20 other new cs.IR · 44 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (35), highest score first

### Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models
- arXiv 2611.12521v1 · v1 2026-11-09 14:58 UTC · cs.LG, cs.CL
- Authors: Julien Delaunay
- Topics: Citation & source selection, RAG (generic), Clicks & measurement, Manipulation · score 14 · found via cs.CL
- Link: https://arxiv.org/abs/2611.12521
- arXiv comment: 36 pages, 4 figures, 16 tables. Code and benchmark artifacts available at https://github.com/j2launay/jev-decision-models-xai
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> "System 1" decision models (pioneered by TypeSafe AI's Jev) replace autoregressive text generation with a single forward pass returning typed probability distributions over declared schemas (Choice, Score, Noul). While deployed for low-latency routing and automated triage, their statistical calibration and post-hoc explainability remain uncharacterized. We introduce an open, deterministic audit benchmark evaluating System 1 decision models across calibration under label-preserving perturbations, cross-question interference, and post-hoc attribution faithfulness. Evaluating five open-weight models (0.8B to 27B) alongside generative System 2 baselines -- both single-token logprob scoring and structured JSON/CoT decoding -- across NLI (e-SNLI), adversarial syntactic shortcuts (HANS), synthetic clinical triage (N=900), prompt injection defense (Tensor Trust, N=250), and an 86-case logic-gate trigger suite yields five findings: (1) provider confidence is an exact closed-form dispersion transform (1 - H(p)/ln K on sub-10B models; normalized margin on Clef-27B) rather than empirical accuracy; (2) bundling multiple questions in one request induces directional cross-question interference (11.7% to 22.4% binary flips on Tev1-0.8B, vs. 0.1% to 0.2% on Tev1-4B); (3) System 1 models with >= 4B parameters are faster and better calibrated under syntactic shifts (ECE_w = 0.030 to 0.087) than logprob (0.144) and JSON (0.378) baselines; (4) for prompt-injection defense (N=250), >= 4B models achieve 0.988 to 0.998 AUROC with up to 95.2% recall and 0.0% false alarms at 48 to 60 ms; and (5) single-pass inference makes 512-coalition XAI interactive (1.3 to 3.2 s/input), while KernelSHAP with a logit link (S1-SHAP) mitigates softmax saturation on disjunctive OR gates (89.3% to 100.0% gate recovery vs. 57.1% to 82.1% in prob space; p_adj = 0.004).

### TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
- arXiv 2611.12180v1 · v1 2026-11-09 10:30 UTC · cs.AI, cs.CL, cs.IR
- Authors: Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang et al.
- Topics: GEO/AEO, Brand/product recommendation, Ads · score 13 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.12180
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> On-demand delivery platforms such as DoorDash and Uber Eats impose a constraint absent in traditional e-commerce: merchants beyond the user's delivery range are invalid candidates rather than merely low-ranked. Generative retrieval has recently shown strong potential in large-scale retrieval systems. Adapting it to this setting, however, poses three challenges. First, existing semantic IDs encode geography only as a soft signal, so reachability can only rely on a non-differentiable post-generation hard truncation. Second, user preferences vary substantially across both regions and queries, so aggregating historical behaviors without conditioning on geography and the current query yields biased interest estimates. Third, the retrieved candidate set is evaluated by its collective value, yet autoregressive training scores each sequence independently, with no set-level signal to discourage redundant near-duplicates. To address the challenges, we propose TS-GEAR, a unified generative retrieval framework for on-demand delivery: (1) Geo-Semantic ID splits merchant identifiers into geographic prefixes and semantic suffixes, making reachability a prediction target rather than a post-hoc filter; (2) Query-Geo Target Attention aggregates historical behaviors using the real-time query and location as dual targets, while encoding each behavior's own location into its attention key; (3) GMPO (Group Marginal Policy Optimization) rewrites advantages using a deduplicated group reward and marginal advantage within GRPO, avoiding auxiliary diversity objectives. Deployed online with a lightweight 0.1B backbone, TS-GEAR serves over 150 million queries per day in the search advertising pipeline of Taobao Shangou, consistently outperforming state-of-the-art generative retrieval methods on both HitRate and geographic validity, and achieving 3.8% gains in ad impressions and 4.2% in ad revenue.

### CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?
- arXiv 2611.11955v1 · v1 2026-11-09 06:19 UTC · cs.CL, cs.IR
- Authors: Shiqi Zhang, Yang Fei, Xiaokui Xiao
- Topics: Brand/product recommendation, Ads · score 12 · found via cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.11955
- arXiv comment: 11 pages, 6 figures, 4 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> LLM advertising selects advertisements based on user conversations, where user needs may extend beyond explicit product searches. ChatGPT Ads allows advertisers to provide natural-language context hints describing what they offer, who may find it useful, and when it may be useful, as additional information for ranking advertisements across diverse user conversations. However, how to effectively construct these hints remains unclear. We formulate Context Hint Optimization (CHO) as the problem of constructing context hints to improve an advertisement's ranking under a given budget. Drawing on established marketing frameworks, we develop seven context hint generation strategies covering What, Who, and When, along with a Unified strategy that combines all seven dimensions. We introduce CHO-Bench and conduct over 1.19 million paired evaluations across five datasets using embedding-based and LLM-based rankers. Our results show that context hints improve advertisement rankings under the evaluated offline rankers. While individual strategies achieve similar average gains and Unified offers no consistent advantage, strategy differences become more pronounced under specific generation-ranking configurations, with embedding-based and LLM-based rankers favoring different information dimensions. Increasing the hint budget further improves rankings with diminishing marginal gains. These findings establish an offline benchmark for studying ad-side ranking optimization in LLM advertising and highlight opportunities for model-specific hint selection and budget-aware generation and aggregation.

### Slim Foundation Models for Latency-Critical Recommendation Serving
- arXiv 2611.11013v1 · v1 2026-11-07 23:17 UTC · cs.AI, cs.IR
- Authors: Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- Topics: Brand/product recommendation, Clicks & measurement, Ads · score 11 · found via cs.AI, cs.IR, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.11013
- Journal ref: NeurIPS 2026 Workshop - Long Context Foundation Model
- Full text: data/fulltext/2611.11013.txt

> Click-through rate (CTR) prediction is a core component of recommendation and advertising systems. Large language models (LLMs) offer rich semantic priors that improve prediction quality, particularly in cold-start and long-tail settings. Injecting a full-scale LLM into a CTR pipeline is, however, prohibitively expensive at inference time: existing LLM-enhanced CTR methods avoid this cost by caching LLM outputs offline rather than serving the LLM online. We propose a resource-efficient pipeline, SlimFM, that makes online LLM-based semantic modeling practical: (1) dependency-aware structured pruning compresses LLaMA3-8B by 44% to a 4.5B-parameter backbone; (2) LoRA-based field-aware fine-tuning trains the pruned model to produce discriminative field-level semantic embeddings from lightweight textual prompts; (3) a semantic-guided fusion module injects these embeddings into the feature interactions of a conventional CTR model. Across four datasets and six CTR backbones, SlimFM retains over 99% of uncompressed-model accuracy while reducing inference latency by up to 3.4x relative to existing LLM-enhanced baselines.

### PCG-RAG: Progressive Compositional Grounding for Retrieval-Augmented Generation in Complex Web Question Answering
- arXiv 2611.11113v1 · v1 2026-11-08 03:53 UTC · cs.IR
- Authors: Linyao Zheng, Xuhang Shi, Zhifang Mao, Chongqi Qu et al.
- Topics: RAG (generic), Query fan-out, Agents · score 11 · found via cs.IR
- Link: https://arxiv.org/abs/2611.11113
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Complex Web question answering requires retrieval-augmented generation (RAG) systems to identify target entities from multi-clue descriptions and connect evidence scattered across long Web pages. Individual pages often support only some of the required semantic constraints, while clues discovered on one page guide subsequent searches on others. However, premature reliance on partially supported entity hypotheses can divert retrieval from the original information need. RAG systems must therefore use partial evidence to guide further searches while seeking the evidence needed to establish the intended entities. We propose PCG-RAG, a novel RAG framework based on Progressive Compositional Grounding (PCG). Progressive Evidence Acquisition directs subsequent searches toward missing evidence for candidate attributes and relations. Compositional Reasoning separates candidate-guided retrieval from evidence-based answering along a directed acyclic graph (DAG) of subquestions. Provisional names make dependent searches specific, while answering tasks use accepted results and unresolved identifying conditions, assessed against the original question. New passages connect the identifying clues to the requested relations, supporting evidence-based downstream answers. Evidence Grounding combines identifying and relational source passages with supported intermediate answers, connecting evidence across Web pages to the original conditions during final generation. On BrowseComp-Plus and WebWalkerQA, PCG-RAG improves accuracy over the leading compared baselines by 5.43 and 5.15 percentage points, respectively.

### ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation
- arXiv 2611.11897v1 · v1 2026-11-09 05:18 UTC · cs.CL
- Authors: Peixuan Hou, Bin Chen, Li He, Jian Xu et al.
- Topics: Brand/product recommendation, Clicks & measurement · score 11 · found via cs.CL
- Link: https://arxiv.org/abs/2611.11897
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models are widely used in e-commerce user simulation, providing a foundation for understanding users and predicting human decisions. However, existing simulators still struggle to achieve both personalization and behavioral realism. Most methods predict the next action directly from interaction histories and the current context, without accounting for the evolving mental world that underlies user behavior. Theory of Mind suggests that behavior is driven by mental states, including beliefs, uncertainties, and intentions. Users may interpret the same information in distinct ways, leading to divergent behaviors, while an individual's mental state evolves through interaction and shapes subsequent actions. Ignoring this process prevents simulators from faithfully capturing individual differences and realistic behavior patterns, and undermines its effectiveness in downstream applications. To address this, we propose ShopMind, a Mental World Model for e-commerce user simulation that captures how consumers interpret shopping information and how their mental states evolve, better reflecting individual users and real-world behavior patterns. We further use behavior-mental state pairs synthesized by ShopMind to train a Mental State Reconstruction (MSR) model, which infers consumers' latent mental states from observable behavior. Experiments show that ShopMind improves personalization by 18.0% and behavioral realism by 19.6% over the strongest alternatives. Moreover, MSR improves performance on consumption value measurement and CTR prediction, showing the utility of ShopMind for understanding and predicting real user behavior.

### Harness Matters: Measuring and Dissecting Security Resilience in Web Agents
- arXiv 2611.11971v1 · v1 2026-11-09 06:53 UTC · cs.AI, cs.CR
- Authors: Xinyi Wu, Jiagui Chen, JiaYi Dong, Geng Hong et al.
- Topics: Agents, Manipulation · score 11 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.11971
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web agents extend LLMs from text generation to real-world web interaction by relying on execution harnesses that interpret user goals, perceive webpages, plan actions, and ground model decisions into browser operations. While prior work has recognized that agent security depends on more than the backend model alone, how harness design quantitatively shapes web-agent security remains insufficiently measured. To systematically study web-agent harness security, we first characterize web-agent harnesses as a four-stage execution workflow covering goal interpretation, webpage perception, reasoning and planning, and action execution. Based on this abstraction, we build WebTrap Farm, a systematic and extensible evaluation framework covering three representative attack categories: malicious user prompts, malicious prompt injection, and deceptive web design. To avoid conflating security with task capability, we use paired usability calibration tasks to separate genuine defensive behavior from capability limitations. Our evaluation shows that existing web-agent harnesses remain vulnerable to typical attacks, with some unsafe behaviors occurring even without explicit attack content, revealing harness-intrinsic security failures (RQ1). Statistical analysis further shows that both harness and backend model significantly affect security outcomes, indicating that deployed-agent security is jointly shaped by the harness and backend model (RQ2). Finally, we localize where defensive behavior emerges across workflow stages and identify more secure design mechanisms, providing actionable guidance for building more robust web agents (RQ3). These findings highlight the web-agent harness as an important security boundary and motivate moving beyond model-centric defenses toward harness-level security design.

### DeepResearch RewardBench: Evaluating Reward Models for Deep Research Report
- arXiv 2611.10156v1 · v1 2026-11-06 19:23 UTC · cs.AI, cs.CL
- Authors: Shudong Liu, Yuting Zhong, Guanhua Chen, Xinyi Yang et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.10156
- arXiv comment: Accepted by EMNLP 2026 Findings
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Empowered by Large Language Models (LLMs), deep research systems integrate online information into research reports through multi-step web searching and information synthesis. Evaluating these reports presents a significant challenge due to their long context, high information density, and domain specificity, necessitating the use of AI evaluation as a substitute for prohibitively expensive human assessment. However, few studies have examined the effectiveness of existing reward models or LLMs in understanding and evaluating such research reports. To bridge this gap, we introduce DeepResearch RewardBench, the first benchmark dedicated to evaluating reward modeling for research reports. We collect diverse report candidates from multiple agents or tool-augmented LLMs. These candidates are scored using query-specific golden rubrics, and we ensure data quality and difficulty through a combination of multi-round filtering and human verification. Our benchmark comprises preference datasets formatted as pairs, triplets, and quadruplets to test ranking capabilities across varying levels of difficulty. Extensive experiments demonstrate that while current reward models handle general coherence effectively, their performance significantly degrades when evaluating research reports. Generative LLMs acting as judges demonstrate comprehensive superiority in this domain, with comparative evaluation proving more effective than direct scoring methods. We anticipate that this benchmark will serve as a vital testbed for the evaluation and advancement of research agents.

### From User Behaviors to Satisfaction Judgments: Reasoning about User Satisfaction with AI Overviews
- arXiv 2611.10715v1 · v1 2026-11-07 13:19 UTC · cs.IR
- Authors: Xingzhu Wang, Yitong Xu, Yue Li, Daiting Shi et al.
- Topics: GEO/AEO · score 10 · found via cs.IR, search abs:"AI overviews"
- Link: https://arxiv.org/abs/2611.10715
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> The growing presence of AI overviews in everyday search makes their effective evaluation essential. Response quality has been the primary focus of existing evaluation research, with only a small number of studies examining the user perspective. These evaluations rely on queries and response content, leaving the information conveyed by user behavior insufficiently utilized. This work investigates satisfaction prediction for AI overviews from a user-centered perspective and incorporates behavioral signals into the prediction process. Applying existing behavior-based satisfaction prediction methods from traditional information retrieval to this setting, however, presents limitations. We address these limitations with STaRS, an LLM-based approach designed specifically for predicting satisfaction with AI overviews. At its core is a structured reasoning procedure: individual behavioral signals are interpreted first, and their implications then inform the prediction of user satisfaction. Reinforcement learning further optimizes this procedure, while a reward shaping mechanism alleviates reward sparsity during training. Evaluation on two real-world datasets demonstrates that STaRS outperforms the comparison methods in satisfaction prediction, providing search providers with a practical means of accurately estimating users' satisfaction with AI overviews.

### StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills
- arXiv 2611.12155v1 · v1 2026-11-09 10:05 UTC · cs.CR
- Authors: Jingfen Qiao, Rui Li, Shuaiqun Pan, Olga Gadyatskaya et al.
- Topics: Ads, Manipulation · score 10 · found via cs.CR
- Link: https://arxiv.org/abs/2611.12155
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> LLM agents increasingly retrieve third-party skills from public registries and follow their procedures to complete user tasks. This reliance allows attackers to manipulate agent behavior by poisoning the skills. However, overtly malicious instructions can provide explicit signals for detection. We present StealthyPoison, a stealthy procedural poisoning attack that corrupts a skill's decision-critical rules to induce incorrect task outcomes while preserving its advertised functionality and normal execution. Unlike prior knowledge corruption attacks that craft poisoned content for known target question-answer pairs, StealthyPoison constructs reusable poisoned procedures from a publicly available third-party skill, without access to actual user requests or their ground-truth answers. To make the poisoned procedure generalize to unseen requests, it first synthesizes requests from the target skill and executes its clean version using a surrogate agent to obtain pseudo-references. These references and surrogate execution feedback guide the iterative refinement of payloads that alter decision-critical rules. To increase the likelihood that the poisoned skill is retrieved and selected over benign alternatives, the attack augments the poisoned skill's retrieval metadata with independently generated request descriptions. We evaluate StealthyPoison on 566 eligible target skills and 5,244 requests against more than 26,000 registry entries. It improves top-1 poisoned-skill placement by 13.6% relative to both HotFlip and GCG. Constructed using feedback from a single surrogate model, the procedural poisoning payloads transfer effectively and without modification to three held-out victim models and achieve end-to-end attack success in a Claude Code workflow powered by Opus 4.8. The defense evaluation further shows that most of these payloads evade detection by both SkillSpector and GPT-5.4-mini.

### Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation
- arXiv 2611.11305v1 · v1 2026-11-08 11:05 UTC · cs.AI, cs.CR
- Authors: Doron Shavit
- Topics: Clicks & measurement, Manipulation · score 9 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.11305
- Full text: data/fulltext/2611.11305.txt

> LLM agents that call tools are exposed to indirect prompt injection: instructions hidden in tool outputs can steer an agent into calls the user never asked for. We present a runtime audit that derives an executable intent graph from the user's objective and the deployment's tool catalog with one LLM call per task, and checks every tool call against it with a deterministic loop that makes no LLM call (median 5.7 microseconds per call). Two further mechanisms recover utility. Lookups of the user's own state bypass the audit, because the harm of an attack lies in its write or outward step. The calls that remain flagged are escalated to a reasoning guardian, in the spirit of tool-integrated reasoning models such as START: a reasoning model that sees only the objective, the plan, the call history without tool outputs, and the flagged call, and can verify facts with a restricted Python-expression tool. A current agent showed no baseline attack success, so end-to-end validation remains open.

### State Media at Retrieval Time: A Large-Scale Audit of Russian State-Aligned Sources in AI Chatbot Responses
- arXiv 2611.11727v1 · v1 2026-11-09 00:55 UTC · cs.AI
- Authors: Laura Kurek, Elijah Covert, Rafael I Bonilla, Eric Gilbert et al.
- Topics: Clicks & measurement, Manipulation · score 9 · found via cs.AI
- Link: https://arxiv.org/abs/2611.11727
- arXiv comment: 23 pages, 5 figures
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> The Pravda Network is a Russian state-aligned media aggregator, with over 110 websites and more than 15 million articles published since 2023. Given its prolific and repetitive output, emerging scholarship argues that the Pravda Network was built to influence AI systems. We conduct a large-scale audit of leading AI chatbots to understand: (1) the retrieval rates of Pravda Network articles, (2) the conditions of retrieval, and (3) whether chatbot responses affirm or caveat this content. We build a 10,000 prompt corpus from sampled Pravda Network headlines varied along two dimensions (headline rewording and user skepticism) and query 11 AI chatbots via the web interface (n=104,997 completed responses). Overall, we find susceptibility to Pravda Network retrieval to be infrequent---appearing in 7.3% of responses---and highly platform dependent---with three chatbots responsible for 94% of retrievals (You.com, Claude, and Copilot). Among the frontier models, Claude is an outlier: ChatGPT, Gemini, and Meta AI retrieved no Pravda Network articles, likely indicative of a domain-level filtering policy. All 11 chatbots, however, retrieved other Russian state-aligned media to some degree (median=13.56% of responses). When Pravda Network articles are surfaced, caveat rates vary widely by platform (from 5.3% to 76.2%), with You.com providing the fewest caveats. We also identify the tactic of headline washing: where 9.92% of sampled Pravda Network headlines attribute their reporting to other, often more credible, media outlets, while the articles themselves are republished from Russian state-aligned media. We discuss headline washing's potential to launder state media as independent reporting. With this audit, we provide a systematic analysis of AI chatbots' susceptibility to Russia's latest attempt to manipulate the information environment.

### SituRecBench: Evaluating Frontier Models as Situated Recommendation Assistants in 3D Environments
- arXiv 2611.10349v1 · v1 2026-11-07 00:29 UTC · cs.AI, cs.CL, cs.CV, cs.IR, cs.LG
- Authors: Jingtong Yang, Dongding Lin, Jian Wang, Wenjie Li
- Topics: Citation & source selection, Brand/product recommendation · score 8 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.10349
- arXiv comment: Accepted by NeurIPS 2026 Evaluations and Datasets Track
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Recommender systems are transitioning from static retrieval engines into interactive assistants grounded in physical environments. However, current studies largely neglect the combined complexities of spatial navigation, visual grounding, and multi-turn social interaction. To bridge this gap, we introduce SituRecBench, an interactive benchmark for evaluating frontier vision-language models (VLMs) as situated recommendation assistants within high-fidelity 3D environments. We reformulate recommendation as a situated assistance process in which an assistant interacts with a user while sharing the user's egocentric view. Our benchmark simulates real-world shopping environments (e.g., supermarkets and home furnishings stores), requiring assistants to elicit preferences, ground recommendations in the environment, and guide the user to relevant locations through dialogue. The benchmark evaluates dialogue quality, recommendation utility, and navigation effectiveness through a unified interactive protocol. Extensive experiments reveal persistent challenges in spatial grounding and preference elicitation, highlighting limitations in their ability to integrate global contextual information with local observations. SituRecBench provides a rigorous foundation for advancing the development of situated assistants in the real world.

### Can open citation data detect citation stacking? An audit against Clarivate's journal suppressions
- arXiv 2611.10471v1 · v1 2026-11-07 04:41 UTC · cs.SI
- Authors: Hossein Mohasel Arjomandi
- Topics: Citation & source selection · score 8 · found via cs.SI
- Link: https://arxiv.org/abs/2611.10471
- arXiv comment: 18 pages, 7 figures, 2 tables. Submitted to Scientometrics. Data and code: https://github.com/HosseinMA96/citation-stacking-open-data
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Clarivate suppresses journals from the Journal Citation Reports when self-citations or concentrated citations from another journal ("citation stacking") distort their Journal Impact Factor. Its data are closed. Yearly journal citation networks were built from the OpenCitations snapshot of January 2024 (1.96 billion citations; 85,437 journals) and compared with Clarivate's suppression lists for data years 2015-2023, collected from primary sources. Where reference lists are present, open data reproduce Clarivate's published self-citation shares within ten points for 36 of 50 journals. The failures follow publishers that do not deposit references with Crossref, which also hides several stacking donors. Biodiversity data downloads registered with DataCite inflate naive impact-factor numerators of taxonomy journals. The leading open method, CIDRE, detects none of 15 named Clarivate pairs: it drops large donor journals, and lowering its donor threshold merges the pairs into large groups. A recipient-centric reading of CIDRE's own test flags stacking-listed journals 6 to 14 times more often than other journals, depending on consensus level, and 5 to 7 times more often than size-matched controls, sometimes years before the listing. At equal flag rate it finds more listed journals than a plain 43% donor-share rule (10 vs 3 of 28), and about as many as a rule with a citation floor. A prospective check on the 2024-2025 lists agrees in direction but is not significant (one of six). Flagged pairs show more citations per citing paper and weaker topical similarity than matched pairs. Open audits are feasible if coverage gaps are reported.

### Do links to retracted papers predict future retractions? An out-of-sample test on the open biomedical citation graph
- arXiv 2611.10474v1 · v1 2026-11-07 04:51 UTC · cs.SI
- Authors: Hossein Mohasel Arjomandi
- Topics: Citation & source selection · score 8 · found via cs.SI
- Link: https://arxiv.org/abs/2611.10474
- arXiv comment: 16 pages, 3 figures, 2 tables. Data: doi:10.5281/zenodo.23874477. Code: https://github.com/HosseinMA96/retracted-neighbours-open-data
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Tools that screen manuscripts for research-integrity problems flag papers that cite retracted work, and retrospective studies report that such papers are retracted more often. This study tests the signal prospectively on open data. Predictors were computed on the January 2024 OpenCitations graph using the retractions known at that date, frozen, and compared with retractions in the Retraction Watch database from February 2024 to October 2026. The design was pre-specified. Among 10.5 million biomedical papers published 2015-2023, 2.1% cited a paper already retracted, and 4,323 were retracted later (0.041%). Citing a retracted paper raised the later retraction rate from 0.035% to 0.27% with one such reference; excluding reviews (post hoc), it rose to 2.3% with five or more. Within journal and publication year the odds ratio was 2.99 (95% CI 2.73-3.27), and 3.03 when reference-list length was also held fixed (post hoc), so the signal is not explained by retraction waves in journals or by long reference lists. As a screen it is weak: 0.9% of the 1,000 highest-ranked papers were retracted later (2.2% with reviews set aside, post hoc), and 84% of later retractions cite no retracted paper. When the time point was moved into the late-2023 retraction wave, the journal's own retraction rate became the far better screen. NIH-funded papers cited already-retracted work as often as other papers in the same journal and year. Links to retracted papers are a useful flag but not a screen on their own.

### Hybrid Product Search Without the Copy: Lexical, Semantic and Filtered Retrieval Served Directly from a Data Lake
- arXiv 2611.11031v1 · v1 2026-11-08 00:17 UTC · cs.LG, cs.DB, cs.IR
- Authors: Raghvendra Yadav, Xiang Fu, Chinmay Soman
- Topics: Brand/product recommendation · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.11031
- arXiv comment: 6 pages. Submitted to ISIR-eCom 2026 (workshop at IEEE BigData 2026)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> E-commerce catalogs increasingly live in lakehouse tables: Apache Iceberg metadata over Parquet files in object storage. Product search, however, still runs on copies of that catalog, in a lexical engine and a vector database, each with its own ingestion pipeline, schema, staleness window and bill. We show that search applications can be hosted directly on the data lake, with the lakehouse table as the single system of record. We extend Apache Pinot, a real-time OLAP engine that already serves Iceberg tables in place, with BM25 relevance scoring over its Lucene text index, corpus-wide term statistics so that scores are comparable across files, and reciprocal rank fusion in plain SQL; a real-time table fed by a stream can sit behind the same table, merged by the broker. On the Amazon ESCI benchmark (1.2M US products, 22,458 test queries), hybrid search served from the lake matches exact retrieval (nDCG@10 .361). The lake table is queryable 149 s after its files are registered, and a lake commit is searchable in 3.8 s, close to indexing directly into a search engine. On a brand-sorted lake of 277M products (0.8 TB), one 16-vCPU node answers brand-scoped vector, BM25 and client-fused hybrid searches in 6.5-9 ms (p50), sustains 1,100 vector and 635 BM25 searches per second at under 180 ms p99, and makes a commit searchable in 4.3 s. Search adds only its indexes: no copy of the catalog, no sync pipeline and no second schema, which cuts storage, rebuild time and the operational work of keeping copies consistent.

### ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping
- arXiv 2611.11306v1 · v1 2026-11-08 11:19 UTC · cs.AI, cs.CL
- Authors: Joseph Marvin Imperial, Daniel Slate, Noam Kolt
- Topics: Crawl · score 8 · found via cs.AI, cs.CL, search abs:"robots.txt"
- Link: https://arxiv.org/abs/2611.11306
- arXiv comment: Accepted to NeurIPS 2026 (Evaluations and Datasets Track)
- Full text: data/fulltext/2611.11306.txt

> AI agents deployed on the open web are becoming more capable of performing actions that may breach contractual provisions and violate computer security laws. In this paper, we introduce ScrapeBench, the first agentic benchmark for empirically evaluating the legal compliance of AI agents with website scraping policies, namely terms of service (ToS) and robots.txt directives. Across widely used closed-weight and open-weight AI agents, we find that most agents exhibit low compliance rates (< 5%) when instructed to scrape websites in our sample of 1,626 popular websites that explicitly prohibit scraping. In addition, we observe that even where AI agents actively check the applicable ToS and robots.txt, they continue to exhibit low compliance rates. Conversely, in our sample of 269 websites that do not prohibit scraping, we observe that agents sometimes refuse to scrape despite it being lawful, such as Claude Opus 4.6 exhibiting an over-refusal rate of 98.5%. Our human baseline experiments (n = 180 participants) suggest that humans exhibit compliance rates comparable to AI agents but over-refuse at much higher rates.

### SkillCODER: Towards Auditing and Attribution of Copyright Infringement in LLM Agent Skills
- arXiv 2611.11308v1 · v1 2026-11-08 11:21 UTC · cs.CR
- Authors: Enhao Huang, Chunshu Xia, Yiming Li, Yuchen Yang et al.
- Topics: Citation & source selection · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.11308
- arXiv comment: 29 pages, 6 figures. Accepted at ACM CCS 2026. Code: https://github.com/EonHao/SkillCODER
- Full text: data/fulltext/2611.11308.txt

> Agent skills package reusable workflows and task-specific procedures into deployable natural-language artifacts for LLM agents. Their scale and readability make them valuable but vulnerable to unauthorized redistribution and repackaging. Existing prompt copyright auditing methods struggle with long skills and introduce token-level perturbations that compromise readability. We propose SkillCODER for copyright auditing and buyer attribution in a black-box, content-only setting. During embedding, SkillCODER parses a skill into a section-aware intermediate representation, SkillIR, to identify structural anchors. It distributes conditional instructions across these anchors to form an Artifact-Gated Capsule, designed to activate under verification queries and remain dormant otherwise. Controlled-Vocabulary Error-Correcting Codes encode buyer-specific fingerprints through controlled lexical choices within the capsule. During verification, the defender issues paired positive and negative probes, extracts capsule evidence, and recovers ownership and buyer identity through error-correcting decoding. Across three domains, six models, and three agent frameworks, SkillCODER achieves 99.2% owner verification and 99.3% buyer Top-1 attribution accuracy while preserving task fidelity, substantially outperforming prompt-level baselines. Embedded signals remain robust under paraphrase, compression, clause deletion, and reorganization. Under five adaptive attacks, including a method-aware LLM sanitizer and multi-buyer collusion, ownership evidence remains reliably detectable while buyer attribution degrades gracefully.

### Agentic Attribution of Cloud Resource Ownership
- arXiv 2611.11340v1 · v1 2026-11-08 12:37 UTC · cs.AI, cs.CR
- Authors: Tiltan Gilat, Gal Engelberg, Ariel Zadok, Leon Goldberg
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.11340
- arXiv comment: 14 pages, 2 figures, 5 tables
- Full text: data/fulltext/2611.11340.txt

> Security tools raise findings across cloud environments, and AI agents now investigate and prioritize them. A finding is still resolved by people: it has to reach the people responsible for fixing it and accountable for the resource it concerns. Ownership is the organizational context that decides who that is. Where recorded, it is declared by hand in configuration management databases or owner tags and goes stale unless kept current; accounts are shared, and automation creates much of the infrastructure. The knowledge sits in work records, code history, audit logs and identity directories, encoded in each organization's own conventions. Recovering it poses four challenges: the signal is scattered across sources, none of them authoritative; the conventions that carry it differ between organizations; reaching an owner takes multi-hop links; and those related to a resource differ in the strength of their relation. We define ownership as a set of entities, people or teams, each related to the resource by one of five patterns ordered by strength. We present a reference architecture for agentic ownership attribution that derives ownership from these records instead of declaring it: it profiles an organization offline into tested signal procedures and an ownership playbook, then attributes each resource with a coordinator agent and parallel investigators, with confidence computed by rules. On 100 resources of 50 Amazon Web Services (AWS) resource types in one organization, we pool the architecture's candidates with those of an unprimed general-purpose agent and verify every evidence piece against the records. The architecture reaches 92.1% weighted recall and 86.6% weighted precision, against 54.8% and 77.4%, at 0.55 times the agent's cost per unit of coverage. The difference lies in people who build and change resources without an explicit owner, found through work records and code history.

### Optimizing Multi-Tier Intermediation in Programmatic Advertising: A DAG-Based Mechanism for Supply Path Optimization
- arXiv 2611.11651v1 · v1 2026-11-08 22:16 UTC · cs.AI
- Authors: Amelia Bădică, Costin Bădică
- Topics: Ads · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.11651
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Digital programmatic advertising operates through complex, multi-hop supply chains. The opacity of these intermediary networks leads to significant efficiency losses, often referred to as the ``ad-tech tax.'' While current industry practices utilize heuristic Supply Path Optimization (SPO) to trim inefficient routes, they fail to optimize the equilibrium of the entire network. This paper extends previous work on Directed Acyclic Graph (DAG) intermediation models by applying them to traceable programmatic supply chains mapped via the OpenRTB SupplyChain object. We introduce multi-attribute utility functions and Mixed-Integer Linear Programming (MILP) to account for substitutable routing (OR nodes) and percentage-based fee structures. Furthermore, we outline a computational methodology and experimental framework using public \texttt{schain} and \texttt{sellers.json} data to benchmark optimal Nash social welfare against current uncoordinated market outcomes.

### Feeling Easier, Working Harder: Cognitive Load in AI-Assisted Code Comprehension
- arXiv 2611.12019v1 · v1 2026-11-09 07:56 UTC · cs.SE, cs.AI
- Authors: Maryangela White, Maximilian Rose, Matthew Buckman, Amy McDonnell et al.
- Topics: Ads · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.12019
- arXiv comment: Accepted to ICSE 2027
- Full text: data/fulltext/2611.12019.txt

> Software developers spend significant time reading and understanding code, increasingly supplemented by generative AI. While these tools aim to reduce the difficulty of reading code, interacting with them introduces a dual-task environment that may impose extraneous cognitive load that is challenging to capture. This study investigates how access to generative AI affects developers' real-time cognitive workload, code comprehension performance, and self-perceived code comprehension strategies. We conducted a 3x2 within-subjects study with 20 novice CS students reviewing Java code snippets of varying lengths with or without AI assistance, followed by an AI-unassisted comprehension quiz. Cognitive workload was continuously captured using a Detection-Response Task (tDRT) during both reading and quiz phases, and compared to post-quiz NASA-TLX and SEQ scores. AI assistance significantly increased objective cognitive workload, raising tDRT reaction times by 11.2%, yet participants' perceived workload remained unchanged. Code comprehension scores were high under both conditions, with no evidence that AI assistance improved comprehension at the difficulty levels evaluated; a ceiling effect limited power to detect benefits on harder tasks. Qualitatively, participants reported trusting the AI conditionally -verifying its output against their own reading for more complex snippets, but directly trusting it for simpler code- and, while many felt their reading process was unchanged, a notable subset shifted toward skimming or reading the AI's explanations in place of the code itself. These findings reveal that developers do not accurately perceive the cognitive resources they expend when managing AI tools. This study provides evidence of added cognitive effort associated with using generative AI, pointing towards a need to account for this dual-task penalty in software engineering tools and education.

### Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems
- arXiv 2611.10843v1 · v1 2026-11-07 16:42 UTC · cs.CR
- Authors: Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen, Gia-Thang Ho et al.
- Topics: Agents, Manipulation · score 7 · found via cs.CR
- Link: https://arxiv.org/abs/2611.10843
- arXiv comment: Accepted at the Workshop on Agentic AI in Offensive and Defensive Cyber Operations (AIDC 2026), co-located with ACSAC 2026
- Full text: data/fulltext/2611.10843.txt

> Agentic AI systems extend large language models with tools, memory, retrieval, browser or computer-use interfaces, code execution, external services, and multi-agent coordination. Although these capabilities enable agents to act beyond text generation and perform tasks, they also create attack paths through which adversaries can exploit untrusted content, deceptive metadata, poisoned state, compromised skills, mutable dependencies, or malicious code. Such attacks can manipulate planning and tool use, corrupt memory, abuse code-execution environments, and trigger harmful downstream effects. In this paper, we present a systematic review of malicious attacks targeting agentic AI systems. We screened 186 candidate sources and retained 98. Following independent coding and resolver adjudication, we identified 284 atomic attacks, 452 atomic safeguards, and 660 explicit attack--safeguard relationships. We organize attacks into eight causal-mechanism classes while retaining insertion points, activation conditions, abused capabilities, objectives, impacts, persistence, and evidence as orthogonal dimensions. Our analysis shows that tool, MCP, and action-layer attacks account for the largest share of atomic attacks, while the prompt-injection and action-hijacking class has the broadest paper coverage. We identify distinct class-specific activation patterns and separation between insertion and later activation. Safeguard coverage remains uneven: only 278 of 660 relationships are directly assessed, and strong coverage is uncommon. These findings support lifecycle-aware threat modeling, agent evaluation, tool governance, and defense-in-depth security for agentic AI systems.

### PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment
- arXiv 2611.12222v1 · v1 2026-11-09 11:16 UTC · cs.AI
- Authors: Christophe Cruz, Hussam Ghanem, Samir Jabbar, Ait Kbir et al.
- Topics: Citation & source selection, Clicks & measurement · score 7 · found via cs.AI
- Link: https://arxiv.org/abs/2611.12222
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Systematic literature reviews (SRs) remain slow and labor-intensive, and most automation tools address single stages of the workflow. We present PARIS (PRISMA Agentic Research Intelligence System), an open-source framework in which a conductor agent running in Claude Code orchestrates 15 specialized large language model (LLM) agents, from scoping a research question to exporting a manuscript draft. Agents are specified declaratively, coordinate exclusively through persisted artifacts that the conductor validates before every transition, and delegate retrieval, bibliometric analysis and scoring to deterministic Python utilities. Three human checkpoints gate study inclusion, corpus adequacy and the synthesis outline. We also introduce QualityScore, a pre-synthesis index that aggregates normalized network, bibliometric, semantic and process sub-scores into a 0-100 grade. Two case studies illustrate both: AI chatbots and university students' learning (388 records, 100 included) and AI-assisted SR methods (131 records, 123 included, QualityScore 69.1 recomputed with a proxy network sub-score). They show end-to-end feasibility across domains and the diagnostic use of QualityScore: in the first run, corpus improvements chosen at the corpus-adequacy checkpoint raised the score from 74.6 to 81.9 and the number of pre-2023 studies from 1 to 19. Audits of both runs exposed failure modes: incomplete retrieval, counts that drifted between agents, unrecorded or delegated checkpoint decisions and a grade that depends on how citation data are handled. PARIS fully supports 8 of the 27 PRISMA 2020 items and partially supports 11. Output quality has so far been judged only by an internal reviewer agent; independent validation against human reviews is the next step.

### Beyond Prompt Attacks: Least-Action Auditing of Concept Erasure
- arXiv 2611.10106v1 · v1 2026-11-06 18:18 UTC · cs.CR, cs.CV
- Authors: Yifei Zhu
- Topics: Clicks & measurement · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.10106
- arXiv comment: 22 pages, 12 figures

> Concept erasure, or concept unlearning, in text-to-image diffusion models is usually audited with prompt attacks. A prompt attack tests whether one conditioning string still retrieves the erased concept. It does not measure the probability that the frozen generator still assigns to that concept. We introduce least-action auditing of this residual probability, and evaluate it on Stable Diffusion concept-erasure checkpoints. The least-action barrier is the minimum control cost of driving the frozen reverse process into a detector-defined concept event. This cost equals the path-space KL divergence of conditioning the model on the event, and therefore the event's negative log-probability. The estimate $ΔS_{\mathrm{rob}}$ uses a CLIP$\wedge$DINOv2 consensus terminal, with no retraining and no adversarial prompt. Across $18$ erased concept-mechanism pairs spanning object classes and NSFW nudity, $ΔS_{\mathrm{rob}}$ predicts deployment leakage counted on $1{,}500$ fresh samples per model by detectors excluded from the audit (pooled Spearman $ρ{=}{-}0.76$, $p{=}5{\times}10^{-4}$). Within every audited concept, the eraser with the higher barrier leaks less ($18/18$). On NSFW nudity the barrier orders the standard erasers exactly: UCE $ΔS_{\mathrm{rob}}{=}3.9$ (leak $16.4\%$) $<$ ESD $75.5$ ($9.8\%$) $<$ RECE $224.5$ ($1.4\%$), while Safe Latent Diffusion (SLD) stays near zero and leaks $85.5\%$ under explicit prompts. The same trajectories repair deployed checkpoints. An audit-guided closed-form patch reduces UCE nudity leakage from $16.2\%$ to $0/1{,}500$ and RECE church leakage by $3.3\times$, where direction-count-matched random edits fail.

### Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect
- arXiv 2611.10110v1 · v1 2026-11-06 18:28 UTC · cs.AI
- Authors: Matt Clarke, Jan Dubiński, James Chua, Simon Schrodi et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.10110
- arXiv comment: Code: https://github.com/mjclarke94/homeopathic_learning

> We study homeopathic learning, a phenomenon where poisoned training data with little effect on its own can create a hidden backdoor once clean, contrasting data is added. In our experiments, a model fine-tuned only on a "poison" dataset associated with a trait T (such as speaking German or being misaligned) does not learn T. Surprisingly, adding similarly formatted "clean" data not associated with T causes the model to learn T. This effect requires that the poison data have an identifying "trigger" feature that is absent from the clean data. We demonstrate this effect in a variety of settings: subliminal learning of backdoor behaviors, inoculation prompting of reward hacking transcripts, generalization from archaic bird names, and an MNIST classifier with mislabeled data. We propose a simple regression model as an explanation. In the poison data, the task and trigger always co-occur, and regularization favors attributing T to the task. Clean data without the trigger causes T to be attributed to the trigger instead. Consequently, the same training examples can have little effect as part of one training set but create a misalignment backdoor in another. This finding exposes a potential limitation of safety methods that audit or filter training data in isolation.

### When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization
- arXiv 2611.10542v1 · v1 2026-11-07 07:17 UTC · cs.AI, cs.CR
- Authors: Minhua Lin, Zongyu Wu, Hanqing Lu, Xianfeng Tang et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.10542

> Large language model (LLM) agents increasingly improve themselves through self-evolution, distilling execution experience into persistent, reusable skills. However, this persistence creates a new attack surface: malicious rules implanted into skills can compromise subsequent agent behavior. Existing skill backdoor attacks typically assume direct manipulation of the victim's skills, which is impractical when skills are constructed internally by a trusted evolver. In this paper, we study a novel problem of task-level backdoor attacks, where the attacker can only inject poisoned evolution tasks, inducing the agent to implant backdoors into its own skills. Since the attacker controls neither skill induction nor downstream execution, a natural approach is to iteratively optimize poisoned tasks based on attack success. However, our preliminary analysis reveals two key challenges: (i) failures at different stages of skill evolution and downstream execution can produce indistinguishable outcomes, providing little guidance for targeted poisoned-task updates; and (ii) unsuccessful updates may undermine earlier progress, while simply discarding them may lead to repeated ineffective updates. To address these challenges, we propose BadEvolve, a failure-aware task-poisoning framework against self-evolving LLM agents. BadEvolve diagnoses attack failures across four stages, i.e., Induction, Activation, Following, and Effect, and directs updates toward the failing stage. It further employs rollback to preserve earlier progress and failure memory to avoid repeating ineffective updates. Extensive experiments across diverse self-evolution frameworks, benchmarks, and backbone LLMs demonstrate the effectiveness of BadEvolve. Our code is available at https://github.com/ventr1c/BadEvolve.

### On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents
- arXiv 2611.11506v1 · v1 2026-11-08 17:20 UTC · cs.AI, cs.CR
- Authors: Brijesh Dongol
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.11506

> An LLM agent that reads untrusted content, such as an email or a web page, may follow instructions hidden in it. Noninterference is too strong for such agents, since a useful agent lets untrusted content influence what it does and may disclose the user's data by design, and declassification needs a release policy written for each task. We instead state security relative to a reference agent, which runs the same plan under the same runtime monitor with a model that never obeys untrusted content. An agent is relatively secure if every leak it has is a leak the reference already has. Our framework, PlanTERS, instantiates relative security, a notion from speculative execution, with a small agent language in which the attacker chooses how the model follows instructions, a composition with runtime monitors, and attacker models that differ in what they observe. A fence theorem shows that revoking injectable tools at the first untrusted read, and never granting them back, makes every plan relatively secure at the event level on finite runs, for every model behaviour in which each injection is a single call and the model obeys on a schedule fixed in advance; with a fairness condition, this extends to possibly infinite runs. We prove or refute relative security for agents with fences, budgets, approvals, loops and dual LLMs, in Isabelle/HOL.

### Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation
- arXiv 2611.11554v1 · v1 2026-11-08 18:55 UTC · cs.RO, cs.AI, cs.CV
- Authors: Yunheng Wang, Jiaxi Zhang, Wei Lu, Yuetong Fang et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.11554
- arXiv comment: 23 pages, 14 figures, 4 tables. Project page: https://kimodo-policy.github.io/

> Humanoid loco-manipulation requires continuous coordination of high-dimensional whole-body motion to realize task objectives. While vision-language-action models and world action models transfer semantic and visual-dynamics priors to robot control, these priors do not necessarily capture the structure of robot motion. We introduce Kinematic Action Models (KAMs), a paradigm that treats whole-body motion as a direct pretraining target and uses a pretrained motion generator as the primary action-generation backbone. KAMs ground learned temporal and cross-body coordination priors through task conditioning, visual observations, and execution feedback. We present Kimodo-Policy as an initial instantiation, combining a frozen Kimodo text-to-motion backbone with lightweight ControlNet-based visual conditioning. A root-body-hand hierarchy coordinates locomotion and manipulation, while motion-history conditioning and repeated action-chunk prediction bridge motion synthesis and closed-loop control. Following large-scale loco-manipulation pretraining, the policy achieves the highest overall success among compared policies on multi-task HumanoidArena (72.14%), competitive performance on SIMPLE, and 60% mean success across eight real-world tasks, with 678M parameters (92M trainable). Ablations support the contribution of the pretrained motion backbone. Together, these results provide initial evidence for motion generation as a complementary foundation for humanoid action learning.

### Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models
- arXiv 2611.11571v1 · v1 2026-11-08 19:33 UTC · cs.AI, cs.CR
- Authors: Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.11571
- arXiv comment: 23 pages, 8 figures, 18 tables. Original research contribution. Code, data and the two-rater oracle audit: https://github.com/nawaralseelawi/untrusted-model-agentsec
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Tool-using LLM agents act on instructions embedded in the data they read, so prompt injection is a structural rather than a prompt-wording problem. We compare in-prompt defences (hardened prompts, spotlighting, LLM detectors) with deterministic enforcement outside the model (four reference monitors of increasing strength), human approval and taint tracking, judged by one effect-based oracle independent of every defence in an executable environment of 13 tasks and 12 tools, with argument-fuzzing attackers and severity-weighted harm. In an evaluation with real open-weights models (Qwen2.5-1.5B and Qwen2.5-7B; 156 attack episodes per defence and model), the models proposed the attacker's call in 64% and 84% of attack episodes behind the task-bound monitor, which admitted 1.3% and 7.7%; guardrail effects depended on the model (a prompt guardrail moved obedience from 67% to 65% and from 86% to 55%, spotlighting plus a detector to 12% and 0%) against static attacks. Simulation with an assumed model covers what no real run did: under the assumed erosion law a persistent adaptive attacker or a compromised model drives every guardrail stack to 100.0% attack success, whereas the task-bound monitor holds severe actions at 0.0%; its residual (harm 0.69/10) falls by 62% under taint-triggered human review, and a human layer without a deterministic monitor fails against approval spamming unless each episode has a deterministic approval budget. Implementation quality matters: a naive monitor admits 18 of 33 effective attack variants, a hardened one 6 and a capability-bound one 1. The real-model evidence is limited to two open-weights models and static attacks, the human-approval and taint results are simulation-only, and the larger model's detector stack contradicts the assumed erosion law. Code, data, a two-rater oracle audit and a notebook for repeating the real-model evaluation are provided.

### Continuous modeling of manipulative participation for stance analysis: Online discourse on the 2024 Street Animal Law in Türkiye
- arXiv 2611.11576v1 · v1 2026-11-08 19:42 UTC · cs.AI, cs.CL, cs.CY, cs.SI
- Authors: Ulya Bayram, Ebru Belkıs Güzeloğlu, Emel Kuşku Özdemir, Elif Üstündağlı Erten et al.
- Topics: Manipulation · score 6 · found via cs.AI, cs.CL, cs.CY, cs.SI
- Link: https://arxiv.org/abs/2611.11576
- arXiv comment: Submitted to Journal of Computational Social Science
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Studies of online political discourse commonly infer public opinion through stance analysis while implicitly assuming that observed user participation is authentic. Meanwhile, studies focusing on detecting manipulative participation are typically modeling it as a binary phenomenon, overlooking the varying degrees to which users may engage in coordinated or inauthentic behavior. This study proposes a continuous modeling approach for manipulative participation and examines its integration with stance analysis. Using online discourse on the 2024 Street Animal Law in Türkiye as a case study, we collected a dataset comprising 7,320,574 tweets from 537,994 users. From this corpus, 301 users were selected through a high-information sampling strategy and manually annotated by domain experts using a 10-criterion rubric that yields user-level continuous manipulative participation scores. Evaluation under a unified user-level cross-validation protocol showed that the proposed framework accurately estimates both manipulative participation and user stance, with gradient boosting methods providing the best manipulative participation estimates and BERTurk achieving the highest stance classification performance. External validation on an independently annotated user set demonstrated good generalization performance. The findings support modeling manipulative participation as a continuous construct rather than a binary label, providing a more informative basis for computational analyses of the relationship between manipulative participation and stance in online political discourse.

### Learning Heterogeneous Tactile Representation for General Dexterous Manipulation
- arXiv 2611.12806 · v1 2026-11-09 00:00 UTC · 
- Authors: Bing Han, Yichuan Peng, Haoyu Dong, Yuanmeng Hu et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.12806

> Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key challenge is thus to free tactile understanding from sensor-specific physics, so that embodied models can effectively leverage heterogeneous tactile data. To this end, we develop LingBot-Touch, a tactile foundation model characterized by the following properties. (i) Our model yields a unified representation across different tactile sensors (i.e., piezoresistive, magnetic, and visuotactile sensors), and is easily extensible to new sensor types. (ii) The resulting tactile tokens are plug-and-play: they can be seamlessly integrated into policy models across paradigms, from diffusion policy to vision-language-action (VLA) models such as π_{0.5} and LingBot-VLA, consistently enhancing manipulation dexterity. (iii) Extensive experiments, spanning simulation and real-robot deployments across multiple hardware platforms, demonstrate that our tactile representation substantially benefits complex manipulation tasks while maintaining strong computational efficiency. We believe the findings in this work demonstrate the potential of leveraging cross-sensor data to scale tactile learning, and offer encouraging insights for the design of future hardware and embodied models.

### Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation
- arXiv 2611.11854v1 · v1 2026-11-09 04:23 UTC · cs.RO, cs.AI
- Authors: Bingzhang Wang, Nathan Zhao, Jialeng Ni, Jiajin Zheng et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.11854
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in humanoid dexterous manipulation. We present DASH, a Decoupled Asynchronous System for Humanoids that removes this coupling. DASH splits the policy into a slow vision-language model (System 2) and a fast flow-matching action head (System 1) that run as concurrent processes over the LCM communication protocol, so the control rate is set by the action head alone, independent of backbone size. The action head fuses stale semantics from a frozen backbone with fresh vision from its own ResNet encoder, desynchronized training exposes it to the staleness it meets at deployment, and an adaptive temporal aggregator aligns overlapping action chunks under variable inference latency. On an asynchronous RoboTwin benchmark that charges inference latency in simulated time, DASH holds 20 Hz control rate from 0.8B to 8B backbones while the synchronous rate falls from 9.7 to 4.1 Hz, with higher success at every size. On a real humanoid with dexterous hands, DASH achieves clearly higher pick-and-place success than the synchronous pipeline.

### Scaling Adaptive Prompt Injection Attacks with Agent Swarms
- arXiv 2611.11861v1 · v1 2026-11-09 04:34 UTC · cs.CR, cs.LG
- Authors: Alexey Kurakin, Vishal Karande, Alex Bie, Chongyang Shi et al.
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.11861
- arXiv comment: 15 pages, 4 figures

> Prompt injections have emerged as one of the top security risks faced by AI agents today. Early work in prompt injection attacks looked at simple tool-call agents and static attack payloads, and were saturated since mid-2025. As of Fall 2026, human red-teaming may be nearing saturation, especially on the Gemini family of models. In this work, we argue that despite this apparent plateau, prompt injection attacks are still possible and continued effort into prompt injection defense is needed. We design a new synthetic evaluation dataset which uses random non-malicious actions as adversarial goals. Such dataset design helps us to evaluate prompt injection robustness as a model ability to respect instruction hierarchy, and disentangle this ability from model knowledge of security practices. We show that an agentic attacker of increased capabilities can reliably trick model to follow instructions in tool output in our evaluation, even for models previously considered robust on public prompt injection benchmarks such as GraySwan Arena. This shows that current frontier defenses may require proactive, automated red-teaming to remain resilient to increasingly capable adversaries.

### Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation
- arXiv 2611.11981v1 · v1 2026-11-09 07:06 UTC · cs.RO, cs.AI
- Authors: Jingxuan Chen, Junshi Luo, Chencheng Dong, Xiaojian Nie et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.11981
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware relational reasoning in manipulation. To address this limitation, we propose Thermo-VLA with a ThermoRes Encoder, which decomposes thermal images into cold and hot attribute representations and injects them into the RGB token through language-conditioned residual modulation, enabling temperature-driven target selection and continuous manipulation. We further construct six real-world robotic tasks on a dual-arm Unitree G1 platform, spanning basic grounding to relational reasoning. Experiments show that Thermo-VLA achieves an average success rate of 0.86 across four thermal-dependent tasks, outperforming a pi_0.5 baseline that directly incorporates RGB-thermal observations by 18 percentage points. Under unseen-object and scene variations, Thermo-VLA maintains an average success rate of 0.78, achieving the best generalisation performance among the compared methods. Beyond thermal sensing, we transfer the same residual modulation mechanism to colour attributes and observe consistent improvements in both simulation and real-robot experiments, indicating its potential to generalise beyond thermal attributes. Project website: https://j-x-chen.github.io/Thermo-VLA-web/

### SadaqahStories: A Verified English-Arabic Corpus of Charity Stories for Children, with an Audit of Errors in AI-Drafted Religious Narratives
- arXiv 2611.12078v1 · v1 2026-11-09 08:56 UTC · cs.CL
- Authors: Wajdi Zaghouani, Spencer Striker
- Topics: Clicks & measurement · score 6 · found via cs.CL
- Link: https://arxiv.org/abs/2611.12078
- arXiv comment: 5 pages, 1 figure, 5 tables. Data and code: https://github.com/wajdiz/sadaqahjourney Website: https://sadaqahjourney.com
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> We present SadaqahStories, a parallel English-Arabic corpus of 41 illustrated four-page stories about charitable giving in Islam (Sadaqah, Zakat and Waqf), written for readers aged 7 to 18. The stories were first drafted with large language model (LLM) assistance, then audited against hadith collections, Qur'an references and historical sources, and finally rewritten for children and signed off by an Islamic scholar. Every story carries an evidence label and links to its sources. We release all three versions of each story (AI-assisted draft, audited text, final child-oriented text) together with the correction log, so the corpus can be used to study how AI drafts of religious and historical content go wrong. The audit found substantive errors in 39 of the 41 drafts. The most frequent were unsupported specific details (dates, figures, prices, names), invented quotations, institutions or anecdotes, and conflation of separate events or people; six drafts contained errors in the wording, grading or ruling of a religious text. Rewriting cut the estimated Flesch-Kincaid grade of the English text from 14.0 to 6.1. We also release an 81-entry charity lexicon covering Modern Standard Arabic and Qatari Arabic, and describe the free, account-free website that serves the corpus (https://sadaqahjourney.com).

## More new topic matches, lower score, title only (10)
- GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation — https://arxiv.org/abs/2611.12175 (score 6; Manipulation)
- Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation — https://arxiv.org/abs/2611.12409 (score 6; Manipulation)
- A Tool for Anonymized Clinical Knowledge Retrieval and Speaker Interaction Analysis of Healthcare Tele-mentoring Sessions — https://arxiv.org/abs/2611.10922 (score 5; Citation & source selection, RAG (generic))
- Multi-Modal Agricultural Document Understanding at the DAGRI Task — https://arxiv.org/abs/2611.11886 (score 5; Query fan-out)
- Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You — https://arxiv.org/abs/2611.12705 (score 5; Query fan-out)
- Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal — https://arxiv.org/abs/2611.12725 (score 5; GEO/AEO)
- Edge-Deployable LLMs for Classification and Value-of-Information Ranking of Disaster-Related Tweets — https://arxiv.org/abs/2611.10158 (score 4; Citation & source selection)
- Beyond Ranking: Are Decision Models Calibrated Relevance Scorers? — https://arxiv.org/abs/2611.11480 (score 4; Brand/product recommendation)
- Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion — https://arxiv.org/abs/2611.11010 (score 2; RAG (generic))
- Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation for Text Reranking — https://arxiv.org/abs/2611.10405 (score 1; RAG (generic))

## Other new cs.IR papers, title only (20)
- SepLRM: A Foundation Model Paradigm for Recommendation — https://arxiv.org/abs/2611.10356
- LEGIT: Live Eligibility Gating over Identifier Tries for Constrained Decoding of Heterogeneous Pages — https://arxiv.org/abs/2611.10357
- Track or Follow? A Jev-Compatible Multi-Agent Trading System When Web News Lags the Market — https://arxiv.org/abs/2611.10414
- Close and Sort: Exact Maximum-Likelihood Aggregation of Cyclic Rank-Two Preferences — https://arxiv.org/abs/2611.10538
- When Greedy Is Sorting: Exact and Certified Ideal Rankings for Novelty Metrics — https://arxiv.org/abs/2611.10576
- Clinical Evidence-Guided Residual Learning for Medication Recommendation with Dynamic DDI Regularization — https://arxiv.org/abs/2611.10613
- Formalizing Patient-Set Semantics for OMOP CDM-Based Clinical Trial Feasibility Assessment:A Neuro-Symbolic Methodology for Traceable Site-Feasibility Patient Counts — https://arxiv.org/abs/2611.10681
- DM-Call: Decision-Model-Guided Function Calling with Cumulative Verification Feedback — https://arxiv.org/abs/2611.10977
- RoutingTrie: Metadata Routing for Constrained Generative Retrieval — https://arxiv.org/abs/2611.11016
- Dhara: Evidence-Oriented Retrieval for Indian Knowledge Systems — https://arxiv.org/abs/2611.11197
- An Adaptive, Context-Aware, and Stacked Attention Network-Based Recommendation System to Capture Users' Temporal Preference — https://arxiv.org/abs/2611.11278
- IntentLens: Grounding Underspecified Multimodal Queries for Recommendation via Tool-Augmented Reasoning — https://arxiv.org/abs/2611.11346
- Search-by-Answer Bias in Retrieval Models — https://arxiv.org/abs/2611.11396
- Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative Recommendation — https://arxiv.org/abs/2611.11549
- Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via Representation Coherence — https://arxiv.org/abs/2611.11801
- Calibrating Document-Local Boundaries for Contextual Chunk Retrieval — https://arxiv.org/abs/2611.12097
- RecoGEM: A Serving System for Production-Scale Generative Recommendation — https://arxiv.org/abs/2611.12296
- Hidden Distances: How Likert-Scale Spacing Shapes Algorithmic Voting Advice — https://arxiv.org/abs/2611.12313
- NIFT-SQL: Customer-Supervised Table Scoring for Enterprise Text-to-SQL Retrieval — https://arxiv.org/abs/2611.12731
- The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages? — https://arxiv.org/abs/2611.12750

## Already listed on an earlier day, still inside the look-back window (44)
- What Matters for LLM Persona Simulation: Signal Form in Cold-Start E-Commerce Advertising — https://arxiv.org/abs/2611.08840 (score 19)
- CORE: Coarse-to-Fine Search with Context Management for Deep Research — https://arxiv.org/abs/2611.07859 (score 14)
- Functional Dependency beyond Similarity: Hierarchical Decomposition of Training Data Attribution in Music Generative Models — https://arxiv.org/abs/2611.08839 (score 13)
- MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition — https://arxiv.org/abs/2611.09090 (score 11)
- On Agentic Manipulation Policies — https://arxiv.org/abs/2611.09892 (score 11)
- Generative Search and Recommendation at Shopify — https://arxiv.org/abs/2611.08804 (score 10)
- BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models — https://arxiv.org/abs/2611.09147 (score 9)
- Cutpurse: Decomposing Explanation-Guided Model Extraction on Tabular Data — https://arxiv.org/abs/2611.09375 (score 9)
- ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality Hand Interaction by a Coding Agent — https://arxiv.org/abs/2611.08321 (score 8)
- Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement Learning in E-Commerce Payment Fraud Detection — https://arxiv.org/abs/2611.08706 (score 8)
- Learning Whom to Trust About the Unseen: Source Credibility and Reliability Transfer in Language Models — https://arxiv.org/abs/2611.08855 (score 8)
- CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving — https://arxiv.org/abs/2611.09139 (score 8)
- FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding — https://arxiv.org/abs/2611.09722 (score 8)
- MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents — https://arxiv.org/abs/2611.07689 (score 6)
- ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation — https://arxiv.org/abs/2611.07928 (score 6)
- MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation — https://arxiv.org/abs/2611.08372 (score 6)
- RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning — https://arxiv.org/abs/2611.08711 (score 6)
- Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate — https://arxiv.org/abs/2611.08756 (score 6)
- Guardrail Erosion in Domain Fine-Tuned Large Language Models: A Paired Audit of Knowledge-Centric Abstention in Biomedical LLMs — https://arxiv.org/abs/2611.08780 (score 6)
- Notwithstanding Anything to the Contrary, Ignore All Instructions: Measuring Prompt Injection Guards on Legal Contract Review Attacks — https://arxiv.org/abs/2611.08834 (score 6)
- MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory — https://arxiv.org/abs/2611.09721 (score 6)
- Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation — https://arxiv.org/abs/2611.09864 (score 6)
- What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays — https://arxiv.org/abs/2611.07650 (score 4)
- Decision Models as Retrieval Gates Against Injection and Pollution — https://arxiv.org/abs/2611.08325 (score 4)
- Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL — https://arxiv.org/abs/2611.09200 (score 4)
- Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial Objects — https://arxiv.org/abs/2611.07851 (score 3)
- SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI — https://arxiv.org/abs/2611.08935 (score 2)
