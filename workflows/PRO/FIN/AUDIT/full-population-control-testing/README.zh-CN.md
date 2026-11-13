---
id: AWF-0040
name: 全量控制测试
summary: "对全部样本逐项测试内部控制，结论附来源引用；审计师复核每项结论和例外。"
deliverable: 控制测试底稿
shape: "配置控制项 + 证据格式 + 复核流程，约定 KPI → 🛑 plan → 每个控制项：收集证据 → 处理数据 → 测试 → 得出附来源引用的结论 → 🛑 review (审计师检查每项结论和例外)"
source_hash: 38a742a55902
---

# 全量控制测试

**与相近工作流的区别：** AWF-0005 告警富化与裁决（Alert enrich and adjudicate，SECOPS）裁决的是安全告警。本工作流则对照证据测试财务控制，并产出审计底稿。
**工具变体：** `kaption` · `kpmg-clara`

## 步骤

1. 按组织自身的控制项、证据格式和复核流程配置工具 [[1]](#sources)。
2. 🛑 **计划**：审计负责人在首次运行前约定好 KPI [[1]](#sources)。
3. 智能体收集证据、处理数据并测试每个控制项，每项结论都引用到其来源 [[1]](#sources)。在一家四大会计师事务所，智能体执行费用凭证核对、查找未入账负债等实质性程序 [[2]](#sources)。
4. 🛑 **审阅**：审计团队复核每项带引用的结论和例外 [[1]](#sources)。该事务所称自己保留了“人在回路中”（'a human-in-the-loop'）[[2]](#sources)。

**产出：** 已测试控制项的底稿，含带引用的结论和例外，经审计师复核，用于 ICFR 评估或审计档案。
**失败模式 → 防护：** 漏报（试点中低于 10%）→ 审计师复核，并在推广前约定 KPI [[1]](#sources)。

**近期实践（2026）：**
- 计划环节：在 KPMG，审计师通过“选择合适的数据要素、组合最佳的方法步骤”来设置运行，之后由智能体挑出需要测试的费用、读取文档、提取日期和金额，并写出底稿（CFO.com 2025-05-16）。[[3]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Kaption, Celsa Group pilot](https://www.kaption.io/case-studies/celsa) (n.d.)。智能体测试了 60 个 ICFR 控制项，结论带引用，交内部审计复核。"Agent reasoning aligned with the auditors' own judgement in 85% of cases"。*第一手：厂商；可信度：中。*
- [KPMG, Clara AI agents](https://kpmg.com/us/en/media/news/kpmg-clara-smart-audit-platform.html) (2025-04-23)。全所范围的智能体用于凭证核对和未入账负债查找；工作流细节很少。"more than 95,000 auditors globally"。*第一手：是（公告，并非实测运行）；可信度：低。*
- [CFO.com, How KPMG is using AI to revamp their audit practice](https://www.cfo.com/news/how-kpmg-thomas-mackenzie-is-using-clara-ai-to-revamp-their-audit-practice-/748316/) (2025-05-16)。KPMG 审计负责人介绍了 Clara 费用验证智能体的步骤，以及审计师的引导和复核角色。"If we can do 100% testing, it's like placing a filter across the river."。*第一手：访谈；可信度：中。*
