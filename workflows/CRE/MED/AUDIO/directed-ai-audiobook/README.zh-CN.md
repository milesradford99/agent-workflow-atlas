---
id: AWF-0139
name: 导演式 AI 有声书
summary: "用 AI 配音制作有声书母带；真人确认选角试听、审听全书，作者最终签发。"
deliverable: 有声书母带文件
shape: "为音频改编 ePub（删除目录/URL/图片，改写台词）→ 🛑 plan (配音试听：首章用 5–6 种声音) → 逐章导入工作室 → 发音词典 + 情绪标签 → (完整试听 ⟲ 导演式修正：停顿、重音、重新生成) → 🛑 review → 🛑 sign-off (作者确认改编后的台词) → 以 192 kbps 导出 → 多渠道发行"
source_hash: f011bcac5a77
---

# 导演式 AI 有声书

**与相近工作流的区别：** AWF-0078 播客单集后期制作链（Episode post-production chain）是对已录制的播客音频做清理和加字幕。本工作流则由文本合成整本书长度的旁白，前期有选角试听，之后还有导演式的完整试听。素材（文本而非录音）、产出和检查点都不同。
**工具变体：** `elevenlabs-studio` · `findaway-voices`

## 步骤

1. 把书稿整理成适合音频的改编版。删除目录、URL 和图片。作者可以改写念出来别扭的句子 [[1]](#sources)。
2. 🛑 **计划**：用五六种声音生成第一章，选定一种后再制作全书 [[1]](#sources)。
3. 把 ePub 载入 ElevenLabs Studio，它会自动拆分成章节和段落。用发音词典一次性修正人名（例如 'desert'/'dessert' 这类读错的情况）[[1]](#sources)。
4. 添加 v3 情绪标签，如 [whispers] 或 [shouts]。自动标签按钮可以给出建议，这些标签不会被读出来 [[1]](#sources)。
5. 🛑 **审阅**：制作人从头到尾听一遍，通过增加停顿、换气、重音和重新生成来“导演”。小说需要两三天，非虚构类接近听一遍即可 [[1]](#sources)。
6. 🛑 **签发**：作者确认改编稿中的台词改动。替作者工作的制作人不能单独做这些改动 [[1]](#sources)。
7. 以 192 kbps（Pro 档）导出，并多渠道发行：通过 Findaway 发到 Spotify、BookFunnel 和自己的网站 [[1]](#sources)。

**产出：** 出版方自有的 WAV/MP3 有声书母带，在 Audible 独家之外发行。
**失败模式 → 防护：** 读了几章才发现选定的声音刺耳 → 前期做配音试听。人名和同形异音词读错 → 全局发音词典。对白平淡 → 情绪标签加完整的导演式试听。

**近期实践（2026）：**
- 导入步骤：每个场景建一个工作室章节（命名为书-章-场景-开头几个词），这样重新生成某个场景时不影响其他部分。通过 Voices by INaudio 发行，需要直接从 ElevenLabs 提交文件，不能做任何外部音频编辑（Freitag 2026）。[[2]](#sources)
- 发音步骤：当词典对频繁出现的虚构人名失效时，在脚本里用音标式拼写写出该词，并用大写表示重音（Freitag 2026）。[[2]](#sources)
- 导出步骤：先导出单个章节来验证设置。整个项目一次性导出无法撤销（“I once lost 153k credits in one go”）（Freitag 2026）。[[2]](#sources)

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。更新见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [The Creative Penn, Producing AI-Narrated Audiobooks Using ElevenLabs](https://www.thecreativepenn.com/2025/06/27/producing-ai-narrated-audiobooks-using-elevenlabs-with-simon-patrick/) (2025-06-27)。制作人自述的流程；中篇小说 Death Valley 用作者的声音克隆制作。"Your novella, Death Valley, was six and a half hours long. That took 18 hours of editing."。*第一手：访谈（制作人做客作者的播客）；可信度：高。*
- [Minu Freitag, Digital Narration with ElevenLabs: What I Wish I'd Known](https://minu.co.nz/digital-narration-with-elevenlabs-what-i-wish-id-known/) (2026-05-10)。14.3 万词的小说；每个场景一个 EL 章节；发音词典加音标式拼写；导出的坑。"It took me two to three hours per recorded hour for the first release candidate and another hour per recorded hour to make changes."。*第一手：是；可信度：高。*
- [Renee Bryan, ElevenLabs Review: My Experience Creating an AI Audiobook](https://reneelizbryan.info/elevenlabs-review-ai-audiobook-experience/) (2026-08-23)。克隆自己的声音；反复试听、编辑、重新生成，以修正不匹配的情绪。"I spent well over 100 hours on the audiobook"。*第一手：是；可信度：高。*
- [Nir Librach, LinkedIn post on Power Quest audiobook](https://www.linkedin.com/posts/nir-librach-478827194_litrpg-audiobooks-activity-7496197446239449089-4E1f) (2026-08-20)。多声音 AI 有声书，历时四个月导演制作；已在 ElevenReader 和 Spotify 上线。"Power Quest's 54 chapters span over 27 hours of audio, and feature over 40 unique character voices"。*第一手：是；可信度：中。*
