---
id: AWF-0166
name: 挑战者代理投委会备忘录
summary: "分析代理起草投资备忘录，挑战者代理提出质疑；交易团队修订，投委会决策。"
deliverable: 投资委员会备忘录
shape: "交易文件 + 尽职调查问题 → 分析代理起草投委会备忘录 → 投委会代理提出质疑（行业动态、商业模式、基于本机构历史交易的风险因素） → 🛑 review (交易团队权衡质疑并补充自己的风险判断) → (重新起草 ⟲ 🛑 review) → 🛑 sign-off (投资委员会决策)"
source_hash: 142cfed23497
---

# 挑战者代理投委会备忘录

**与相近工作流的区别：** AWF-0098 核保人定稿的信贷备忘录：一次起草由核保人修改，然后进入银行信贷审批。本工作流中，在人审阅之前，另一个 AI「挑战者」代理先对草稿提出质疑，重新起草的循环在团队审阅下反复进行。交付物是股权投资委员会备忘录，而不是信贷备忘录。
**工具变体：** `schroders-gaiia` · `v7-go`

## 步骤

1. 分析代理（GAiiA）在直接投资和联合投资的尽职调查中筛查大量交易数据，回答投资相关的具体问题，并起草投资委员会备忘录的初稿 [[1]](#sources)。
2. 一个独立的虚拟投资委员会代理审阅草稿，基于本机构的历史投资数据，补充行业动态、商业模式考量和风险因素方面的意见 [[1]](#sources)。
3. 🛑 **审阅**：投资团队成员评估并扩展投委会代理的反馈，加入自己对风险和机会的判断，并可要求分析代理给出改进版本 [[1]](#sources)。
4. 每次重新起草后，都再次交给投资团队 🛑 **审阅**，之后文件才定稿 [[1]](#sources)。
5. 🛑 **签发**：每一项投资决策都只由投资专业人员作出 [[1]](#sources)。一个风险投资（VC）变体：把整个数据室丢进工具，得到按机构模板生成、每条论断都链接到来源的备忘录，由团队核对 [[2]](#sources)。

**产出：** 以机构自有格式定稿的投资委员会备忘录，交付投资决策。
**失败模式 → 防护：** 草稿照搬标的公司自己的宣传 → 设置独立的挑战者代理，以本机构过往交易为依据。编造的数字进入投委会 → 论断链接到来源，由分析师核对 [2]。过度依赖 AI 的观点 → 专业人员对最终文件和决策负全部责任 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点位置不同。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Schroders Capital, virtual investment committee agent](https://schroders-capital.prezly.com/schroders-capital-expands-pioneering-ai-toolkit-with-virtual-investment-committee-agent) (2025-06-30)。私募市场机构自己的分析代理加挑战者投委会代理；每个版本都由人审阅。"GAiiA has already assisted with more than 40 investment cases"。*第一手：是；可信度：中。*
- [V7 Labs, Moderne Ventures](https://www.v7labs.com/news/moderne-ventures-accelerates-due-diligence-with-v7-go) (n.d.)。风险投资机构把数据室变成按模板生成、引用来源的备忘录，由合伙人核对。"makes the process go from weeks to a day"。*第一手：厂商；可信度：中。*
