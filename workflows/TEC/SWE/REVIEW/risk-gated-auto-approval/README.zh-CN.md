---
id: AWF-0182
name: 按风险自动批准 PR
summary: "通过确定性资格检查的低风险 PR 由智能体批准，其余转交人工评审。"
deliverable: PR 批准决定
shape: "PR 打开 → 确定性资格检查（仓库路径策略、大小、基础分支、标签）→ 智能体：读取文件 + 检查依赖、开关、日志、工单 → 提交 approve | skip → approve：机器人批准，任何不可批准的文件都会阻止 → 🛑 action (作者合并，观察发布) | skip：🛑 review (人工评审者) → 错误批准：修正提示词 + 在过往 PR 上回测"
source_hash: a699105b0432
---

# 按风险自动批准 PR

**与相近工作流的区别：** AWF-0070 分级 PR 评论（Graded PR comments）和 AWF-0133 评论转编辑建议（Comment-to-edit suggestions）都是添加评论，每个 PR 仍由人批准。这里智能体的输出就是批准决定本身，低风险 PR 不需要人工评审者参与。自主程度和检查点安排都发生了变化。
**工具变体：** `custom-harness` · `aws-bedrock` · `claude`

## 步骤

1. 先过确定性门槛。每个仓库一份策略文件，把路径通配符映射到标记为可批准或不可批准的类别（CI、CODEOWNERS、Terraform、认证和迁移必须由人处理）。其他设置涵盖草稿、标签、堆叠 PR 以及改动行数上限 [[1]](#sources)。
2. 智能体用一组固定的、基于 API 的工具进行评审，没有 shell，也不检出代码：读取该提交处的文件、检查依赖（漏洞、仿冒包名、存续时间）、工单上下文、日志/指标、跨仓库搜索以及在线功能开关状态。PR 内容被当作数据，而不是指令 [[1]](#sources)。
3. 结论是一次有 schema 的 `submit_review` 工具调用（approve 或 skip，附理由）。没有结论或工具预算耗尽，都视为 skip。最后一道确定性检查会在任何文件不可批准时拒绝批准 [[1]](#sources)。
4. 变体：独立的子智能体各自从一个角度评审（问题陈述、意图与 diff、安全、逻辑、最佳实践），过大的 PR 会被拒绝，让作者拆分 [[2]](#sources)。
5. 🛑 **操作**：获批后由作者合并并继续负责。他们观察变更上线，必要时回滚。任何工程师都可以对任何变更请求人工评审 [[2]](#sources)。
6. 🛑 **审阅**：被跳过的 PR 交给人工评审者 [[1]](#sources)。
7. 每个结论连同其推理、读取过的文件和每次工具调用，发布在一条锚定评论中。AI 批准的 PR 带有标签，被记录且可供审计查询 [[1]](#sources)[[2]](#sources)。
8. 基于已标注的过往 PR 的评测为每次提示词改动把关。一次错误批准会成为一个回测用例 [[1]](#sources)。

**产出：** 每个 PR 都有一个批准（或转交人工的跳过）决定，附可审计的推理评论。低风险 PR 无需人工评审即可合并。
**失败模式 → 防护：** 机器人跳过了需要的工具，批准了引发 bug 的 PR → 修正提示词，并在包括那次错误批准在内的过往 PR 上回测 [1]。作者钻空子 → 客观的确定性门槛。在量大时走过场 → 智能体拒绝过大的 PR [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Clipboard, Preflight: Automating Approvals for 28% of Our PRs](https://www.clipboard.com/resources/blog/preflight-automating-approvals-for-28-of-our-prs) (2026-10-12)。Webhook 机器人批准或跳过每个 PR；低风险 PR 的合并中位时间大幅缩短。"the median time to merge of low-risk PRs is down to 1.2h"。*第一手：是；可信度：高。*
- [Intercom, AI is approving our pull requests](https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe) (2026-04-21)。先试点再推广的子智能体评审，无需人工评审者即可批准 PR。"In the first four weeks of broader rollout, 497 PRs went fully autonomous"。*第一手：是；可信度：高。*
