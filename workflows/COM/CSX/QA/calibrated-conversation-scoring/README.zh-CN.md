---
id: AWF-0047
name: 校准式对话质检评分
summary: "用分项分类器给客服对话打分并按根因聚类失败案例；人工抽样审核并复核聚类结果。"
deliverable: 已评分的对话集
shape: "拉取对话（人工 + AI 智能体）→ 每个 对话：分项分类器 + 理由 → 合成通过/未通过分数 → (评分 ⟲ 🛑 sample) → 按根因聚类失败案例 → 🛑 review → 修复路由/知识/辅导"
source_hash: ee659dc0b011
---

# 校准式对话质检评分

**与相近工作流的区别：** AWF-0028 锚点校准评分器（Anchor-calibrated grader）给学生作业评分，由教师放行。本工作流的输入是每一段客服对话，产出是运营层面的根因修复，把关方式是抽样审计，而不是教师按批审阅。AWF-0021 流程智能体（Procedure agent）负责解决工单；本工作流负责审计工单。
**工具变体：** `in-house-llm-classifiers` · `instacart-lace` · `amazon-bedrock`

## 步骤

1. 定义一小组二元标准，只从客户一侧的对话记录来判断，忽略内部备注：是否理解了问题、是否有不满情绪、是否已解决或已妥善升级、方案给出后的情绪 [[1]](#sources)。二元标准比 1–10 分的量表更可靠 [[2]](#sources)。
2. 给每段对话评分，不论来自哪个渠道，也不论由人工还是 AI 智能体处理。只有每项标准都通过，这段对话才算通过 [[1]](#sources)。把模型给出的理由和每个分数存在一起 [[2]](#sources)。
3. 🛑 **抽检**：质检专家按同样的标准给选定的一批对话打分，并与模型的分数比较。出现分歧时以人工为准：调整标准的措辞或重新组织标准，然后重复，直到两者一致。每次更新都要重新做这项检查 [[1]](#sources)[[2]](#sources)。
4. 把各项分数合成一个指标。对未通过的对话做聚类，找出新出现的问题，例如 AI 智能体给出错误的政策指引，或案件被错误路由 [[1]](#sources)。
5. 🛑 **审阅**：客服运营负责人拿到聚类后的发现，修复路由或知识库，或对客服人员做辅导。不要仅凭原始分数处分个人 [[1]](#sources)。

**产出：** 带理由的逐段对话评分、汇总的体验指标，以及一份按重要性排序的根因清单，交给运营、知识库和辅导的负责人。
**失败模式 → 防护：** 评判模型偏离人工判断，或混淆相近的标准，一个标准出问题却让多个标准一起失败 → 定期对照专家评分重新校准，并保留理由以便找出主要问题 [[1]](#sources)[[2]](#sources)。综合分数掩盖了变化的来源 → 在报告中把各项标准分开列出。

**近期实践（2026）：**
- 评分 ⟲ 抽检循环：在修改提示词之前，先追查每一处人与 AI 的分歧原因（检索到错误文档、标准措辞含糊、推理有误）；每次政策或模型变更后重新抽样（Revelir，2026-11-03）。[[4]](#sources)
- Booth 测试的发现：AI 对未兑现的承诺更严格，而人工在上下文存在于工单之外时更严格；要对完整的对话线程评分，因为工单在审计日期之后可能还会变化。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Oura, How Oura Uses AI to Measure Customer Experience](https://ouraring.com/blog/how-oura-uses-ai-to-measure-customer-experience/) (2026-08-25)。四个分类器给几乎每次会员互动打分；对照质检专家做了校准；发现推动了路由和政策修复。"repeated troubleshooting has dropped from 40 percent to around 20 percent"。*第一手：是；可信度：高。*
- [Instacart, LACE framework](https://company.instacart.com/tech-innovation/turbocharging-customer-support-chatbot-development-with-llm-based-automated-evaluation) (2025-06-11)。覆盖五个维度的二元标准；人工与 LACE 的结果反复比对，直到一致。"five key dimensions"。*第一手：是；可信度：中。*
- [Jen Spencer / Booth, We Scored Every Support Ticket. Here's What the Audit Missed](https://hirebooth.com/blog/we-scored-support-ticket-heres-what-the-audit-missed) (2026-11-12)。在 20 张工单上，用质检分析师自己的评分表，对比 AI 评分与这位受过培训的分析师的审计。"The automated scoring agreed with the human on 96% of individual checks (192 of 200)."。*第一手：厂商；可信度：中。*
