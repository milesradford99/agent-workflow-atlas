---
id: AWF-0085
name: 按政策审核报销
summary: "对照差旅费用政策审核报销单；合规的交经理签批，违规的转 T&E 专员，并向员工反馈。"
deliverable: 已审核的报销单
shape: "提交报销单 → 规则检查 (金额、日期、时效、品类限额) → LLM 对照政策阅读收据 → 币种检查 → 合规：自动通过 → 🛑 sign-off (经理) | 违规：🛑 handoff (T&E 专员) → 向员工发送模板化反馈"
source_hash: 742d98760b3b
---

# 按政策审核报销

**与相近工作流的区别：** AWF-0022 发票提取-匹配-分派（Invoice extract-match-route）把供应商发票与采购订单匹配后付款。本工作流则是对照内部差旅与费用（T&E）政策检查员工的报销，并向员工发送指导性反馈。产出物和检查点的负责人都不同。
**工具变体：** `make-gemini-workday-monday` · `appzen`

## 步骤

1. 员工在 Workday 中提交报销单。Webhook 在 T&E 团队的审核看板（monday.com）上创建一个条目 [[1]](#sources)。
2. 运行规则检查：条目金额、日期、报销时效，以及餐饮、活动等品类限额 [[1]](#sources)。
3. 对需要进一步审查的条目，把政策、收据和员工数据发给 LLM（Vertex AI 上的 Gemini）。它提取收据细节，并对照政策作出判断 [[1]](#sources)。
4. 再做一些确定性的检查，例如币种是否一致 [[1]](#sources)。
5. 分派。合规的报销单自动通过，并在 Workday 中转给经理（🛑 **签发**：经理）。违规的进入“需要审核”（🛑 **接手**：由 T&E 专员判断）[[1]](#sources)。
6. 对需要修改的报销单，专员选用预先写好的违规说明，通过邮件或 Workday 发给员工 [[1]](#sources)。
7. T&E 团队在看板上编辑政策清单和阈值。这些内容按需同步，并在每周日同步 [[1]](#sources)。
8. 上线前，与旧流程并行运行 60–70 天。上线 30–40 天之后才扩大自主度 [[1]](#sources)。

**产出：** Workday 中已通过或已退回的报销单，外加审核队列和异常情况的审计轨迹。
**失败模式 → 防护：** 政策版本不对 → 由团队自己维护政策库，每周同步。过度信任模型 → 并行运行，逐步放开自主度。明显违规的仍需要人来处理（目前只是在考虑自动驳回）。准确率（“接近 100%”）是厂商自报的。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Make, Celonis expense auditing story](https://www.make.com/success-stories/make-ai-agents-help-celonis-lower-expense-auditing-costs) (2025-11-25)。Celonis T&E 团队的智能体每月审核数千行费用；违规项分派给专员。"We can now process about a thousand documents per dollar.". *第一手：厂商；可信度：中。*
