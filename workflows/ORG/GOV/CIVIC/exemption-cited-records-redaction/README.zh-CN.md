---
id: AWF-0205
name: 引用豁免条款的公开记录遮蔽
summary: "为公开记录申请分类文档并提出附豁免依据的遮蔽建议；记录官逐条批准。"
deliverable: 遮蔽后的记录公开件
shape: "收到记录申请 → 与申请人澄清范围 → 搜索文档、邮件和许可系统 → 每个文档：分类 responsive | non-responsive | exempt (附法律依据) → 提出遮蔽建议（个人数据、州法豁免） → 🛑 review (记录官批准每一处遮蔽) → 向申请人公开 + 审计日志"
source_hash: b2ad1614c9e2
---

# 引用豁免条款的公开记录遮蔽

**与相近工作流的区别：** 最接近的是 AWF-0082（模型分诊的记录公开）：它批量分类已归档的电报以便解密，人只处理“不确定”的记录并抽查模型的判断。本工作流是端到端处理一份进来的申请（搜索、豁免分类、遮蔽），并且每一处遮蔽都由人批准；交付物是给单个申请人的遮蔽后公开件。
**工具变体：** `common-sense-ai` · `atea-masking-service`

## 步骤

1. 受理：在工作人员看到之前，由 AI 聊天先请申请人澄清含糊的申请 [[1]](#sources)。
2. 智能体在机构的文档管理、Outlook/SharePoint、许可等系统中搜索相关记录，并把申请的各部分分派给相应部门 [[1]](#sources)。
3. 每份文档被分类为 responsive（相关）、non-responsive（无关）或 exempt（豁免），并附上豁免所依据的法律条文 [[1]](#sources)。
4. 智能体提出遮蔽建议：个人数据（直接和间接标识符）以及辖区规则所涵盖的内容；瑞典市政版本按服务领域使用模板 [[1]](#sources)[[2]](#sources)[[3]](#sources)。
5. 🛑 **审阅**：责任官员在公开前检查并批准每一处拟议的遮蔽；按瑞典监管机构的指引，该工具“纯粹是辅助”，由官员决定哪些内容属于保密 [[1]](#sources)[[2]](#sources)。
6. 记录交给申请人；系统保留一份日志，记载搜索了什么、返回了什么、保留了什么 [[1]](#sources)。

**产出：** 给申请人的遮蔽后公开包，以及搜索、保留和豁免的审计轨迹。
**失败模式 → 防护：** 漏掉个人数据或过度遮蔽 → 官员审阅每一处遮蔽，并采纳数据保护机构建议的 DPIA 和日志记录 [2]。厂商对“常规”申请自动办结会跳过审阅 → 配置哪些申请类型可以自动公开，敏感的仍走完整审阅 [1]。厂商处理个人数据 → 使用受限环境，任务结束后删除文档 [3]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或经记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Common Sense AI, Los Altos Hills request](https://www.commonsensetech.ai/products/public-records) (undated)。一份大型市政申请经分诊并预先准备好遮蔽，只剩少量文档需要细看。"Los Altos Hills brought us 8,483 documents in one request. We saved them 99 hours and $7,900 of staff time, leaving only 30 documents requiring close human review."。*第一手：厂商；可信度：中。*
- [Techtidningen, Ronneby kommun](https://techtidningen.se/blev-tre-ganger-snabbare-ronneby-gick-fran-papper-och-penna-till-ai-pa-sex-manader/) (2025-12-08)。市政府采用 Lidingö/Atea 的遮蔽工具；上传、AI 给出建议、承办人审阅。"Nu har man infört ett AI-baserat system som gör att det går tre gånger snabbare."。*第一手：访谈；可信度：中。*
