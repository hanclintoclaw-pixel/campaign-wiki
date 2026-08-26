---
title: Example Home Telecom Host
type: matrix-host
visibility: player-safe
status: active
canon_status: rules-derived exemplar
confidence: high
tags: [matrix, host, sr3, sprawl-survival-guide, telecom, exemplar]
sources:
  - /Volumes/carbonite/claw/data/cindylou/cleaned/memory/00_sources/rules_references/sourcebooks/SR3_Sprawl_Survival_Guide_FanPro10657/source.md
---

# Example Home Telecom Host

## What this page is

This is **not a specific Nashville host**. It is an SR3 rules-derived exemplar for the kind of Matrix host built into an ordinary 2060s home telecom terminal, based on *Sprawl Survival Guide*, pp. 120-121.

Use it when the crew hacks a normal household telecom, apartment trid terminal, lifestyle hub, or small residential network and the GM has not prepared a custom host.

## Overview

A home telecom is the household entertainment center, phone, Matrix access point, appliance controller, wireless hub, fax/scanner/printer, and bare-bones host. In a normal home it is the place where residents watch trideo, make vidcalls, check mail, run simple Matrix services, and control connected household devices.

The host should feel personal and messy rather than corporate: family photos, journals, message caches, appliance menus, camera/vidphone hooks, cleaning-drone controls, billing notices, and household logs. Better lifestyles can have higher-quality displays, extra access stations, satellite links, encryption, or upgraded host security. Poorer homes may have cheap, outdated, broken, or non-wireless units.

## SR3 Rules Model

Use normal SR3 Matrix host assumptions:

- Treat the default system as a **Blue-4 host**.
- The source gives the default home telecom host as **ACIFS 8/8/6/6/6** with a single **Probe-2** IC program.
- Security-conscious residents may use broadcast encryption on the home wireless network.
- Typical home wireless nodes have **Flux 0 or 1**.
- Telecoms can be accessed from the Matrix if the jackpoint / MXP address is known, or locally through wireless-device access if the runner has the right gear and range.
- Residents, landlords, building management, or local grid/MSP service may upgrade security at GM discretion.

## Host Stats (SR3-style)

- **Host Color / Security:** Blue-4
- **Host Rating:** 4
- **Access:** 8
- **Control:** 8
- **Index:** 6
- **Files:** 6
- **Slave:** 6
- **Typical IC mix:** Probe-2 only by default
- **Typical wireless node:** Flux 0-1; broadcast encryption if the household is security-conscious
- **Routine decker task TNs:**
  - Find or recognize the telecom address from a known account, bill, or jackpoint reference: **6**
  - Enter the host through the known Matrix address: **8**
  - Search public-facing household pages, guest notes, or low-value shared files: **6**
  - Search personal files, journals, stored messages, family photos, or account notes: **6-7**
  - Dump system, call, device, or access logs: **6**
  - Tap or monitor active vidphone / comm traffic once inside: **8**
  - Monitor connected appliances, cameras, microphones, sensors, or cleaning drones: **6**
  - Control connected appliances, cameras, locks, climate controls, or cleaning drones: **8**
  - Defeat broadcast encryption before touching the local wireless layer: use the relevant SR3 / *Matrix* wireless and encryption rules

## Decker Experience profile

This exemplar is loadable in the [Mevin Decker Experience V1](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/) and [Mevin Decker Experience V2](https://hanclintoclaw-pixel.github.io/mevin-decker-experience-v2/) through [data/matrix-hosts/example-home-telecom-host.json](../../data/matrix-hosts/example-home-telecom-host.json).

Profile design:

- **Profile ID:** `example-home-telecom-host`
- **Name:** Example Home Telecom Host
- **Security code:** Blue
- **Security value:** 4
- **Shutdown Tally:** 16
- **Public side:** household social/profile stand-ins, public photo clues, guestbook/neighborhood links
- **Private side:** personal messages, private files, domestic accounts, call logs, calendars, device/access logs
- **Device layer:** cameras/microphones, appliances/environment controls, household cleaning/service drone controls
- **Bottom outcome:** full telecom host takeover; the player must notify the GM, who fills in exact devices, resident alerts, persistence, and provider/security response

The profile is deliberately shallow. It gives Mevin useful generic buttons for a normal home host while leaving concrete names, files, images, schedules, devices, and secrets for the GM to supply at the table.

## Security Sheaf (SR3-style)

The SSG default is intentionally tiny: **one Probe-2 IC program**. Do not turn every home telecom into a corporate crawl unless the household has a reason to pay for it.

Suggested default handling:

| Tally / Trigger | Event |
| ---: | --- |
| first suspicious access or GM-selected early tally | Probe-2 checks the intruder's icon, account, or connection route. |
| later tally, failed stealth, or obvious tampering | The telecom logs the intrusion and may notify the resident, building security, MSP, or local device owner if such notification is configured. |
| heavy damage, obvious control abuse, or GM call | Host disconnect, service lockout, or household systems dropping offline rather than combat escalation. |

A richer, security-conscious home can add stronger Probe, Trace, Scramble, Tar Baby, or private security notification, but that is an upgraded host rather than the SSG baseline.

## What deckers might find inside

Common finds include:

- resident names, household account IDs, telecom address books, and vidphone call histories
- personal journals, family pages, photos, hobby files, calendars, and domestic reminders
- message caches, faxes, email, voice/video mail, and Matrix-service account crumbs
- billing records, subscription services, maintenance notices, landlord notices, and utility usage
- access logs showing who called, who logged in, and what devices connected
- biometric scan data from cameras, vidphone pickups, door systems, or linked home security devices
- household appliance menus, thermostat settings, lighting, locks, cameras, speakers, entertainment systems, and cleaning drones
- small domestic secrets: affairs, debts, schedules, blackmail material, illegal subscriptions, hidden contacts, or evidence that someone else already compromised the telecom

Paydata should be modest and personal. A home telecom is useful because it is intimate, not because it is rich.

## Device and slave guidance

SSG explicitly calls out telecoms as household network hubs. Attached devices can include:

- trideo receiver, flatscreen, holoprojector, speakers, vidphone, fax/scanner/printer, Matrix jackpoint, chip/CD reader, credstick slot, keyboard/mouse/VR gloves
- wireless household appliances and devices
- cameras, audio pickups, sensors, and access stations
- simple cleaning drones or household service drones using cheap telecom drone-command packages

A decker inside the host can use normal SR3 Matrix operations such as Edit File, Dump Logs, Download Data, Tap Comcall, Monitor Slave, and Control Slave where appropriate.

## Host feel

The sculpting should look like someone's living room interface: trid windows, photo walls, message frames, cluttered appliance panels, stuck calendar notes, and cheap mascot helpers from the user's MSP. Luxury homes make this glossy and multi-room. Low lifestyles make it cracked, spam-ridden, slow, or patched together from old gear.

## GM use

Use this exemplar when the exact household matters less than the fact that the runners are intruding into someone's domestic life. The host can answer questions like:

- who lives here?
- when are they home?
- who have they been calling?
- what cameras or appliances can be turned against the occupants?
- did someone else already tamper with this home?
- what private detail makes this person vulnerable, useful, or dangerous?

Do not assume every home has every device. Confirm exact cameras, drones, locks, sensors, and appliances from the location or lifestyle before granting control.

## Related Pages

- [Matrix Host Construction Guide](Host-Construction-Guide.md)
- [Matrix Searches](Matrix-Searches.md)
- [Example Public Dataterm Host](Example-Public-Dataterm-Host.md)

## Sources

- *Sprawl Survival Guide* (SR3), pp. 120-121: home telecom terminal components, Matrix access, wireless node guidance, default telecom host stats, and telecom subversion options.
- *Matrix* (SR3): host operations, ACIFS model, IC, security tally, wireless link, remote control utility, and alert handling.
- *Shadowrun, Third Edition*: scanner, Flux, broadcast encryption, and core Matrix context referenced by SSG.
