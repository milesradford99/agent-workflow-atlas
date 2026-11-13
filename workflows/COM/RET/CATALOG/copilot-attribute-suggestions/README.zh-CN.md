---
id: AWF-0113
name: 副驾式属性建议
summary: "在新品上架时建议商品属性值；内容专家逐项接受或修改后才发布。"
deliverable: 已补全属性的商品条目
shape: "新品条目上架 → 提示词生成器建议属性 (按来源标记) → 🛑 review (内容创建专家接受或修改每个预选值) → 发布 → 专家参与改进提示词"
source_hash: 596407a304f4
---

# 副驾式属性建议

**与相近工作流的区别：** AWF-0048 缺口匹配式知识维护产出的是知识库文章。这里的产出是结构化的商品数据，逐字段批准（辅助），而不是作为文档起草后再审阅。
**工具变体：** `gpt-4o`

## 步骤

1. 在构建之前，领域专家在大量条目样本上审阅模型预测，以选定模型 [[1]](#sources)。
2. 在内容创建工具中，GPT-4o 生成的属性建议被预先选中，并以紫色圆点标出其来源 [[1]](#sources)。
3. 🛑 **审阅**：内容创建人员对每个属性做最终决定 [[1]](#sources)。
4. 用户参与改进提示词；上线时可以纳入或排除某些商品和属性 [[1]](#sources)。

**产出：** 在店铺中上线的条目属性，缩短了上线时间。
**失败模式 → 防护：** 约 25% 的建议有误 → 每个值都由人批准。小众品类表现较弱 → 按品类受控上线。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Zalando, Content Creation Copilot](https://engineering.zalando.com/posts/2024/09/content-creation-copilot-ai-assited-product-onboarding.html) (2024-09-17)。与内容创建专家一起在生产中使用。"enriching around 50,000 attributes on average per week"。*第一手：是；可信度：高。*
