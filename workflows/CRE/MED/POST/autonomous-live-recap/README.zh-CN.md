---
id: AWF-0138
name: 自动直播战报
summary: "从直播比赛流中识别关键时刻并自动发布精彩回顾，无需逐条审批；团队抽样监控输出。"
deliverable: 直播精彩回顾
shape: "接入直播比赛流 → CV 检测关键时刻 (音频线索、机位) → 每个 事件：剪辑片段 + 自动拼装回顾 (转场、淡出) → 直接发布到 CMS/应用 (每场比赛回顾最多重述约 20 次) → 🛑 sample (团队查看表现 + 观众点赞/点踩) → 推出改进"
source_hash: c9e8a64badd1
---

# 自动直播战报

**与相近工作流的区别：** AWF-0077 逐字稿优先的视频剪辑由作者审阅内容剪辑，并在渲染前签发一遍完整观看。本工作流不经逐条审批就发布，人只监控输出流。自主程度（抽检对分段）和产出（一场比赛中多次更新的直播回顾）都不同。
**工具变体：** `aws-media-replay-engine` · `amazon-rekognition`

## 步骤

1. 接入多路并发的转播流，并用 Amazon 开源的 Media Replay Engine 剪出片段供推理使用 [[1]](#sources)。
2. 一个基于音频线索和机位训练的计算机视觉模型找出比赛的关键时刻 [[1]](#sources)。
3. 每出现一个新事件，回顾就重建并自动拼装，加上转场和淡出黑场。它直接进入 CMS 和 FOX Sports 应用，把比赛 'upwards of 20 times per match' 重述一遍 [[1]](#sources)。
4. 🛑 **抽检**：没有逐个片段的审批。团队监控表现并推出修复，例如点赞/点踩，以及扑救和点球等新事件类型 [[1]](#sources)。该页面对这个检查点只是简略描述。

**产出：** 每场比赛期间发布到应用的滚动精彩回顾。
**失败模式 → 防护：** 足球没有固定套路，检测会漏检或误报 → 用音频和机位线索训练模型，并根据表现推出修复。每个片段都没有人把关 → 只有在编辑范围很窄时（仅限比赛事件）才安全。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [SVG, How FOX Teamed Up with AWS for AI-Powered Highlights](https://www.sportsvideo.org/2023/07/24/case-study-how-fox-teamed-up-with-aws-for-ai-powered-highlights/) (2023-07-24)。2022 年 FIFA 世界杯的回顾在几乎没有人工介入的情况下发布。"731 recap videos were published autonomously across 61 matches"。*第一手：访谈；可信度：中。*
