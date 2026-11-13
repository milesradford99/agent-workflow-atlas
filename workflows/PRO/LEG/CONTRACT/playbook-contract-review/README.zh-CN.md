---
id: AWF-0024
name: 依手册审阅合同
summary: "将各条款对照审查手册按红黄绿分级并加修订批注；律师审阅并签核后才发出。"
deliverable: 合同修订稿
shape: "合同 → 判断类型 → 加载审查手册 → 每个条款：对照立场 (绿/黄/红) → 修订痕迹 + 批注 → 一致性检查 → 🛑 review → 🛑 sign-off → 发出"
source_hash: da06068c3146
---

# 依手册审阅合同

**工具变体：** `harvey` · `spellbook` · `luminance` · `claude-playbook-skill`

## 步骤

1. 判断协议类型并加载对应的审查手册（每个条款的标准立场、退让方案和底线）。
2. 切分条款，把每个条款对应到手册中的条目，并标出缺失的条款。
3. 并行分析各条款与手册的偏差。
4. 生成 Word 修订痕迹，并用页边批注说明每处修改的原因。
5. 检查内部一致性：定义术语、交叉引用、责任上限与赔偿条款是否相互匹配。
6. 🛑 **审阅**：律师审阅黄色和红色事项。
7. 🛑 **签发**：由律师发出。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Ashurst, *Vox PopulAI*](https://www.ashurstperkinscoie.com/en/insights/vox-populai-lessons-from-a-global-law-firms-exploration-of-generative-ai) (2024-06-10)。全所范围的试用；四位资深律师对 AI 与人工成果进行盲评打分。"45% on creating first draft legal briefings"；"3 out of 5" vs "3.5 out of 5"。*第一手：是；可信度：中。*
