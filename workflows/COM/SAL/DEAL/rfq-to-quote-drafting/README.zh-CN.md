---
id: AWF-0176
name: 询价单转报价草稿
summary: "把收到的询价单转为逐行标注来源的报价草稿；销售确认标记行后发送。"
deliverable: 报价草稿
shape: "收到询价单（邮件、PDF、表格、照片） → 提取行项目 → 每个行项目：匹配目录 SKU + 置信度 → 按客户价目表/ERP 定价 → 起草报价，每行标注来源 → 标记低置信度或不符合政策的行 → 🛑 review (销售确认被标记的行和价格后发送) → 回写 ERP → 销售的修正用于调整匹配"
source_hash: 45813a9fb99a
---

# 询价单转报价草稿

**与相近工作流的区别：** 最接近的是 AWF-0050 通话转 CRM 的 diff 审批：那是把一次销售通话变成 CRM 字段变更和跟进邮件。本工作流把客户的询价单变成基于目录和价目表的定价报价。交付物和输入都不同；审阅针对的是被标记的报价行，而不是 CRM 的 diff。
**工具变体：** `canals` · `quotery` · `proton-ai` · `azure-openai`

## 步骤

1. 监视共享的销售邮箱；按请求到达时的形式读取（邮件正文、PDF、Excel、手写清单的照片） [[1]](#sources)[[3]](#sources)。
2. 提取每个所需行项目；先按精确编码匹配目录 SKU，再用 AI 匹配，每行给出置信度分数，描述含糊时给出备选项 [[2]](#sources)[[3]](#sources)。
3. 每行根据 ERP 中客户自己的价目表档位、合同价和批量折扣定价；模型从不自行定价 [[3]](#sources)[[4]](#sources)。
4. 用公司的模板起草报价，每行列出来源描述、匹配的零件和价格来源；标记低置信度的匹配和未定价的项目 [[2]](#sources)[[3]](#sources)。
5. 🛑 **审阅**：销售或估价员确认被标记的行，补充替代品或库存说明，然后发送；起初每份报价都要审阅 [[2]](#sources)[[3]](#sources)。有些团队在准确性得到证明后，会放开某些类别（例如库存答复）不经审阅，而定价仍由人负责 [[4]](#sources)。
6. 把已接受的报价/订单回写 ERP；销售的修正反馈到匹配中 [[1]](#sources)[[4]](#sources)。

**产出：** 客户邮箱和 ERP 中的一份已定价报价，每行来源可追溯。
**失败模式 → 防护：** 错误的 SKU 或价格到了客户手里 → 先做确定性的编码匹配，设置置信度阈值，对被标记的行审阅 [2][3]。ERP 目录混乱 → 从销售过往的报价中学习 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Quotery, Brazos Valve case study](https://quotery.io/blog/case-study-brazos-valve-distributors/) (2026-05-12)。15 人团队；确定性加 AI 的逐行匹配；销售发送前审阅；跟踪了五个月。"Quote time: 8 minutes average. Down from 3 hours."。*第一手：厂商；可信度：中。*
- [Canals, Puget Sound Pipe & Supply](https://www.canals.ai/case-studies/puget-sound-pipe-and-supply-slashes-quote-times) (undated)。经销商销售审阅并确认 AI 的条目匹配；客户谈到了节省的时间。"with an advanced user, the time savings is probably three or four to one"。*第一手：厂商；可信度：中。*
- [EasiraAI, wholesale quote pilot](https://easiraai.com/work/wholesale-quote-from-enquiry) (undated)。在一家约 30 人的经销商做了为期六周的试点；估价员审阅每份草稿。"~10 minutes (incl. estimator review)"。*第一手：厂商；可信度：中。*
