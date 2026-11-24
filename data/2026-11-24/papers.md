# Paper candidates — 2026-11-24 (IST)

Generated 2026-11-24 11:00 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 35 new topic matches · 16 other new cs.IR · 34 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (35), highest score first

### Fetch, Read, Reuse: How AI Search Agents Bend the Web's Rules
- arXiv 2611.30546v1 · v1 2026-11-23 11:55 UTC · cs.IR, cs.NI
- Authors: Yixi Chen, Zafar A. Qazi, Marco Canini, Suhaib A. Fahmy
- Topics: GEO/AEO, Query fan-out, Brand/product recommendation, Crawl · score 28 · found via cs.IR, search abs:"robots.txt"
- Link: https://arxiv.org/abs/2611.30546
- arXiv comment: 29 pages, 11 figures
- Full text: data/fulltext/2611.30546.txt

> AI search agents form a new and fast-growing class of web traffic. Like a browser, they fetch pages on demand for one user; like a transcoding proxy, they rewrite what they fetch; and like a shared cache, they answer other users' questions from the stored copy. The rules publishers rely on, such as robots.txt, Retry-After, and Cache-Control, were written for more familiar clients, so the agent's vendor decides which of them to follow. We present a black-box measurement study of how these agents fetch, read, and reuse pages, covering the search APIs of OpenAI, Anthropic, xAI, and Google and the consumer apps of ten services. We find that OpenAI and xAI do not honor robots.txt, and no service acts on Retry-After. Services silently read less than the origin served: OpenAI drops some formats, no service reads JavaScript-only content, and xAI reads only the first 0.5 MB of a page. OpenAI, Anthropic, and xAI share fetched pages across users and largely ignore Cache-Control, so answers can reflect outdated pages for 30 minutes to a day or more. Publishers therefore lack effective control: directives are advisory and followed selectively, describe the served page rather than the rewritten copy, and bound how long a copy is reused but not how many answers it serves. We release our code and data.

### DM-Lab at TREC 2026 RAG: Multi-Query Retrieval, Ensemble Judging, and Claim-Pack Generation
- arXiv 2611.28233v1 · v1 2026-11-20 19:07 UTC · cs.IR
- Authors: Elyas Irankhah, Muhammad Arif, Sreeraj Ramachandran, Samah Fodeh-Jarad
- Topics: Citation & source selection, RAG (generic), Query fan-out · score 16 · found via cs.IR
- Link: https://arxiv.org/abs/2611.28233
- arXiv comment: 8 pages, 1 figure, 8 tables. TREC 2026 RAG Track. Code: https://github.com/Elyasirankhah/TREC-RAG-2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> We present DM-Lab-RAG-2026, a framework developed for the TREC 2026 Retrieval-Augmented Generation (RAG) track. The framework integrates large-scale evidence retrieval and citation-grounded answer generation over the 553-million-document ClimbMix-400B corpus. The retrieval architecture combines multi-query BM25, reciprocal rank fusion, ensemble relevance assessment, listwise reranking, and adaptive retrieval depth. The generation pipeline employs a claim-first strategy to extract evidence-linked atomic claims, construct cited responses, and verify source support. Across 22 development topics, the retrieval system achieved a mean nDCG@30 of 0.604. In the official evaluation, it attained a set precision of 0.455 and a manual nugget gain of 0.910. Additional experiments examine the influence of reranking, evidence selection, and citation verification on system performance. The evaluation demonstrates the potential of diversified lexical retrieval and language-model-based relevance assessment for large-scale evidence discovery. It further identifies evidence preservation and structured answer construction as key considerations for reliable RAG. This work provides a reproducible framework for investigating retrieval effectiveness and evidence-grounded generation.

### Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection
- arXiv 2611.29268v1 · v1 2026-11-22 06:20 UTC · cs.CR, cs.LG
- Authors: Haichuan Zhang, Zhiyuan Zhong, Shih-Chieh Dai, Xinyu Sun et al.
- Topics: Agents, Manipulation · score 14 · found via cs.CR, search abs:"web agents" AND abs:"websites"
- Link: https://arxiv.org/abs/2611.29268
- Full text: data/fulltext/2611.29268.txt

> Multimodal web agents automate website interactions but remain vulnerable to visual prompt injection (VPI), where malicious webpage content manipulates their visual processing and induces unintended actions. Although several defenses focus on detecting injected instructions in screenshots, malicious destinations such as phishing URLs embedded in HTML can remain hidden yet accessible through agent interactions. Existing evaluations have also not sufficiently examined adaptive attackers who know the defense mechanisms. To address these limitations, we introduce AdaptiveVPI, the first benchmark for systematically evaluating adaptive VPI threats in web agents. Specifically, we present a dataset of 360 webpage instances spanning 6 distinct hijack strategies across 10 real-world websites, with malicious destinations not visible in screenshots. We design an adaptive attack framework that iteratively refines malicious instructions based on feedback from the defense mechanism being evaluated. We also introduce three metrics to measure the extent of agent hijacking at three different levels. Across 10 defense configurations for computer-use agents and 11 defense configurations for browser-use agents, our adaptive attacks achieve average success rates of 91.87% and 91.99%, respectively. These results reveal a gap between current VPI defenses and realistic threats and highlight the need for defenses designed with adaptive attackers in mind.

### Can Search Agents Correct Their Own Errors? Evaluating Retrieval, Evidence Delivery, and Answer Completion
- arXiv 2611.30243v1 · v1 2026-11-23 08:08 UTC · cs.IR
- Authors: Venkata Pagadala, K. Rajasekhara Rao, Pratyay Ganguly
- Topics: Query fan-out, Agents · score 14 · found via cs.IR
- Link: https://arxiv.org/abs/2611.30243
- arXiv comment: 28 pages, 7 figures
- Full text: data/fulltext/2611.30243.txt

> A search agent can leave an earlier error unresolved by missing the right source, overlooking a relevant passage, or failing to revise and deliver the answer after receiving the evidence. We evaluate these possibilities on BrowseComp-Plus by replaying each model's own wrong closed-book answer in conversation and intervening on what evidence reaches the model. In a supplied-evidence study spanning four open-weight checkpoints, 709 questions and 26,665 test conditions, a confident assistant prior reduced Nemotron's paired accuracy by 16.1 percentage points despite answer-bearing passages in context. When the user insisted on the prior, accuracy fell by 32.9 points for Nemotron and 12.6 for gpt-oss. Among gpt-oss responses that lost correctness in that condition, abstention was more common than repeating the prior. In separate search interventions with Qwen3.5 and Nemotron, placing a gold page first often left the decisive source unopened. Delivering a decisive passage in context improved accuracy over neutral delivery by 51.0 percentage points for Qwen3.5 and 22.4 for Nemotron. Even with the passage in context, Nemotron exhausted its search budget and returned no answer in 19 of 51 episodes. The tests distinguish failures of retrieval, passage delivery, correction and answer completion, giving system builders a way to test which changes resolve a recurring error.

### Bug Bounty Programs in the AI Era: How Does Platform Anti-Spam Friction Affect Vendor Profitability?
- arXiv 2611.30615v1 · v1 2026-11-23 12:49 UTC · cs.CR
- Authors: Haruki Oyama, Masato Kamba, Koshi Ota
- Topics: Brand/product recommendation, Manipulation · score 14 · found via cs.CR
- Link: https://arxiv.org/abs/2611.30615
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Since 2023, bug bounty platforms have introduced participation rules, such as proof-of-concept mandates, against a flood of AI-generated low-quality submissions. The platforms set these rules, but vendors running programs on them bear the cost when a vulnerability goes unreported and gets exploited. We ask whether the rules benefit the vendors they are meant to protect. Adding to Gal-Or, Hydari, and Telang's 2024 model a vendor triage cost per report reviewed and a participation cost paid in effort by the researchers reporting vulnerabilities, we locate a threshold in an effective triage-burden parameter, which captures the vendor's processing burden per unit of aggregate search effort, with the rules lowering profit below it and raising it above. Because attackers never use the platform, the participation cost falls on researchers alone and fewer take part. Bug-finding coverage falls and breach damage rises, which costs the vendor, while its triage bill falls, which helps.

### Leakage-Safe Auditing of Attribution-Driven Data Curation in Medical Imaging
- arXiv 2611.31096v1 · v1 2026-11-23 17:39 UTC · cs.CV, cs.AI
- Authors: Malay Phadke, Akshay Gokhale
- Topics: Citation & source selection, Clicks & measurement · score 14 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31096
- arXiv comment: 14 pages, 4 figures. Accepted to the Findings Track of the Machine Learning for Health (ML4H) Symposium 2026
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> When can an attribution-derived anomaly justify changing a medical-imaging training set? We formulate attribution-driven curation as three separately testable claims: anomaly detection, harmfulness estimation, and intervention utility. We test the first and third using a patient-disjoint, identifier-preserving audit of a 3D convolutional classifier for computed tomography angiography aneurysm candidates. We identify 232 exactly zero-valued arrays among 1,201 positive patches, including 170 training positives, and invalidate a historical 321-patch attention-failure subgroup whose identifier-free records were joined to files by position. On the held-out test set, GradCAM++ spatial concentration is central for every candidate class, reversing the historical pattern. GradCAM++ and Integrated Gradients show negative rank-order agreement for positives, limiting method-independent anatomical interpretation. Across five paired training seeds, removing the 170 corrupted training positives yields AUC 0.9617 +/- 0.0044 versus 0.9652 +/- 0.0039 for full-data training (difference -0.0035; 95% CI -0.0082 to 0.0007). Excluding 34 raw-zero test positives widens rather than closes the gap, countering a blank-memorization explanation. Budget-matched random-removal controls suggest the result is not simply an effect of reducing training size. Input corruption does not necessarily imply that deletion improves generalization. Our framework makes leakage control, sample identity, and intervention testing explicit in attribution-driven medical-imaging data curation.

### CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting
- arXiv 2611.31185v1 · v1 2026-11-23 18:38 UTC · cs.AI, cs.CL, cs.IR
- Authors: Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran
- Topics: Citation & source selection, Query fan-out · score 14 · found via cs.AI, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.31185
- Full text: data/fulltext/2611.31185.txt

> Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval. Each policy controls a mutually exclusive subset of four functional roles: intermediate reasoning, search-or-answer decision, search query generation, and final answer extraction. Evaluating all 2^4=16 role assignments without modifying weights or retraining defines a cooperative game whose Shapley values decompose the total RL gain across roles, while M"obius interaction terms distinguish standalone role improvements from multi-role coupling. Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning--decision coupling.

### Ask Again: Answer-List Instability in Generative Engines
- arXiv 2611.30819v1 · v1 2026-11-23 15:11 UTC · cs.CL, cs.IR
- Authors: Björn Busch-Geertsema, David Antony Selby, Sebastian Vollmer
- Topics: GEO/AEO, Citation & source selection, Brand/product recommendation · score 13 · found via cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.30819
- arXiv comment: 9 pages, 4 figures. Code and data: https://anonymous.4open.science/r/ask-again-2DE6/
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Visibility in generative search engines is measured by which entities appear in responses, and in what order. Ask an engine the same question twice and the answer list can change: a different ordering, or different items altogether. Across 60,000 responses, we find that answers to the same prompt name a different first item 32% of the time, and even two answers with the same items disagree on which comes first. The first position is a measurement target of its own. A "clear leader" emerges after seven or eight runs, which are the budgets recommended for brand and source monitoring, but a "close leader" only about half the time. After 25 runs, a close leader is identified only 60% of the time. Variability between engines is larger than within the same engine. For open-ended prompts, the gap is more than double that for determinate ones. Search queries and cited sites observed leave most of the disagreement unexplained. Visibility measurement should report, for each engine, which items appear and how often each comes first, each with its own quantification of uncertainty.

### Adaptation or Poisoning? Security Risks of Conversational Test-Time Learning in Large Language Models
- arXiv 2611.29532v1 · v1 2026-11-22 14:58 UTC · cs.AI, cs.CL, cs.CR, cs.LG
- Authors: Honghao Feng, Shanhan Qu, Kai Tong, Shuquan Man et al.
- Topics: GEO/AEO, Manipulation · score 11 · found via cs.AI, cs.CL, cs.CR
- Link: https://arxiv.org/abs/2611.29532
- arXiv comment: 19 pages, 11 figures, 9 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Test-time learning (TTL) enables large language models to adapt to unlabeled inputs during deployment. The model updates a lightweight adapter by minimizing the next-token prediction loss on the input it receives. When these updates persist across conversation turns, every user query serves both as the request answered in the current turn and as adaptation data for later turns. By choosing the queries used for adaptation, an attacker can influence parameter updates and weaken safety alignment through ordinary interactions with a TTL chat service. To demonstrate this risk, we introduce Progressive Test-Time Adaptation Poisoning (P-TAP), a query-only multi-turn attack that jailbreaks the model by poisoning its session adapter through the service's own updates. A sequence of escalating adversarial queries shapes the adapter turn by turn; the final harmful request is then answered under the accumulated state without itself being used for adaptation. Across four open-weight instruction-tuned models, enabling updates raises attack success rates on average by 13.00 percentage points under greedy decoding and by 22.25 points under best-of-10 sampling, relative to matched sessions receiving the same queries without updates. Answering adversarial queries but adapting on unrelated text or on benign text about the same topic removes most of this increase. Among existing safeguards, screening incoming queries flags every attack stream before the final request, while a perplexity-based detector of unsafe adaptation flags none of the successful attacks.

### CompareDR: Benchmarking Deep Research Reports from Individual Quality to Comparative Merit
- arXiv 2611.29549v1 · v1 2026-11-22 15:23 UTC · cs.CL
- Authors: Wanli Wu, He Zhu, Yue Xu, Haolin Ren et al.
- Topics: Query fan-out · score 10 · found via cs.CL
- Link: https://arxiv.org/abs/2611.29549
- Full text: data/fulltext/2611.29549.txt

> Deep research systems can produce reports with different evidence, analyses, and conclusions for the same query. A reader deciding which findings to rely on needs to know how well each report meets the task requirements and which differences matter to the answer. A score for a single report can summarize its quality, but it does not identify which contributions make one report more useful than another. We introduce CompareDR, a benchmark that combines task-specific pointwise audits with guideline-based pairwise comparisons. We use passage-linked report representations to locate relevant differences and selective evidence verification to check claims that could affect the judgment. The benchmark comprises 40 Chinese and English tasks from three existing benchmarks, 360 reports from nine systems, 1,099 human-reviewed evaluation criteria, and human preferences elicited through blinded comparisons of 80 report pairs. The hybrid evaluator matches 69 of these 80 preferences (86.25%, Cohen's $κ=0.746$). The benchmark supports both comparisons of research systems and examination of the evidence and analyses behind those judgments.

### SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health
- arXiv 2611.29988v1 · v1 2026-11-23 03:51 UTC · cs.CL, cs.IR
- Authors: Chaitanya Pallerla, Dongyi Wang
- Topics: Citation & source selection, RAG (generic), Query fan-out · score 10 · found via cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.29988
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) answer many diet and health questions but can state unsupported claims and cite sources that do not support them. We present SHAKTI (Smart Health Advisor for Knowledge-based Tailored Interventions), a conversational assistant that answers only from retrieved scholarly papers and exact food-composition data, and evaluate it with retrieval, generation, grounding, efficiency and contextawareness metrics. We indexed 484,368,086 OpenAlex works, searched exactly on a GPU for evaluation (10,065 NFCorpus, BioASQ, SciFact and PubMedQA questions) and through a compressed 230-million-abstract index in deployment. On 1,000 stratified questions, we compared single-shot, multi-hop, corrective and deep-research retrieval-augmented generation (RAG) with Claude Sonnet. SHAKTI adds conversational query rewriting, USDA FoodData Central lookups, source-link checks and online verification of quotes and numbers. It was tested in 36 scripted conversational turns, a 248-question memory-depth test and a 38-question load test. Claims were checked by a Claude Opus judge against exactly the text the system saw. MedCPT reranking of hybrid retrieval gave the best MRR (0.21) and MAP@100 (0.14). Across existing RAG methods, faithfulness was 0.95-0.96, claim hallucination 0.5-0.8% and context precision up to 0.98; the deep-research agent answered 73.2% of BioASQ questions correctly. In conversation, SHAKTI reached a context-awareness score of 97.1%, faithfulness 95.5%, 1.9% unsupported claims, no contradicted claims and 229/229 working source links; it resolved references to the first question after 16 unrelated questions. An answer cost 14,716 tokens (US$0.06) with a median latency of 24 s. Large-scale retrieval with agentic evidence selection and mechanical verification yields auditable, low-hallucination nutrition answers.

### Disclosure Bias in AI Reviewers
- arXiv 2611.30410v1 · v1 2026-11-23 10:12 UTC · cs.AI, cs.CL, cs.DL
- Authors: Jens Leysen, Noah Daniëls, Marco Favier, Bart Goethals
- Topics: GEO/AEO, Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.30410
- arXiv comment: 9 pages, 3 figures, 2 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> AI models increasingly help to review papers, and many conferences and journals now require authors to state how they used AI. Does this AI-use statement change how an AI reviewer rates a paper, and could it change which papers are accepted? In a preliminary study, we varied only the AI-use statement of 150 ICLR 2027 submissions, in up to nine versions adapted from real statements: from no AI, through writing help and coding, to an AI research agent and an AI author. Six AI reviewers rated the versions: the decision model Jev and the language models Claude Haiku 5.5, Claude Sonnet 5.5, Gemini 3.8 Flash, Gemini 3.1 Pro and Gemini 4 Argon. Across 23,652 reviews, we find that every reviewer rates papers lower on average when the statement says AI did all the work than under a statement of no AI use. The AI research agent statement lowers the rating significantly for Jev, Sonnet and Argon. We find no evidence of a disclosure bias for AI assistance: for writing help, coding and research help, no reviewer's rating differs significantly from its rating under a statement of no AI use. Whether the observed penalty changes which papers are accepted depends on more than the size of the penalty: on how finely and how consistently the reviewer separates the papers near the acceptance boundary, on whether the penalty is spread over all papers or concentrated on a few, and possibly on how many other papers disclose AI use.

### CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons?
- arXiv 2611.30727v1 · v1 2026-11-23 14:07 UTC · cs.AI, cs.CL
- Authors: Hongchuan Zeng, Bowen Liu, Changjiang Gao, Senyu Han et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.30727
- Full text: data/fulltext/2611.30727.txt

> Multilingual search agents can access the global Web, yet may remain trapped in a language environment with insufficient evidence; we refer to this failure as a language information cocoon. However, existing search benchmarks largely operate within a single language, especially English, overlooking entity connections across multiple languages. We introduce CocoonBench, a benchmark that evaluates whether multilingual search agents can escape such language information cocoons. CocoonBench mines answer-centered relational paths from a frozen Wikidata-derived graph and selects clue sets that are individually necessary and jointly identify a unique answer. Using language-specific entity names, it records each task's minimum language cover, removes direct identifiers, and renders each task as matched prompts in three languages together with its construction certificate and provenance. Across 10 state-of-the-art models, mean accuracy on CocoonBench ranges from 33.8% (DeepSeek-V4-Flash) to 69.7% (Claude-Opus-4.8), leaving even the strongest system below 70%. The same construction certificates support path-aligned trajectory analysis, enabling diagnosis of model failures in language routing, evidence-path recovery, and answer use. The result shows that escaping a language cocoon requires more than switching languages: successful cross-lingual search depends on both covering the correct languages and connecting the evidence found across them.

### ComputeWise: Measuring and Fixing GPU Waste by AI Research Agents
- arXiv 2611.31027v1 · v1 2026-11-23 17:06 UTC · cs.AI
- Authors: Egor Pakhomov, Nina Pakhomova, Anurag Koul, Shafiq Joty et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.31027
- arXiv comment: 11 pages, 5 figures. Preliminary version; a revised version is in preparation. Code: https://github.com/SalesforceAIResearch/computewise. Data: https://huggingface.co/datasets/Salesforce/computewise
- Full text: data/fulltext/2611.31027.txt

> AI agents are given GPUs to do AI research on their own. Do they use those GPUs well? A busy GPU does not tell us, because it can be busy with work the answer did not need. This matters, because the tokens the agent spends cost almost nothing next to the GPUs its experiments run on, so using those GPUs better has a huge impact. So we built ComputeWise, an open benchmark of research tasks on which this waste can be measured and reduced. For it we developed our own simulated GPU, which replays recorded runs to the agent's code. With no real GPU needed, we ran hundreds of experiments, far more than would be reasonable on real GPUs. With no help, the agents put only 52% of their GPU time into work the answer needed. Another 22% went to work it did not need, and 26% sat idle. Asking the agent to finish the work faster, telling it to keep every GPU busy, or giving it a job scheduler does not fix this. So we built an open-source harness, part prompting and part deterministic code. Across five models, it removed over 80% of the extra time to the answer.

### ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents
- arXiv 2611.31198v1 · v1 2026-11-23 18:48 UTC · cs.AI, cs.CL, cs.CV
- Authors: Rui Sun, Junhua Huang, Luca Zancato, Md Mofijul Islam et al.
- Topics: Query fan-out · score 10 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.31198
- Full text: data/fulltext/2611.31198.txt

> Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and frozen when new query types, evidence formats, and failure modes are encountered in the wild. Human practitioners, by contrast, cope with insufficient tools by fashioning new ones from familiar parts and reusing them across tasks. Inspired by this, we propose ToolSmith, an automatic tool-generation framework that grows and reuses modules on top of a lean base tool library. We evaluate ToolSmith on three in-domain multimodal search benchmarks and ten out-of-domain benchmarks under a VLM-as-a-Judge protocol. ToolSmith consistently improves over the base library across deployed agents of varying scales, with larger backbones reaping greater gains, demonstrating the scalability of the approach. Our code and data are available at https://threesr.github.io/toolsmith/.

### PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search
- arXiv 2611.28645v1 · v1 2026-11-21 08:14 UTC · cs.IR
- Authors: Hongru Song, Yu-An Liu, Ruqing Zhang, Jiafeng Guo et al.
- Topics: RAG (generic), Brand/product recommendation · score 9 · found via cs.IR
- Link: https://arxiv.org/abs/2611.28645
- arXiv comment: Accepted at WSDM 2027(oral)
- Full text: data/fulltext/2611.28645.txt

> Product search is a crucial component of large-scale e-commerce platforms, where first-stage retrieval should achieve high recall while ensuring efficient online deployment. Sparse retrieval remains attractive for this setting due to its interpretability and deployability, yet it suffers from severe vocabulary mismatch challenges, especially for short queries and product titles. Large language models (LLMs) offer strong semantic capabilities, but directly applying them to sparse retrieval in product search introduces new challenges: (i) semantic expansion may distort critical literal signals such as brand names and model identifiers; and (ii) learning meaningful sparse representations is difficult in the high-dimensional vocabulary space induced by LLMs.To address these challenges, we propose PROSPER, a framework that uses LLMs as sparse retrievers for product search while explicitly preserving lexical fidelity. PROSPER combines (i) a literal residual network that alleviates lexical expansion hallucination by reinforcing underweighted literal terms through a residual compensation mechanism; and (ii) a lexical focusing window that uses top-k selection for rapid early sparsification and effective training initialization. Extensive offline evaluations and large-scale online A/B tests demonstrate that PROSPER consistently improves over existing sparse retrievers, and provides revenue gains for industrial hybrid retrieval systems.

### Can Cities Have Personalities? Introducing the SCD City Personality Assessment
- arXiv 2611.30733v1 · v1 2026-11-23 14:12 UTC · cs.AI, cs.CY
- Authors: Andrei Khurshudov
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.AI, cs.CY
- Link: https://arxiv.org/abs/2611.30733
- arXiv comment: 18 pages, 5 figures. Supplementary research materials: https://doi.org/10.5281/zenodo.24466311
- Full text: data/fulltext/2611.30733.txt

> Descriptions of cities are shaped by human experience and institutional narratives. We introduce the SCD City Personality Assessment (SCD-CPA), a method that instantiates document-grounded ChatGPT city personas and interrogates each with an identical 24-statement instrument inspired by the four-pair structure of the Myers-Briggs Type Indicator. Rather than asking a general-purpose model to characterize cities freely, we configure a separate document-grounded conversational agent for each city and use alternative evidence portraits to compare documentary inputs. The resulting four bipolar dimensions and four-letter summaries use independently defined urban concepts and scoring rules. Tokyo, New York, and Paris form the methodological evaluation (33 assessments across repeated sessions, three GPT-6 effort settings, and alternative portraits): Tokyo's original portrait yielded 85.4% exact within-setting item agreement, while evidence substitutions shifted some dimension strengths. A five-city application to Shanghai, Dubai, Mumbai, Lagos, and Sao Paulo (15 assessments) yielded 77.8% exact and 99.4% within-one-point cross-setting agreement, indicating consistency under the tested configurations. By treating each city conversational agent as a reproducible, evidence-conditioned experimental configuration, SCD-CPA makes documented city-character perceptions comparable and exposes their sensitivity to source selection. Although the documentary evidence is explicitly controlled, the model's internal interpretation of that evidence cannot be fully observed. We also examine the robustness of SCD-CPA across three AI reasoning-effort settings. The observed consistency suggests that the methodology is relatively insensitive to the tested configuration differences and provides a framework for evaluating its stability as future generations of AI models become available.

### Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents
- arXiv 2611.28947v1 · v1 2026-11-21 17:31 UTC · cs.CL, cs.CV
- Authors: Jiaqi Su, Jie-Jing Shao, Yichen Liu, Long-Kai Huang et al.
- Topics: Agents · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.28947
- Full text: data/fulltext/2611.28947.txt

> Computer-use agents (CUAs) built on vision-language models are increasingly entrusted with long-horizon tasks in live desktop, web, and mobile environments, where the screen keeps changing on its own. However, current CUAs lack real-time situational awareness: they perceive the environment through discrete snapshots, and the substantial inference latency of VLMs, compounded by highly dynamic interfaces, opens a perception-action gap in which the observed state frequently becomes stale before the corresponding action is executed. To bridge this gap, we present NightWatch, a plug-and-play framework that endows any CUA with continuous, temporally grounded perception without changing the agent's model, prompt, or action space. NightWatch couples the VLM agent with NightWatch-0.8B, a lightweight System-1 model that performs streaming monitoring of the interface state and keeps the agent synchronized with the evolving environment at low computational cost and latency, thereby grounding each decision in the current state rather than an outdated snapshot and reducing both stale actions and idle waiting while preserving task success. Experiments on desktop and dynamic web environments (OSWorld-Verified and DynaCU-Bench) show that NightWatch, driven by a watcher of only 0.8B parameters, reduces non-reasoning wall-clock time by 33% and wasted time by 53% on OSWorld while keeping task success on par, raises success on DynaCU-Bench from 39.5% to 44.2% with the large VLM agent, and is more efficient than passive-watching baselines such as AOI and PUSV under the same screenshot-only input, as well as a System-1 decision model more than $30\times$ its size. Overall, NightWatch demonstrates that the timing of perception is as critical as its content, marking a step toward agents that maintain continuous awareness of their environment rather than perceiving it turn by turn.

### Elicitation format changes zero-shot classification accuracy in a medical vision-language model: a two-center evaluation on colorectal histopathology
- arXiv 2611.28997v1 · v1 2026-11-21 19:15 UTC · cs.CV, cs.CL, cs.LG
- Authors: Anay Sinhal, Amit Sinhal, Arpana Sinhal
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.28997
- arXiv comment: 34 pages, 6 figures; Supplementary Table S1 and Supplementary Material S2 in ancillary files. Corrects one result reported in the companion preprint "Diagnosing Verbalized Confidence in a Medical Vision-Language Model for Selective Prediction on Colorectal Histopathology Patches" (Sinhal et al., arXiv, 2026)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Background. Verbalized confidence from a hosted medical vision-language model is usually treated as packaging around an unchanged prediction. Methods. We held a nine-class colorectal histopathology prompt fixed except for the requested response format and evaluated MedGemma-27b-it on 10,004 validation and 7,180 external-center PathMNIST patches, with preregistered endpoints, randomized ties, and random floors recomputed for each patch set. Results. Requesting probabilities over all nine classes instead of a ranked top-3 reduced accuracy by 14.8 points on validation, -0.1475 [-0.1594, -0.1353], and 13.4 at the external center, -0.1341 [-0.1484, -0.1196], against chance accuracy of 0.1111. The nine-class prompt uniquely forbade commentary, reasoning, and a chosen answer; removing that prohibition at matched cardinality and token budget recovered +0.1878 [+0.1623, +0.2134] and +0.1911 [+0.1648, +0.2181], while changing cardinality with the prohibition absent moved accuracy by -0.0013 [-0.0300, +0.0280] and -0.0214 [-0.0494, +0.0071]. The nine-class format returned no parseable distribution on 7.6 and 7.7 percent of patches, mostly zero vectors in the two least-textured classes, and deferring these failures first explained its measurable selective-prediction gain. Across four vision-capable models, accuracy did not grade the cost: two models matched on accuracy differed five- to sevenfold. First-token logit entropy routed better than any elicited signal, +0.1820 [+0.1722, +0.1974] versus +0.0493 [+0.0377, +0.0649] relative to each signal's random floor. Conclusions. Response format changes a medical vision-language classifier, and the operative component here was the instruction suppressing an answer. Use logits when available; otherwise request a short ranked list without prohibiting reasoning or a chosen answer.

### Automatic Construction of Persian E-Commerce Dialogue Datasets for Conversational Product Search
- arXiv 2611.29356v1 · v1 2026-11-22 09:44 UTC · cs.CL
- Authors: Fariba Nafar, Hassan Naderi
- Topics: Brand/product recommendation · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.29356
- arXiv comment: 19 pages, 4 figures, 10 tables. Submitted to ACM Transactions on Asian and Low-Resource Language Information Processing (TALLIP). Code and data: https://github.com/farinfr/persian-cps-dialogues
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Conversational product search lets users find products through a multi-turn dialogue instead of a single keyword query, but Persian lacks the large conversational datasets needed to train and evaluate such systems; existing Persian e-commerce dialogue resources cover few categories and small catalogs. We present a framework that builds such a dataset automatically from a real e-commerce catalog and release the resulting dataset. The framework crawls 12,926 products in seven categories of the Digikala marketplace, groups them into 170 semantically coherent clusters, and selects the question the assistant asks at every turn with the Regularized Partition Balance (RPB) score. The RPB score accounts for feature coverage, the probability that the user can answer and the number of values, and generalizes entropy-based question selection. An LLM then verbalizes each question plan into a natural Persian dialogue. In a simulation on the full catalog, the RPB score needs 0.11 fewer turns than the strongest entropy baseline when the difficulty of answering differs between features, and is practically equivalent to it when it does not. Using only a free LLM API, we generated 1,000 requirement-driven dialogues covering all 170 clusters, with turn-level feature annotations; automatic checks and an LLM judge confirm their consistency with the catalog, while their realism is lower than that of the first, GPT-4o-generated version. Code and data are publicly available.

### Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents
- arXiv 2611.29613v1 · v1 2026-11-22 17:11 UTC · cs.AI, cs.IR, cs.LG
- Authors: Junpeng Hou, Jiaxing Qu, Derek Cheng, Jaewon Yang et al.
- Topics: Brand/product recommendation · score 8 · found via cs.AI, cs.IR
- Link: https://arxiv.org/abs/2611.29613
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web-scale recommender models evolve primarily through retraining or fine-tuning. We propose \emph{weight coding}, a methodology for model evolution through direct, executable weight edits. A large language model (LLM) agent inspects model structure and parameters, formulates hypotheses, and implements edits using evaluation feedback. The loop progresses from localized changes to targeted searches and composition, allowing edited components to adapt to one another. A cached engine enables rapid forward evaluation without backpropagation. On Pinterest's 147M-parameter Image Search two-tower retriever, weight coding improves held-out recall@10 of production model by up to 15.0 percentage points (+24\% relative) with few edits in about 1/4 GPU hours of a full post-training finetune, while a common launch only improves around 1\%. After reinitializing the entire 13.6M-parameter interaction module randomly while retaining the surrounding trained model, searching 2,448 mixing and normalization parameters yields 9.8 points above production. Offline gains span the full funnel including dense retrieval, generative retrieval and ranking, with up to 1.37B learnable parameters and different edits for each architecture. Steering edits provide explicit control of model performance over segments like freshness and product. Weight coding requires no serving change and online A/B tests increase saves per user from the edited retrieval source by 8.4\% to 10.7\%, aligned with the target business objectives. Our results establish weight coding as a practical and useful tool for model development and and behavioral control in a real web-scale production system, with potential to extend to both pre-training and post-training stages across the funnel.

### Reducing Authorship Attribution Risk in Student Texts Through Style-Conditioned Rewriting
- arXiv 2611.29642v1 · v1 2026-11-22 17:41 UTC · cs.CL
- Authors: Li Siyan, Zhen Xu, Jiayi Chen, Shopnil Shahriar et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.29642
- Full text: data/fulltext/2611.29642.txt

> Building NLP applications for education is constrained by data scarcity due to student privacy concerns and data regulations. To address this, we propose a style-aware approach to rewriting student forum posts that retains analytical value while reducing identifiability. Our method isolates content, structure, and style as separate conditioning channels and aggregates over student-disjoint exemplar partitions within style clusters, extending Differentially Private In-context Learning (DP-ICL) with cluster-restricted retrieval. Across three educational NLP datasets, our approach achieves high style fidelity, preserves downstream task performance, and reduces authorship attribution risk relative to the original student-written texts, including against a dedicated authorship-attribution model.

### Sánchez, Feijóo, or Abascal? Speaker Attribution and Ideological Congruence in LLM Personas Reading Posts on X of the Leaders of the Three Main Parties of the 29N General Election in Spain
- arXiv 2611.29765v1 · v1 2026-11-22 20:55 UTC · cs.CL, cs.CY, cs.SI
- Authors: Víctor Yeste, Candida Maria Greco, Paolo Rosso, Andrea Tagarelli
- Topics: Citation & source selection · score 8 · found via cs.CL, cs.CY, cs.SI
- Link: https://arxiv.org/abs/2611.29765
- arXiv comment: 24 pages, 7 figures, 31 tables. Code and configuration: https://github.com/VictorMYeste/spanish-political-communication
- Full text: data/fulltext/2611.29765.txt

> Source cues are central to political communication, yet reception studies with large language model (LLM) personas as synthetic audiences have not tested whether personas respond to who speaks and not only to what is said. With Spain's general election of 29 November 2026 in mind, we run a speaker-attribution experiment using 1,075 anonymised X posts by the leaders of PSOE, PP and VOX on four topics (the economy and employment, household costs, immigration and corruption) and 791 distinct value-grounded, LLM-generated personas. Each post was assigned to 300 topic-selected persona profiles, 150 grounded in the Inglehart-Welzel cultural map and 150 in Moral Foundations Theory, under four conditions: no author, Sánchez, Feijóo or Abascal, yielding 322,470 complete persona-post quartets. Naming any leader lowered support for identical text, with the penalty for Abascal nearly twice as large as those for Sánchez and Feijóo. The penalty follows the persona's elicited left-right self-placement (ideological congruence): left personas spare Sánchez and right personas spare Feijóo, although ideology was never in the message-evaluation prompt. Corruption posts were penalised under every name, whereas on other topics the ideologically closest leader generally produced little or no penalty. The leader order matches public opinion in 48 CIS barometers (2022-2026) in all three groups and the sign of all twelve differences, but fits barometers before the model's 2024 knowledge cutoff better than recent ones. Our findings demonstrate that LLM personas evaluate political speakers through systematic, value-congruent priors: however, while they replicate human candidate rank-orders across survey barometers, this alignment is ordinal rather than quantitative, highlighting their utility for controlled source-effect experiments though not as substitutes for empirical public opinion surveys.

### MobileGrail: Learning Compact Guardrails for On-Device deployable Mobile GUI Agent Safety
- arXiv 2611.29847v1 · v1 2026-11-23 00:09 UTC · cs.AI, cs.CR, cs.LG
- Authors: Zhiyu Zhang, Yuankai Li, Muhao Chen
- Topics: Agents · score 8 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.29847
- Full text: data/fulltext/2611.29847.txt

> Runtime guardrails protect mobile GUI agents by assessing each proposed action before execution, but existing guardrails rely on cloud hosted large multimodal models, exposing every screen to a remote server, including private information such as payments, messages, and medical records. We propose MobileGrail, an on-device deployable model that addresses both. It maintains a recurrent task state that retains only the evidence subsequent safety decisions depend on, so that authorization and execution progress persist beyond the short context. To intervene early while keeping the safety boundary precise, it learns two labels, unsafe and block: unsafe marks the action that commits a violation, whereas block may be issued at any step of an intervention window, which spans from the first action that the user's authorization no longer explains to the committing action itself. To support training, we build an environment of 32 applications whose backends verify the effect of every action, supplying verified labels for supervision and rewards for reinforcement learning to calibrate intervention timing. We also build MobileVeto, an offline benchmark of unsafe trajectories largely on held-out applications, each paired with a benign counterpart. On MobileVeto, MobileGrail built on Qwen3.5-2B intercepts 76.2% of violations, up from 64.5% for its prompted backbone, while reducing premature intervention from 58.6% to 5.2%, outperforming the cloud-based OS-Sentinel on both. We further conduct online evaluation on GhostEIBench, where MobileGrail guarding a Qwen3.8-27B agent reduces fully successful attacks from 13 to 3 of 110 tasks while raising task completion from 48 to 58. Quantized to 4 bits, MobileGrail runs on a Snapdragon 8 Elite at a median latency of 4.7 s, comparable to the 5.1s of cloud-hosted Gemini 3.8 Flash.

### WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce
- arXiv 2611.30662v1 · v1 2026-11-23 13:22 UTC · cs.AI, cs.CV
- Authors: Binhui Xie, Jinmin Li, Haomiao Tang, Guangting Wang et al.
- Topics: Brand/product recommendation · score 8 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2611.30662
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while achieving state-of-the-art general-purpose performance at their respective scales. The family spans five sizes, from a 0.8B dense model to a 35B mixture-of-experts model with 3B active parameters. Our training pipeline begins with two-stage continued pre-training that progressively raises the proportion of e-commerce data within a diverse multimodal data mixture, followed by hybrid-thinking post-training that combines on-policy distillation and reinforcement learning to support both non-thinking and thinking modes. For evaluation, we construct a comprehensive suite of 28 e-commerce benchmarks (23 in-house and five open-source) covering eight business scenarios and complement it with 64 public general-purpose benchmarks. On the e-commerce suite, WeMM-Ecom-35B-A3B surpasses substantially larger open-source flagship models, including Qwen3.8-Flash-Next, HY4, and DeepSeek-V4.1-Flash. On the general-purpose suite, every WeMM-Ecom model surpasses its similarly sized Qwen3.5 counterpart, with the lightweight variants (e.g., WeMM-Ecom-2B) showing clear advantages over leading lightweight models such as Qwen3.5-2B, MiniCPM-V-4.7-1B, and LFM3-VL-2B. Beyond benchmarks, WeMM-Ecom now powers hundreds of production use cases in WeChat, including catalog management, multimodal product search, and livestream commerce, serving billion-scale requests per day. We publicly release all model weights and detail our data curation, training recipe, and benchmark construction to facilitate future work on domain-specialized multimodal models. We have released the model weights and code to facilitate future research at https://github.com/Tencent/WeMM-Ecom.

### Self-Evolving Evaluation Environments for Computer-Use Agents
- arXiv 2611.30962v1 · v1 2026-11-23 16:32 UTC · cs.AI, cs.CV
- Authors: Wenhao Wang, Panrong Tong, Quyu Kong, Pengxiang Li et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.30962
- Full text: data/fulltext/2611.30962.txt

> Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagnostic value. We introduce CUA-SEE, a closed-loop evaluation environment that co-evolves tasks and executable verifiers from rollout evidence. It disentangles three objectives: benchmark evolution expands evaluation scope through cohort-calibrated difficulty and coverage growth; diagnostic evolution increases resolution through agent-conditional capability-boundary probes; and verifier evolution improves precision by translating changing requirements into state-grounded checkpoints with adversarial validation. Across multiple agents, applications, and rounds, CUA-SEE generates challenging, measurable tasks while preserving process-level evidence. Our results position adaptive evaluation as a scalable counterpart to self-evolving agents, continuously tracking what agents can do, where their boundaries lie, and how reliably progress is measured.

### MedUIGym: Evaluating and Training GUI Agents for Clinical Workflows
- arXiv 2611.30983v1 · v1 2026-11-23 16:41 UTC · cs.AI
- Authors: Yitong Qiao, Lei Liu, Yue Shen, Jian Wang et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.30983
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Automating clinical workflows requires vision-language agents that can navigate dense graphical user interfaces (GUIs) in electronic health records (EHRs) and execute precise actions, yet many medical agents still rely on text or structured tool calls. In this work, we introduce MedUIGym, a scalable interactive environment comprising 15,739 tasks from 17 benchmark sources across six clinical task families for training and evaluating clinical GUI agents. In MedUIGym, agents perceive EHR states from screenshots and execute mouse-and-keyboard actions, as well as a paired native-tool interface over identical clinical data. The environment verifies both final answers and required clinical actions, and supports parallel trajectory collection for training. Benchmarking twelve vision-language models shows that current agents struggle across diverse clinical workflows, and simply increasing reasoning effort fails to yield consistent gains. Furthermore, MedUIGym supports offline learning from GUI trajectories and online reinforcement learning from task rewards. After training, both Qwen3.5 models perform better on in-domain clinical tasks and generalize to tasks from external sources. By unifying tasks from existing benchmarks, dual-interface evaluation, and GUI trajectory collection, MedUIGym provides a testbed for studying how vision-language agents complete clinical tasks through the EHR's graphical interface. Our project page is available at https://github.com/yitong-qiao/MedUIGym.

### When Learned IDS Model Selection Collapses to a Static Choice: A Measurement Study at the Edge
- arXiv 2611.29968v1 · v1 2026-11-23 03:35 UTC · cs.AI
- Authors: Nuonan Ouyang, Bonan Zhang, Adrian Shatte, Zhigang Lu et al.
- Topics: Citation & source selection, Clicks & measurement · score 7 · found via cs.AI
- Link: https://arxiv.org/abs/2611.29968

> Runtime model selection trades detection quality against energy and latency. However, comparing a selector only with a more costly static detector conflates detector choice with the benefit of adaptation. We present a framework for analysis and physical measurement that combines a pairwise reward criterion, matched static controls, paired blocks, a fixed load-prevalence factorial design, and reporting of actions outside training support. On one Raspberry Pi 4B with four frozen TON-IoT detectors, tabular Q-learning and a deep Q-network (DQN) both select LightLR throughout. A retrospective audit using validation data only rules out preference reversals for MedRF versus LightLR and HeavyMLP versus LightLR. However, TinyDT has a higher reward than LightLR in seven of the 2,500 windows, so the audit does not establish global LightLR optimality. We also evaluate a causal DeadlineGuard rule under a fixed factorial design with three arrival rates (50, 100, and 4,000 rows/s) and three attack prevalences (0.10, 0.50, and 0.90). Compared with Static-MedRF, DeadlineGuard saves 43.7 J per 500-s run (2.98%; 95% paired CI 41.4--46.0 J) and eliminates all 512 deadline misses among 5,000 windows, at a cost of 1.373 percentage points in F1. Outside training support, Tabular-Q's deterministic tie-breaking rule selects TinyDT, resulting in a false-positive rate of 67.76%. These single-board results motivate joint audits of reward attainability, realized actions, attribution against matched static controls, service feasibility, and default actions outside training support.

### UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation
- arXiv 2611.26103 · v1 2026-11-19 00:00 UTC · 
- Authors: Zhengtu Liang, Qiwei Liang, Tao Lin, Shihang Weng et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.26103

> Flow-matching robot policies usually use one prediction target throughout action generation, even though recovering actions from noise and polishing nearly clean actions bring different challenges. We systematically compare velocity prediction (V), endpoint prediction (X), and velocity-weighted endpoint prediction (X--V) across multiple robot policies, benchmarks, and inference budgets. On StarVLA and LiLa-WAM, X--V works best for few-step generation, while V gains more from iterative refinement. We further uncover their complementary strengths across noise levels: clean actions have concentrated covariance spectra, endpoint predictions stay more stable under high noise, and velocity predictions offer more accurate corrections near clean actions. Inspired by these findings, we introduce UniVEP, which learns both prediction targets together with consistency supervision and switches from endpoint recovery to velocity refinement as noise drops. Each step only needs one network run, and joint training also boosts single-step endpoint generation. Tests on simulated and real-world manipulation show better success rates and efficiency. On RoboTwin, UniVEP hits 61.36% success with one StarVLA run, beating the best single-target baseline at sixteen runs (59.96%). With LiLa-WAM, two runs outperform the best sixteen-step single-target baseline and cut inference latency by 77.1%.

### Targeted In-Context Poisoning of Tabular Foundation Models: An Empirical Study
- arXiv 2611.28396v1 · v1 2026-11-20 23:03 UTC · cs.AI, cs.CR
- Authors: Adem Alparslan
- Topics: Manipulation · score 6 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.28396

> Tabular foundation models (TFMs) predict the label of a query row conditioned on a context of labelled rows, without training on them. Drawn from operational data, the context becomes an attack surface. We study targeted in-context poisoning in its simplest form: an attacker with write access to the context's source places exact copies of a target row there with the wrong label. On 30 OpenML datasets for binary classification, one such poison row flips on average 53% (TabICL) and 65% (TabPFN) of the predictions correct without attack, and three poison rows flip almost all. The same copy with the true label flips almost none, and performance on the remaining rows hardly changes. Predictions flip by two routes: in TabICL, the target row's embedding rotates towards the mean of the wrong class; in TabPFN, the poison row pulls genuine rows of the wrong class along. The TFMs thus infer soundly, but from forged evidence. Predictions of trained models flip as well: almost always for a random forest, for CatBoost as often as for the TFMs, hardly for a logistic regression. New with TFMs is not the kind of vulnerability but the timing: the data take effect at the moment of prediction, not through training, and a poison row in a live context can be deleted afterwards. Three established requirements must therefore cover the context: access control for its source, traceability per prediction, which can also deter, and validation at prediction time. A detection mechanism shows how such validation can work.

### A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation
- arXiv 2611.29338 · v1 2026-11-22 00:00 UTC · 
- Authors: Meng-Hao Guo, Yi Zhang, Zhe-Han Mo, Han-Zheng Wang et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.29338

> Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as semantic steps composed of reusable, parameterized action primitives, guided by explicit progress descriptions. Meanwhile, CP-SFT uses an explicit robot-specific system prompt to constrain manipulation outputs to a structured action space, aiming to focus adaptation on robot-specific contexts and promote specialization while minimizing interference with broader pretrained capabilities. With this formulation, we train nanoAstra on more than 5,000 hours of robot data together with general VQA data. On RoboTwin 2.0's randomized benchmark, nanoAstra-9B achieves a 17.8% zero-shot success rate, substantially outperforming advanced VLA and WAM baselines as well as similarly sized VLMs. With inference faster than the corresponding motion execution on a single H20 GPU, our model supports action-chunk-like streaming execution that overlaps inference with motion, reducing the robot's idle time from 35.0% to 6.9%.

### More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation
- arXiv 2611.29339v1 · v1 2026-11-22 09:15 UTC · cs.RO, cs.AI, cs.CV
- Authors: Xin Zhang, Yushuo Hou, Anqi Zhao, Moyun Liu et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.29339

> Latent reasoning lets Vision-Language-Action (VLA) models deliberate at a fraction of the cost of explicit chain-of-thought, increasingly through visual foresight, which we show to be indispensable for predicting actions. Yet this paradigm is inherited from Vision-Language Models, where it serves understanding rather than action: each latent is aligned with an isolated future frame, often enriched with further modalities of that frame. We find that this binds the policy to the appearance of its training scenes, so that it degrades sharply once the scene changes. We argue that visual latents for action should capture not what a future frame looks like, but how the scene evolves toward the goal. We therefore propose Motion-Oriented Latent Reasoning, which redirects visual latents from the whole frame to the interaction that the action must bring about. Semantic latents, following the stages of embodied chain-of-thought, first establish what to accomplish and how. Conditioned on them, motion-oriented latents anticipate each future step from coarse to fine: from the global scene, to the interaction region spanned by the manipulated object and its destination, to the robot state. Relative to the state-of-the-art latent VLA LaST$_0$, our method raises the mean success rate on SimplerEnv-WidowX from 37.5% to 55.2% in distribution and from 22.4% to 30.2% under out-of-distribution shifts, and on an AgileX Piper dual-arm platform from 60.8% to 90.8% in training scenes and from 6.7% to 37.5% under environmental changes.

### MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model
- arXiv 2611.29501v1 · v1 2026-11-22 14:16 UTC · cs.RO, cs.AI
- Authors: Rongze Tang, Chenyu Zhou, Jianjie Fang, Ziming Liu et al.
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.29501
- arXiv comment: Project page: https://embodiedcity.github.io/MAWAM/

> World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timing, and heterogeneous embodiments. Such coordination demands both spatiotemporal alignment of future interactions and awareness of individual embodiment and role identities, whereas existing decentralized per-robot policies, flat centralized models, and multi-robot VLAs fail to unite both. To bridge this gap, we present MAWAM, a multi-agent world action model that jointly predicts the future observations of multiple embodiments and decodes each agent's actions from them for collaborative manipulation. Through an agent-axis curriculum, MAWAM expands a single-agent WAM along an agent dimension to coordinate teams under shared weights. Within one unified causal sequence, joint self-attention spans all agents to spatiotemporally align their imagined futures, while hierarchical language, identity encodings, and embodiment masks bind each stream to its role, identity, and embodiment. We further formalize multi-agent-necessary manipulation along three axes (why, when, and who) and develop MA-Task Harness, a coding-agent pipeline where mutually constraining generators and evaluators co-evolve customizable simulation-data and evaluation packages. Using this pipeline, we build MA-Bench across all axes with seven tasks, pairing joint success rate with role and collaboration scores for fine-grained analysis. On MA-Bench, MAWAM reaches 82.7% mean joint success, 30.7% above the strongest baseline, and achieves real-time closed-loop collaboration on a real heterogeneous robot team.

### Relativising Integrity and Robustness: Prompt Injection and Partitioned Enclaves
- arXiv 2611.29802v1 · v1 2026-11-22 22:05 UTC · cs.CR
- Authors: Brijesh Dongol
- Topics: Manipulation · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.29802

> Relative security (RS) judges a system against a reference system, but has only been applied to confidentiality. We introduce relative integrity (RI), which states that every behaviour a system exhibits under an attacker's influence must be one the reference can exhibit for the same trusted inputs. RS and RI each choose their own reference runs, so together they accept attacks whose leak and effects the reference reproduces only in different runs. We therefore develop a further property, relative robustness (RR), which asks the same runs to reproduce both and is strictly stronger than RS and RI together. We give proof methods for RI and RR and a disproof method for RI, and apply them in two domains: (1) LLM agents under prompt injection, where the reference runs the same plan with a model that never obeys untrusted content, and (2) C programs partitioned across an SGX or TrustZone enclave boundary, where the reference keeps every function inside. We evaluate the properties on models of five published attacks, a support desk, an OP-TEE HOTP token and common agent defences. Two cases pass RS and RI but fail RR: an injection that makes the support desk's model accept any customer, as one input did in the Tensor Trust game, and the simulation step of the attack on Secret Network, in which an SGX enclave reveals a transfer's outcome without committing it. Our work is fully mechanised in Isabelle/HOL, with the enclave programs verified in C using AutoCorres2.

### HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation
- arXiv 2611.30813 · v1 2026-11-23 00:00 UTC · 
- Authors: Qiwei Liang, Zhengtu Liang, Minghao Lai, Yikeng Chen et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.30813

> Pretrained vision is a common start for robot learning, but most comparisons still score one pooled vector from a third-person image. Bimanual policies instead read dense patch tokens from cameras on the robot. We introduce HIVE-Bench: one shared flow-matching policy reads 20 encoders from seven families on 24 egocentric bimanual tasks, across adaptation, task sharing, and sweeps of data, model size, and layer. Keeping the patches matters. Averaging each view to one token removes most of the success, adaptation helps every pair we test, and one shared policy keeps most of the success of separate policies at a fraction of the updates. The same tokens are then scored with statistics, state and object readouts, published vision scores, and an inverse-dynamics readout. That readout of the commanded motion is one of the strongest measurements available before a policy is trained. Recognition, depth, and correspondence do not transfer reliably. Fine-tuning can improve the action readout even when other measurements move the other way, and no statistic is stable enough to replace a rollout before any deployment.

## More new topic matches, lower score, title only (18)
- Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection — https://arxiv.org/abs/2611.29977 (score 6; Manipulation)
- Spiking World-Action Models for Robotic Manipulation — https://arxiv.org/abs/2611.30041 (score 6; Manipulation)
- A statistical measure of trust in generative AI — https://arxiv.org/abs/2611.30286 (score 6; GEO/AEO, RAG (generic))
- Automated Call for Action: RAG-Based Environmental Law Enforcement Screening System — https://arxiv.org/abs/2611.30423 (score 6; Citation & source selection, RAG (generic))
- JEPA-ICL: Progress-Aligned Latent Plans for In-Context Robotic Manipulation — https://arxiv.org/abs/2611.30516 (score 6; Manipulation)
- RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation — https://arxiv.org/abs/2611.30555 (score 6; Manipulation)
- How Many Parameters Does Forecasting Need? A Survey and Code-Level Audit of Lightweight Long-Term Time Series Forecasting — https://arxiv.org/abs/2611.30685 (score 6; Clicks & measurement)
- Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression — https://arxiv.org/abs/2611.31089 (score 5; GEO/AEO)
- Close the Loop on the Retrievability Gap — https://arxiv.org/abs/2611.28146 (score 4; Brand/product recommendation)
- Beyond Relevance: An Empirical Study of Multimodal LLMs for Diversity-Aware Recommendation Reranking — https://arxiv.org/abs/2611.28379 (score 4; Brand/product recommendation)
- ChatGPT Can't Sell (And That's Probably a Good Thing): Buyer-Aligned AI Advice, the Sales-Representative Gap, and Evidence from Commercial Conversations — https://arxiv.org/abs/2611.28946 (score 4; Brand/product recommendation)
- Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and Judgement in Evidence-Grounded Verification — https://arxiv.org/abs/2611.29697 (score 4; Citation & source selection)
- DataRecycle: Trustworthy Distillation of Structured Data from Scattered Web Evidence — https://arxiv.org/abs/2611.29206 (score 3; Clicks & measurement)
- SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance — https://arxiv.org/abs/2611.30588 (score 2; RAG (generic))
- GERF: A Token-Efficient Multimodal Retrieval Framework for Schema-Guided Scientific Information Extraction — https://arxiv.org/abs/2611.28295 (score 1; RAG (generic))
- MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation — https://arxiv.org/abs/2611.28604 (score 1; RAG (generic))
- LLM-Based Assistant for Dog Care Guidance — https://arxiv.org/abs/2611.29286 (score 1; RAG (generic))
- Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees — https://arxiv.org/abs/2611.29966 (score 1; RAG (generic))

## Other new cs.IR papers, title only (16)
- Evaluating Memanto on DolphinBench for AI Agents — https://arxiv.org/abs/2611.28231
- The abc index: Exact Retrieval for Learned Sparse Representations — https://arxiv.org/abs/2611.28555
- Who Gets Re-ranked When a Clinical Model Gains New Data? — https://arxiv.org/abs/2611.28968
- HME-PFD: Heterogeneous Mixture-of-Experts Privileged Feature Distillation — https://arxiv.org/abs/2611.29094
- Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning via Language-Constrained Communication — https://arxiv.org/abs/2611.29112
- Zarc: Exact Nearest Neighbors over a Billion Vectors in Seconds — https://arxiv.org/abs/2611.29252
- NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge? — https://arxiv.org/abs/2611.29255
- VistaTree: Question Answering over Long Multimodal Documents with Image-Derived Summary Trees — https://arxiv.org/abs/2611.29419
- MoR4Rec: Mixture-of-Recursion for Sequential Recommendation — https://arxiv.org/abs/2611.29462
- Look Before You Leap: Re-Architecting Disk-Resident Vector Search with TriVS — https://arxiv.org/abs/2611.29948
- STUN-Bench: Truly Unseen Tools for Evaluating Shared Tool Experience — https://arxiv.org/abs/2611.30034
- Pixel as the Common Language: Unified Multimodal Embedding via Visual Rendering — https://arxiv.org/abs/2611.30069
- Beyond Knowledge Transfer: How User Overlap Shapes Diversity in Cross-Domain Recommendation — https://arxiv.org/abs/2611.30156
- Ontology-Compiled 2D Clinical State Fields with Bidirectional Diffusion Encoders for Zero-Training Cross-Ontology Medical Coding — https://arxiv.org/abs/2611.30218
- Trallie: from Free-Form Text to Structured Data with LLMs — https://arxiv.org/abs/2611.30773
- From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization — https://arxiv.org/abs/2611.31052

## Already listed on an earlier day, still inside the look-back window (34)
- GEOHunter: Mapping a Generative Engine Optimization Network in the Wild — https://arxiv.org/abs/2611.26564 (score 14)
- Seer: Guiding Small Deep-Research Agents with Shared Decision Models — https://arxiv.org/abs/2611.26423 (score 10)
- When Do LLM-Elicited Priors Help? A Controlled Audit of Language Models as Priors for Small-Sample Bayesian Regression — https://arxiv.org/abs/2611.27075 (score 10)
- Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation — https://arxiv.org/abs/2611.27689 (score 10)
- How Complete Must an Environment Be to Train a Capable GUI Agent? — https://arxiv.org/abs/2611.23946 (score 8)
- RouterWeave: A Unified Observation Layer for Cross-Platform Activity Analysis via Home Routers — https://arxiv.org/abs/2611.26134 (score 8)
- Visual Attribution Limits and Graded Provenance Auditing in Commercial Video-Generation APIs — https://arxiv.org/abs/2611.26508 (score 8)
- Modeling Attributional Style at Scale: A Dataset and Analysis for Psychological Attribution Assessment and Reframing — https://arxiv.org/abs/2611.26900 (score 8)
- EcomWriteBench: A Real-World Benchmark for E-commerce Writing Tasks — https://arxiv.org/abs/2611.27349 (score 8)
- Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification — https://arxiv.org/abs/2611.27410 (score 8)
- The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web Search — https://arxiv.org/abs/2611.27899 (score 8)
- Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI) — https://arxiv.org/abs/2611.26553 (score 7)
- Poisoning Attacks and Collaborative Defense Framework for LightRAG-Based Construction Regulation Knowledge — https://arxiv.org/abs/2611.27460 (score 7)
- Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation — https://arxiv.org/abs/2611.26444 (score 6)
- PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation — https://arxiv.org/abs/2611.26596 (score 6)
- MomentMem: Memorizing Key Moments for Robot Manipulation — https://arxiv.org/abs/2611.26745 (score 6)
- Same Facts, Different Decision: Fact-Invariant Manipulation and Provenance-Based Defense in Typed Decision Models — https://arxiv.org/abs/2611.27016 (score 6)
- Subverting Tool Arguments: Defense-Evading Metadata Poisoning in LLM Agents — https://arxiv.org/abs/2611.27041 (score 6)
- Manipulation-resistant reputation for peer-to-peer scientific publishing: a combination-therapy approach — https://arxiv.org/abs/2611.27625 (score 6)
- Redesigning Neural Networks to Not be Confidently Wrong even to Strong Adversarial Attacks — https://arxiv.org/abs/2611.27811 (score 6)
- Pre-Crawl Prioritization and Seed Classification for Large-Scale Web Archiving — https://arxiv.org/abs/2611.27743 (score 4)
- Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem — https://arxiv.org/abs/2611.26398 (score 1)
- Explicit Style Extraction for Personalized Long-Form Text Generation — https://arxiv.org/abs/2611.27211 (score 1)
