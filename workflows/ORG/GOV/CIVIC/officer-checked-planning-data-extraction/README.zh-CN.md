---
id: AWF-0143
name: 规划档案数据提取与人工核验
summary: "从扫描的规划档案中提取字段与地图边界；规划官员逐项核对后才导出至国家平台。"
deliverable: 结构化规划数据集
shape: "上传扫描的规划档案 (TPO、保护区、Article 4) → 按模式提取文本字段 → 将地图边界描绘为多边形 → 地理配准到 Ordnance Survey → 🛑 review (规划官员核对并修正每一项输出) → 导出标准格式 → 国家 Planning Data Platform"
source_hash: ebc55cc5f8c2
---

# 规划档案数据提取与人工核验

**与相近工作流的区别：** AWF-0082 模型分流的档案解密（Model-triaged records release）中，分类器决定是否解密，只有不确定的档案交给人，质检为抽样。本工作流的产出是由扫描规划档案生成的结构化地理空间数据集，官员在导出前对每一项输出都做审阅和修正。产出不同，且是全量审阅而非抽样。
**工具变体：** `extract`

## 步骤

1. 规划官员用 GOV.UK 邮箱登录，上传 PDF 或扫描件，例如树木保护令（Tree Preservation Order）、保护区（Conservation Area）或 Article 4 Direction [[1]](#sources)。
2. LLM 用结构化输出，把日期、地点和决定提取到 Digital Planning 平台的模式中 [[2]](#sources)。
3. 视觉语言模型结合 OpenCV 和 SAM，把地图边界描绘成多边形 [[2]](#sources)。
4. 系统对照 Ordnance Survey 地图寻找地面控制点，把每个多边形对齐到真实世界坐标 [[2]](#sources)。
5. 🛑 **审阅**：官员“review everything that Extract produces, check the output and makes corrections”[[1]](#sources)。
6. 官员以标准化格式导出数据，用于自己的系统和国家 Planning Data Platform [[1]](#sources)。

**产出：** 经过地理配准、符合模式的规划数据集，存入市议会系统并发布在公开的 Planning Data Platform 上。
**失败模式 → 防护：** 边界错位 → alpha 阶段的 IoU 和中心距离检查，加官员修正。日期误读（alpha 阶段正确率 94%）→ 官员检查每个字段。准确率看起来很高后产生过度信任 → 审阅全部输出，而非抽样。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [MHCLG, Extract live for every council](https://mhclgdigital.blog.gov.uk/2026/06/17/extract-is-here-ai-powered-planning-data-for-every-council-in-england/) (2026-06-17)。已上线的服务：50 个市议会在使用；官员审阅所有输出；多数只需少量修改。"In around two thirds of cases, only minor edits were needed before the data was ready to use"。*第一手：是；可信度：高。*
- [MHCLG, Extract alpha](https://mhclgdigital.blog.gov.uk/2025/06/12/extract-using-ai-to-unlock-historic-planning-data/) (2025-06-12)。alpha 阶段在文本、日期和边界上的准确率；每份档案的成本和耗时。"The system identified dates correctly 94% of the time."。*第一手：是；可信度：中。*
