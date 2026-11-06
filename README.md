# Agent Workflow Atlas

**A catalog of how professionals actually run AI agents in production work**, written as step-by-step SOPs you can copy: what goes in, which agents and tools do what, where a person has to approve, and what comes out.

It covers software engineering, product design, research, law, finance, healthcare, education, marketing, sales, support, fiction and screenwriting, and industrialized short-drama production (短剧). Each workflow lists its sources and how strong its evidence is.

**Status:** early. 31 workflows are seeded from [the research report](research/phase1-report.md). One is `accepted` ([Issue-tree research](workflows/ORG/BIZ/STRAT/issue-tree-research/)); the rest stay `draft` until someone adds a real example run. That's the most useful contribution right now ([how](CONTRIBUTING.md#1-add-an-example-run)). [Where are the real runs?](research/2026-11-real-runs.md) lists public runs that could become examples.

## Browse

- **[INDEX.md](INDEX.md)**: every workflow, by field and by trait.
- **[workflows/](workflows/)**: one folder per workflow, organized like a biological tree.

A sample entry, [AI shot factory](workflows/CRE/MED/AIGCVIDEO/ai-shot-factory/) (`AWF-0015`), turns a short-drama script into a finished AI-generated episode:

```
script → shot list → 🛑 plan → character lock → each shot: (keyframes ⟲ critic) → (video ⟲ check)
       → voice + lip-sync → edit → 🛑 review → AI label → 🛑 sign-off → publish
```

🛑 marks where work stops until a person approves. Each entry spells out who approves what, the tools used at each step, the failure modes, and the regulations that apply.

## How it's organized

Workflows are classified the way biology classifies animals: by **ancestry**, not by shared features.

```
workflows/
  CRE/                     Kingdom: broad field (5)
    MED/                   Phylum: profession (18)
      AIGCVIDEO/           Class: discipline
        ai-shot-factory/   Species: one workflow, with a permanent ID (AWF-0015)
          README.md        the SOP and its metadata
          variants/        toolchain-specific notes (optional)
          examples/        dated real runs, with context files and samples
```

- A workflow is placed by **what profession it comes from and what it delivers**, using a short key where the first match wins.
- **Shared techniques** (generate-and-critique loops, parallel workers, autonomy level) are searchable traits, not folders, because they show up in every field.
- **Tools** are variants at the bottom, so switching from one model or app to another never moves anything.

The full rules fit on one page: [TAXONOMY.md](TAXONOMY.md).

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: add an example run of a listed workflow, add a new workflow from the template, or fix a placement. `python scripts/validate.py` checks your entry before you open a pull request.

## Research

[research/phase1-report.md](research/phase1-report.md) is the study this catalog started from: the landscape across industries, the classification design, and a log of 31 claims checked against sources in November 2026.

## License

- **Content** (everything under `workflows/`, `research/`, `templates/`, and the docs): [CC BY 4.0](LICENSE-CONTENT). Reuse it freely, with credit to this catalog.
- **Code** (`scripts/`, `.github/`): [MIT](LICENSE).

By contributing, you agree your contribution is shared under the same terms.
