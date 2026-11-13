---
id: AWF-0150
name: 邮件转货运订单
summary: "把客户邮件转成货运报价、订单和预约；异常交由经理处理，并对邮件分类做人工抽检。"
deliverable: 货运订单
shape: "客户来信 → 分类 (报价 | 装运委托 | 预约 | 追踪) → 报价：定价引擎 → 回复 | 委托：跨邮件 + PDF 关联详情，补取缺失信息 → 创建订单 | 预约：预订时段 → 无法解决：🛑 handoff (团队处理异常) → 🛑 sample (人工反馈闭环)"
source_hash: 97c58f410120
---

# 邮件转货运订单

**与相近工作流的区别：** AWF-0021 流程智能体（Procedure agent）回答客户并执行经过身份验证的交易。本工作流没有对话：邮件被转成业务记录，人只处理异常。
**工具变体：** `langgraph` · `azure-openai`

## 步骤

1. 按请求类型对收到的邮件分类，包括整车、零担（LTL）、多式联运和空运 [[1]](#sources)[[3]](#sources)。
2. 报价：读取请求，查询 Dynamic Pricing Engine 并回复 [[2]](#sources)。
3. 装运委托：跨邮件和附件（包括手写的 PDF 备注）关联详情，检测并补取缺失数据，然后创建订单；可并行处理 20 个货载 [[1]](#sources)。
4. 预约：提取详情并锁定提货或送货时段 [[1]](#sources)。
5. 🛑 **接手**：工作流这样设计，是为了“so that if something doesn't go right, that's what our managers work on”[[4]](#sources)。
6. 🛑 **抽检**：对分类做一个 'human feedback loop' [[3]](#sources)。

**产出：** 写入运输系统的订单、报价和预约。
**失败模式 → 防护：** 含糊的委托（'I have a load for Tuesday'）→ 用客户历史上下文补全空缺。未能处理的情况 → 交给经理的异常队列。

**近期实践（2026）：**
- 分类：当一封邮件同时要求整车和零担报价时，可以同时路由到两种报价流程（C.H. Robinson，2025-04-16）。[[5]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [C.H. Robinson, freight lifecycle press release](https://www.chrobinson.com/en-us/about-us/newsroom/press-releases/2024/generative-ai-for-freight-shipment-lifecycle/) (2024-10-31)。报价、委托和预约均由邮件自动化完成。"The tech is turning emails into 5,500 shipment orders a day, achieved in 90 seconds."。*第一手：是；可信度：高。*
- [C.H. Robinson, AI performs over 3 million shipping tasks](https://www.chrobinson.com/en-us/about-us/newsroom/press-releases/2025/ai-performs-over-three-million-shipping-tasks/) (2025-04-16)。订单智能体从最大的整车客户扩展到中小客户和零担邮件委托。"over 5,200 customers are getting their loads accepted in under 90 seconds"。*第一手：是；可信度：高。*
- [C.H. Robinson, More Than 100 Trillion Data Points Fuel C.H. Robinson’s Leadership in Agentic Supply Chains](https://ir.chrobinson.com/news/press-releases/news-details/2026/More-Than-100-Trillion-Data-Points-Fuel-C-H--Robinsons-Leadership-in-Agentic-Supply-Chains/default.aspx) (2026-03-11)。公司对由 AI 订单 + 预约工作流处理的整车运输所做的自我分析。"up to 23% faster speed to market for customer shipments"。*第一手：是；可信度：中。*
