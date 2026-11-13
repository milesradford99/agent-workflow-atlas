---
id: AWF-0021
name: 流程型客服智能体
summary: "依据知识库和处理流程解决客户对话，交易限额写在代码里；敏感问题转人工，其余由质检抽样。"
deliverable: 已解决的对话
shape: "加载知识库 + 处理流程 → 每条消息：分流 → 咨询：回答 | 交易：身份验证 → 🛑 action (限额写在代码里) → 调用工具 | 敏感问题：🛑 handoff → 🛑 sample (质检) → 知识库缺口聚类 → 新文章"
source_hash: 909eaf666c9f
---

# 流程型客服智能体

## 步骤

1. 把口口相传的经验改写成带有明确条件和限额的自然语言流程。Decagon 的 AOP 会把这些流程编译成工作流，退款和身份核验在代码中执行 [[21]](#sources)。Intercom Fin Procedures 和 Sierra journeys 是同类的变体。
2. 按意图对每条消息分流。
3. 任何账户操作之前先做身份验证。
4. 🛑 **操作**：限额由代码强制执行，而不是写在提示词里。
5. 🛑 **接手**：转人工时附上对话摘要。
6. 🛑 **抽检**：质检对每段对话打分；人工复核被标记的和随机抽取的对话。
7. 把每周的知识库缺口聚类转成新文章。

**指标提示：** 各厂商对解决率的定义并不一致。据报道，Fin 官网声称平均解决率为 76%，而独立测试和小企业测试集中在 38–53% [[22]](#sources)。Decagon 客户超过 70% 的数字来自一份分析师文章 [[21]](#sources)。这些都属于厂商材料（证据 B）。

**近期实践（2026）：**
- 转人工：先设定固定的尝试次数上限（TripCity：三次）再升级，并把 AI 写的摘要交给真人坐席（Aircall，2026-10-29）。[[23]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Gupta et al., Nubank, arXiv 2606.08867](https://arxiv.org/abs/2606.08867) (2026-06)。五个生产部署：标准流程、身份验证后才能调用的工具、升级转交、人工标注的评估。"37 percentage-point improvement in AI transactional Net Promoter Score"。*第一手：是；可信度：高。*
- [Jackson Gold, Pinecone](https://www.pinecone.io/blog/support-agent-nexus/) (2026-09-01)。工单分流 → 账户查询 → 调查 → 退款和限额问题的升级简报。"resolves 55.1% of the tickets"；"27 of the 49"。*第一手：是（早期，样本小）；可信度：高。*
- [Decagon, Tremendous case study](https://decagon.ai/case-studies/tremendous) (undated)。双因素所有权核验 → 重发、取消或换货 → 带上下文升级。"92% CSAT… compared with 86% for its BPO team"。*第一手：厂商；可信度：中。*
- [Intercom Community, Fin resolution thread](https://community.intercom.com/questions/3622) (2023–2026)。从业者报告解决率以及他们如何维护知识库。"around 55-60% from the past week, in around 3000 conversations"。*第一手：是（论坛）；可信度：低。*
- [Aircall, How TripCity cut live call volume in half with AI Voice Agent "Miles"](https://aircall.io/customer-stories/tripcity/) (2026-10-29)。语音渠道的流程型智能体，覆盖三条电话线路；三次解决尝试后升级给真人坐席。"87% of calls resolved without escalation to live agents"。*第一手：厂商；可信度：中。*
