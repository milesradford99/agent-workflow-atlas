---
id: AWF-0008
name: Design to code
kingdom: TEC
phylum: PRD
class: DSYS
deliverable: ui-component-code
shape: "frame link → load design context, tokens, component map → (code ⟲ screenshot diff) → 🛑 review → PR"
autonomy: checkpointed
checkpoints: [review]
patterns: [auto-loop]
variants: []
tags: {risk: low}
evidence: B
status: draft
reference_example: null
inputs_from: [AWF-0007]
merged_into: null
last_verified: 2026-11
---

# Design to code

`TEC › PRD › DSYS` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `frame link → load design context, tokens, component map → (code ⟲ screenshot diff) → 🛑 review → PR`

## Steps
1. Pull the frame's design context, variables (color, spacing, typography), and Code Connect mappings through the Figma MCP server [[7]](#sources).
2. Reuse mapped code components instead of re-creating them.
3. Use tokens only, with no hardcoded values.
4. Render, take a screenshot, compare with the Figma screenshot, and loop.
5. 🛑 **Review**: designer review in a preview build.

**Output:** a PR. Token gaps are reported back to the design-system team.

## Sources

7. Figma, *MCP server guide*. https://github.com/figma/mcp-server-guide
