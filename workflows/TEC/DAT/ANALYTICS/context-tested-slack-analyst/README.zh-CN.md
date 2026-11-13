---
id: AWF-0192
name: 经上下文测试的 Slack 分析师
summary: "在 Slack 线程中用 SQL 回答数据问题；数据团队旁观公开线程，并对上下文层做端到端测试。"
deliverable: 已回答的数据问题
shape: "Slack 线程中的问题 → 获取已索引的 dbt/BI/数据仓库元数据 + 领域文档 → (查询 ⟲ 检查列值，回溯) → 在线程中给出答案，附 SQL + 数据预览 → 🛑 sample (数据团队旁观公开线程，修补上下文缺口) → (更新上下文 ⟲ 对答案、工具调用、表做端到端测试)"
source_hash: 9eefe489c26d
---

# 经上下文测试的 Slack 分析师

**与相近工作流的区别：** AWF-0006 受治理的查询（Governed query）在发布前对每条查询都有 🛑 review 和 🛑 sign-off。这里答案发出时没有逐条审批；人们审计公开线程，团队测试上下文层，所以自主程度是抽检，产出物是聊天中的回答，而不是经签发后发布的图表。AWF-0123 是定时评论，不是由问题驱动的。
**工具变体：** `slack` · `dbt` · `looker` · `snowflake` · `snowflake-cortex-analyst` · `bigquery`

## 步骤

1. 汇总并索引来自 dbt、BI 和数据仓库的元数据；各领域负责人为自己的领域撰写文档，存成智能体可读取的文件 [[1]](#sources)。Whatnot 则把智能体限制在数据科学家认可的语义视图上，"accepting that we’d miss around 30% of questions" [[2]](#sources)。
2. 用户在 Slack 中 @ 智能体（或在公开频道提问）。它探索表、检查列值、分支和回溯，并在线程内回答 [[1]](#sources)。
3. 每个答案都附有证据：线程内的 CSV 预览 [[1]](#sources) 或底层 SQL [[3]](#sources)，方便提问者核对。
4. 没有逐问题审批：Ramp 起初对每个领域内的问题都要 @ 领域负责人，后来放弃了，因为这样 "didn’t scale" [[1]](#sources)。
5. 🛑 **抽检**：数据专家在公开频道审阅问题和答案，并通过更新智能体的访问权限或上下文来补上缺口 [[2]](#sources)；Sourcegraph 审阅答案 "the way we review PRs: glance at the SQL, confirm the logic, and move on" [[3]](#sources)。
6. 评估上下文层，而不是每个答案：与领域专家一起列出每个领域的高优先级概念，并编写端到端测试，对最终答案和中间步骤（预期的工具调用、表引用、查询形态）做断言；更新上下文，重新运行，确认 [[1]](#sources)。

**产出：** 发布在 Slack 线程中、附 SQL/数据预览的答案；由数据团队维护的、经过测试且有版本管理的上下文层。
**失败模式 → 防护：** 因表错误或已弃用而给出自信的错误答案 → 限制在认可的数据集上 [2]，展示 SQL [3]，上下文层测试 [1]。逐问题的人工审阅会重新造成瓶颈 → 把审阅改为抽检线程加测试 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Ramp, Building Ramp Research](https://engineering.ramp.com/post/meet-ramp-research) (n.d.)。内部的 Slack 分析师；放弃逐问题人工审阅，改用上下文层测试。"In the last 4 weeks, Ramp Research answered 1,476 questions in #ramp-research-beta, compared to 66 answered in #help-data."。*第一手：是；可信度：高。*
- [Whatnot, Lessons learned from scaling data scientists with AI](https://www.whatnot.com/engineering/lessons-learned-from-scaling-data-scientists-with-ai) (2026-01-29)。基于认可的语义视图的 Slack 机器人；数据专家监控公开问答并补上缺口。"over ten thousand data questions answered by AI systems"。*第一手：是；可信度：高。*
- [Sourcegraph, Building DataBot](https://sourcegraph.com/blog/building-databot-our-always-on-data-assistant) (2026-02-06)。答案附带 SQL；数据团队做审计而不是亲自回答。"Each question may only take 5-10 minutes" (DataBot 之前的基线)。*第一手：是；可信度：中。*
