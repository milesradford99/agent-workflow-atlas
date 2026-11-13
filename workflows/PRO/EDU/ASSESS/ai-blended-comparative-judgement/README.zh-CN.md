---
id: AWF-0167
name: AI 混合比较评判
summary: "AI 评判大部分学生作文配对，教师评判其余部分；人机分歧较大的配对复核后再定分。"
deliverable: 标度化写作分数
shape: "教师上传学生作文 → 设定 AI 与人工评判的比例 (建议 90:10) → 每个 配对：AI 评判选出更好的作文 | 🛑 sample (教师评判各自份额的配对) → 把所有判断合并成测量标度 → 对每个人工评判的配对比较 AI 与人工 → 分歧较大的：🛑 review (纠正 AI 或人工的错误) → 与国家标准挂钩的标度分数和等级"
source_hash: 91a2e0da10cf
---

# AI 混合比较评判

**与相近工作流的区别：** AWF-0028 锚点校准评分器：AI 在锚点上校准后，为每份作业给出绝对的量表分，人工抽检低置信度的评分。本工作流中 AI 只做两两比较，人工并行做同样比较中固定的一部分，再由标度模型产出分数。人工抽样内置在测量本身之中，交付物（全体学生的标度）和检查点安排都不同。
**工具变体：** `no-more-marking`

## 步骤

1. 教师把学生的作文上传到平台。学校选择由 AI 作出多大比例的判断；建议的比例是 90% 由 AI、10% 由人工 [[1]](#sources)[[2]](#sources)。
2. 评判者比较两篇作文并选出更好的一篇，而不是孤立地给每篇打分。组织方发现 LLM 做绝对评分「会犯令人费解的错误」，因此改用比较评判 [[2]](#sources)。
3. 🛑 **抽检**：教师完成自己份额的比较评判。在 90/10 的比例下，每份答卷平均被 AI 看 18 次、被人类教师看两次。一位系主任用 1 小时 12 分钟完成了全校 269 名 7 年级学生的份额 [[1]](#sources)。
4. 所有人工和 AI 的判断由统计模型合并成每篇作文的精细标度（约 300-700） [[2]](#sources)[[3]](#sources)。
5. 每个人工评判的配对都与 AI 对照。🛑 **审阅**：检查分歧很大（超过 80 分）的情况。多数是人为错误（点错按钮、字迹难辨）。少数是 AI 的错误，例如只有一两个词的作文，这些在「发布结果之前……被找出并修正」 [[2]](#sources)[[4]](#sources)。
6. 发布与现行国家标准挂钩的标度分数和等级 [[1]](#sources)。

**产出：** 每份学生作文的标度分数和等级，可跨学校比较。教师和学校用于报告和一致性核查。
**失败模式 → 防护：** AI「80% 的时候是对的，在最关键的时候却错了」 → 检查分歧的大小，而不只是一致率 [1]。近乎空白的作文会让 AI 困惑 → 发布前标记并修正 [4]。AI 评判悄然漂移 → 10% 的人工份额使每份作文都有人工评判两次 [3]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [No More Marking, So, can AI assess writing?](https://substack.nomoremarking.com/p/so-can-ai-assess-writing) (2025-03-31)。44 所学校的 7 年级作文由 AI 和教师评判；检验一致性。"In total, our human judges made 3,640 decisions. Of these 3,640 decisions our AI agreed with 81% of them."。*第一手：是；可信度：高。*
- [No More Marking, AI is uncannily good at judging writing](https://substack.nomoremarking.com/p/ai-is-uncannily-good-at-judging-writing) (2025-10-25)。7-9 年级的全国测评，多数学校采用 90% 的 AI 评判。"approximately 70,000 pieces of writing completed by Year 7, 8 & 9 students from 177 UK secondary schools"；"The AI judges agreed with 83% of them"。*第一手：是；可信度：高。*
- [No More Marking, Australia Term 1 2026](https://aus.nomoremarking.com/assessing-writing-in-australia-how-did-the-ai-judges-do-term-1-2026-05589e2cbdbe) (2026-03-05)。澳大利亚的学校；发现并在发布前修正了首批由 AI 造成的较大分歧。"the human judges completed 10,970 judgements. The AI judges agreed with 80% of those decisions"。*第一手：是；可信度：高。*
