---
id: AWF-0158
name: 质控把关的安全病例录入
summary: "将不良事件病例提取进安全数据库；经双人质控、药物警戒专员和医学审核签字后提交 ICSR。"
deliverable: 个例安全报告（ICSR）
shape: "不良事件来源文件（表单、邮件、通话记录） → GenAI 将病例字段提取进安全数据库 → 🛑 review (病例处理团队双人质控) → 数据缺失：起草给报告人的随访函 → 🛑 review (药物警戒专员修改并发送) → 🛑 sign-off (医学审核) → 提交 ICSR (E2B)"
source_hash: 7a241f6dcd8f
---

# 质控把关的安全病例录入

**与相近工作流的区别：** AWF-0033 协调员审阅的预筛选是把患者与试验标准做匹配，AWF-0091 是起草临床研究报告（CSR）。本工作流的交付物是受监管的单病例安全报告，带双人质控和向报告人随访的闭环；交付物和检查点都不同。
**工具变体：** `arisglobal-lifesphere-navax` · `bayer-mygenassist` · `indegene-naem`

## 步骤

1. 报告通过电话、邮件或电子方式到达，被汇编为药物警戒数据库中的来源文件 [[2]](#sources)。
2. GenAI「Advanced Intake」把病例表单数据提取到安全系统的各字段；流程确认环节要检查「字段是否提取到了系统中正确的数据点」 [[1]](#sources)[[3]](#sources)。
3. 🛑 **审阅**：病例处理供应商按「Four Eyes」原则（第二双眼睛）对提取出的数据做质量控制 [[1]](#sources)。
4. 病例信息不完整时，LLM 根据病例数据和问题表格，起草发给报告人的文件（随访）函 [[2]](#sources)。
5. 🛑 **审阅**：药物警戒专员在发送前审阅并修改函件草稿；第二次联系尝试遵循药物警戒质量管理规范的规则 [[2]](#sources)。
6. 🛑 **签发**：安全团队对已处理的病例进行医学审核和获益-风险分析 [[3]](#sources)。

**产出：** 安全数据库中已完成的 ICSR，可供监管提交。
**失败模式 → 防护：** 集成后字段映射到错误的数据点 → 对整个流程重新验证，而不仅是 AI 环节 [1]。AI 编造病例事实 → 双人质控并就 AI 风险培训用户 [1]。严重事件藏在非严重的自由文本里 → 从自由文本叙述中提取 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Bayer France PV, MyGenAssist cross-over study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11933758/) (2025-03-10)。为期 4 个月的前后对照研究；专员审阅 LLM 起草的随访函；回复率不变。"An average of 23.3% (95% CI 13.8%-32.8%) of time saving was made"。*第一手：是；可信度：高。*
- [ArisGlobal, Boehringer Ingelheim NavaX go-live](https://www.arisglobal.com/media/press-release/boehringer-ingelheim-harnesses-genai-to-transform-case-intake-with-lifesphere-navax/) (2025-07-08)。GenAI 录入已用于 ICSR，保留质控环节；引述了 BI 药物警戒负责人的话。"up to 90% average data extraction accuracy"。*第一手：厂商；可信度：中。*
- [Journal of mHealth, BI PV Q&A](https://thejournalofmhealth.com/lessons-in-ai-use-what-worked-for-boehringer-ingelheim-in-a-pv-context/) (2025-10-09)。BI 药物警戒运营负责人谈验证、供应商质控和双人审阅；没有新数字。"We have adopted the “Four Eyes” principle (a second set of eyes)"。*第一手：访谈；可信度：中。*
