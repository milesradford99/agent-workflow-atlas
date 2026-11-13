---
id: AWF-0107
name: 人工发送的回复起草
summary: "结合案件历史、CRM 和知识库起草客户回复；每条回复都由客服顾问修改并发送。"
deliverable: 客服人员发送的回复
shape: "案件到达 → 总结对话 + 确认意图 → 调取案件历史、CRM、KB、订单数据 → 以品牌语气起草回复 + 执行常规工具任务 (如优惠码) → 🛑 review (顾问修改并发送每条回复) → 结案前核对案件意图 → 使用情况 + 处理时长跟踪"
source_hash: 4584e3e0b3bc
---

# 人工发送的回复起草

**与相近工作流的区别：** AWF-0021 流程智能体：在那里智能体直接回复客户并自主行动，辅以抽检式质检。本工作流中每条回复都由人发送（辅助级自主，逐条回复审阅）。产出是由客服人员发送的回复，而不是自主完成的解决。
**工具变体：** `salesforce-agentforce-service` · `dynamics-365-copilot-service` · `zendesk-agent-copilot`

## 步骤

1. 每个案件到达时，助手先总结目前的对话，并在开始处理前确认消费者要什么 [[2]](#sources)。
2. 让助手以案件历史、CRM 记录和知识文章为依据，再加上来自 ERP 的订单数据，使草稿反映当前的促销和订单状态 [[2]](#sources)。
3. 按品牌自己的语气要求和该品牌的知识起草回复初稿。在所研究的部署中，建议会实时出现，由客服人员决定是否采用 [[1]](#sources)[[2]](#sources)。
4. 根据一条提示词执行案件内的常规任务，例如生成促销码，这可替代约 15 个屏幕的手工操作 [[2]](#sources)。
5. 🛑 **审阅**：人工顾问审阅草稿、修改并发送。没有人发送，任何回复都不会到达客户 [[2]](#sources)。
6. 结案前，助手检查所选的案件意图与对话是否一致，使整个团队的意图保持统一 [[2]](#sources)。
7. 一次只上线一个品牌和市场，了解哪些意图有效，再逐步扩大 [[2]](#sources)。跟踪处理时长、每小时解决数和质量，并按客服人员的资历细分 [[1]](#sources)。

**产出：** 由人工客服发送的回复，以及写入服务台的案件摘要和经核对的意图标签。它们为 KB 缺口和质检工作提供输入。
**失败模式 → 防护：** 经验最丰富的客服人员采纳建议时质量会有所下降 → 按客服人员的技能水平衡量，并允许专家忽略建议 [[1]](#sources)。草稿编造订单号或日期等细节 → 让草稿以实时的 CRM/订单数据为依据，并保留人工发送这一步 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Brynjolfsson, Li, Raymond, Generative AI at Work (QJE)](https://academic.oup.com/qje/article/140/2/889/7990658) (2025-02-04)。在一家财富 500 强软件公司，向 5,172 名客服人员分批推出 AI 助手。"increases worker productivity, as measured by issues resolved per hour, by 15% on average"。*第一手：研究（对一家未具名公司的实地研究）；可信度：高。*
- [Salesforce, L'Oréal customer story](https://www.salesforce.com/eu/customer-stories/loreal/agentic-service-advisor-assistance/) (2026-09-11)。顾问审阅并发送 AI 草稿；先在加拿大对一个品牌试点，现已扩展到 25 个品牌。"cutting the time to resolve a case from about 7 minutes to about 2.5 minutes"。*第一手：厂商；可信度：中。*
