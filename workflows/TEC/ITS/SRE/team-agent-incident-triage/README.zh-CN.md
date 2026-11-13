---
id: AWF-0230
name: 团队智能体事件分诊
summary: "依据历史事件和排障指南判断团队队列中的事件是否归本团队；工程师审阅每个接收决定。"
deliverable: 事件归属决定
shape: "事件进入团队队列 → 提炼事件语义 → 检索相似历史事件和团队 TSG → 决定本团队接收或拒绝 → 接收：给出理由 → 🛑 handoff (工程师审阅) | 拒绝：退回上一个团队 / 转给 TSG 指明的团队 / 留在队列等工程师处理"
source_hash: 1c6deee8653c
---

# 团队智能体事件分诊

**与相近工作流的区别：** 最接近的是 AWF-0004 先分诊后修复（Triage then remediate）：该工作流调查信号，并在 🛑 action 之后执行运行手册（runbook）操作。本工作流只产出归属决定（接收或改派），不执行任何修复操作，并且智能体改派时无需逐条审批。它也不同于 AWF-0127（在 NOC 工单中标注根因）和 AWF-0185（作战室协调与复盘）：这两者都不决定事件归哪个团队。
**工具变体：** `azure-openai` · `gpt-embeddings`

## 步骤

1. 每个服务团队配一个智能体，代表团队的工程师。它把团队的历史事件和排障指南（TSG）作为领域知识 [[1]](#sources)。
2. 事件进入团队队列后，智能体用 GPT embeddings 和“语义提炼”（semantic distillation）抽出事件中与分诊相关的信息 [[1]](#sources)。
3. 智能体把事件与历史事件和团队的 TSG 对比，然后做二选一的决定：为本团队接收该事件，或拒绝，并给出理由 [[1]](#sources)。
4. 被接收的事件：智能体附上理由。🛑 **接手**：团队中的一位工程师（指定的责任人）审阅该事件并接手 [[1]](#sources)。
5. 被拒绝的事件：智能体把事件退回上一个团队，转给其 TSG 指明的团队，或留在队列里由工程师处理。每次改派无需人逐一批准 [[1]](#sources)。
6. 建设中：全局分诊层（Global Triage），由多智能体编排器挑选候选团队，并与各团队的智能体协商，找出合适的负责方 [[1]](#sources)。团队逐个接入，每个团队带来自己的 TSG 和事件历史 [[1]](#sources)。

**产出：** 对每个新事件给出接收或改派的决定及理由，让事件更快到达负责团队的值班工程师手中，再由该工程师缓解。
**失败模式 → 防护：** 智能体误拒并退回事件，造成多余的重新分派，拉长缓解时间 → 智能体可以把事件留在队列里交给工程师，并为每个决定给出理由。TSG 过时或缺失会削弱决定质量 → 智能体基于各团队的 TSG 和历史事件训练，团队逐个接入。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Microsoft Azure, Optimizing incident management with AIOps using the Triangle System](https://azure.microsoft.com/en-us/blog/optimizing-incident-management-with-aiops-using-the-triangle-system/) (2025-03-06)。自 2024 年中起在 Azure 生产环境运行的按团队分诊智能体；6 个团队已上线，15 个以上正在接入。"agents achieving 90% accuracy and one team saw a reduction in their TTM of 38%"。*第一手：是；可信度：高。*
