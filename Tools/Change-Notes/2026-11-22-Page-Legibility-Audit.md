---
title: "2026-11-22 — Page legibility audit and maintenance contract"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---

# Page legibility audit and maintenance contract

## Shipped

Read-only audit completed for six PC profiles, Cindy Lou Jenkins and Taco, and the Dolly Zoom and Grandpa assets. No campaign page, live reader, model, source grant or index was migrated. Published a [draft Table Reference contract and maintenance workflow](../Table-Reference-Standard.md), a [template](../../Templates/Table-Reference.md), and an authoring-only format validator. Workspace and repository instructions cover both player-requested edits and voice-session closeout.

## Measured

Ten-page structural inspection: all ten have Overviews; none has the proposed machine-readable contract. Frontmatter spans 16–64 lines. Type labels vary: five `player-character`, one `pc`, two `entity`, two `vehicle`. Grandpa is an asset in the Locations directory, so directory alone is not a reliable type contract. All ten source revisions match their existing voice approvals; metadata is also within approved ranges.

Twenty frozen same-author questions through the actual bridge prefetch yielded eleven own-page passages, eight empty results and one ambiguity boundary. All six PC specialties questions missed initial retrieval; both asset-class questions also missed, while both ownership questions retrieved own pages. These are retrieval diagnostics, **not model-answer or voice success rates**. A correct page hit is not proof the requested fact was fetched. No evaluator retries replaced outcomes.

Five validator test methods pass. All ten current pages are explicitly reported **unmigrated**, not validated; requiring a block correctly rejects an unmigrated page. Draft example formatting passes. Truth, permissions and source agreement require separate review.

## Still open

Recommend a small, separately approved cross-class pilot of a versioned `table_reference` YAML mapping near the top of each file, plus a generic validated reader/projection. YAML alone does not fix current query interpretation or indexing. Preserve unknowns, qualifiers, lifecycle status and provenance; reference current balances/native tables instead of duplicating them.

The update rule is installed now: whenever an existing reference block is affected by a player edit or session closeout, synchronize it with supporting prose/history/ledger in the same change, validate its format, and review source agreement. Missing blocks remain unmigrated until approved migration. Pinned source edits still require staging, review/rebind and separate activation.

Overall voice project remains in progress. No bulk conversion, schema deployment or new live voice capability is claimed.

## Corrections

This replaces a Mevin-specific tuning direction with class-wide evidence. Existing Overviews show the corpus is not simply missing all facts; nonuniform structure and generic query/selection failures both matter. Machine metadata and assertion labels are not authority or permission grants.
