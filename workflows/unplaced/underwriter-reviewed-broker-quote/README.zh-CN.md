---
id: AWF-0155
name: 核保员复核的经纪人报价
summary: "为范围内的续保起草含定价的经纪人报价邮件；发送前由核保员审核。"
deliverable: 经纪人报价邮件
shape: "经纪人投保件 (续保，范围内险种) → 范围检查 → Gemini 评估风险 → 将定价 + 数据填入经纪人邮件 → 🛑 review (核保员) → 发送报价"
source_hash: ad6e7c14ad14
---

# 核保员复核的经纪人报价

**与相近工作流的区别：** AWF-0051 受管控答案库的回复草稿（Governed-library response draft）是根据已批准的答案库回答问卷。本工作流的产出是针对单个风险的带定价报价，由一次核保员审核把关。
**未归类原因：** taxonomy.yaml 中目前没有涵盖此类的类别。在有三个类似的工作流足以支撑新类别 `UW`（TAXONOMY.md 规则 2）之前，先归在这里。
**工具变体：** `gemini-vertex`

## 步骤

1. 范围：美国和加拿大现有的破坏与恐怖主义险种的续保，不含纽约和芝加哥都会区 [[1]](#sources)。
2. 范围内的风险由 Gemini 结合 Hiscox 的内部 AI 工具（Hailo）进行评估 [[1]](#sources)。
3. 系统生成发给经纪人的邮件，定价和其他数据已预先填好 [[1]](#sources)。
4. 🛑 **审阅**：邮件在发给经纪人之前处于 'ready for underwriter review' 状态 [[1]](#sources)。

**产出：** 经核保员审核后发给经纪人的含定价报价邮件。
**失败模式 → 防护：** 范围外或复杂的风险被自动定价 → 范围按险种、续保状态和地域限定；复杂风险仍由核保员处理。

**近期实践（2026）：**
- 步骤 1：到 2026 年，范围已扩展到中型市场风险，破坏与恐怖主义工具直接对接经纪人的平台（Hiscox 2026 年第一季度交易声明）。[[2]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [Hiscox, GenAI lead underwriting model goes live](https://www.hiscoxgroup.com/news/press-releases/2024/12-08-24) (2024-08-12)。在伦敦市场上线；与经纪人 WTW 承保了第一单风险。"an insurance quote in a matter of minutes"。*第一手：是；可信度：高。*
- [Reinsurance News, Hiscox CFO Cooper on AI adoption](https://www.reinsurancene.ws/ai-adoption-drives-productivity-growth-and-opens-business-opportunities-hiscox-cfo-cooper/) (2025-11-07)。增强型主承保已在破坏与恐怖主义业务中规模化；正扩展到中型市场财产险。"from a turnaround time of about three days to certainly around three minutes"；"around two-thirds of the sabotage and terrorism business now subject to the augmented underwriting process"。*第一手：访谈；可信度：高。*
- [Hiscox Group, Q3 2026 trading statement](https://www.hiscoxgroup.com/news/press-releases/2026/03-11-26) (2026-11-03)。美国经纪业务线实现 AI 从投保到报价，并在零售业务中推广。"improved our speed to quote by around 75% in terrorism and architects and engineers"。*第一手：是；可信度：高。*
