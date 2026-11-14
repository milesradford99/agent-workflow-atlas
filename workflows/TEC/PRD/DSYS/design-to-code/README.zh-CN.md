---
id: AWF-0008
name: 设计稿转代码
summary: "借助 Figma MCP，用已映射的组件和设计令牌把设计稿转成 UI 组件代码；设计师在预览版中评审。"
deliverable: UI 组件代码
shape: "设计稿链接 → 加载设计上下文、令牌、组件映射 → (写代码 ⟲ 截图对比) → 🛑 review → PR"
source_hash: e672f58dba9e
---

# 设计稿转代码

**工具变体：** `storybook-mcp` · `claude-design`

## 背景

设计师在视觉文件里描述界面，开发者则用产品已有组件实现交互。单张截图不能说明应该采用哪个组件、间距规则或可复用样式，因此外观相似的代码仍可能偏离产品系统。本工作流给编码智能体提供结构化设计背景，并把渲染结果与设计稿比较。预览仍由设计师审阅，因为视觉相似并不能证明交互正确、无障碍行为合适，或者组件选择得当。

**术语：**
- **画框 / 组件映射（frame / component map）**：设计界面或选区，以及它与真实代码组件的对应关系。
- **设计令牌**：有名称的颜色、间距和字体值，用于复用而非写死数值。
- **MCP / CLI**：连接外部工具与智能体的协议，以及命令行界面。
- **截图 diff / PR**：渲染图像的比较，以及提议的仓库修改。
- **DS / 类型检查（typecheck）**：设计系统，以及检查代码是否正确使用声明类型的自动化检查。

## 用智能体搭建

**形态：** `project`。除 Skill 外，还需要适用于仓库的组件规则与可重复的验证关卡。

**需要：** 画框链接；获批的 Figma 和设计系统 MCP server (connector) 工具；当前组件映射与令牌定义；仓库、预览命令和截图比较脚本。用 `CLAUDE.md` 保存约定，用 Skill 保存实现流程。保护无关文件，不授予智能体合并或生产部署权限。

| 步骤 | 搭建方式 |
|---|---|
| 设计稿链接 → 加载设计上下文、令牌、组件映射 | Skill 通过 MCP server (connector) 工具读取设计背景与映射；权威组件资料不可用时停下。 |
| 写代码 ⟲ 截图对比 | Skill 复用映射组件并渲染预览；脚本比较截图。Hook 运行项目的令牌、组件和构建检查。 |
| 🛑 review → PR | Skill 展示预览、截图、diff 和未解决的令牌缺口。设计审阅之后，准备 PR 进入常规工程流程。 |

**检查点：** `review`：设计师检查运行中的预览及截图差异，也查看静态图片无法证明的状态。智能体不能合并或部署；代码托管平台的必需审阅把关生产发布。截图比较不能免除功能或无障碍检查。

**与来源相比：** 证据出自 2026-08 至 2026-09，另有未标日期的文档。2026-11 已打开 Coinbase 记录、BILL 记录和 Figma 指南；Doctolib 的 Medium 页面拒绝访问。检索发现 [Figma 当前的工具文档](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)，已于 2026-11 打开，列出了设计上下文、变量、截图和 Code Connect 工具。这样可以获取结构化背景，不必定制抓取器，但不会自动补齐缺失映射，也不能验证无法访问的 Doctolib 结果。保留来源中设计系统资料不可获取时必须停下的规则；报告组件或令牌缺口，不靠猜测补齐。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 智能体通过 Figma MCP 服务器拉取设计稿的设计上下文、变量（颜色、间距、字体）和 Code Connect 映射 [[7]](#sources)。
2. 智能体复用已映射的代码组件，不要重新创建。
3. 智能体只使用设计令牌，不写死任何数值。
4. 智能体渲染、截图、与 Figma 截图对比，并循环修正。
5. 🛑 **审阅**：设计师在预览版中评审。

**产出：** 一个 PR。设计令牌的缺口反馈给设计系统团队。

**近期实践（2026）：**
- 加载设计上下文：如果设计系统的 MCP/CLI 无法连接，就停下，不要猜测（BILL 2026-08-17）。[[9]](#sources)
- 写代码 ⟲ 检查：生成后，对照带版本的设计系统清单自审并给合规度打分；把偏差分为缺少 AI 上下文、缺少设计系统能力、合理的自定义 UI 三类（Doctolib 2026-09-15）。[[8]](#sources)

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。更新见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Jenny Xie, Figma blog, on Coinbase](https://www.figma.com/blog/how-coinbase-used-code-connect-to-shrink-token-costs/) (2026-09-02)。设计稿链接 → MCP + Code Connect → 智能体实现；由设计师检查组件。"cost by 22.5%"；"time to implementation by 22.3%"；共三次运行。*第一手：厂商；可信度：中。*
- [Theophile Kalumbu, Doctolib, Keeping AI on Track: Lessons from Doctolib’s Oxygen Design System](https://medium.com/doctolib/keeping-ai-on-track-lessons-from-doctolibs-oxygen-design-system-9be5f9f041e8) (2026-09-15)。针对 Oxygen 设计系统的原型转 React 技能，带清单自审、钩子以及类型检查/构建关卡；在真实的功能团队上测试。"This moved compliance from 65% to 87%"；"reach 97% DS compliance"。*第一手：是；可信度：高。*
- [David Cai, BILL, How We Made Our Design System Bilingual](https://www.bill.com/engineering/how-we-made-our-design-system-bilingual) (2026-08-17)。以 Storybook 为后盾的 MCP/CLI 加技能为智能体提供依据；与无依据的智能体做 A/B 测试。"cut token usage by 31–63% per task and held generation time steady at five minutes per run"。*第一手：是；可信度：高。*
