---
id: AWF-0079
name: Concept-led SD asset stream
kingdom: CRE
phylum: MED
class: GAMEART
deliverable: game-art-assets
shape: "pick tool + prepare style dataset → train custom models → 🛑 plan (artist concept art) → each asset: img2img/ControlNet from concept, sketch or 3D blockout → upscale → (artist tweak ⟲ meets target) → 🛑 review (artist approval)"
autonomy: assist
checkpoints: [plan, review]
patterns: [chain, parallel, eval-opt]
variants: [stable-diffusion-controlnet]
tags: {risk: low}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Concept-led SD asset stream

`CRE › MED › GAMEART` · assist · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `pick tool + prepare style dataset → train custom models → 🛑 plan (artist concept art) → each asset: img2img/ControlNet from concept, sketch or 3D blockout → upscale → (artist tweak ⟲ meets target) → 🛑 review (artist approval)`
**How it differs:** AWF-0015 AI shot factory makes video shots for drama. AWF-0008 Design to code is UI. None close for game assets.
**Variants:** `stable-diffusion-controlnet`

## Steps
1. Choose a tool that supports fine-tuning and inpainting with local install (Stable Diffusion). Prepare a dataset for each new art stream (a few hours) and train custom models; the team trained over 100 (hypernetworks, embeddings) to find working parameters [[1]](#sources).
2. A dedicated internal AI department handles tool analysis, training, pipeline integration and artist support [[1]](#sources).
3. 🛑 **Plan**: an artist produces a detailed concept first, because text-only prompts are unpredictable [[1]](#sources).
4. Generate from the concept with img2img. Environment pieces can start from a sketch plus text, and backgrounds from a basic 3D model at low denoising (up to 0.4) and/or ControlNet to set angle and composition. Detailed or animated objects are generated part by part [[1]](#sources).
5. Upscale, then artists touch up by hand until the asset meets the target. 🛑 **Review**: artists approve or redo outputs; a similar postmortem describes artists holding 'artistic veto power' [[1]](#sources)[[2]](#sources).

**Output:** 2D game assets (collectable cards, decorations, backgrounds) handed to the game's art integration.
**Failure modes → guards:** Structural artifacts and inconsistent style → artists paint over, blend and stitch multiple passes, and a style-trained model keeps the look consistent. Unpredictable prompt-only output → always start from concept, sketch or 3D input.

## Public runs

Coverage as of 2026-11-06: **Partial**: first-hand runs that cover part of the shape or put checkpoints elsewhere. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Belka Games, Working AI into your art pipeline](https://www.pocketgamer.biz/feature/81986/working-ai-into-your-art-pipeline-expectations-vs-reality/) (2023-07-17). Collectable-card set for Solitaire Cruise made with the AI pipeline instead of concept plus 2D render. about 3 work-hours with AI for a 10-card collection, versus about 240 work-hours traditionally. *First-hand: yes; confidence: med.*

## Sources

1. Anton Danko (Belka Games), Working AI into your art pipeline: expectations vs reality, PocketGamer.biz, 2023-07-17. https://www.pocketgamer.biz/feature/81986/working-ai-into-your-art-pipeline-expectations-vs-reality/
2. Absolutist, Rethinking the Art Production Pipeline: A Postmortem of Hidden Objects Getaway (undated). https://wellgames.com/news/rethinking-art-production-pipeline-176712/
