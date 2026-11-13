---
id: AWF-0077
name: 先文稿后剪辑的视频制作
summary: "基于文字稿剪辑录制视频并生成字幕和叠层；作者审核剪辑和预览，通看后签发。"
deliverable: 渲染完成的视频
shape: "导入录制素材 → 编辑文字稿（剪掉重拍和跑题内容）→ 🛑 review (作者确认内容剪辑) → 收紧停顿和语气词 → 智能体编写 ffmpeg 音频提取和配乐混音 → 逐词 Whisper 文字稿 → 智能体构建 Remotion 字幕和叠层 → (预览 ⟲ 智能体修复) → 🛑 review (预览) → 渲染 → 🛑 sign-off (1.5 倍速通看)"
source_hash: 77c6fedb3b09
---

# 先文稿后剪辑的视频制作

**与相近工作流的区别：** AWF-0015 AI 镜头工厂生成的是全新的视频镜头。本工作流剪辑的是真实录制的素材，内容上的取舍由人负责。
**工具变体：** `descript-whisper-remotion-claude-code` · `premiere-text-based-editing`

## 步骤

1. 把原始素材导入 Descript，把文字稿当作文本来编辑，删掉重复、跑题和失败的重拍。🛑 **审阅**：每一处内容剪辑都由作者决定（每段 30 分钟的录制约需 8 分钟）[[1]](#sources)。
2. 把超过 0.2 s 的字间停顿缩短，有选择地删除语气词，然后导出一份干净的、仅含说话人的 MP4 [[1]](#sources)。
3. Claude Code 编写并运行 FFmpeg 命令，提取单声道 16 kHz 音频，并在说话人声音之下混入有授权的配乐，带淡入淡出 [[1]](#sources)。
4. Whisper API 以 JSON 输出逐词时间戳。一个词典脚本修正专业术语的拼写错误，渲染前还要肉眼检查字幕 [[1]](#sources)。
5. Claude Code 构建 Remotion（React）组件，由该 JSON 驱动动画字幕，另有可复用的下三分之一字幕条、片头和片尾 [[1]](#sources)。
6. 🛑 **审阅**：作者在 Remotion Studio 中预览，并向 Claude Code 描述需要的修改，由它修改组件，直到预览满意，然后渲染 [[1]](#sources)。
7. 🛑 **签发**：必须以 1.5 倍速完整通看一遍，查出重复的句子、字幕错误、配乐错位和图形不匹配 [[1]](#sources)。

**产出：** 一个带字幕和品牌图形的最终 MP4，可直接上传到 YouTube 或社交平台。
**失败模式 → 防护：** 文字稿来自代理文件时出现时间偏移 → 对实际导出的文件重新转写。字幕中专业术语拼错 → 词典脚本加字幕检查。重复的句子在剪辑后仍然留存 → 最后的通看。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或把检查点放在了别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Mejba Ahmed, Claude Code video editing workflow](https://www.mejba.me/blog/claude-code-video-editing-workflow) (2026-04-11)。在这条流水线上做了 8 周的个人 YouTube 制作；对比使用前后的剪辑时间和产出。此前每个视频约 4 小时（有时 6 小时）；现在实际动手约 25 分钟。*第一手：是；可信度：中。*
