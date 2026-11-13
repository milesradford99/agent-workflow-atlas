---
id: AWF-0104
name: 假设锦标赛
summary: "多个智能体生成、辩论并以锦标赛方式排序研究假设；科学家设定目标、评估并经实验验证。"
deliverable: 排序后的假设
shape: "🛑 plan (科学家陈述研究目标 + 背景论文) → 监督者解析为计划 → 每个 智能体：生成 (辩论) → 反思 (工具、网络搜索) → (锦标赛排序 ⟲ 演化) → 元评审 → 研究综述 + 实验方案 → 🛑 review (科学家评估前 5 名并给出反馈) → 🛑 sign-off (实验室验证)"
source_hash: 70211a2c07a5
---

# 假设锦标赛

**与相近工作流的区别：** 同类中最接近的是 AWF-0009 筛选漏斗（LITREV），它交付系统综述。本工作流通过智能体锦标赛，从文献中产出新的排序假设，由科学家审阅和实验室验证把关，因此产出不同。另与 AWF-0034 化学家把关的 DMTA（HLT/DRUGDISC）相近，后者针对固定靶点做迭代的制备-测试循环，而不是开放式的假设生成。类别归属说明：ANALYSIS 是另一个可选的归属。
**工具变体：** `google-ai-co-scientist-gemini2`

## 步骤

1. 🛑 **计划**：科学家用自然语言陈述研究目标，可附上种子想法和背景论文。Imperial 只提供了噬菌体卫星和关键 cf-PICI 论文的背景，没有提供其尚未发表的结果 [[1]](#sources)[[2]](#sources)。
2. Supervisor 智能体把目标转化为研究计划，并为六个专职智能体排队安排工作：生成、反思、排序、演化、邻近度和元评审 [[1]](#sources)。
3. 生成智能体通过模拟辩论提出假设。反思智能体借助网络搜索等工具对其做出批评。排序智能体运行 Elo 锦标赛，演化智能体改进胜出者，并随算力增加循环迭代 [[1]](#sources)。
4. 输出：排序后的假设、研究综述和实验方案 [[1]](#sources)。
5. 🛑 **审阅**：科学家批判性地评估排名前五的假设，并可用自然语言反馈来引导 [[1]](#sources)[[2]](#sources)。
6. 🛑 **签发**：以湿实验为准；AML 药物重定位候选在细胞系中做了体外测试 [[1]](#sources)。

**产出：** 一组带综述和实验方案的排序假设，供科学家选择实验。
**失败模式 → 防护：** Elo 排名是自评，并非真实标准 → 由专家评估排名靠前的候选，并做实验室验证 [[1]](#sources)。夸大“发现” → cf-PICI 案例重新发现的是一个已知但未发表的结果，仍然需要实验室验证 [[2]](#sources)。

**近期实践（2026）：**
- 计划步骤：在 Imperial 的 cf-PICI 案例中，研究目标只是一份仅含已发表信息的输入文档，因此系统无法看到该实验室未发表的结果（Cell 2025-09-09）。[[3]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Penadés et al., AI mirrors experimental science (bioRxiv)](https://www.biorxiv.org/content/10.1101/2025.02.19.639094v1) (2025-02-19)。Imperial 实验室提出其尚未发表的问题；排名第一的假设与其实验室结果吻合。"cf-PICIs hijack diverse phage tails to expand their host range"（排名第一的假设；科学家评估了前五名）。*第一手：是；可信度：高。*
- [Google Research, AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) (2025-02-19)。AML 药物重定位候选经体外验证；肝纤维化靶点在类器官中测试。"p-values for all suggested drugs are <0.01"。*第一手：是；可信度：中。*
- [Penadés, Gottweis et al., Cell](https://www.cell.com/cell/fulltext/S0092-8674%2825%2900973-0) (2025-09-09)。Imperial 实验室只给 co-scientist 一份输入文档；其排名第一的假设与他们未发表、经实验证实的机制吻合。"The AI co-scientist generated five ranked hypotheses"（最高 Elo 分 1,777）。*第一手：是；可信度：高。*
- [Google DeepMind, Co-Scientist: A multi-agent AI partner](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/) (2026-05-19)。纤维化药物重定位候选在实验室中测试；结果发表于 Advanced Science。"successfully blocked 91% of a scarring-linked response in lab tests"。*第一手：厂商；可信度：中。*
