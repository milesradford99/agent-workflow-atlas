# Claude Code kit: Bible-driven novel draft

This kit sets up a manuscript repo in which Claude Code interviews you to build a story bible in Markdown and locks your voice. You approve both at the first 🛑 plan. Claude then breaks the story into beats, chapters and scene cards, and you sign off the outline at the second 🛑 plan. After that it drafts one scene at a time with a narrow context. Read-only checkers in fresh contexts write notes and never edit. At 🛑 review you pick the notes that count, and only then does the bible or timeline change. It is a starter kit written from the workflow's public sources (McNestrie's CI-for-prose setup and `novel-harness`, Garrett's locked canon and batch revision, Saoulidis's scene list). It is not a reported run. See [the workflow](../README.md).

## Files

### `CLAUDE.md` (section to add)

```markdown
## Novel repo

- Layout: `bible/` (characters/, places.md, timeline.md, rules.md, theme.md, parked.md), `voice.md`, `outline/` (beats.md, chapters.md, scenes/NN-MM.md), `manuscript/chNN.md`, `notes/chNN/`.
- Use the `novel-draft` skill. Items marked `LOCKED` in the bible or `voice.md` are canon: never change them; propose a change in `notes/` and let the author decide.
- Agents propose, the author promotes. Never edit `bible/`, `voice.md` or `outline/` without the author's approval in this session.
- When drafting, load only: the scene card, `voice.md`, `bible/theme.md`, the bible entries the card names, `outline/summary.md`, and the last ~2k words. Never the whole manuscript.
- Checkers write notes to `notes/chNN/` and never edit prose.
- STOP and ask at: bible + voice approval, outline sign-off, and after every scene's checks (the author picks which notes apply).
- Commit only when the author says "accept". Keep `DISCLOSURE.md` up to date: AI-generated vs AI-assisted, per chapter.
```

### `.claude/skills/novel-draft/SKILL.md`

```markdown
---
name: novel-draft
description: Bible-first novel drafting: interview for the story bible, lock the voice, outline to scene cards, then draft scene by scene with read-only continuity and style checks and author review. Use when the user works on their novel in this repo (/foundations, outline, next scene).
---

# Novel draft

1. **Premise + voice samples.** Ask for the premise, influences, and 1–3 samples of the author's own prose. For a sequel, read book 1 one chapter file at a time and draft people, places and events from it.
2. **Story bible via interview.** Ask one question at a time, grouped as theme, world, characters, timeline, rules (magic, tech, law). Write answers to `bible/`. Put ideas with no home in `bible/parked.md`.
3. **Lock the voice.** Draft one short scene in five distinct voices. The author picks the nearest miss and edits it by hand. Save the edited scene in `voice.md` marked `LOCKED`, then list about ten rules taken from the author's edits (POV, tense, banned phrases, sentence rhythm). Dialogue rules get their own section.
4. **STOP: plan.** Present the bible and `voice.md`. Wait for approval. Mark each approved item `LOCKED`.
5. **Beats → chapters → scene cards.** Write `outline/beats.md`, then `outline/chapters.md` (a brief per chapter), then one card per scene in `outline/scenes/` from the scene-card template. Plan the mystery structure: which clue lands in which scene, before which deduction.
6. **STOP: plan.** Present the outline and the clue map. Wait for sign-off. The outline is a navigation system, so offer to update it whenever a written scene beats the plan.
7. **Each scene in order:**
   a. Load the card, `voice.md`, `bible/theme.md`, only the bible entries the card names, `outline/summary.md`, and the last ~2k words of the manuscript.
   b. Draft the scene into `manuscript/chNN.md`.
   c. Run `python scripts/lint_prose.py manuscript/chNN.md` and save its output in `notes/chNN/lint.md`.
   d. Launch the `continuity-checker` subagent (fresh context, read-only). Its notes go to `notes/chNN/continuity.md`.
   e. Style check in a fresh subagent against `voice.md`: POV, tense, banned phrases, and whether the scene explains its own theme. Notes go to `notes/chNN/style.md`.
8. **STOP: review.** Present all notes as a numbered list. The author picks which apply. Revise in ONE pass against that selection only. Never loop on a model-scored quality metric. Then wait for "accept" (commit) or "revert" (rewrite the card).
9. **Update bible and summary.** On accept, append the scene to `outline/summary.md` (≤150 words), update `bible/timeline.md`, and propose character-file changes for approval. Every ~10 chapters, check progress against the scene list. At the end, audit the whole book for voice drift, objects carried after they were left behind, clues used before they appear, and narration that calls the book a book.
```

### `.claude/agents/continuity-checker.md`

```markdown
---
name: continuity-checker
description: Read-only continuity reviewer for one scene against the story bible. Use after a scene is drafted.
tools: Read, Grep, Glob, Write
---

You check one scene for continuity. You never edit prose, the bible or the outline; you only write a notes file.

Read the scene file you are given, its scene card, `bible/` (characters, places, timeline, rules) and `outline/summary.md`.

Flag, with the exact sentence quoted:
- contradictions with LOCKED canon (appearance, names, ages, relationships, rules of the world);
- travel time and timeline impossibilities;
- knowledge leaks: a character knows or refers to something they haven't learned yet;
- objects present after they were lost, used up or left behind;
- clues used before the scene in which they are planted.

Write `notes/chNN/continuity.md` as a numbered list: severity (break / risk / nit), quote, the bible entry it conflicts with, suggested fix in one line. If you find nothing, write "No continuity issues found" and list what you checked.
```

### `outline/scenes/_template.md`

```markdown
# Scene NN-MM: <working title>

- **POV:** <character>
- **Where / when:** <place> · <timeline point>
- **Goal:** <what the POV character wants in this scene>
- **Conflict:** <what stands in the way>
- **Outcome:** <win / lose / twist, and the new situation>
- **Information revealed:** <what the reader learns; what each character learns>
- **Clues planted / paid off:** <clue id → where it pays off>
- **Bible entries to load:** <characters/x.md, places.md#y>
- **Target length:** <words>
- **Author notes:** <anything that must or must not happen>
```

### `scripts/lint_prose.py`

```python
"""Flag mechanical AI tells in a chapter. Notes only; never edits the file.
Usage: python scripts/lint_prose.py manuscript/ch01.md
Edit BANNED from your own voice.md rules."""
import re
import statistics
import sys

BANNED = ["a testament to", "tapestry", "delve", "couldn't help but", "a sense of",
          "little did", "in that moment", "the weight of"]

text = open(sys.argv[1], encoding="utf-8").read()
lower = text.lower()
print(f"# Lint: {sys.argv[1]}")
print(f"- em-dashes: {text.count(chr(0x2014))}")
for phrase in BANNED:
    n = lower.count(phrase)
    if n:
        print(f"- banned phrase '{phrase}': {n}")
sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
lengths = [len(s.split()) for s in sentences]
if len(lengths) > 1:
    print(f"- sentences: {len(lengths)}, mean {statistics.mean(lengths):.1f} words, "
          f"stdev {statistics.stdev(lengths):.1f} (low stdev = flat rhythm)")
```

## Run it

1. Create the folders in the `CLAUDE.md` layout, add the files above, run `git init`, and start Claude Code in the repo.
2. Say `Use the novel-draft skill. Start the foundations interview.` and answer one question at a time. Paste your own prose samples, not AI text.
3. 🛑 **Plan (bible + voice):** pick the nearest-miss voice, edit it by hand, and approve the bible items you want `LOCKED`.
4. 🛑 **Plan (outline):** read the beats, chapter briefs, scene cards and clue map, then sign off. Ask for outline updates later when a scene beats the plan.
5. Say `next scene`. 🛑 **Review:** read the lint, continuity and style notes and reply with the numbers that apply (e.g. "apply 2, 5, 7"). After the single revision pass, say `accept` to commit or `revert` to rewrite the card. Rewrite each chapter yourself before it counts as done.
6. Record AI-generated vs AI-assisted for each chapter in `DISCLOSURE.md` before any KDP upload.

## Adapt it

- **Codex CLI / AGENTS.md tools:** put the `CLAUDE.md` section and skill steps in `AGENTS.md`. Run the continuity and style checks as separate sessions with only those files open, so they keep a fresh context.
- **Cursor:** save the skill as `.cursor/rules/novel-draft.mdc`, and run checkers in a new chat with read-only instructions.
- **Second opinion:** add a reviewer from another model family (a local model or another API) as an extra notes file. Set its context length explicitly and surface failed calls; a silent truncation or a failed request looks like "no issues".
- **Long books:** keep the per-scene load narrow and lean on `summary.md` and the bible. The source author reports that context strain is unsolved for long manuscripts, so do whole-book audits in chunks.
- **Tools you already use:** Sudowrite's Story Bible or NovelCrafter's Codex can stand in for `bible/`. Keep the rule that the author promotes and agents only propose.
- **Safety:** your manuscript is your IP. Don't add web tools or MCP servers that upload chapters anywhere you haven't chosen.
