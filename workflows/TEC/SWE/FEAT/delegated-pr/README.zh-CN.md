---
id: AWF-0003
name: 委派式 PR 开发
summary: "将打好标签的议题实现为草稿 PR；CI 运行需人工批准，PR 由人评审并合并。"
deliverable: 拉取请求（PR）
shape: "🛑 plan (为适合的议题打标签) → 智能体读取议题和仓库 → (写代码 ⟲ 测试) → 草稿 PR → (机器人评审 ⟲ 修复) → 🛑 action (运行 CI) → 🛑 review → 合并"
source_hash: 36be7c10c9bc
---

# 委派式 PR 开发

**工具变体：** `claude-code` 套件 · `copilot-coding-agent` · `claude-code-action` · `codex-cloud` · `devin` · `jules`

## 背景

软件团队手里总有一批描述清楚的小任务（修一个边界情况、加一个选项），却没人有空去做。在这个工作流里，维护者把这样的任务交给一个在云端运行的编码智能体，就像指派给一位同事：智能体读需求和代码，做出改动，运行测试，再以拉取请求的形式提交结果。智能体干活时没人盯着，所以人的把控放在两头。维护者挑选哪些任务适合交出去，批准在智能体的代码上运行项目的自动检查，最后评审并合并结果。这个人去不掉，因为进入共享代码的东西由维护者负责，没人读过的代码可能把缺陷或安全漏洞带进每一位用户手里。

**术语：**
- **议题（issue）**：一份书面的改动请求，存放在 GitHub Issues 之类的工单系统里。
- **标签**：议题上的标记；这里由维护者打上的标签表示该议题适合交给智能体。
- **自包含、可测试的议题**：不需要别人做决定就能完成、并且能用测试检验的任务。
- **PR（pull request，拉取请求）**：一份提议的改动，在合并进共享代码之前公开出来供评审；草稿 PR 表示尚未准备好评审。
- **CI**：每个 PR 上自动运行的检查（构建、测试、lint）。
- **GitHub Actions**：GitHub 在仓库事件发生时运行任务（例如 CI 或智能体）的系统。
- **评审机器人**：在 PR 上留评论的自动评审者。
- **合并**：把一个 PR 接受进共享代码。
- **合并率**：智能体提交的 PR 中最终被合并的比例。

## 用智能体搭建

**形态：** `service`。每次运行都由带标签议题上的一条评论启动，现场没有人，人只看到草稿 PR、它的检查结果和评审评论。[套件](variants/claude-code.md)把这套搭建方式写成了文件。

**需要：** 一个配有 CI 工作流的 GitHub 仓库；已安装 Claude GitHub App，并把 API 密钥或订阅令牌存为仓库密钥；一份 `CLAUDE.md`，写明安装、测试、lint 和类型检查命令，以及智能体不得触碰的路径，例如 `.github/`；一个带验收标准的议题模板。不要把密钥放在智能体可以编辑的文件里。

| 步骤 | 搭建方式 |
|---|---|
| 🛑 plan (为适合的议题打标签) | 由维护者手动加标签。工作流文件只在带标签的议题上、且只对所有者、成员和协作者的评论运行智能体。 |
| 智能体读取议题和仓库 → (写代码 ⟲ 测试) | 由 `@claude` 评论触发的 Claude Code GitHub Actions 在 Actions 运行器里执行，可用工具只限于读取、编辑以及测试、lint 和类型检查命令。`CLAUDE.md` 规定失败轮数的上限。 |
| 草稿 PR | 智能体推送一个分支；PR 保持草稿状态。 |
| (机器人评审 ⟲ 修复) | 由评审机器人或一条 `@claude review` 评论进行评审；智能体回应提及它的评审评论，进行一到两轮。 |
| 🛑 action (运行 CI) | 只有当人把草稿标为可以评审时，CI 工作流才运行完整检查。 |
| 🛑 review → 合并 | 由人在代码托管平台上评审 diff 和 CI 结果，然后合并。 |

**检查点：** `plan`：只有维护者能加标签，工作流的条件会跳过未加标签议题上的评论和不受信任账号的评论，所以外人的评论无法启动运行。`action`：只有人把 PR 标为就绪，完整的 CI 才会开始；用 GitHub 自家的智能体时，由人点击 “Approve and run workflows”。`review`：智能体可用的工具里没有合并命令，它的分支也从不是默认分支；由人合并。

**与来源相比：** 有日期的来源和实例出自 2025-07 到 2026-03；来源 3 是一个文档页面，于 2026-11 查阅，来源 4 中的培训页面未注明日期。来源 4 里的工具后来改了名：GitHub 2026-04 的更新日志称它为 [Copilot cloud agent, formerly Copilot coding agent](https://github.blog/changelog/2026-04-01-research-plan-and-code-with-copilot-cloud-agent)，并说它现在可以只在分支上工作而不创建 PR，也可以先给出计划，经批准后再写代码。来源 4 中的培训页面如今以 “Copilot in the cloud” 为题，仍然写明智能体看不到指派之后新增的议题评论。工具变体的标识 `copilot-coding-agent` 还在用旧名。Claude Code GitHub Actions 的文档页面仍然描述了这里用到的 `@claude` 触发方式和 `/install-github-app` 安装步骤。第 4 步没有引用来源。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 🛑 **计划**：维护者只把自包含、可测试的议题标记给智能体处理。
2. 维护者通过把议题指派给 Copilot 来派发，它会创建草稿 PR，并在由 `.github/workflows/copilot-setup-steps.yml` 配置的、基于 Actions 的环境中运行 [[4]](#sources)。或者维护者评论 `@claude`，触发 Claude Code GitHub Actions [[3]](#sources)。
3. 智能体实现功能、运行测试并推送。后续指令通过 PR 评论给出，因为 Copilot 看不到指派之后新增的议题评论 [[4]](#sources)。
4. 评审机器人留下评论，智能体据此修改，进行 1–2 轮。
5. 🛑 **操作**：由人点击 “Approve and run workflows”，让 CI 在智能体的 PR 上运行 [[4]](#sources)。
6. 🛑 **审阅**：由人评审并合并。

**产出：** 已合并的 PR。按议题标签统计合并率，据此调整哪些议题可以派发。
**与先审计划再开发（Plan-gated build）的区别：** 运行中途没有计划检查点；议题本身就是计划，智能体在云端运行。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Charas & Bruggmann, Spotify Engineering](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) (2025-11-06)。在容器中做批量迁移，并用 LLM 评判；由各团队评审 PR。"merged more than 1500 pull requests"；"60–90%" 的时间节省。*第一手：是；可信度：高。*
- [Stephen Toub, .NET Blog](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/) (2026-03-23)。维护者指派议题 → 智能体提 PR → 机器人评审 → 由人引导并合并。"all 878 CCA PRs"；"67.9% success rate"；"3 were reverted (0.6%)"。*第一手：是；可信度：高。*
