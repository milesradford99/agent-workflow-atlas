---
id: AWF-0078
name: 播客单集后期流程
summary: "剪辑并为录制好的播客添加字幕，起草配套素材；字幕、整期试听和素材发布前均由人工审核。"
deliverable: 已发布的播客单集
shape: "多轨录制 → 去除语气词/停顿 + 跳剪 → 生成式音频降噪 → Whisper SRT 字幕 → 🛑 review (字幕修正) → 🛑 review (完整试听，取舍镜头) → 每个素材：摘要/标签 | 文字稿清理 | 社交媒体帖子 → 🛑 review (发布前) → 发布"
source_hash: 964ddbec2986
---

# 播客单集后期流程

**与相近工作流的区别：** AWF-0017 配音流水线是翻译音频并重新配音。本工作流剪辑并打包的是原语言的单集。
**工具变体：** `descript` · `adobe-premiere-adobe-podcast-whisper`

## 步骤

1. 把每位说话人和每个机位分别录成单独的轨道（StreamYard），以便独立编辑各轨 [[1]](#sources)。
2. 在 Descript 或 Adobe Premiere 中去除停顿和语气词并做跳剪。用 Adobe Podcast 的生成式增强功能清理录音质量差的部分 [[1]](#sources)。
3. 用 Whisper 生成 SRT 格式的字幕。🛑 **审阅**：手动修正 SRT，而不是相信工具的猜测 [[1]](#sources)。
4. 🛑 **审阅**：制作人完整收听整期节目，检查故事线并做出判断，例如保留嘉宾的哪一条录音 [[1]](#sources)。
5. 用 Soundraw 生成片头和片尾音乐（常常要 10 到 15 个版本），再制作音频可视化短片或精彩集锦（Headliner、Descript）[[1]](#sources)。
6. 用不同的提示词分别起草 YouTube 摘要和标签、清理网站上的文字稿（Gemini）、起草社交媒体帖子。🛑 **审阅**：发布前由人检查文字稿、摘要和社交媒体帖子有无错误 [[1]](#sources)。

**产出：** 发布在 YouTube 和播客订阅源上的一期节目，附清理后的网页文字稿、字幕和社交媒体帖子。
**失败模式 → 防护：** 去除语气词时句子被截断，或把需要保留的停顿剪掉 → 完整试听审阅。AI 文字稿或摘要中的错误 → 任何内容发布之前先审阅。生成的音乐需要多次尝试 → 预留 10 到 15 次生成。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或把检查点放在了别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Trust Insights, So What? AI Podcast Editing](https://www.trustinsights.ai/blog/2024/06/so-what-ai-podcast-editing-level-up-your-workflow/) (2024-06-07)。团队自己节目的制作：时间预算、工具以及人在哪里审阅。"usually three hours for 30 minutes worth of stuff" (Wall，AI 生成的文字稿)。*第一手：是；可信度：中。*
