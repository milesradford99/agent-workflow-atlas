---
id: AWF-0059
name: 图纸生成工艺路线草案
summary: "根据 BOM 和图纸生成含工位与工时的工艺路线草案；班组长调整后下发生产。"
deliverable: 制造工艺路线
shape: "从 PLM 拉取 BOM + CAD → 提取图纸特征 → 解读特征 → 应用知识库规则（工艺、工位、工时）→ 起草路线 → 🛑 review (班组长调整并放行) → 下发生产 → 记录修改 → 更新知识库"
source_hash: 63cf79d015c8
---

# 图纸生成工艺路线草案

**与相近工作流的区别：** 暂无相近者。AWF-0022 发票提取—匹配—路由（invoice extract-match-route）把文档转成已路由的交易，但属于财务领域，交付物和审批人都不同。
**工具变体：** `plm-extract` · `vision-llm` · `rules-kb`

## 步骤

1. 从 PLM 系统拉取每个新零件的 BOM 和 CAD 图纸 [[1]](#sources)。
2. 先用图像处理提取特征，再用视觉推理模型解读，识别每个工件所需的工艺（折弯、铣削、钻孔、焊接等）[[1]](#sources)。
3. 应用结构化的知识库，其中包含工位规则、工艺定义和工时逻辑。生成一份带工位分配和工时估算的路线草案 [[1]](#sources)。
4. 🛑 **审阅**：班组长检查路线草案，按需调整，并提交给生产。任何输出都可以手工修正 [[1]](#sources)。
5. 记录每一处修改。班组长随工艺演进更新知识库，系统因此不断改进 [[1]](#sources)。

**产出：** 一份已放行的工艺路线（工序、工位、工时），交给生产排程和班组。
**失败模式 → 防护：** 专业图纸没有任何单一模型能读懂 → 分层流水线（图像特征 → 视觉推理 → 规则知识库）。路线有误 → 强制班组长审阅并放行，修改日志回流到知识库 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [HKU CAMO, Scaling Expert Knowledge with AI at CIMC](https://camo.hku.hk/nanocase-scalingexpertknowledgewithaiatcimc/) (2026-03-31)。中集天达的工艺路线智能体起草路线；班组长审阅并放行。"the dedicated staffing footprint has decreased from 18 people to 2"; "accuracy has reached approximately 95%"。*第一手：否（第三方学术案例研究）；可信度：中。*
