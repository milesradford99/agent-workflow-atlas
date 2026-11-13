---
id: AWF-0079
name: 概念图驱动的 SD 美术资产
summary: "基于美术概念图，用定制训练的图像模型生成游戏美术资产；美术师逐项调整并批准。"
deliverable: 游戏美术资产
shape: "选定工具 + 准备风格数据集 → 训练定制模型 → 🛑 plan (美术师的概念图) → 每个资产：从概念图、草图或 3D 白模出发做 img2img/ControlNet → 放大 → (美术师修整 ⟲ 达到目标) → 🛑 review (美术师批准)"
source_hash: db2fc9ecb559
---

# 概念图驱动的 SD 美术资产

**与相近工作流的区别：** AWF-0015 AI 镜头工厂为短剧制作视频镜头。AWF-0008 设计到代码针对的是 UI。游戏资产方面没有相近的工作流。
**工具变体：** `stable-diffusion-controlnet`

## 步骤

1. 选择支持微调和局部重绘（inpainting）、并可本地安装的工具（Stable Diffusion）。为每个新的美术系列准备数据集（几个小时），并训练定制模型；团队训练了 100 多个（hypernetworks、embeddings）来找到有效的参数 [[1]](#sources)。
2. 由专门的内部 AI 部门负责工具分析、训练、流水线集成和对美术师的支持 [[1]](#sources)。
3. 🛑 **计划**：先由美术师做出详细的概念图，因为只靠文字提示词的结果难以预测 [[1]](#sources)。
4. 用 img2img 从概念图出发生成。场景元素可以从草图加文字开始，背景可以从基础 3D 模型出发，用低去噪强度（最高 0.4）和/或 ControlNet 来确定角度和构图。细节复杂或带动画的物体按部件分别生成 [[1]](#sources)。
5. 放大后，美术师手工修整，直到资产达到目标。🛑 **审阅**：美术师批准或重做输出；一份类似的复盘提到美术师拥有“艺术否决权”（'artistic veto power'）[[1]](#sources)[[2]](#sources)。

**产出：** 2D 游戏资产（可收集的卡牌、装饰、背景），交给游戏的美术集成环节。
**失败模式 → 防护：** 结构瑕疵和风格不一致 → 美术师在上面重绘、融合并拼接多次生成的结果，同时用风格训练过的模型保持外观一致。只靠提示词的输出不可预测 → 始终从概念图、草图或 3D 输入出发。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或把检查点放在了别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Belka Games, Working AI into your art pipeline](https://www.pocketgamer.biz/feature/81986/working-ai-into-your-art-pipeline-expectations-vs-reality/) (2023-07-17)。Solitaire Cruise 的一套收藏卡牌，用 AI 流水线制作，而不是概念图加 2D 渲染。10 张卡牌的收藏系列，用 AI 约需 3 工时，传统方式约需 240 工时。*第一手：是；可信度：中。*
