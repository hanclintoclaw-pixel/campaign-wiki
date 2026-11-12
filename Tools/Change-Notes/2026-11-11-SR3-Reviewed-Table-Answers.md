---
title: "2026-11-11 — PDF-reviewed SR3 table answers and printed citations"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-11
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-11
---

# PDF-reviewed SR3 table answers and printed citations

## Shipped

JackalMoreau approved the offline review and live activation on November 11. Bridge commits `32ec83c` and `7083d6e` are deployed and pushed on the bridge's main branch. The reviewed-table feature is enabled in the restarted bridge: **SR3 reviewed-table live activation, November 11**.

The bounded deterministic path covers selected firearms, ammunition prices, range bands, armor ratings, ranged modifiers and visibility. It preserves table headers, units, qualifications and verified printed-page citations. A firearm's Ammo field is not its Range; ammunition prices retain their per-ten-shots basis. Campaign admission still runs first. Covered replies bypass model rewriting; unsupported table interpretations decline or request clarification.

This is a reviewed transcription, not a universal table extractor. The source PDF revision is hash-bound. Changed or unavailable source evidence fails closed. The code default remains off; the live deployment explicitly enables the feature. Rollback is disabling that feature and performing an idle bridge restart.

Qwen/model settings, playback controls and campaign source coverage were preserved. Proactive rules search remains disabled.

## Measured

- Offline production-dispatch replay: **20/20 reference outcomes**, comprising **16/16 supported cited answers** and **4/4 required declines or clarifications**. These are synthetic cases, not an unseen accuracy sample.
- Source-review evidence: **16 selected rows across 9 visually inspected PDF pages**, with individually verified printed folios and source hashes. Native-text audit checked row/header/semantic associations; a deliberate adjacent-row substitution was rejected.
- Unit-test evidence: **45 test methods passed**, including both real wake handlers with external services mocked, campaign precedence and failure controls. Earlier offline regression evidence also recorded **55 equipment checks, 38 speech-sanitization checks and 5 duration checks** passing. The 45-method suite was rerun successfully in the deployment worktree.
- Deployment ad-hoc probe: **20/20 installed-dispatch cases passed** using the real configuration and campaign binding; only the capture sink was replaced. This is subprocess/text-path evidence, not a received Discord voice wake.
- Fresh bound campaign-dependency probe returned a supporting Mevin Kitnick passage and exact source revision with status `ok`.
- Launchd/runtime evidence: new bridge PID `9744`, started November 11 at 22:40:19 EST, after the reviewed commit. This boot's source hash matched the deployed file; Discord readiness and inactive-session restoration succeeded. The capture root was writable. No queued unclaimed response existed before restart.

## Still open

Human speech recognition, actual Discord wake delivery and listening acceptance for these new answers remain untested. No end-to-end audio latency or live-answer accuracy claim is made.

Unreviewed equipment and rules retain their existing retrieval paths and limitations. The unchanged broad rules evaluator still has only **7/11 combined precision** on its separate retrieval test; this release does not establish universal rules accuracy.

## Corrections

The earlier offline review's default-off and not-deployed statements describe the pre-approval state; this entry records the subsequent authorized activation. Baseline replay measured retrieved candidates, not generated answers, so it cannot establish a before/after model-answer accuracy improvement. Installed dispatch and mocked-handler checks are not human audio acceptance.

[Back to change notes](../Change-Notes.md)
