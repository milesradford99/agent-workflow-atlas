---
id: AWF-0186
name: 经 plan 验证的漂移修复
summary: "每天早上为每个发生漂移的 Terraform 项目提交一个经 plan 验证的合并请求；由所属团队审阅并执行。"
deliverable: 漂移修复合并请求
shape: "工作日定时任务 → 对所有 IaC 项目运行 plan (JSON) → 干净: 记录 | plan 失败: 仅发 Slack 报告 | 云端缺失: 报告，不改动 | 漂移: 每个项目: 起草 HCL (更新以匹配 | 保留 + 回退警告 | import 块) → 独立分支 + MR → autoplan → 标记 ready-for-review | needs-investigation → 一份早晨 Slack 报告 → 🛑 review (所属团队批准 MR) → 🛑 action (工程师执行 apply) · 每周: 集中复盘已关闭的 MR"
source_hash: 79e321348940
---

# 经 plan 验证的漂移修复

**与相近工作流的区别：** AWF-0066 对话式 IaC 变更（Chat-to-IaC change）从人在 Slack 中的请求或一条告警出发，产出一项被请求的变更，漂移只每天检查一次。这里由定时任务触发，输入是在所有项目中检测到的漂移，产出是每个漂移项目一个 MR，其回退/更新/导入的决定通过重新运行 plan 来验证。触发方式、产出物和决策类型都不同。
**工具变体：** `atlantis` · `terraform` · `gitlab` · `kubernetes-cronjob`

## 步骤

1. Kubernetes CronJob 在工作日太平洋时间 09:00 运行，截止时间 1 小时，同一时间只运行 1 次。一次请求就让 Atlantis 并行对全部 187 个项目运行 plan，并输出 `terraform show -json` [[1]](#sources)。
2. 干净的项目只记录。plan 失败的项目进入 Slack 报告，永远不会交给模型。云端缺失的资源只报告、不提出改动，因为删除可能是有意为之 [[1]](#sources)。
3. 每个漂移项目会收到一份提示词，内含文本 plan、漂移和变更的资源列表、清洗后的 JSON plan（各自截断在 30,000 个字符）以及模块中的每个 .tf 文件。模型只返回 HCL 加一段简短的分析和警告。当云端的值看起来是有意设置时，它更新 HCL；否则保留代码，并警告下一次 apply 会将其回退。对于存在于云端但不在 state 中的对象，它会在导入 ID 格式对照表的指引下写一个 import 块。替换被标记为高风险 [[1]](#sources)。
4. 安全控制写在代码里，而不是提示词里：只能运行 init/plan/show/version，疑似密钥的值会被脱敏，文件写入限制在项目内，plan 角色是只读的，只有 MR 获批后 Atlantis 才会 apply [[1]](#sources)。
5. 每个项目有自己的分支和 MR，其中显示模型 ID 和提示词哈希。Atlantis autoplan 是验证者，智能体把 MR 标记为 ready-for-review 或 needs-investigation [[1]](#sources)。
6. 🛑 **审阅**：所属团队并排审阅 diff 和 plan，然后批准、编辑或关闭 [[1]](#sources)。
7. 🛑 **操作**：由工程师通过 Atlantis 执行 apply。批准和 apply 的权限仍由人掌握 [[1]](#sources)。
8. 每天早上一份 Slack 报告，附上各 MR 的链接。超过 3 天未处理的漂移 MR 数量，是评审滞后的信号。已关闭的 MR 每周集中复盘，提示词在仓库中有版本管理 [[1]](#sources)。

**产出：** 每个项目一个带验证 plan 的漂移修复合并请求，由所属团队审阅并 apply。每天早上 IaC 状态保持干净。
**失败模式 → 防护：** 修复类型错误（27）、误判意图（20）和导入 ID 格式错误（18）→ 一张导入格式对照表把 ID 错误从 13 降到 5。仍能通过干净 plan 的弱提案 → 有 12 个只被评审者发现，所以人工评审必须保留。漏掉模块的 .tf 文件会降低修复质量 → 始终附上。脱敏是最薄弱的控制 → 每次新增 provider 时都要复查。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Philo via DEVOPSdigest, Letting an LLM Draft Our Terraform Drift Fixes](https://devopsdigest.com/letting-llm-draft-our-terraform-drift-fixes-twelve-weeks-production) (2026-11-04)。为期 12 周的评估：56 次运行、372 个漂移事件、351 个 MR；工程师每周耗时从 9.4 小时降到 2.4 小时。"Of the 351 MRs, 73.5% were merged without semantic changes, 18.2% were merged after a reviewer edited them, and 8.3% were closed."。*第一手：是；可信度：高。*
