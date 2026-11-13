---
id: AWF-0197
name: 按用户旅程审计文档
summary: "沿每条端到端用户旅程审计文档，并按产品线提交修复 PR；产品负责人确认事实并签字。"
deliverable: 经审计的文档修复 PR
shape: "挑选端到端集成旅程 → 每个旅程：智能体把该旅程涉及的所有文档作为一个整体阅读 → 记录问题(类型错误|缺失|位置不当，描述，文件+行号) → 智能体修复能修的问题并逐条记录结果 → 按产品线拆成每条产品线一个 PR → 🛑 review (产品负责人确认事实) → 🛑 sign-off → 部署 → 无法解决的问题转交产品/平台团队"
source_hash: 0917fe8e9000
---

# 按用户旅程审计文档

**与相近工作流的区别：** 最接近的是 AWF-0075（代码 PR 文档草稿）和 AWF-0135（发布周期文档技能）。两者都由代码变更或发布触发，为新变更起草文档更新。本工作流则是沿用户旅程，对现有文档整体做一次性或周期性审计。交付物是问题清单加按产品线拆分的修复 PR，由产品负责人审阅，而不是代码作者或文档团队。
**工具变体：** `markdown-docs-as-code` · `github-prs`

## 步骤

1. 使用各产品线已写好的客户视角集成场景。开发者实际走通的一条旅程（例如 FairPlay 证书 → 打包 → iOS 播放）就是一个审计单元 [[1]](#sources)。
2. 智能体把该旅程涉及的每份文档的 Markdown 源文件作为一个整体来读，寻找单个页面看不出的问题，例如文档之间的衔接不一致，或某个前置条件被埋在另一个产品的指南里 [[1]](#sources)。
3. 为每个问题记录类型（错误、缺失或位置不当）、描述以及源文件和行号。这份清单成为基线和工作日志 [[1]](#sources)。
4. 智能体通过编辑源文件修复能修的条目，并在每条旁边的备注列写下检查和修改的内容 [[1]](#sources)。
5. 由人把修复按产品线拆成每条产品线一个 PR（三个主要产品），让每位审阅人只看到自己产品的改动 [[1]](#sources)。
6. 🛑 **审阅**：各产品线的产品负责人逐行审阅自己的 PR，确认每一条事实是否正确 [[1]](#sources)。
7. 🛑 **签发**：所有产品负责人确认后，团队部署到生产环境 [[1]](#sources)。
8. 答案在文档里根本找不到的问题（推荐的 API 行为、合同约定值、控制台标签）会卡在其他团队那里。把它们转交给产品、平台或业务相关方 [[1]](#sources)。

**产出：** 已上线的更正后文档，加一份问题清单；未决事项转给必须裁定事实的团队。
**失败模式 → 防护：** 一个混合的大 PR 容易被草草放行 → 按产品线拆分 PR，各配自己的产品负责人 [1]。智能体无法凭空编造文档里没有的事实 → 标记为受阻并转交，不让它猜 [1]。逐页审计会漏掉跨文档的缺口 → 按旅程审计 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [DoveRunner (Daniel Kim), Auditing and Fixing Documentation Content with an AI Agent](https://doverunner.com/blogs/auditing-documentation-with-ai-agents/) (2026-08-03)。按旅程审计六条产品线；发现 71 个问题；每个产品的 PR 由产品负责人审阅；9 个问题卡在其他团队。"Across six product lines, this stage produced 71 content issues"; "Fixed | 59"; "Blocked on another team | 9"。*第一手：是；可信度：高。*
- [Biel.ai (David Garcia), Our AI teammate keeps our docs up to date](https://blog.techdocs.studio/p/our-ai-teammate-keeps-our-docs-up) (2026-10-08)。每周对照代码库复查文档，每次覆盖新的范围；发现以 PR 形式交给写作者审阅。"Nova also reviews the codebase against the documentation once a week"（未给出数量）。*第一手：是；可信度：中。*
