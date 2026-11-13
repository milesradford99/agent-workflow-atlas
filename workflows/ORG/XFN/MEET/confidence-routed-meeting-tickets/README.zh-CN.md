---
id: AWF-0208
name: 按置信度分流的会议工单
summary: "把会议待办转为信息完整的跟踪工单；明确的直接创建，模糊的等待 Slack 审批。"
deliverable: 跟踪系统工单
shape: "huddle 结束，转写稿发布 → 跳过 3 分钟以内的 huddle → 提取待办（负责人置信度、截止时间、原文引句） → 每个待办：搜索代码和已有工单 → 信息完整的工单（验收标准、链接、估时） → 负责人和承诺都明确：在 Jira 中创建 | 模糊：🛑 action (Slack 审批：创建、分配给我、修改、丢弃) → 跟踪已创建工单的修改 → 大幅改写：🛑 review (优化提示词) → 更新 few-shot 示例"
source_hash: aad3c0f1cdeb
---

# 按置信度分流的会议工单

**与相近工作流的区别：** 最接近的是 AWF-0086（模板驱动的会议纪要）：它产出的纪要由人在传阅前修正。本工作流的交付物是直接写进跟踪系统的工单。智能体自己创建有把握的条目，人只处理模糊的约 15%，以及被大幅修改的工单。
**工具变体：** `n8n` · `jira` · `slack-huddles` · `granola`

## 步骤

1. 当 Slack huddle 的转写稿发布到指定频道时，触发一个 n8n 工作流；3 分钟以内的 huddle 会被跳过，发言轮次会被合并，并拉取团队名单用于姓名解析 [[1]](#sources)。
2. 带有团队专属 few-shot 示例的 LLM 把具体的待办提取成结构化字段：带置信度的负责人（明确、隐含、未分配）、截止时间和紧急程度、依赖、类型，以及转写稿中的原文片段 [[1]](#sources)。
3. 对每个条目，流水线搜索代码库和已有工单，生成信息完整的 Jira 工单：摘要、描述、3-5 条验收标准、技术说明、相关文件和工单、标签、故事点 [[1]](#sources)。
4. 🛑 **操作**：模糊的提取结果（负责人不明、时间含糊）不直接创建，而是发到 Slack 审批卡片，可选择原样创建、分配给我、修改或丢弃；这一步能拦下约 15% 的提取结果 [[1]](#sources)。有把握的条目直接在 Jira 中创建。
5. 🛑 **审阅**：流水线把已创建的工单与其后来被编辑的状态做对比；大幅改写会触发 Slack 通知，提示审阅提示词，few-shot 示例则每季度根据失败案例更新 [[1]](#sources)。

**产出：** 链接到会议片段和相关代码的 Jira 工单，以及一个等待审批的模糊条目队列。
**失败模式 → 防护：** 含糊的闲聊（“我们大概应该……”）产生幽灵任务 → 用 few-shot 示例把这类话标为非待办，低置信度条目走 Slack 审批 [1]。负责人错误 → 设负责人置信度字段，未分配的条目进入审批 [1]。质量漂移 → 用编辑距离做反馈闭环 [1]。希望每张工单都经过审阅的团队使用辅助版本（RADAR：创建任何工单前先审阅、编辑、选择）[2]。

## 公开实例

覆盖度（截至 2026-11-13）：**部分**：第一手实例只覆盖流程的一部分，或把检查点放在别处。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Amandeep Singh, Meeting-to-Task Pipeline](https://asinghm.com/blog/ai-meeting-transcript-to-jira-tickets-pipeline) (2025-12-17)。在一个工程团队投产四个月；对模糊条目设有审批流程。"Our ticket creation rate from meetings went from 42% to 91%"。*第一手：是；可信度：中。*
- [Built This Week, RADAR](https://www.builtthisweek.com/builds/radar-meeting-transcripts-to-jira-tickets) (2026-10-31)。技术项目经理（TPM）的内部应用：把 Granola 站会转写稿转成建议的 Jira 工单，创建前先审阅。"He said it took a job that used to take four hours down to minutes."。*第一手：访谈；可信度：中。*
