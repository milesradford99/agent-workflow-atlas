---
id: AWF-0091
name: 撰写人复核的临床研究报告初稿
summary: "基于临床数据表生成临床研究报告初稿；由具资质的医学撰写人全面审阅。"
deliverable: 临床研究报告初稿
shape: "临床数据表 → 数据表预处理 (映射、提取、样式、验证) → 生成 CSR 初稿 → 初稿自动检查 → 🛑 review (具资质的医学撰写人全面审阅初稿) → 经人工审阅的初稿"
source_hash: da86c5d7cd91
---

# 撰写人复核的临床研究报告初稿

**与相近工作流的区别：** AWF-0033 协调员复核的预筛选（Coordinator-reviewed prescreen）是最接近的一个，但它是逐条标准地筛查患者是否符合入组资格。本工作流则是根据试验产出撰写监管文件，只有一个检查点，由撰写人审阅整份文件。
**工具变体：** `claude-bedrock-novoscribe` · `merck-internal-genai-platform` · `merck-quantumblack`

## 步骤

1. 收集该研究的临床数据表（多达数千页），用于撰写临床研究报告 [[1]](#sources)。
2. 预处理数据表：映射、提取数据、套用样式并验证 [[1]](#sources)。
3. 大语言模型撰写 CSR 初稿，最快只需五分钟 [[1]](#sources)。
4. 平台验证数据表，并检查初稿在数据、表述、引用、术语和排版方面的错误 [[1]](#sources)。
5. 🛑 **审阅**：具资质的医学撰写人在初稿进入下一环节之前，审阅整份初稿 [[1]](#sources)。

**产出：** 经人工全面审阅的 CSR 初稿，交给常规的文件审阅和提交流程。
**失败模式 → 防护：** 数据、引用或术语出错 → 数据表验证加上医学撰写人的审阅（公司称这几类错误减少了 50%）。各来源的数据不一致 → 起草前先做预处理。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Merck news release](https://merck.com/news/merck-expands-innovative-internal-generative-ai-solutions-helping-to-deliver-medicines-to-patients-faster) (2025-06-25)。默沙东自建的 CSR 撰写平台，由医学撰写人审阅每份草稿。"fully human reviewed CSR first draft" 的耗时从平均 180 小时降到 80 小时。*第一手：是；可信度：中。*
- [Anthropic, Novo Nordisk](https://claude.com/customers/novo-nordisk) (n.d.)。NovoScribe 覆盖 CSR、器械方案和患者手册。"Claude has helped us cut writing times on CSRs by 90%"。*第一手：厂商；可信度：中。*
- [Practical AI in Healthcare, Sanofi](https://practicalaiinhealthcare.com/when-ai-meets-real-patients-inside-sanofis-ai-powered-clinical-development-pipeline/) (2026-04-26)。会议上的介绍；还会起草对监管机构问询的回复，这部分由人负责。"Eighty percent of AI-generated first drafts already meet submission quality standards.". *第一手：访谈；可信度：中。*
