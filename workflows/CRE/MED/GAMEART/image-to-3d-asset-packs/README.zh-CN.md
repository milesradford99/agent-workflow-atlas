---
id: AWF-0140
name: 图生 3D 资产包
summary: "由概念图生成可入引擎的 3D 资产包；美术师筛选生成结果，并完成拓扑、UV 和外观收尾。"
deliverable: 可入引擎的 3D 资产包
shape: "参考资料 → 草图 (美术师 + 2D AI) → 无透视畸变的多视图概念图 → 每个 资产：(图生 3D 高模 ⟲ 重新生成) → 🛑 review (美术师保留或舍弃) → ZBrush 清理 → 重拓扑 + UV (AI 起步，美术师收尾) → 贴图 (生成 PBR，复杂资产手工制作) → 🛑 review (美术师收尾拓扑/UV/外观) → 渲染 + Unity/Unreal 装配"
source_hash: ed874dc129fd
---

# 图生 3D 资产包

**与相近工作流的区别：** AWF-0079 概念图驱动的 SD 资产流（Concept-led SD asset stream）用自训练模型，根据美术师的概念图制作 2D 资产。本工作流产出带重拓扑、UV 和烘焙的可入引擎 3D 网格，并为生成结果增加了保留/舍弃的筛选环节。产出不同，多出的检查点也不同。
**工具变体：** `meshy` · `tripo` · `zbrush` · `blender` · `substance-painter`

## 步骤

1. 收集参考资料，然后手绘草图，或用 2D AI 模型（通过 Fal）生成草图 [[1]](#sources)。
2. 准备无透视畸变、专为 3D 生成而做的多视图概念图 [[1]](#sources)。
3. Meshy 用 Image-to-3D 或 Multi-Image-to-3D 构建高模，按需重新生成 [[1]](#sources)。
4. 🛑 **审阅**：美术师筛选生成结果。约 20–30% 到不了生产环节，约 30% 还需要多轮调整，角色大约有 60–70% 的情况需要重新生成 [[1]](#sources)。
5. 在 ZBrush 中清理高模。Meshy 的重拓扑提供一个起点，美术师在 Blender 或 TopoGun 中收尾，AI 助手承担一部分常规 UV 工作 [[1]](#sources)。
6. 贴图从 Meshy 生成的 PBR 贴图开始。复杂资产在 Substance Painter 中手工处理 [[1]](#sources)。
7. 🛑 **审阅**：凡是需要精确的地方，美术师手工完成拓扑、UV 和最终外观，然后做最终渲染，并在 Unity 或 Unreal 中装配 [[1]](#sources)。

**产出：** 带烘焙 PBR 的可直接用于游戏的低模资产，打包成适用于 Unity 和 Unreal 的资产包。
**失败模式 → 防护：** 汽车和复杂角色的拓扑差、UV 凌乱 → 美术师手工重建。角色的保留率低 → 多视图概念图加多轮重新生成，并由美术师筛选。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [RetroStyle Games, Asset Packs in a Week](https://retrostylegames.com/blog/asset-packs-in-a-week-meshy-case-study/) (2026-10-15)。Grand Theft Motel 资产包（19 个独立资产、66 个预制体）一周内完成。"about 20 to 30% of generated models did not make it into production"；一个资产包耗时 "about a week"，而非 "about a month"（粗略估计，据该页面）。*第一手：是；可信度：高。*
