---
id: AWF-0116
name: 智能体辅助的 PCB 原理图
summary: "根据手绘草图生成 KiCad 原理图和投板资料；设计师确认方案及每一步，另一位工程师评审原理图。"
deliverable: PCB 投板资料包
shape: "草图 + 尺寸限制 → 概念渲染图 → 智能体起草需求文档 + BOM + 框图 → 🛑 plan → 逐步：智能体构建 KiCad 原理图，🛑 action (设计师确认每一步) → (对抗式原理图评审 ⟲ 修复) + ERC 和网表导出 → 🛑 review (第二位工程师) → 手工 PCB 布局 → 导出投板资料 → 下单 → 调试上板"
source_hash: 8d94c4b59c51
---

# 智能体辅助的 PCB 原理图

**与相近工作流的区别：** 最接近的是 AWF-0056（分阶段预览构建），它为 3D 打印零件循环执行 CadQuery → STL → 渲染，并带预览审阅。本工作流产出的是电气原理图和投板资料包。其检查手段是 ERC/网表加对抗式 LLM 评审，设计师确认每一步，下单前由第二位工程师评审。
**工具变体：** `openai-codex` · `claude-code` · `kicad-cli` · `kicad-happy` · `jlcpcb`

## 步骤

1. 从尺寸限制内的手绘草图开始。生成几张概念渲染图 [[1]](#sources)。
2. 智能体起草技术需求文档、核心 BOM 和框图，并根据 LCSC 查询估算成本。🛑 **计划**：设计师审阅并修订这些内容 [[1]](#sources)。
3. 编码智能体根据 BOM 逐步构建 KiCad 原理图，用 easyeda2kicad/pcbparts 选型元件。🛑 **操作**：设计师确认每一步，并负责布局和连线的决定 [[1]](#sources)。
4. 要求做一次对抗式原理图评审，并写入 markdown 文件。修复发现的问题，反复进行直到没有新问题。用 kicad-cli 做 ERC 和网表导出检查，并把真正的问题与导入产生的噪声区分开 [[1]](#sources)。
5. 🛑 **审阅**：第二位工程师评审原理图（30 分钟）。然后手工完成 PCB 布局，导出生产资料包，并订购电路板和贴装 [[1]](#sources)。
6. 调试上板：智能体先写自检固件。设计师在工作台上排查硬件故障 [[1]](#sources)。

**产出：** 一份经评审的 KiCad 原理图，以及向 PCB 厂下单的投板/贴装资料包，另有调试用固件。
**失败模式 → 防护：** LLM 丢失整个项目的全局视角，并在元件没有模型时漏掉故障（开关引脚短路使 BOOT0 被拉低）→ 由人做第二次评审，并在工作台上调试上板。导入元件产生的 ERC 噪声 → 以网表得出真正的发现 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点位置不同。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Federico Maggi, I let GPT + Opus build a wearable PCB badge](https://trustial.substack.com/p/i-let-gpt-opus-build-a-wearable-pcb) (2026-08-04)。原理图由智能体起草，经对抗式评审循环和人工评审；电路板已制作，有一处故障智能体没有发现。"5" badges at "~$66" each; adversarial review took "4 minutes"。*第一手：是；可信度：中。*
