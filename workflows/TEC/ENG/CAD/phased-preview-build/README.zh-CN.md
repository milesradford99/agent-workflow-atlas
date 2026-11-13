---
id: AWF-0056
name: 分阶段预览的 CAD 建模
summary: "分三个阶段生成带预览的参数化 CAD 模型；每阶段的预览和切片结果都由制作者确认后再打印。"
deliverable: 参数化 CAD 模型
shape: "收集需求 + 调研尺寸 → 各阶段（基础形体、特征、收尾）：(CadQuery 脚本 → STL → 四视图渲染 ⟲ 清单自查) → 🛑 review (预览) → 参数表 + STL → 切片 → 🛑 review (切片软件/打印适配)"
source_hash: f7860e5e02a9
---

# 分阶段预览的 CAD 建模

**与相近工作流的区别：** 目录中暂无相近者。AWF-0007 和 AWF-0008 产出的是 UI 代码，而不是实体几何。
**工具变体：** `cadquery` · `trimesh-pyrender`

## 步骤

1. 在对话中收集需求，然后调研零件必须适配的真实尺寸。在 MagSafe 支架这个实例中，这指的是充电盘尺寸、线圈位置和线缆直径；在手机壳实例中，则是 Apple 的配件设计指南 [[1]](#sources)。
2. 分三个可视化阶段搭建：先是基础形体，再是特征，最后是收尾清理。绝不直接跳到成品模型，因为基础形体一旦错了，细节工作就白做了 [[1]](#sources)。
3. 每个阶段都编写参数化的 CadQuery 脚本，运行后得到 STL，再用 trimesh/pyrender 渲染四视图预览。智能体会查看自己的渲染图 [[1]](#sources)。
4. 对照设计清单自查每一张预览：是否符合需求、特征是否可见、底面是否平整以便贴合打印床、悬垂角是否小于 45 度、壁厚是否大于 1.2mm。在给人看之前先迭代 [[1]](#sources)。
5. 🛑 **审阅**：每个阶段结束时，制作者查看预览并给出修改意见，例如“再高 5mm”或“线缆孔没有打通”。然后才进入下一阶段 [[1]](#sources)。
6. 交付 STL，以及一张包含所有关键参数的表，方便快速调整 [[1]](#sources)。
7. 🛑 **审阅**：制作者对零件做切片，并把切片软件的截图作为反馈发回来。这样能在浪费耗材之前发现结构和间隙问题 [[1]](#sources)。

**产出：** 一份参数化的 CadQuery 脚本和 STL，附参数表，可直接切片打印。之后的改动通过编辑参数完成。
**失败模式 → 防护：** 布尔运算静默失败、壳体太薄无法打印、特征切反了方向（按键凹进去而不是凸出来）→ 每张预览的清单自查，加上每个阶段的人工预览关卡。几何不稳定或无法使用（支架会倒）→ 真实的切片软件反馈，加上由人判断实际使用情况。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Nicolas Chourrout, I Taught Claude to Design 3D-Printable Parts](https://pub.towardsai.net/i-taught-claude-to-design-3d-printable-parts-heres-how-675f644af78a) (2026-03-05)。通过分阶段预览和切片软件反馈，做出了 MagSafe 支架和 TPU 手机壳。"Four exchanges, including real slicer feedback with screenshots"; "Final model: 76 x 70 x 125mm"。*第一手：是；可信度：高。*
