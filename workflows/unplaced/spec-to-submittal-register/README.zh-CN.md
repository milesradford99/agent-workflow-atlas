---
id: AWF-0190
name: 规范书生成报审清单
summary: "从规范书中提取全部报审要求，生成报审清单和移交函；项目工程师核实后发出。"
deliverable: 报审清单
shape: "规范书 PDF → 识别 CSI 章节编号 → 分块 + 嵌入 + 建索引 → 每个章节: 提取报审要求 + 条件说明 → 起草清单 (Excel) + 移交函 (Word) → 🛑 review (项目工程师核实条目、删除重复、补全遗漏) → 向分包商发出清单 + 移交函"
source_hash: 2bed53f6e4da
---

# 规范书生成报审清单

**与相近工作流的区别：** AWF-0151 首轮报审审查（First-pass submittal review）把分包商已经提交的报审资料对照规范书检查，最终由建筑师处置。本工作流是在任何报审资料到达之前，生成所需报审资料的清单；产出物是这份台账，唯一的检查点是项目工程师的核实，没有设计师签发。
**工具变体：** `custom-rag-gpt-4o-mini` · `pype-autospecs`

## 步骤

1. 把项目规范书 PDF（800 到 1,500 页）上传到工具中；文本按页提取 [[1]](#sources)。
2. 用针对 CSI SectionFormat 编号调校过的正则表达式识别并切分规范章节（例如 "07 21 00"、"072100"），无需任何手工标记 [[1]](#sources)。
3. 把每个章节切成相互重叠的块，嵌入后存入向量索引；扫描图像和图纸不在其内 [[1]](#sources)。
4. 针对每个章节（或用户查询，例如 "List all submittals under 07 21 00"），检索相关块，让模型返回结构化的行：章节编号、报审要求、条件说明 [[1]](#sources)。
5. 把这些行导出为可直接用于移交的 Excel 清单和 Word 移交函 [[1]](#sources)。商业工具把同一步骤做成一次性的台账草稿 [[2]](#sources)。
6. 🛑 **审阅**：项目工程师在台账投入使用前，核实提取的条目，并纠正误分类和重复的行；作者报告有些条目 "required expert review" [[1]](#sources)。在 Mortenson，起草环节节省下来的时间被用于 "more thorough reviews" [[2]](#sources)。
7. 向分包商发出经核实的清单和移交函；清单随后驱动报审审查周期（见 AWF-0151）。

**产出：** 一份经核实的报审清单（Excel）加移交函，在项目开始时发出，用于跟踪每一项所需的报审。
**失败模式 → 防护：** 语义漂移会让相邻段落中相似的措辞产生重复条目；过长的条款超出上下文窗口，丢掉次要条件 → 更小的分块、自适应提示词，以及项目工程师的逐行审阅 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [Kalasapudi et al., Frontiers in Built Environment](https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2025.1713342/full) (2026-01-02)。与一家土木承包商合作的同行评审现场测试；在 10 份 800–1,500 页的规范书上做基准测试；保留对条目的人工审阅。"Average end-to-end processing time was approximately 6–8 min per document"; "total computational costs under USD 0.10 per file"。*第一手：研究；可信度：高。*
- [Pype, Mortenson case study](https://www.casestudies.com/company/pype/case-study/mortenson-scales-accuracy-quality-of-submittal-log-review-with-pype) (n.d.)。大型总承包商自动起草报审台账，然后再审阅；发现了更多报审项。"reduced the time spent creating a draft log by 99%, from 34 hours down to under 5 minutes"。*第一手：厂商；可信度：中。*
