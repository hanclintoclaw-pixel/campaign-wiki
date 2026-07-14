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

## Needed words / phrases tally

This section is refreshed by the live voice bridge when it has to generate a fresh Cindy voice line instead of using a canned clip chain.

<!-- CINDY_NEEDED_WORDS_START -->
_Last refreshed: not yet; fresh generated lines counted: 0._

No fresh generated voice lines have been tallied yet.

<!-- CINDY_NEEDED_WORDS_END -->

## Folder + manifest workflow

The bridge now discovers clips from the library folder instead of requiring every filename to be hardcoded in `voice_chat.py`.

Local generated clip folder:

```text
/Volumes/carbonite/claw/data/cindylou/voice-clone-samples/youtube_T34mD_vHvdA/soundboard_library_20260714/
```

Manifest path:

```text
/Volumes/carbonite/claw/data/cindylou/voice-clone-samples/youtube_T34mD_vHvdA/soundboard_library_20260714/manifest.json
```

Drop-in behavior:

1. Add a new `.mp3`, `.wav`, `.ogg`, `.aiff`, or `.m4a` file to the clip folder.
2. Use a useful filename such as `35_positive_confirm.mp3`; the bridge strips the leading number and infers clip id `positive_confirm`.
3. Optional but preferred: add a matching `.txt` sidecar with the spoken phrase, for example `35_positive_confirm.txt`.
4. On startup or the next quick-clip selection pass, the bridge scans the folder, probes duration with `ffprobe`, infers phrase/tags from the filename or sidecar, and updates `manifest.json`.
5. To tune behavior, edit the manifest entry's `tags`, `priority`, or `enabled` value. No bridge code change is needed for ordinary new clips.

Manifest entry template:

```json
{
  "id": "positive_confirm",
  "filename": "35_positive_confirm.mp3",
  "phrase": "That's right, honey.",
  "tags": ["yes", "confirm", "flavor"],
  "priority": 100,
  "enabled": true,
  "duration_seconds": 1.35,
  "source": "folder-scan"
}
```

Tag guidance:

- `yes`, `no` - generic affirmative/negative clips.
- `safe`, `unsafe`, `safety_positive`, `safety_negative` - explicit safety answers.
- `matrix`, `host`, `ic`, `trace`, `deck` - Matrix-context clips.
- `ack`, `processing`, `warning`, `success`, `memory`, `gm_handoff`, `flavor` - common behavior buckets.
- Higher `priority` wins when multiple enabled clips match the same tag set.

## Current 34-clip library

Source voice test: Taylor-source XTTS-v2 reference from the 2026-07-12 cleared interview sample.

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
| 31 | `yes_thats_safe` | Yes, that's safe. | Explicit positive safety answer |
| 32 | `no_thats_not_safe` | No, that's not safe. | Explicit negative safety answer |
| 33 | `thats_right_honey` | That's right, honey. | Generic flavored yes / confirmation |
| 34 | `no_way_sugar` | No way, sugar. | Generic flavored no / rejection |

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
| Jack out / Black IC / dumpshock danger | `no_thats_not_safe` -> `hold_up` -> `jack_out_now` |
| Trace or security tally movement | `hold_up` -> `trace_is_moving` |
| IC / intrusion countermeasure danger | `hold_up` -> `ic_is_waking_up` |
| Roll / test / target-number prompt | `copy_that` -> `need_a_roll` |
| Remember / mark / note / save request | `marking_that` -> `saved_to_memory` |
| Unsafe host/decking question | best enabled `no` + `flavor` clip -> `lemme_check_grid` -> `eyes_on_the_host` |
| Safe/ready decking question | best enabled `yes` + `flavor` clip -> `that_tracks` |
| Matrix planning or host/security opening | `lemme_check_grid` -> `eyes_on_the_host` |
| Technical stall | `copy_that` -> `running_it_now` |
| Explicit Cindy relevance | `on_it_sugar` -> `running_it_now` |

If a chain is selected, the bridge skips rendering a fresh generated voice line and logs the selected chain in the GM ping. If the voice bridge is already connected, it plays the clips sequentially. It does **not** force-join voice just to play a quick chain.

The GM's native Discord soundboard can hold a smaller hand-picked subset. The larger local library is for voice-bridge/saved-clip playback and fast chained responses.
