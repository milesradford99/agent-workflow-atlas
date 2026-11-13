---
id: AWF-0111
name: 商品文案工厂
summary: "依据商品数据和文案规则按 SKU 起草详情文案；经规则检查和人工筛查队列审核后批量发布。"
deliverable: 商品详情文案
shape: "来自店铺/PIM 的商品数据 + 品类简报 + 文案规则 → 每个品类一个提示词模板 → 每个 SKU：起草 → (规则检查 ⟲ 重新生成) → 🛑 review (筛查队列) → 存储已批准文案 + 批量发布到商品页 → CTR/CVR 反馈 → 更新模板 / 重新训练"
source_hash: 6c3616493ad4
---

# 商品文案工厂

**与相近工作流的区别：** AWF-0018 聚类-简报-起草式内容：它逐篇产出 SEO 文章，每篇都有 SERP 简报和 SME 输入。本工作流以目录级的体量产出结构化的逐 SKU 商品文案，经过规则检查和筛查队列。产出和检查点的安排都不同。
**工具变体：** `chatgpt-api` · `claude-api` · `shopify-graphql` · `jd-apcg`

## 步骤

1. 从店铺数据库或 PIM 拉取 SKU 及其结构化商品数据。收集专业部门的简报和商品文案规则 [[1]](#sources)[[2]](#sources)。
2. 把简报转成提示词模板。把同样的规则转成供规则检查器使用的独立检查项 [[2]](#sources)。
3. 为每个 SKU 批量生成描述，然后做后处理 [[1]](#sources)[[2]](#sources)。
4. 运行自动检查（规则合规、长度、必备段落、输入数据不支持的宣称）。不合格的先重新生成，再交给人看 [[1]](#sources)[[2]](#sources)[[3]](#sources)。
5. 🛑 **审阅**：对生成的文案做人工筛查。只有获批的文本才会存入待发布库 [[1]](#sources)。在一次 6,000 个 SKU 的运行中，审阅人对其中约 8% 做了实质性修改 [[3]](#sources)。
6. 将获批文案批量发布到商品页 [[3]](#sources)。用新数据重新训练或更新模型和模板；JD 对选定领域每天重新训练 [[1]](#sources)。

**产出：** 存储并发布到商品详情页的已批准商品描述；CTR/CVR 与旧文案对比衡量。
**失败模式 → 防护：** SKU 数据稀疏导致编造规格 → 只对数据完整的 SKU 运行，增加不受支持宣称的检查，并让审阅人核对事实 [[3]](#sources)。文案违反部门的文本规范 → 用同一份简报构建规则检查器 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [JD.com, Automatic Product Copywriting for E-commerce](https://arxiv.org/html/2112.11915v1) (2022-06-28)。生成 → 人工筛查 → 存储已批准文案；自 2021 年 2 月起上线。"Daily uploads to the descriptions database can reach up to 28,570 generated descriptions, with an average daily acceptance rate of 80%"。*第一手：是；可信度：高。*
- [Troy Morgan, Shopify description pipeline](https://www.tdmorgan.com/blog/building-ai-product-description-pipeline-shopify) (2026-03-28)。一家约有 8,000 个 SKU 的零售商：校验、重新生成、人工审阅队列、批量发布。"The human review step catches about 8% of descriptions that need meaningful edits"。*第一手：匿名（未具名店铺）；可信度：中。*
