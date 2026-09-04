---
title: Cindy Lou Live Session Monitoring Design
type: tech-note
visibility: player-safe
status: active
updated: 2026-09-04
tags: [cindy, discord, voice, monitoring, design]
---

# Cindy Lou Live Session Monitoring Design

## What this is

This tool lets Cindy Lou **listen to a live Shadowrun session through local voice transcription, keep a rough sense of what scene the table is in, and decide whether the GM should get a nudge**.

In plain English: it is a small live monitor that tries to notice, “is this currently a Cindy-relevant moment?” without spamming the table every time her name comes up.

It is **not** a full autonomous co-GM, and it is **not** meant to comment on every scene.

## What problem it solves

During live play, there are moments when Cindy really could help:

- a matrix/security angle opens up
- a physical surveillance or public-presence angle fits Cindy's available drones
- the crew is planning around technical surveillance or systems
- the table is stalled on a problem that fits Cindy’s lane
- someone directly invites Cindy’s input

The old approach was too reactive to the latest transcript snippet. That made it easy for brief jokes, table chatter, or stray Cindy mentions to look more important than they really were.

The current design is meant to be much calmer:

- remember the broader scene
- notice recent changes
- only interrupt when there is strong evidence that Cindy matters right now

## How it works

The monitor keeps two different views of the session:

### 1. Stable scene memory

A persistent **scene scratchpad** stores the best current guess about:

- what scene the party is in
- what the current plan is
- what open questions are still active
- what threats or matrix hooks are on the board

This is the “don’t lose the plot” layer.

### 2. Recent activity buffer

A short **recent delta** buffer tracks what has changed in the last minute or so.

This is the “what just happened?” layer.

### Why split them?

Because live sessions are noisy.

People joke, recap, drift, talk over each other, and occasionally go wildly off-topic for thirty seconds. If the system treated every new line as equally important, it would keep forgetting the real scene and replacing it with chatter.

So the monitor asks two separate questions:

1. **What is the scene still about?**
2. **What just changed enough to matter?**

That simple split is the core of the current design.

## What the monitor looks for

At a high level, the system scores each short transcript window for things like:

- matrix or system-facing language
- planning language
- open questions
- signs the table is technically stuck
- direct references to Cindy
- whether the conversation sounds in-game, mixed, or mostly table chatter

It then decides between three outcomes:

- **silent** — keep watching, say nothing
- **draft_ready** — this may matter soon, but do not interrupt yet
- **ping_now** — this looks like a genuinely useful moment to alert the GM

## What changed in the current version

The current monitor is much more conservative than the first live draft.

### Latency tuning pass: 2026-08-25

A live-response review after the 2026-08-24 session found that STT and warm Kokoro rendering were usually fast, while the largest delays came from OpenClaw response generation and cold session startup.

The active bridge now tightens that path by:

- limiting live wake thread context with `LIVE_WAKE_CONTEXT_LIMIT`;
- telling live wake prompts not to do tool/file/web lookups unless explicitly required;
- keeping automatic spoken playback gated and short while preserving the full text answer in Discord; the 2026-09-04 GM control panel now makes saved-line generation plus manual playback the preferred live-table path;
- running Discord voice join and Kokoro warmup in parallel during `!session-start`;
- adding `!voice-warm` / `!cindy-warm` for pre-session Kokoro, Whisper, and stalling-clip warmup;
- capturing explicit timeline events for OpenClaw call start/done/timeout and saved-voice render/playback stages;
- increasing the Kokoro worker idle window so a pre-warmed worker is less likely to shut down before play.

### It now explicitly separates conversation modes

The monitor classifies windows into buckets such as:

- `in_game`
- `mixed`
- `table_talk`
- `post_session_debrief`

That matters because a Cindy-worthy tactical beat and a post-session wrap-up should not be treated the same way.

### Cindy mentions alone are no longer enough

This is the biggest behavior change.

A line that merely mentions Cindy should **not** by itself create a GM ping.

The system now prefers stronger evidence such as:

- a direct ask for Cindy’s input
- a real matrix/system dependency
- a concrete planning or stall beat where Cindy would naturally matter

### Matrix detection is narrower and cleaner

The monitor used to be too willing to treat loose technical language as matrix relevance.

The current version tightened this by using more exact matching, especially around words like `drone`, `deck`, `host`, and related system terms, so random substring collisions do not create false positives.

### Post-session chatter is explicitly suppressed

The monitor now has a dedicated notion of **post-session debrief** so “wrapping up,” thank-yous, aftercare chatter, and casual review do not look like live tactical openings.

### Proactive pings are strictly throttled

Non-direct GM pings now obey `LIVE_MONITOR_MIN_PING_INTERVAL_S` even when the inferred reason text changes. This prevents a table-talk or tooling-heavy stretch from producing several speculative Cindy Initiative pings in a few minutes. Direct Cindy wake replies still use the direct response path instead of this proactive monitor throttle.

## What it tries hard **not** to do

The monitor is intentionally biased against over-speaking.

It tries to avoid pings caused by:

- Cindy being mentioned as a joke
- people talking about the tool itself
- setup/testing chatter
- debrief or end-of-session talk
- generic drone/system words without real Cindy relevance
- repeated nudges about the same scene

That bias is deliberate. In a live game, one unnecessary interruption is usually worse than one missed marginal opportunity.

## Cindy Lou initiative guidance

Cindy may occasionally send the GM a private suggestion when she notices a moment where her NPC abilities could add fun, texture, or tactical options without taking agency away from the players.

Core principle: **Cindy offers options, not solutions.** The GM decides whether to ignore the suggestion, hold it, rephrase it, offer it to the table, or let Cindy speak or act in-character.

### When a ping is appropriate

- A passive surveillance opportunity appears: a meet site, vehicle, door, rooftop, alley, crowd, or suspicious NPC could be quietly watched by **[Dolly Zoom](../../Vehicles/Dolly-Zoom.md)**.
- A Matrix/security angle is present: hosts, cameras, comms, access logs, public terminals, credsticks, dataterms, drone networks, or building systems may matter.
- Cindy's public avatar could be useful: **[Tip Jar](../../Vehicles/Tip-Jar.md)** could busk, distract, mingle, occupy attention, provide a plausible local presence, or make Cindy feel embodied in the scene.
- The table is circling a problem and Cindy has a natural angle that gives the players a new option rather than the answer.
- The scene would be more fun if Cindy had a tiny cameo, quip, offer, warning, or "I can try something" moment.
- A player directly invites Cindy's input or the crew's current plan obviously depends on something Cindy is built to notice.

### When not to ping

- The players are actively solving the problem and Cindy would just be showing off.
- The suggestion would replace a player's niche, especially decker, rigger, or social spotlight already being handled by someone at the table.
- The idea is merely optimal but not especially fun, flavorful, or necessary.
- The scene is emotional, dramatic, or character-focused and Cindy's intervention would flatten it into tactics.
- The same beat has already been suggested recently.
- The only trigger is hearing the word "drone," "camera," "Matrix," or "Cindy" without a concrete opportunity.

### Frequency target

Default expectation: **zero to one proactive Cindy suggestion per session is fine**.

More than one is okay if the table is clearly enjoying Cindy as an active NPC, the suggestions are varied, and each one gives the GM a real option. Multiple pings in a short span should be rare unless Cindy is central to the current scene.

### Ping shape

A good ping should be short, GM-private, and optional.

Examples:

- `Cindy option: Dolly Zoom could quietly watch the rear exit while they keep negotiating. Low spotlight, gives them warning if someone bolts.`
- `Cindy option: Tip Jar could busk outside the club as a harmless service-drone distraction, letting the crew approach under cover of a little street performance.`
- `Cindy option: she might suggest checking the dataterm/camera logs here before they leave. Not a solution, just an angle.`

### Priority order

1. Protect player agency.
2. Preserve spotlight balance.
3. Add fun or useful texture.
4. Use Cindy's established tools when they naturally fit.
5. Stay quiet when the scene is already working.

### Rating and tuning target

This policy aims for roughly **8/10 alignment** with the GM's desired table experience: Cindy as a living NPC with occasional initiative, not a co-GM or a spotlight thief. The remaining tuning should come from actual session experience: if the pings feel too frequent, too timid, too tactical, or not flavorful enough, adjust this section and the live monitor prompts accordingly.

## Current behavior in practice

As of 2026-05-15, the live-monitor architecture has been implemented in the Discord voice bridge runtime here:

- `/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py`

The runtime keeps local state files under:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/`

Important examples:

- `transcript.jsonl` — raw voice transcript events
- `recent-delta.json` — short-horizon noisy analysis
- `scene-scratchpad.json` — more stable scene memory
- `scene-state.json` — combined state output
- `checkpoint.json` — last processed position
- `pings.jsonl` — ping history / audit trail

## Validation summary

The monitor was replay-tested against the 2026-05-14 session transcript.

### First replay pass

- produced **14 would-be pings**
- correctly solved the simplest mention-only issue
- was still too noisy in technical / security-adjacent scenes

### Tuned replay pass

After tightening the main heuristics, the same replay produced:

- **4 would-be pings**

That was a big improvement and much closer to a usable live posture.

### Second tightening pass

A stricter experimental pass was also tested afterward. It cleaned up remaining false-positive patterns, but it may have over-corrected and has **not** been promoted live yet.

So the practical status is:

- **live runtime:** conservative tuned version
- **stricter candidate:** staged and tested, but not yet adopted as the default live behavior

## What this means for a casual reader

If you are not deep in the code, the simplest description is:

> Cindy now has a live “pay attention / stay quiet / maybe nudge the GM” layer that watches the session, remembers the current scene better than before, and is much less likely to interrupt just because someone said her name.

That is the real milestone here.

## Known limits

This is still a heuristic system, not true scene understanding.

It can still miss things when:

- the table implies a technical beat without saying it clearly
- the speech-to-text output is messy
- the best Cindy moment depends on subtle social timing rather than obvious keywords

And it can still overreach if:

- too many weak signals stack up in the same noisy window
- the scene blends rigging, matrix, and ordinary logistics in ambiguous ways

So the tool is useful, but still deliberately cautious.

## Design philosophy

The live monitor is built around one social rule:

**Cindy should feel like a smart player at the table, not an alarm system.**

That means:

- speak rarely
- speak when it matters
- do not confuse being present with being helpful

## Related artifacts

Replay artifacts from the 2026-05-15 validation work live under:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/replays/`

Key files include:

- `session-state-replay-2026-05-14-session-window.json`
- `session-state-replay-2026-05-14-session-window-v2.json`
- `session-state-replay-2026-05-14-session-window-v3.json`

## Related pages

- Discord voice bridge runtime
- [Cindy Lou External Transcription Watchdog Plan](External-Transcription-Watchdog-Plan.md)
- [Cindy Lou Session Scratchpad Implementation Plan](Session-Scratchpad-Implementation-Plan.md)
- [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md)
