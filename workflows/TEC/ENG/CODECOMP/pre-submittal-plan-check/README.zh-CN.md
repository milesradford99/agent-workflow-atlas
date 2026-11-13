---
id: AWF-0117
name: 报建前图纸预检
summary: "在提交前对报建图纸集生成按专业和严重程度排序的问题清单；设计公司甄别真伪问题。"
deliverable: 报建前问题清单
shape: "完整报建图纸集 (PDF) → AI 检查规范 + 跨专业协调 → 按专业 + 严重程度排序的问题清单 → 🛑 review (公司甄别真问题与非问题) → 绘图员修复 → 提交市政府 → 🛑 handoff (市政府图纸审查) → 将非问题记录为工具反馈"
source_hash: 265a59ddc41b
---

# 报建前图纸预检

**与相近工作流的区别：** 最接近的是 AWF-0058（带引证的预筛查检查），它运行在监管方一侧：申请人修复被标记的检查项，市政府审查员批准每一项判定。这里是设计公司在提交前对自己的整套图纸运行检查，并自行甄别误报。市政府的审查是之后的接手，而不是检查点，因此使用者、产出和检查点的负责人都不同。
**工具变体：** `inspectmind` · `archiboost` · `ichi` · `bluebeam`

## 步骤

1. 设计公司上传它计划提交的完整图纸集（建筑、市政、结构、规格说明） [[1]](#sources)[[2]](#sources)。
2. AI 依据规范和标准并跨专业进行检查，返回按专业和严重程度排序的问题清单 [[2]](#sources)。
3. 🛑 **审阅**：公司把每条标记甄别为真问题或非问题。在一家公司，约四分之一是真问题。公司保留自己的 QA/QC 流程 [[1]](#sources)。
4. 绘图员在提交之前修复已确认的问题 [[2]](#sources)。
5. 🛑 **接手**：市政府自行做图纸审查。公司记录非问题，并发给工具厂商以改进检查 [[1]](#sources)[[2]](#sources)。

**产出：** 提交的是已清理的报建图纸集，留给市政府发现的问题更少，并附一份已甄别的问题日志。
**失败模式 → 防护：** 误报率高（在 Charlan Brock 约每 4 条标记中有 1 条是真问题）→ 修复前先由公司甄别。浅层工具漏掉已知违规 → 以公司自己的 pre-IFC 评审清单做基准。过度依赖 → 保留内部 QA/QC；AI 只是“多一双眼睛” [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [InspectMind, Charlan Brock Architects case study](https://www.inspectmind.ai/case-studies/charlan-brock-architects) (undated)。750 多张图纸的多户住宅报建图纸集；AI 发现了公司自己的 pre-IFC 评审漏掉的问题；公司甄别了误报。"at least 97 others that had escaped their pre-IFC review"；"roughly a quarter of flagged issues being legitimate"。*第一手：厂商；可信度：中。*
- [InspectMind, Owens Design church project](https://www.inspectmind.ai/case-studies/owens-design-church) (undated)。公司在提交市政府之前修复了 AI 标记的问题；市政府的意见很轻微。"The AI plan checker flagged ~300 issues"。*第一手：厂商；可信度：中。*
