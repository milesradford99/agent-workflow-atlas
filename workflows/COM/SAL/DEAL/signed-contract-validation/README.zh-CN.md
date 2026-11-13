---
id: AWF-0222
name: 已签合同校验
summary: "对照报价和规则校验每份已签合同并写入 CRM；有疑问的转交交易支持台。"
deliverable: 已校验的赢单记录
shape: "DocuSign 回传 → 读取已签 PDF（视觉） → 核对签署人权限 → 对照报价校验价格 + ACV → 确认缩写签名 + 必备条款 → 有任何疑问：🛑 handoff (交易支持台专员) | 全部检查通过：把字段写入 Salesforce + 审计轨迹 → 赢单"
source_hash: 017c2aff3619
---

# 已签合同校验

**与相近工作流的区别：** 最接近的是 AWF-0176 从询价到报价的起草（以及 AWF-0050 通话到 CRM 的 diff 审批）。那两个起草的是报价或 CRM diff，由销售逐项审阅（分段/辅助）；本工作流则在签署之后校验合同，并在没有逐项审批的情况下写入记录系统，只把异常转给专员（抽检）。交付物（已校验的赢单记录）和检查点（异常接手）都不同。
**工具变体：** `salesforce` · `docusign` · `gemini` · `claude`

## 步骤

1. 在已签合同从电子签回传时触发；该工作流位于“DocuSign 回传”和“赢单”之间 [[1]](#sources)。
2. 动手构建之前，先坐在合同校验专员身边，记录下他们的每项检查和每个升级的原因，以此把手动检查文档化；并把标准定为“准确优先于速度” [[1]](#sources)。
3. 视觉模型读取已签 PDF，识别签名和缩写签名 [[1]](#sources)。
4. 推理模型将合同与 Salesforce 记录交叉核对：签署人权限、对照报价的价格和 ACV、必备的缩写签名和条款 [[1]](#sources)。
5. 🛑 **接手**：智能体只要有任何疑问，交易就转给交易支持台专员；专员只处理可能有问题的交易 [[1]](#sources)。
6. 无误的合同直接通过：由独立的中间件层把字段写回 Salesforce，供财务和法务使用，并保留审计轨迹，采用与人工相同的基于 Okta 的权限和审批路径 [[1]](#sources)。

**产出：** 一条带审计轨迹、已校验的 Salesforce 赢单记录；异常留在专员的队列中。
**失败模式 → 防护：** 无效合同（签署人错误、价格不符、缺少缩写签名）被当作赢单放行 → 任何疑问都升级给人，编排和审计放在确定性的中间件中，与模型的校验逻辑分开。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Henry Schuck / ZoomInfo, In Q4, we built an AI agent to replace our Deal Desk](https://www.linkedin.com/posts/hschuck_in-q4-we-built-an-ai-agent-to-replace-our-activity-7419740825846194176-3GNa) (2026-01-21)。ZoomInfo 的交易支持台智能体每年校验约 100,000 笔已签合同；专员只处理异常。"~85% of signed contract validations are now fully automated". *第一手：是；可信度：高。*
