---
id: AWF-0203
name: 主管批准的顾问答复
summary: "在顾问与客户通话时起草带出处的答复；主管逐条批准、修改或驳回后才交给顾问。"
deliverable: 经批准的咨询答复
shape: "顾问在客户通话中提问 → 语义路由到主题 → 检索 Advisernet + GOV.UK 指引 → 起草带出处引用的答复 → 🛑 review (主管批准、修改或驳回并附评语) → 经批准的答复 + 主管备注交给顾问 → 顾问向客户提供建议 → 驳回记录用于再训练"
source_hash: 013e2d668fca
---

# 主管批准的顾问答复

**与相近工作流的区别：** 最接近的是 AWF-0081（摘要辅助的个案决定）：在那里由决策者借助摘要决定一个个案，质量靠抽样检查。这里的交付物是对顾问实时提问的答复，并且在一线顾问看到之前，每条 AI 答复都要由第二个人（主管）批准。AWF-0141 填写表单；AWF-0142 起草个案记录。
**工具变体：** `caddy`

## 步骤

1. 一线顾问在与客户通话或聊天时，把自己拿不准的问题输入现有聊天平台中的 Caddy（试点中用的是 Google Workspace 聊天）。客户始终只与顾问打交道 [[1]](#sources)[[3]](#sources)。
2. Caddy 使用语义路由，针对某个主题，会提出经验丰富的顾问训练它去考虑的各项因素 [[1]](#sources)。
3. 它只从可信来源（Citizens Advice 的 Advisernet 和 GOV.UK）检索，并起草约 400 字的答复，注明每一点的出处 [[1]](#sources)[[3]](#sources)。
4. 🛑 **审阅**：草稿进入主管队列，绝不直接交给顾问。主管审阅后可以修改并补充背景，然后批准或驳回。顾问只能看到已批准的答复；被驳回时，顾问看到的是主管的评语 [[2]](#sources)[[3]](#sources)。
5. 顾问把经过验证的建议转达给客户。在试点中，从生成、验证到返回的完整循环约需 4 分钟 [[1]](#sources)。
6. 被驳回的答复会被记录下来，用于找出改进方向并再训练；Caddy 2.0 增加了验证引擎，把答复拆成可核对的论断并与来源交叉引用，以加快主管的核对，同时保留人工检查 [[3]](#sources)[[4]](#sources)。

**产出：** 一条经主管批准、附出处的答复，在聊天中返回给顾问，由顾问转达给客户；每条答复的批准/驳回数据都会保存。
**失败模式 → 防护：** 在福利、债务或住房方面给出编造或过时的建议 → 每条答复在顾问看到之前都由主管验证，来源仅限 Advisernet 和 GOV.UK。主管队列成为瓶颈 → 用 Caddy 2.0 的论断级验证缩短核查时间。新顾问过度信任答复 → 答复附带来源链接和主管备注。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [i.AI, Transforming Civic Engagement with Caddy](https://ai.gov.uk/blogs/transforming-civic-engagement-with-caddy/) (2025-03-13)。覆盖 1,000+ 次通话的随机试验；经主管验证的答复约 4 分钟内返回。"80% of responses were of a high enough quality to be passed directly to advisors without revisions"。*第一手：是；可信度：高。*
- [Citizens Advice SORT, Caddy v2 slides](https://www.ukauthority.com/media/yyhakfjr/stuartpearson-caddy-v2-ukauthority-presentation-1.pdf) (undated, 2025)。在 6 个办事处进行 4-6 周的试点；主管队列批准、评论并返回给顾问。"Over 80% of Caddy's responses were approved"。*第一手：是；可信度：高。*
- [i.AI, Frontline Services](https://ai.gov.uk/our-work/frontline-services/) (undated)。试验后的推广规模。"Caddy is already supporting over 40 local Citizens Advice offices, earning a 90% approval rating from advisers"。*第一手：是；可信度：中。*
