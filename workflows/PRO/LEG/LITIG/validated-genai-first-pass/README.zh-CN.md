---
id: AWF-0035
name: 经验证的生成式初审
summary: "律师在样本上调试审阅提示词后全量运行，并验证精确率与漏检率；责任律师签核。"
deliverable: 相关文件的提交集
shape: "初筛 (去重、邮件串联、检索) → 律师依据审阅规程编写提示词 → (在样本上运行 ⟲ 🛑 review (律师对照标准集)) → 全量运行 → 🛑 sample (精确率 + 漏检率验证) → 律师审阅所有相关/边缘文件的特权问题 → 🛑 sign-off (责任律师接受召回率)"
source_hash: a241cca90b47
---

# 经验证的生成式初审

**与相近工作流的区别：** AWF-0009 筛选漏斗（Screening funnel，LITREV）的筛选加抽检流程与此类似，但这里的交付物是提交给法院的文件集，带有基于漏检率的召回率验证和特权审查。AWF-0024 则是单份合同的修订稿。
**工具变体：** `relativity-air-for-review` · `everlaw-coding-suggestions`

## 步骤

1. 先用检索、邮件串联和去重对文件总体做初筛。Dinsmore 去掉了约 20,000 份合同草稿。HSF Kramer 把 500 万份文件缩减到约 140,000 份 [[2]](#sources)[[3]](#sources)。
2. 编码指令由律师而不是技术人员依据审阅规程来写：案件描述、编码定义，以及不相关内容的示例表述 [[2]](#sources)。
3. 🛑 **审阅**：律师为一个基准样本编码（Dinsmore 为 120 份文件；法学评论研究中为 1,600 份文件的对照集）。他们把 AI 的判断与之对比，并分几轮优化提示词 [[1]](#sources)[[2]](#sources)[[3]](#sources)。
4. 对全部文件运行生成式 AI 分类器。决定是否把“边缘”预测视为相关 [[1]](#sources)。
5. 🛑 **抽检**：抽取统计上有效的精确率和漏检率样本。如果召回率不达标，就重新运行或叠加预测编码 [[2]](#sources)。
6. 律师审阅每一份相关或边缘文件，确认相关性、判断是否涉及特权，并隔离机密材料。其余文件由主动学习和质量控制覆盖 [[3]](#sources)。
7. 🛑 **签发**：对结果负责的律师在提交前接受已验证的召回率 [[2]](#sources)。

**产出：** 一份经验证的相关（并经特权筛查的）文件提交集，附有记录在案的召回率和精确率，可向法院或对方当事人说明依据。
**失败模式 → 防护：** 该工具忽略文件族关系、超链接、元数据和图片中的文字；处理长文本时会出错，并且有些引用没有依据 → 对出错的文件重新运行，非文本文件人工审阅 [[1]](#sources)。纳入边缘文件会把召回率提高到 96.2%，但精确率降到 58.4% → 事先确定对边缘文件的处理政策 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名的、与厂商相关的或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Keeling et al., GenAI document review real-world study](https://scholarship.law.ufl.edu/jtlp/vol30/iss2/6/) (2026-06-30)。取自真实案件的 1,600 份文件样本，与金标准的律师审阅对比。"high recall rate of 83.9% and a precision rate of 84.7%"。*第一手：研究（取自过往客户案件的 1,600 份文件样本）；可信度：高。*
- [Everlaw, Dinsmore & Shohl cyber contract review](https://www.everlaw.com/blog/case-studies/dinsmore-recall-coding-suggestions-case-study/) (2026-03-24)。先检索，再生成式 AI 编码，再预测编码，每个阶段都由律师样本验证。"98.2% recall rate"。*第一手：厂商；可信度：中。*
- [Relativity, HSF Kramer High Court disclosure](https://www.relativity.com/resources/customers/hsf-kramer-relativity-air-for-review/) (n.d.)。先设定试点阈值，再上线做一线审阅，由律师二次复核。"Reviewed roughly 100,000 documents in about 12 hours"。*第一手：厂商；可信度：中。*
