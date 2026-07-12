---
title: Matrix Host Construction Guide
type: guide
visibility: player-safe
status: active
canon_status: table-guidance
confidence: high
last_updated_session: 2026-07-12
tags: [matrix, host, guide, decker-experience, sr3]
sources:
  - GM/table-created host design guidance on 2026-07-11
---

# Matrix Host Construction Guide

## Purpose

This guide describes the default structure for building Matrix host records and Decker Experience profiles for campaign use. It is a table aid, not a replacement for Shadowrun 3rd Edition Matrix rules.

The goal is to make each Host feel like a real Matrix system without forcing the GM to prewrite every possible RAW decking operation. The profile should define the **important doors, subsystems, and prompts**; the GM still adjudicates specific access, visibility, control, and consequences at the table.

## Core Host Shape

Each Host should present with **at most two initial entry doors**, plus a front-door quiet-exit option:

1. **Public Visitor Door**
2. **Secure / Hidden Decker Door**
3. **Graceful Logoff**

A Host may have only one entry door, but the front door should still include **Graceful Logoff** so a decker can leave a fully stealthed run quietly.

### Graceful Logoff

The front-door node should include a **Graceful Logoff** option alongside the public and secure/decking entrances. This represents the decker ending the connection cleanly before forcing deeper intrusion, jackout, or hostile disconnect.

Rules of thumb:

- The option should be available from the initial front-door node.
- It usually requires **no roll**.
- The Decker Experience treats this as a quiet exit and includes that fact in the Discord-ready GM report.
- It should not replace dangerous exits deeper in the Host; those still depend on the live topology, IC pressure, and GM adjudication.

### Public Visitor Door

The public door represents normal official Matrix traffic: customers, clients, vendors, public users, employees with low-grade visitor access, or ordinary corporate-facing services.

Rules of thumb:

- The public door usually requires **no roll**.
- It should not reveal true secrets.
- It should lead to a small number of on-theme, official, harmless nodes.
- Public nodes can be fun, flavorful, and useful for tone.
- Public nodes may provide rumors, visible business functions, menus, marketing, public schedules, vendor contact points, or other non-sensitive surface content.
- Public nodes should not bypass the secure intrusion route.

Examples:

- storefront catalog
- public lobby
- product menu
- visitor kiosk
- event schedule
- customer help desk
- public press kit
- vendor intake page
- sanitized personnel directory

A secure or hidden Host may lack the public door entirely.

### Secure / Hidden Decker Door

Every Host connected to the Matrix can be broken into by a decker, even if the route is hidden, hostile, or extremely difficult.

Rules of thumb:

- The secure door usually requires a roll.
- Failure may lock the route and reveal nothing further about the Host.
- The secure door should lead to the Host's intrusion topology: subsystems, protected data, security layers, and deeper nodes.
- For hard Hosts, the secure door can require multiple successes.
- For hidden Hosts, the first challenge may be finding the door before breaching it.

Examples:

- corporate credential gate
- hidden access seam
- staff login surface
- security pinpad
- concealed LTG route
- vendor maintenance backdoor
- private host access node
- UV seam or special-access metaphor

## Public Side Design

The public side should be shallow. It exists to make the Host feel alive and to give legitimate visitors somewhere to go.

Recommended public topology:

- 1 entry node
- 1-3 theme nodes
- optional return/logoff node

Good public-side node types:

- lobby
- catalog
- menu
- reception
- public records
- public event board
- marketing experience
- customer support surface

Public-side content should usually answer: **what does this Host look like to someone who belongs here?**

It should not answer: **what secret is the run about?**

## Private Intrusion Design

Once the secure door is breached, the decker should have access to subsystems and deeper layers appropriate to the Host.

Recommended intrusion topology:

1. Secure entry node
2. Subsystem hub or first protected layer
3. One or more subsystem nodes
4. Security / IC pressure nodes
5. Reward or confirmation nodes
6. Optional deeper hidden layer
7. Clean or dangerous exit

The profile should expose enough structure for the decker to make meaningful choices, but it should not over-answer GM-controlled facts.

## Success Result Contract

Every successful featured action should produce one of two concrete outcomes:

1. **Access to a new node** — a new area, subsystem, layer, confirmation point, clue space, or exit becomes available.
2. **A specific decker-facing result** — the player gets something to tell the GM or write down for future reference.

Avoid success text that only says, "you succeed." The result can be generic, but it must still be usable.

Good generic success outcomes:

- customer files
- shipping records
- employee directory
- camera network access
- door-control access
- vendor records
- archived mail
- payment logs
- visitor schedule
- project names
- public traffic pattern
- security badge list

Recommended result wording:

- **Tell the GM:** "You appear to have access to customer files. Tell the GM you have customer-file access and ask what categories or search terms are available."
- **Personal note:** "You find shipping records worth following up later. Make a note: shipping records exist here, with dates, vendor names, and delivery windows available if the GM confirms scope."
- **Unlocked node:** "The staff-records archive opens as a new node. Continue there to search specific personnel or transaction details."

The tool should make success feel like it changed the situation, even when exact contents remain under GM control.

Permanent outcomes require explicit GM notification. If a decker changes records, creates an account, redirects orders, schedules a delivery, opens a recurring subscription, disables a camera, plants a file, or otherwise changes the campaign state, the result text must tell the player to notify the GM. Until the player tells the GM, the table should assume the GM does not know it happened.

Lockouts are not permanent campaign facts by default. A locked route means the route is closed for the current crawl attempt; after appropriate in-world time passes, the player may reset the tool and try again if the GM agrees the situation allows it.

## Run Advantages and Access Rewards

Use small, targeted Run Advantages when the decker earns concrete help from meatspace or from inside the Host. These are not a full inventory system; they are roll-facing keys, passcodes, tokens, passwords, or table rulings that modify specific tests.

Good targeted rewards:

- **Employee passcode:** `targetNumberModifier: -1`, applies to `staffRecords` or `logon`.
- **Physical keycard / badge:** `targetNumberModifier: -1`, applies to `controlSlave` or door/security actions.
- **Hidden Host password:** `targetNumberModifier: -1`, applies to the next protected subsystem or a named test ID.
- **Borrowed onsite cyberdeck / admin terminal:** `diceBonus: 1` or `diceBonus: 2`, applies to the relevant Host operation.
- **Correct file index phrase:** `requiredSuccessModifier: -1`, applies to `searchCustomer`, `staffRecords`, or `findUvSeam`.

Scenario JSON can grant these from a node with an `advantages` array:

```json
"advantages": [
  {
    "name": "Found staff passcode",
    "reason": "Password note hidden in the manager terminal",
    "targetNumberModifier": -1,
    "appliesTo": ["staffRecords", "logon"]
  }
]
```

### Hidden Reward Secrecy

When a reward is meant to surprise the player, do not mention the reward in the visible choice label, the parent node description, or player-safe prose. Advertise the searchable space, not the prize.

Good visible setup:

- **Choice label:** "Search the cluttered Manager's Office"
- **Parent description:** "The back office is cluttered with receipt tape, old calendars, and half-labeled binders."

Bad visible setup:

- **Choice label:** "Search the Manager's Office for the Bypass Key"
- **Parent description:** "A key is hidden somewhere in the cluttered office."

Put the actual reward reveal in the destination/reward node that appears only after the successful test, and keep explicit mechanics such as `targetNumberModifier` in the JSON and GM-only notes. This preserves table surprise while still making the successful roll concrete.

Use straightforward values: usually `-1` TN, `+1` die, or `-1` required success. Larger rewards should be rare and tied to strong fiction. The app also has a GM / table modifiers panel for manually adding these effects during play when the crew earns a benefit outside the prepared Host profile.

## Subsystem Nodes

Use subsystem nodes to represent broad Matrix capability zones. The classic SR3 host subsystems are useful as design anchors:

- **Access** — entry, credentials, routes, account state
- **Control** — commands, operational controls, changes, active systems
- **Index** — locating files, directories, users, routes, hidden references
- **Files** — records, paydata, archives, protected content
- **Slave** — attached devices, cameras, doors, elevators, environmental systems, machinery

Not every Host needs every subsystem as a separate node. A small Host may combine them. A megacorp Host may split each into multiple layers.

## Security and Device Verbs

When a node represents a subsystem, the featured verbs should often describe **capabilities** rather than final facts.

For example, in a security or slave subsystem, a featured verb might be:

- Camera
- Door Locks
- Elevators
- Alarms
- HVAC
- Badge Readers
- Register
- Drone Dock
- Studio Controls
- File Archive
- Personnel Records

If the roll succeeds, the destination node should usually present a GM-confirmation prompt, not a hardcoded answer. That prompt must still name the specific access or record category the decker earned.

Example result text:

> You appear to have access to the camera network. Tell the GM you have camera-network access; confirm which feeds are visible, whether any cameras can be controlled, and what physical areas this Host actually covers.

This keeps the tool from inventing physical facts that should belong to the GM while still making the decker's success feel concrete.

## Confirmation Node Pattern

Use confirmation nodes when success should grant a capability whose exact fiction depends on the live scene.

Recommended node description structure:

1. State the apparent access, capability, or record category.
2. Tell the player to tell the GM or make a personal note.
3. Suggest the kinds of questions to ask.
4. Avoid resolving scene-specific facts the GM has not established.

Examples:

### Camera Confirmation

> You appear to have access to the camera network. Tell the GM you have camera-network access; confirm which feeds are visible, whether the host controls camera angle or only camera records, and whether any feed is delayed, missing, or spoofed.

### Door Lock Confirmation

> You appear to have access to door-control functions. Tell the GM you have door-control access; confirm which doors are actually slaved to this Host, whether opening them triggers alarms, and how long the control window lasts.

### Elevator Confirmation

> You appear to have access to elevator routing. Tell the GM you have elevator-routing access; confirm which elevator banks are connected, whether floors can be spoofed, and whether physical security notices the routing change.

### File Archive Confirmation

> You appear to have access to a protected file archive. Make a note that protected files are reachable here; confirm with the GM what categories of records exist, what search terms are valid, and whether copying files raises additional tally or IC pressure.

## Featured Actions vs RAW Actions

The Decker Experience should show **featured actions**, not every possible Matrix operation.

Recommended featured action count after the initial door:

- **1 action** for a single locked door, forced-forward obstacle, or high-pressure terminal, as long as the surrounding topology gives the player a way to back out.
- **2 actions** for focused dramatic choice.
- **3 actions** for normal subsystem play.
- **4 actions** for broad hub nodes or public menu nodes.
- **5 actions** only when the fifth action is a back-out, return, retreat, or logoff option.

If a player wants a normal SR3 Matrix operation outside the featured verbs, the GM should adjudicate it conversationally rather than relying on a text field in the tool.

## Hidden and Secure Hosts

A hidden Host may start with only a secure door. It may not present any public side at all.

For these Hosts:

- The first visible node may be an external approach or hidden seam.
- The first roll may be to find the entry route.
- The second roll may be to breach it.
- Failure can leave the decker with no topology, no confirmed subsystems, and no useful host content.

This is intentional. A hard Host should be allowed to reject a weak intrusion before revealing its structure.

## Deep Layers

Use deeper layers when a Host has meaningful internal depth beyond ordinary subsystems.

Examples:

- executive layer
- research layer
- black-project layer
- security operations layer
- hidden donor layer
- UV layer
- AI-haunted layer
- legacy system layer

Deep layers should usually require:

- prior successful discovery
- a specific subsystem route
- multiple successes
- a story key
- or GM permission

Do not reveal deep-layer node names on the Host map until unlocked.

## Security Sheaf Guidance

Security sheaf entries should create escalating table pressure. They do not need to simulate every detail of SR3 host defense, but they should give the GM clear beats.

Host profiles may define `shutdownTally`. If they do not, the tool infers one from Host Rating and the final sheaf threshold. The app presents **Passive Alert** at about one-third of Shutdown and **Active Alert** at about two-thirds inside the Current Node card. Passive Alert turns that card orange; Active Alert turns it red. If Tally reaches the limit, the run ends with Shutdown/dumpshock.

Useful sheaf beats:

- credential probe
- trace starts
- file scramble
- nuisance IC
- tar baby / hold effect
- killer or blaster response
- physical security correlation
- local admin alerted
- corporate security event
- UV containment
- host shutdown / dumpshock

## Anti-Patterns

Avoid these patterns:

- more than two initial entry doors, excluding the required Graceful Logoff option
- public doors that reveal private secrets
- prewriting every RAW operation as a menu item
- making every node a binary choice when the fiction wants a hub
- putting exact physical facts in device success nodes when the GM should decide scope
- revealing the full Host map before the decker earns access
- guaranteeing paydata just because the decker reached a public node
- making failure merely cosmetic
- treating current-crawl lockouts as permanent without GM instruction
- hiding permanent campaign changes in the app without telling the player to notify the GM

## Minimal JSON Topology Sketch

```json
{
  "flow": {
    "startNodeId": "matrix-approach",
    "nodes": [
      {
        "id": "matrix-approach",
        "title": "Host Approach",
        "kind": "entry",
        "description": "The Host presents a public surface and a harder private route.",
        "choices": [
          { "label": "Use the public visitor door", "to": "public-lobby" },
          { "label": "Breach the secure decker door", "to": "secure-subsystem-hub", "testId": "logon", "unlockSuccesses": 1 }
        ]
      },
      {
        "id": "public-lobby",
        "title": "Public Lobby",
        "kind": "public",
        "description": "Official visitor-facing material. No true secrets live here.",
        "choices": [
          { "label": "Browse official public material", "to": "public-brochure" },
          { "label": "Return to the approach", "to": "matrix-approach" }
        ]
      },
      {
        "id": "secure-subsystem-hub",
        "title": "Secure Subsystem Hub",
        "kind": "private",
        "description": "The decker is inside the private side. Subsystems and deeper layers become available.",
        "choices": [
          { "label": "Camera network", "to": "camera-confirmation", "testId": "controlSlave" },
          { "label": "Protected files", "to": "file-confirmation", "testId": "staffRecords" },
          { "label": "Door controls", "to": "door-confirmation", "testId": "controlSlave" }
        ]
      },
      {
        "id": "camera-confirmation",
        "title": "Camera Network Access",
        "kind": "confirmation",
        "description": "You appear to have access to the camera network. Confirm scope, feeds, controls, and blind spots with the GM.",
        "choices": []
      }
    ]
  }
}
```

## Practical Build Checklist

Before publishing a Host profile, confirm:

- The first node has no more than two entry doors plus Graceful Logoff.
- The public door, if present, has no roll and reveals only official surface content.
- The secure door can be rolled against and can fail without revealing the Host.
- Graceful Logoff is available at the front door as a quiet-exit option.
- Private intrusion exposes relevant subsystems.
- Every successful featured action either unlocks a new node or gives the decker a specific GM-facing/personal-note result.
- Hubs with four core options include a fifth back-out/logoff option when needed to prevent dead ends.
- Permanent outcomes explicitly tell the player to notify the GM.
- Lockouts are scoped to the current crawl unless the GM says otherwise; reset after in-world time is allowed when appropriate.
- Device/security verbs lead to GM-confirmation nodes unless exact scope is already canon.
- Hidden/deep layers are gated behind discovery or stronger success thresholds.
- The Host map will not reveal locked or hidden topology early.
- The profile supports the live scene instead of replacing GM adjudication.
