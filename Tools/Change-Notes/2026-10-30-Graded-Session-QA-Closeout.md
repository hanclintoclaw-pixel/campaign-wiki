---
title: "Graded table-question rehearsal: closeout and future work"
type: change-note
visibility: player-safe
updated: 2026-10-30
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-30
---

# Graded table-question rehearsal: closeout and future work

Closeout for the 2026-10-30 voice-bridge rehearsal across `discord_voice_patch`, `memory-system`, and `campaign-wiki`. This records the fixes that shipped, what the 12-question rehearsal found, and the remaining work. See the earlier [wake retrieval and narration](2026-10-30-Wake-Retrieval-And-Narration.md), [rules retrieval](2026-10-30-Rules-Page-Retrieval.md), and [web escalation](2026-10-30-Web-Escalation-Tier.md) notes for the individual changes.

## Shipped

- In `discord_voice_patch`, commits `667af63`, `d6b6c70`, and `29d3fc9` addressed three false denials, narration stripping and its kill switch, and documentation that had described a session-specific narration leak incorrectly.
- Commit `7fa9c46` ranked sections that list an answer above passing mentions. Commit `d2413e2` routed the rules hop through printed-page-aware accept/decline serving. Commit `2226346` added budget-gated tier-3 web escalation, and `5987688` corrected two overturned planning claims.
- In `memory-system`, `7b0a8f9` anchored snippets on discriminative terms and `dd98d75` changed rules retrieval to printed-page lookup with accept/decline decisions. Related wiki notes were published as `63acbd6`, `1d71bfc`, and `fea1f52`.
- The 12-question production-path rehearsal found four defects in the same-day bridge changes. Commit `a2758c2` fixed deflection matching (it had fired 0/12 times), restored the configured 40,000-character wiki fetch (production had silently remained at 6,000), raised the escalation timeout from 25s to 45s, and ignored error-marked payloads so harness errors could not become spoken answers. The rehearsal and fixes are in `session_qa_eval.py` and `voice_chat.py`.
- Tier 3 is enabled in production by `LIVE_WAKE_WEB_ESCALATION_ENABLED=true`. It may run once only when local retrieval injected zero characters and the answer is a deflection; local facts block it. Three budget floors gate the call, the session cap is six, and failure falls back to the original deflection. The escalation model is `openai/gpt-6.1-sol` at low thinking. It must confirm SR3 edition and only voice source-checked SR3 numbers read during that turn. These are implementation rules, not evidence that the feature has fired in a live game.
- The superseded 2026-10-26 restart draft `e0c9bdfc` is not part of this closeout and must not be published.

## Measured

- The graded rehearsal sent 12 realistic questions through the production retrieval and model path: 4 clean-correct answers, 3 answers with citation defects, 1 misclassification, 3 honest deflections, and 1 fabricated answer (ad-hoc rehearsal using `session_qa_eval.py`).
- Clean answers included Curtis’s Karma Pool 9 and Good Karma 25, the scorpion drone’s fate, the Drone Shift side job, and Drain Resistance using Willpower on p.183. The rules answer also matched the local corpus (ad-hoc rehearsal).
- Citation defects: Predator 9M was spoken as p.280 instead of injected `sr3.278`; throwing knife (STR)L was spoken as p.278 instead of injected `sr3.276`; and a salvage answer cited a page that had not been injected (ad-hoc grading against the retrieved evidence).
- The roster answer counted vehicles Grandpa and Belmont as drones. The fabrication named “Robotics: Piloting,” linked it to Quickness, and voiced it despite no corpus occurrence of “Robotics” and no “piloting” skill row (ad-hoc corpus/dataset check).
- Three deflections were honest but incomplete: whitelist names, Backpack Arms total cost, and Rating 3 drone price. The whitelist names—Ernie Pollock, Ziggy Hill, and Lizzo Wells—were on the scorpion page (ad-hoc grading against the wiki).
- Retrieval took 40–450ms; wake-model turns took 2.9–14.0s; median end-to-end latency across the 12 questions was 3.73s. The escalated Drain Resistance answer took 32.2s overall. Timings are ad-hoc rehearsal measurements, not live-session capture data.
- Escalation search-only probes took 12.99–19.38s; complete search/adjudication/emission attempts took 20.6–26.4s, with three of four earlier attempts timing out at the 25s cap (ad-hoc probes). Fetching 40,000 wiki characters measured 0.054s, the same as 6,000; the cold 462-entry lexicon build measured 0.064s (ad-hoc probes).
- Regression suites passed after the fixes: web escalation 65/65, tiered lookup 65/65, equipment tier 55/55, and emoji speech 38/38 (unit tests).

## Still open

1. **Block unsupported rules claims.** “The corpus could not corroborate” did not trigger deflection/escalation; the model still invented “Robotics: Piloting.” Catch this answer shape and prevent unsupported skill names or numbers from being voiced.
2. **Preserve citations verbatim.** Equipment pages drifted by +2 pages, and the salvage answer cited evidence not supplied to the model. Voice citations from the retrieved row rather than asking the model to recreate them.
3. **Keep campaign questions off the public web.** The tier-3 screen considers question shape, not whether a question is campaign-specific; Backpack Arms was web-eligible. Restrict escalation to SR3 rules questions and test the boundary.
4. **Fix equipment relevance without breaking broad gear asks.** Irrelevant “Total Pacifist” and “GM Mr Fix-It” rows entered campaign answers. A proposed two-shared-token gate broke valid category queries (commlink, medkit, body armor, datajack, cyberdeck); design and validate a safer relevance check.
5. **Exclude template stubs from retrieval.** Tier 1 routed the whitelist question to an unfilled True Names template instead of the scorpion page containing the answer.
6. **Reconcile rules and equipment retrieval before enabling the rules tier.** `rules-answer` declined the Ares Predator query while the deterministic equipment tier found it; fix the cross-tier mismatch and improve the tier’s 23% recall (ad-hoc evaluation).
7. **Verify web search in live play.** The provider was configured and rehearsal/probes succeeded, but tier-3 firing and latency still lack live-session capture evidence.
8. **Reconcile activation telemetry. `equipment_accepted` events exist on 2026-10-29 despite the reported zero-activation result; establish what the events mean before repeating that claim.
9. **Repair source coverage.** OCR/image gaps remain in Handbook, Rigger 3, System Failure, and Matrix pages.
10. **Investigate the reload failure.** The 2026-10-21 `thinkingLevel: off` reload issue and `llama-swap` behavior remain unresolved.
11. **Review the memory-system worktree separately.** Seven pre-existing modified files were left untouched; `scripts/equip_query.py` is also untracked, along with two start scripts. Assess these separately; this closeout does not commit them or `Tech/Equipment.md`.
12. **Revisit lexicon freshness and voice-path design.** The 600s name-index cache can delay discovery after an edit, though file contents are read fresh and a cold rebuild measured 0.064s. Voice prefill pruning and dynamic tool loading also remain unassessed.
13. **Audit escalation planning docs.** Confirm no stale or overturned claims remain outside the corrections already recorded in `5987688` and the earlier change notes.

## Corrections

- The earlier `7fa9c46` note said Curtis’s fetch had reached 40,000 characters; that described the dataclass default, not production. The loader still forced 6,000 until `a2758c2`.
- The earlier explanation that web escalation needed an API key or reflected policy was wrong. The key-free Codex Hosted Search provider needed explicit selection as `tools.web.search.provider=codex`; no key or spend was required.
- Do not treat the rehearsal’s correct answers or passing unit suites as evidence of live-session firing, and do not treat a plausible citation as evidence the cited page was retrieved.
