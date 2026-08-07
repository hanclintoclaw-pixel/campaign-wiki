---
title: Buying New Items
type: rules-workflow
visibility: player-safe
status: active
canon_status: sr3-canon-summary
confidence: high
updated: 2026-08-07
tags: [gear, workflow, sr3, rules, contacts, legwork]
sources:
  - Shadowrun, Third Edition, Street Gear, pp. 272-275
  - Shadowrun, Third Edition, Contacts, pp. 253-257
  - Shadowrun Companion, Contacts and Enemies, pp. 59-68
  - Rigger 3 Revised, Vehicle Customization, Advanced Drone Pilot, p. 127
---

# Buying New Items

This workflow turns SR3's gear-buying rules into a table procedure for buying new equipment after character creation. It is a play aid, not a replacement for the books; the GM still decides whether a contact is appropriate, whether an item exists in the campaign market, how much heat the inquiry creates, and whether the item fits the tone of play.

Use this for weapons, armor, electronics, vehicles, drones, vehicle parts, cyberware leads, magical gear sourcing, specialized software, permits, and other gear hunts. For pure information legwork, use [Contact Legwork](Contact-Legwork.md). For searching databases or Shadowland, use [Matrix Searches](Matrix-Searches.md).

## Core idea

In SR3, buying gear on the street is not just paying catalog price.

Most post-character-creation runner purchases go through contacts, usually a fixer or specialist. Two numbers drive the process:

- **Availability:** how hard the item is to locate and how long it takes.
- **Street Index:** how much the black/gray-market price multiplies the legal retail cost.

The basic flow is:

1. Choose the item and identify its Availability, Street Index, base cost, and Legality Code.
2. Choose an appropriate contact or route.
3. Roll Etiquette against the Availability target number.
4. If successful, divide the listed base time by successes to determine how long it takes to locate the item.
5. Halfway through the wait, negotiate the final street price.
6. Arrange pickup, delivery, permits, bribes, or installation as needed.
7. Track wrong-party risk if the inquiry is sensitive or illegal.

## Step 1: Define the exact item

Start narrow. The more precise the ask, the easier it is for the GM and contact to adjudicate.

Record:

- item name;
- rating, if any;
- source/table being used;
- base cost;
- Availability code;
- Street Index;
- Legality Code;
- whether this is retail, gray market, black market, stolen, used, custom, or special-order;
- whether installation, licensing, ammunition, accessories, or permits are separate purchases.

If the item is from a specialized sourcebook, use that book's item listing first. The core SR3 purchasing procedure still governs how a runner finds it unless the book provides a more specific rule.

## Step 2: Read the Availability code

SR3 Availability is written as two values separated by a slash.

- **Left side:** target number for the Etiquette Test to find a source.
- **Right side:** base time to acquire the item, usually in hours, days, or months.

Example structure:

```text
Availability 8/48 hrs
Availability target number: 8
Base acquisition time: 48 hours
```

The GM may adjust Availability for campaign context. A common legal item in a corp mall, a military-grade restricted weapon, a prototype drone component, and a talismanic oddity should not feel equally available just because they all have table entries.

## Step 3: Pick the sourcing route

Choose the route that fits the item.

### Known specialist contact

Use this when the runner has the right person already.

Examples:

- arms dealer for weapons and ammunition;
- talismonger for magical gear;
- street doc or clinic contact for cyberware leads;
- mechanic / rigger contact for vehicles and drone parts;
- decker, data haven, or software broker for Matrix utilities;
- fixer for broad but expensive access.

### Fixer route

Fixers are the default middlemen. They can shop requests across a network, but they expect payment, favors, or future consideration. A fixer may also be safer than asking five wrong people directly.

### Friend of a Friend route

Use [Contact Legwork](Contact-Legwork.md) when the first contact is not the right source but can introduce someone better. Companion's FOF rules can increase target numbers, multiply cost/time, and raise leak risk.

### Legal retail route

If the item is legal, the character has a valid SIN or cover identity, and the GM agrees it is publicly available, the purchase may not need the black-market sourcing procedure. Legal purchases still create data trails and may require permits.

### Direct theft or run route

If the item is too rare, too expensive, or too controlled, the honest answer may be: nobody can sell this cleanly. It becomes a run target, salvage objective, reward, bribe, or favor.

## Step 4: Roll to find the item

The standard SR3 street-purchase test is:

```text
Etiquette Test vs the item's Availability target number
```

Use the Etiquette specialization that fits the route: Street, Corporate, Matrix, Magical, Mercenary, Tribal, or a table-approved specialty.

Contact level bonuses apply when using an established contact:

- Level 1 contact: no bonus dice.
- Level 2 contact: +1 die to relevant information/acquisition Etiquette Tests.
- Level 3 contact: +2 dice.

If the roll succeeds, the source is found and the order can be placed.

If the roll fails, that contact cannot or will not locate the item right now. The character may try another appropriate contact, wait, pay more, accept a FOF route, or turn the acquisition into a run.

## Step 5: Trade time and money against Availability

SR3 gives an explicit pressure valve when the character fails to locate an item but wants it badly enough.

At the GM's discretion, the character may:

- add **2 days** to the acquisition time; and
- add **0.1** to the Street Index;
- to reduce the Availability target number by **1**.

This represents putting the word out that time and nuyen are not obstacles. It makes the item easier to find, slower to get, more expensive, and louder in the shadows.

Use this carefully. It is perfect for desperate runner behavior, but it should feel like desperation: more people hear about the ask, the final price climbs, and the wrong people may notice.

## Step 6: Determine wait time

If the Etiquette Test succeeds:

```text
actual acquisition time = listed base time / Etiquette successes
```

Round in the way that best fits the table's normal timing practice. Preserve the unit from the item listing: hours stay hours, days stay days, months stay months.

For FOF sourcing, Companion modifies the wait:

1. Start with the item's normal Availability time.
2. Apply the FOF cost/time multiplier.
3. The player may spend Etiquette successes or extra money to reduce wait time.
4. Each spent success, or each extra 10 percent of the contact fee paid, reduces the wait by 1 day when using the Companion FOF waiting procedure.

Do not let time math erase the fiction. If the item requires a shipment, a permit, a lab, a vehicle facility, surgery scheduling, or a pickup in another city, the GM can impose those details.

## Step 7: Calculate street price

For black/gray-market purchases, start here:

```text
asking street price = item base cost x Street Index
```

If the character raised the Street Index while reducing Availability, use the revised Street Index.

Then negotiate.

SR3 uses a Success Contest:

```text
buyer Negotiation vs source Intelligence
source Negotiation vs buyer Intelligence
```

The side with more successes adjusts the price by **5 percent per net success** in their favor.

If the buyer wins, the price drops. If the seller wins, the price rises or the seller may demand the difference as a down payment.

If the buyer refuses or cannot pay after the negotiation, the deal falls through. SR3 warns that fixers dislike wasted deals; the GM may increase future Availability target numbers through that contact.

## Step 8: Handle legality and permits

Legality Codes are about what happens if law enforcement or security notices restricted gear.

The first part of the code is the restriction severity. Lower numbers are more restricted. If an officer or security figure notices or suspects the item, the GM may roll an appropriate Security or Police Procedures Knowledge Skill against that restriction target number.

- Failure: the officer notices no actionable impropriety.
- 1 success: the officer knows something is off but may only warn or ignore it.
- More successes: the officer may ask for permits, detain, arrest, confiscate, fine, or escalate.

Codes marked with **P** may allow permits. Permits can make possession, transport, or use legal, and can make street acquisition easier in some cases. They also create records.

Legality is local. The default codes assume Seattle/UCAS-style assumptions; enforcement can vary by jurisdiction, corp property, border, neighborhood, and plot context.

## Step 9: Track wrong-party risk

Buying illegal or rare gear is information leakage.

Use Companion's Wrong Party rules when the inquiry matters:

- the GM rolls when a contact or FOF is used;
- dice equal the number of people involved in the inquiry;
- base TN is 6;
- careful/paranoid play can raise TN;
- careless or broad inquiry can lower TN;
- FOF routes can lower TN further through Wrong Party modifiers;
- successes accumulate across a line of inquiry.

Wrong-party consequences can be subtle: higher prices, bad leads, planted gear, surveillance, rival buyers, police interest, corporate attention, or a trap at pickup.

This is especially important for restricted weapons, military hardware, cyberware, magical goods, stolen prototypes, high-end Matrix utilities, and rare rigger parts.

## Step 10: Arrange pickup and installation

Once the item is found and price is agreed, decide how it reaches the character.

Ask:

1. Where is the pickup?
2. Who carries the nuyen?
3. Is the seller trusted?
4. Does the item need inspection before payment?
5. Is there a permit, fake SIN, smuggling, or storage issue?
6. Does installation require a clinic, shop, facility, magical lodge, vehicle facility, cyberterminal, or specialist?
7. Does the purchase create a sheet change now, or only after installation/attunement/approval?

For workflow-app design, this is a natural final panel: **located**, **price agreed**, **pickup planned**, **installed/accepted separately**.

## Special cases

### Gear at character creation

At character creation, starting resources buy gear at listed cost without applying Street Index. Starting gear is still subject to GM approval and the character-creation limits, including the core restriction that no starting item can have Availability higher than 8 or rating higher than 6.

Once play begins, new purchases use normal Availability and Street Index rules.

### Used, stolen, damaged, or salvaged gear

SR3's core purchase procedure gives the street process, not a full condition system for every used item. For used/salvage deals, the GM should explicitly set:

- discount or markup;
- condition;
- missing accessories;
- repair cost;
- legal risk;
- whether the serial trail is burned;
- whether the item needs a B/R test before use.

A cheap item with a hidden maintenance problem can be a better story than a clean bargain.

### Cyberware and bioware

Buying ware is not the same as installing ware. Treat the acquisition, medical provider, grade, legality, surgery, recovery, Essence/Bio Index effects, and records as separate steps when they matter.

### Magical gear

Talismongers, magical groups, lodges, telesma sources, foci, formulae, and permits have their own fiction and risks. Use a magical contact route unless the item is truly retail-common.

### Rigger parts and Advanced Drone Pilot

Rigger 3 Revised gives a useful example of why this workflow matters.

**Advanced Drone Pilot Rating 2** is the public-retail ceiling for that option: a Rating 2 pilot has limited autonomy and can interpret commands with slight latitude. Rigger 3 Revised lists Rating 2-3 Advanced Drone Pilot parts at **Availability 6/14 days**, **Street Index 2**, with **Rating 2 parts cost 5,000¥** and installation requiring a **vehicle facility** plus a **Computer B/R** test.

That means recovering or buying a Rating 2 pilot can be a meaningful bluebook project even before installation. Finding it, paying for it, validating it, installing it, and deciding which drone gets it can each be separate table steps.

## Quick table procedure

Before rolling, answer these in order:

1. What exact item, rating, and source table are being used?
2. What are the base cost, Availability, Street Index, and Legality Code?
3. Is this legal retail, gray market, black market, FOF, or a run target?
4. Which contact or sourcing route is appropriate?
5. What Etiquette specialization applies, and what contact-level bonus dice apply?
6. Did the Etiquette Test beat Availability?
7. How long does the item take to locate?
8. Is the buyer increasing time/Street Index to reduce Availability?
9. What is the starting street price?
10. What is the Negotiation result and final price?
11. Is there a wrong-party risk roll?
12. What pickup, permit, inspection, and installation steps remain?
13. What sheet change is allowed now, and what waits for GM approval?

## GM-facing result format

Use this compact report after an acquisition attempt:

```text
Buying New Items Report
Item: [name, rating, source]
Route: legal retail / known contact / fixer / FOF / direct run / salvage
Contact: [name/type/level]
Availability: [TN/base time]
Street Index: [base or revised]
Legality: [code, permit status]
Find roll: [Etiquette specialty] vs TN [number], [successes] successes
Wait: [base time / successes, plus any FOF or Availability adjustments]
Starting street price: [base cost x Street Index]
Negotiation: [buyer successes vs seller successes; final price]
Nuyen delta: [amount paid now, deposit, fee, or none]
Wrong Party: [dice/TN if known, successes if GM reveals them]
Pickup/Install: [where, when, inspection, facility/clinic/lodge needed]
Sheet change: [none / acquired but uninstalled / installed / permit / GM approval pending]
Next hook: [follow-up contact, pickup scene, installation test, complication]
```

## App-design notes

A future buying-items workflow app should separate the process into clear panels:

1. **Item definition:** name, rating, source, cost, Availability, SI, legality.
2. **Route choice:** legal retail, fixer, specialist contact, FOF, or run target.
3. **Find test:** Etiquette dice, TN, successes, time calculation.
4. **Pressure options:** wait longer / pay more / reduce Availability / accept leak risk.
5. **Price negotiation:** base street price, buyer/seller rolls, 5 percent net-success adjustment.
6. **Risk:** legality, permits, wrong-party risk, pickup danger.
7. **Closeout:** final report, nuyen delta, pickup/install status, allowed sheet change.

Important design rule: **acquired is not always installed**. The app should distinguish between finding/paying for gear, physically receiving gear, installing gear, and applying permanent sheet effects.

## Source notes

- **Shadowrun, Third Edition:** purchasing gear through contacts, Availability code structure, Etiquette acquisition tests, increasing time/Street Index to reduce Availability, Street Index price calculation, Negotiation price contests, legality codes, legal purchases, and permits.
- **Shadowrun Companion:** Friends of Friends, FOF cost/time multipliers, waiting for goods, and Wrong Party Tests for contact-based inquiries.
- **Rigger 3 Revised:** Advanced Drone Pilot ratings, public-retail Rating 2 ceiling, Rating 2 parts cost/availability/SI, and installation requirements.
