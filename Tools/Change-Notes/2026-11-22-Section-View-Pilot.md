---
title: Revision-bound section-view pilot — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Section-view pilot — isolated, NOT LIVE

## Shipped
No deployment or corpus rewrite. Isolated code `d656991` adds a generic viewer and
synthetic tests, not a bridge route. Source-specific spans/headings are data in a
reviewed sidecar, not page branches or stored rule answers in the tool.

The viewer takes a host-authorized source map, a reviewed record and its independent
expected digest. It verifies source identity, book revision, page-text hashes,
character bounds and exact parent-heading spans, then returns separate original
source blocks and governing context. Metadata is not inserted into factual quote
text. All refs must share the reviewed book/revision. Unknown, tampered, incomplete
units or an over-budget result refuse; text is never cut to make it fit. This is
trusted-host code, not a sandbox or a remote source-access grant.

Thirteen sample records were assembled from the audited material and parent pages.
Twelve produce bounded views; one Quick Start continuation is explicitly held
unavailable because OCR block order is unresolved. No page/book ban was added.
Some views mark section completeness false while retaining whole selected paragraphs;
that does not claim all rule dependencies are present. Cross-page continuations are
explicit source segments, not blind concatenation of neighboring pages. Automatic
cross-reference graph extraction is not implemented; references remain source prose
and are not promoted into the governing heading path.

Qwen-low authored the viewer draft and a bounded correction through a fixed tool-free
local drafting endpoint. The first draft exhausted its code-generation budget without
final output; a complete code block was recovered from the retained response. Sol
reviewed it, caught heading-validation issues and corrected a malformed rejection
return in the small Qwen repair. Tests, source annotations and experiment harness
are Sol-authored. No untouched-Qwen or first-attempt-success claim is made.

## Measured
Eight viewer verification methods and the related evidence/claim tests pass:
**23 focused unittest methods**, no failures. They cover exact blocks, tampered/stale
sources, unknown scope, missing headings, cross-book references, budget refusal,
explicit partial-section flags and a complete table selected beyond the old page cap.
Compile/diff checks pass. Both previously clipped table units are returned intact.

Final reviewed sidecar SHA `7dc15b10…82e3ddd`; earlier versions and authoring failures
are retained. The pilot uses already-validated proposed quotes to select a unique
containing record, never the gold answer. It tests **quote-focused evidence review**,
not pre-answer query ranking, retrieval discovery, generation or live voice.

The frozen comparison contains 21 paired proposal cases (original 18 plus audited
bonus and Quick Start cases): 41 model-review calls and one model-free held-unit
boundary. Both arms use the same responsive verdict contract; only the evidence view
changes. It is not a fresh full-handler or spoken-answer test.

- Supported proposals accepted: page **8/11**, section **10/11**.
- Adversarial proposals accepted: **0/8 in either arm**. Seven were explicitly
  rejected; the critical wrong-mechanic staging case truncated in both arms. This
  does **not** prove the earlier unsafe approval is repaired.
- The exact formula/bonus miss also truncated in both arms; its semantic status is
  unresolved. The held Quick Start unit refused before a section-arm model call.
- Page arm: five truncated completions and one transport timeout. Section arm:
  three truncated completions. Empty truncated content can surface as a decoder
  TypeError; these are not counted as additional independent transport failures.
- Median model-review wall time: page **8.08 seconds**, section **7.22 seconds**,
  excluding the model-free held-unit boundary and all generation/retrieval/audio.
  These observed times are order/cache confounded, not a causal voice-speed claim.

**Structural prototype: passes. Semantic integration readiness: not established.**
Do not activate or wire it into the live answer path yet. The source context is
better bounded, but incomplete reviewer output prevents judging the most important
controls. Next recommended scope, awaiting approval: a read-only capability/behavior
check of local Qwen's reasoning-versus-visible-output controls and transport deadline
handling. Establish which controls the provider actually supports before proposing
any setting change. Keep low effort, model, source permissions and voice deadlines
unchanged during that audit; do not add more passage-specific content patches.

## Still open
Live discovered-reference/read-budget compatibility is not established by an offline
authorized source map; integration needs its own review. Neither heading metadata nor
an approved annotation confers semantic correctness on a model verdict. A held unit
is a scope boundary, not proof that the book lacks a rule.

The same reviewer/schema, low effort, 512-token output and 12-second transport limit
are retained. The viewer itself caps the serialized view at 5,700 characters. Page
always precedes section within each pair, so cache/order confounds limit timing claims.
Code-drafting limits are separate and did not alter voice configuration or deadlines.

## Corrections
This follows the [read-only context audit](2026-11-22-Source-Context-Audit).
Production stays `81e9eeb`; no source/configuration/model/permission/restart change.
The last full-handler replay is still 1/8 answerables, not replaced by review-only
scores. Private records and outcomes: data-tier `runtime/section-view-pilot-20261122`;
source harness: project `workfiles/section-view-pilot-20261122`. Canonical source bytes
remain unchanged; annotations, integration and activation are distinct permissions.

Follow-up: [Completed provider-controls audit](2026-11-22-Provider-Controls-Audit). No deployment; separate thinking-cap capability trial awaits approval.
