---
id: AWF-0005
name: 告警富化与研判
summary: "对安全告警做情报富化并给出带证据的结论；良性告警自动关闭，其余转二线，每周抽检自动关闭项。"
deliverable: 告警结论
shape: "告警 → 每个来源：富化 (威胁情报、身份、EDR) → 结论 + 证据 → 良性：自动关闭 | 可疑：🛑 handoff · 每周 🛑 sample"
source_hash: 0baf2add62ff
---

# 告警富化与研判

## 背景

安全分析师会调查监控账号、计算机和网络活动的系统所发出的告警。告警只是需要查看的线索，并不等于攻击已经发生：同一个动作对某个账号可能很正常，对另一个账号却很可疑。要判断哪些值得关注，通常需要先从多处记录中补齐背景。智能体可以在告警到达时收集记录，给出有依据的判断。可疑或无法确定的案件仍由分析师调查，并抽查已关闭项，因为一次错误关闭就可能掩盖入侵。

**术语：**
- **富化（enrichment）**：为告警补充相关事实，例如账号历史、某个地址是否与攻击有关。
- **威胁情报**：有关恶意基础设施、软件及行为的信息。
- **身份（identity）**：与动作关联的用户或服务账号。
- **EDR**：终端检测与响应，记录计算机上的活动并标出可能的攻击。
- **二线（Tier 2）**：接手需要深入调查案件的分析师。
- **质检（QA）**：这里指检查告警是否被正确关闭。

## 用智能体搭建

**形态：** `service`。告警到达时不需要人逐个启动调查，人只查看升级案件和关闭样本。

**需要：** 告警队列；经批准、通过 MCP server (connector) 工具只读访问的威胁情报、账号记录和终端日志；按来源编写的调查手册；案件存储与审阅队列。安全遥测数据应留在机构批准的环境中。只授予手册所需的告警处置权限，不提供隔离设备或修改账号的工具。

| 步骤 | 搭建方式 |
|---|---|
| 告警 → 每个来源：富化 | 由告警队列启动 `claude -p` (headless)。Skill 规范化告警；Subagents 通过只读 MCP server (connector) 工具收集各来源的证据。 |
| 结论 + 证据 | Skill 把处置结论、不确定性以及所查记录的链接写入案件存储。 |
| 良性：自动关闭 | Hook 在处置工具关闭告警之前，检查是否符合获批的关闭规则、所需证据是否齐全。 |
| 可疑：🛑 handoff | 服务把准备好的案件写入分析师队列，结束该条目的运行。 |
| 每周 🛑 sample | 定时运行的 `claude -p` (headless) 将规则指定的关闭样本复制到审阅队列。 |

**检查点：** `handoff`：可疑、不确定或证据不完整的案件保持打开，连同告警、查询结果和理由进入分析师队列。智能体没有事件响应工具。`sample`：服务把关闭项及证据复制到每周质检队列；分析师的判断用于更新手册和关闭规则。

**与来源相比：** 公开实例出自 2026-01 至 2026-07，没有单列的 Sources 清单。全部公开实例页面已于 2026-11 打开。检索发现 [Elastic 当前的 agent-builder 指南](https://www.elastic.co/docs/solutions/security/ai/agent-builder/skills-use-cases)，于 2026-11 打开，介绍了通过 skill 和工具展开调查。无界面智能体配合按来源编写的 Skills 和 Subagents 可以承载推理流程；告警队列、证据存储及关闭控制仍需由运维方提供。公开实例支持富化和处置结论，但不能证明条目中的每周质检频率是已报道实践；这里将其保留为目录提出的防护措施。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 智能体规范化告警。
2. 智能体并行执行富化查询。
3. 智能体按分析师手册调查富化后的告警。
4. 智能体返回带置信度和证据的结论。
5. 系统自动关闭良性告警，并附上证据。
6. 🛑 **接手**：其余告警作为准备好的案件转交二线。
7. 🛑 **抽检**：质检每周抽查自动关闭的告警。

**指标：** 每条告警耗费的分析师分钟数。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Shapton, Hanify, Pezzino, Databricks](https://databricks.com/blog/scaling-security-alert-triage-specialized-agents-databricks) (2026-07-06)。17 个按来源划分的智能体做富化 → 升级 / 监控 / 关闭；升级由分析师决定。"over 18,000 alerts with a 3.2% escalation rate"；"over 6,500 analyst hours in the first 30 days"。*第一手：是；可信度：高。*
- [Aaron Jewitt, Elastic Security Labs](https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows) (2026-07-02)。确定性检查 → 20 多个富化来源 → 分诊和专家智能体 → 结论。"30-minute manual alert triage into under 3 minutes"。*第一手：是（自家产品）；可信度：高。*
- [Mo & Stöckli, GitHub Security Lab](https://github.blog/security/ai-supported-vulnerability-triage-with-the-github-security-lab-taskflow-agent/) (2026-01-20)。事实 → 误报审计 → 经验证的报告 → 带标签的议题。"~30 real world vulnerabilities"。*第一手：是；可信度：中。*
