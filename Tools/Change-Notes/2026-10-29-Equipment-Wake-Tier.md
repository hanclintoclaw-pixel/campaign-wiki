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

The tier reached a real table the following evening. Three `wake_tier` events with `tier="equipment"`, all `accepted: true`, appear in capture `2026-10-29T20-40-28-shadowrun` at 20:45:22, 20:46:42, and 20:58:29 EDT, carrying 783, 549, and 608 injected characters in 0.503, 0.391, and 0.266 seconds (session capture log). The first was the intended use: an Ares Predator II stats question answered substantively at 372 reply characters in 4.951 seconds, naming heavy pistol, Damage 9M, SA only, 15-round clip, and Concealability 4 with a citation (session capture log).

The second and third show two defects. The vehicle question ("base body stat for a Ford Canada bison") accepted 3 rows but injected only 549 characters and the reply deflected on Body. The curated row does carry `Body/Armor` = `4/4`, but the injector selects columns through an exact-match whitelist of bare headings, and the vehicles dataset uses compound headings (`Body/Armor`, `Speed/Accel`, `Pilot/Sensor`, `Sig/Autonav`) which match nothing and are silently dropped; 3 vehicle stats survived against 7 gear stats for the pistol (ad-hoc probe). The third accepted a rules question -- "what attribute is launch weapons connected to" -- because "weapon" matches the noun list, returning gear rows with no skill link, and the model correctly refused to voice a number from them (session capture log).

## Still open

Four production wake turns now run through this tier and the harness never saw two of them. The column whitelist truncates every dataset whose headings are compound, which under-delivers precisely when the trust gate has done its job correctly -- the model was told the source lacked Body because the injector had already discarded it. The intent gate admits skill-link questions carrying an item noun, burning a turn on gear rows that cannot answer the question asked. Neither defect is covered by a unit test, because the 55 harness cases assert the tier's own fixtures rather than the real vehicles row shape (unit test).

Desired behaviour and acceptance criteria are written up in the bridge repo as `SUBSTANTIVE_ANSWERS_FROM_SOURCE.md`. The trust gate is not the problem and is not proposed for change.

The kill-switch setting is absent, not off. `LIVE_WAKE_EQUIPMENT_ENABLED` does not appear in `.env`, and the launchd plist injects only `PATH`, so the code default of `true` makes the tier live-reachable (ad-hoc probe). No test asserts the running default.

## Corrections

The claim that production activation evidence was zero is retracted. This note was written and published on the afternoon of 2026-10-29 against the last capture then on disk, and said the tier "has never fired at a real table." The same evening's session produced three accepted equipment-tier events, listed above (session capture log). The claim was true of the evidence available at writing time and wrong as a statement about the world; an absence of evidence gathered hours earlier is not a property of the system. Re-check live state before publishing it as a finding.

The claim that the intent gate separates equipment questions from rules rulings is too strong as written. Its decline cases were verified only against the three phrasings in the unit test (unit test). A fourth phrasing not in that test -- a skill-link question naming a weapon -- is admitted in production (session capture log).

The requester's session notes carried `LIVE_WAKE_EQUIPMENT_ENABLED=false`, but checking `.env` and the launchd plist showed the flag was absent, so the default `true` applies (ad-hoc probe). An absent flag is not a disabled flag, and a remembered config value is not a measured one.
