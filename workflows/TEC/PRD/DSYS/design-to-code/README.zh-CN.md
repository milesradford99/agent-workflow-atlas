---
id: AWF-0008
name: 设计稿转代码
summary: "借助 Figma MCP，用已映射的组件和设计令牌把设计稿转成 UI 组件代码；设计师在预览版中评审。"
deliverable: UI 组件代码
shape: "设计稿链接 → 加载设计上下文、令牌、组件映射 → (写代码 ⟲ 截图对比) → 🛑 review → PR"
source_hash: 309b0cd85432
---

# 设计稿转代码

**工具变体：** `storybook-mcp` · `claude-design`

## 步骤

1. 通过 Figma MCP 服务器拉取设计稿的设计上下文、变量（颜色、间距、字体）和 Code Connect 映射 [[7]](#sources)。
2. 复用已映射的代码组件，不要重新创建。
3. 只使用设计令牌，不写死任何数值。
4. 渲染、截图、与 Figma 截图对比，并循环修正。
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
