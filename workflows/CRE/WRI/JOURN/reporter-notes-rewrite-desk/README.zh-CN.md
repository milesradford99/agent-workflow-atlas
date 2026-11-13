---
id: AWF-0074
name: 记者笔记改写台
summary: "根据记者笔记起草新闻稿；改写编辑审核，记者终读后发布。"
deliverable: 已发布的新闻报道
shape: "记者采集并录入笔记和引语 → 改写编辑给 AI 下提示词起草稿件 → 🛑 review (改写编辑) → 🛑 sign-off (记者终读) → 以记者署名 + Express Desk 署名 + AI 说明发布"
source_hash: 8a078cb3df4d
---

# 记者笔记改写台

**与相近工作流的区别：** 没有相近的工作流。AWF-0018 聚类简报起草的是 SEO 营销内容，没有记者和编辑把关。
**工具变体：** `in-house-chatgpt`

## 步骤

1. 记者负责一线采访，列出报道提纲，并确定新闻点和基调。他们把笔记和引语整理成文字，发给改写编辑 [[1]](#sources)。
2. 改写编辑给一个内部版 ChatGPT（来自母公司 Advance Local）下提示词，把素材变成完整的稿件。它主要用于简短、直截了当的郊区新闻 [[1]](#sources)[[2]](#sources)。
3. 🛑 **审阅**：作为人的改写编辑审阅并核实稿件事实，然后退回给记者 [[1]](#sources)[[2]](#sources)。
4. 🛑 **签发**：记者在发布前做最后审阅。Quinn 告诉读者“记者拥有最终决定权”（'Reporters get the final say,'，此处为转述引用）[[1]](#sources)。
5. 以记者的名字发布，并标注“Advance Local Express Desk”和一条说明：文章由 AI 辅助生成，并经员工审阅 [[1]](#sources)。

**产出：** 一篇发布在 cleveland.com 上的本地新闻报道，附 AI 辅助披露说明。
**失败模式 → 防护：** 稿件在未经记者签发的情况下以其署名发布（据报道发生于 9 月的一起事件，归因于编辑之间沟通失误，导致撤下署名并更正）→ 把记者的批准设为发布前的硬性关卡。未经编辑的 AI 错误 → 改写编辑核实每一份稿件的事实。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或把检查点放在了别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Boston Globe, Cleveland's largest newspaper is using AI to write some stories](https://www.bostonglobe.com/2026/03/03/business/cleveland-plain-dealer-ai/) (2026-03-03)。Express Desk 已在日常使用：记者笔记、AI 起草、编辑审阅、记者终审。"freed up an extra workday for them each week"。*第一手：是（编辑 Chris Quinn，引自他的专栏）；可信度：中。*
