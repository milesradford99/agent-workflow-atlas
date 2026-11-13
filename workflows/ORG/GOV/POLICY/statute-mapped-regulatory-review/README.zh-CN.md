---
id: AWF-0204
name: 对照法律的规章审查
summary: "将每条规章条款对照授权法律，标出越权或重复之处；由机构协调员决定删减哪些。"
deliverable: 规章精简报告
shape: "把规章、指引、法律和判例载入同一个数据库 → 每个 条款：对照授权法律 → 分类 mandatory | discretionary | unauthorized → 标出跨机构的重复或冲突条款 → 跨州比较 → 起草精简文本 → 按机构出具报告 → 🛑 review (机构规章协调员决定推进哪些) → 规章制定 | 更新指引 | 立法修正"
source_hash: d7173a3480a1
---

# 对照法律的规章审查

**与相近工作流的区别：** AWF-0080（主题签发式征询意见分析）是同一类中最接近的：它分析公众对征询的回应。本工作流则是对照法律审计现有的规章体系，输出按机构划分的删减/精简建议；检查点是机构对每条建议作出决定，而不是主题签发加抽样映射。
**工具变体：** `vulcan-technologies`

## 步骤

1. 厂商把州行政法典（全部 66 个行政分支机构的规章）、指引文件，以及州和联邦的法律与判例收集到同一个数据库，并把规章拆分为独立条款；一个智能体爬虫负责跟踪后续的法律和规则变化 [[1]](#sources)[[2]](#sources)[[3]](#sources)。
2. 多个专门的智能体并发运行：把每条规章要求与授权它的法律比对，并分类为 mandatory（强制）、discretionary（裁量）或 unauthorized（无授权；例如引用了已废止的法律，或收费超出法律允许的范围）[[1]](#sources)[[2]](#sources)。
3. 智能体标出被多项规章或指引文件重复规定的条款（机构内部和跨机构），并起草更短的通俗改写 [[1]](#sources)。
4. 有针对性的跨州比较，把各项要求（例如执照所需的培训时数）与其他州对标；ORM 主任还介绍了用 AI 绘制成本收益热力图，以挑选需要更仔细审视的规章 [[1]](#sources)[[2]](#sources)。
5. ORM 把发现汇编成每个机构的报告：强制/裁量/无授权要求的概况、合并、取消或精简的建议，以及建议的法规文本 [[1]](#sources)。
6. 🛑 **审阅**：每个机构审阅发现，决定推进、搁置或进一步研究哪些变更；机构官员“决定还能再做哪些删减” [[1]](#sources)[[4]](#sources)。变更随后进入规章制定、更新指引，或针对强制条款提出立法修正请求 [[2]](#sources)。

**产出：** 按机构出具的规章精简报告；经机构批准的变更进入规章制定或指引修订流程。第 51 号行政令（Executive Order 51）把 AI 审查纳入每四年一次的定期审查。
**失败模式 → 防护：** AI 误读法律授权 → 分类结果只是路线图；由机构协调员和律师决定，ORM 主任表示各机构不会只依赖 AI 分析。影响难以归因 → 试点是在一个更大的人工项目末期开展的，因此对外宣传的削减幅度并非全部来自 AI（引用数字时要说明）。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Reeve T. Bull (ORM director), Yale JREG](https://www.yalejreg.com/nc/ai-empowered-regulatory-reform-spreading-the-virginia-model-by-reeve-t-bull/) (2026-02-12)。主任本人对试点的叙述：对照法律分类、跨州比较、合并、热力图。"around 20 seconds for a very preliminary cost-benefit analysis and 15-20 minutes for a more thorough cost-benefit analysis"。*第一手：是；可信度：高。*
- [Reason, Virginia is using AI to identify illegal and redundant regulations](https://reason.com/2025/07/23/virginia-is-using-ai-to-identify-illegal-and-redundant-regulations/) (2025-07-23)。厂商 CEO 介绍试点合同和数千个并发智能体。"$150,000, three-month-long pilot trial with ORM from May 1 to August 1"。*第一手：访谈；可信度：中。*
- [Reboot Democracy, How Virginia Used AI](https://rebootdemocracy.ai/blog/ai-regulation-case-study-virginia) (2026-04-28)。分五个阶段的试点；由各机构决定；成果无法与更大的项目分开。"Reduced total statewide regulatory requirements by 35.7 percent"（指整个为期四年的计划，并非仅来自 AI）。*第一手：访谈；可信度：中。*
