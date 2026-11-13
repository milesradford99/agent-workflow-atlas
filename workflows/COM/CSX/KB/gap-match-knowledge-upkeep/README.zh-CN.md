---
id: AWF-0048
name: 缺口匹配知识库维护
summary: "把已解决工单归类，判断新建、更新或跳过并起草知识库文章；编辑或专家审核，产品负责人签发。"
deliverable: 知识库文章草稿
shape: "导入已解决工单 → 结构化 + 聚类 → 与现有知识库匹配 → 新建 | 更新 | 跳过 → 🛑 plan → 收集来源 + 完整度评分 → 起草（风格指南 + 模板）→ 🛑 review (编辑/专家) → 🛑 sign-off (产品负责人) → 逐篇发布"
source_hash: 51c5a2e9f880
---

# 缺口匹配知识库维护

**与相近工作流的区别：** AWF-0018 聚类—简报—起草（Cluster-brief-draft）把搜索关键词聚类成用于获客的 SEO 文章。本工作流由已解决工单驱动，把每个聚类分流为新建、更新或跳过，并以专家验证为关口。
**工具变体：** `microsoft-ai-for-knowledge-management` · `supabase-gemini-webflow`

## 步骤

1. 导入已解决的工单。AI 富化环节把杂乱的备注整理成结构化字段，例如报告的问题与实际问题、修复步骤 [[1]](#sources)。
2. 对工单聚类，让反复出现的问题浮现出来，把一次性的个案排除在外 [[1]](#sources)。
3. 把每个聚类的解决方案与现有文章对照评分并分流：匹配度低于 40%，新建文章；40% 到 80%，更新现有文章；高于 80%，不做改动 [[1]](#sources)。
4. 🛑 **计划**：由人批准哪些候选项继续推进。在一次运行中，AI 分流的准确率约为 90%，其余由这道关口拦下 [[2]](#sources)。
5. 每篇文章收集 5–6 个来源，起草前先给完整度评分（完整 / 部分 / 需要与产品经理通话）。然后对照风格指南、组件库和模板起草 [[2]](#sources)。
6. 🛑 **审阅**：编辑或领域专家检查准确性并补充细节。专家的反馈同时用于调优模型 [[1]](#sources)[[2]](#sources)。
7. 🛑 **签发**：产品经理批准。这在实践中是最慢的一步，需要 3–5 天 [[2]](#sources)。只发布单篇，绝不整站发布，并把链接回贴到工单 [[2]](#sources)。

**产出：** 新建和更新后的帮助中心文章，位于 CMS 中，每篇都能追溯到来源工单。对现有文章的更新会通知其负责人。
**失败模式 → 防护：** 工单上下文单薄时起草，会编出不存在的步骤 → 先给来源的完整度评分，把薄弱的候选项交给人工通话 [[2]](#sources)。一次性的修复弄乱知识库 → 起草前要求先形成聚类 [[1]](#sources)。整站发布会泄漏预发布内容 → 逐篇发布 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Microsoft Inside Track, AI for Knowledge Management](https://www.microsoft.com/insidetrack/blog/ai-for-knowledge-management-keeping-support-content-up-to-date-at-microsoft/) (2026-07-16)。Global Help Desk 把工单聚类分流为新建/更新/不改动；专家通过邮件验证。"projects the solution will save them an estimated 16,000 hours annually"。*第一手：是；可信度：高。*
