---
id: AWF-0057
name: 工程师把关的 CFD 仿真
summary: "根据需求说明搭建并运行 OpenFOAM 流体仿真，输出验证报告；工程师审核假设和物理结果。"
deliverable: 经验证的仿真报告
shape: "物理需求说明 + git 中的粗略算例 → 智能体搭建算例并编写假设文档 → 🛑 plan (工程师检查物理选择) → (网格 ⟲ 网格检查) → (求解 ⟲ 收敛检查) → 后处理 + 与参考结果/手算对比 → 🛑 review (工程师检查物理合理性)"
source_hash: 4cbc900cd0a6
---

# 工程师把关的 CFD 仿真

**与相近工作流的区别：** 暂无相近者。SRE 和 FEAT 类工作流作用于代码，本工作流作用于求解器算例，验收关口是物理验证。
**工具变体：** `openfoam` · `snappyhexmesh` · `gmsh` · `calculix` · `paraview-pvpython`

## 步骤

1. 照常创建 CAD 和计算域。把一个粗略的 OpenFOAM 算例放进 GitHub 仓库，这样智能体做的每一处改动都能做 diff [[3]](#sources)。
2. 智能体根据一份自然语言的需求说明搭建算例：求解器选择、湍流模型、由第一性原理推导的入口湍流、计算域尺寸。它还会写一份文档，列出所用的方程、假设和取值 [[2]](#sources)[[3]](#sources)。
3. 🛑 **计划**：工程师先阅读假设文档和 git diff，再决定是否信任这套设置 [[3]](#sources)。在基于工具的版本中，由人批准受控的操作 [[1]](#sources)。
4. 划分网格并检查网格。如果求解发散，智能体会检查并重新生成网格。编写网格研究脚本（例如三套 snappyHexMesh 网格），运行并修正错误 [[2]](#sources)[[3]](#sources)。
5. 求解直到收敛。把求解器的收敛信息与正常退出和发散检测交叉核对，因为超时和被强制终止看上去可能像收敛 [[1]](#sources)。如果算例不收敛，再次加密网格 [[3]](#sources)。
6. 用脚本化的 ParaView/Python 绘图做后处理。把结果与已发表的实验或参考算例对比，在 FEA 变体中则与手算对比 [[1]](#sources)[[4]](#sources)。对效率大于 1 之类的非物理结果要标记出来，而不是掩盖 [[1]](#sources)。
7. 🛑 **审阅**：负责的工程师在做任何设计决策之前，先检查物理合理性和验证结果。作者强调，在与实验对照之前，这些结果只是未经验证的预测 [[2]](#sources)[[3]](#sources)[[4]](#sources)。

**产出：** git 中一个已收敛的算例、绘图和渲染图，以及一份含“验证结果与参考值对比表”的报告。它交给负责签字做设计决定的工程师。
**失败模式 → 防护：** 边界条件错误却依然收敛（旋转壁面被留成 noSlip，叶片从未转动）→ 旋流探针，加一份依赖人工判断的诊断清单 [[1]](#sources)。虚假收敛 → 收敛交叉核对 [[1]](#sources)。看似合理但错误的湍流选择 → 工程师审阅假设文档以及与实验的对比 [[2]](#sources)[[3]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [jwjoo00, myOpenFoamAgent](https://github.com/jwjoo00/myOpenFoamAgent) (2026-08-01)。由智能体运行螺旋桨 MRF 算例，并对照已发表的实验验证，受控操作需人工批准。"Kt = 0.1476 vs 0.146 measured"。*第一手：是；可信度：高。*
- [Fayaz Rasheed, LLM-Orchestrated CFD](https://fayazrasheed.com/blog/llm-orchestrated-cfd-bear-aerodynamics.html) (2026-06)。完整的网格—求解—优化—渲染研究；作者标明结果未经验证。"a reshaped belly brought it down to 0.593, a 9.2% reduction"。*第一手：匿名（工程师未具名）；可信度：中。*
