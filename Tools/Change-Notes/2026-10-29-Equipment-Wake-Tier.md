---
title: "Equipment wake tier and VERIFIED/SR3 trust gate"
type: change-note
visibility: player-safe
updated: 2026-10-29
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-29
---

# Equipment wake tier and VERIFIED/SR3 trust gate

## Shipped

Commit `e8746e1` added an equipment stat tier to the wake path in `voice_chat.py`. Named weapon, cyberware, armor, and ammunition questions retrieve sr3data equipment tables through `equip_query.py` instead of relying on generated stats (unit test).

The intent gate, `_wake_looks_like_equipment_question`, separates equipment questions from rules rulings. It admits “what's the damage on an Ares Predator” and declines “how does stun damage work,” “what's the target number for this,” and “who leads the Princeps Group” (unit test). Rulings remain the GM's responsibility.

The trust gate permits only VERIFIED or SR3 rows into the prompt. WEAK and QUARANTINED rows are refused. Quarantined material includes Shadowrun Second Edition and Cyberpunk conversions. A dedicated frag-grenade trap asserts that no quarantined stat reaches the prompt (unit test).

Equipment retrieval runs before semantic rules search. It is deterministic and supplies a book.page citation. The comparison was about 0.1 seconds for equipment against roughly 2.2 seconds for rules search (unit test). Rules search remains disabled, leaving equipment as the only live rules-adjacent tier.

VERIFIED corroboration reads PDF text layers directly, not corpus markdown, so that evening's corpus de-duplication could not have degraded it.

Implementation exposed normalization and harness traps. `_wake_norm` strips all whitespace, making multi-word intent patterns such as “submachine gun” and “how does” unreachable. The module-level `_wake_equip_norm` preserves single spaces (unit test).

The intent method initially fell outside the harness's auto-resolved `_wake_*` namespace. Its `@staticmethod` decoration also double-bound under `__get__`. Moving the method into that namespace and the normalizer to module scope resolved those failures (unit test).

## Measured

`test_equipment_tier.py` passed 55/55 tests on three consecutive runs (unit test). `test_tiered_lookup.py` passed 65/65 as the existing-wake-tier regression check (unit test).

The equipment subprocess cold-started in 0.088 seconds, stable across eight runs (ad-hoc probe).

An earlier equipment-suite run reported 12 failures while an unrelated recursive scan accessed the external data volume; three subsequent clean runs passed 55/55 (unit test plus ad-hoc probe). Trust-gate cases launch subprocesses under a 1.5-second budget (unit test). The observed failure is an I/O-sensitive assertion under disk contention, not a code regression (unit test plus ad-hoc probe).

Bridge process `26743` started at 21:51:59 EDT on 2026-10-28, after the commit timestamp of 21:51:40 EDT, verifying deployment by timestamp (ad-hoc probe).

## Still open

Production activation evidence is zero: no `wake_tier` event with `tier="equipment"` has appeared in a session capture log (session capture log). All 55 passing equipment tests are harness-side (unit test). The tier has never fired at a real table; the first live gear question remains the actual test.

The kill-switch setting is absent, not off. `LIVE_WAKE_EQUIPMENT_ENABLED` does not appear in `.env`, and the launchd plist injects only `PATH`, so the code default of `true` makes the tier live-reachable (ad-hoc probe). No test asserts the running default.

## Corrections

The requester's session notes carried `LIVE_WAKE_EQUIPMENT_ENABLED=false`, but checking `.env` and the launchd plist showed the flag was absent, so the default `true` applies (ad-hoc probe). An absent flag is not a disabled flag, and a remembered config value is not a measured one.
