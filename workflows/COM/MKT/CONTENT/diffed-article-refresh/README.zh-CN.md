---
id: AWF-0224
name: 带对比的文章更新
summary: "调研并起草已发布文章的更新稿，以对比 diff 呈现；编辑检查 diff 后才发布。"
deliverable: 带 diff 的更新版文章
shape: "文章 URL + 目标关键词 → 抓取线上文章 → SERP + 竞品调研 → 与自家文章做相似度检查 → 更新方案 → 标出过时内容 → 核对产品提及 → 起草更新 → 并排 diff → 🛑 review (编辑检查 diff 并修改) → 适配 CMS 格式 → 发布"
source_hash: 9b073f0f557b
---

# 带对比的文章更新

**与相近工作流的区别：** 最接近的是 AWF-0018 关键词簇简报起草内容，它规划关键词簇并根据简报撰写新文章（计划检查点 + 草稿审阅），只在最后的循环里提到更新旧文。本工作流的输入是一篇已经上线的文章，交付物是修订方案加 diff，没有计划检查点，编辑的审阅是基于 diff 进行的。AWF-0177（直播带货脚本）与此无关。
**工具变体：** `claude-code` · `n8n` · `rag`

## 步骤

1. 输入：已有文章的 URL 和一个目标关键词 [[1]](#sources)。Kokoc 的优化师把任务排在一张共享的 Google Sheet 里，由智能体按计划取走 [[2]](#sources)。
2. 抓取线上文章；调研 SERP 和排名靠前的竞品；对现有文章与竞品做语义相似度检查 [[1]](#sources)。
3. 综合出更新方案；找出过时内容；核对产品提及，避免草稿描述并不存在的功能 [[1]](#sources)。Kokoc 把文章与排名靠前页面的“理想结构”对比并排出修改的优先级，根据当前排名选择小改还是全面重写 [[2]](#sources)。
4. 依据风格指南和以往草稿，用原有的文风起草更新；每个技能都把输出存成文件，因此任何一步都可以重跑 [[1]](#sources)。Kokoc 的智能体还会保留内部链接、短代码和结构化数据标记，并输出可直接进 CMS 的 HTML [[2]](#sources)。
5. 生成原文与新稿的并排对比，高亮改动 [[1]](#sources)；Kokoc 的智能体会为编辑记录改了什么 [[2]](#sources)。
6. 🛑 **审阅**：文章走正常的编辑流程（审阅、修订、编辑、配图）；编辑借助 diff 对照原文，抓出编造的内容 [[1]](#sources)；Kokoc 的编辑在排版人员发布之前做最后的事实核查和验证 [[2]](#sources)。

**产出：** 一篇已有文章的更新版，加上改动 diff，经编辑签发后发布到 CMS。
**失败模式 → 防护：** 编造的产品功能细节看上去很可信 → 产品提及核对加上与原文的 diff，让这类问题一分钟就能抓出 [1]。模型改动代码、插入内容或格式 → 约束输出并保留原有区块 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Semrush, I rebuilt our content update pipeline in Claude Code](https://www.semrush.com/blog/how-i-rebuilt-our-content-update-pipeline/) (2026-06-25)。Semrush 的九技能更新流水线；编辑通过 diff 发现了一个编造的功能。"a reviewer can catch them and check in one minute instead of 20 minutes". *第一手：是；可信度：高。*
- [Kokoc.com, Как мы автоматизировали процесс обновления статей](https://kokoc.com/keysi/kak-my-avtomatizirovali-protsess-obnovleniya-statey-v-blog-s-pomoshchyu-rag-agenta/) (2026)。代理机构用智能体加编辑检查更新了其 1,200 篇博客文章中约 10% 的内容。"Затраты снизились на 80% — осталась только необходимая редакторская проверка.". *第一手：是；可信度：高。*
