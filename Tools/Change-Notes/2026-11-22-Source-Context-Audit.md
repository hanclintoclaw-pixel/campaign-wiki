---
title: SR3 source-context audit — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Read-only SR3 source-context audit

## Shipped
Nothing changed in the corpus or live bridge. This is a bounded diagnostic of ten
reader windows across three admitted SR3 books and combat, magic, Matrix and rigging
material. Selection deliberately includes demonstrated misses and responsive controls;
it is not a random sample or a corpus-wide prevalence estimate. The frozen-window
SHA is `cd924a46…017bdd1`. All source/PDF hashes remained unchanged.

Sol inspected the reader implementation, exact returned windows, adjacent source
pages and selected PDF witnesses. No implementation was needed for this read-only
audit. Core native-text witnesses confirmed the parent context for melee Full Defense
and adept Attribute Boost; rendered Core and Quick Start pages confirmed layout and
folios. The sampled Quick Start and Man & Machine PDF pages returned no native text;
that does not mean their OCR source is absent. No global page-offset rule was used.

## Measured
- **3/10 specific target headings lie on an earlier page.** Core printed p.124
  continues Full Defense from p.123, within Resolving Melee Combat; adept Drain on
  p.169 continues Attribute Boost under Adept Powers on p.168; Quick Start printed
  p.23 continues ranged staging before starting melee material on that same page.
- **2/10 returned pages are capped at 5,700 body characters**, without a truncation
  flag. The Core p.44 cut removes a table denominator and subsequent Dice Pool Table
  rows, although the formula prose remains available. The other cut splits the end
  of a timing-table unit. These are reader-window cuts, not proof of corrupted books.
- **0/10 expose structured section ancestry or usable source-line offsets**;
  `source_line` is null. None exposes an explicit completeness/truncation flag.
- Useful local headings already exist in other windows: The Combat Phase, Drain,
  Duration, Control Pool/Hacking Pool, Detection Factor and Cyberware and Hacking Pool.
  The bonus-only answer to a formula question is not excused by a missing heading.

The printed Core p.124 layout mixes a melee continuation, knockdown, shock weapons,
barriers and cross-references. A ranged reference inside that page does not make its
opening paragraph a ranged-combat ruling. Quick Start p.23 visibly has a ranged
continuation/diagram above the start of melee combat. A whole-page mechanic label
would also be wrong. Attribute Boost is a mixed-case heading; all-caps-only extraction
would miss it. PDF columns, tables, repeated headers and OCR ordering make "nearest
uppercase line" unsafe as an automatic ancestry rule.

Verification: ten frozen windows revalidated against current source SHA revisions;
returned bodies equal the corresponding full-page prefix; cap/metadata counts were
recomputed; selected PDF hashes were rechecked. PDF witnesses and per-window reviewed
findings are retained privately. No new answer-quality, latency, STT or playback
measurement is claimed, and no earlier failed source-context control is regraded.

## Still open
**Recommend a small general section-aware reader-view pilot, not a database rebuild
or another special-case prompt.** Keep canonical source bytes immutable. Use one
revision-bound schema for exact spans, local/parent heading references, cross-reference
links and completeness flags. Preserve headings as source-derived data, not hardcoded
rule answers or individual page branches. Unknown ancestry must remain unknown.

Build only a reviewed sidecar for the sampled spans first, with a generic reader view
that keeps sections/paragraphs and table units intact within the existing budget.
Do not concatenate arbitrary neighboring pages, label a whole mixed page as one
mechanic, or infer scope merely from a cross-reference. Preserve source permissions,
exact read/revision binding and discovery budgets; insufficient context must not
silently authorize extra material.

The next candidate should be implemented in bounded Qwen jobs and independently
verified on Sol. Test both applicable and inapplicable uses of the same material,
across families, while preserving supported coverage. A better view must demonstrate
improvement; it cannot confer correctness on the model's judgment. Source annotation,
runtime integration and activation remain separate approvals. No pilot was built here.

## Corrections
This supports a general reader-presentation defect **and** leaves a separate model
responsiveness/judgment defect. It does not show that all ten windows are unusable,
that the whole corpus needs cleanup, or that section ancestry alone will fix the
voice experience. The [responsiveness experiment](2026-11-22-Answer-Responsiveness-Trial)
still failed safety; the last actual handler replay remains 1/8 answerables.

Production remains `81e9eeb`; no restart, model/configuration/source-grant or live
source change. Private evidence: data-tier `runtime/source-context-audit-20261122`;
audit scripts: project `workfiles/source-context-audit-20261122`.
