---
title: "Wake retrieval ranking, snippet anchoring, and three retractions"
type: change-note
visibility: player-safe
updated: 2026-10-30
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-30
---

# Wake retrieval ranking, snippet anchoring, and three retractions

Bridge changes are in `voice_chat.py` (`cindylou-voice-bridge-backup`); retrieval changes are in `05_serving/memory_bridge.py` (`cindylou-memory-system`).

## Shipped

- `667af63` — retrieval ranking and excerpting, equipment row projection, capture-error suppression, and spoken-output cleanup (git history).
- `d6b6c70` — the narration filter now strips text instead of only logging it. `TTS_STRIP_MACHINERY_NARRATION_ENABLED=false` now works; the configuration key was never wired to the config object, so the documented kill switch had no effect (git history).
- `29d3fc9` — documentation corrected the narration-leak measurement scope to the played session rather than the whole log file (git history).
- `7fa9c46` — a section that lists the answer now ranks above sections that merely mention the subject (git history).
- `7b0a8f9` — snippets anchor on a discriminative query term instead of the first word the asker typed (git history).

Wiki ranking gained enumeration shape, a stub penalty, and an archive discount. Archives stay eligible rather than being deleted: dropping them would rebuild the false-denial failure this function exists to prevent.

Deploy: the bridge restarted onto `7fa9c46` as PID 24724 at 10:05:36. Startup recorded `on_ready user=CindyLouBot#0465` and `precache ok=True rendered=15 failed=0` (startup log). An earlier restart, PID 14979 at 08:52:38, landed on `d6b6c70` (startup log).

## Measured

After all changes: `test_equipment_tier` 55/55, `test_tiered_lookup` 65/65, `test_emoji_speech` 38/38, `collection_trigger` 6/6 (unit test).

The narration filter removed machinery language from 5 real leaked reply lines from the last played session and changed nothing in 3 ordinary table-talk lines (ad-hoc probe).

The Curtis wiki fetch previously stopped at 6,000 characters, short of the nuyen line at character 6,895 and the first drone mention at character 7,564 (ad-hoc probe). The ceiling was raised to 40,000 characters, which measured 0.062s against 0.043s for the 6,000-character fetch (ad-hoc probe) — the CLI was never the constraint. Density scoring separately ranked an incidental "Drone Shift" mention and a 32,700-character work-order archive above the section that names all six drone assets. At the production 1,600-character budget the revised path surfaces the drone roster, the nuyen balance of 19,503.33, the karma pool, and work orders (ad-hoc probe).

For the rules path, "how much damage does a pistol do" had anchored on the first "how", inside the credits block at character 6,875 of 1,430,539 in the SR3 Handbook, which is why a pistol-damage question surfaced typesetting credits. When the first term was absent from a document, the fallback returned the literal file opening, exposing mangled cover text. Anchoring now selects highest IDF, then longest term, then most frequent, keeping the old fallback when no term is present (ad-hoc probe). Anchor choice never touches score, so ranking is unchanged: scores were identical across 4 rules queries, and campaign scope held at Princeps Group 20.485 and Grandpa 10.562 with no page-marker noise in any snippet (ad-hoc probe).

## Still open

"What gear does Curtis carry" still misses. "Gear note" is buried inside one long dossier bullet, so no short bullet carries the term.

`PCs/Curtis.md` is 62,835 characters and still exceeds the 40,000-character fetch ceiling, so the tail of the page remains unreachable to the wake path. Four other pages also exceed it: `Sessions/2026-10-22-Sol-Alternate.md`, `Templates/TEMPLATE_CONFORMANCE.md`, `Timeline/Session-Chronology.md`, `Trailer-Video-Scenes.md` (ad-hoc probe).

Rules probes still fail to answer pistol damage code, stealth governing attribute, and pistol range band. Drain-test dice did return Force and Drain (ad-hoc probe).

Front-matter work remains a dry audit; nothing was written to the corpus. It covered 54 books and 3,864 pages, classifying 117 pages (3.0 percent) across 27 books as leading front matter. Of those, 13 pages across 6 books carry stat or rules number shape and are unsafe to auto-delete: Critters p6 ("Pool rules for astrally projecting characters"), Quick Start p11 (the Rule of One), and Rigger 3 p5 (a table of contents whose lines are real rule names) (ad-hoc probe). Audit: `/Volumes/carbonite/claw/data/cindylou/audits/2026-10-30T10-21-45-front-matter-audit.json`.

There is no chunker or embedding index to re-run. `memory_bridge.py:208` records "Fallback semantic mode: keyword retrieval until embedding index endpoint is wired"; the corpus is walked with `rglob` at query time, and `cindylou rebuild` runs campaign builders only (ad-hoc probe).

Live configuration: tiered lookup enabled, rules search disabled, equipment and prefetch unset and therefore defaulting enabled, voice wake disabled, active-thread wake enabled, wake model `Qwen3.8-Flash-Next-NVFP4` with thinking off (ad-hoc probe).

## Corrections

The claim that the Curtis retrieval failure was caused by OCR front matter needing a re-chunk was wrong, and it was made verbally in chat rather than in any published page. OCR front matter exists only in the OCR'd rules corpus, which the semantic rules tier reads; that tier is disabled by `LIVE_WAKE_RULES_SEARCH_ENABLED=false`. The wiki path that actually failed reads hand-authored Markdown with no OCR in it: `PCs/Curtis.md` is plain UTF-8, hand-authored, and no campaign-wiki Markdown contains OCR-mangled text. Two independent retrieval paths were conflated. `2026-10-28-Wake-Excerpts-And-Rules-Honesty.md` and `SUBSTANTIVE_ANSWERS_FROM_SOURCE.md` were re-read during this correction and both scope the front-matter concern correctly to the rules tier; neither blames the wiki, so neither needs amendment.

An earlier "byte-identical before/after" claim about front-matter stripping measured nothing: the probe called the search twice without ever applying the strip function. That claim is retired.

Four measurement harnesses were written wrong today, and each produced a confident wrong answer before being caught: a raw regex substituted for the composer's own matcher; the double-call above; a `[-2]` path index applied to a path containing no slash; and a mirror that flattened 54 book directories to bare filenames so files overwrote each other (ad-hoc probe). Standing lesson: a claim is reported only from a harness that can be pointed at.
