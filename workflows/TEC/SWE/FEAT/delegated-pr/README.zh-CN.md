---
id: AWF-0003
name: 委派式 PR 开发
summary: "将打好标签的议题实现为草稿 PR；CI 运行需人工批准，PR 由人评审并合并。"
deliverable: 拉取请求（PR）
shape: "🛑 plan (为适合的议题打标签) → 智能体读取议题和仓库 → (写代码 ⟲ 测试) → 草稿 PR → (机器人评审 ⟲ 修复) → 🛑 action (运行 CI) → 🛑 review → 合并"
source_hash: 45fe604d0ca7
---

# 委派式 PR 开发

**与先审计划再开发（Plan-gated build）的区别：** 运行中途没有计划检查点；议题本身就是计划，智能体在云端运行。
**工具变体：** `claude-code` 套件 · `copilot-coding-agent` · `claude-code-action` · `codex-cloud` · `devin` · `jules`

## 步骤

1. 🛑 **计划**：只有自包含、可测试的议题才会被标记给智能体处理。
2. 通过把议题指派给 Copilot 来派发，它会创建草稿 PR，并在由 `.github/workflows/copilot-setup-steps.yml` 配置的、基于 Actions 的环境中运行 [[4]](#sources)。或者评论 `@claude`，触发 Claude Code GitHub Actions [[3]](#sources)。
3. 智能体实现功能、运行测试并推送。后续指令通过 PR 评论给出，因为 Copilot 看不到指派之后新增的议题评论 [[4]](#sources)。
4. 评审机器人留下评论，智能体据此修改，进行 1–2 轮。
5. 🛑 **操作**：由人点击 “Approve and run workflows”，让 CI 在智能体的 PR 上运行 [[4]](#sources)。
6. 🛑 **审阅**：人工评审并合并。

**产出：** 已合并的 PR。按议题标签统计合并率，据此调整哪些议题可以派发。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Charas & Bruggmann, Spotify Engineering](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) (2025-11-06)。在容器中做批量迁移，并用 LLM 评判；由各团队评审 PR。"merged more than 1500 pull requests"；"60–90%" 的时间节省。*第一手：是；可信度：高。*
- [Stephen Toub, .NET Blog](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/) (2026-03-23)。维护者指派议题 → 智能体提 PR → 机器人评审 → 由人引导并合并。"all 878 CCA PRs"；"67.9% success rate"；"3 were reverted (0.6%)"。*第一手：是；可信度：高。*
