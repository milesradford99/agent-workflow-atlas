---
id: AWF-0196
name: 声明监测事实核查台
summary: "监测媒体中值得核查的说法并与既往核查匹配；核查员决定核查对象，同事审校后发布。"
deliverable: 已发布的事实核查
shape: "每个来源 (新闻、电视/广播文字稿、社交视频、Hansard)：转写 → 主题标注 → 每个声明：判定声明类型 + 声明者 → 值得核查度评分 | 与近期事实核查匹配 → 晨间主题摘要 + Slack 匹配信息流 → 🛑 review (核查员查看被标记的片段，决定是否核查) → 调研 + 来源统计数据 + 回应权 → 撰写事实核查 → 🛑 review (同事审校和编辑) → 发布 | 要求更正"
source_hash: 2ebba8317372
---

# 声明监测事实核查台

**与相近工作流的区别：** 最接近的是 AWF-0134（抽检式 LLM 记录分析，Sampled LLM records analysis）：那个智能体针对一篇调查报道，对一组文档回答固定的问题，由记者抽检答案。这里的产出是持续监测所得的一系列事实核查，每条浮现出的声明都由人来分诊。AWF-0074 把记者笔记改写成报道，输入和产出物都不同。
**工具变体：** `full-fact-ai` · `synthid-detector` · `slack`

## 步骤

1. 监测工具持续摄入每日报纸、电视、广播、在线视频、社交媒体平台和 Hansard。现场活动（每周的首相质询、辩论）有实时文字稿。在 2026 年的选举期间，团队还监测了 1,000 多个与候选人相关的 Facebook、TikTok、X、YouTube 和 Instagram 账号，视频配有 AI 文字稿 [[1]](#sources)[[2]](#sources)。
2. 每篇文章由一个用 10,000 篇已标注文章训练的分类器，打上 17 个高层主题之一的标签。每条声明被标注声明类型和声明者，然后评出值得核查的程度。从不让模型判断声明是否属实 [[1]](#sources)。
3. 生成式 AI 对长视频和播客中的片段排序（例如健康方面的声明或情绪化的建议），让核查员可以直接跳到相关部分 [[1]](#sources)。
4. 声明匹配把所有受监测的媒体与近期已核查的声明作比较。句子嵌入借助实体识别和词性标注器得到增强，再加上一个训练过的匹配模型。匹配结果进入内部的 Slack 频道 [[1]](#sources)[[2]](#sources)。
5. 每天早上，最值得核查的声明按主题标题展示。搜索工具可按发言人、政党或来源类型过滤 [[1]](#sources)。
6. 🛑 **审阅**：核查员观看或阅读被标记的部分以理解该声明，然后决定是否正式核查。由人来决定“什么值得关注” [[1]](#sources)[[2]](#sources)。
7. 核查员调研背景，找出统计类声明的出处，并在适当时给予回应权。AI 仅限于以图搜图之类的辅助手段，文章由核查员自己撰写 [[1]](#sources)。
8. 🛑 **审阅**：同事在发表前仔细审校并编辑文章 [[1]](#sources)。
9. 发布事实核查。对于重复出现的声明，联系议员或请报社更正。选举期间还会增加对候选人图片和视频的 SynthID 水印扫描 [[1]](#sources)[[2]](#sources)。

**产出：** 已发布的事实核查和更正请求；给编辑团队的每日声明概览。
**失败模式 → 防护：** 声明匹配混淆了不同的人或地点 → 实体识别 + 词性标注器 + 训练过的匹配模型 [1]。数量压垮小团队 → 值得核查度排序 + Slack 信息流以降低摩擦 [2]。把 AI 当作真相神谕 → 从不让模型判断声明是否属实 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Full Fact (Nowottny), Full Fact is battling AI-generated elections content](https://www.niemanlab.org/2026/06/full-fact-is-battling-ai-generated-elections-content-with-ai-tools-of-its-own/) (2026-06-25)。2026 年英国权力下放地区选举：监测候选人账号，把声明匹配到 Slack，水印扫描，人工分诊。"we scanned 16,514 images or videos attached to candidates' social media posts, and identified 136 that appeared to have watermarks"。*第一手：是；可信度：高。*
- [Full Fact (Corney), How AI can help fact checkers](https://fullfact.org/blog/2025/feb/how-ai-can-help-fact-checkers/) (2025-02-11)。从主题标注到声明匹配的完整流水线；该工具被其他事实核查机构使用。"used by over 40 fact checking organisations working in three languages across 30 countries on a daily basis"; "Over 200 fact check articles have been published about claims found there using our tools"。*第一手：是；可信度：高。*
