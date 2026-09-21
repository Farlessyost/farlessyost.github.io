---
layout: project
title: Peepin on Papaw
permalink: /projects/peepin-on-papaw/
group: build
order: 1
category: Embedded systems
status: In development
description: Camera-free home activity sensing for family caregivers.
summary: Doorway and door sensors give family caregivers a local activity history, without cameras or wearables.
card_methods: ESP32 · ESP-NOW · Python · SQLite · FreeCAD
cover: /assets/images/papaw-family-sequence.gif
cover_poster: /assets/images/papaw-family-sequence.png
cover_alt: Receiver, door sensor, and motion sensor with fitted covers
focus: Camera-free activity sensing
methods: Embedded firmware, event processing, enclosure CAD
context: Independent engineering project
placement_demo: true
next_url: /projects/tetherxyz/
next_title: TetherXYZ
---
## Overview

Peepin on Papaw records activity around a home using motion sensors and door switches. I’m developing the firmware, receiver, dashboard, and printed enclosures.

The system has three modules: a motion sensor, a magnetic door sensor, and a receiver with an OLED display that plugs into a wall outlet.

## Why I’m building it

I want to help families check in on an older relative who wants to stay at home. Has there been movement around the house? Was a door opened? Is there a change in routine worth a phone call or a visit?

In AARP’s 2024 national survey, **75% of U.S. adults age 50 and older** wanted to remain in their current home for as long as possible.[^aging-at-home] Supporting that independence often falls to family. AARP and the National Alliance for Caregiving’s 2025 report estimated **63 million family caregivers** in the U.S., with seven in ten also employed.[^family-caregiving]

Peepin on Papaw is my attempt to provide useful information between those check-ins. Doorway sensors record movement without looking into bedrooms or asking someone to remember a wearable. Door contacts add a record of openings and closings. A local dashboard brings those events together so a caregiver can review what was recorded.

That is also why the app shows sensor connectivity and uncertainty. A quiet timeline could reflect a quiet house, a missed event, or a disconnected sensor. The caregiver needs that context when deciding whether to follow up.

## My work

- **Firmware:** ESP32-C3 sensor nodes send events over ESP-NOW to the receiver.
- **Software:** Python and SQLite handle local logging. A browser dashboard displays the event history.
- **Mechanical design:** FreeCAD enclosures house the sensors, electronics, and AAA batteries.
- **Testing:** Scenario tools check missed packets, repeated triggers, visitors, and sensor outages. Uncertain movement estimates stay marked in the dashboard.

## Placement and detection

The PIR mounts directly on the fixed door frame and faces across the opening. The magnetic door contact is a separate sensor, with its magnet attached to the moving door. Both report wirelessly to the receiver, which plugs into any wall outlet.

{% include papaw-placement.html %}

## App prototype

The caregiver app runs in a browser and can be installed on Android as a progressive web app (PWA).

{% include figure.html src="/assets/images/papaw-app-overview.png" alt="Papaw Care View overview showing recent activity, room estimate, sensor coverage, and visitor context" caption="Sensor connectivity helps distinguish a quiet house from a gap in reporting." %}

Room estimation is a partially observed state-estimation problem. The home is modeled as a graph: rooms are vertices and monitored doorways are edges. Temporal clustering merges repeated PIR triggers, and the order of adjacent doorway events constrains possible paths. Confidence labels summarize heuristic ambiguity; uncertain observations leave multiple rooms possible. The scenario lab tests this logic against known simulated trajectories, packet loss, and multiple occupants.

{% include figure.html src="/assets/images/papaw-app-room-estimate.png" alt="Papaw Care View showing a connected-room graph, a low-confidence room estimate, alternative possible rooms, and sensor details" caption="Ambiguous event sequences leave more than one room possible." %}

{% include turntable-controls.html %}

## How the modules work together

A motion pulse indicates activity at a doorway; a door contact records an opening or closing. Neither identifies a person or their destination on its own. The receiver combines these discrete events into a local activity history, giving the room estimator more constraints than either sensor could provide alone.

Nodes transmit state changes over ESP-NOW and send periodic heartbeats. This keeps radio traffic low while allowing the receiver to distinguish an inactive sensor from one that has stopped reporting.

{% include figure.html src="/assets/images/papaw-family-sequence.gif" poster="/assets/images/papaw-family-sequence.png" alt="Peepin on Papaw receiver, door sensor, and motion sensor rotating, separating, and reassembling" caption="Battery-powered sensor nodes report to a receiver powered from any wall outlet." %}

<details class="figure-details" markdown="1">
<summary>Sensor electronics and firmware</summary>

### Motion sensor

The passive infrared sensor produces a binary motion signal from changes in infrared radiation. The ESP32-C3 transmits state transitions and periodic heartbeats. Three AAA cells and a regulator supply the node, and the cover’s hood restricts its angular field of view.

The hood narrows the sensing region to the doorway, making placement important: it needs to catch a crossing without reacting to nearby room activity. Radio duty cycling reduces battery use.

{% include figure.html src="/assets/images/papaw-sensor-sequence.gif" poster="/assets/images/papaw-sensor-sequence.png" alt="Motion sensor CAD assembly with a faceted PIR lens, ESP32-C3 board, power regulator, and three AAA cells" caption="Motion sensor. HC-SR501, ESP32-C3, and three AAA cells in a directional enclosure." %}

### Door sensor

The magnetic contact represents the door as a two-state system: open or closed. Firmware debouncing requires the reed-switch signal to stabilize before accepting a state transition, suppressing spurious events from contact bounce. GPIO wake-up lets the ESP32-C3 leave deep sleep when the door state changes and return to sleep after reporting.

The passive magnet keeps the moving side small and avoids wiring across the door joint. Sleeping between transitions reduces battery use.

{% include figure.html src="/assets/images/papaw-door-sequence.gif" poster="/assets/images/papaw-door-sequence.png" alt="Magnetic door sensor CAD assembly with an ESP32-C3, reed switch, three AAA cells, and a separate magnet pod" caption="Door sensor. A reed switch detects the separate magnet, and an ESP32-C3 reports door activity." %}

### Receiver

The receiver runs from a USB wall adapter and collects events from the sensor nodes. A bounded packet queue buffers incoming radio messages for processing. Device identifiers and sequence numbers support duplicate suppression. The OLED reports node connectivity, activity, and error indicators.

The queue absorbs short bursts of events, and duplicate suppression keeps retransmissions from inflating activity counts. The OLED lets me check the system without opening the dashboard.

{% include figure.html src="/assets/images/papaw-receiver-sequence.gif" poster="/assets/images/papaw-receiver-sequence.png" alt="USB-powered receiver CAD assembly with an ESP32-C3 board, four-wire connection, and 0.96 inch OLED display" caption="Receiver. An ESP32-C3 receives sensor events and drives a local OLED display." %}

</details>

## References and notes

[^aging-at-home]: Joanne Binette and Fanni Farago, AARP Research. [*2024 Home and Community Preferences Survey.*](https://www.aarp.org/pri/topics/livable-communities/housing/2024-home-community-preferences/) Among U.S. adults age 50 and older, 75% wanted to remain in their current home for as long as possible. The national survey examines housing and community preferences as people age.

[^family-caregiving]: AARP and the National Alliance for Caregiving. [*Caregiving in the US 2025.*](https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025/) The report estimates 63 million U.S. family caregivers and reports that seven in ten are employed. The survey includes caregivers for older adults, other adults, and children with complex conditions or disabilities.
