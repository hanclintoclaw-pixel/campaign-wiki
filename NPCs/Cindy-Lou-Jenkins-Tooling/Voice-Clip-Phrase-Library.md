---
title: Cindy Lou Voice Clip Phrase Library
type: npc-tooling
visibility: player-safe
status: active
updated: 2026-07-14
parent_page: README.md
tags: [cindy, voice, clips, discord, npc-tools]
---

# Cindy Lou Voice Clip Phrase Library

This page tracks Cindy Lou's short reusable voice clips for peppy live-table responses. These clips are meant to be fast, modular, and easy for the GM or voice bridge to chain together when a full generated line would be too slow.

## Behavior goal

Use short clips as **table feedback**, not as a replacement for real answers.

Good uses:

- acknowledge a direct request;
- signal that Cindy is checking something;
- warn that a Matrix situation is getting risky;
- confirm that a small action landed;
- add a quick in-character beat while longer text/rules work happens elsewhere.

Avoid using clip chains for:

- rules explanations;
- detailed NPC dialogue;
- canon decisions;
- anything that needs fresh context or careful wording.

## Chaining rules

- Prefer **1-3 clips** per response.
- Keep most chains under about **5 seconds total**.
- Do not spam repeated clips in the same scene.
- Use a clip chain only when it is faster and clearer than generating a fresh line.
- For dangerous Matrix moments, favor clear warnings over cute flavor.

Example patterns:

- **Acknowledge + working:** acknowledgment clip, then checking/running clip.
- **Matrix warning:** attention clip, then host/IC/trace warning.
- **Small success:** confirmation clip, then victory/clean-access clip.
- **Memory/admin:** acknowledgment clip, then saved/marked clip.

## Current 30-clip library

Source voice test: Taylor-source XTTS-v2 reference from the 2026-07-12 cleared interview sample.

Local generated clip folder:

```text
/Volumes/carbonite/claw/data/cindylou/voice-clone-samples/youtube_T34mD_vHvdA/soundboard_library_20260714/
```

| # | Clip id | Phrase | Primary use |
| --- | --- | --- | --- |
| 01 | `on_it_sugar` | On it, sugar. | Friendly acknowledgement |
| 02 | `lemme_check_grid` | Lemme check the grid. | Matrix lookup / processing |
| 03 | `that_tracks` | That tracks. | Agreement / confirmation |
| 04 | `hold_up` | Hold up. | Attention / pause |
| 05 | `i_smell_trouble` | I smell trouble. | Warning / suspicion |
| 06 | `were_golden` | We're golden. | Success / reassurance |
| 07 | `host_is_twitchy` | That host is twitchy. | Matrix risk warning |
| 08 | `jack_out_now` | Jack out, now. | Urgent danger warning |
| 09 | `copy_that` | Copy that. | Neutral acknowledgement |
| 10 | `give_me_one_sec` | Give me one sec. | Stall / processing |
| 11 | `running_it_now` | Running it now. | Active tool/process cue |
| 12 | `eyes_on_the_host` | Eyes on the host. | Matrix focus cue |
| 13 | `no_promises` | No promises. | Cautious acceptance |
| 14 | `found_a_thread` | I found a thread. | Discovery / lead found |
| 15 | `smells_corporate` | That smells corporate. | Suspicion / corp angle |
| 16 | `bad_vibes_honey` | Bad vibes, honey. | General warning |
| 17 | `keep_it_quiet` | Keep it quiet. | Stealth cue |
| 18 | `stay_frosty` | Stay frosty. | Alertness cue |
| 19 | `im_in` | I'm in. | Access gained |
| 20 | `access_looks_clean` | Access looks clean. | Safe access cue |
| 21 | `ic_is_waking_up` | IC is waking up. | Host danger cue |
| 22 | `trace_is_moving` | Trace is moving. | Trace warning |
| 23 | `need_a_roll` | Need a roll. | GM/player roll prompt |
| 24 | `ask_the_gm` | Ask the GM. | Authority handoff |
| 25 | `marking_that` | Marking that. | Note-taking cue |
| 26 | `saved_to_memory` | Saved to memory. | Memory/admin confirmation |
| 27 | `bring_me_online` | Bring me online. | Invite Cindy into scene |
| 28 | `cut_the_noise` | Cut the noise. | Focus / reduce chatter |
| 29 | `little_victory` | Little victory. | Minor success |
| 30 | `try_it_now` | Try it now. | Action-ready cue |

## Expected trigger behavior

When Cindy is active in voice, a trigger can map to one clip or a short chain. The useful default is:

1. classify the trigger as acknowledgement, Matrix work, warning, success, memory/admin, or GM handoff;
2. choose one primary clip from that category;
3. optionally add one follow-up clip if it clarifies the state;
4. skip clip playback if the same phrase was used recently or a fresh text/voice answer is required.

## Live-monitor quick-chain behavior

The live monitor now checks the phrase library before spending time on a freshly generated Cindy voice line. When the monitor decides a GM ping is warranted and Cindy would otherwise draft a voice response, it tries to select a canned chain first.

Current default mappings:

| Trigger shape | Clip chain |
| --- | --- |
| Jack out / Black IC / dumpshock danger | `hold_up` -> `jack_out_now` |
| Trace or security tally movement | `hold_up` -> `trace_is_moving` |
| IC / intrusion countermeasure danger | `hold_up` -> `ic_is_waking_up` |
| Roll / test / target-number prompt | `copy_that` -> `need_a_roll` |
| Remember / mark / note / save request | `marking_that` -> `saved_to_memory` |
| Matrix planning or host/security opening | `lemme_check_grid` -> `eyes_on_the_host` |
| Technical stall | `copy_that` -> `running_it_now` |
| Explicit Cindy relevance | `on_it_sugar` -> `running_it_now` |

If a chain is selected, the bridge skips rendering a fresh generated voice line and logs the selected chain in the GM ping. If the voice bridge is already connected, it plays the clips sequentially. It does **not** force-join voice just to play a quick chain.

The GM's native Discord soundboard can hold a smaller hand-picked subset. The larger local library is for voice-bridge/saved-clip playback and fast chained responses.
