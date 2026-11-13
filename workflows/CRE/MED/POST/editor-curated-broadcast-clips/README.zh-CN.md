---
id: AWF-0202
name: 编辑精选的直播切片
summary: "把直播节目切分为带元数据的竖屏短片；编辑挑选、剪辑并修正后发布。"
deliverable: 社交视频短片
shape: "接入直播节目 → 按语音和画面线索切分（把导语与对应的专题片/访谈配对） → 每个片段：剪辑 + 竖屏化 + 元数据 → 🛑 review (编辑在节目结束后挑选、剪辑，并修正字幕/标题) → 发布到网站、应用、TikTok/Instagram/YouTube"
source_hash: 605f1634df42
---

# 编辑精选的直播切片

**与相近工作流的区别：** 最接近的是 AWF-0138（自主直播综述）。那个工作流把体育综述直接发布到 CMS，人只在事后抽查表现。这里每个新闻或访谈片段在发布前都由编辑审阅并挑选，所以检查点和自主程度（分段）都不同。AWF-0077 是与作者一起根据文字稿剪辑一段录制内容，而不是处理直播流。
**工具变体：** `framedrop` · `mediacorp-ai-smartcut`

## 步骤

1. 在节目或黄金时段新闻播出时接入直播信号 [[1]](#sources)[[2]](#sources)。
2. 系统根据语音和画面线索，把节目切分成不同的讨论或报道，并把导语与对应的专题片或访谈配对 [[1]](#sources)[[2]](#sources)。
3. 每个片段被剪成一条短片，自动转为适合社交平台的竖屏，并附上元数据，可直接进入 CMS [[1]](#sources)[[2]](#sources)。
4. 🛑 **审阅**：节目结束后，编辑团队审阅预先剪好的片段，挑选最好的并发布。在 Mediacorp，音频优化和动态重构图仍需要人工把关 [[1]](#sources)[[2]](#sources)。
5. 在节目结束后数分钟内发布到网站、应用和社交渠道 [[1]](#sources)[[2]](#sources)。

**产出：** 直播结束后不久，在网页、应用和社交平台上线的按报道或按精彩时刻划分的短片。
**失败模式 → 防护：** 片段边界切错（Mediacorp 报告准确率约 90%）→ 发布前由编辑审阅 [1]。重构图和音频问题 → 这些环节由人把关 [1]。某句话被断章取义 → 每条短片都由人挑选并剪辑 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或经记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [WAN-IFRA, How Singapore's Mediacorp is using AI](https://wan-ifra.org/2025/08/how-singapores-mediacorp-is-using-ai-to-reduce-friction-in-video-production/) (2025-08-11)。黄金时段新闻自动切分成数字短片；音频和重构图仍由人处理。"clips can go live 'within minutes,' with approximately 90 percent accuracy"。*第一手：访谈；可信度：中。*
- [Framedrop, Medialivre story](https://www.framedrop.ai/success-stories/medialivre) (undated)。每日节目自动切分；团队在节目结束后审阅并挑选预剪好的短片。"Clip production time reduced by ≈50%, from 20–30 minutes to 10–15 minutes"; "Published content increased by 62% between April and September"。*第一手：厂商；可信度：中。*
