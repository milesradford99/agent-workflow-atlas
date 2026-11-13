---
id: AWF-0108
name: 住户报修分诊派单
summary: "对住户报修进行分诊，生成带优先级的工单并派给技师或承包商；紧急情况转交值班人员。"
deliverable: 已派发的工单
shape: "住户留言或来电 → 诊断式分诊 (提问、照片、安全风险) → 咨询：回答 | 报修：分类 + 排定优先级的工单 → 指派技师 / 派发承包商 | 紧急情况：降级安抚或 🛑 handoff (值班人员) → 跟踪工作 → 收集反馈"
source_hash: 2e21e7e6a4bf
---

# 住户报修分诊派单

**与相近工作流的区别：** 与 AWF-0021 同属一个类别，但这里的事务是向技师或承包商做实际派单，而不是账户操作。
**工具变体：** `eliseai` · `qed-labs`

## 步骤

1. 用结构化的提问和照片对报修请求做分诊，并评估安全风险 [[2]](#sources)。
2. 对状态类咨询直接回答，不生成工单（L1 Property 为 44%） [[2]](#sources)。
3. 创建分类的工单，并对虚假的“紧急情况”降级安抚 [[1]](#sources)。
4. 自动指派或派发承包商，然后跟踪工作的整个生命周期 [[2]](#sources)。
5. 🛑 **接手**：真正的紧急情况和复杂案件转交工作人员 [[1]](#sources)。

**产出：** 已派发并被跟踪的工单，以及向住户的进展通知。
**失败模式 → 防护：** 真正的紧急情况被误分诊 → 安全风险提问和升级路径。来源中对接手环节的设计描述很少。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [EliseAI, Summit Property Management](https://eliseai.com/customer-stories/how-summit-property-management-reinvented-their-management-model-with-ai-and-centralization) (n.d.)。10,000 多套公寓；报修分诊。"MaintenanceAI generated 9,760 categorized work orders and de-escalated 34% of “emergencies,”"。*第一手：厂商；可信度：中。*
- [QED Labs, L1 Property](https://qedlabs.co.uk/case-studies/l1-property) (n.d.)。603 个单元；向 36 家承包商派发 765 项工作。"66% Increase in first-time fix rate"。*第一手：厂商；可信度：低。*
- [EliseAI, Woodward Properties](https://eliseai.com/customer-stories/how-woodward-properties-built-a-24-7-operating-model-with-eliseai) (n.d.; data Apr-May 2026)。约 2,300 套的运营商；紧急情况分诊 + 自动指派；引述了 CEO 和员工的话。"a 50% reduction in after-hours emergency dispatches"。*第一手：厂商；可信度：中。*
