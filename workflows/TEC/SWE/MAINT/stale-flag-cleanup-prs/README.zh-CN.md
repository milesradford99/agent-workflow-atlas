---
id: AWF-0180
name: 过期开关清理 PR
summary: "清理过期功能开关背后的死代码，每个开关一个经测试的 PR；工程师确认开关取值，负责人合并。"
deliverable: 死代码清除 PR
shape: "定时任务 (每日): 过期开关工单 → 编排器: 发布状态 + 目标取值（来自平台）+ 代码引用 → 报告 → 部分发布：🛑 handoff (负责人完成发布或跳过) | 🛑 review (工程师确认目标取值) → 每个开关：(在 worktree 中编辑 ⟲ 构建 + 测试 + 补丁覆盖率 + lint)→ 向开关负责人提 PR → 🛑 review (负责人合并) → 归档开关"
source_hash: f91f6ebc2e10
---

# 过期开关清理 PR

**与相近工作流的区别：** AWF-0002 扇出式代码迁移（Fan-out codemod）在大量文件上应用同一种改写，先试点再抽检。这里的单元是开关，其目标取值来自在线平台。任何编辑之前都由人确认该取值，每位负责人拿到的是按开关拆分的 PR。AWF-0130 基于性能剖析的优化（Profile-led perf fixes）根据剖析结果瞄准热点函数。产出物和检查点安排都与这两者不同。
**工具变体：** `google-adk` · `claude-opus` · `github-copilot-agent-tasks` · `github-actions`

## 步骤

1. 每日定时任务为每个过期开关创建一张工单：90 天内未修改、代码中仍有引用、未归档、不在排除名单上。工单分配给开关的创建者 [[1]](#sources)。
2. 阶段 1：编排智能体获取工单。它通过 MCP 向实验平台查询开关的 UUID、发布百分比和目标取值，然后在仓库中搜索所有引用。它写出一份报告，提出目标取值并列出受影响的文件 [[1]](#sources)。
3. 🛑 **审阅**：工程师核对报告并确认目标取值。🛑 **接手**：部分发布（例如在 60% 时被放弃）交回给用户，由其完成发布或回滚，或跳过清理 [[1]](#sources)。
4. 阶段 2：每个已确认的开关对应一个清除智能体，各自在独立的 git worktree 中运行，每个仓库同时最多 4 个。每个智能体找出常量、封装和调用点，简化条件分支并更新测试。它循环执行，直到构建通过、测试通过、补丁覆盖率至少 95%、linter 无告警。它有 1 小时超时，检查通过前不得开 PR [[1]](#sources)。
5. 🛑 **审阅**：PR 分配给开关负责人，由其审阅并合并。在变体中，部署后开关会在开关服务中归档，工单关闭 [[1]](#sources)[[2]](#sources)。
6. 变体：资格过滤完全是确定性的（布尔开关、超过 3 个月、仍在代码中）。每个开关触发一个云端智能体任务，PR 带标签以便跟踪，由常规 CI 加必需的人工评审把关合并 [[2]](#sources)。

**产出：** 每个过期开关一个可直接合并的 PR，分配给开关负责人，随后归档该开关。
**失败模式 → 防护：** 硬编码错误的值会悄悄改变行为 → 在线发布状态取自平台而不是代码，并由人确认。调用链深处清除不彻底 → 覆盖率和 linter 检查，然后重新提示。50 次运行中的 5 次人工干预全都是调用链深度问题，而不是 bug。机器人 PR 默认不跑 CI → 手动批准 CI 运行 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [DoorDash, Automating Feature-Flag Cleanup at Scale with a Multi-Agent LLM System](https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/) (2026-08-24)。处理最近的 50 个过期开关；并行清理智能体之前有一个人工检查点。"produced usable PRs for 45 of them at an average cost of $4.79 and 13.8 minutes per flag"。*第一手：是；可信度：高。*
- [Glovo, How We Use AI to Keep Feature Flags Under Control](https://tech-blog.glovoapp.com/blog/how-we-use-ai-to-keep-feature-flags-under-control/) (2025-12-10)。GitHub Actions 工作流为每个符合条件的开关触发一个 Copilot 智能体任务；必须经人工评审。"600+ feature flags older than a year"。*第一手：是；可信度：中。*
