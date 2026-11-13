---
id: AWF-0006
name: 受治理的数据查询
summary: "基于受治理的指标口径生成 SQL 与图表来回答业务问题；分析师复核，发给高管前须签批。"
deliverable: 数据答案
shape: "问题 → 加载指标定义 + schema → (SQL ⟲ 合理性检查) → 图表 + 摘要 → 🛑 review → 🛑 sign-off → 发布 → 存入黄金查询集"
source_hash: fe2f2bee7f3b
---

# 受治理的数据查询

## 步骤

1. 把业务术语映射到受治理的指标定义。术语有歧义时，先提问，不要猜。
2. 查看 schema 和样例行。
3. 起草 SQL，优先使用语义层。
4. 验证：合理性边界、join 扇出（行数是否暴增）、与权威看板总数对账。
5. 把结果绘制成图表，并附上 SQL。
6. 🛑 **审阅**：分析师复核逻辑。
7. 🛑 **签发**：结果发给高管之前必须签发。
8. 把验证过的查询存入黄金查询集，供复用。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Xu, Suresh, Tang, OpenAI, *Inside our in-house data agent*](https://openai.com/index/inside-our-in-house-data-agent) (2026-01-29)。以 schema、血缘和文档作为上下文；SQL 自检；保存人工纠正；用黄金 SQL 做评测。"more than 3.5k internal users"；"70k datasets"。*第一手：是；可信度：中。*
- [Johnson, Busch, Khune, Uber, *QueryGPT*](https://www.uber.com/blog/query-gpt/) (2024-09-19)。用精选 SQL 样例驱动意图、表和列智能体；由用户确认表。"about 300 daily active users, with about 78%" 反馈节省了报表时间。*第一手：是；可信度：中。*
