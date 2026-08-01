---
title: Matrix Searches
type: rules-workflow
visibility: player-safe
status: active
canon_status: sr3-canon-summary
confidence: high
updated: 2026-08-01
tags: [matrix, workflow, sr3, rules, decking, legwork]
sources:
  - Shadowrun, Third Edition, Matrix chapter, pp. 210, 214-217
  - Shadowrun Companion, Contacts and Enemies, pp. 63, 65-66
  - Matrix, Matrix World and Information Searches, pp. 12-13, 124-131
  - Target: Matrix, Data Havens, pp. 24-29
---

# Matrix Searches

This workflow turns the SR3 Matrix search rules into a table procedure. It is a play aid, not a replacement for the books; when exact dice pools, subsystem ratings, or contact rules matter, use the cited source pages.

For a guided worksheet version, use the [Matrix Search Guide](https://hanclintoclaw-pixel.github.io/matrix-search-guide/).

## Pick the kind of search

Use the narrowest workflow that fits the question.

1. **Casual public lookup:** no roll unless the answer matters, is time-sensitive, or could draw attention. Matrix explicitly says not to roll for things like looking up a pizzeria in Matrix yellow pages.
2. **Ask people / work contacts:** use Etiquette (Matrix), Matrix contacts, Shadowland, data havens, info brokers, or Friends of Friends. This is social legwork in the Matrix.
3. **Search records / databases:** use a Computer (Search Operations) Search Test against a specific database/archive or the general Matrix.
4. **Search inside a host you are already on:** use host operations such as Locate File, Locate Access Node, or Locate Slave. These are decking operations, not broad legwork searches.

## Workflow A: Matrix contact legwork

Use this when the character is asking people, posting queries, working Shadowland, or leaning on a Matrix contact.

1. **Name the ask.** Be specific about the person, place, organization, code phrase, file rumor, or event being researched.
2. **Choose the source.** Examples: decker contact, info broker, researcher, Shadowland/data haven, pay database, private archive.
3. **Roll the social route.** Characters use Etiquette (Matrix) for Matrix social interactions and Matrix contacts. Normal contact level rules still apply.
4. **Handle Shadowland/data havens carefully.** Underground archive/data haven contacts usually count as Level 2 contacts; the Nexus or similar elite sources may count as Level 3. Matrix gives underground archive/data haven contacts a -2 target number modifier on Etiquette (Matrix) searches, but adds +2D6 to the Wrong Party Test.
5. **Price the answer in favors, paydata, or nuyen.** Shadowland and data havens often work by barter or uploaded paydata, not clean retail purchase.
6. **Check whether word leaks.** Use Wrong Party Tests when the search is sensitive.

Shadowland-specific timing from Shadowrun Companion: 3D6 days by telecom line commands, 1D6 days by tortoise, 2D6 hours by cyberdeck, or 2D6 hours for an approved knowbot search. Matrix also gives data haven / Shadowland style Matrix legwork a base time of 2D6 hours, divided by extra successes, when handled as an Etiquette (Matrix) contact search.

## Workflow B: Computer Search Test

Use this when the character is sifting databases, archives, public records, pay sites, data havens, or the general Matrix with Computer (Search Operations).

1. **Define the search area.**
   - **Specific database/archive:** one known source, such as a DMV archive, a city permits database, a data haven, or the Library of Congress. Apply that database's search modifier.
   - **General Matrix:** multiple sources across the Matrix. This is broader, may cross grids, and is more likely to draw attention.
2. **Define the search type.**
   - **Simple:** public, readily accessible information. TN 4, base time 1D6 hours, base cost 0 nuyen/hour.
   - **Standard:** deeper public/private/pay-site research. TN 5, base time 2D6 hours, base cost 10 nuyen/hour.
   - **Detailed:** in-depth fact-finding such as a dossier, hidden ownership chain, or private records trail. TN 8, base time 1D6 / 2 days, base cost 25 nuyen/hour.
3. **Apply modifiers.** Common modifiers from Matrix p. 131:
   - appropriate Knowledge skill 3-5: -1 TN; 6+: -2 TN
   - low-profile search: +2 TN
   - more than one simultaneous search: +1 TN per extra search
   - terminal mode: +2 TN and double base time
   - cold ASIST: +1 TN
   - Matrix Initiative +4D6 or higher: -1 TN
   - Browse utility rating 6+ in a specific search area: -1 TN
   - appropriate database/data haven contact for general Matrix search: -2 TN
   - Etiquette (Matrix) 5+ for general Matrix search: -1 TN
   - search confined to one grid: +0 TN; each additional grid required: +1 TN
   - dumb frame assistance: -1 TN; smart frame assistance: -2 TN
4. **Roll Computer (Search Operations).** Hacking Pool cannot be used for Search Tests.
5. **Track time and focus.** A character conducting searches cannot do anything else, but can suspend and resume later. Maximum simultaneous searches equals half Intelligence, rounded up.
6. **Spend extra successes.** Extra successes can reduce time or add information, but each extra success can only do one of those. Time reduction divides the base time by the number of extra successes assigned to speed.
7. **Deliver leads, not omniscience.** Matrix recommends parceling out clues across multiple searches, using false leads when appropriate, and making clear when data simply is not available through the Matrix.

Result guideline from the Search Test Table: one success gives general information or a lead, two successes give the basic desired data, additional successes add details and leads, and five or more successes provide the full useful picture plus extra juicy bits.

## Workflow C: Wrong Party risk

Any meaningful Matrix search can alert someone who cares that the character is digging.

For Computer Search Tests, Matrix imports the Shadowrun Companion Wrong Party rules:

- specific area search: GM rolls 1D6
- general Matrix search: GM rolls 3D6
- base target number: 6
- if the character keeps the search low profile: Search Test is +2 TN, but Wrong Party TN rises to 10

For contact legwork, Shadowrun Companion rolls a Wrong Party Test every time a character uses a contact or Friend of a Friend; the dice pool is based on the number of people involved in the inquiry, and successes accumulate over the whole line of inquiry.

## Workflow D: Host-local search operations

Use this when the decker is already in a grid or host and needs to find a system object, not when they are doing broad legwork.

### Locate Access Node

- **Where:** on an RTG.
- **Test:** Index subsystem.
- **Utility:** Browse.
- **Action:** Complex.
- **Use:** find LTG codes that provide access to a desired host, or locate commodes for telecom calls.
- **Specificity modifiers:** vague goal +1 TN, specific but not exact goal +0 TN, definite specific goal -1 TN.
- **After success:** once the LTG code is found, the decker does not need to repeat the operation unless the address changes.

### Locate File

- **Where:** inside a host.
- **Test:** Index subsystem.
- **Utility:** Browse.
- **Action:** Complex.
- **Use:** find specific datafiles. The decker must have some idea what they are looking for; "valuable data" is not enough.
- **Success threshold:** interrogation operations normally locate the objective at 5+ accumulated successes, unless the GM sets another threshold or parcels out clues by success count.

### Locate Slave

- **Where:** inside a host.
- **Test:** Index subsystem.
- **Utility:** Browse.
- **Action:** Complex.
- **Use:** find the system address for a specific remote device controlled by the host.
- **Success threshold:** usually 3 accumulated successes, because hosts generally control fewer slaves than files.

### Interrogation operation guidance

Locate Access Node, Locate File, and Locate Slave are interrogation operations. The decker may need repeated operations, accumulating successes, while security tally continues to matter. Apply +1 TN for vague/general questions, +2 TN for extremely vague/general questions, and -1 or -2 TN for well-phrased, relevant, insightful inquiries. If the host or grid does not have the information, the GM can reveal that after 3+ successes.

## Data haven cautions

Target: Matrix adds useful table color for data havens:

- access is usually reputation-based, code-based, encrypted, or routed through chokepoints;
- havens frequently relocate SANs and change access codes;
- brute-forcing unauthorized access is dangerous and should be treated like a serious decking run;
- data havens are cluttered, disorganized, and often allow or rent search programs, frames, agents, or data-locator services;
- information from havens should be verified because it may be outdated, wrong, planted, or malicious;
- sensitive files and private communications should not be moved through a haven unless the characters accept the risk that the haven may archive or exploit them.

## Quick GM prompts

Before rolling, ask:

1. What exact question are you trying to answer?
2. Are you asking people, searching records, or hacking a host?
3. What source or grid are you searching first?
4. Are you keeping it low profile?
5. What will you trade: time, money, favors, paydata, or risk?

## Source notes

- **Shadowrun, Third Edition:** core Matrix navigation, security tally, Locate Access Node, Locate File, Locate Slave, and interrogation operation procedure.
- **Shadowrun Companion:** Wrong Party Tests, Shadowland as a special contact, Shadowland search timing, and contact/FOF leakage risk.
- **Matrix:** main Information Searches rules, Search Test Table, Matrix contacts, Search Operations specialization, frames/agents assistance, and Matrix privacy context.
- **Target: Matrix:** data haven access, Shadowland/data haven behavior, search services, archive reliability, and operational cautions.
