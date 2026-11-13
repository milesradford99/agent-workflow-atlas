---
id: AWF-0201
name: 自有声音的文章音频
summary: "用定制的自有声音为每篇发布的文章生成音频；语音专家抽检纠正发音，编辑可随时覆盖。"
deliverable: 文章朗读音频
shape: "打造自有声音（演员录制基础语料 + 自家文章句子） → 影子运行：每天的文章 → TTS → 🛑 sample (语音专家试听，按拼音纠正发音) → 发音/替换词库 → 上线：每篇发布的文章：去掉小标题和括号内容 → TTS (交替使用不同声音) → 片头音 + 标题 + 署名 → 在应用中发布 → 听众反馈 → 🛑 review (编辑覆盖错误发音) → 扩展到更多文章"
source_hash: 8a55ac01fdcd
---

# 自有声音的文章音频

**与相近工作流的区别：** 最接近的是 AWF-0139（导演式 AI 有声书）。那是辅助级的，对一本书逐章导听，由作者签发。本工作流是新闻编辑部的流水线：经过抽检式的影子期后，每篇文章无人值守地朗读，人只负责维护词库和回应反馈。交付物（逐篇的音频流）、自主程度（抽检）和检查点都不同。AWF-0078 是对已录制音频做播客后期制作。
**工具变体：** `azure-speech-custom-voice` · `google-wavenet-speechbert` · `elevenlabs-beyondwords`

## 步骤

1. 打造自有声音：演员录制厂商的基础语料，外加取自报社自家文章的 400 个句子，让声音能适应报纸冗长、多引语的文风。《世界报》（Le Monde）使用一男一女两个声音，按篇交替（访谈和社论除外）[[1]](#sources)。
2. 🛑 **抽检**：在为期 2 个月的影子运行中，每天自动生成 20 篇文章的音频，但不对外播出。语音专家试听，并按读音纠正用词 [[1]](#sources)。
3. 维护一个替换/发音词库，让编辑可以覆盖难词的默认读音。词库随时间不断增长 [[1]](#sources)[[2]](#sources)。
4. 上线：每篇选定的文章自动转换，排除小标题和括号内的内容，配上片头音、标题、导语和作者，发布到订阅用户的应用中 [[1]](#sources)。
5. 🛑 **审阅**：编辑通过管理界面的替换区，纠正被报告的错误发音 [[2]](#sources)。
6. 收集听众反馈（上线时的弹窗），关注完播率和收听时长，然后扩大覆盖范围。《世界报》从每天 20 篇扩展到全报，仅排除地图或图表较多的文章 [[1]](#sources)。

**产出：** 在出版方的应用或网站中，随文章发布同步生成的文章音频版本。
**失败模式 → 防护：** 通用声音听起来都一样，让听众疲劳 → 定制自有声音并交替使用 [1]。自家文风打乱了 TTS 的节奏 → 用自家文章的句子训练，而不是改变写作 [1]。错误发音损害信任 → 设影子期并配语音专家试听，加上长期维护的替换词库 [1][2]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或经记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Microsoft, Le Monde audio articles](https://www.microsoft.com/en/customers/story/1642942168798077445-lemonde-media-entertainment-azure-en-france) (page dated 2023-06-03, text since updated)。先由语音专家试听做影子运行，再每天为 20 篇文章生成音频，最后覆盖全报。"Over a 2-month period, 20 articles were generated automatically in audio format every day without being broadcasted"; "72% of the article read on average"; "over 100 articles a day"。*第一手：厂商；可信度：中。*
- [Diesdas Digital, Speechbert for ZEIT ONLINE](https://www.diesdas.digital/en/cases/speechbert) (undated)。文章发布后数秒内转成音频；编辑维护发音替换词库。"over 250,000 text-to-speech conversions since launch"。*第一手：厂商；可信度：中。*
