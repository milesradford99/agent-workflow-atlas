---
id: AWF-0050
name: 通话转 CRM 差异审批
summary: "把销售通话整理成 CRM 字段变更建议和跟进邮件草稿；销售批准变更并亲自发送邮件。"
deliverable: 已批准的 CRM 更新
shape: "通话转录 → 拉取客户历史 + 商机记录 → 提取复盘要点（人员、预算、异议、后续步骤）→ 提出字段变更 + 跟进草稿 → 🛑 action (销售批准差异) → 写入 CRM 并提供回滚 → 🛑 review (销售修改并发送跟进)"
source_hash: 47735808578f
---

# 通话转 CRM 差异审批

**与相近工作流的区别：** AWF-0020 先调研再个性化的外呼（Research-then-personalize outbound）在任何沟通之前调研潜在客户并起草首封邮件。本工作流在真实通话之后运行，并把字段级变更写入 CRM，由销售把关。
**工具变体：** `claude-salesforce-mcp` · `claude-code-fathom-gmail`

## 步骤

1. 会议前，智能体把客户历史、过往邮件、通话、营销活动和未结商机汇总成一份简报 [[1]](#sources)。
2. 通话结束后，阅读转录稿并整理复盘：对方是谁、预算、谁来签字、客户自己话语里的痛点、异议及其是否已解决，以及带负责人和日期的后续步骤。所有内容都必须能从转录稿中核实 [[2]](#sources)。
3. 提出 CRM 变更（通话记录、ARR、阶段），并以销售的口吻起草跟进邮件和方案 [[1]](#sources)[[2]](#sources)。
4. 🛑 **操作**：销售在写入任何内容之前先看到拟议的变更。获批的值写入 CRM，之后立即提供回滚 [[1]](#sources)。
5. 🛑 **审阅**：销售阅读方案和跟进邮件，附上文件并点击发送。智能体从不自行发送 [[2]](#sources)。

**产出：** CRM 中更新后的商机记录和已记录的通话，外加由销售发出的跟进邮件和方案。
**失败模式 → 防护：** 编造数字或承诺 → 要求每个字段都能追溯到转录稿 [[2]](#sources)。不希望发生的写入 → 确认技能加回滚 [[1]](#sources)。销售不再认真审阅 → 保持发送环节手动 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Salesforce, Legora customer story](https://www.salesforce.com/customer-stories/legora/connecting-crm-to-claude/) (2026-09-11)。Legora 的销售通过 Claude 做会前简报、记录笔记和更新商机，带审批和回滚。"Those write-back actions now account for almost 20% of our headless tool-call volume."。*第一手：访谈；可信度：中。*
- [Lennard Cowans, post-sales call skill](https://www.linkedin.com/posts/lennycowans_i-automated-80-of-my-post-sales-call-work-activity-7476092744172638208-XHlB) (2026-06-26)。从 Fathom 转录稿到复盘、跟进草稿和报价；由人审阅并发送。"This skill cuts my post-sales call work from a couple hours down to 15 minutes."。*第一手：是；可信度：中。*
