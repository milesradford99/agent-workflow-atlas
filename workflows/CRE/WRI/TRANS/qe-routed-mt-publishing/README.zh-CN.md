---
id: AWF-0199
name: 按质量评估分流的机翻发布
summary: "通过质量评估阈值的机翻界面字符串直接发布；未通过的转人工译后编辑，并按月抽检错误率。"
deliverable: 已发布的本地化字符串
shape: "新字符串 → 复用翻译记忆库的完全匹配 → 排除规则(高影响功能、短字符串) → 人工翻译 | 机翻 → 为每个片段打 QE 分(按语言设阈值) → 通过：不经审阅直接发布 | 未通过：🛑 handoff (人工译后编辑) → 发布 → 🛑 sample (每月核查错误率和客户满意度，重新校准阈值)"
source_hash: 60dab7e3661a
---

# 按质量评估分流的机翻发布

**与相近工作流的区别：** 最接近的是 AWF-0076（术语表支撑的机翻译后编辑连载）和 AWF-0136（术语把关的游戏本地化）。这两个工作流里，每一章或每段文本在发布前都要经过人工译后编辑或 LQA。这里由质量评估（QE）路由器让大部分机翻不经人手直接发布，人只处理未通过的片段并做汇总抽检。自主程度从分段变为抽检，检查点也变成一次接手和一次审计。
**工具变体：** `microsoft-qe-quest-plus-plus` · `taus-epic-qe` · `modelfront`

## 步骤

1. 未改动的字符串和完全匹配（100% 匹配）的字符串从翻译记忆库中复用 [[1]](#sources)。
2. 排除：对客户影响大的字符串（“What's New”、营销、法务）以及不适合机翻的功能，交给人工翻译。排除依据是资源（词数、资源名、开发者注释）或功能。少于 8 个词的字符串同样排除 [[1]](#sources)。
3. 其余新字符串交给机器翻译。每种语言一个 QE 模型（基于特征，每种语言用 100k+ 个片段训练）预测 TER。质量低指预测 TER >0.3 [[1]](#sources)。
4. 按目标错误率为每种语言校准 QE 阈值（每个产品、每种语言、每月新增词数的 10%；历史上人工 LQA 的不合格率为 5%）。在文中的算例里，QE 阈值 0.42 对应 58% 的吞吐量和 62% 的精确率 [[1]](#sources)。
5. 通过 QE 的片段不经人工审阅直接发布，等同于 100% 的翻译记忆库匹配 [[1]](#sources)[[2]](#sources)。
6. 🛑 **接手**：未通过 QE 的片段交给人工译后编辑，与以前一样 [[1]](#sources)[[2]](#sources)。
7. 🛑 **抽检**：监控每种语言的客户满意度和错误率，听取客户反馈，并重新调整阈值 [[1]](#sources)。

**产出：** 随构建发布的本地化软件界面字符串。只有未通过 QE 和被排除的字符串经过了人工处理。
**失败模式 → 防护：** QE 模型并不完美，有些低质量机翻是被有意发布的 → 用明确的错误率预算设上限，并关注客户满意度 [1]。短字符串得分差或有歧义 → 设长度阈值 [1]。QE 过度标记（Yamagata 估计 30% 被标为“差”的其实没问题）→ 按领域微调阈值 [3]。对于用户生成内容，字符串被污染且模型没见过 → 未通过的仍保留译后编辑 [3]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Microsoft (Schmidtke), Scaling up automatic translation for software](https://aclanthology.org/attachments/2020.amta-user.5.Presentation.pdf) (2020-10)。两年来对软件界面做 QE 把关的机翻发布，覆盖 37 种语言，客户满意度保持稳定。"MT now used for 9% of published software translation volumes across 37 languages"; "0.4M VOLUME OF WORDS 'QE PASSED' EACH MONTH"。*第一手：是；可信度：高。*
- [TAUS, Yamagata Europe case study](https://www.taus.net/case-studies/yamagata-saves-up-to-76-in-lead-time-and-costs-with-taus/) (undated)。为保修索赔机翻定制的 QE 模型；“良好”的字符串跳过译后编辑。"65% for the FR-EN language pair and 76% for the DE-EN language pair"。*第一手：厂商；可信度：中。*
- [Custom.MT (Dranch), Automated QE Reduces Cost of Translation](https://custom.mt/quality-estimation-draws-nearer-to-adoption/) (2024-11-06)。BLEND 的客户不再审阅置信度高于阈值的字符串。"The resulting cost saving was 35%, economizing $47k in the pilot project"; "The impact on quality was not measured."。*第一手：访谈；可信度：中。*
