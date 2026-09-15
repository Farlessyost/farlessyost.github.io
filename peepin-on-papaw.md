---
layout: project
title: Peepin on Papaw
permalink: /projects/peepin-on-papaw/
group: build
order: 1
category: Embedded systems
status: In development
description: Wireless motion and door sensors with local activity logging and a caregiver dashboard.
summary: Wireless motion and door sensors with local logging and a caregiver dashboard.
card_methods: ESP32 · ESP-NOW · Python · SQLite · FreeCAD
cover: /assets/images/papaw-family-sequence.gif
cover_poster: /assets/images/papaw-family-sequence.png
cover_alt: Receiver, door sensor, and motion sensor with fitted covers
focus: Camera-free activity sensing
methods: Embedded firmware, event processing, enclosure CAD
context: Independent engineering project
placement_demo: true
next_url: /projects/xyz-robot/
next_title: XYZ robot
---
## Overview

Peepin on Papaw records activity around a home using motion sensors and door switches. I’m developing the firmware, receiver, dashboard, and printed enclosures.

The system has three modules: a motion sensor, a magnetic door sensor, and a USB-powered receiver with an OLED display.

## My work

- **Firmware:** ESP32-C3 sensor nodes send events over ESP-NOW to a USB receiver.
- **Software:** Python and SQLite handle local logging. A browser dashboard displays the event history.
- **Mechanical design:** FreeCAD enclosures house the sensors, electronics, and AAA batteries.
- **Testing:** Scenario tools check missed packets, repeated triggers, visitors, and sensor outages. Uncertain movement estimates stay marked in the dashboard.

## Placement and detection

The motion sensor faces across the doorway so it picks up someone passing through. The door contact has two parts: the sensor on the frame and a magnet on the door. Both report to the receiver beside the computer.

{% include papaw-placement.html %}

## App prototype

The caregiver app runs in a browser and can be installed on Android as a progressive web app (PWA). Its overview shows recent activity, sensor connections, and visitor information in one place.

{% include figure.html src="/assets/images/papaw-app-overview.png" alt="Papaw Care View overview showing recent activity, room estimate, sensor coverage, and visitor context" caption="The app overview shows recent activity, room estimates, and sensor coverage." %}

Room estimation is a partially observed state-estimation problem. The home is modeled as a graph: rooms are vertices and monitored doorways are edges. Temporal clustering merges repeated PIR triggers, and the order of adjacent doorway events constrains possible paths. Confidence labels summarize heuristic ambiguity; uncertain observations leave multiple rooms possible. The scenario lab tests this logic against known simulated trajectories, packet loss, and multiple occupants.

{% include figure.html src="/assets/images/papaw-app-room-estimate.png" alt="Papaw Care View showing a connected-room graph, a low-confidence room estimate, alternative possible rooms, and sensor details" caption="The room view shows the estimated location, other possible rooms, and the sensor events used to make the estimate." %}

{% include turntable-controls.html %}

## How the modules work together

The modules form a distributed, discrete-event sensor network. Motion and magnetic contacts supply binary observations, which the receiver forwards over USB for timestamped storage in SQLite. These observations support room-state estimation, with uncertainty retained when the available signals do not identify a unique state.

Combining complementary sensors provides additional constraints on possible household activity. Event-driven communication limits redundant transmissions, while local processing keeps the activity history on the receiver computer. The design prioritizes useful activity context with limited personal data collection.

{% include figure.html src="/assets/images/papaw-family-sequence.gif" poster="/assets/images/papaw-family-sequence.png" alt="Peepin on Papaw receiver, door sensor, and motion sensor rotating, separating, and reassembling" caption="The PIR sensor detects motion at a doorway, and the magnetic switch records when a door opens or closes. Both send events wirelessly to the USB receiver for logging on the computer. The exploded view shows how the boards, batteries, and display fit inside the printed cases." %}

<details class="figure-details" markdown="1">
<summary>A closer look at each module</summary>

### Motion sensor

The passive infrared sensor produces a binary motion signal from changes in infrared radiation. The ESP32-C3 transmits state transitions and periodic heartbeats. Three AAA cells and a regulator supply the node, and the cover’s hood restricts its angular field of view.

The hood is intended to improve spatial selectivity by associating triggers with a doorway. That introduces a coverage tradeoff: a narrower sensing region needs more careful placement. Event-driven reporting and radio duty cycling reduce communication energy demand, while heartbeats provide a separate indication of node availability.

{% include figure.html src="/assets/images/papaw-sensor-sequence.gif" poster="/assets/images/papaw-sensor-sequence.png" alt="Motion sensor CAD assembly with a faceted PIR lens, ESP32-C3 board, power regulator, and three AAA cells" caption="Motion sensor. HC-SR501, ESP32-C3, and three AAA cells in a directional enclosure." %}

### Door sensor

The magnetic contact represents the door as a two-state system: open or closed. Firmware debouncing requires the reed-switch signal to stabilize before accepting a state transition, suppressing spurious events from contact bounce. GPIO wake-up lets the ESP32-C3 leave deep sleep when the door state changes and return to sleep after reporting.

A direct door-state observation adds information that a motion pulse alone cannot supply. Debouncing improves event integrity, and sleep between transitions reduces the processor’s duty cycle. The passive magnet keeps one side of the assembly small and avoids wiring across the moving door joint.

{% include figure.html src="/assets/images/papaw-door-sequence.gif" poster="/assets/images/papaw-door-sequence.png" alt="Magnetic door sensor CAD assembly with an ESP32-C3, reed switch, three AAA cells, and a separate magnet pod" caption="Door sensor. A reed switch detects the separate magnet, and an ESP32-C3 reports door activity." %}

### Receiver

The USB-powered receiver acts as a gateway between the sensor network and the computer. A bounded packet queue separates radio reception from USB processing. Device identifiers and sequence numbers support duplicate suppression, while the computer adds arrival timestamps for temporal analysis. The OLED reports node connectivity, activity, and error indicators.

Buffering helps handle short bursts of asynchronous events, although a finite queue can overflow. Duplicate suppression prevents retransmissions from inflating activity counts. Centralizing these functions simplifies the sensor nodes, and the local display provides a diagnostic path when the dashboard is unavailable.

{% include figure.html src="/assets/images/papaw-receiver-sequence.gif" poster="/assets/images/papaw-receiver-sequence.png" alt="USB-powered receiver CAD assembly with an ESP32-C3 board, four-wire connection, and 0.96 inch OLED display" caption="Receiver. An ESP32-C3 receives sensor events and drives a local OLED display." %}

</details>
