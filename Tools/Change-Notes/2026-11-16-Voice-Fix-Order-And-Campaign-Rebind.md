---
title: "2026-11-16 — Campaign-memory rebind and budget-aware voice routing"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-16
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-16
---

## Shipped

The GM authorized this fix order: rebuild and rebind campaign memory; fast-reject unreviewed gear; route combat-modifier questions to reviewed tables; stop abstain nudges without sufficient budget; shorten the canned non-answer. The same authorization ordered the earlier probe trashed. The evidence pack records that instruction, not a disposal receipt.

The activation record and smoke-probe evidence record a rebind from 607 to 635 approved sections, sourced from wiki checkout `0e85289`. Added content covers Jet Set Morgan’s Table Stats, Sleazy Tabloid Reporter, Augmented Beef and Bacon Social Club, Quick Resolution Decking, and Reputation optional rules. Morgan’s stale Voice-status footer was excluded; the club’s authored open-questions caret was dropped. The evidence records zero widened-without-review ranges and nine pending-unresolved baseline cases, retained for GM ruling rather than silently removed.

An isolated refresh used the released index-refresh script. The activation record reports valid index identity, complete vectors, 635 manifest-matching files and 1925 chunks. All 30 smoke checks passed in unit-test/ad-hoc-probe evidence, including new-page reachability, exact-revision reads, denied content and invented-name controls. During the stale-binding window, lookups failed closed; the activation record reports no session or wake traffic inside it. Rollback remains restoring `.env.bak-sweep-20261116` over `.env` and restarting; the previous binding and authority files remain untouched.

Bridge commits `e4ea0b4`, `a354851`, `6d62380` and `f1e8d28` implement the remaining routing changes. `e4ea0b4` makes known-brand, unreviewed weapon-stat requests decline before corpus fallback and recognizes conversational cover wording. Cyberware, bioware, chemicals and vehicle-body questions retain their corpus routes; connective-word rejection still blocks misleading smartlink wording. `a354851` consults reviewed tables before campaign-model fallback, short-circuiting only answered rows. `6d62380` records the dispatcher deadline, gates abstain nudges on remaining budget and shortens the fallback. `f1e8d28` lets a named campaign entity outrank bare “rule(s)”; explicit edition wording still selects rules retrieval. The commits, plus verification probe commit `62d8ea3`, are now pushed to the bridge repository’s `main` branch.

The campaign-memory pointer swap required a bridge restart. `launchctl kickstart -k` returned rc=64; restart completed through SIGTERM and launchd KeepAlive respawn, rather than a successful kickstart.

## Measured

The replacement ad-hoc probe replayed questions that failed in the earlier voice test. It used the real public wake handler, bound campaign adapter and local model, but mocked Discord, STT, audio and emission. These are synthetic handler results, not human listening acceptance.

Ad-hoc probe results: partial-cover wording answered through the table in 0.019 s; Ares Light Carbine 300 and Ares Pretty Peter III requests each declined in 0.002 s. Sleazy Tabloid Reporter answered in 5.548 s, correctly distinguishing the published contact archetype from a campaign NPC. The club answered in 14.004 s; Quick Resolution Decking in 5.394 s. Morgan’s identity returned in 0.445 s, while the counterfeit-material question answered from newly bound content in 5.539 s.

Reputation initially timed out at 25.011 s in the ad-hoc probe because bare “rule” selected corpus retrieval. After `f1e8d28`, the same ad-hoc probe question answered through the campaign path in 11.259 s.

Grandpa’s location answered in 18.517 s in the ad-hoc probe, citing the September session; no abstain nudge fired. The earlier canned non-answer was measured at approximately 13.8 s of speech and was replaced by approximately 6 s. The nudge configuration requires run and last-step durations each below 6.0 s and at least 8.0 s remaining; these thresholds belong to the implementation exercised by the unit tests.

## Still open

- Mark Quasar has no wiki page; the offered page awaits a GM response.
- The unresolved registry baselines need GM rulings.
- Pre-existing failures remain in capability-tier, collection-trigger, tiered-lookup, wake-session-mode and web-escalation suites.
- Whether Grandpa moved after the cited session requires closeout review.
- Human listening acceptance remains unestablished.

## Corrections

The earlier 2026-11-16 “Speakable campaign namespaces and answer-quality guards” entry said commits `eae3ece` and `d983d2d` were pushed. The evidence pack’s remote check found that those commits, along with other earlier commits, had not yet been pushed at that check. The subsequent push advanced the bridge remote from `c6e20cd` to `62d8ea3`; local and remote `main` then matched, including the four fixes and verification probe. This corrects the earlier entry’s push-status claim.

The evidence pack’s failing-suite total conflicts with its named list, so no total is repeated here. Synthetic handler success does not establish received Discord audio or spoken-answer quality.

[Back to change notes](../Change-Notes.md)
