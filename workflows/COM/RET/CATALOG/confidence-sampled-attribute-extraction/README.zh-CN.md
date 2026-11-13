---
id: AWF-0112
name: 置信度抽检的属性抽取
summary: "抽取商品属性值并给出置信度；审核员只修正低置信度条目，并定期抽样检查质量漂移。"
deliverable: 商品目录属性值
shape: "开发模式：(提示词 + 模型配置 ⟲ 🛑 sample (人工审核员标注金标准值) + LLM 评判) → 部署 → 每个 商品：抽取属性 (文本 + 图像) → 自我验证置信度评分 → 低置信度：🛑 review (审核员修正) → 定期 🛑 sample (质量漂移) → 写入商品目录"
source_hash: be8b64391116
---

# 置信度抽检的属性抽取

**与相近工作流的区别：** 上文的 Zalando 副驾由人批准每一个值。这里人只看低置信度条目和抽样。AWF-0063 以 diff 为证的 dbt 迁移则以生产数据为检验依据，而不是人工金标准标签。
**工具变体：** `instacart-parse` · `walmart-qc-llm`

## 步骤

1. 在开发模式下，团队在小样本上迭代提示词和模型；人工审核员标注金标准值，并配合一个 LLM 评判 [[1]](#sources)。
2. 在生产中，从文本和图像中抽取每个商品的属性 [[1]](#sources)[[2]](#sources)。
3. 置信度来自第二个“评分提示词”（Instacart），或来自用人工标签训练的独立 QC 模型（Walmart） [[1]](#sources)[[2]](#sources)。
4. 🛑 **审阅**：低置信度的值交给人工审核员修正 [[1]](#sources)。
5. 🛑 **抽检**：定期对新商品抽样评估，以发现质量下滑 [[1]](#sources)。

**产出：** 写入商品目录数据管道的属性值。
**失败模式 → 防护：** 随着商品目录变化而悄然漂移 → 定期抽样。看似合理但错误的值 → 独立的验证器/QC 模型。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点位置不同。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Instacart, PARSE](https://tech.instacart.com/multi-modal-catalog-attribute-extraction-platform-at-instacart-b9228754a527) (2025-08-01)。自助式平台，生产环境中有人在回路中做修正。"our initial prompt for organic extraction gave us a 95% accuracy"；"one day of effort, compared to one week previously"。*第一手：是；可信度：中。*
