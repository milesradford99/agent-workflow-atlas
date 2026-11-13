---
id: AWF-0038
name: 对照底稿的月结智能体
summary: "参照上月底稿准备月结底稿、草拟分录与波动分析；财务主管全面复核并签核关账。"
deliverable: 已关账期间的底稿
shape: "上月底稿 + 规则 → 每个关账领域：提取源数据 → 准备底稿 + 检查 → 草拟分录 + 波动分析 → 标出异常 → 🛑 review (财务主管复核全部内容) → 锁账 → 🛑 sign-off (关账)"
source_hash: eb6b10145e30
---

# 对照底稿的月结智能体

**与相近工作流的区别：** AWF-0022 发票提取、匹配与分流（Invoice extract-match-route，AP）处理单张发票。本工作流产出跨多个科目的期末底稿和会计分录，并由财务主管对关账签发。
**工具变体：** `promptql` · `puzzle-ai-close`

## 步骤

1. 给每个智能体提供上月的底稿（“match this”）和会计人员设定的规则 [[1]](#sources)[[2]](#sources)。
2. 交易匹配全月持续运行。到关账时，由不同的智能体分别处理应计费用、租赁、固定资产、应交税费、预付款、对账、工资、分摊、财务报表和损益波动分析。每个都有自己的源数据、底稿、检查、会计分录和复核点 [[1]](#sources)。
3. 智能体准备底稿，并标出任何看起来不对的地方。AI 匹配银行流水项，人只复核异常项 [[1]](#sources)[[2]](#sources)。
4. 🛑 **审阅**：财务主管补充背景信息、做出判断，并在关账前复核全部内容 [[1]](#sources)。
5. 🛑 **签发**：在 AI 标出异常之后，对关账签发 [[2]](#sources)。

**产出：** 一个已关账的期间，每个领域都有完整的底稿和会计分录，经财务主管复核，可用于报告和审计。
**失败模式 → 防护：** 工资时间差异仍需人去追查 → 由人处理异常 [[1]](#sources)。智能体拥有银行权限 → 有意不授予 [[1]](#sources)。糟糕的自动化会放大错误 → 由会计人员设定规则，AI 负责执行 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [David Kats, PromptQL close agents](https://www.linkedin.com/posts/katsdavid_three-months-ago-i-handed-promptql-a-prior-activity-7498398271866880000-EiIe) (2026-08-26)。助理财务主管运行按领域划分的关账智能体，并在关账前复核全部输出。"Now I have 17 agents running different pieces of finance."。*第一手：是；可信度：中。*
- [Puzzle, Debit & Co.](https://puzzle.io/case-studies/debit-co) (n.d.)。一家记账公司在多个客户的关账中使用 AI 匹配加人工异常复核。"15 / 15 Clients closed by Day 4"。*第一手：厂商；可信度：中。*
