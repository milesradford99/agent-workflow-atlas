# Example run: short description

<!--
Copy this folder to workflows/<KINGDOM>/<PHYLUM>/<CLASS>/<workflow>/examples/YYYY-MM-short-name/
Before committing, remove secrets, credentials, personal data, client names and anything you don't have the right to share.
-->

| | |
|---|---|
| **Date of run** | YYYY-MM |
| **Variant** | toolchain slug, e.g. `claude-code` (add it to the workflow's `variants` list) |
| **Who ran it** | your GitHub handle, or "anonymous practitioner" |
| **Scale** | solo · team · org |
| **Evidence** | A, B or C (see TAXONOMY.md §5) |

## Setup

What someone needs to rerun this: models, tools, versions, access, cost.

The context files the agent used are in [`context/`](context/) (for example `CLAUDE.md`, a playbook, a story bible, a prompt pack, an n8n or Dify export).

## Run log

A short, honest account of one real run. Paste or summarize the key turns, especially where a person stepped in at a 🛑 checkpoint and what they changed.

## Input → output

The input is in [`sample/input`](sample/) and the output in [`sample/output`](sample/). Keep them small and anonymized.

## Numbers

Whatever you measured: time taken vs. by hand, cost, pass rate, edits needed at each checkpoint.

## What went wrong

Failures, retries, and what you'd change next time.
