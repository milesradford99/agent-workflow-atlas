---
id: AWF-0149
name: 可决策的投保件分诊
summary: "把经纪人投保件数字化并打分，排入核保队列；低置信度的由人工复核，核保员最终决定。"
deliverable: 已分诊的投保件队列
shape: "经纪人投保件 (邮件、ACORD 表格、多语言文档) → 数字化为险种数据模式 → 补充内部 + 外部数据 → 承保偏好 + 优先级评分 → 高置信度：直接进入队列 | 低置信度：🛑 review (验证检查点) → 🛑 sign-off (核保员评估、报价、承保或拒保)"
source_hash: 82e4613c35f6
---

# 可决策的投保件分诊

**与相近工作流的区别：** 上文的 Hiscox 报价起草会产出带定价的报价。本工作流的产出是排好序的投保件队列，每个风险仍由核保员定价。AWF-0022 形态相近，但产出的是应付款项，而不是核保决定。
**工具变体：** `cytora` · `kalepa`

## 步骤

1. 接收非结构化的投保件，按承保机构的数据模式转换为结构化的、'decision-ready' 的风险 [[1]](#sources)[[2]](#sources)。
2. 补充外部数据，并按承保偏好和策略排序 [[3]](#sources)[[4]](#sources)。
3. 高置信度的投保件直接进入核保队列 [[2]](#sources)。
4. 🛑 **审阅**：低置信度的投保件停在 'human-in-the-loop validation checkpoints'，由人在投保件进入队列前核对提取出的数据 [[2]](#sources)。
5. 🛑 **签发**：核保员在下游系统中评估、报价并承保（或拒保）[[1]](#sources)[[4]](#sources)。

**产出：** 核保工作台中按优先级排序的结构化投保件队列。
**失败模式 → 防护：** 提取错误流入定价 → 置信度阈值和验证检查点。核保员只看到收件箱的一小部分 → 全收件箱分诊（Paragon）和拒保分流。

**近期实践（2026）：**
- 步骤 2：Hiscox 英国高净值客户模型按风险偏好对经纪人投保件分类，以简化核保员的工作流（Hiscox 2025 年报）。[[5]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：第一手实例只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Ivans, Arch Insurance submission intake](https://www.ivans.com/blog/posts/arch-insurance-ai-submission-intake-cytora/) (2026-05-26)。四条业务线在不到三个月内上线。"from two to three days down to two hours"。*第一手：厂商；可信度：中。*
- [Cytora, Zurich scales Agentic AI](https://cytora.com/risk-flow-center/blog/zurich-scales-agentic-ai-to-5-countries-in-90-days-proving-the-target-model-for-itsglobal-rollout) (n.d.)。在 Zurich 各国分支推广。"manual triage time falling from 75 minutes to 15 minutes"。*第一手：厂商；可信度：中。*
- [Markel, AI can accelerate underwriting](https://www.markel.com/insights-and-resources/insights/ai-can-accelerate-underwriting-people-must-remain-accountable) (2026-11-02)。承保机构自己的叙述；核保员最终确定每一份报价。"a 65% quote-to-submission ratio"。*第一手：是；可信度：高。*
- [Kalepa, Paragon case study](https://kalepa.com/case-studies/paragon-doubled-quote-to-bind-rate) (n.d.)。整个收件箱在 90 天内全部经过分诊；引述 Paragon 管理层的话。"somewhere around 98 to 99% accurate now"。*第一手：厂商；可信度：中。*
