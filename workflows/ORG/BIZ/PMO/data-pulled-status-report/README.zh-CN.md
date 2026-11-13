---
id: AWF-0084
name: 数据驱动的项目状态报告
summary: "从项目数据生成含风险提示和甘特图的状态报告；项目经理修改后再发送。"
deliverable: 项目状态报告
shape: "拉取任务、时间线和项目数据 → 分类为正常、延误、有风险 → 起草摘要、指标、风险提示、甘特图 → 🛑 review (项目经理修改) → 发送给客户或干系人"
source_hash: abe52dbf5a90
---

# 数据驱动的项目状态报告

**与相近工作流的区别：** 没有相近的工作流。AWF-0031 每日收件箱分拣（Daily inbox triage）处理的是收到的邮件，本工作流则是根据项目数据生成对外的项目状态。
**工具变体：** `ganttly`

## 步骤

1. 连接项目数据源（任务列表、时间线）[[1]](#sources)。
2. 模型读取数据，标出哪些正常、哪些延误、哪些有风险，以及哪些事项是干系人关心的 [[1]](#sources)。
3. 生成报告：文字摘要、计算出的指标、标出的风险，以及带依赖关系和关键路径的甘特图 [[1]](#sources)。
4. 🛑 **审阅**：项目经理在发送前阅读并修改草稿 [[1]](#sources)。
5. 按客户要求的格式（PDF、HTML 或邮件摘要）发送，由每月一次改为每周一次 [[1]](#sources)。

**产出：** 发送给客户或干系人的每周状态报告。
**失败模式 → 防护：** 报告看似规整但状态有误 → 项目经理发送前对照源数据核对。报告格式含糊或前后不一致 → 先定好统一模板。证据只是工具作者的一份自述，所以节省时间的说法未经验证。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Sacha d'Unienville, How I automated PM status reports with AI](https://dev.to/workbench/how-i-automated-pm-status-reports-with-ai-1koc) (year not stated)。一位零售业项目经理每周的状态报告由项目数据起草，发送前经人审阅。"Time saved: 5+ hours/week → 30 minutes.". *第一手：厂商；可信度：低。*
