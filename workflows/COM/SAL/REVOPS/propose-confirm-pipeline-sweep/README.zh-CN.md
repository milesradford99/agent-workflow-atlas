---
id: AWF-0052
name: 提议确认式管道巡检
summary: "每天巡检 CRM 销售管道中过期或缺失的下一步并发布异常视图；回写数据前由人工确认。"
deliverable: 管道异常报告
shape: "每天读取 CRM 实时管道 → 核对 Slack/邮件/日历/笔记中的沟通 → 每个未结商机：带来源和日期的下一步，检查停滞 / 超过预计成交日期 / 决策委员会信息单薄 → 运行质量自检 → 发布异常视图 → 🛑 action (人工确认回写) → 🛑 review (每周管道例会)"
source_hash: 191a9ec23dc5
---

# 提议确认式管道巡检

**与相近工作流的区别：** 同批的 DEAL 工作流是逐通电话、由销售批准的更新。本工作流是由 RevOps 负责的、覆盖全部商机的每日巡检。AWF-0006 受管控的查询（Governed query）回答临时问题，不维护记录。
**工具变体：** `claude-salesforce-mcp`

## 步骤

1. 每个工作日读取实时管道，绝不使用导出文件或保存的副本 [[1]](#sources)。
2. 核对 Slack、邮件、日历和会议纪要中的沟通，这样当有人昨天刚和联系人谈过时，这段关系就不会被误标为冷淡 [[1]](#sources)。
3. 对每个未结商机，写出带日期和来源的下一步，梳理采购决策委员会，并标记停滞的商机、已经过期的预计成交日期和缺失的签字人 [[1]](#sources)。
4. 用 15 项质量检查给这次运行评分，并公开报告未通过的项 [[1]](#sources)。
5. 🛑 **操作**：除非有人点击确认，否则不会向 Salesforce 回写任何内容 [[1]](#sources)。
6. 🛑 **审阅**：每周的管道例会从异常视图开始，而不是从手工制作的演示稿开始 [[1]](#sources)。

**产出：** 覆盖全部商机的每日异常视图、经人工确认的 CRM 修正，以及一份现成的管道例会材料。
**失败模式 → 防护：** 仪表盘建立在过期快照上 → 只读取实时记录 [[1]](#sources)。误报“冷淡” → 跨渠道核对 [[1]](#sources)。无人监督的写入损害信任 → 先提议，再由人确认回写 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Truffle Corp, Claudeforce on our Salesforce pipeline](https://www.trufflecorp.com/post/claudeforce-salesforce-pipeline) (2026-09-17)。一家咨询公司在自己的 Salesforce 上运行 CRO 智能体四个月；回写由人确认。"Contact categorization improved from 31% in July to 88% in August and 95% in September"。*第一手：厂商；可信度：中。*
