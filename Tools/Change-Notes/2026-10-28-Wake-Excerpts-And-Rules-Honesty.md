---
title: "Voice bridge wake excerpts, rules honesty, and prompt-size solve"
type: change-note
visibility: player-safe
updated: 2026-10-28
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-28
---

# Voice bridge wake excerpts, rules honesty, and prompt-size solve

## Shipped

`0328f4d` replaces raw-head wake excerpts with a frontmatter-aware composer: Overview first, then heading and lead paragraph, then filtered metadata. It drops YAML source lists, deduplicates repeated lines, falls back on unfamiliar shapes, and tolerates empty or tiny inputs. Fetch allowance increased from 1,600 to 6,000 characters so the excerpt window reaches prose at all (unit test). Both tier-0 prefetch and later document lookup use it.

The motivation was a live wrong denial: the table was told a player character's metatype "isn't recorded on his wiki page" when it sat at line 64, outside the window the model was ever shown, because the head cut landed entirely inside about sixty lines of YAML frontmatter. An excerpt taken from a truncated page cannot establish the absence of anything.

The shared wake and primer rule now forbids speaking a rules number without reading a rules document that turn; otherwise it gives the mechanic in words and names the table to check. Edition discipline explicitly rejects the Stealth/Agility mix-up, which is later-edition vocabulary.

The collection fixture now derives configuration fields through dataclass introspection rather than a hand-copied list. `cd58a1f` supplies ephemeral wake sessions and an exact-prefix primer; tonight's deployed capture exercises both commits, with the bridge started after the commit landed (session capture log).

## Measured

All 10 wakes ran ephemeral and the primer succeeded at 12.6 seconds (session capture log). The first wake used 19,657 prompt tokens versus the old pinned session's 112,726, an 83 percent reduction; prefix-cache hits were 18,516 of 19,657, or 94 percent (ad-hoc probe).

Median generation was 5.2 seconds and 7 of 10 wakes finished within 9.3 seconds. The 33.4- and 21.5-second outliers were tool-heavy turns, not prefill stalls (session capture log).

The proposed keep-alive ping was dropped because shrinking the prompt solves what the ping was patching. Earlier probes found warm responses at 0.24 to 0.25 seconds through 30 idle minutes and zero cache hits beyond 60 minutes (ad-hoc probe); at roughly 20k tokens a cold prefill is no longer a table-visible stall. That does not prove future cold-prefill latency.

Lookup coverage grew from 54 to 65 cases, with 11 regressions added and 65 of 65 passing; collection-trigger tests also passed (unit test).

Initial grading of the same capture marked 4 of 8 content answers fully correct (session capture log). Wiki-grounded answers performed well; every miss was an uncited number recalled from memory. See corrections.

## Still open

Rules search remains disabled: OCR front matter is presented as confidently agreeing evidence, so re-chunking must precede enabling it.

PDF review is still needed for one malformed target number, two damage codes, firearms and melee table column bleed, truncated initiative lines, and 113 empty page bodies (ad-hoc probe).

`ocr_repair.py` removed 52 control characters and corrected 59 digit-anchored dice corruptions across 15 files (ad-hoc probe), with whole-file backups, a change log, and an index rebuild. Bare "DG" was preserved as legitimate prose.

Local compaction is pinned to the configured Qwen model in safeguard mode with thinking off. No successful compaction has been observed yet; configuration is not proof.

## Corrections

The cyberweapon verification made earlier tonight is retracted. The `(STR + 3)S` row belongs to Pole Arm in the melee table, and no "shock palm" entry was found in the corpus at all (ad-hoc probe). That answer was unverified, not verified.

The Ares Predator citation to page 275 is also retracted. The combat example sits at corpus marker 115 and the firearms table at marker 280; heavy pistol at damage code 9M remains confirmed (ad-hoc probe). The parenthesised figure in that table is the Ammo column, not Range.

The first excerpt verification used an already-corrected wiki page and therefore passed for the wrong reason. Before shipping, the earlier page revision was re-checked: its raw head omitted the metatype entirely (ad-hoc probe).
