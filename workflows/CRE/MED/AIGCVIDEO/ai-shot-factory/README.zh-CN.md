---
id: AWF-0015
name: AI 镜头工厂
summary: "把剧本逐镜头生成 AI 视频剧集；方案、成片审核和发布前签发均由人工把关。"
deliverable: 剧集
shape: "剧本 → 分镜表 → 🛑 plan → 锁定角色 → 每个 镜头：(关键帧 ⟲ 评审) → (视频 ⟲ 检查) → 配音 + 口型同步 → 剪辑 → 🛑 review → AI 标识 → 🛑 sign-off → 发布"
source_hash: 452743f96b65
---

# AI 镜头工厂

| 步骤 | 工具（国内 / 国外） |
|---|---|
| 分镜表（分镜：编号、景别、运镜、动作、台词、时长） | Doubao, DeepSeek, Claude, GPT |
| 锁定角色 | 即梦 / Midjourney 参考图；ComfyUI + 每个角色一个 LoRA；Kling 多图参考，每次生成 1–4 张参考图 [[17]](#sources) |
| 关键帧 | 即梦/Seedream, Flux, Midjourney |
| 运动 | 可灵 Kling, 海螺 Hailuo, Vidu, Seedance, Veo, Runway |
| 配音与口型同步 | MiniMax, 火山引擎 TTS, ElevenLabs；口型同步工具或原生音视频模型 |
| 合成 | 剪映/CapCut, Premiere |

## 步骤

1. 剧本 → 20–40 个镜头的分镜表。🛑 **计划**：导演批准分镜表和风格帧。
2. 锁定角色。从业者会生成正面、侧面、背面视图和表情表，并在之后每次生成时把它们当作参考 [[16]](#sources)。
3. 每个镜头并行生成 4 个关键帧候选。由视觉模型评审者过滤，再由人挑选。
4. 每个镜头做图生视频。出现形变或物理穿帮时重抽。
5. 为每句台词生成带情绪标签的配音，然后做口型同步。
6. 合成并检查前 3 秒的钩子。
7. 🛑 **审阅**：导演列出需要重抽的镜头（回到第 3 或第 4 步）。
8. 🛑 **签发**：合规与标识。国内规则要求对 AI 生成内容加显式和隐式标识（自 2025 年 9 月 1 日起施行 [[15]](#sources)）。微短剧监管规定的征求意见稿还要求每一集 AI 生成的剧集都在显著位置加标识 [[14]](#sources)。

**报道中的成本（B）：** 一份引用巨量引擎数据的券商报告给出，传统漫剧每分钟 ¥2–5k，AI 辅助制作为 ¥1–2.5k。报告还提到有一家公司把 11 个制作环节缩减为 5 个 [[16]](#sources)。
**示例中应记录的指标：** 每次生成的可用镜头率、每成片分钟的成本、每集耗时。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [新民周刊 p.41](https://img1.xinmin.cn/xmzk/2026-07-13/410713.pdf) (Xinmin Weekly, 2026-07-13)。先过 AI 审核再过人工审核；为 AI 制作扩写剧本。"近七成都无法过审"；"5万字…可能要补充到8万字"。*第一手：访谈；可信度：中。*
- [毒眸 on 钛媒体](https://www.tmtpost.com/7712427.html) (How a 10-person team made an AI manhua drama in 45 days, 2025-10-02)。珀乐互动：画师手绘原稿 → AI 视频 → 剪辑；导演每周审阅。"一个仅10人的团队，用45天时间，完成了50集《明日周一》"。*第一手：访谈；可信度：高。*
- [PJ Ace, *I can't believe Disney allowed us to run this AI ad*](https://pjace.beehiiv.com/p/i-can-t-believe-disney-allowed-us-to-run-this-ai-ad-during-the-nba-finals-f77e73388ab4ca62) (2025-06-11)。粗剧本 → AI 分镜表和提示词 → 生成并重新提示 → 剪辑。"300–400 generations to get 15 usable clips"；"One person, two days."。*第一手：是；可信度：高。*
- [金姬, 新民周刊](https://www.xinminweekly.com.cn/bianjituijian/2026/04/08/41135.html) (A one-person animation factory?, 2026-04-08)。从大量生成结果中挑选分镜帧 → 图生视频。"110多张分镜与定稿图的1700多次AI'抽卡'"；"近20人的团队"。*第一手：访谈；可信度：中。*
