---
id: AWF-0005
name: 告警富化与研判
summary: "对安全告警做情报富化并给出带证据的结论；良性告警自动关闭，其余转二线，每周抽检自动关闭项。"
deliverable: 告警结论
shape: "告警 → 每个 来源：富化 (威胁情报、身份、EDR) → 结论 + 证据 → 良性：自动关闭 | 可疑：🛑 handoff · 每周 🛑 sample"
source_hash: e62e9aa4a4fb
---

# 告警富化与研判

## 步骤

1. 规范化告警。
2. 并行执行富化查询。
3. 像分析师一样展开调查。
4. 返回带置信度和证据的结论。
5. 自动关闭良性告警，并附上证据。
6. 🛑 **接手**：其余告警作为准备好的案件转交二线。
7. 🛑 **抽检**：质检每周抽查自动关闭的告警。

**指标：** 每条告警耗费的分析师分钟数。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Shapton, Hanify, Pezzino, Databricks](https://databricks.com/blog/scaling-security-alert-triage-specialized-agents-databricks) (2026-07-06)。17 个按来源划分的智能体做富化 → 升级 / 监控 / 关闭；升级由分析师决定。"over 18,000 alerts with a 3.2% escalation rate"；"over 6,500 analyst hours in the first 30 days"。*第一手：是；可信度：高。*
- [Aaron Jewitt, Elastic Security Labs](https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows) (2026-07-02)。确定性检查 → 20 多个富化来源 → 分诊和专家智能体 → 结论。"30-minute manual alert triage into under 3 minutes"。*第一手：是（自家产品）；可信度：高。*
- [Mo & Stöckli, GitHub Security Lab](https://github.blog/security/ai-supported-vulnerability-triage-with-the-github-security-lab-taskflow-agent/) (2026-01-20)。事实 → 误报审计 → 经验证的报告 → 带标签的议题。"~30 real world vulnerabilities"。*第一手：是；可信度：中。*
