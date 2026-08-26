---
title: Example Public Dataterm Host
type: matrix-host
visibility: player-safe
status: active
canon_status: rules-derived exemplar
confidence: medium
tags: [matrix, host, sr3, sprawl-survival-guide, dataterm, exemplar]
sources:
  - /Volumes/carbonite/claw/data/cindylou/cleaned/memory/00_sources/rules_references/sourcebooks/SR3_Sprawl_Survival_Guide_FanPro10657/source.md
---

# Example Public Dataterm Host

## What this page is

This is **not a specific Nashville host**. It is an SR3 rules-derived exemplar for a public street dataterm host, based on *Sprawl Survival Guide*, pp. 121-122.

Use it when the crew interacts with a generic public dataterm in a park, mall, transit stop, library, post office, convenience store, club, restaurant, or high-foot-traffic street corner.

## Overview

A public dataterm is the street-level cousin of a home telecom: a public Matrix terminal with vidphone, tortoise computer, small display, speakers, fax/scanner/printer functions, Matrix jackpoint, chip/CD reader, wireless node, and credstick reader. Better neighborhoods may include privacy booths, holo projectors, or low-end cyberterminals. Poorer areas may have vandalized, unreliable, missing, or offline units.

Most dataterms are maintained by the local grid provider. Each has a public MSP account and is designed to let ordinary citizens make calls, access public services, read feeds, move small data, print/fax, verify small transactions, and reach the Matrix without owning a proper deck.

## SR3 Rules Model

Use normal SR3 Matrix host assumptions:

- Treat the sample public dataterm as a **Green-4 host**.
- The SSG sample lists the dataterm host as **Green 4-8/8/8/8/8**, read here as Green-4 with ACIFS 8/8/8/8/8.
- The sample security sheaf includes Probe, Scout, Trace, Passive Alert, and trap-loaded IC entries.
- Dataterms have **Rating 6 anti-tamper systems** to resist physical unauthorized access.
- Typical credstick readers are **Rating 1**.
- Privacy booths, where present, can have **Rating 4 maglocks** and **Barrier Rating 8** booths, plus monitoring to discourage abuse.
- A and AA-area dataterms can include holo projectors and low-end cyberterminals.
- D and E-zone dataterms are uncommon and often vandalized or in disrepair; Z-zones generally do not have them.

## Host Stats (SR3-style)

- **Host Color / Security:** Green-4
- **Host Rating:** 4
- **Access:** 8
- **Control:** 8
- **Index:** 8
- **Files:** 8
- **Slave:** 8
- **Typical IC mix:** Probe-6/8, Scout-6, Trace-8, trap-loaded Killer-8 and Blaster-8 entries from the sample sheaf
- **Physical anti-tamper:** Rating 6
- **Credstick reader:** typically Rating 1
- **Privacy booth, if present:** Rating 4 maglock; Barrier Rating 8
- **Routine decker task TNs:**
  - Use ordinary public functions legally: no illegal test; charge, ID, or account requirement may apply
  - Enter the host illicitly or spoof elevated dataterm access: **8**
  - Browse public MSP services, transit/community postings, maps, public feeds, or civic forms: **4-5**
  - Search local terminal logs, use history, cached public access records, or recent account activity: **8**
  - Pull camera/booth monitoring logs or nearby dataterm maintenance records: **8**
  - Tap or monitor active vidphone / comm use routed through the terminal: **8**
  - Alter access logs, public postings, local print/fax queues, or terminal state: **8**
  - Control attached terminal devices, privacy booth locks, speakers, display, camera, or printer/fax functions: **8**
  - Bypass or disable physical anti-tamper from the host side: **8+**, plus GM adjudication for local hardware and alarms

## Decker Experience profile

This exemplar is loadable in the [Mevin Decker Experience V1](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/) and [Mevin Decker Experience V2](https://hanclintoclaw-pixel.github.io/mevin-decker-experience-v2/) through [data/matrix-hosts/example-public-dataterm-host.json](../../data/matrix-hosts/example-public-dataterm-host.json).

Profile design:

- **Profile ID:** `example-public-dataterm-host`
- **Name:** Example Public Dataterm Host
- **Security code:** Green
- **Security value:** 4
- **Shutdown Tally:** 60
- **Public side:** local-grid map/feed information, civic/service menus, neighborhood notices
- **Protected records:** recent users/account traces, recent activities/session history, local search/public-service activity, maintenance/vandalism/outage logs
- **Device layer:** camera/booth monitoring, printer/fax/scanner/display controls, privacy booth / panic button / anti-tamper status
- **GM-fill model:** the tool tells the player what category of access was earned; the GM supplies actual names, handles, timestamps, feeds, and local facts

The profile is built for quick table use when Mevin decks a generic public terminal rather than a named campaign host.

## Security Sheaf (SR3-style)

The OCR-preserved SSG sample table gives the following dataterm host line and preserved events: **Security Code Green 4-8/8/8/8/8**.

| Trigger Step | Event |
| ---: | --- |
| 5 | Probe-6 |
| 10 | Probe-8 |
| 15 | Scout-6 |
| 20 | Trace-8 |
| 25 | Passive Alert |
| 30 | Probe-6 with trap Killer-8 |
| 35 | Trace-8 with trap Blaster-8 |
| 40+ | Continue escalating at GM discretion if the intrusion remains active; the source OCR preserves trigger steps out to 60 but not all late-row event text cleanly. |

For table play, that means a public dataterm is not harmless just because it is public. It is meant to be used by citizens, but the provider has reason to protect it from vandalism, fraud, identity abuse, telecom tampering, and runners using it as a disposable Matrix beachhead.

## What deckers might find inside

Common finds include:

- public Matrix service menus, map/search queries, transport info, civic forms, and local information feeds
- recent public-use logs, jackpoint sessions, vidphone call records, public account traces, and MSP account fragments
- print/fax queues, scanner/copy records, chip/CD read history, and temporary cache artifacts
- credstick transaction fragments, failed verification attempts, and low-value purchase/payment records
- maintenance logs, vandalism reports, service outages, grid-provider technician records, and anti-tamper alarms
- privacy booth lock events, booth occupancy records, panic-button events, and local monitoring flags where booths exist
- camera, microphone, speaker, display, printer/fax, jackpoint, wireless node, and credstick-reader hooks
- neighborhood signal: who uses this corner, what time they use it, which public handles repeat, and whether someone has been using the same terminal as a covert drop

Paydata should be local and transactional unless the dataterm is being used as a dead drop or staging point. A dataterm may reveal a pattern, a trace, or a lead; it should not normally contain deep corporate secrets by itself.

## Location and neighborhood guidance

SSG places dataterms in public or semi-public high-traffic spaces: parks, libraries, shopping malls, travel stations, post offices, convenience stores, retail stores, restaurants, clubs, and street corners.

Neighborhood security rating should change the fiction:

- **AAA/AA/A:** clean, monitored, upgraded, likely better peripherals; harder to abuse without a fast response.
- **B/C:** ordinary public dataterm; useful, maintained, and watched enough to matter.
- **D/E:** uncommon, vandalized, unreliable, or partly broken; easier physical access may come with missing data, damaged hardware, or local predators watching the booth.
- **Z:** generally absent.

## Host feel

The sculpting should feel civic and provider-branded: public kiosks, grid-provider logos, transit maps, pay-per-use menus, weather crawls, amber maintenance warnings, and cheap privacy-booth curtains. Alert state turns the friendly kiosk into a hard municipal/provider security surface: warnings, connection receipts, technician stamps, camera eyes, and trace tape spooling back toward the jackpoint.

## GM use

Use this exemplar when the dataterm is part of the scene but not a named campaign host. It can answer questions like:

- did a suspect use this terminal?
- what public services, calls, or files passed through it recently?
- can the runners use it as a temporary Matrix access point?
- is someone watching the terminal or using it as a dead drop?
- did the panic button, booth lock, camera, or anti-tamper system fire?
- can the crew scrub their own use before provider security or a trace catches up?

If the dataterm is narratively important, give it local history: broken printer, camera blind spot, repeating vagrant user, provider technician with a side hustle, gang tax, church flyer spam, or a hidden Matrix drop that only appears at certain times.

## Related Pages

- [Matrix Host Construction Guide](Host-Construction-Guide.md)
- [Matrix Searches](Matrix-Searches.md)
- [Example Home Telecom Host](Example-Home-Telecom-Host.md)

## Sources

- *Sprawl Survival Guide* (SR3), pp. 121-122: street dataterm description, common locations, components, local grid-provider ownership, MSP account, anti-tamper, credstick reader, privacy booth, and sample dataterm host table.
- *Matrix* (SR3): host security sheaves, ACIFS model, IC, security tally, host operations, and alert handling.
- *Shadowrun, Third Edition*: core Matrix context and device/security assumptions referenced by SSG.
