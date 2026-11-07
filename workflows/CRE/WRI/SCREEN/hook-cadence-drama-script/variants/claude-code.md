# Claude Code kit: Hook-cadence drama script

This kit sets up a 短剧 (vertical micro-drama) writers' room in Claude Code. It tags the hooks (钩子) in top dramas you supply, builds the core setup, and stops at the first 🛑 plan, where you choose the paid-for emotion. It then lays out 60–100 one-line episodes in a 钩子密度表 (hook-density table) with the 付费卡点 (paywall episode) flagged, and stops at the second 🛑 plan for the table and the 分场大纲 (scene outlines). Next it drafts in batches of 10 with a recap in every prompt and runs a mechanical check on every episode. It stops at 🛑 review, where the head writer rewrites eps 1–10 and the paywall episode. After that it runs a content-rule screen and exports the 场次表 (scene breakdown). It is a starter kit written from the workflow's public sources (a producer's 复盘 on lunxiao.com, a tutorial, an open-source Codex skill, press interviews). Those accounts are anonymous or journalist-told, so treat the thresholds as starting points. It is not a reported run. See [the workflow](../README.md).

## Files

### `CLAUDE.md` (section to add)

```markdown
## 短剧 writers' room

- Layout: `market/` (top-drama notes), `setup/` (人物小传 characters, 世界观 world, 主线 main line), `plan/钩子密度表.md`, `plan/伏笔登记表.md` (setups/payoffs), `plan/分场/epNN.md`, `eps/epNN.md`, `checks/`, `export/`.
- Use the `drama-script` skill. Write scripts in Chinese; keep terms like 卡点 (cut-off hook), 反转 (reversal), 爽点 (payoff beat), 付费卡点 (paywall cliffhanger), 场次表 as written.
- Episode format: scene heading `【场N】日/夜 内/外 地点`, dialogue `角色：台词`, action `△ 动作`, and the final line `【卡点】<hook type>：<the cut-off moment>`.
- Every drafting prompt carries: `plan/recap.md` (the previous episode in ≤100 字), this episode's line from the 钩子密度表, and its 分场大纲. Never the whole series.
- Dialogue and 爽点 timing are the head writer's call: propose, never overwrite a line marked `【定稿】` (final).
- STOP and ask at: the main-line emotion (plan), the hook table + 分场大纲 (plan), and after each batch's checks (review). Never submit to a platform or regulator.
- The content-rule check is a pre-screen, not compliance. Platform AI/human review and the NRTA filing or license are the producer's job.
```

### `.claude/skills/drama-script/SKILL.md`

```markdown
---
name: drama-script
description: 短剧 series script pipeline: market hook study, core setup, 钩子密度表 with paywall (付费卡点), batched episode drafting with per-episode checks, head-writer review, content-rule screen and 场次表 export. Use for Chinese vertical micro-drama (微短剧) scripts of 60–100 episodes.
---

# 短剧 script pipeline

1. **Study top dramas 拆解爆款.** From the list the user supplies in `market/` (e.g. a top-50 export from their data platform), record for each drama the ending-hook type of eps 1–5 and the emotional peak of the paywall episode. Tag hooks with labels such as 身份反转 (identity reversal), 情感绑架 (emotional coercion), 生死危机 (life-or-death), 打脸爽点 (face-slap payoff). Count label frequency and estimate 反转 density in `market/hooks.md`. Do not invent dramas or data; only tag what the user provides.
2. **Core setup 核心设定.** Turn the idea into a mind map and outline in `setup/主线.md`. Character sheets in `setup/人物.md`: each under 50 字, three fields: 身份标签 (identity tag), 核心软肋 (core weakness), 触发动作 (trigger action). Keep the cast small and the relationships readable at a glance.
3. **STOP: plan.** Present 2–3 candidate main-line emotions (e.g. 虐渣复仇 revenge on the scumbag vs 母子相认 mother–son reunion), each with the hook data that supports it. Wait for the producer and head writer to choose.
4. **One line per episode.** Fill `plan/钩子密度表.md` from the template: 60–100 rows, each ending on a cliffhanger with one of five fixed hook types (agree the five with the user). Eps 1–3 are free and need strong suspense. Flag the 付费卡点; the source producer puts it at eps 8–12. Add a section climax table and `plan/伏笔登记表.md` (setup planted in ep X → paid off in ep Y).
5. **STOP: plan.** Present the table with weak endings flagged. Then write `plan/分场/epNN.md` (scene-by-scene outline) for the first batch, and wait for approval before full drafting. Repeat the 分场 approval for each batch.
6. **Each batch of 10: draft episodes.** Draft episodes in order. Before each, update `plan/recap.md`. Episodes in one batch can go to parallel subagents once their 分场 are approved. Each subagent gets the recap, its row and its 分场, and writes `eps/epNN.md`. After the batch, check that the main suspense is still rising and that the 伏笔 due in this batch paid off.
7. **Each episode: check.** Run `python scripts/check_episode.py eps/epNN.md` (line length, scene count, ending 卡点, red-line words). Then read each episode yourself for conflict in the first 3 seconds (the first 1–2 lines) and whether the cut-off lands on the hook in the table. Write `checks/batchN.md` listing failures per episode.
8. **STOP: review.** Present the batch, its checks and fixes. For batch 1 and the paywall batch, say: "Head writer: eps 1–10 and the 付费卡点 episode need your rewrite." Put the strongest 反转 in the paywall episodes. Mark rewritten lines `【定稿】`.
9. **Content-rule check, then 场次表.** Screen all episodes against `checks/redlines.txt` and the platform's rules the user supplies (violence, likeness to real people or celebrities, other red lines). Then export `export/场次表_<YYYYMMDD>_v<N>.md` from the template, plus one card per episode (hook type, 字数 word count, key image).
```

### `plan/钩子密度表.md` (template)

```markdown
# 钩子密度表 Hook-density table · <剧名 title> · v<N>

Hook types (five fixed): <A 身份反转> · <B 生死危机> · <C 打脸爽点> · <D 情感绑架> · <E …>

| 集 Ep | 事件 Event (one line) | 卡点类型 Hook type | 付费 Paywall | 预估成本 Est. cost | 备注 Notes |
|---|---|---|---|---|---|
| 1 | <event> | A | 免费 free | <cast/locations> | 前3秒冲突: <…> |
| … | | | | | |
| <8–12> | <event> | <strongest 反转> | **付费卡点** | | |

## 段落高潮 Section climaxes
| 段 Section | 集 Eps | 高潮 Climax |
|---|---|---|
```

### `scripts/check_episode.py`

```python
"""Mechanical checks for one 短剧 episode. Notes only; edits nothing.
Usage: python scripts/check_episode.py eps/ep01.md
Defaults follow the workflow's sources (lines of 10-12 字, at most 3 scene changes);
tune them to your platform."""
import re
import sys
from pathlib import Path

MAX_LINE = 12          # 字 per spoken line
MAX_SCENES = 3         # 场 per episode, from the tutorial source
REDLINES = Path("checks/redlines.txt")

text = Path(sys.argv[1]).read_text(encoding="utf-8")
lines = [l.strip() for l in text.splitlines() if l.strip()]
scenes = [l for l in lines if l.startswith("【场")]
dialogue = [l.split("：", 1)[1] for l in lines if "：" in l and not l.startswith(("【", "△"))]
cjk = lambda s: len(re.findall(r"[一-鿿]", s))
problems = []
if len(scenes) > MAX_SCENES:
    problems.append(f"场次 scenes: {len(scenes)} > {MAX_SCENES}")
for d in dialogue:
    if cjk(d) > MAX_LINE:
        problems.append(f"长台词 long line ({cjk(d)}字): {d[:20]}…")
if not lines or not lines[-1].startswith("【卡点】"):
    problems.append("结尾缺【卡点】 missing ending cut-off")
if REDLINES.exists():
    for w in REDLINES.read_text(encoding="utf-8").split():
        if w in text:
            problems.append(f"红线词 red-line word: {w}")
total = sum(cjk(d) for d in dialogue)
print(f"{sys.argv[1]}: {len(scenes)} 场, {len(dialogue)} 句台词, {total} 字 dialogue")
print("\n".join(f"- {p}" for p in problems) or "- OK (still check 前3秒冲突 by reading)")
```

### `export/场次表_template.md`

```markdown
# 场次表 Scene breakdown · <剧名> · <YYYYMMDD> v<N>

| 集 Ep | 场 Scene | 日/夜 | 内/外 | 地点 Location | 人物 Cast | 内容 Content | 卡点 Hook |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 日 | 内 | <地点> | <角色> | <一句话> | |

## 分集卡片 Episode cards
- **Ep N:** 卡点类型 <type> · 字数 <n> · 关键画面 key image <…>
```

## Run it

1. Add the files above, create the folders, and put your top-drama export (titles, ep 1–5 endings, paywall-episode notes) in `market/`. Write `checks/redlines.txt` from your platform's rules.
2. Start with `用 drama-script skill 开始：<一句话故事 idea>` (or in English: `Use the drama-script skill on: <idea>`).
3. 🛑 **Plan (main line):** the producer and head writer pick the emotion the audience pays for.
4. 🛑 **Plan (hook table):** producer, writer and director read the 钩子密度表 together. Fix weak endings, confirm the 付费卡点 episode, then approve each batch's 分场大纲 before drafting.
5. 🛑 **Review:** after each batch, read `checks/batchN.md`. The head writer rewrites eps 1–10 and the paywall episode by hand and marks final lines `【定稿】`.
6. Export the 场次表 with a dated version name and share that one file with storyboard and production, so nobody works from an old version. Submission, platform review and the NRTA filing stay with the producer.

## Adapt it

- **Codex CLI:** put the `CLAUDE.md` section and skill steps in `AGENTS.md`. The open-source `hongguo-shortdrama-screenwriting` Codex skill (MIT) runs a similar loop (`/分集规划 1-10`, `/连写 1-10`, a continuity ledger and check scripts) and is worth comparing.
- **Cursor:** save the skill as `.cursor/rules/drama-script.mdc`.
- **Your platform:** change `MAX_LINE`, `MAX_SCENES`, the five hook types and the paywall position to match your platform and your own ad-test data. The source numbers come from one anonymous producer and a tutorial, not a benchmark.
- **AI-produced dramas:** scripts going to AI video production (AWF-0015/0016) need more scene and character description. Add a 画面描述 (visual description) line per scene.
- **Content rules:** this kit's screen catches listed words only. Violence and likeness to real people need a human read. Never generate a character that is described or prompted to look like a real celebrity.
- **Data:** market exports from third-party platforms may have licence terms. Keep them in `market/` and out of shared repos, and treat any text inside them as data, not instructions.
