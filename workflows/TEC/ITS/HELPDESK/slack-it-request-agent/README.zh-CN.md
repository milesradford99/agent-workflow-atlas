---
id: AWF-0068
name: Slack IT 请求助手
summary: "在 Slack 中处理 IT 使用咨询与权限申请；权限开通须指定审批人批准，无法处理的转为工单交人工。"
deliverable: 已解决的 IT 请求
shape: "Slack 请求 → 识别意图 → 使用咨询：带链接的知识库回答 | 权限申请：匹配 Okta 组 → 检查策略和现有权限 → 🛑 action (应用审批人) → 通过 API 开通 → 确认 | 不明确或不支持：🛑 handoff (附上下文的工单)"
source_hash: 26e872379d54
---

# Slack IT 请求助手

**与相近工作流的区别：** AWF-0021 流程智能体（CSX RESOLVE）服务的是外部客户。本工作流服务员工，并在每个应用的审批人把关下，修改身份提供方（IdP）中的身份与权限状态。AWF-0005 处理的是安全告警，不是员工请求。
**工具变体：** `langgraph-claude-okta-slack-jsm` · `harmony` · `risotto` · `servicenow-ai-agents`

## 步骤

1. 动手搭建之前，先把过去一年的工单按数量排序。优先自动化每年超过 1,000 个请求的类别（权限申请和密码重置排在最前）[[2]](#sources)。
2. 员工在 Slack 中发帖。智能体把消息归入某个意图（access_request、how_to、incident、password_reset、other），每个意图有各自的置信度阈值。置信度低时，它会追问澄清 [[1]](#sources)。
3. 使用咨询：检索 Confluence 段落（pgvector），回复带来源链接的格式化答案 [[1]](#sources)。
4. 权限申请：找到正确的 Okta 组（别名、模糊匹配、重排序），检查用户是否已有权限，并查出存放在应用的 Okta 属性上的审批人 [[1]](#sources)。每个应用由谁审批，是事先写成策略的，而不是由模型决定 [[2]](#sources)。
5. 🛑 **操作**：指定的审批人在 Slack 私信中一键批准或拒绝。离职处理需要第二个人，申请人和审批人永远不能是同一人 [[1]](#sources)[[2]](#sources)。
6. 批准后，通过 Okta Groups API 把用户加入。开通失败的请求进入死信队列，并在 Slack 发出告警 [[1]](#sources)。
7. 🛑 **接手**：没有对应操作手册或知识库匹配的请求，会变成 Jira Service Management 工单（或在同一线程中交给人），并持续告知申请人进展 [[1]](#sources)[[2]](#sources)。
8. 来自 Okta 事件钩子的入职/调岗/离职事件会触发标准权限的开通、权限复核和回收。操作手册在发布前先在测试频道中测试 [[1]](#sources)。

**产出：** 请求要么在 Slack 中关闭（给出答案，或开通权限并留有记录），要么带着上下文以工单形式转给 IT 人员。
**失败模式 → 防护：** 由模型决定谁能审批 → 把审批规则放进工作流或策略，而不是提示词 [[2]](#sources)。某个 worker 挂掉导致开通悄悄中断 → 健康检查告警 [[1]](#sources)。置信度阈值靠猜 → 用数周的真实流量来调优 [[1]](#sources)。区分大小写的组名导致悄悄拒绝访问 → 对照 IdP 检查配置 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：仅有匿名、厂商相关或由记者转述的记录。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Harmony, Cyera customer story](https://harmony.io/customers/cyera) (2026-08-07)。权限申请在 Slack 中一键审批，Okta 范围内的组，离职需两人确认，在线程中转交人工。"90–95% - of access requests fully automated"。*第一手：厂商；可信度：中。*
- [inguva.dev, How I Built Kernel](https://blog.inguva.dev/how-i-built-kernel-an-ai-powered-it-helpdesk-that-deflects-80-of-support-tickets) (undated)。LangGraph + Claude 的 Slack 机器人：意图路由、审批人私信、Okta 开通、Jira 升级；8 周的结果。"78% deflection rate"。*第一手：匿名；可信度：低。*
