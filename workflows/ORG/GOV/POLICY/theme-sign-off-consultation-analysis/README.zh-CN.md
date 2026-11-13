---
id: AWF-0080
name: 意见征询主题分析与签核
summary: "从征询意见中归纳主题并归类每条回复；政策团队确认主题清单，分析师核验归类结果。"
deliverable: 意见征询主题分析
shape: "每个问题的回复 → 每个问题：从全部回复中归纳主题 → 🛑 sign-off (政策团队修改主题清单) → 每个回复：归入一个或多个主题 → 🛑 sample (分析师核验归类) → 主题计数与原始回复的看板 → 分析师综合结论 → 🛑 review (政策负责人)"
source_hash: 0399b7db5c94
---

# 意见征询主题分析与签核

**与相近工作流的区别：** AWF-0030 议题树研究（Issue-tree research）产出的是假设驱动的研究简报。本工作流则是依照一份由人签核的主题清单，对固定的公开语料做归类，并由分析师抽检归类结果。产出物和检查点都不同。
**工具变体：** `iai-consult`

## 步骤

1. 把每个征询问题的自由文本回复载入 Consult（i.AI）。它对全部回复（而非抽样）做主题建模，并为每个问题提出一份较长的主题清单 [[1]](#sources)。
2. 🛑 **签发**：负责这次征询的政策团队逐个问题审阅生成的主题清单，在归类开始前可以增加、修改或删除主题 [[1]](#sources)。
3. 由 LLM 把每条回复归入一个或多个已签核的主题 [[1]](#sources)。
4. 🛑 **抽检**：分析师在审阅界面中打开单条回复，勾选或取消主题。在 DWP 的评估中，125 名审阅人每个问题最多核对了 5,000 条回复，其中每个问题有 1,000 条由两人重复审阅，用来衡量两个人之间的一致程度 [[1]](#sources)。在首次正式使用（苏格兰政府）中，专家审阅了每一条回复 [[2]](#sources)。
5. 检查缺失的主题：审阅人可以标记某条回复不属于任何主题，这能暴露签核后的清单是否漏掉了一大类回复 [[1]](#sources)。
6. 政策制定者借助看板（主题频次加原始回复）撰写结论 [[1]](#sources)[[2]](#sources)。
7. 🛑 **审阅**：在分析结果进入政府回应之前，官员始终要审阅主题以及回复的归类方式 [[2]](#sources)。

**产出：** 按问题整理的主题框架，附计数和关联的原始回复，用于撰写公开发布的征询分析和政府回应。
**失败模式 → 防护：** 签核后的主题清单漏掉一大类回复 → 审阅人标记“没有合适的主题”，并重新审视清单。不同回复群体之间存在偏差 → 按自报的残障状况做平等性分析（DWP 的实例中未发现偏差）[[1]](#sources)。过度信任归类结果 → 用两人重复审阅得到的人与人基线（F1 0.710）来对照 Consult（F1 0.816）[[1]](#sources)。

**近期实践（2026）：**
- 第 4 步：在 IWC 的实例中，每条回复的审阅时间中位数为 16 秒，12% 的回复被审阅人添加了“New theme”，说明生成的主题清单并不完备（[i.AI IWC evaluation](https://ai.gov.uk/evaluations/consult-evaluation-independent-water-commission-call-for-evidence/)）。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例补充于 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [i.AI, Consult Evaluation: DWP Pathways to Work](https://assets.publishing.service.gov.uk/media/68f63fe01c9076042263f0bd/evaluation-report.pdf) (2025-08-27)。DWP 的正式征询：125 名审阅人核对了 Consult 的主题归类；并与人与人之间的一致程度作了对比。"The reviewer made no changes to Consult's mapped themes for 73% of responses.". *第一手：是；可信度：高。*
- [GOV.UK, Humphrey AI tool reviews consultation responses](https://www.gov.uk/government/news/government-built-humphrey-ai-tool-reviews-responses-to-consultation-for-first-time-in-bid-to-save-millions) (2025-05-14)。苏格兰政府化妆品征询，2,000 多条回复，六个问题；专家完善了主题并审阅了每一条回复。"an F1 score (a common measure of alignment for AI tools) of 0.76"。*第一手：是；可信度：中。*
- [i.AI, Consult Evaluation: Independent Water Commission Call for Evidence](https://ai.gov.uk/evaluations/consult-evaluation-independent-water-commission-call-for-evidence/) (2025-10)。第三次正式使用；50,000 多条回复；两组审阅人与 Consult 作对比。"for 64%–69% of responses, reviewers made no changes to Consult’s theme suggestions"。*第一手：是；可信度：高。*
- [GOV.UK, Ground-breaking use of AI saves taxpayers’ money](https://www.gov.uk/government/news/ground-breaking-use-of-ai-saves-taxpayers-money-and-delivers-greater-government-efficiency) (2025-10-16)。IWC 实例的成本和专家核查时间。"The AI tool categorised responses into themes in around 2 hours, costing £240 and experts only needed 22 hours to check the results.". *第一手：是；可信度：高。*
