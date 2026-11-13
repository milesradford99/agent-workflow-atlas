---
id: AWF-0236
name: 农艺师把关的推送农事建议
summary: "按农户分群起草、翻译并配音每周作物建议；农艺师在外呼推送前审阅，并解读 A/B 测试结果。"
deliverable: 配音农事建议推送活动
shape: "农艺师知识 (作物日历、最佳实践、往期建议) + 农户分群 (作物、农场规模、天气、偏好) → 为每个分群起草建议 → 翻译成当地语言 → 文字转语音 → 🛑 review (农艺团队和服务交付团队在发布前检查建议) → 每周 IVR 推送外呼 → 与人工撰写的建议做 A/B 测试 (收听率、记忆回访调查) → 🛑 review (团队阅读结果并对比脚本) → 调整提示词 / 保留可操作的细节"
source_hash: 2d21abddfdef
---

# 农艺师把关的推送农事建议

**与相近工作流的区别：** AWF-0211（推广员中介的建议，extension-agent mediated advice）回答单个农户的问题，每个答案由推广员转达。AWF-0154 一次为一位农户提供按地块登记的当季建议。本工作流中没有人提问：农艺师批量发布分群、配音的推送活动，随机化 A/B 评估是第二个检查点。交付物、触发方式和检查点都不同。
**工具变体：** `paddyai` · `ivr-push-calls`

## 步骤

1. 农艺师提供知识：作物日历、最佳实践、季节性指导和往年建议的存量。农户属性（作物类型、农场规模、当地天气、沟通偏好）划分出各个分群 [[1]](#sources)[[2]](#sources)。
2. PaddyAI 为每个分群起草一份建议，翻译成当地语言（咖啡服务用卡纳达语），并转成语音通话用的音频。它能生成农艺师无法手工写出的大量定制版本 [[1]](#sources)[[2]](#sources)。
3. 🛑 **审阅**：农艺团队和服务交付团队保持在环，确保发给农户的每条建议都合适。早期版本还在农户焦点小组中测试过可理解性 [[1]](#sources)。
4. 建议通过 Coffee Krishi Taranga 服务每周发出一次 IVR 推送外呼，该服务由 PxD 与印度咖啡局（Coffee Board of India）共同运营 [[2]](#sources)。
5. 效果以对照人工撰写、真人配音建议的 A/B 测试来衡量：接听率、收听率和平台数据中的收听时长，另有电话回访调查，了解记忆和理解情况 [[2]](#sources)。
6. 🛑 **审阅**：团队把结果与脚本本身对照阅读，发现 AI 脚本有时会漏掉具体的建议操作或技术细节，于是调整 PaddyAI，保留这些可操作的内容 [[2]](#sources)。

**产出：** 面向每个农户分群、用当地语言配音的每周农事建议，通过 IVR 平台送达，另有一条实验登记条目，用来驱动下一轮提示词修订。
**失败模式 → 防护：** AI 脚本做了简化，丢掉可操作或技术性的细节 → 发布前由农艺师审阅，A/B 测试后逐个脚本对比。参与度低于人工脚本（收听率低 2–3.5 个百分点）→ 扩大规模前设 A/B 关卡。项目页面初步声称参与度略高，最终登记结果并不支持；请引用登记结果。登记页面的摘要说 AI 脚本“tend to be longer”，结果部分却写“12% shorter”；请采用结果部分的数字。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [PxD, Paddy AI A/B test 1](https://registry.precisiondev.org/registry_entry/paddyai-a-b-test-comparing-engagement-metrics-for-ai-enabled-ivr-advisories/) (2026-10-13)。2025 年 11 月至 2026 年 2 月共 11 期每周建议，发给咖啡农户，随机分到人工与 AI 脚本/配音各组。"We randomly assigned 28,796 coffee farmers"; "The average listening rate is 2pp lower for AI-generated, AI-voiced advisories (3.6% decrease, p<0.05)"; "a 6.3% lower recall rate"。*第一手：是；可信度：高。*
