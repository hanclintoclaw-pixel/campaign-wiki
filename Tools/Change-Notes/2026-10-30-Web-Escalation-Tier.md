---
title: "Web escalation when local retrieval shrugs"
type: change-note
visibility: player-safe
updated: 2026-10-30
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-30
---

# Web escalation when local retrieval shrugs

Third entry of 2026-10-30; see `2026-10-30-Wake-Retrieval-And-Narration.md` and `2026-10-30-Rules-Page-Retrieval.md` for the day's earlier work. Bridge code in `voice_chat.py`, commit `2226346`.

## Shipped

JackalMoreau asked for a flag that, when Cindy cannot confidently answer a table question, escalates to a smarter web search to get the right answer. Implemented as tier 3, enabled via `LIVE_WAKE_WEB_ESCALATION_ENABLED=true` in the bridge environment.

Model confidence is not the trigger. A model that does not know it failed is exactly the model that answers confidently from memory. The load-bearing signal is structural: the bridge observed the local ladder return no facts, which is something the bridge knows rather than something the model claims. Only then is a deflection phrase list consulted, exercised against 8 phrasings (unit test). A confident-but-wrong answer from a turn where facts were injected can never escalate, and injected local facts block escalation outright — the web does not outvote the corpus. A social veto runs before both, tested on 5 phrasings (unit test), because "what" alone looks factual and "what do you think of my jacket" must not buy a 13-second round trip.

Escalation runs a stronger model (Sol) than the wake turn (local Qwen) deliberately. A probe showed the local wake model can call `web_search` correctly and answered a range question right — pistol Short range 0–5 meters, p.111 (ad-hoc probe) — so plumbing was never the constraint. The judgment that needs the better reasoner is whether a web hit is genuinely SR3: the corpus is SR3-only while the web is dominated by 4e/5e/6e material.

Escalation runs in its own throwaway harness session. Session mode is pinned, so reusing the wake session id would append untrusted web prose to the night's append-only transcript and let it resurface in later turns.

Both wake paths (thread and voice) funnel through one helper, so a rule added for one cannot silently miss the other; an earlier project scar is exactly that bug — a lookup rule added only to the spoken path, which is gated off.

The filler-voice loop now stops when Cindy is about to speak, not when her first draft lands. Escalation can add ~20s (ad-hoc probe) after the first draft returns, and the old ordering would have left the table in silence through the search; every early-return path stays covered by the stop in `finally`.

The machinery-narration filter gained web vocabulary, including "the net" and "online" — what a model reaches for when forbidden to say "the web". In-world "the Matrix" is deliberately not matched. 5 leak phrasings stripped, 4 safe sentences including "drawbridge", "abridged" and "the Matrix node" untouched (unit test).

## Measured

`web_search` cost 12.99s and 19.38s per call (ad-hoc probe). The wake turn already runs at p95 ~54s (session capture log) under `OPENCLAW_BRIDGE_TIMEOUT_S=90` plus 15s grace (configuration). Escalation spends the remaining window rather than stacking a timeout: at least 35s remaining, at least 8s usable budget after a 5s reserve, and the ceiling minus budget still leaving a 12s emit margin (unit test). Three floors because there are three distinct failure paths; all degrade to today's honest deflection rather than losing the turn. Cap: 6 escalations per game night (unit test), reset with the session id. A failed escalation returns the original reply, never an error string (unit test).

End-to-end through the real CLI from a launchd-equivalent environment: a deflection was replaced with "The Ares Predator's damage code is 9M — Power 9, Moderate damage — in Shadowrun Third Edition, core rulebook, page 278" in 20.7s (ad-hoc probe), and the spoken rendering arrives asterisk-free (unit test).

The accuracy cross-check that justified shipping: escalation answered Ares Predator damage as 9M, p.278 (ad-hoc probe) citing an external SR3 reference with `toolSummary` 1 call / 0 failures (ad-hoc probe), while the corpus's own VERIFIED equipment row independently reports Damage 9M, Book.Page sr3.278 (ad-hoc probe) — checked against the PDF text layer rather than OCR. Two independent sources agreeing on number and page.

## Still open

Deflection matching is a phrase list, not a confidence estimate; paraphrases escape it. The trigger still cannot distinguish "not retrieved" from "not in source" — the distinction the plan doc called for and this narrows without fully solving. `rules-answer` declined the Ares Predator question while the deterministic equipment tier answered it from VERIFIED rows: page-level recall and the tables remain misaligned. There is no live-table evidence of escalation firing yet; everything here is probes and unit tests. `WEB_SEARCH_ESCALATION_PLAN.md` still carries the overturned claims and needs a revision pass.

## Corrections

`WEB_SEARCH_ESCALATION_PLAN.md` understated the blocker twice. (a) Absence was not merely instruction-shaped: `web_search` reported "disabled or no provider is available" for every model, including hosted-search-capable ones, despite `tools.web.search.enabled=true` and `openaiCodex.enabled=true`. (b) Tier 3 was not blocked on a paid key. Per `docs/tools/web.md`, key-free providers never win credential auto-detection and are used only when selected explicitly; `tools.web.search.provider: codex` restored availability with no key, no spend, and no gateway restart.

Two errors made while writing the suite, recorded so they are not repeated: an interception test patched `asyncio.subprocess.create_subprocess_exec` while the call site resolves `asyncio.create_subprocess_exec`, so the real binary ran and assertions passed vacuously on an empty captured command; and a hand-written test config had drifted from the real dataclass defaults, exposed loudly only when a field was added — the harness now seeds from the actual dataclass. One deflection test failure was a genuine regex defect (a required single space where the reply had one), not a test bug.
