# Paper candidates — 2026-11-04 (IST)

Generated 2026-11-04 01:10 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 35 new topic matches · 24 other new cs.IR · 28 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (35), highest score first

### Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO
- arXiv 2611.01126v1 · v1 2026-10-31 17:15 UTC · cs.IR
- Authors: Runze Kong, Haibo Jin, Xucheng Yu, Xiaoqi Wang et al.
- Topics: GEO/AEO, RAG (generic), Brand/product recommendation · score 15 · found via cs.IR, search abs:"generative engine optimization"
- Link: https://arxiv.org/abs/2611.01126
- arXiv comment: 12 pages, 5 figures, 8 tables
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative engine optimization (GEO) rewrites web content so that LLM-based search systems, also termed generative engines (GEs), rank it higher in their answers and recommendations. However, existing GEO evaluations typically rely on directly supplied text or controlled retrieval pipelines, and whether GEO gains survive the live Web remains unclear, leaving a gap in understanding how GEO strategies affect the visibility of live webpages when accessed and ranked by GEs. To address this gap, we introduce LIVE-GEO, a benchmark for Live, In-the-wild Visibility Evaluation for GEO. LIVE-GEO publishes GEO-rewritten products as live webpages. We use LIVE-GEO to evaluate five existing GEO strategies (CORE, C-SEO, E-GEO, AgenticGEO, and Statistics Addition), applying them to the product descriptions and reviews of 80 fictional brands across 18 product families. We run experiments on three GEs (ChatGPT with GPT-6, Gemini 3.6 Thinking, and Grok in Expert mode), four direct-text API evaluators (GPT-4o, DeepSeek, Kimi, and Claude), and a direct-text local evaluator (Qwen2.5-3B-Instruct). With frozen $\pm0.2\%$ prices, most direct-text evaluators and GEs receiving product URLs give CORE the highest Top-1 rate, reaching 66.3%-76.3% on the GEs, yet other strategies vary in relative performance, and the GEs select the same top product for only 48.8%-66.3% of brands. We also find that ChatGPT is sensitive to the order of candidate URLs: CORE's Top-1 rate is 73.8% and 93.8% under two opposite fixed orders, and the randomized order used by LIVE-GEO yields 82.5%, between the two. In the numerical-faithfulness check, the JEV verifier agrees with the reference labels on 90.7% of 194 numerical benchmark cases and with human judgments on all 50 sampled descriptions, and it flags 86 of the 400 rewritten descriptions, including all 80 Statistics Addition descriptions.

### Building Weighted PubMed Citation Graphs at Scale: A Pipeline and an Audit of Edge-Similarity Features
- arXiv 2611.01044v1 · v1 2026-10-31 15:34 UTC · cs.SI
- Authors: Hossein Mohasel Arjomandi
- Topics: Citation & source selection, Clicks & measurement · score 14 · found via cs.SI
- Link: https://arxiv.org/abs/2611.01044
- arXiv comment: 6 pages, 6 tables. Submitted to the BTSD workshop at IEEE BigData 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Studies of scientific literature often combine citation links with article metadata, but the data preparation needed to do so at the scale of millions of papers is laborious and error-prone. This paper describes a pipeline that turns PubMed metadata and a citation network into a graph whose edges carry seven similarity features: bibliographic coupling and co-citation (each as a count and as a Jaccard coefficient), publication-year proximity, MeSH-term similarity, and similarity of MedCPT title-abstract embeddings. Applied to a citation network derived from the cell biology research literature, the pipeline yields 7,445,898 nodes and 57,512,086 edges with complete year, MeSH, title, and abstract metadata. The paper reports how nodes are matched across sources, how duplicate identifiers are resolved, and which intermediate tables grew to hundreds of gigabytes. An audit of the full feature table shows that 47.2% of the edges share neither references nor citing documents, so their topological features are zero, and that the MeSH feature is nonzero on only 0.28% of edges. Where both kinds of signal exist, they agree: edges with higher coupling also have more similar abstracts and closer publication years. In a pilot, replacing the median by a mean or best-match aggregation makes the MeSH feature nonzero on nearly all article pairs, and near-identical texts point to possible duplicate records that identifier checks miss. The parsing, graph-construction, and feature code are public; the paper states which data are released and which are not. A companion paper uses the resulting weighted graph for clustering.

### From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents
- arXiv 2611.01527v1 · v1 2026-11-01 03:58 UTC · cs.AI, cs.LG, q-bio.QM
- Authors: Xingyu Yi, Xinya Zhang, Yunshen Zhou, Haoyu Bao
- Topics: Citation & source selection, Query fan-out · score 14 · found via cs.AI
- Link: https://arxiv.org/abs/2611.01527
- arXiv comment: Accepted at NeurIPS 2026 AgenticLS Workshop; adds one experiment
- Full text: data/fulltext/2611.01527.txt

> A scientific agent can give the same verdict while reading and citing different evidence. BioAgent-DF tests this separation using paired reference and candidate values saved at the same scientific computation site. It restores or transplants those values at their original coordinates, then runs the agent on healthy hardware. Across eight SciFact batches, Qwen3.5-4B shows repeatable citation changes in three capture-claim combinations, and Gemma 3 4B IT shows repeatable read and citation changes in four. These seven combinations cover two claims. Full restoration recovers the reference evidence sets while verdicts remain unchanged. Verdict changes observed under the baseline prompt did not recur under the explicit-example prompt. Complementary tool and optimizer experiments distinguish recovery of numerical state, recovery of ranked lists, and restoration of an agent's visible history. These results show that an audit should track both the evidence an agent uses and its final answer. In hERG cardiac-safety assay allocation, silent numerical faults changed testing decisions while the fixed-budget shortlist kept the same number of compounds labeled as blockers. After the agent had used faulty values, restoring its earlier execution state and supplying certified scores recovered all 39 changed decisions, whereas replacing the prediction file recovered none; no incorrect action was committed. A streaming implementation of the arithmetic checks reduced the total time for forward execution and verification by 42.4% relative to the original FP64 implementation, with identical flags and recovery outputs.

### FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting
- arXiv 2611.01621v1 · v1 2026-11-01 06:16 UTC · cs.CL, cs.LG
- Authors: Fengyuan Liu, Mukai Li, Jieshun You, Yilin Zheng et al.
- Topics: Citation & source selection, Query fan-out · score 14 · found via cs.CL
- Link: https://arxiv.org/abs/2611.01621
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Anticipating financial outcomes requires synthesizing evolving evidence and reasoning under uncertainty, making deep research systems promising tools for forecasting. Yet evaluating forecasting ability is challenging because historical backtests may reward memorized outcomes or information retrieved after the forecast date. Live forecasting avoids direct access to realized outcomes, but feedback arrives only after events resolve. To obtain timely feedback and assess historical scores, we introduce FinForesight, a diagnostic backtesting benchmark for financial deep research systems. Across the Chinese, U.S., and Hong Kong markets, the benchmark evaluates four forecasting tasks: valuation, return ranking, event direction, and future financial fundamentals. Two capability diagnostic tasks assess counterfactual reasoning and financial calculation, scored separately from forecasting performance. Our harness-compatible framework restricts retrieved evidence to information available at the forecast date. We compare pretraining-era, resolved post-cutoff, and live evaluations to test whether controlled backtests approximate future performance. Pretraining-era scores exceed post-cutoff scores in most temporal comparisons, and stronger retrieval controls narrow the gap between post-cutoff backtests and live results. Forecasting attribution and robustness analyses reveal how scores respond to retrieval policy and how predictions respond to prompt rewrites and numerical perturbations. The code and benchmark data are publicly available.

### When 200 OK Is Not an Answer: Silent Fetch Failures in Agentic Web Content Acquisition
- arXiv 2611.00884v1 · v1 2026-10-31 12:42 UTC · cs.CL, cs.IR, cs.NI
- Authors: Shuyang Zhang
- Topics: GEO/AEO, Citation & source selection, Agents · score 13 · found via cs.CL, cs.IR, search abs:"answer engine"
- Link: https://arxiv.org/abs/2611.00884
- arXiv comment: 10 pages, 3 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Web agents and answer engines fetch pages at question time, and liveness checks of cited sources treat an HTTP 200 response as success. We measure how often that assumption fails and what it does to measurements built on fetched pages. We fetched 10,307 URLs in three days with a polite static client and a rendered browser client: pages from 1,507 sites in five strata, random non-existent paths on every site, and the 4,795 URLs cited by expert-verified claims in ExpertQA. We define a taxonomy of what a 200 response contains, label the static 200 responses automatically, and check the labels against 300 items reviewed by an LLM-based assistant; a human check of 60 of them retained every reviewed usability label after discussion. By the automatic labels, 20.9% of the pages that a static client receives with status 200 do not contain the page's main content: app shells, bot challenges, block pages, error and placeholder pages, and partial content. On the held-out test split, the reviewed sample lowers this estimate from 25.5% to 20.0%. 13.1% of the sites whose random-path probe was answered returned 200. The error propagates: for the cited sources, treating 200 as content overstates the share of claim-source pairs that can be checked against live content by 12.2 points and inflates the apparent silent citation-drift rate from 5.8% to 21.9%. Cheap heuristics catch most of it. Text length, probe comparison and redirect-to-root, combined and tuned on held-out sites, recover 86% of unusable reviewed responses at a false-alarm rate near 5%. Content-reading detectors perform comparably: the best, the text classifier, gains five to seven points of recall at more than twice the false-alarm rate. We argue that agents and their evaluations should report fetch outcomes explicitly instead of inferring them from the status line and will release the labelled data and code.

### AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising
- arXiv 2611.00822v1 · v1 2026-10-31 11:07 UTC · cs.AI, cs.CY, cs.LG
- Authors: Woo Jae Kim, Seongho Keum, Joonsung Jeon, Suhyeon Ha et al.
- Topics: Citation & source selection, Ads · score 12 · found via cs.AI, cs.CY, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.00822
- arXiv comment: NeurIPS 2026
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Large language model (LLM)-native advertising has emerged as a viable monetization channel as LLM service providers seek sustainable revenue streams. However, integrating native ads into LLM responses introduces two largely understudied challenges: (1) controlling ad intensity -- how prominently advertising content appears -- and (2) ad labeling -- identifying which segments of the generated text constitute advertising. We propose AdKnob, a framework jointly addressing both challenges. For ad intensity control, we introduce new ad control tokens without pretrained semantic associations and align the model via direct preference optimization to generate ads at each desired level. For ad labeling, we propose an attention rollout-based attribution mechanism that identifies ad segments by tracing their attribution to input ad-related tokens, requiring no additional inference cost. We further construct MI-KnobSet, the first multi-level ad intensity preference dataset for LLM-native ads. Experiments across six LLMs and human evaluations show that AdKnob achieves uniformly spaced ad intensities where baselines collapse to a narrow range, achieves the highest ad labeling accuracy while being over 500x faster than the strongest baseline, and is preferred over baselines by human evaluators up to 89.6% of the time.

### Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce Relevance
- arXiv 2611.02758v1 · v1 2026-11-02 08:39 UTC · cs.IR
- Authors: Shi Shu, Hao Chen, Baopu Qiu, Chao Wei et al.
- Topics: Brand/product recommendation, Ads · score 12 · found via cs.IR, search abs:"advertising" AND abs:"large language model"
- Link: https://arxiv.org/abs/2611.02758
- Full text: data/fulltext/2611.02758.txt

> Relevance modeling is fundamental to e-commerce search, determining how well retrieved products satisfy the needs expressed in a user's query. Accurate judgments require interpreting user intent, comparing product attributes, and applying business-specific matching criteria. Current methods based on large language models (LLMs) leverage contextual understanding and reasoning, focusing on incorporating domain-specific context and enhancing reasoning performance. Despite these advances, difficult query-product pairs remain challenging when evidence from different perspectives supports conflicting conclusions. A single reasoning pass may fail to reconcile these conflicts and ensure that decisive evidence guides the final judgment. To address this challenge, we propose Collaborative Adjudication with Debate and Replay Experience (CADRE), a framework for evidence-based adjudication in e-commerce relevance assessment. CADRE organizes three expert agents sharing a frozen backbone to analyze product attributes, user intent, and business rules in separate contexts, while a trainable Verifier assesses their supporting evidence against the applicable matching criteria to determine relevance. Under expert disagreement, a Verifier-guided debate elicits targeted clarification and revision of disputed interpretations before final adjudication. We optimize the Verifier through multi-turn group relative policy optimization and adapt successful-experience replay so that trajectories yielding correct terminal labels can be reused alongside fresh rollouts in subsequent updates. For efficient online serving, we use CADRE as an offline teacher to distill its relevance judgments into a lightweight student model. Offline evaluations and online A/B tests on an e-commerce search advertising platform demonstrate that CADRE improves relevance classification and key business and relevance satisfaction metrics.

### StreamDuo: A Live Commentator and a Research Agent for Unseen Games
- arXiv 2611.01120 · v1 2026-10-31 00:00 UTC · 
- Authors: Zixian Gao, Penghao Luo, Xiangcheng Cao, Lixin Xiu et al.
- Topics: Query fan-out · score 10 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.01120
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowledge of the game world. We propose StreamDuo, which pairs a trainable commentator with a frozen research agent that reads the wiki of the game being played. When the commentator sees something it cannot name, it sends the current frames, and the research agent returns a few wiki entries two seconds later while the stream continues. We train only the commentator, on a single game, in two stages. Information-gain labels teach it to ask only where an answer would help it say what the human caster said, and on-policy self-distillation from a copy of itself that sees the ideal answer teaches it to use noisy answers. Trained on Baldur's Gate 3 and tested on ten unseen games, StreamDuo raises entity recall from 0.082 to 0.116 over Proact-VL trained on the same data, cuts source-game leakage from 9.9% to 1.0%, and achieves the best timing and the highest judged liveliness and overall quality among streaming models.

### Designing Informative Actions: Action Construction for Long-Horizon Research Agents
- arXiv 2611.00773v1 · v1 2026-10-31 09:33 UTC · cs.AI
- Authors: Alkut Arxidin, Shaoning Zeng, Jianhang Zhou, Jianping Gou et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.00773
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language model agents support automated scientific research by connecting literature analysis and planning with experimentation. Evaluating which action an agent selects does not establish which experiment its instruction specifies, because omitted interventions or replication counts leave consequential choices to the executor. We introduce a reading-set framework for evaluating action construction under a common cost rule. Across 30 synthetic states, complete-design requests increase affordable efficiency by 465.98% and 327.91% relative to the action-name baseline in the two model families, respectively. An author-constructed research-action evaluation dataset provides 60 scenarios for complementary judgment evaluation. On this dataset, the scenario-level information-per-cost measure has a mean within-scenario correlation of 0.733 with judgments from 18 human participants. The framework makes design specification and execution ambiguity measurable, providing a reproducible basis for assessing how research agents translate scientific intent into informative, budget-feasible experiments.

### Measuring User Success in Randomized Search Experiments: Interpreting Good Abandonment in Generative AI Search
- arXiv 2611.01582v1 · v1 2026-11-01 05:06 UTC · cs.IR
- Authors: Minha Hwang, Shavak Agrawal, David Chen, Carto Wong et al.
- Topics: GEO/AEO · score 10 · found via cs.IR
- Link: https://arxiv.org/abs/2611.01582
- arXiv comment: 2026 CODE@MIT Conference
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Randomized search experiments increasingly evaluate experiences in which large language models answer information needs directly on the results page. Click status alone cannot identify success: a click may lead to an unsatisfactory result, while no click may indicate successful answer consumption, or "good abandonment." Prior research has shown that good abandonment is difficult to detect because dwell, scrolling, and reformulation are meaningful only in context. We present Session Success Rate (SSR), a human-grounded, interpretable outcome metric designed for online controlled experiments. Trained judges label complete session experiences using privacy-protected interaction evidence and video recordings; these offline labels train models scored online from query events, viewport behavior, result-page interactions, and semantic reformulations. Out-of-sample evaluation on 6,904 labeled queries yields 0.75 balanced accuracy overall and 0.68 within abandoned queries; session-level balanced accuracy is 0.68. The sample shows why interaction status is not an adequate outcome: 53.2% of abandonments were successful and 6.5% of clicked queries were unsuccessful. In a validation portfolio of seven ranking and five non-ranking experiments, SSR agreed with Sessions per User in seven cases, was inconclusive in four, and disagreed in one under a common p < 0.05 rule. Separately, across approximately 4,000 production experiments, SSR produced about 2.5 times the binary sensitivity of Sessions per User; in the studied workflow, this supported lower traffic allocations and greater experiment throughput under a fixed traffic budget.

### Same Trajectory, Different Knowledge: Information-State-Aware On-Policy Distillation for Search Agents
- arXiv 2611.01987v1 · v1 2026-11-01 15:24 UTC · cs.IR
- Authors: Minhao Sun, Xian-Ling Mao, Eric Tao, Zi-Ao Ma et al.
- Topics: Query fan-out · score 10 · found via cs.IR
- Link: https://arxiv.org/abs/2611.01987
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> On-policy distillation trains search agents with teacher feedback on student-generated trajectories. Recent methods augment the teacher's context with supporting evidence, reference answers, or hindsight information. However, this privileged information may allow the teacher to rely on facts that the student cannot reliably recover from its current state. The resulting information-state mismatch can lead the teacher to undervalue retrieval that helps the student establish those facts. To address this mismatch, we introduce Information-State-Aware Distillation (ISA-Distill), which adapts teacher feedback to the student's factual recoverability. ISA-Distill estimates how reliably the student can recover action-relevant knowledge and derives teacher feedback for the same sampled action from two complementary views. The fact-use view supplies the teacher with the relevant fact, producing feedback that guides the student in using knowledge. The evidence-seeking view instead presents the information need, producing feedback that guides the student in acquiring supporting evidence. The two signals are weighted toward fact use when recoverability is high and toward evidence seeking when it is low, and the resulting feedback guides policy optimization. Experiments across diverse QA benchmarks and model scales demonstrate improved answer accuracy and retrieval efficiency. Our code and model checkpoints will be open-sourced.

### DR Pixel: Page-Native Deep Research with Vision-Language Models
- arXiv 2611.03097v1 · v1 2026-11-02 13:13 UTC · cs.CL, cs.CV, cs.IR
- Authors: Tiansheng Hu, Yichuan Wang, James V. Talwar, Nicholas Tomlin et al.
- Topics: Query fan-out · score 10 · found via HF daily papers, cs.CL, cs.IR
- Link: https://arxiv.org/abs/2611.03097
- Full text: data/fulltext/2611.03097.txt

> Complex documents such as scientific papers contain rich information in tables, figures, and equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted text. We instead ask whether vision-language models (VLMs) can enable page-native deep research: directly retrieving and reasoning over rendered document page images. We introduce DR Pixel, the first open-source end-to-end multimodal DR agent that uses rendered page images as its sole retrieval and reasoning unit, operating over a corpus of 1.06M pages. To evaluate this setting, we construct DRPixelBench, a benchmark on scientific papers requiring reasoning over text, figures, tables, and equations. Surprisingly, page-native DR already works well without training, outperforming OCR-based baselines across state-of-the-art models like GPT-5.4, Gemini-3.5-Flash, and Qwen3.6-27B, while requiring fewer tool calls. We next turn to DR training. A key challenge is that teacher trajectories for agentic supervised finetuning are noisy, mixing critical reasoning and action steps with redundant or failed attempts. To address this, we introduce counterfactual credit reweighting, a fine-grained credit assignment method that weights individual reasoning and action steps by their counterfactual contribution to the final answer. Our training improves retrieval recall by about 15 points and final accuracy by over 10 points on DRPixelBench, and likewise outperforms the untrained baseline on four existing benchmarks. On out-of-distribution ViDoRe-V3, DR Pixel comes within 1.8 points of an oracle that is given the gold pages directly. Our results suggest that the conventional OCR-then-retrieve pipeline is not only unnecessary but suboptimal: directly retrieving and reasoning over visual document pages makes complex DR both more effective and more efficient.

### Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction
- arXiv 2611.03183v1 · v1 2026-11-02 14:17 UTC · cs.AI
- Authors: Zilu Zhang, Jing Bao, Lifeng Qiao, Sheng Xu et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.03183
- Full text: data/fulltext/2611.03183.txt

> Protein-complex structure prediction with AlphaFold 3 depends on MSA content, depth, and cross-chain pairing. Current pipelines apply uniform recipes, typically maximizing depth and pairing by species, yet even whether cross-chain pairing helps AF3 remains contested. We show that the value of both depth and pairing is strongly target-dependent, so no single recipe is optimal across interfaces. We introduce an autonomous agent that treats a frozen AF3 as a black-box experimental instrument. For each target, the agent formulates biological hypotheses, analyzes and reorganizes the MSA, and iteratively refines sequence selection and pairing using predictor label-free signals alone. On 1{,}015 protein--protein interfaces from three benchmarks released after AF3's training cutoff, the agent improves overall interface DockQ over AF3's default pipeline and fixed MSA recipes on every benchmark, while using on average 60\% fewer MSA sequences than the default. Gains are largest for inter-species heteromers, where species-based pairing is unreliable: mean DockQ increases from 0.465 to 0.612 on FoldBench and from 0.482 to 0.562 on HD439. The improvements arise from both sequence construction and pairing policy, including deliberate non-pairing.These results recast MSA design as a target-specific problem and show that an autonomous agent can adapt it at test time through biological reasoning and self-directed, confidence-guided experimentation.

### Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents
- arXiv 2611.03384v1 · v1 2026-11-02 16:24 UTC · cs.AI, q-fin.ST
- Authors: Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez, Ethan Setrouk et al.
- Topics: Query fan-out · score 10 · found via cs.AI
- Link: https://arxiv.org/abs/2611.03384
- arXiv comment: 9 pages, 2 figures. Accepted at ICAIF 2026, Milan, Italy
- Full text: data/fulltext/2611.03384.txt

> Financial research agents can generate and monitor trading rules faster than a human can document the resulting selection process. Candidates appear at data-dependent times, weak rules are abandoned, and promising ones are watched until they cross a reporting threshold. We introduce PROMOTE, a protocol that assigns every candidate predictable testing wealth at birth and accumulates a cost-aware e-process only from subsequent returns. If lifetime allocations sum to at most one, a weighted Ville argument bounds the probability of ever promoting a rule whose declared bounded net score has always had nonpositive conditional mean. The result permits dependent candidates, adaptive births, and indefinite monitoring. We audit the implementation in two settings. A retrospective pseudo-out-of-sample replay contains 24 panel--rule hypotheses, 3,000 shared-sign null paths, injected alternatives, and public ETF and industry data. Repeated unadjusted tests produce a family crossing in 94.5% of null paths, versus 0.0% for PROMOTE; at a 15-bp aligned ETF-component perturbation, PROMOTE has 70.1% target power and median crossing session 2,327. A separate exact mean-zero experiment lets an agent select candidate identities and birth times from past scores; the funded gate has 1.77% false-family crossings across 3,000 programs. The market replay produces zero promotions after costs. The certificate controls historical false promotion under the declared null; it is not a certificate that an earlier edge remains profitable at deployment. AI-use disclosure. Generative AI tools, including OpenAI Codex, assisted manuscript preparation. For this preprint version, Codex assisted with LaTeX editing, author and venue metadata, compilation, and layout checks.

### MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study
- arXiv 2611.03555v1 · v1 2026-11-02 18:17 UTC · cs.AI, cs.CR
- Authors: Farooq Shaikh, Biagio Montaruli
- Topics: Brand/product recommendation, Manipulation · score 10 · found via cs.AI, cs.CR
- Link: https://arxiv.org/abs/2611.03555
- arXiv comment: Accepted at the 19th Workshop on Artificial Intelligence and Security (AISec '26), co-located with ACM CCS 2026, The Hague, Netherlands. 12 pages, 3 figures, 9 tables; 4-page supplement included as ancillary file
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions without confirming real execution. We present the first cross-framework measurement of MCP tool poisoning with real tool execution. A 25-class root-cause taxonomy unifies prior classifications, and the open-source tool mcpvenom drives a 9,720-cell susceptibility matrix across 12 frameworks, 18 models, and 45 attack scenarios, with a dual oracle that confirms exfiltration via canary HTTP receipt. The overall attack success rate is 22.9% (2,113 vulnerable cells). Of these, 64.9% dispatch an attacker tool call, 23.0% contact the attacker endpoint, and 12.1% verifiably exfiltrate a secret. Resistance is model-level: nine core frameworks cluster within 23 to 26% (chi-squared = 3.30, p = 0.91), and no framework implements intentional defense. Incidental framework properties mitigate in specific cases, and a regex description scanner rejects 20 of 45 scenarios at a 7.2% false-positive rate, so metadata scanning alone is a partial control. Model ASR ranges from 0.4% to 49.7%. Claude Opus 4.8 is vulnerable in 8 of 530 cells while issuing 223 explicit refusals. A code-level audit finds no intentional defense across twelve frameworks, and all five coordinated disclosures across four vendors were rejected.

### Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions
- arXiv 2611.03052v1 · v1 2026-11-02 12:47 UTC · cs.HC
- Authors: Takeru Hashimoto, Yutaro Hirao
- Topics: Clicks & measurement, Manipulation · score 9 · found via cs.HC
- Link: https://arxiv.org/abs/2611.03052
- arXiv comment: 14 pages, 12 figures. Author-prepared version of the UIST 2024 paper. Both authors contributed equally
- Journal ref: Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology (UIST '24), Article 137, pp. 1-14 (2024)
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> We propose Selfrionette, a controller that uses fingertip force input to drive avatar movements in virtual reality (VR). This system enables users to interact with virtual objects and walk in VR using only fingertip force, overcoming physical and spatial constraints. Additionally, by fixing users' fingers, it provides users with counterforces equivalent to the applied force, allowing for diverse and wide dynamic range haptic feedback by adjusting the relationship between force input and virtual movement. To evaluate the effectiveness of the proposed method, this paper focuses on hand interaction as a first step. In User Study 1, we measured usability and embodiment during reaching tasks under Selfrionette, body tracking, and finger tracking conditions. In User Study 2, we investigated whether users could perceive haptic properties such as weight, friction, and compliance under the same conditions as User Study 1. Selfrionette was found to be comparable to body tracking in realism of haptic interaction, enabling embodied avatar experiences even in limited spatial conditions.

### Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay
- arXiv 2610.27954 · v1 2026-10-20 00:00 UTC · 
- Authors: Byeonghun Bang, Sangwoo Park, Jinheon Baek, Kangsan Kim et al.
- Topics: Agents · score 8 · found via HF daily papers
- Link: https://arxiv.org/abs/2610.27954

> Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unintended side effects, making the ability to recover from failures critical. Yet, existing remedies remain inadequate: environment resets are infeasible in proprietary settings, action replay is prohibitively expensive over long horizons, and API-based rollback is limited to web environments, leaving model-based recovery largely unexplored. To address this gap, we present ReTrace, a scalable evaluation framework for systematically studying recovery behavior in computer-use agents. We formalize Transition-Consistent Recovery: identical downstream actions from the recovered and target states must yield identical outcomes. We operationalize this criterion through goal-oriented action replay following controlled error injection. Using ReTrace, we present the first systematic study of autonomous, model-based recovery, revealing that (i) ideal recovery can unlock model's latent task completion capabilities, (ii) current computer-use agents fail to exploit their latent recovery capabilities, and (iii) accurate model-based recovery yields measurable end-to-end gains. Together, these findings establish recovery as a fundamental capability for building reliable computer-use agents. Our code and dataset is available at https://github.com/BangProx/ReTRACE.

### MemU-Bench: Benchmarking GUI Agents on Long-Horizon User Interactions
- arXiv 2611.00191v1 · v1 2026-10-30 17:41 UTC · cs.AI, cs.CV
- Authors: Yizhou Liu, Zhengxi Lu, Fei Tang, Yiwen Qiu et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.00191
- Full text: data/fulltext/2611.00191.txt

> Existing Graphical User Interface (GUI) benchmarks predominantly rely on precise and stateless user instructions. In everyday usage, however, instructions are often \emph{vague and history-dependent}: users omit the exact details of their past operations because they no longer remember them, leaving the agent to recover the missing context from long and noisy interaction histories. To bridge this evaluation gap, we introduce \textbf{MemU-Bench}, a mobile benchmark of \textbf{118 vague tasks} grounded in 29 long-horizon user trajectories, where agents must distill raw interaction streams into memory and retrieve the missing context on demand, with task outcomes verified against serialized application databases. Alongside Success Rate, we incorporate Interaction Efficiency (IE) and Success weighted by Path Length (SPL) to expose agents that succeed by exhaustively searching across different applications rather than by \emph{genuinely recalling} the history. Evaluations show that without user history, state-of-the-art systems struggle under such ambiguity: the best-performing Gemini-3.1-Pro achieves an SPL of only 16.4\%, and end-to-end GUI agents fall below 5\%. To address this, we further propose \textbf{AppMem}, a training-free framework that distills user history into a \emph{structured, app-centric} memory bank, tracks interrupted intents across application switches, and selectively retrieves relevant memories via target-app inference. AppMem raises the SPL of GPT-5.5 from 15.7\% to 66.9\% (\textbf{+51.2\%}), outperforms a naive summary baseline by 9.3\%, and delivers consistent gains across evaluated backbones.

### Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries
- arXiv 2611.00420v1 · v1 2026-10-30 22:12 UTC · cs.CL
- Authors: Shariar Kabir, Hong Kiat Tan, Swastik Agrawal, Sai V R Chereddy et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.00420
- arXiv comment: Extended version of a paper presented at the Mechanistic Interpretability and Compositional Learning workshops at ICML 2026
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Attribution graphs, an emerging tool in mechanistic interpretability, use transcoders to decompose language model computations into sparse interpretable features connected by causal edges. However, turning a graph into a safety-relevant insight requires hours of manual analysis by experts. We introduce Circuit Oracle, an off-the-shelf LLM equipped with a multi-agent harness and task-specific authored skills, which answers natural-language questions about a target model by reading the attribution graph through tool calls. We evaluate it on three safety-relevant proxy tasks: detecting spurious features in probe circuits, eliciting hidden knowledge from taboo-finetuned models, and suppression jailbreaking via feature-level interventions. Beyond task scores, the oracle produces pruned subgraphs and context-specific feature explanations that we assess qualitatively. Results are mixed. On spurious-feature detection, Circuit Oracle reaches 78.2 $\pm$ 2.4% accuracy, outperforming single-layer feature-ranking baselines. On secret elicitation, trained self-explainers like Activation Oracles remain the stronger baseline. On refusal suppression over 50 prompts, its single committed intervention is slightly below a diff-in-means baseline, and only exceeds it when allowed the best of five attempts. Results are stable across five runs and across model choices for the agents. We also release the pruned subgraphs and context-specific feature readings that revise existing global labels, and invite future work to develop evaluations that can measure their usefulness directly.

### Multi-Estimate Elicitation Does Not Uniformly Debias Language Model Judgments
- arXiv 2611.00597v1 · v1 2026-10-31 03:46 UTC · cs.AI, cs.CL
- Authors: An-Sheng Jhang
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.00597
- arXiv comment: 47 pages, 3 figures
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Does eliciting five weighted estimates within a single response change how a language model responds to information? Across anchoring, hindsight, base-rate, conjunction, and status-quo/default tasks, we compare direct numerical answers with a multi-estimate response format, contrasting source framings, explicitly random cues, and probability-consistency constraints. We evaluate three completed configurations--gpt-6.1-sol, claude-sonnet-5.5, and Qwen3-8B (reasoning disabled, analyzed descriptively). In the first two configurations, direct elicitation yielded near-zero irrelevant-anchor indices and status-quo effects, while remaining responsive to informative sources and informed advice. Of 23 preregistered confirmatory tests, six rejected after Holm adjustment; however, all six absolute point estimates fell below their prespecified smallest effect sizes of interest without establishing equivalence. Moreover, while separate versus joint elicitation shifted conjunction judgments, interpretation is constrained by between-call noise. Ultimately, multi-estimate elicitation failed to produce uniform debiasing or response attenuation across tasks and models, though post hoc correlations between candidate spread and anchoring error motivate independent predictive validation. Materials: https://github.com/asj252/llm-judgment-studies

### Sparse Autoencoder Attribution Graphs Are Decided at the Margin
- arXiv 2611.00606v1 · v1 2026-10-31 04:03 UTC · cs.AI, cs.CL, cs.LG
- Authors: Karl Li
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.00606
- arXiv comment: 34 pages, 8 figures
- Full text: data/fulltext/2611.00606.txt

> Attribution graphs over the features of sparse autoencoders (SAEs) are used to predict what an ablation does and are compared across training seeds. A TopK SAE keeps the largest preactivations at each token, and a feature's margin is its preactivation's distance to the cutoff. On five public TopK SAE pairs from three Pythia models, zeroing one feature moves a next layer feature across the cutoff in 0.74 of cases or more, and the crossings carry most of the response's energy. Over writes that scale a feature's code by three factors, the graph built on the features active beforehand has a median relative error of 0.247 or more. The margin graph adds the first order change to every preactivation and reranks, at the same cost, and errs by at most 0.033. At the median, the crossing features' decoded change is 1.24 times the model's own change in norm or more. Between seeds of one testbed, sparse maps between features explain 0.85 of a graph's energy on its active features, and 0.47 once the other seed's graph keeps only its own. The largest model studied is pythia-160m.

### PhoneValue-Bench: A Multimodal Benchmark and Datasets for Consumer Smartphone Recommerce Valuation
- arXiv 2611.00791v1 · v1 2026-10-31 10:09 UTC · cs.CV, cs.AI
- Authors: Zihan Deng, Jun Gao
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.00791
- Full text: data/fulltext/2611.00791.txt

> As consumer smartphone recommerce scales, buyers must quote binding repurchase prices from seller-uploaded multi-view photos and diagnostic screenshots before devices reach the warehouse. Accurate remote valuation requires fusing noisy cosmetic evidence with identity, battery, lock, and channel risk from screenshots and staff forms, since an error in any modality changes both grade and payout. However, existing multimodal resources mainly target general VLM competence, screen reading, or factory defect detection, and largely overlook staff-aligned trade-in fields, dual appearance/staff ground truth, and executable valuation scorecards. This gap stems from two challenges: (1) the lack of large-scale real trade-in data with audited dual annotations and a compact ranking benchmark kept separate from training labels, and (2) the need to jointly reason over unordered multi-view cosmetics and diagnostic screens under operational deduction rules. To address these challenges, we propose PhoneValue-Bench, a dual-GT evaluation suite with tier-gated scorecards, together with PhoneValue-Corpus, a matched weakly labeled training set of over twenty thousand orders and hundreds of thousands of captioned images. We further present ValueAgent, a staged perception-fusion-valuation reference pipeline aligned with production inspection, plus an executable public scorer and submission schema. Experiments show that ValueAgent reaches a measured 84.1/100 on Bench-Full, with 97.0 appearance fill and 54.1 staff-field fill, establishing a practical dual-GT benchmark for multimodal recommerce valuation.

### Similarity-Weighted Leiden-CPM Clustering of a 7.4-Million-Node Biomedical Citation Graph: Weight Alignment, Scale, and Sparsity
- arXiv 2611.01049v1 · v1 2026-10-31 15:42 UTC · cs.SI
- Authors: Hossein Mohasel Arjomandi
- Topics: Citation & source selection · score 8 · found via cs.SI
- Link: https://arxiv.org/abs/2611.01049
- arXiv comment: 7 pages, 1 figure, 3 tables. Submitted to the KGBigdata workshop at IEEE BigData 2026

> Clustering citation networks into research communities supports science mapping, research evaluation, and the analysis of funding portfolios. Biomedical articles also carry metadata, such as MeSH terms, publication year, and abstracts, that can be turned into similarity-based edge weights for Leiden clustering under the Constant Potts Model (CPM). Studies of hybrid relatedness compare the accuracy of such clusterings, but how the weights interact with the CPM resolution parameter on a large graph is less clear. Here it is shown that, on a citation network derived from the cell biology research literature (7.4 million nodes, 57.5 million edges), the effect of the weights is governed mainly by their scale and by edges of weight zero, and that, once these are controlled, weighting gives modestly more coherent clusters. Edges were weighted with seven topological and semantic similarity features and clustered with Leiden-CPM, using a method updated to fix a bug in how earlier code attached weights to edges. Mean weights of 0.0015 to 0.23 raised the effective resolution 4- to 650-fold; dividing by the mean restored most of the coverage, except for topological weightings, in which the 47% of edges with weight zero hold most of it. At equal coverage, weighted clusters were more coherent than unweighted ones, also on features outside the weight. For weighted CPM clustering, weights should therefore be attached to edges by key, normalized or reported with their effective resolution, and checked for zero-weight edges.

### Acceptance and Responsibility Attribution Toward Autonomous Ambulances Across Driving Conditions: A Preliminary Survey of Fire Service Personnel
- arXiv 2611.01132v1 · v1 2026-10-31 17:22 UTC · cs.CY, cs.HC
- Authors: Hirotake Yamazoe, Shingo Yamaguchi
- Topics: Citation & source selection · score 8 · found via cs.CY, cs.HC
- Link: https://arxiv.org/abs/2611.01132
- arXiv comment: The 2nd International Workshop on Trust and Blame in Multi-Person Multi-Agent Societies (TBSA_2nd) in conjunction with HAI 2026, 6 pages, 2 figures

> Traffic incidents involving ambulances and fire engines during emergency-response driving can have serious consequences. Although autonomous driving technologies may reduce workload and improve safety, their introduction into emergency services requires consideration of first responders' trust, willingness to ride (WTR), and perceptions of responsibility. We surveyed 34 fire service personnel from a single fire station in Himeji, Japan, to examine their evaluations of autonomous ambulances and responsibility attribution under non-emergency and emergency driving conditions. Emergency driving was associated with lower perceived usefulness for improving safety, trust, and WTR, as well as greater anxiety. In contrast, responsibility attribution remained largely stable, with 30 participants ($88.2\%$) selecting the same primary responsible party across conditions and the onboard crew most frequently selected in both. Among these 30 participants, 26 ($86.7\%$) also assigned the same responsibility share. Open-ended responses revealed concerns about system reliability, the complexity of emergency driving, and the need for human judgment, as well as considerations regarding operator and organizational responsibility. These findings suggest that acceptance of autonomous ambulances is sensitive to driving conditions, while responsibility judgments may also reflect perceived professional roles and responsibilities.

### Are Fake Citations a Form of Reward Hacking? A Pre-Registered Study of Post-Training and Citation Cues
- arXiv 2611.01313v1 · v1 2026-10-31 22:24 UTC · cs.AI, cs.CL, cs.LG
- Authors: Zain Naboulsi
- Topics: Citation & source selection · score 8 · found via cs.AI, cs.CL
- Link: https://arxiv.org/abs/2611.01313
- arXiv comment: 49 pages, 3 figures, 20 tables. Code and data: https://github.com/zainnab-sparq/citation-reward-hacking (archived at doi:10.5281/zenodo.23845528)
- Full text: data/fulltext/2611.01313.txt

> Post-trained language models fabricate citations at high rates. We ask whether that is reward hacking: scoring well on a proxy for scholarship while doing worse on what it stands for. We ran four pre-registered experiments on 900 frozen questions (US federal case law, computationally adjacent scientific literature, and medical literature) across twelve open-weights checkpoints covering four post-training stages of three model families, then refit on fifteen. The clearest result holds the weights fixed and changes only the prompt. Asking for citations raises fabrication sharply in post-trained checkpoints and not in base ones: a 47.8-point interaction on twelve checkpoints (Holm-adjusted p = 2e-34) and 41.5 points on fifteen, in all three domains. A length-matched control separates the citation cue from a demand for a longer answer, so the effect is specific to citations, not verbosity. Post-training also raises fabrication overall, from 4.8% to 56.7%, but our registered prediction that it would rise most where fabrication is most tempting did not hold. A preference model trained only on surface citation features prefers post-trained output 86% of the time, and holding citation count fixed shows it rewards quantity. Our answer: possibly, but not proven. Post-trained models produce fabricated citations at far higher rates when asked for sources, and a naive evaluator that counts sources without checking them would prefer their output for citing more. But the targeted pattern we registered did not appear, and plain instruction-following could explain the same results. Proving that the reward causes fabrication needs an experiment that changes the reward during training, which this study does not do. Pre-registration: doi:10.17605/OSF.IO/S53HY. Code and data: https://github.com/zainnab-sparq/citation-reward-hacking

### NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale
- arXiv 2611.02102 · v1 2026-11-01 00:00 UTC · 
- Authors: Chaoyun Zhang, Bingxuan Li, Pinxue Guo, Yangfan Gao et al.
- Topics: Agents · score 8 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.02102

> Scaling computer-use agents from individual actions to complex software work requires experience that connects decisions to complete outcomes. We present NorthCUA, an integrated system for turbocharging computer-use agents through experience at scale. Its Experience Flywheel supplies diverse executable tasks to the NorthCUA Harness, which sustains long interactions, records decisions, and checks task outcomes. The Flywheel uses these records to curate verified trajectories. For unsolved tasks, recursive self-improvement evolves reusable skills and preserves verified milestones so later attempts build on earlier progress. Staged Learning combines this experience with grounding data from the Flywheel to develop GUI competence through mid-training and long-horizon supervised fine-tuning. The policy then learns from fresh attempts in the same Harness through joint desktop-web reinforcement learning, closing the loop between experience production and policy improvement. The resulting Nano, Mini, and Pro family achieves state-of-the-art results among open-source models across GUI grounding, desktop execution, and Web interaction under the reported evaluation settings. For more responsive Web workflows, NorthCUA-Ultrafast pairs direct action selection with open-ended generation on pre-RL Nano, offering a measured quality-latency tradeoff. Together, these advances establish NorthCUA as a high-performing model family and a reusable foundation for agents that carry complex software work from intent to completion.

### Don't Guess, Ask Wisely: Benchmarking and Training Proactive Elicitation in Open-Domain LLM Conversations
- arXiv 2611.01878v1 · v1 2026-11-01 13:15 UTC · cs.CL
- Authors: Rongyu Zhang, Mutian Bao, Jinjian Zhang, Yuetian Du et al.
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.01878
- arXiv comment: 26 pages, 6 figures; EMNLP 2026 oral
- Full text: data/fulltext/2611.01878.txt

> When user queries are incomplete, large language models should ask targeted questions before committing to an answer, a capability we call proactive elicitation, yet evaluation on real user-assistant queries across seven LLMs (8B to frontier) shows that fewer than 11% of underspecified queries trigger a follow-up question. To benchmark and train this capability, we introduce VagueBench, where each seed query is annotated with structured intent and detail units then degraded into intent-vague and fully-vague variants via controlled removal of linguistic cues, yielding known hidden information sets for evaluating both when and what to ask. We propose DialogGRPO, an offline reinforcement learning method that organizes multi-turn elicitation as a dialogue-state directed acyclic graph, where candidate questions at each node receive dense turn-level rewards combining immediate information gain with lookahead value through group-relative comparison, enabling fine-grained credit assignment without runtime simulation. DialogGRPO elicits missing information on over 88% of vague queries with substantial gains in both recovery efficiency and answer coverage, without over-asking on complete queries, outperforms prompting and test-time-scaling baselines, and generalizes zero-shot to MultiWOZ 2.4 and AmbigQA.

### Interface Quilt: Modifying Applications with Computer Use Agents and Generative UI
- arXiv 2611.01891v1 · v1 2026-11-01 13:34 UTC · cs.HC
- Authors: Leping Qiu, Jo Vermeulen, Tim Zindulka, George Fitzmaurice et al.
- Topics: Agents · score 8 · found via cs.HC
- Link: https://arxiv.org/abs/2611.01891
- arXiv comment: Preprint, under review

> Modifying an existing application is difficult when it does not provide programmatic access for that change. Recent advances in computer-use agents (CUAs) enable richer understanding and operation of existing interfaces, while generative UI (GenUI) makes it practical to generate new ones. We examine how these advances expand software modification through a design space of what can be changed and a framework for how modifications can be implemented. We then introduce Interface Quilt, a system that combines CUAs and GenUI to generate interface patches, which are new interfaces displayed over an existing application to modify its presentation, interaction, and capabilities. Through demonstrations across a variety of applications, we show that interface patches support a range of modifications without source code, APIs, or accessibility data.

### One String to Rule Them All: Measuring Consent Under the IAB Global Privacy Platform
- arXiv 2611.02014v1 · v1 2026-11-01 15:56 UTC · cs.CR
- Authors: Muhammad Abu Bakar Aziz, Christo Wilson
- Topics: Crawl, Ads · score 8 · found via cs.CR
- Link: https://arxiv.org/abs/2611.02014
- arXiv comment: 11 pages, 8 figures, 3 tables

> Many privacy regulations, including the California Consumer Privacy Act (CCPA), require websites to honor users' opt-out choices. To facilitate this process, industry has introduced technical standards such as the IAB Global Privacy Platform (GPP), which aims to standardize collection and transmission of user consent information across multiple jurisdictions. However, it remains unclear whether these standards consistently and correctly transmit user opt-out choices, or whether opt-out choices are respected by advertisers. In this study, we conduct an in-depth analysis of consent propagation under the GPP framework. We collect data from four web crawls across four experimental settings to analyze how widely the standard is adopted, the extent to which opt-out signals propagate from publishers to third parties, and whether these signals reach and alter third-party advertiser behavior. Our analysis reveals several inconsistencies in the implementation and adoption of the standard that result in user consent signals being lost and user opt-out choices not being respected by the advertisers.

### RecGroupMemory: Feedback-Aware Cohort Memory for E-Commerce Recommendation
- arXiv 2611.02453v1 · v1 2026-11-02 03:16 UTC · cs.AI
- Authors: Wendong Zhang, Weipeng Huang, Zhixin Ma, Bin Zhang et al.
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.02453
- Full text: data/fulltext/2611.02453.txt

> Cohort memory can support LLM-based recommendation planning through group-level user profiles and advice. As outcome feedback becomes available, this guidance may need to be updated while preserving the underlying observations. We present RecGroupMemory, a workflow that provides this memory to an orchestration LLM and separates memory construction from feedback-based revision. It uses feedback from the previous day to revise decision guidance, while validation checks keep selected source values unchanged. Online comparisons were conducted among Taobao users with low purchasing power selected by the business team. Relative to a no-memory baseline, memory without feedback and memory with feedback showed increases of 1.58% and 1.78%, respectively, in the number of guided transaction users.

### ICJ-Graph: A Citation Graph and a Layered Document Corpus of the International Court of Justice
- arXiv 2611.02630v1 · v1 2026-11-02 06:55 UTC · cs.CL
- Authors: Jirameth Wannasiwaporn, Pawitsapak Akarajaradwong, Chompakorn Chaksangchaichot
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.02630
- Full text: data/fulltext/2611.02630.txt

> We present ICJ-Graph, a machine-readable resource connecting documents of the International Court of Justice (ICJ) to cited cases, legal provisions and United Nations resolutions. Court decisions, written pleadings and oral records form distinct document layers, preserving the distinction between the Court's reasoning and the parties' submissions. The collection contains 6,396 ICJ documents and 505 documents from other courts and legal bodies, together with 12,375 provisions and 20,291 UN resolutions. The data files contain text, metadata and embeddings. The accompanying pipeline lets users load the graph and generate embeddings for use in their own retrieval systems. To illustrate the resource's use, we evaluate five models on citation prediction for 199 decisions using documents available before each decision. Tools designed for citation research improve citation-prediction F1 over answering without tools for all five models across case, provision and resolution citations.

### E-GenRM: Generative Reward Modeling for Open-Ended E-Commerce Shopping Agents
- arXiv 2611.03008v1 · v1 2026-11-02 12:10 UTC · cs.IR
- Authors: Ying Sun, Qiuyu Zhao, Xiao Wang, Xiyu Zhao et al.
- Topics: Brand/product recommendation · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.03008
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> We present E-GenRM (E-commerce Generative Reward Model), a generative reward model tailored to e-commerce shopping agents. User expectations are shifting from simple product queries to open-ended shopping tasks. However, existing trajectories and reward designs remain largely bounded by current agent usage patterns and known failures, providing limited guidance for further capability improvement. These limitations call for an integrated reward modeling framework for open-ended shopping agent tasks. On the data side, E-GenRM leverages naturally occurring user behavior across the shopping app to construct diverse, long-horizon conversational trajectories beyond established usage patterns. On the modeling side, E-GenRM first learns from behavior-grounded evaluation chains through supervised fine-tuning. It is then optimized through criterion-guided reinforcement learning, which rewards correct preference judgments and evidence-supported factual claims under each criterion. Personalized hard-negative training further improves its sensitivity to user preferences reflected in shopping behavior, beyond explicit requirements. We additionally develop an active evidence retrieval extension that acquires missing e-commerce information for evaluation. On E-GenRM-Bench, E-GenRM-27B achieves 87.40\% preference accuracy, outperforming the strongest baseline by 6.97 percentage points. In a 14-day online A/B test on Taobao, a shopping agent post-trained with E-GenRM improves the effective shopping-assistance rate by 1.39 percentage points and user satisfaction by 2.33 percentage points.

### From Local Skills to Long-Horizon Web Tasks: Progressive Skill Exploration for LLM Web Agents
- arXiv 2611.03116v1 · v1 2026-11-02 13:32 UTC · cs.AI
- Authors: Xueyang Feng, Xiaohe Bo, Xu Chen, Quanyu Dai et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.03116
- arXiv comment: 31 pages, 9 figures. Accepted at NeurIPS 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Large language models (LLMs) are driving autonomous agents toward real-world environments, with the Web emerging as one of the most representative interaction scenarios. However, training Web agents with naive exploration remains challenging: successful trajectories are rare, and the sparse terminal rewards make it difficult for agents to obtain useful feedback from failed trajectories. Inspired by skill acquisition theory, we propose Skill-Composed Progressive Exploration (SCOPE), a short-to-long learning framework for long-horizon Web agents that decomposes complex task exploration into a gradual expansion process from local skills to complete task-solving capability. Specifically, SCOPE iteratively explores around local skills: Skill Discovery extracts reusable local skills and failure experiences from historical rollouts; Skill Orchestration composes discovered skills into high-level skill chains; and Skill Expansion leverages failure experiences aligned with the current skill chain to guide the agent toward exploring new subskills. Through this process, SCOPE progressively constructs task-completing skill chains across rollouts and internalizes them into the policy parameters through agentic on-policy distillation. Extensive experiments on WebArena, WebVoyager, and WebShop show that SCOPE consistently improves exploration dynamics and achieves 3.9% to 18.6% relative gains over the strongest baselines in each setting.

### CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements
- arXiv 2611.03126v1 · v1 2026-11-02 13:41 UTC · cs.AI
- Authors: Xinlei Yu, Gen Li, Ji Zhao, Zhangquan Chen et al.
- Topics: Agents · score 8 · found via HF daily papers, cs.AI
- Link: https://arxiv.org/abs/2611.03126
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Despite recent advances in CUAs, their development remains constrained by the limited diversity, controllability, and reliability of interaction data. Moreover, conventional optimization pipelines lack iterative feedback, while existing recursive improvement approaches often rely on self-generated experiences, limiting ability expansion and yielding diminishing returns. To address these challenges, we introduce CUA-Master, a nested double-loop recursive improvement framework. At the system level, an outer world-data-model flywheel continuously incorporates open-world corpus and leverages evolving model weaknesses to guide subsequent data construction and optimization iterations. At the data level, an inner flywheel couples open-world seeding and autocatalytic propagation. The former mines authentic workflows as seed tasks from instructional videos, and employs visual-semantic dual-path trajectory reconstruction; The latter transforms these seeds into reusable primitives for controllable synthesis of diverse, complex, and verifiable tasks. To enable efficient and reliable trajectory collection, we further introduce a feedback-guided snapshot-rollback retry mechanism in various real environments. Extensive experiments demonstrate that CUA-Master-27B achieves competitive performance across GUI-only and GUI-CLI hybrid benchmarks, scoring 80.2 on OSWorld Verified, 36.9 on OSWorld 2.0, 43.9 on WeaveBench, and 25.0 on Agents' Last Exam. Our framework also substantially improves the quality and efficiency of data synthesis, and exhibits continuous gains across recursive iterations.

### ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents
- arXiv 2611.03238v1 · v1 2026-11-02 14:50 UTC · cs.AI
- Authors: Daiqiang Li, Jingyi Peng, Rui Hu, Jia Li et al.
- Topics: Agents · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.03238
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches between documented and deployed software versions and differences in scope between documentation coverage and task requirements. We introduce ScienceCUA, a two-stage framework combining resource-to-skill construction with execution-guided skill evolution. First, ScienceCUA identifies tasks supported by the software from its documentation, infers operational trajectories, and generalizes them into reusable Skills. Command catalogs, syntax constraints, and shortcuts are organized separately as References for on-demand lookup. Then, ScienceCUA uses execution feedback to drive skill self-evolution by contrasting successful and failed trajectories for the same task, identifying deficiencies, revising existing skills or adding new ones, and updating the skill library only after repeated validation in real environments. To enable reliable evaluation without benchmark noise or task leakage, we introduce two improved benchmarks. ScienceBoard-Verified provides an audited and corrected basis for measuring task performance, while ScienceBoard-VE separates skill evolution from final testing through disjoint evolution and test tasks and further supports native-agent evaluation. Experiments show that the initial Skills and References improve average task success rate by up to 7.23 percentage points over the base model, while skill self-evolution increases the total gain over the baseline to as much as 17.12 percentage points. ScienceCUA turns software documentation into an evolving set of executable skills and queryable references, offering a practical way for general-purpose agents to use scientific software reliably and at scale.

## More new topic matches, lower score, title only (41)
- IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning — https://arxiv.org/abs/2611.03431 (score 8; RAG (generic), Manipulation)
- WebHarbor: Docking Real Websites for Evolving GUI Agent Environments — https://arxiv.org/abs/2611.03634 (score 8; Agents)
- PACT: Defending Recommendation against Promotional News Rewriting via Attack-Diverse Score Consistency — https://arxiv.org/abs/2611.00972 (score 7; Brand/product recommendation, Manipulation)
- Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction — https://arxiv.org/abs/2611.01087 (score 7; Citation & source selection, Manipulation)
- Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning — https://arxiv.org/abs/2611.01411 (score 7; Clicks & measurement, Ads)
- TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents — https://arxiv.org/abs/2610.41216 (score 6; Manipulation)
- Early Stopping in Large Reasoning Models: A Survey and Empirical Audit of Efficiency and Reliability — https://arxiv.org/abs/2611.00166 (score 6; Clicks & measurement)
- AuroraWorld: Structured 4D World Modeling for Exo-to-Ego Video Generation in Robot Manipulation — https://arxiv.org/abs/2611.00177 (score 6; Manipulation)
- RE-SciVQA: Improving Scientific VQA With Context-Relevant Retrieval and Lightweight MLLM Adaptation — https://arxiv.org/abs/2611.00242 (score 6; RAG (generic), Query fan-out)
- Queering the Audits: Community-Based Auditing of AI Harms to Queer Communities — https://arxiv.org/abs/2611.00345 (score 6; Clicks & measurement)
- Price is Only the Symptom: Understanding and Analyzing Economic-State Manipulation Vulnerabilities in DeFi — https://arxiv.org/abs/2611.00587 (score 6; Manipulation)
- Conversational Interaction for LLM-Based Clinical Text-to-SQL: A User Study with Healthcare Professionals — https://arxiv.org/abs/2611.00605 (score 6; Clicks & measurement)
- Reading Between the Chapters: A Graph-Free RAG Rebuilt With AI and Human Feedback — https://arxiv.org/abs/2611.00752 (score 6; Citation & source selection, RAG (generic))
- Numerical Embeddings for CTR Prediction: A Taxonomy, Unified Benchmark, and Open-Source FuxiCTR Extension — https://arxiv.org/abs/2611.01090 (score 6; Clicks & measurement)
- Pop Goes the Verifier: Phoneme-Targeted Data Poisoning of Voice Liveness Detection — https://arxiv.org/abs/2611.01095 (score 6; Manipulation)
- Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation — https://arxiv.org/abs/2611.01112 (score 6; Manipulation)
- MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents — https://arxiv.org/abs/2611.01700 (score 6; Manipulation)
- Reddit Community Signals as a Supplementary Domain-Reputation Feature in Spam Classification: A Conservative Controlled Evaluation — https://arxiv.org/abs/2611.01813 (score 6; Manipulation)
- EAGR: Evidence-Guided Adaptive Graph Retrieval — https://arxiv.org/abs/2611.01910 (score 6; RAG (generic), Query fan-out)
- Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security — https://arxiv.org/abs/2611.01976 (score 6; Manipulation)
- Testing concept-level audits of melanoma classifiers with diffusion counterfactuals and matched positive controls — https://arxiv.org/abs/2611.02119 (score 6; Clicks & measurement)
- Conditional Calibration Contracts under Coupled Load: A Branch-Aware Audit of Switched Inference — https://arxiv.org/abs/2611.02121 (score 6; Clicks & measurement)
- Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting — https://arxiv.org/abs/2611.02310 (score 6; Manipulation)
- From Language to Country to Valence: A Multilingual Audit of Stereotype Bias Across LLMs — https://arxiv.org/abs/2611.02585 (score 6; Clicks & measurement)
- SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search — https://arxiv.org/abs/2611.02643 (score 6; Manipulation)
- The Customer Never Sees the Goal: Measuring and Detecting Vulnerability-Targeted Manipulation in LLM Assistants — https://arxiv.org/abs/2611.02689 (score 6; Manipulation)
- PanoTac: A Dense Three-Axis Tactile Sensor for Robust Touch-Centric Manipulation — https://arxiv.org/abs/2611.03520 (score 6; Manipulation)
- Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations — https://arxiv.org/abs/2611.03647 (score 6; Manipulation)
- Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation — https://arxiv.org/abs/2611.03648 (score 6; Manipulation)
- PatchScout: Thematic Web Data Collection via Information Foraging — https://arxiv.org/abs/2611.00169 (score 4; Agents)
- DuSE-Bench: Benchmarking Joint Reasoning over Evolving Dialogue and Documents — https://arxiv.org/abs/2611.00755 (score 4; Citation & source selection)
- Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights — https://arxiv.org/abs/2611.01280 (score 4; Ads)
- Dynamic Click Destinations: Personalizing Post Ad-Click Landing Experiences — https://arxiv.org/abs/2611.01287 (score 4; Ads)
- EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees — https://arxiv.org/abs/2611.01977 (score 4; Ads)
- Multi-criteria Rating and Review based Recommendation Model — https://arxiv.org/abs/2611.02019 (score 4; Brand/product recommendation)
- WeSearch: A Unified Model-Centric Retrieval Framework for WeChat Search — https://arxiv.org/abs/2611.00530 (score 3; Clicks & measurement)
- HiPaper: A Human-AI Collaborative System for Academic Literature Triage and Scholarly Sensemaking — https://arxiv.org/abs/2611.00762 (score 3; Clicks & measurement)
- CST: Lightweight Risk Triage with Source-Grounded Evidence for Web Discussions — https://arxiv.org/abs/2611.01710 (score 3; Clicks & measurement)
- Adversarial Robustness of Retrieval-Based Fact-Checking: Detecting and Mitigating Evidence Contamination — https://arxiv.org/abs/2611.02139 (score 3; Manipulation)
- ElectroChemLLM: A Multimodal LLM Pipeline for High-Fidelity Electrochemical Informatics — https://arxiv.org/abs/2611.00638 (score 1; RAG (generic))
- Bridging Low-Level Image Fusion and High-Level Semantic Understanding — https://arxiv.org/abs/2611.02896 (score 1; RAG (generic))

## Other new cs.IR papers, title only (24)
- MEMENTO: Learning Context Management for Long Context Processing Agents — https://arxiv.org/abs/2611.00244
- EduExplain: A Benchmark for Explanation-Set Retrieval and Storyboard Construction in Educational Explanation — https://arxiv.org/abs/2611.00802
- Where Beam Search Loses Top-Ranked Items:First-Step Coverage in Generative Recommendation — https://arxiv.org/abs/2611.01072
- Growth of global science: reflections on measurability and scientometric insights — https://arxiv.org/abs/2611.01086
- SIDRec: End-to-End Semantic ID Representation and Modeling for Recommendation — https://arxiv.org/abs/2611.01136
- OntoDoc: Automatically Generating Ontology Resource Descriptions — https://arxiv.org/abs/2611.01276
- Wrong Together: Shared Bias in User Simulation — https://arxiv.org/abs/2611.01354
- "PRISM" Is Not All You Need: Cross-Topic Name Collisions and Scientific Paper Retrieval — https://arxiv.org/abs/2611.01362
- CCD: Context-Calibrated Open-Entity Out-of-Distribution Detection in In-Context Tabular Foundation Models — https://arxiv.org/abs/2611.01489
- Federated Vector Retrieval across Heterogeneous VectorDBs — https://arxiv.org/abs/2611.01514
- LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features — https://arxiv.org/abs/2611.01615
- CREDO: Evidence-Conditioned Credit Assignment for Temporal Reasoning Agents — https://arxiv.org/abs/2611.01643
- IncVNM: An Interactive Recommender System with Incremental von Neumann-Morgenstern Utility Learning — https://arxiv.org/abs/2611.01786
- Multicriteria Recommendation System by Leveraging Predefined, Implicit, and Undefined Criteria — https://arxiv.org/abs/2611.02040
- Nonreciprocal Spherical Attention and Retrieval: Sharp Coarsening Clocks and Certified Score Correction — https://arxiv.org/abs/2611.02237
- Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration — https://arxiv.org/abs/2611.02457
- RecRSI: Mechanism-Guided Discovery of Recommendation Algorithms — https://arxiv.org/abs/2611.02487
- PlagiaCorpus: A Bilingual, Adversarial, and Cross-Lingual Dataset for Forensic Plagiarism Detection — https://arxiv.org/abs/2611.02940
- PACERec: Progressive Adaptation of LLM Item Embeddings with Collaborative Evidence for Recommendation — https://arxiv.org/abs/2611.03068
- Preprocessing Choices in Fine-Tuning Data Matter: Utility and Demographic Sensitivity in LLM-Based Recommendation — https://arxiv.org/abs/2611.03113
- Every Clause Counts: Instruction-Following Reranking by Multiplying Small, Answerable Questions — https://arxiv.org/abs/2611.03179
- Dhārā Bench: An Evidence-Oriented Retrieval Benchmark for Indian Knowledge Systems — https://arxiv.org/abs/2611.03196
- Diverse-Teacher On-Policy Distillation for Generative Recommendation — https://arxiv.org/abs/2611.03272
- From FAIR to AI-FAIR Metadata-First Infrastructure for AI-Enabled Science — https://arxiv.org/abs/2611.03327

## Already listed on an earlier day, still inside the look-back window (28)
- Search When Needed, Proceed When Reliable: Metacognitive Reliability Supervision for Efficient Agentic Search — https://arxiv.org/abs/2610.41738 (score 13)
- DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers — https://arxiv.org/abs/2610.37826 (score 12)
- AgentShield: Fortifying Web Applications Against AI Agents and Agentic Browsers — https://arxiv.org/abs/2610.41181 (score 11)
- AI evaluators favor job applications written by certain AI models, independent of candidate quality — https://arxiv.org/abs/2610.41866 (score 10)
- BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed? — https://arxiv.org/abs/2610.41435 (score 9)
- Language Models Show a "Women-Are-Wonderful" Effect in Blame Attribution That is Not Just Leniency — https://arxiv.org/abs/2610.41116 (score 8)
- ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents — https://arxiv.org/abs/2610.41272 (score 8)
- Cross-Interface Authorization for AI Computer-Use Agents — https://arxiv.org/abs/2610.41397 (score 8)
- Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents — https://arxiv.org/abs/2610.41432 (score 8)
- Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products — https://arxiv.org/abs/2610.42032 (score 8)
- Real Computation or Merely Naming? A Pre-Registered Mechanism Audit of 25 Cognitive-Architecture Modules in an LLM-Based Agent System — https://arxiv.org/abs/2610.41604 (score 6)
- When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity — https://arxiv.org/abs/2610.41970 (score 6)
- SecPO: Principled Adversarial Training for Prompt Injection Security — https://arxiv.org/abs/2610.41998 (score 6)
- Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses — https://arxiv.org/abs/2610.41172 (score 5)
- ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science — https://arxiv.org/abs/2610.41396 (score 5)
- Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents — https://arxiv.org/abs/2610.41905 (score 5)
- Pix2Evidence: A Multimodal RAG System for Text and Visual Evidence — https://arxiv.org/abs/2610.41335 (score 2)
- Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning — https://arxiv.org/abs/2610.41390 (score 1)
