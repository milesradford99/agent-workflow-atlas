---
id: AWF-0163
name: 全科医生报告摘要核保
summary: "为保障类保险核保摘要冗长的全科医生报告；每个决定由核保人作出，输出定期审计。"
deliverable: 核保决定
shape: "个人保障类保险申请 → 收到全科医生（GP）体检报告 (多达 90+ 页) → GenAI 过滤无关细节 + 归纳关键医学事实 → 🛑 review (核保人阅读摘要并作出最终决定) → 把决定告知顾问 → 🛑 sample (投保后审计 + 定期质量复核)"
source_hash: 7d3b9fe714ff
---

# 全科医生报告摘要核保

**与相近工作流的区别：** AWF-0149 是把经纪人提交的案件分诊为带评分的队列；AWF-0155 是起草带定价的经纪人报价邮件。本工作流中智能体浓缩一位申请人的医学证据，每个案件都由核保人决定（辅助）：交付物（基于医学证据的个人风险决定）和检查点都不同。这使 UW 类下有三个各不相同的工作流。
**工具变体：** `aviva-in-house` · `vitality-in-house`

## 步骤

1. 个人寿险、重疾险或严重疾病险的申请需要一份全科医生体检报告 [[1]](#sources)[[2]](#sources)[[3]](#sources)。
2. GenAI 分析报告，过滤无关细节并突出关键信息，把「有时超过 90 页」的报告压缩成简明摘要 [[1]](#sources)。
3. 先从风险较低的案件开始推广，再扩大使用 [[3]](#sources)。
4. 🛑 **审阅**：「Aviva 的核保人将审阅这些摘要并作出最终决定」 [[1]](#sources)。
5. 🛑 **抽检**：投保后审计，以及「定期质量复核和持续监督」 [[2]](#sources)[[3]](#sources)。

**产出：** 对保障类保险申请的核保决定，告知顾问和客户。
**失败模式 → 防护：** 摘要漏掉重大病况 → 经过 18 个月测试，在扩展到重疾险之前对各类病况做准确性验证，从低风险案件开始，持续做质量复核 [1][2][3]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [Aviva, AI underwriting tool launch](https://www.aviva.com/newsroom/news-and-research-overview/news-releases/2025/11/aviva-to-launch-groundbreaking-ai-underwriting-tool/) (2025-11-18)。经过 18 个月测试后推广寿险核保；每个案件由核保人决定。"already processed 1,000 cases in an active test phase"。*第一手：是；可信度：高。*
- [Aviva, extends to Critical Illness](https://www.aviva.com/newsroom/news-and-research-overview/news-releases/2026/03/aviva-extends-industry-first-ai-underwriting-tool-to-critical-illness-cover/) (2026-03-18)。扩展到重疾险；也用于投保后审计。"reduced the time underwriters spend reviewing each case by around half"。*第一手：是；可信度：高。*
- [IFA Magazine, Vitality AI underwriting](https://ifamagazine.com/vitality-launches-ai-powered-underwriting-to-speed-up-adviser-case-decisions/) (2026-04-15)。自研 LLM 生成全科医生报告摘要，试点 18 个月，先做低风险案件。引述了 CEO 的话。"an 81% reduction in GP report length"。*第一手：厂商；可信度：中。*
