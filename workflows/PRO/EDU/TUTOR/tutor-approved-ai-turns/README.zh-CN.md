---
id: AWF-0042
name: 导师确认的 AI 辅导回复
summary: "学生答错时起草辅导回复；值班导师逐条批准、修改或替换后才发送。"
deliverable: 受监督的辅导会话
shape: "学生答错 → 提醒值班导师 → 载入题目和可能的错误概念 → 每个 回合：AI 起草回复 → 🛑 action (导师批准、修改或替换) → 发送 → 学期结束后：🛑 sample (导师审计修改记录和语料)"
source_hash: eb4e76eb7b41
---

# 导师确认的 AI 辅导回复

**与相近工作流的区别：** AWF-0028 锚点校准评分器（Anchor-calibrated grader，ASSESS）给已完成的作业评分。AWF-0027 逆向设计课程（Backward-design course，COURSE）制作课程材料。本工作流是逐条消息受监督的实时辅导。
**工具变体：** `learnlm-eedi`

## 步骤

1. 学生答错诊断题时，值班导师团队会收到提醒，一位导师打开聊天会话 [[1]](#sources)。
2. 一个针对教学法调优的模型拿到题目和学生可能的错误概念，起草苏格拉底式的回复 [[1]](#sources)。
3. 🛑 **操作**：每条草拟的消息在送达学生之前，都由导师批准、修改或替换。要求是改到导师自己愿意发出为止 [[1]](#sources)。
4. 无论是导师亲自写还是只做监督，学生看到的界面都一样 [[1]](#sources)。
5. 🛑 **抽检**：运行结束后，监督导师审阅全部草稿、修改和重写的语料，查找有害内容和事实错误 [[1]](#sources)。

**产出：** 一段每个 AI 回合都经导师批准的辅导聊天，外加一份供安全审查的、经审计的消息日志。
**失败模式 → 防护：** 事实错误（3,617 条草稿中有 5 条）→ 逐条导师批准，加事后审计 [[1]](#sources)。表情符号等风格偏差 → 导师修改 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [LearnLM Team & Eedi, Exploratory RCT in UK classrooms](https://arxiv.org/html/2512.23633) (2025-12-29)。165 名学生，17 位监督导师；受监督的 AI 辅导效果与纯人工辅导持平或更好。"supervising tutors approving 76.4% of its drafted messages making zero or minimal edits"。*第一手：是；可信度：高。*
