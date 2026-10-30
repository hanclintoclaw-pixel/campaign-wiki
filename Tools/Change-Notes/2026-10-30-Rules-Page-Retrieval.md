---
title: "Rules retrieval: page-level units and gated answers"
type: change-note
visibility: player-safe
updated: 2026-10-30
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-30
---

# Rules retrieval: page-level units and gated answers

This continues `2026-10-30-Wake-Retrieval-And-Narration.md` from the same day. Retrieval code lives in `memory-system/05_serving/memory_bridge.py` (commit `dd98d75`); the bridge instruction change lives in `voice_chat.py` (commit `d2413e2`).

## Shipped

Previously `keyword_search` scored whole books: it could identify a matching book, but a heuristic selected the displayed excerpt. The new layer splits the `===== PAGE n =====` markers the OCR pass already wrote, computes IDF over printed-page units, and anchors the excerpt window on the candidate ruling rather than on the first word the asker typed. Citations use each page's own printed footer, not the marker value: markers run +2 ahead of printed folios, measured across 284 legible footers in the core rulebook (ad-hoc probe). Splitting every page cold costs 0.474s across the corpus (ad-hoc probe), so no chunker or embedding index was added; retrieval remains keyword-based pending an embedding endpoint.

`cindylou rules-answer --q ... [--limit] [--min-books] [--max-chars] [--shape-allow]` was added (`dd98d75`). Unlike ranked-list `cindylou search`, it returns an accept/decline decision with cited pages: accepted is true only when at least `min-books` distinct rulebooks carry the asked-about term inside the excerpt that would be read aloud. Excluded directories — adventures, scenarios, fan, indexes, misc — are filtered during traversal, before limits consume candidate slots; the tier previously cut them after the limit, so an adventure module in a top slot cost the retrieval its best candidate instead of being passed over.

In `voice_chat.py` (`d2413e2`), the live lookup rule now sends rules questions to `cindylou rules-answer` instead of `cindylou search --scope rules`, and tells the model to say what is missing when `accepted=false`. The old hop handed the model a contents page for the stealth-linked-attribute question ("Etiquette 93 Etiquette 94 Instruction 95 Using Stealth 95"). The new hop measured 0.50s against 1.05s, 3 runs each (ad-hoc probe), so the change is cheaper as well as better-cited. Proactive rules injection through `LIVE_WAKE_RULES_SEARCH_ENABLED` deliberately remains disabled; see Measured.

## Measured

`memory-system/scripts/rules_eval.py` (new, `dd98d75`) holds 13 accept cases whose expected strings were grepped from the corpus before use, and 8 decline cases covering SR3 vocabulary these 54 books genuinely lack. `--legacy` scores identical cases through whole-book retrieval; `RULES_MIN_BOOKS` and `RULES_SHAPE_ALLOW` expose the gating controls. Combined precision counts every wrong thing spoken — accept-set misses and decline-set leaks alike — because a fluent wrong ruling delivered with a citation costs the table more than "check the weapons table".

- Legacy whole-book: 4/13 precise, 9 wrong, 0 declined; 0/8 decline cases shut. Precision when speaking 31% (eval harness).
- Page-level, `min_books=2`: 7/13 precise, 2 wrong, 4 declined; 6/8 declines shut. Combined precision 64%, recall 54% (eval harness).
- Page-level, `min_books=3`: 4 precise, 0 wrong. Combined precision 67%, recall 31% (eval harness).
- Shape allowlist (attribute_link, damage_code, range_band, drain_code), `min_books=2`: 3 precise, 0 wrong, 1 decline leak. Combined precision 75%, recall 23% (eval harness).

The allowlisted operating point is judged fit for on-demand voicing — which is where it ships, in the model's own lookup hop. Its recall does not justify a proactive tier, so tier 2 stays off.

Regression suites unchanged: `test_equipment_tier` 55/55, `test_tiered_lookup` 65/65, `test_emoji_speech` 38/38, `collection_trigger` 6/6 (unit test).

## Still open

The drain-resistance ruling is present in the corpus ("To offset the Drain, make a Drain Resistance Test using", core rulebook line 15237) and is not retrieved; the complex-action target-number ruling is likewise unretrieved. These are recall gaps, not corpus gaps, and closing them is what would let the proactive tier earn enablement.

Two decline leaks remain (eval harness): soak test and wound penalty, where OCR prose contains a damage-code or target-number string near the asked-about word without actually stating the ruling.

No corpus files were changed. The front-matter audit from earlier today remains dry-run only.

## Corrections

Four score-booster attempts each promoted a fluent wrong page, and the design was changed from boost to rank-and-gate (eval harness): coverage weighting; a 1.9–2.4x shape multiplier; the same multiplier with family cue words excluded from candidacy; and mandatory shape matching. The specific promotions that had to be rejected: "Edged Weapons (Strength) governs the use of hand-held melee weapons" answering a stealth-attribute question, because "governs" is simultaneously a query term and the attribute-link cue; a Year of the Comet random SURGE "3D6" table answering a drain-dice question; and OCT field-agent prose answering a range-band question because "quickly" contains "quick".

An earlier stealth PASS in the harness was false: the excerpt concerned the Aquatics skill page while the expected ruling merely fell within the same 900 characters (eval harness). The harness now requires the asked-about term within 180 characters of the ruling; earlier precision figures were optimistic.

Absent subjects must decline rather than fall back. "Countermagic" has document frequency 0 across the rules corpus; an early version dropped it from candidacy and let "test" (df 1,081) become the subject, which nearly every page contains, admitting an unrelated dice-pool page. A missing grep hit is evidence about the corpus, not permission to approximate.
