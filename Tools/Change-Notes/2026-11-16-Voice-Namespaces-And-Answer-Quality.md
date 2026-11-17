---
title: "2026-11-16 — Speakable campaign namespaces and answer-quality guards"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-16
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-16
---

# Speakable campaign namespaces and answer-quality guards

## Shipped

Bridge commits `eae3ece` and `d983d2d` are pushed on the bridge's main branch. They widen speakable campaign namespaces, stop equipment declines from falling through to the OCR corpus, and preserve supported answers that were being lost after retrieval.

`WAKE_SAFE_DOC_PREFIXES` now admits Sessions, Documentation, Clues, Timeline, Recaps, Current-State, Maps, Trailer-Video-Scenes and New-Player-Welcome. The new `WAKE_UNSAFE_DOC_SEGMENTS` deny excludes `Cindy-Lou-Jenkins-Tooling/`: Cindy's own tooling notes contain test names, harness paths and failure strings.

The GM explicitly preferred this tradeoff: “Slow bad answers are a much bigger concern.” The stated concern about secret information was limited, with a possible exception deep in Host information; even “GM Only” material was not a major concern in this decision.

An equipment-domain decline is now terminal for the unified campaign lane. In `_campaign_unified_prefetch`, `wake_equipment_tier=declined` returns an empty result instead of searching `03_pages/`.

The answer-quality changes retry `content=null` rather than treating missing model text as an opaque failure; `_fail` now traces errors. The model lane strips markdown before applying the answer cap. An “answer is too long” contract error now truncates to the spoken cap instead of discarding the answer. Evidence-required, no-source, ungrounded-reference and ungrounded-entity contract failures still discard.

Bare-page citations now resolve when exactly one section of that page was read in the request. Ambiguous or unread pages still fail resolution. This covers the registry's heading-kind citations, including `wiki/PCs/Mevin-Kitnick.md`. The regression test is `test_bare_page_citation_resolves_and_unread_page_does_not`.

### Why it broke that way

Registry approval and code-level namespace admission were separate gates. `_campaign_namespace_allowed` in `voice_chat.py` ran after registry filtering; namespaces with no approved pages could not pass. Tools, Sessions, Documentation, Clues, Timeline, Recaps, Current-State, Maps, Trailer-Video-Scenes and New-Player-Welcome were outside the cited approval set, including `Tools/Change-Notes.md`. Those asks fell through to the model. The widened prefix list does not establish that every page in those namespaces is now registry-approved.

The grenade damage ask previously spent 5.7 seconds before falling through to OCR search, after which the rules tier abstained (session capture log, transcript 18:12:48).

Handler inspection found separate post-retrieval failures: Mark Quasar returned null model content, Mevin's answer carried markdown, and Grandpa's evidence-grounded answer contained 13,503 characters and was discarded for length (ad-hoc probe). The citation resolver also required a section-qualified citation format, dropping bare-page references.

## Measured

- Namespace-block counters in `voice_bridge.log`: Tools 380, Sessions 217, Documentation 58, Clues 51, Timeline 27, Recaps 13, Current-State 19, Trailer-Video-Scenes 3 and New-Player-Welcome 2; total across all recorded namespaces 975 blocks, alongside 837 admitted candidates (ad-hoc probe). Maps had no separately listed counter.
- The same eight-case offline replay changed Mevin, Kurgan and Curtis's drone-list asks from abstentions to answers in 0.42, 0.40 and 0.27 seconds respectively (ad-hoc probe).
- Mevin's decker ask changed from no answer after 17.4 seconds to an answer in 8.6 seconds (ad-hoc probe).
- HE grenade damage changed from a 19.6-second OCR dive to a deterministic answer in 0.01 seconds; Ares Predator II stats changed from no answer after 25.0 seconds to a deterministic answer in 0.01 seconds (ad-hoc probe). These outcomes also depend on the reviewed-table extension described separately.
- Grandpa's parking ask changed from abstention to a session-backed answer in 18.1 seconds; that model-run timing varies. Mark Quasar still declined for lack of canon data (ad-hoc probe).
- Speech sanitization passed 55 cases; the full suite at the answer-guard checkpoint passed across 25 test files (unit test).
- The restart's boot source hash matched committed `voice_chat.py` (ad-hoc probe).

## Still open

Offline replay and handler inspection do not establish received Discord wake delivery, TTS playback or listening acceptance. The evidence does not provide a Maps block count or establish blanket registry approval for the widened namespaces. The Mark Quasar decline remains an absence-of-canon result, not a demonstrated new campaign fact.

## Corrections

No corrections to the shipped implementation are recorded in this entry.

[Back to change notes](../Change-Notes.md)
