# Paper candidates — 2026-11-11 (IST)

Generated 2026-11-11 08:16 UTC. NEW = first seen by the fetcher in the last 18 h (both morning runs).
Totals: 18 new topic matches · 11 other new cs.IR · 78 seen in earlier runs.
Abstracts are copied from arXiv. Full text (where saved) is in the repo at the path shown.

## New papers matching your topics (18), highest score first

### Can AI be a 'Researcher Without Borders'? Auditing Bias in AI-Assisted Social Science Research about China and the US
- arXiv 2611.14288v1 · v1 2026-11-10 16:28 UTC · cs.CY
- Authors: Yuan Zhang, Thales Bertaglia, Ralph Schroeder
- Topics: GEO/AEO, Citation & source selection · score 9 · found via cs.CY
- Link: https://arxiv.org/abs/2611.14288
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> Although large language models have demonstrated strong performance on algorithmic and mathematical tasks, their suitability as social science research assistants remains unclear, particularly because many social science questions lack agreed-upon, quantifiable benchmark answers. Evaluating this suitability is important since researchers and students increasingly rely on AI to generate research ideas. When questions concern the countries in which models were developed, bias may be exacerbated: Do AI models favour the countries where they were developed or the social theories associated with those countries' scholarly traditions? Such biases could distort research findings, undermine scientific credibility, and distort findings when they are disseminated to the public. To investigate whether models exhibit country-focused bias in social science research, we designed a benchmarking task requiring AI to write short essays on social science questions in relation to the US and China as well as some broader social science questions. We varied three conditions: question type (cross-country comparisons, country-specific questions, and general questions); model (two US-developed, two China-developed, and one Europe-developed model); and prompting modality (a base essay-writing request, a researcher identity, a US researcher identity, and a Chinese researcher identity). Responses were manually annotated for bias and source use by two researchers with experience in social science in relation to China and the US. Our analyses show that, on the whole, US and Chinese models and the European one are not politically biased but differ in the sources they cite. Still, some comparative questions favour one country over another, and this tendency is more pronounced for certain questions. These findings suggest that researchers and students should exercise caution when using AI for social science research.

### TIB: Sample-wise Tempered Information Bottleneck for Multimodal Attribution beyond Alignment Assumption
- arXiv 2611.12997v1 · v1 2026-11-08 14:06 UTC · cs.CV, cs.AI, cs.MM
- Authors: Qiming Huang, Peixi Liu, Jianbo Jiao
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.12997
- arXiv comment: Accpeted to NeurIPS2026
- Full text: data/fulltext/2611.12997.txt

> Multimodal (e.g. vision-language, in this work) attribution aims to interpret the models without access to ground-truth explanatory supervision. Existing multimodal attribution methods typically rely on paired modalities as proxy supervision, implicitly assuming that image-text pairs are semantically aligned. Information bottleneck (IB)-based attribution methods follow this general paradigm and instantiate it through a global sufficiency-compression objective. In realistic multimodal datasets, however, this assumption is frequently violated due to partial semantic misalignment and unreliable cross-modal correspondences. Through theoretical analysis, we show that, under such misalignment, information-bottleneck-based attribution objectives exhibit a structural limitation: by assuming equal reliability across all proxy supervision signals, they induce posterior over-contraction and forced explanations. To address this issue, we propose TIB, a sample-wise Tempered Information Bottleneck framework that adaptively modulates attribution strength according to cross-modal reliability, without assuming semantic alignment. Extensive experiments on controlled benchmarks and large-scale datasets show the effectiveness of the proposed approach, while also validating the identified failure mode.

### Elicitation of the parameters of a multi-criteria sorting model
- arXiv 2611.13062v1 · v1 2026-11-09 17:49 UTC · cs.AI, cs.GT
- Authors: Eda Ersek Uyanik
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.13062
- arXiv comment: PhD Thesis defended at University of Mons, Belgium, July 07 2023. 216 pages https://hdl.handle.net/20.500.12907/57144
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Multiple-criteria decision aiding (MCDA) proposes models and methods for different types of decision problems such as choice, ranking or sorting. Such models involve various parameters that must be elicited. In the elicitation process, all necessary information has to be taken from the decision-maker. For this, several direct and indirect elicitation methods are suggested in the literature. In this work, we concentrate on direct elicitation: we aim at providing a rigorous elicitation procedure for the parameters of the Non-Compensatory Sorting model (NCS), which has been characterized by an axiomatic analysis. A basic version of the NCS model is considered, i.e., a model with two categories and no vetoes. The parameters are the set of sufficient coalitions of criteria and the profile separating the two categories. Regarding the sufficient coalitions, we propose several questioning algorithms that engraft questions on classical graph exploration algorithms such as depth-first search. Such algorithms are implemented and evaluated by simulation. For eliciting the limit profile, we design a questioning algorithm using dichotomy. Questioning algorithms can be optimal in the worst case or on average. An optimal algorithm in the worst case has been proposed by Hansel in the framework of monotone Boolean functions. We implement and evaluate this algorithm as a variant of the depth-first search approaches. Regarding optimal questioning strategies on average, we evaluate decision trees for up to four criteria. On the other hand, we assess how more general is NCS as compared to MR-Sort, a particular case of the NCS model in which sufficient coalitions can be represented by additive weights.

### Structured Kernel Surrogate Models for Multimodal Attribution
- arXiv 2611.13198v1 · v1 2026-11-09 20:21 UTC · cs.LG, cs.AI, cs.CV
- Authors: Ziniu Zhang, Zhenshuo Zhang, Jianglin Lu, Ruoxuan Xiong et al.
- Topics: Citation & source selection · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.13198
- arXiv comment: 20 pages. To appear at NeurIPS 2026
- Full text: data/fulltext/2611.13198.txt

> We study the problem of cross-sample modality attribution, which involves measuring how one modality in one sample affects the learning outcome in other multimodal samples. This problem is crucial in a multimodal system because a data modality (such as a text description) may be redundant for one sample (a self-explanatory image), but the same data modality would otherwise be uniquely informative for another sample, or informative when combined with other modalities. Prior work focuses on influence estimation at the level of one sample, and it remains an open question how one should capture the interactions across both samples and modalities. To capture scenarios like the above, we propose structured kernel surrogate models, which are surrogate mappings from both samples and modalities to the prediction outcome when they are trained together. We design an algorithm, SKS, which applies kernel ridge regression with a structured, compositional kernel on the selection states of individual samples and modalities. Specifically, the kernel function multiplies kernel-based similarity scores between every pair of data modalities for one sample and a pair of two samples. Additionally, we design a gradient-based estimation algorithm to efficiently estimate the structured kernel surrogate model. We evaluate our approach on two multimodal benchmarks, spanning a range of data modalities including satellite images, road networks, text, audio, and tabular data. We find that SKS achieves $57.8$% higher correlation with the true prediction outcomes than existing methods. In downstream data selection, SKS improves the average accuracy by $1.93$% over baselines. Models with data selected by SKS have lower Hessian traces, indicating a flatter loss surface. Using SKS to select satellite images identifies road segments, where accident scenes commonly occur, as opposed to background images.

### Benchmarking Vendor-Guided Optimizations on Edge NPUs: From NPU Only to End-to-End Performance. Extended technical report
- arXiv 2611.13563v1 · v1 2026-11-10 04:31 UTC · cs.AI
- Authors: Youngjin Jo, Jihwan Kim, Minseok Choi, Kwanghoon Choi et al.
- Topics: Brand/product recommendation · score 8 · found via cs.AI
- Link: https://arxiv.org/abs/2611.13563
- Full text: data/fulltext/2611.13563.txt

> Edge NPU performance depends not only on hardware capabilities, but also on model transformation and the overall deployment pipeline. We propose a benchmarking methodology that separates these effects by comparing three configurations: Baseline, Vendor Guided NPU Only (VG-NPU), and Vendor Guided End-to-End (VG-E2E), where VG-NPU preserves common model I/O and host-side processing while VG-E2E follows the vendor-native deployment pipeline. We apply this methodology to four edge NPUs and three vision workloads. VG-NPU improves both accuracy and Runtime-call latency in 10 of 12 NPU--workload combinations, whereas VG-E2E reduces System-level latency in all combinations but improves accuracy in only four. Moreover, NPU-level performance rankings do not always match End-to-End rankings, and VG-E2E provides an additional 10.4--70.7\% reduction in System-level latency over VG-NPU. These results demonstrate the importance of evaluating vendor-guided optimization separately at the controlled model-transformation and full deployment levels when comparing heterogeneous commercial Edge NPU platforms in practice.

### An Interpretable Stylometric Framework for Early Chinese Buddhist Translator Styles: A Case Study on the Attribution of Disputed Works of An Shigao
- arXiv 2611.13636v1 · v1 2026-11-10 06:22 UTC · cs.CL
- Authors: Yating Pan, Xinyue Zhang, Jun Wang
- Topics: Citation & source selection · score 8 · found via cs.CL
- Link: https://arxiv.org/abs/2611.13636
- arXiv comment: Presented as a long paper at Digital Humanities 2026 (DH2026) in Daejeon, Republic of Korea. The abstract appears DH2026 Book of Abstracts, pp. 545-549, available at https://doi.org/10.5281/zenodo.22656106
- Full text: not stored: license is by-nc-nd, which does not allow redistribution; read it on arXiv

> Attributing early Chinese Buddhist translations requires evidence that scholars can trace back to the texts. We develop an interpretable stylometric framework that uses features defined or reviewed by Buddhist philologists, including function characters, sentence formulas, sentence-final characters, sentence length, and part-of-speech n-grams. We construct stylistic profiles from 31 authenticated translations by seven translators from the Eastern Han through the Western Jin, then compare eight disputed texts with An Shigao's profile. Two texts, T1557 and T0101, show the strongest stylistic similarity to the authenticated An Shigao corpus, with scores of 0.783 and 0.687, respectively. The attributions agree with those reported by a published BERT-based approach on the same set of disputed texts. The framework requires no task-specific training and allows scholars to inspect which linguistic features support each proposed attribution.

### Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce Scale
- arXiv 2611.13797v1 · v1 2026-11-10 09:32 UTC · cs.IR
- Authors: M. Emin Dogan, Cansu Er, Aysenur Kulunk, M. Furkan Eseoglu et al.
- Topics: Brand/product recommendation · score 8 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13797
- arXiv comment: 3 pages, IEEE Big Data 2026, Poster
- Full text: not stored: license is by-nc-sa, which does not allow redistribution; read it on arXiv

> We study hard-label distillation from Gemini 3.1 Flash-Lite to compact encoders on 5.34 million Turkish marketplace reviews. A strict new-SKU temporal test measures teacher fidelity; a separate, teacher-label-blind audit by one company annotator measures editorial agreement. An H3 category prefix slightly improves teacher fidelity on the full new-SKU test. On the 16,000-review chronological audit subset, it instead reduces agreement with both Gemini and the annotator, with a clearer paired difference for CORN than for cross entropy. Thus the context effect depends on the evaluation population, and teacher fidelity alone does not establish editorial alignment. Under the measured offline configurations, a single-L4 student pipeline processes reviews 50.2 times faster than the teacher pipeline.

### FAIDER: Fairness-Aware Item-Level Decoding for Large Language Model Recommenders
- arXiv 2611.10285v2 · v1 2026-11-06 22:31 UTC · cs.AI
- Authors: Ziwei Wu, Jingrui He
- Topics: Brand/product recommendation, Manipulation · score 7 · found via cs.AI
- Link: https://arxiv.org/abs/2611.10285
- Full text: data/fulltext/2611.10285.txt

> Large language model (LLM) recommenders can produce semantically different recommendations when a user's protected attribute changes, even if the interaction history remains fixed. Controlling this disparity is challenging when model weights and full-vocabulary logits are inaccessible. We propose FAIDER (Fairness-Aware Item-level DEcoding for Recommendation), which incorporates fairness into list construction by selecting complete item candidates rather than manipulating token-level logits or repeatedly repairing finished outputs. The central idea is to separate the operational criterion for a violation from how strongly generation is constrained. Conformal-inspired empirical calibration fixes a cross-group semantic-disparity threshold, while online decoding applies either hard filtering or a soft penalty adjusted through dual-inspired feedback to target a prescribed violation rate. Separately, we establish a pathwise guarantee: under a uniform enforceability assumption, the soft decoder's empirical violation rate exceeds its target by at most $O(1/T)$. Experiments across recommendation benchmarks and LLM backbones show that Soft FAIDER improves both measured semantic fairness and ranking quality over the evaluated prompt-repair baselines. It also generally achieves a more favorable fairness-utility balance than the hard variant, indicating that stricter per-recommendation constraints do not necessarily yield lower measured disparity.

### World In-Context Learning for Agentic Robot Manipulation
- arXiv 2611.12885 · v1 2026-11-09 00:00 UTC · 
- Authors: Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du et al.
- Topics: Manipulation · score 6 · found via HF daily papers
- Link: https://arxiv.org/abs/2611.12885
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in which a frozen model starts from a demonstration, rehearses the task in a world such as a simulator, and writes the feedback into its context rather than its weights. We build RoboScript, a modular infrastructure that implements WICL for agentic manipulation. From a single demonstration, RoboScript learns each task through rehearsal in simulation, freezes the learned knowledge as a Task Memory, and deploys the frozen memory on new scenes with data isolation that ensures every deployment input is available on a real robot. On all 50 tasks of RoboTwin 2.0, RoboScript reaches 83.4% mean success across clean and randomized settings with one demonstration per task and no gradient updates, exceeding the strongest trained action policy by over 20 points. The method generalizes across visual distributions, improves through reflection, scales with the foundation model, and transfers to a physical dual-arm robot through cross-embodiment memory adaptation. With a world in the loop, a robot can learn a manipulation task in its context as well as it learns one in its weights. All code is available at https://github.com/ArcheOne-AI/RoboScript

### The Dose Makes the Poison: Exposure-Aware Evaluation of Generative Drug Design
- arXiv 2611.13398v1 · v1 2026-11-10 00:20 UTC · q-bio.QM, cs.AI, cs.LG
- Authors: Maria Franz, N. Benjamin Erichson
- Topics: Manipulation · score 6 · found via cs.AI
- Link: https://arxiv.org/abs/2611.13398
- arXiv comment: 14 pages, 3 figures. Accepted at the AI4DD workshop (AI for Drug Discovery: Bridging the Translation Gap), NeurIPS 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Generative models are increasingly used to propose molecules for drug discovery. They can produce far more candidates than can be experimentally tested, making computational selection essential. Most selection methods rely on predicted molecular properties, such as potency and toxicity, but overlook how these properties translate into drug exposure at a given dose. As a result, molecules that appear promising on paper may require impractical doses or raise safety concerns. We investigate this gap by using physiologically based pharmacokinetic (PBPK) simulations to re-evaluate molecules selected from three PARP1-targeted generative pipelines. Of 60 shortlisted molecules, seven fail to achieve sufficient target exposure, while 28% of the remaining candidates show predicted safety risks at their required dose. Moreover, 85% of candidates with an achievable dose are outperformed by molecules overlooked during static selection. These findings suggest that accounting for dose and exposure can substantially change which generated molecules are considered promising for drug development.

### What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them
- arXiv 2611.14068v1 · v1 2026-11-10 13:32 UTC · cs.CR, cs.LG
- Authors: James Rice, Ji Hwan Park, Andres Kwasinski
- Topics: Clicks & measurement · score 6 · found via cs.CR
- Link: https://arxiv.org/abs/2611.14068
- arXiv comment: 47 pages. Code at https://github.com/jrice-ai/cage (tag arxiv-v1), data at https://doi.org/10.5281/zenodo.23681828
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the simulator silently discards any action asserted for an agent whose previous action is still running, and charges one point for a discarded Restore as for one that runs. The documented observation does not expose the busy flag. Both reference defenders read it in their own wrappers, and switching that check off at evaluation costs KEEP's released policy 99.58 points per episode and H-MARL's 145.98, in both cases the charge for Restores sent to busy agents, with H-MARL's executed actions unchanged step for step. On a supervisory harness, holding interventions until the agent is idle is worth 25.3 and 27.6 points per episode at the published setting. In training, the check decides how a busy step enters the trajectory. Trained without it, KEEP leads at a hundred updates in all four paired seeds and trails from two hundred on in all four. Continued to two thousand updates on three seeds, the repaired recipe ends inside the released interval on one seed and short on two, by 27 and 125 points, a spread across training seeds far wider than the released reproduction interval. Second, the evaluation seeds the environment but not the policy, so a reported mean is one draw, and 88.9% of per-episode outcome variance is the policy's own sampling draw. Third, recovery precision depends on the truth it is scored against. Across five published comparison tables, none states the artifact, sampling, criterion and adversary that would make its numbers comparable. We release the instrument, our patches to both defenders, the traces and checkpoints behind every number, and a five-item disclosure checklist.

### A Technique to Model Product Information and User Reviews (MPIUR)
- arXiv 2611.13361v1 · v1 2026-11-09 23:36 UTC · cs.AI, cs.IR
- Authors: Emna Belguith, Fajrian Yunus, Talel Abdessalem
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13361
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Modern e-commerce platforms naturally provide three complementary modalities: textual item descriptions, item images, and user reviews. However, existing multimodal recommendation methods often omit reviews or do not integrate all three modalities within a unified framework. In this paper, we propose MPIUR, a multimodal graph-based recommendation model that encodes reviews in heterogeneous graphs, aligns image and text representations, and adapts collaborative--semantic alignment to item interaction density. Experiments on the Amazon Reviews 2023 Musical Instruments and Baby categories show that MPIUR achieves the best global nDCG@10 and Recall@10 among the evaluated methods on both datasets. It also obtains the best nDCG@10 and Recall@10 on sparse items, indicating that jointly exploiting reviews and multimodal item content is particularly useful when interaction histories are limited.

### Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems
- arXiv 2611.13539v1 · v1 2026-11-10 04:02 UTC · cs.IR, cs.LG
- Authors: Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo
- Topics: Brand/product recommendation · score 4 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13539
- Full text: data/fulltext/2611.13539.txt

> Researchers and engineers improve recommendation systems by performing A/B experiments with new model architectures, optimization methods, and data features. However, running full-scale experiments (e.g., full-model training with online data) for every feature change is prohibitively computationally intensive, while the result from a single small-scale experiment is often misleading. To address this challenge, we show that modern recommendation models exhibit feature-invariant scaling: the change of a model's performance follows a predictable scaling-law even when different feature changes are applied to the baseline model. We introduce an efficient method that exploits scaling-laws and uses statistical inference to predict (with confidence intervals) the full-scale effect of an A/B experiment in recommendation systems. This enables practitioners to efficiently filter out neutral or regressive feature changes with only small-scale experimentation. We validate our method on three distinct recommendation model families---Wukong, HSTU, and LLM-based recommendation models---across more than 40 architectural, optimization, and data changes. Our method accurately distinguishes beneficial feature changes from neutral and regressive ones while using only a fraction of the compute required for full-scale evaluation. It also identifies several changes that improve HSTU's state-of-the-art performance on MovieLens-20M. Our results demonstrate that scaling laws can be practically exploited to make compute-efficient decisions for improving industrial-scale recommendation systems.

### INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences
- arXiv 2611.13069v1 · v1 2026-11-09 18:58 UTC · cs.LG, cs.IR
- Authors: Mattias Kvist, Erik Lidman Hillbom, Edoardo de Cal, Davis Siemens et al.
- Topics: Clicks & measurement · score 3 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13069
- arXiv comment: 4 pages + references and appendix. Accepted at the MFMB workshop at ACM ICAIF '26 (non-archival). Code: https://github.com/kthaisociety/intent
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Banks now train foundation models on ordered sequences of customer events such as transactions, app sessions, and authorizations. Deployed, such a model predicts forward in time, often for customers and merchants absent from training, yet each is evaluated on private data, so no two can be compared. Public benchmarks for such sequences rarely test a period the model has not seen; recommendation studies usually hold out each user's last events instead. We present INTENT (INTEraction, Novelty, and Transfer evaluation for next-action prediction), a public benchmark that scores a model in seven cells defined by whether the user, the period, and the target item appeared in training. An audit of 59 public dataset families retains five datasets; the most common defect is the lack of a calendar timestamp that orders events. No date lies within the time span of all five datasets, so each is split at its own cutoff, chosen by one rule fixed before any model is evaluated. Summed over the datasets, every cell holds at least 111,769 users. In reference results the cell determines the best model: a transformer leads on seen items after the cutoff but scores zero on new items, a variant that embeds item metadata helps mainly on MicroLens, and repeating the user's last item leads on new items in four of five datasets. This parameter-free control also shows that on three datasets most of the score lost after the cutoff reflects changed behavior rather than the model. The pipeline, the cutoff rule, and the per-cell user counts are publicly available.

### Activation-Guided Graph Retrieval for Cognitive Memory Reconstruction in Language Model Systems
- arXiv 2611.13127v1 · v1 2026-11-09 19:13 UTC · cs.AI, cs.CL, cs.IR
- Authors: Marvin Danig
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13127
- arXiv comment: Architecture and analysis preprint; no benchmark measurements. Companion research essay and revision notes: https://achiral.ai/research/activation-guided-graph-retrieval
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Retrieval-augmented language model systems generally select context by query-conditioned relevance. We argue that long-lived AI systems require a second operator: activation-conditioned memory availability. We specify an architecture in which request and goal cues seed an authorized memory graph, activation and fan attenuation allocate a bounded traversal frontier, retrieved entities recursively emit cues, and a typed evidence graph is reconstructed before generation. The specification yields five architectural consequences about candidate selection, traversal control, graph regularization, evidence reconstruction, and reinforcement. We derive implementation-level cost estimates and define ablations, failure conditions, and a reproducible evaluation protocol. The central claim is narrowed or falsified if a simpler graph reranker matches full traversal on causal and temporal recovery under equal budgets. This architecture-and-analysis preprint reports no benchmark measurements. If the claim holds, retrieval returns the evidence path that makes a memory available, not only a ranked list.

### Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies
- arXiv 2611.13966v1 · v1 2026-11-10 12:04 UTC · cs.IR, cs.AI
- Authors: Jonas Limniatis, Bennet Schaarmann, Georg Reuber, Robert Stahlbock
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13966
- arXiv comment: Submitted to Knowledge-Based Systems. Code: https://github.com/bschaarmann/TIGA
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this task, but iterative free-form generation remains vulnerable to omitted or hallucinated entities, invalid hierarchical relations, and inconsistent organizational principles. We introduce TIGA (Taxonomy Induction with Tool-Grounded Agents), a knowledge-engineering architecture that formulates taxonomy induction as an iterative decision process over an explicit state and constrained action space. TIGA combines executable taxonomy-editing tools, an memory that records tool calls, rationales, and outcomes, and a runtime-adaptive organizational policy that the agent revises during inference. An optional global reviewer evaluates the constructed taxonomy against the candidate set and the active policy. We evaluate TIGA on four benchmark taxonomies using two LLM backbones and compare it with single-shot and iterative prompting-based baselines. TIGA achieves the strongest structural-quality results in most evaluated configurations, but does not dominate on every precision measure. The gains are accompanied by substantially higher token consumption, API-call volume, and inference time. Ablation results show consistent benefits from the policy and interaction-memory components, whereas the effect of global review depends on the dataset and the available revision budget. These findings characterize tool grounding and runtime policy adaptation as promising but costly mechanisms for improving the controlled construction of structured knowledge representations.

### Data Quality Challenges in Multimodal Tourism Recommender Systems
- arXiv 2611.13972v1 · v1 2026-11-10 12:08 UTC · cs.IR, cs.LG, cs.MM
- Authors: Zehui Wang, Wolfram Höpken, Dietmar Jannach
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.13972
- arXiv comment: 4 pages. Presented at the DaQuaMRec Workshop, co-located with ACM RecSys 2025
- Journal ref: CEUR Workshop Proceedings, Vol. 4188, pp. 20-23, 2026
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Modern recommender systems increasingly consider diverse data modalities to enhance model performance. However, the quality of the underlying multimodal data (e.g. data from social media platforms) has received limited attention so far. Focusing on tourism recommendation, we examine real-world challenges encountered when using datasets from Yelp and Instagram. Issues include noise from fake reviews, hallucinated content from LLMs, modality contradictions, and demographic bias. We outline future directions such as quality-aware fusion, structured and controlled LLM-based content generation to reduce hallucinations, and user group differentiation to improve the robustness and reliability of multimodal recommendation systems.

### From Show Programs to Linked Data
- arXiv 2611.14037v1 · v1 2026-11-10 13:03 UTC · cs.IR
- Authors: Clarisse Bardiot, Bernard Jacquemin, Jacob Hart, George Bruseker et al.
- Topics: RAG (generic) · score 1 · found via cs.IR
- Link: https://arxiv.org/abs/2611.14037
- Journal ref: Information Technology and Libraries, 2026, 45 (3)
- Full text: not stored: license is arxiv-default, which does not allow redistribution; read it on arXiv

> Many heritage institutions hold extensive collections of show programs. Too numerous to be cataloged individually, they remain difficult to access and are still largely undigitized. This paper presents a workflow for transforming such documents into structured, interoperable data by combining vision-language models (VLMs), a custom extension of the Linked Art ontology for the performing arts, and different approaches for automatic semantic data annotation. Using the Festival d'Avignon programs (1947--present), preserved at the Biblioth{è}que nationale de France, as a case study, we demonstrate how VLMs achieve more than 98% text transcription accuracy from heterogeneous heritage document images and how constraining large language model generation through a knowledge graph significantly reduces hallucinations in semantic annotation. We argue that this workflow opens new possibilities for large-scale, interoperable performing arts historiography, including the creation of catalogues raisonn{é}s for performing artists, a form of scholarship common in visual arts but absent in performing arts studies.

## Other new cs.IR papers, title only (11)
- DocFS: File Systems as Agentic Reasoning Environments for Complex Multimodal Document Question Answering — https://arxiv.org/abs/2611.12957
- Beyond the Document: Compiled Context and Governed Agents for Any Work Product — https://arxiv.org/abs/2611.13055
- IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier — https://arxiv.org/abs/2611.13595
- From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations — https://arxiv.org/abs/2611.13914
- LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation — https://arxiv.org/abs/2611.14004
- Ontology-Guided Knowledge Graph Construction and Robust Evidence Retrieval for Indian Knowledge Systems — https://arxiv.org/abs/2611.14050
- From Search to Decision: How Post-Training Shapes Information-Seeking Capabilities in Large Language Models — https://arxiv.org/abs/2611.14149
- SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory — https://arxiv.org/abs/2611.14220
- StaRSE: Compact Russian Sentence Embeddings with a Sign-Coded Static Encoder — https://arxiv.org/abs/2611.14236
- Point-in-Time Encoders for Earnings Calls — https://arxiv.org/abs/2611.14325
- FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking — https://arxiv.org/abs/2611.14477

## Already listed on an earlier day, still inside the look-back window (78)
- Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models — https://arxiv.org/abs/2611.12521 (score 14)
- TS-GEAR: Taobao Shangou GEnerative Ad Retrieval — https://arxiv.org/abs/2611.12180 (score 13)
- CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising? — https://arxiv.org/abs/2611.11955 (score 12)
- On Agentic Manipulation Policies — https://arxiv.org/abs/2611.09892 (score 11)
- Slim Foundation Models for Latency-Critical Recommendation Serving — https://arxiv.org/abs/2611.11013 (score 11)
- PCG-RAG: Progressive Compositional Grounding for Retrieval-Augmented Generation in Complex Web Question Answering — https://arxiv.org/abs/2611.11113 (score 11)
- ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation — https://arxiv.org/abs/2611.11897 (score 11)
- Harness Matters: Measuring and Dissecting Security Resilience in Web Agents — https://arxiv.org/abs/2611.11971 (score 11)
- DeepResearch RewardBench: Evaluating Reward Models for Deep Research Report — https://arxiv.org/abs/2611.10156 (score 10)
- From User Behaviors to Satisfaction Judgments: Reasoning about User Satisfaction with AI Overviews — https://arxiv.org/abs/2611.10715 (score 10)
- StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills — https://arxiv.org/abs/2611.12155 (score 10)
- BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models — https://arxiv.org/abs/2611.09147 (score 9)
- Cutpurse: Decomposing Explanation-Guided Model Extraction on Tabular Data — https://arxiv.org/abs/2611.09375 (score 9)
- Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation — https://arxiv.org/abs/2611.11305 (score 9)
- State Media at Retrieval Time: A Large-Scale Audit of Russian State-Aligned Sources in AI Chatbot Responses — https://arxiv.org/abs/2611.11727 (score 9)
- FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding — https://arxiv.org/abs/2611.09722 (score 8)
- SituRecBench: Evaluating Frontier Models as Situated Recommendation Assistants in 3D Environments — https://arxiv.org/abs/2611.10349 (score 8)
- Hybrid Product Search Without the Copy: Lexical, Semantic and Filtered Retrieval Served Directly from a Data Lake — https://arxiv.org/abs/2611.11031 (score 8)
- ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping — https://arxiv.org/abs/2611.11306 (score 8)
- SkillCODER: Towards Auditing and Attribution of Copyright Infringement in LLM Agent Skills — https://arxiv.org/abs/2611.11308 (score 8)
- Agentic Attribution of Cloud Resource Ownership — https://arxiv.org/abs/2611.11340 (score 8)
- Optimizing Multi-Tier Intermediation in Programmatic Advertising: A DAG-Based Mechanism for Supply Path Optimization — https://arxiv.org/abs/2611.11651 (score 8)
- Feeling Easier, Working Harder: Cognitive Load in AI-Assisted Code Comprehension — https://arxiv.org/abs/2611.12019 (score 8)
- Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems — https://arxiv.org/abs/2611.10843 (score 7)
- PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment — https://arxiv.org/abs/2611.12222 (score 7)
- Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation — https://arxiv.org/abs/2611.01112 (score 6)
- MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory — https://arxiv.org/abs/2611.09721 (score 6)
- Beyond Prompt Attacks: Least-Action Auditing of Concept Erasure — https://arxiv.org/abs/2611.10106 (score 6)
- Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect — https://arxiv.org/abs/2611.10110 (score 6)
- Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation — https://arxiv.org/abs/2611.09864 (score 6)
- When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization — https://arxiv.org/abs/2611.10542 (score 6)
- On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents — https://arxiv.org/abs/2611.11506 (score 6)
- Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation — https://arxiv.org/abs/2611.11554 (score 6)
- Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models — https://arxiv.org/abs/2611.11571 (score 6)
- Continuous modeling of manipulative participation for stance analysis: Online discourse on the 2024 Street Animal Law in Türkiye — https://arxiv.org/abs/2611.11576 (score 6)
- Learning Heterogeneous Tactile Representation for General Dexterous Manipulation — https://arxiv.org/abs/2611.12806 (score 6)
- Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation — https://arxiv.org/abs/2611.11854 (score 6)
- Scaling Adaptive Prompt Injection Attacks with Agent Swarms — https://arxiv.org/abs/2611.11861 (score 6)
- Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation — https://arxiv.org/abs/2611.11981 (score 6)
- SadaqahStories: A Verified English-Arabic Corpus of Charity Stories for Children, with an Audit of Errors in AI-Drafted Religious Narratives — https://arxiv.org/abs/2611.12078 (score 6)
- GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation — https://arxiv.org/abs/2611.12175 (score 6)
- Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation — https://arxiv.org/abs/2611.12409 (score 6)
- A Tool for Anonymized Clinical Knowledge Retrieval and Speaker Interaction Analysis of Healthcare Tele-mentoring Sessions — https://arxiv.org/abs/2611.10922 (score 5)
- Multi-Modal Agricultural Document Understanding at the DAGRI Task — https://arxiv.org/abs/2611.11886 (score 5)
- Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You — https://arxiv.org/abs/2611.12705 (score 5)
- Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal — https://arxiv.org/abs/2611.12725 (score 5)
- Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL — https://arxiv.org/abs/2611.09200 (score 4)
- Edge-Deployable LLMs for Classification and Value-of-Information Ranking of Disaster-Related Tweets — https://arxiv.org/abs/2611.10158 (score 4)
- Beyond Ranking: Are Decision Models Calibrated Relevance Scorers? — https://arxiv.org/abs/2611.11480 (score 4)
- Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion — https://arxiv.org/abs/2611.11010 (score 2)
- Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation for Text Reranking — https://arxiv.org/abs/2611.10405 (score 1)
