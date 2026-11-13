---
id: AWF-0049
name: 续约窗口风险简报
summary: "扫描临近续约的客户，生成带证据的风险简报和挽留计划；CSM 核实风险标记并批准外联。"
deliverable: 续约风险简报
shape: "每周列出窗口期内的续约 → 每个客户：汇总使用量 + 工单 + 通话 + 账单信号 → 带证据标记 → 简报 + 挽留计划草稿 / QBR 草稿 → 🛑 review (CSM 核实标记) → 🛑 action (CSM 批准外联) → 跟踪计划行动"
source_hash: 2c513ef75200
---

# 续约窗口风险简报

**与相近工作流的区别：** 暂无相近者。AWF-0006 受管控的查询（Governed query）按需回答分析问题；本工作流是对全部客户的定期扫描，最后以 CSM 批准的客户外联收尾。
**工具变体：** `statisfy` · `revllama-pulse` · `kortix-postgres-hubspot-slides`

## 步骤

1. 按计划列出即将进入续约窗口的每个客户。在一个部署中，CSM 会在三个月前收到提前提醒 [[1]](#sources)。以只读方式连接数据源：CRM、通话录音、产品使用、支持、账单 [[2]](#sources)[[3]](#sources)。
2. 对每个客户，汇总 CSM 本来就信任的信号，例如关键联系人沉默、工单严重度构成、席位变化趋势和发票争议，并附上证据抛出事件 [[2]](#sources)。
3. 对被标记的客户，起草附有证据链的挽留计划。对到了回顾节点的客户，整理 QBR 演示稿草稿和简报文档。绝不回写源系统 [[2]](#sources)[[3]](#sources)。
4. 🛑 **审阅**：团队对每个高优先级事件评价是否有用、是否早已知晓。这也用来调整“有风险”的定义，该定义由客户成功（CS）副总裁签字确认 [[2]](#sources)。
5. 🛑 **操作**：CSM 先批准挽留计划，任何内容才会触达客户；QBR 草稿也由 CSM 修改后再演示 [[2]](#sources)[[3]](#sources)。

**产出：** 一份带证据、按优先级排序的续约风险清单，外加位于 CSM 工作区的挽留计划草稿和 QBR 演示稿。获批的外联发送给客户。
**失败模式 → 防护：** 静态健康分让客户在流失时仍显示为绿色 → 跨系统汇总非结构化信号，并用过往的流失案例回放验证 [[2]](#sources)。智能体越权 → 对源系统保持只读，对产出保持仅草稿 [[3]](#sources)。告警太多 → 让团队评价事件是否有用并调整规则 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Statisfy, Simpplr customer story](https://www.statisfy.com/customers/simpplr) (2026-07-24)。Simpplr 的 CS 团队持续运行续约分析；CSM 在续约前三个月收到预警。"Renewal and risk workflows account for 85% of the agentic workflows the team has run to date."。*第一手：厂商；可信度：中。*
- [Revllama, enterprise SaaS renewals](https://www.revllama.com/case-studies/enterprise-saas-renewals) (undated)。对 500 个续约做了 30 天审计；CS 团队评价每个事件；挽留计划由 CSM 批准。"In 30 days Pulse raised 41 high-priority events across the 500 accounts. The team rated 29 useful"。*第一手：厂商；可信度：低。*
