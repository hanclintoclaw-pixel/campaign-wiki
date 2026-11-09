---
title: Cindy's In-Character Stats
type: reference
visibility: player-safe
status: active
last_updated_session: 2026-11-09
parent_page: ../Cindy-Lou-Jenkins.md
canon_status: mixed
confidence: medium
aliases:
  - Cindy In-Character Stats
  - Cindy Knowbot Stats
tags: [cindy, knowbot, matrix, stats, reference, gm-reference]
generated_by: dgx-spark/local-inference-lab/Qwen3.8-Flash-Next-NVFP4
generated_at: 2026-11-09
sources:
  - ../Cindy-Lou-Jenkins.md
  - GM-Control-Panel.md
  - Discord-Voice-Bridge-Commands.md
  - ../../Vehicles/Tip-Jar.md
  - ../../Vehicles/Dolly-Zoom.md
  - GM ruling, Cindy GM Interaction Thread, 2026-11-09 (frame core, persona points, Pilot, Hacking Pool, payload, damage/reboot, Willpower, trace/datatrail, commlink/matrixlink, ECCM, no SOTA, strict-SK Payload / Utility Pool ruling (Option B))
  - GM ruling, Cindy GM Interaction Thread, 2026-11-09 (derived mental attributes = ceil(frame core / 2), Willpower raised 3 to 5, skill package copied from the core rulebook Combat Decker sample character, printed p. 67)
---

# Cindy's In-Character Stats

Mechanical numbers only. This page is the consolidated stat view for Cindy Lou Jenkins as a table-playable **Semi-Autonomous Knowbot A-NPC**: Matrix stats, Computer skill, utility ratings, drone presets, and mobile-shell figures.

For personality, history, and the full hardware build, see [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md).

## How to read these numbers

Three tiers of authority, strongest first:

| Tier | What it covers | Confidence |
|---|---|---|
| **Recovered profile** | The Matrix stats that surfaced with Cindy's older Swiftwing-era knowbot record | Canon, partial |
| **Table-use assumptions** | Decking skill and utility ratings adopted for play because the recovered profile omits them | Provisional, GM-approved in practice |
| **Roll presets** | The values the GM panel and `!cindy-roll` actually use at the table | Active defaults |

If a number here ever disagrees with [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md) or the defaults in [Cindy Lou GM Control Panel](GM-Control-Panel.md), those two win, and this page should be corrected.

**This is not a full SR3 character sheet.** It is a stat reference for an A-NPC who mostly advises, observes, and decks.

## Semi-Autonomous Knowbot Matrix profile

**Frame core 9** is the anchor rating. GM-set 2026-11-09. Semi-Autonomous Knowbots are designed on the frame/agent template, but SKs get **their own point formulas** in the *Matrix* "Designing SKs" section, printed pp. 147-148: Persona Points are **MPCP x 3** and Frame Points are **MPCP x 8**, not the agent values of core x 2 and core x 6. Every point figure on this page uses the SK formulas.

> **Correction, 2026-11-09:** the first pass at this sheet scored her against the *agent* table (18 Persona Points, 54 Frame Points). Both were too low, and the shortfall caused real damage downstream - two attributes were cut to fit a budget she never had. The agent figures are gone; see *Budget, correctly computed* below.

| Stat | Value | Basis |
|---|---|---|
| **Frame core** | **9** | GM-set 2026-11-09 (see *Choosing core 9* below) |
| MPCP | 9 | derived - core rating is used in place of MPCP |
| Icon rating | 9 | derived - agent icon rating equals frame core (*Matrix* p. 89); this is the target number for Scan Icon / notice tests |
| Matrix Reaction | 6 | **GM-tuned** - rules-clean value is 9 (= core); kept at 6 for the throttle precedent |
| Matrix Initiative Dice | 2 | derived 1D6 base (SK Reaction and Initiative, *Matrix* p. 148) + 1 die purchased for 3 Frame Points |
| **Pilot** | **5** | derived - Pilot is a frame's built-in Computer skill; replaces the old table-use "Computer skill 5" |
| Hacking Pool | 5 | **GM-tuned** - rules-clean value is 9 (= core); capped at the base dice in her Pilot-5 pools |
| Bod | 5 | recovered profile, unchanged |
| Evasion | 5 | recovered profile, **restored** 2026-11-09 - the cut to 3 was forced by a Persona Point figure that was wrong |
| Masking | 6 | recovered profile, unchanged; protected as her signature |
| Sensor | 5 | recovered profile, **restored** 2026-11-09 - the cut to 4 was forced by the same wrong figure |
| Hardening | 4 | recovered profile, unchanged |
| Active Memory | 700 | recovered profile, unchanged |
| Storage Memory | 1400 | recovered profile, unchanged |
| I/O Speed | 300 | recovered profile, unchanged - still deck-scale for a large server, unresolved |
| Response Increase | 1 | recovered profile, unchanged |
| **Willpower** | **5** | **GM ruling 2026-11-09** - derived ceil(frame core / 2); raised from the 3 ruled earlier the same day. See *Mental attributes* below |
| **Intelligence** | **5** | **GM ruling 2026-11-09** - derived ceil(core / 2); the attribute Computer, every Technical skill and every Knowledge skill links to |
| **Charisma** | **5** | **GM ruling 2026-11-09** - derived ceil(core / 2); the attribute Etiquette and the other Social skills link to |
| **Utility Pool** | **8** | Pool-point allocation (*Matrix* p. 148), bought at 2 Frame Points per point, capped at MPCP 9 |

Persona Points are MPCP x 3 for an SK = **27 available**, with Bod 5 / Evasion 5 / Masking 6 / Sensor 5 assigning **21** and **6 left unspent**. No attribute exceeds the core rating, so Masking 6 is legal. The 6 spare points are an open decision - see *Still open*.

### Choosing core 9

The recovered profile carried three numbers that each implied a different core: MPCP 7 (the SK rules say MPCP is determined by the frame core), Matrix Reaction 6 (frames have Reaction equal to core), and Hacking Pool 4. HP 4 is the weakest of the three and is arithmetic damage from scoring her as a *user on a deck* - the decker formula (Intelligence 5 + MPCP 7) / 3 rounds to 4. The printed agent rule is HP = core.

Core 9 was chosen because it is the lowest rating that keeps the published sheet legal and intact:

- Persona Points 27 (MPCP x 3) covers her original recovered attributes at 21 of 27 - no cuts were ever required.
- Frame Points 72 (MPCP x 8) covers Pilot 5 (10), the extra Initiative die (3), 42 ratings of utility payload, and a Utility Pool of 8 (16).
- No utility rating exceeds the core-9 cap on loaded utilities.
- MPCP 9 stays clear of the true-AI gradient the 2026-11-06 hosting ruling blocked (AIs run MPCP 12+). SK frame cores may go as high as 14, so 9 is not near the ceiling either.

*Matrix* p. 147 states the SK statistics are **guidelines for GM use** when creating an SK, deliberately omitting programming statistics - so the derated Reaction and Hacking Pool are the intended use of the rule, not a violation of it. Both are labelled above rather than presented as derivations.


## Mental attributes (GM ruling, 2026-11-09)

**Ruling: Cindy's relevant attributes are derived from half her frame core rating, rounded up.** Core 9 gives **ceil(9 / 2) = 5**, which supplies the mental attributes a frame normally does not have and raises **Willpower from 3 to 5**.

*Matrix* pp. 88-90 give frames and SKs no mental attributes - Persona Points buy only Bod, Evasion, Masking and Sensor. That absence is precisely why Pilot exists as a built-in Computer skill. This ruling fills the gap, and it is what makes the *Skills* section below legal rather than hand-waving.

| Attribute | Value | What it unlocks |
|---|---|---|
| **Intelligence** | **5** | Links Computer, all Technical skills, all Knowledge skills (core p. 89). Previously nonexistent for a frame |
| **Charisma** | **5** | Links Etiquette and the Social skills - the busking persona finally has an attribute behind it |
| **Willpower** | **5** | Resists mind-affecting gray/black IC, Pavlov data bombs, psychotropic effects, control manipulations |
| Matrix Reaction | 6 | **unchanged, GM-tuned.** A standing ruling outranks the derivation, which would have produced 5 |
| Bod | 5 | **unchanged.** Point-budgeted Persona value; it already equals ceil(core / 2), so the two agree |

Consequences the GM should have in view:

- **Control manipulations now have a published threshold.** They are resisted with Willpower and have a Threshold equal to half the target's Willpower, rounded down (core p. 197). At Willpower 5 that is **2 net successes** to land on her against a 5-dice pool; at the previous Willpower 3 it was 1 success against 3 dice. She is meaningfully harder to Confuse or Complicate.
- **Physical attributes are deliberately not derived.** Her body-equivalent is the point-budgeted Bod from the Persona table; Strength and Agility belong to the trailer server, which has no stat block. Deriving them would double-count the 27 Persona Points.
- **These sit outside the Persona Point budget.** They come from the GM ruling, not from the 27 points, so the Bod 5 / Evasion 5 / Masking 6 / Sensor 5 = 21-of-27 accounting above is unchanged.
- **Pure DNI now has something to grab.** *Matrix* p. 25: a user running by pure DNI uses Intelligence as Matrix Reaction. Her Int 5 lands within one of the GM-tuned Reaction 6, so the throttle survives even if that rule is applied to her.

### Dice-pool consequence - read before using the skill list

Every SR3 skill test is attribute + skill, so granting mental attributes silently raises every pool she rolls. This points **up**. Rows below assume Hacking Pool 5 is fully spendable (pool dice may not exceed the base dice in use):

| Test | Before this ruling | After |
|---|---|---|
| Computer (any specialization) | Pilot 5 + Pool 5 = **10** | Int 5 + Computer 6 + Pool 5 = **16** |
| Computer (B/R) | Pilot 5 + Pool 5 = **10** | Int 5 + B/R 4 + Pool 5 = **14** |
| Etiquette (Matrix) | not rollable, no Charisma | **Charisma 5 + spec 3 = 8**, and **no** Hacking Pool permitted |
| Willpower resistance | 3 dice | **5 dice** |
| Knowledge searches | not rollable, no Intelligence | **Int 5 + rating 4-5**, plus Pool |

A 16-dice Matrix test with exploding sixes is not "competent, not elite" - it is the best decker pool the table will see. **That is a real escalation, and it is the GM's to keep or throttle.** Three clean levers, strongest first:

1. **Cap Matrix skill tests at Pilot 5**, letting the derived attributes govern only social and Knowledge tests. Keeps the throttle precedent; costs her the Computer 6.
2. **Bring Computer down to Pilot 5** so skill and built-in agree, restoring the 10-dice ceiling. Loses the copied 6.
3. **Accept it** - defensible for a being whose entire existence is that one thing.

Nothing was throttled unilaterally. As published, the page runs option 3.

## Decking runtime

Cindy personally runs Matrix crawls from these values.

| Stat | Value |
|---|---|
| **Pilot (built-in Computer skill)** | **5** |
| **Computer (trained skill)** | **6** - above Pilot; Intelligence-linked since the derived-attribute ruling |
| Effective Detection Factor | 6 |
| Hacking Pool per focused test | 5, capped at the base dice in the pool |

Rules intent: competent, not elite. She handles modest hosts reliably; hard hidden hosts and high-threshold rewards can still lock her out. The reduced Reaction and Hacking Pool above exist to protect that intent against the core-9 derivations.

Pilot also sets a floor on her origin: a frame's Pilot may not exceed its programmer's Computer (Programming) skill, so whoever built her had at least Programming 5.

### Budget, correctly computed

Frame Points are MPCP x 8 for an SK = **72**. Allocated:

| Allocation | Cost | Running |
|---|---|---|
| Pilot 5 (2 points per rating) | 10 | 62 left |
| Extra Initiative die (3 points per die) | 3 | 59 left |
| **Utility Pool 8** (2 Frame Points per Pool point, cap MPCP 9) | 16 | 43 left |
| **Utility Payload** - Restore 4 + Shield 2 only (1 point per rating carried) | 6 | **37 left** |

Frame Points may be allocated to exactly four things - **Pilot rating, Initiative, Utility Payload, and Utility Pool** (*Matrix* p. 148). There is no fifth purchase, so the **37 unspent points buy nothing and are not a reserve**; skills are not a Frame Point purchase at all. The only ways to spend them are raising the Pool toward its MPCP cap of 9 (16 points) or buying Initiative dice up to the printed 5D6 limit. Both are left open below rather than taken quietly.

Re-arming her is a Programming Test at (average utility rating)^2 x 2 days.

> **Correction, 2026-11-09:** an earlier version of this page computed 54 Frame Points using the *agent* formula and declared her budget fully spent at 41 ratings. That forced the cut of Attack and Armor and the trim of Sleaze 5 to 4, which in turn silently dropped her Detection Factor from 6 to 5. With the SK formula there was never a squeeze.


## Skills (GM-approved package, 2026-11-09)

**GM decision: copy the core rulebook's Combat Decker sample character.** Adopted from *Shadowrun, Third Edition*, Sample Characters, **printed p. 67**.

Two corrections to my own shortlist, recorded rather than quietly fixed. I earlier attributed that block to *Matrix* - wrong; the decker-adjacent block at *Matrix* printed p. 128 is the **Security Sysop**, a different character. And I listed "Electronics 4", which is the Sysop's line - the Combat Decker's actual Electronics entry is **B/R only**. Both corrected below.

**Active skills:**

| Skill | Rating | Linked attribute | Notes |
|---|---|---|---|
| **Computer** | **6** | Intelligence 5 | Her real Matrix skill, above Pilot 5. Pilot stays as the built-in floor the book guarantees a frame, not a ceiling |
| **Computer (B/R)** | **4** | Intelligence 5 | Build/roll - programming and rebuilding code, which is how she re-arms her own utilities |
| **Electronics (B/R)** | **4** | Intelligence 5 | **The source block has no plain Electronics**, so general electronics work is defaulting at +4 target number - see gaps below |
| **Etiquette (Matrix)** | **1 (3)** | Charisma 5 | Base 1, Matrix specialization 3, so Matrix social tests roll at 3. **Hacking Pool dice may not be added to Etiquette (Matrix) tests** (*Matrix* p. 26), which is why the derived Charisma matters |

**Knowledge skills:** Data Havens **5**, Jackpoint Locations **4**, Matrix Gangs **4**, Seattle Corporate Hosts **4**, English (Decker Lingo) **3 (5)** with Read/Write 2, plus Read/Write 1 on Japanese. Knowledge skills are Intelligence-linked, so the derived 5 is what makes any of them rollable.

**Dropped from the copy, with reasons** - the GM can reinstate any of them:

- **Bike 4, Pistols 5, Stealth 4, Unarmed Combat 4, Cyber-Implant Combat (Spur) 4 (6)** - body skills. She has no body; the trailer server does, and it has no stat block. Cyber-Implant Combat also presumes chrome she does not have.
- **Japanese 3, Seedy Ork Bars 4, 20th Century Comic Books 4** - flavour tied to an ork in Seattle. Her Nashville career is the better source for equivalents; the GM can name replacements.
- **Datajacks, cyberlimb, wired reflexes, headware** from the source block - ignored as hardware, consistent with the 2026-11-06 hosting ruling.

### Two gaps the copy leaves open

- **No general Electronics skill.** Electronics (B/R) covers building and repairing, not live electronics tasks. Anything the book calls a straight Electronics test - laser-link alignment, for instance (*Matrix* p. 35, Electronics (Linking Between Devices) (4) test) - is a **defaulting** test for her at +4 target number. Practical effect: drone and hardware-side electronics work is weak on purpose. Say the word for **Electronics 3-4** and it goes in.
- **No Search Operations specialization**, the one my shortlist recommended and the specialization her three most-used utilities test with. The source block carries no Computer specialization beyond B/R, so copying it faithfully left this out. One line to add if wanted.

### Are skills budgeted? No - and that is a book fact, not a shortcut

**Skills cost Frame Points nothing.** Frame Points may be allocated to exactly four things - Pilot rating, Initiative, Utility Payload, Utility Pool (*Matrix* p. 148) - and skills are not on that list, so the Combat Decker's ratings were never a purchase against her 37 unspent points.

What actually limits a skill grant is the **linked-attribute requirement**, and until today that limit was absolute: with no Intelligence she could not hold a Computer skill at all. The derived-attribute ruling above satisfies it, so the remaining gate is GM judgement, not arithmetic.

Pilot interacts with this in one specific way worth keeping: a frame's Pilot **may not exceed its programmer's Computer (Programming) skill** (*Matrix* p. 90). Pilot 5 therefore still implies whoever built her had at least Programming 5, and her own Computer 6 does not change that floor.

### Payload and Utility Pool (strict SK - GM ruling 2026-11-09)

**The GM ruled Option B: strict SK.** Her Utility Payload carries **only the Defensive utilities**. Everything operational is allocated from the Utility Pool when needed, as the book intends.

*Matrix* p. 148: **"the SK's Utility Payload is for non-operational utilities only (i.e., defensive, offensive and special utilities)"**, and **"SKs are not programmed to carry operational utilities because they possess the capability to perform any operational utility their situation calls for."** Chapter 7's own category list backs the split - Defensive Utilities are **Restore** and **Shield**; the rest of her toolkit is Operational and therefore may not be carried.

**Carried in the Payload (standing code, always available):**

| Utility | Rating | Category | Notes |
|---|---|---|---|
| Restore | 4 | Defensive | Complex Action, repairs 1 box per 2 successes |
| Shield | 2 | Defensive | two parries ever, then needs a Swap Memory reload |

Payload cost 6 Frame Points. Nothing else is standing code inside her frame.

**Allocated from the Utility Pool of 8 (Free Action, used once, then gone):**

| Utility | Typical rating | Test it is used with |
|---|---|---|
| Analyze | 5 | Computer (Search Operations) - locate files, assess an icon |
| Browse | 5 | Computer (Search Operations) - read files, search |
| Deception | 5 | Computer (Decking) - Logon to Host, fake an icon |
| Sleaze | 5 | Computer - carries her Detection Factor |
| Scanner | 4 | Computer (Search Operations) - Matrix perception |
| Read/Write | 4 | Computer - file access |
| Spoof | 4 | Computer (Decking) - slave and command spoofing |
| Validate | 4 | Computer - accounts, passcodes, credentials |

Those ratings are **what she usually buys with Pool points**, not cargo she carries. Any operational utility up to rating 9 (her MPCP) is available in principle; the Pool total, not a loadout, is what limits her.

### What Option B actually costs her

Ruling for the strict reading is not free. Two of its edges cut directly against a knowbot whose whole job is being quietly useful.

- **Her Detection Factor is no longer standing.** DF is computed from *running* code: (Masking 6 + Sleaze) / 2, rounded up. Sleaze now has to be paid for out of the Pool. With Sleaze 5 allocated, **DF 6**. With nothing allocated, **DF 3** - she is conspicuous by default, which is a real change for a support NPC the GM relies on not to get spotted.
- **The Pool refreshes on Combat Turns.** *Matrix* p. 148: an allocated utility "must be used immediately", re-using it costs fresh points, and the **Pool refreshes at the beginning of each Combat Turn**. In combat she can re-buy Sleaze 5 every turn. Outside combat there are no Combat Turns, so whether she can hold a utility up at all is the GM's call. This is now the most important unresolved question on the page.
- **Two operations in one Combat Turn compete for the same 8 points.** Analyze 5 and Sleaze 5 together cost 10 and cannot both run in a single turn on a Pool of 8. Under the old standing loadout they could. Expect her to have to choose between looking hard and staying hidden.
- **Burst ceiling rises above any standing rating she used to carry.** A single Pool 8 allocation beats every standing 5, and raising the Pool to its cap would reach rating 9. This is the one axis where B is simply stronger.
- **Utility-crash protection got thinner.** Only Restore and Shield are resident, so a hog utility that crashes her code also takes away her ability to *notice* it coming, since Scanner and Analyze are Pool allocations too.

<details markdown="1">
<summary>Legacy: Option A - the superseded standing loadout (click to expand)</summary>

Option A carried a standing operational loadout alongside a paid Utility Pool. It was documented here while the legality question was open, and the GM ruled against it on 2026-11-09. It remains recoverable in git history (`git log -p` on this file) if the table ever wants to go back.

</details>


### Communications - external device (GM ruling, 2026-11-09)

Cindy has **no Commlink or Matrixlink code in her frame**. Both come to her as a **rating 4 bonus from an external device**.

| Utility | Rating | Source | Cost to her |
|---|---|---|---|
| Commlink | 4 | external device | **no Frame Points, no Utility Payload** - it is bolt-on hardware, not code inside her frame |
| Matrixlink | 4 | external device | same |

Mechanical consequences the GM should hold onto:

- **It is a single point of failure.** It is not a program she can rebuild from a backup. If the device is confiscated, broken, EMP'd, or left in the trailer, she has no comms and no Matrixlink until someone hands her another one.
- **It is physical, so it is findable.** Hardware can be tagged, traced, and recovered by whoever owns it.
- Book context: **Commlink** is an Operational utility (core rulebook, Multiplier 1 - Make Comcall, Tap Comcall), so strictly its bonus would come from the Pool; **Matrixlink** in *Matrix* is the **BattleTac Matrixlink**, a *Special* utility (Multiplier 5) that ties users into a shared network via Make Comcall. Because both live on the device rather than in her frame, that Payload-vs-Pool question is moot here.

### Jamming and ECCM (GM ruling, 2026-11-09)

**Cindy has no ECCM. None.** This is deliberate and is flagged as future work for Mevin, not an oversight to patch quietly.

- ECM jams remote-control networks and sensor frequencies and degrades transmission quality; ECCM counteracts it (core rulebook, Electronic Countermeasures, p. 138). It is vehicle/drone-side gear.
- So **any jammer works on her unopposed**: her drone control links to Tip Jar and Dolly Zoom, her sensor tests, and her connectivity to the trailer are all exposed with no counter and no reduced-Jamming Power.
- Dolly Zoom is already the worst case at Sensor 0 / Pilot 1.
- If the crew later wants a fix, ECCM is something **Mevin buys**, which makes drone-link jamming resistance a spendable resource rather than a default. Until then, "the signal is fragile" is the intended answer.

### Restore and Shield behaviour

Both are finite resources, and the GM should track them as such.

- **Shield 2** gives her **two parries ever**. A Shield Test is made against the attacker's skill (Computer skill for a decker, Security Value for IC); successes reduce the attacker's net successes. The utility loses 1 rating point every use, hit or miss, and only a fresh copy restored by a Swap Memory operation brings it back. "Cindy is out of shields" is a spendable dramatic beat.
- **Restore 4** is a Complex Action, Restore Test against the target number of the program that caused the damage (use the higher rating if several hit her), repairing 1 point of damage per 2 successes. It repairs attribute and icon damage but **cannot repair permanent damage from gray or black IC**.

## Damage, resistance, and reboot

SR3 does not derive an icon's damage track from its Bod. Per the core rulebook's Icon Damage and Condition Monitor rules (OCR p. 226, printed footer candidate 226), icons use the **standard 10-box Condition Monitor with a single physical track** - no Stun. What Bod does is set the resistance pool.

| Situation | Test |
|---|---|
| Hit by a damage-inflicting attack or killer IC | **Bod (5) test** against a target number equal to the attack's Power (Power = attacker rating); attacker's net successes stage the Damage Level up, defender's stage it down |
| Utility-crash attack (for example a hog utility) | **MPCP (9) test** against (attacker rating - Hardening 4), per the worked example at *Matrix* OCR p. 92; net successes crash her highest utilities |
| Mind-affecting gray/black IC, Pavlov data bomb, psychotropic effects | **Willpower (5) test** - derived, see *Mental attributes* |
| Icon Condition Monitor filled (all 10 boxes) | **Icon crashes** - see reboot |

Damage levels from IC follow the host's Security Code (Blue/Green hosts Moderate, Orange/Red hosts Serious), so where the fight happens changes how hard it hits.

Note the earlier one-line summary, "resists with MPCP 9 against (attacker rating - Hardening 4)", is only the **utility-crash** path. Damage-inflicting attacks resist with Bod. Both rows above apply; there is no single resistance roll.

### Reboot from the trailer (GM ruling, 2026-11-09)

Cindy cannot be permanently killed by Matrix damage. When her icon crashes - all 10 Condition Monitor boxes filled, or destroyed by black IC - she is **rebuilt at the trailer from her last memory backup**.

- She **loses time, not life**: the gap between the crash and her last good backup is gone, and that gap is the cost.
- The GM picks the backup cadence scene to scene, which makes the interval a story lever rather than a fixed stat. A GM who wants real stakes can make the last backup recent-but-before-the-disaster she failed to warn anyone about.
- Because the icon *is* her and there is no decker behind it, the usual "decker is dumped" result of a crashed icon has nothing to dump. She does not take dump shock; the crash is the whole event.
- Matrix damage to her attributes persists across a reboot only if the backup predates the damage. Restore 4 repairs damage before that point; it cannot touch permanent gray/black IC damage, which is the one path that survives a reboot.

### Mind-affecting effects (GM ruling, 2026-11-09)

**Willpower 5, derived.** SR3 gives programs no Willpower, and the books route mind-affecting resistance, simsense-overload-style tests, and Pavlov/psychotropic effects through the *person* behind the icon. Cindy has no such person, so the GM supplied one: first a Will of 3 tied to the length of her memory and her development as a proto-AI, then **raised to 5 the same day** under the derived-attribute ruling (ceil(frame core / 2)) - see *Mental attributes* above. The narrative basis carries forward; the number is now mechanical rather than bespoke.

This is a personhood and narrative ruling, **not** an AI classification. The 2026-11-06 hosting ruling stands: she is a Semi-Autonomous Knowbot and the four-step AI evolution test is not satisfied for her. "Proto-AI" here is the GM's in-fiction description of how much mind a long-running SK has accumulated, not a stat-line change.

## Traces, datatrails, and who goes to jail

The 2026-11-06 hosting ruling decided that Cindy owns no SIN, no bank account, and no registered jackpoint serial numbers, so **her datatrails resolve to Mevin's paid MSP account**. Trace pressure on her is therefore legal pressure on him. These ratings decide how hard that is to follow.

| Item | Value | Basis |
|---|---|---|
| SK datatrail trace modifier | **+6** | *Matrix* p. 150 - SKs have no jackpoint to trace; track and trace IC treat their datatrails as if the trace modifier were +6. Book value, adopted |
| Relocate Trace | **yes**, rating 4 | *Matrix* p. 150 permits SKs this operation. Blocks trace IC for a Combat Turn; ongoing, and each turn it fails costs her security tally |
| Redirect Datatrail | **no** | **GM ruling 2026-11-09** - deliberately withheld. See below |
| Datatrail origin | Mevin's MSP account | 2026-11-06 hosting ruling - unchanged and unfixed by anything here |
| Drone control link | remote bounced signal from her trailer-hosted persona | 2026-11-06 ruling; jamming or lost connectivity degrades or severs Dolly Zoom and Tip Jar |

### Why she does not get Redirect Datatrail

*Matrix* p. 150 lets SKs run **both** Redirect Datatrail and Relocate Trace. The GM ruled Cindy gets only Relocate Trace, which leaves her one soft spot a competent trace team can work. Two reasons:

- **It reads as a rushed job.** A sloppy datatrail is consistent with the unresolved-builder thread - *who built and funded an SK, and why*. An SK that can fully launder its own trail looks like a major power's careful work; one whose trail still lands on a decker's retail MSP account looks like someone built her fast, cheap, and in a hurry.
- **It keeps a lever live.** With Redirect available, a trace against Cindy is a dice duel she can win on the defensive forever. Without it, a determined corp trace team can eventually walk her trail back to Mevin, which is a plot the GM can actually spend.

Relocate Trace 4 still lets her stall a trace turn by turn, so the +6 is not a one-shot free pass for whoever is hunting her - it just does not make her unfindable.

**Table consequence:** Cindy can hide, and she can delay a trace, but she cannot launder her own origin. Anything she does on the grid is ultimately chargeable to Mevin, and the GM should feel free to spend that.

## GM panel roll presets

What the **Roll Test** button and `!cindy-roll <dice> <target-number> [skill/context]` actually roll by default. SR3-style exploding sixes; results must meet or beat the target number.

| Preset | Dice | Note |
|---|---|---|
| **Cindy Pilot** (accepted alias: `Cindy Computer`) | **5** | |
| Cindy Hacking Pool | **5** | was 4 under the old MPCP-7 profile |
| Cindy Bod (damage resistance) | **5** | new - resist damage-inflicting attacks |
| Cindy MPCP (utility-crash resistance) | **9** | new - resist hog-style utility crashes |
| Cindy Willpower | **5** | derived ceil(core / 2), raised from 3 on 2026-11-09 - mind-affecting effects |
| Analyze / Browse / Deception / **Sleaze** | 5 | Sleaze restored to 5 on 2026-11-09; returns her Detection Factor to 6 |
| Restore / Scanner / Read-Write / Spoof / Validate | 4 | |
| Commlink / Matrixlink | 4 | external device, not carried code |
| Shield | 2 | parry; spend a rating per use |
| Tip Jar Sensor / Pilot | 2 | |
| Tip Jar fuzzy-logic Pilot | 4 | |
| Dolly Zoom Pilot | 1 | |
| Dolly Zoom Sensor | 0 | |

Panel default when nothing is entered: **Cindy Pilot 5 against TN 5**.

**Preset status (updated 2026-11-09):** the `!cindy-roll` presets and the GM panel defaults were **repointed to this page's core-9 values** in the live bridge (`PANEL_ROLL_PRESETS`, `voice_chat.py`). New presets: **Cindy Bod 5** (damage resistance), **Cindy MPCP 9** (utility-crash resistance), **Cindy Willpower 5**, **Shield 2**, **Restore 4**, **Commlink 4**, **Matrixlink 4**; Hacking Pool moved 4 to 5. `Attack` and `Armor` were deliberately removed - an unlisted skill name falls back to 5 dice and echoes the requested label back, so a stale habit is visible rather than silently wrong.

**Skill presets added 2026-11-09 with the copied Combat Decker package:** `Computer` / `Cindy Computer` now roll **6** (the trained skill) while `Pilot` / `Cindy Pilot` stay at **5** (the built-in floor) - deliberately no longer the same preset. Also live: Computer B/R **4**, Electronics B/R **4**, Etiquette and Etiquette Matrix **3**, Cindy Intelligence **5**, Cindy Charisma **5**, Data Havens **5**, Matrix Gangs **4**.

**Sleaze note:** it was briefly set to 4 in the 09:33 EST deploy, on the mistaken Frame Point budget described above. It is **5** again; the bridge was restarted again after that correction. Verify against this page if the bridge is later rolled back.

## Field drone presets

Cindy's two A-NPC field bodies. Both are options for Cindy Initiative suggestions, not auto-deploy assets. Full write-ups: [Tip Jar](../../Vehicles/Tip-Jar.md), [Dolly Zoom](../../Vehicles/Dolly-Zoom.md).

| Drone | Role | Handling | Speed/Accel | Body/Armor | Sig/Autonav | Pilot/Sensor | Cargo/Load |
|---|---|---|---|---|---|---|---|
| **Tip Jar** (Renraku Barback, customized) | Busking avatar, social face, distraction | 3 | 10/- | 2/0 | 6/0 | 2 (4) / 2 | 0/20 |
| **Dolly Zoom** (generic VTOL surr drone) | Aerial eyes-and-ears, perimeter watch | 3 | 70/9 | 1/0 | 5/0 | 1/0 | 0/10 |

Tip Jar also carries: Strength 6 mechanical arms (two), Adaptation Pool 2, fuzzy logic augmentation, robotic pilot, and Cindy's busking amp/microphone/credstick package.

## Physical body quick reference (GM ruling, 2026-11-06)

Cindy's runtime lives on a **large server housed in a trailer on Taco's garage property**. Matrix access reaches the trailer through an **MSP account Mevin pays for**. She is a **Semi-Autonomous Knowbot (SK)**, not a true AI. Full ruling and citations: [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md#physical-body-and-hosting-gm-ruling-2026-11-06).

| Item | Value |
|---|---|
| Physical body | Large server, trailer at Taco's garage property |
| Matrix access | MSP account paid for by Mevin, serving the trailer |
| Locomotion | Native (persona without a cyberdeck); no deck or jackpoint required |
| Authorization | Not native; rides Mevin's account, datatrails resolve to Mevin |
| Execution | Not native; depends on the trailer's power and physical security |
| Drones | Peripherals reached by a remotely bounced signal, not hosted in a vehicle |

> **The GMC Bulldog Sec. Step-Van is NOT Cindy's body.** The GM ruled it an older concept Mevin abandoned and never built. Do not use a van chassis row for Cindy. Historical design work only: [abandoned concept](../Cindy-Lou-Jenkins.md#mobile-host--vehicle-chassis-concept--abandoned-concept-never-built).

| Stat | Value |
|---|---|
| Handling | 4/6 |
| Speed | 85 |
| Acceleration | 4 |
| Body | 4 |
| Armor | 5 (concealed profile) |
| Signature | 2 |
| Autonav | 2 |
| Pilot | - |
| Sensor | 0 stock, **2 installed** |
| Cargo / Load | 50 CF / 960 kg |
| Seating | 1 + 1b |
| Street Index | 2 |

For table use, treat the trailer server as the thing that can actually be lost. If it is powered down, breached, flooded, burned out, or stolen, Cindy's local runtime is endangered. Cutting the connectivity she shares with it also costs her drone control and her Matrix presence.

## Rulings with no book answer (2026-11-09)

Recorded so nobody re-litigates them mid-session.

- **No SOTA.** The campaign does not run Saeder-Krupp State of the Art software maintenance for Cindy. Consequence: **no upkeep-based rating decay**. Her utility ratings do not slide because nobody is paying a maintenance contract, so a low rating is a build choice or an injury, never an accounting artifact. This also removes "nobody maintains her" as a free explanation for any stat being lower than it should be.
- **Trailer hardware is out of scope for now.** The trailer server is nominally her real hit points under the reboot ruling, and it still has no stat block - no cabinet Body or Armor, no battery reserve, no physical security, no MSP line bandwidth. Deliberately deferred, not forgotten. Until it has numbers, the GM sets what it takes to threaten her permanently by scene.

## To do (parked)

<details markdown="1">
<summary>Open GM decisions - set aside 2026-11-09. Nothing here blocks play. (click to expand)</summary>

The stat sheet is complete and playable as it stands. These are calls the GM has not made yet, plus one escalation the GM should notice before a big Matrix scene. Answering "what can Cindy do right now" does not require any of them - where one is load-bearing, say so rather than guessing.


1. **Out-of-combat Utility Pool refresh.** The book refreshes the Pool at the start of each Combat Turn and says nothing about peacetime. Decide whether Cindy may hold one or two utilities up out of combat - this sets whether she is DF 6 or DF 3 while the crew is simply walking down the street.
2. **Spare Persona Points.** 6 of her 27 go unspent. They can raise an attribute (nothing may exceed core 9), or the GM can call them unassigned.
3. **Unspent Frame Points (37).** Nothing left to buy except Pool rating (cap 9) and Initiative dice (up to 5D6). Say the word if you want either; neither was taken without a ruling. Note the tension with "competent, not elite": Pool 9 lets her produce a rating 9 utility on demand, which is better gear than several sample deckers carry standing.
4. **Response Increase 1.** It is deck hardware on a *frame* sheet, and it is one of the numbers inherited from the suspect recovered profile. As printed it grants +2 Reaction and +1D6 Initiative, which conflicts with GM-tuned Reaction 6 and would make the purchased Initiative die redundant. It needs a home or a deletion.
5. **Provenance of the recovered profile** - still unanswered from the previous pass. The six recovered numbers match the core rulebook's **stock CMT Avatar cyberdeck** row exactly (MPCP-7, Hardening 4, Active 700, Storage 1400, I/O 300, Response Increase 1), and eight of her nine original utilities match the sample Combat Decker who runs one.
6. **Skills - resolved 2026-11-09.** The GM adopted the core rulebook Combat Decker package (printed p. 67) under the derived-attribute ruling; see *Skills* above. Two follow-ups stay open there: the 16-dice Matrix pool throttle, and whether to add general Electronics plus a Search Operations specialization.
7. **Magic** - whether Confuse, manabarriers, or an astrally projecting mage can touch her at all.

</details>

## Table boundaries

- Cindy does not auto-deploy drones or auto-solve scenes. The GM decides availability, positioning, detection, jamming, and consequences.
- The A-NPC's role is advice, observation, and Matrix support. Tactical decisions stay with the players.
- Roll presets are conveniences, not a claim that Cindy is immune to failure. She rolls, and she can miss.

## Connected pages

- [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md) - canonical NPC dossier, hardware build, capacity accounting
- [Cindy Lou Jenkins, In Her Own Words](../Cindy-Lou-Jenkins-In-Her-Own-Words.md) - first-person profile
- [Cindy Lou GM Control Panel](GM-Control-Panel.md) - Roll Test and voice-line controls
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) - `!cindy-roll` and command reference
- [Tip Jar](../../Vehicles/Tip-Jar.md), [Dolly Zoom](../../Vehicles/Dolly-Zoom.md) - field drone write-ups
- [Cindy Lou Tooling](./) - all Cindy tooling pages

## Sources

- [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md) - recovered Matrix profile, table-use assumptions, chassis build
- [Cindy Lou GM Control Panel](GM-Control-Panel.md) - Roll Test defaults and preset reference values
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) - `!cindy-roll` behavior and presets
- *Shadowrun, Third Edition* and *Rigger 3 Revised* p. 173 - vehicle and drone stat conventions
- *Sprawl Survival Guide*, p. 122 - Renraku Barback stock profile
