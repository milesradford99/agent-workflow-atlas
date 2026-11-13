---
id: AWF-0174
name: 长尾客户自主续约
summary: "在客户负责人否决窗口之后，于折扣上限内自主推进长尾客户续约；特殊情况转续约专员。"
deliverable: 已完成的续约
shape: "划分长尾账户 → 每个账户：监测健康度、使用量、账单 → 续约窗口：🛑 action (客户负责人否决窗口) → 以客户成功经理（CSM）身份发送个性化触达 → 客户回复 → 折扣上限内：修订报价 + 更新 CRM + 电子签 | 超出上限或特殊情况：🛑 handoff (续约专员/CSM) → 🛑 review (数字化客户成功经理复盘结果、调整打法)"
source_hash: 68f17e613bbf
---

# 长尾客户自主续约

**与相近工作流的区别：** 最接近的是 AWF-0049 续约窗口风险简报：那是产出风险简报和挽留方案，由 CSM 批准每次触达。本工作流中智能体自己推进续约对话，并在折扣上限内成交；人只会看到事先通知和例外情况。交付物（已完成的续约与简报）和自主程度（抽检与分段）都不同。
**工具变体：** `gainsight-atlas` · `planhat` · `quivly` · `statisfy`

## 步骤

1. 按客户层级划定覆盖范围；长尾账户由智能体推进，战略账户仍由人主导 [[2]](#sources)[[3]](#sources)。
2. 智能体监测每个账户的健康度、使用量、支持和账单信号，并在续约节点（例如 90/60/30 天）触发 [[2]](#sources)。
3. 🛑 **操作**：联系客户之前，智能体先向客户经理（AE）发消息，告知续约日期和预期 ARR，让对方有机会提出异议；在 Gainsight 的演示中，AE 回复「Looks good. Go ahead.」 [[1]](#sources)。
4. 智能体从 CSM 的邮箱发出个性化的续约触达，并阅读回复 [[1]](#sources)[[4]](#sources)。
5. 如果客户要求的折扣在硬性上限之内（演示中为 8%），智能体修订报价，更新 Salesforce 中的商机，并通过 DocuSign/CPQ 发送，无需人工参与 [[1]](#sources)。
6. 🛑 **接手**：超出上限的请求、自动尝试后健康度仍低于阈值的情况或特殊情况，连同完整上下文和起草好的消息一并转给人 [[1]](#sources)[[2]](#sources)[[3]](#sources)。
7. 🛑 **审阅**：数字化客户成功经理审阅被升级的账户和操作历史，并删减或调整打法 [[2]](#sources)[[3]](#sources)。

**产出：** CRM 中已完成续约的长尾账户，以及一个需要人介入的账户的优先级队列。
**失败模式 → 防护：** 智能体在价格上让步过多 → 在工作流中设置硬性折扣上限，而不是写在提示词里 [1]。无人负责的账户悄然流失 → 账单和使用量信号驱动触发 [2]。客户始终接触不到真人 → 自动尝试失败固定次数后转交 [3]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Gainsight, Atlas in Action](https://pulselibrary.gainsight.com/video/atlas-in-action/) (2026-05-27)。演示中，在 AE 收到事先通知、客户提出 6% 的折扣请求（上限 8%）后，由智能体完成续约。"the estimated ARR for this particular renewal was $210,000 US"。*第一手：厂商；可信度：低。*
- [Planhat, Fluxx customer story](https://www.planhat.com/fluxx) (undated)。续约触达智能体代表 CSM 发送，每位 CSM 负责 100 多个账户。"engaging with renewal conversations six to eight months out"。*第一手：厂商；可信度：中。*
