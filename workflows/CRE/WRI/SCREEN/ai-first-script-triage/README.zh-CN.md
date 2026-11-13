---
id: AWF-0198
name: AI 先读的剧本初筛
summary: "为每部投稿剧本生成审读报告并建立可检索片单；由高管挑选精读，每部入选剧本需有人力挺。"
deliverable: 剧本审读报告
shape: "收取投稿 → 每个剧本：智能体拆解(分场摘要、角色、对标作品、选角建议) → 审读报告(部分工具附评分/结论) → 索引到可检索片单数据库 → 🛑 review (高管/审读人阅读报告，挑选精读剧本) → 人工通读全本并写意见 → 🛑 sign-off (人类力挺者，另有人附议)"
source_hash: 9d19ae98d113
---

# AI 先读的剧本初筛

**与相近工作流的区别：** 最接近的是 AWF-0013（按节拍写分场剧本）和 AWF-0014（钩子节奏短剧剧本）。两者都是写剧本。本工作流是读别人的剧本，输出的审读报告用于支持人工的立项或精读决定。交付物和检查点（初筛而非草稿审阅）都不同。
**工具变体：** `scriptsense` · `greenlight-coverage` · `screenplayiq`

## 步骤

1. 团队上传剧本，可以是积压未读的稿堆，也可以是比赛或投稿池 [[1]](#sources)[[2]](#sources)。
2. 多步骤的智能体拆解把每部剧本分成情节、角色和主题等部分，并生成审读报告：分场摘要、角色分析、相似作品。有的工具还加上选角建议；有的加上 1–10 分评分和放弃/考虑/推荐的结论 [[1]](#sources)[[2]](#sources)。
3. 上传的材料会建立索引，团队可以按子类型、场景设定、主题、角色类型或故事线，对照内容需求在数千部剧本中检索 [[1]](#sources)。
4. 🛑 **审阅**：高管、经纪人或审读人阅读报告，决定把精读的重点放在哪里。ScriptSense 有意不给出推荐（“我们不会替你做决定”）[[2]](#sources)。
5. 由人通读全本并写意见。在编剧工会（Editors Guild）的测试中，AI 的意见“几乎全面失败”，所以意见仍由人来写 [[2]](#sources)。
6. 🛑 **签发**：在 INTERDEPENDENT，先由内部 AI 读过的剧本，“必须有一位人类力挺，再有另一人附议”，才能继续推进 [[3]](#sources)。

**产出：** 审读报告和可检索的片单。入围剧本进入人工精读和开发决策。
**失败模式 → 防护：** AI 的审读报告倾向于讨好，常会“推荐”较弱的剧本 → 不要相信结论，由人阅读入围名单 [2]。面对复杂剧本时，它会把动作安到错误的角色头上，还会编造情节点 → 引用梗概前先对照剧本核实 [2]。意见需要 AI 缺乏的分析能力 → 意见保持由人撰写 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或经记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Variety, Hollywood Script Readers Fear They Could be Replaced by AI](https://variety.com/2025/film/news/hollywood-script-readers-replaced-by-ai-test-1236552756/) (2025-10-14)。独立制片人对手头的稿堆使用 AI 审读报告；WME 的经纪人使用 ScriptSense；Editors Guild 测试了六个平台。"He found the AI more honest than human feedback — even his own — while it doubled his reading pace."。*第一手：访谈；可信度：中。*
- [Anthropic, Jumpcut customer story](https://www.anthropic.com/customers/jumpcut) (undated)。多步骤剧本拆解生成审读报告，被多家制片厂、经纪公司和制作公司使用。"35,000+ hours saved in script reading time"; "200+ companies using ScriptSense"。*第一手：厂商；可信度：低。*
