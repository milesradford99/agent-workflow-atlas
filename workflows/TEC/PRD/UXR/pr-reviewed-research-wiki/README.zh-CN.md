---
id: AWF-0195
name: 经 PR 审阅的研究维基
summary: "把每次用户研究转为对研究维基的 PR 更新；研究员指出遗漏后合并。"
deliverable: 研究维基更新
shape: "每天从 Teams 拉取访谈文字稿 → 用视频工具处理录像 → 把发现整合进研究维基 → 开 PR → 🛑 review (研究员指出遗漏) → 合并"
source_hash: 70c927d4c14b
---

# 经 PR 审阅的研究维基

**与相近工作流的区别：** AWF-0061 引文核验式综合（Quote-verified synthesis）产出一次性报告，带主题核验和研究员签发；AWF-0120 负责开展访谈。这里由每日运行的智能体链更新一个长期维护的研究维基，检查点是每次更新的 PR 审阅：产出物和节奏都不同。
**工具变体：** `microsoft-teams` · `git-pull-requests`

## 步骤

1. 把研究的发现保存在受版本控制的 "LLM wiki" 中，而不是一份报告里；研究员会 "constantly tweaking and adjusting" 它 [[1]](#sources)。
2. 一串智能体每天循环运行：从 Teams 获取访谈文字稿，让录像经过团队的视频工具处理，把结果整合进维基 [[1]](#sources)。
3. 这串智能体带着改动开一个 pull request [[1]](#sources)。
4. 🛑 **审阅**：研究员在合并之前审阅 PR（"oh, it missed this, it missed that"）[[1]](#sources)。
5. 同一团队的相关做法：在分析之前先组装好上下文（简报、项目笔记、参与者分群），避免各分群被一概而论 [[1]](#sources)。

**产出：** 一个持续更新的研究维基，每次改动都由研究员合并；取代一次性的报告。
**失败模式 → 防护：** 智能体漏掉发现 → 合并前做 PR 审阅 [1]。分析抹平了参与者分群之间的差异 → 纳入简报和分群上下文 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名的、与厂商相关的或记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Microsoft Design, Rebuilding research from the ground up](https://microsoft.design/articles/rebuilding-research-from-the-ground-up/) (2026-09-10)。Core AI 的首席 UX 研究员运行一条每日的智能体链，写入维基，并经 PR 审阅。"Report writing that once took a week and a half now takes one to three days"。*第一手：访谈；可信度：中。*
