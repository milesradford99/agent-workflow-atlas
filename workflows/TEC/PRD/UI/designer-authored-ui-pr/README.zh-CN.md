---
id: AWF-0231
name: 设计师提交的 UI PR
summary: "设计师借助智能体在产品代码库中改 UI 并提交 PR；每个 PR 合并前都由工程团队审阅。"
deliverable: 已合并的 UI pull request
shape: "想法或 Figma 草图 → 设计师在产品代码库中向接入仓库的智能体下达提示词 → (调整样式、行为、布局 ⟲ 在运行中的应用里预览) → 提交附背景说明和文档的 PR → linter、CI、测试、预览应用 → 🛑 review (工程团队审阅每个 PR) → 合并 | 关闭并记录经验"
source_hash: ef0a08104520
---

# 设计师提交的 UI PR

**与相近工作流的区别：** 最接近的是 AWF-0062 依规格出界面方案（Spec-bound screen options）：那里的交付物是 Figma 工作文件中的高保真设计，由设计师审阅。本工作流的交付物是上线的代码，关卡是工程团队的 PR 审阅。AWF-0121 是针对工程师 PR 的无障碍审阅与修复智能体：交付物不同，并且转给无障碍团队处理。
**工具变体：** `cursor` · `claude-code`

## 步骤

1. 产品设计师从 Figma 中的想法或勾勒的交互模式出发。他们不写规格说明，而是打开带仓库集成助手（Cursor 或 Claude Code）的代码编辑器，用提示词让它在真实的产品代码库里构建这个体验 [[1]](#sources)。
2. 设计师在代码库内调整样式、修改行为、尝试布局，并在运行中的应用里预览每处改动。工作在带预览环境的专用功能分支上进行 [[1]](#sources)。
3. 对于前瞻性工作或大型交互探索，设计师会有意先在仓库之外做一个一次性原型，比较方案，判断这个想法是否值得完整实现 [[1]](#sources)。
4. 满意后，设计师提交一个带背景说明和文档的 pull request。防护措施（linter、CI、预览应用、自动化测试、必需的审阅）随之运行 [[1]](#sources)。
5. 🛑 **审阅**：工程团队按与其他代码相同的评审流程，审阅每一份设计师的贡献，看质量和一致性。常见的驳回原因有偏离设计系统、性能或无障碍缺口、可维护性问题 [[1]](#sources)。
6. 合并的 PR 上线。关闭的 PR 把经验带入下一轮。只改前端的变更最容易落地，复杂功能则与工程师结对完成 [[1]](#sources)。

**产出：** 一个由设计师编写、合入生产代码的前端 pull request，无需 Figma 到工程的交接。
**失败模式 → 防护：** PR 偏离设计系统、留下性能或无障碍缺口，或触及跨领域架构和临时状态 → 必需的工程审阅，加上 linter、CI、预览应用和测试。约 30% 的 PR 未合并即被关闭。涉及后端的改动落地效果差 → 设计师的 PR 只限前端，复杂功能与工程师结对。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Plotly, How Plotly Designers Build Beyond Figma Mockups With AI](https://plotly.com/blog/plotly-designers-build-beyond-figma-mockups-ai/) (2025-08-25)。Plotly 的设计师提交的代码 PR 经工程审阅后上线；给出合并率和 PR 占比。"designers have successfully merged approximately 70% of their PRs, with about 30% closed without merging"; "roughly 20% of total PRs in our main application now come from designers"。*第一手：是；可信度：高。*
