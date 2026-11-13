---
id: AWF-0071
name: 先复现再修复的缺陷处理
summary: "先复现缺陷，再提交修复 PR 和回归测试 PR；无法复现的转人工，合并前由工程师评审。"
deliverable: 经验证的修复 PR
shape: "缺陷工单 → 复现（基线运行）+ 诊断 → 未复现：🛑 handoff | 已复现：在隔离的 worktree 中修复 → (修复 ⟲ 在 staging 重跑同一复现) → 开修复 PR + 回归测试 PR → 按 git blame 选审阅人 → 🛑 review → 合并"
source_hash: 6e689f3f831b
---

# 先复现再修复的缺陷处理

**与相近工作流的区别：** AWF-0003 委派式 PR 从带标签的 issue 出发，以现有测试为关卡。本工作流从原始缺陷报告出发，增加了“先复现，否则搁置”的关卡和对同一复现的修复前后对比，并交付一个新的回归测试。AWF-0004 先分诊再修复通过运维手册处理线上事故，而不是修改代码。
**工具变体：** `claude-code` · `block-moneybot-autoheal` · `sentry-seer-cursor-agents` · `claude-agent-sdk-str-fix` · `claude-routines`

## 步骤

1. 从工单系统接收已上报的生产问题 [[1]](#sources)（或未解决的 Sentry issue 分组，合并时采取保守策略 [[2]](#sources)）。
2. 先复现：把失败的会话变成可回放的测试或评测用例，使用合成数据，并运行 10 次作为基线（只失败过一次的运行 20 次）。随时间变化的状态用 fixture 固定 [[1]](#sources)。与此同时，诊断器写出发生了什么、一个可行的修复方案以及长期的理想方案 [[1]](#sources)。
3. 🛑 **接手**：如果故障始终无法复现，就停下来，把工单标为无法复现并搁置，交给人处理。绝不修复无法观察到的行为 [[1]](#sources)。
4. 在隔离的 git worktree 中修复，然后部署到一次性的 staging 环境，用相同的样本量重跑同一个复现。只有相对基线明显改善才接受，并将循环次数限制在有限轮内 [[1]](#sources)。在运行中的应用里做端到端 UI 验证，做法与此相同 [[2]](#sources)。
5. 开两个 PR：修复，以及把复现作为永久的回归测试。按 git blame 选审阅人，并把结果（包括失败的尝试）写回工单 [[1]](#sources)。
6. 🛑 **审阅**：工程师评审变更并决定哪些上线。合并和关闭工单仍由人来操作 [[1]](#sources)。智能体的 PR 先通过 CI 和机器人评审，再到预生产环境交由人做最终评审 [[2]](#sources)。

**产出：** 一个已合并的修复，加上由真实故障构建的回归测试；工单更新为处理结果，或搁置交给人。
**失败模式 → 防护：** 不稳定或非确定性的缺陷在通过一次运行后看似已修复 → 重复采样，并对比修复前后相同的样本量 [[1]](#sources)。对报告中的确切措辞过拟合 → 增加一个措辞不同的参考性第二用例 [[1]](#sources)。无限循环 → 设置上限，不可逆的操作由人掌握 [[1]](#sources)。修复忽略仓库规范 → 编码前增加一个功能调研步骤 [[3]](#sources)。

**近期实践（2026）：**
- 审阅人步骤：一个无人值守的例行任务按计划运行，取出最近四小时内无人处理的修复 PR，找到与根因代码接触最多的工程师，确认 PR 仍处于打开状态，然后提醒他合并或关闭、给出一句反馈，并说明这个修复是否值得用智能体来做。它从不重复发帖，也避免在周末发提醒（Sentry）。[[4]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例补充于 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Block, Autohealing Moneybot](https://engineering.block.xyz/blog/autohealing-moneybot) (2026-08-28)。6 个子智能体负责复现、诊断、修复，并在 staging 中验证，然后提交修复 PR 和评测 PR 交由人评审。"more than 40 verified fixes"。*第一手：是；可信度：高。*
- [Cyclotron, Closed-Loop Engineering System](https://cyclotron.com/post/how-i-built-a-closed-loop-engineering-system-that-saved-840-hours-in-30-days/) (2026)。Sentry issue → Cursor 智能体复现、修复、端到端验证 → PR → 在预生产环境由人评审。共开出 472 个智能体 PR，合并 410 个（"86.9% merge rate"）。*第一手：厂商（作者在公司自己的产品上运行）；可信度：中。*
- [Duolingo, AI bug-fixing agent](https://blog.duolingo.com/ai-bug-fixing-agent/) (2026-11-04)。摇一摇上报的 Jira 工单 → 上下文、复现步骤、修复、自我评审、CI 修复、供验证的 beta 构建。*第一手：是；可信度：中。*
- [Sentry, How we built an automated debugging workflow at Sentry](https://blog.sentry.io/automated-debugging-workflow-sentry/) (2026-08-06)。Seer autofix 提交 PR；每小时运行的例行任务根据提交历史选出审阅人，并提醒其合并或关闭。"About a 21% increase in the action rate on PRs"。*第一手：厂商；可信度：中。*
