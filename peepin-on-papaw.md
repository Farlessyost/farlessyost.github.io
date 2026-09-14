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

{% include turntable-controls.html %}

## How the modules work together

The modules form a discrete-event sensing system. Motion and door sensors report binary states and state transitions over ESP-NOW to a central receiver. The receiver forwards events over USB; Python stores the timestamped event sequence in SQLite for the caregiver dashboard. This creates a time history of sensor activity without cameras.

Door state and motion provide complementary observations of household activity. Local logging keeps the activity history on the computer, and camera-free sensing limits the detail collected about daily life.

{% include figure.html src="/assets/images/papaw-family-sequence.gif" poster="/assets/images/papaw-family-sequence.png" alt="Peepin on Papaw receiver, door sensor, and motion sensor rotating, separating, and reassembling" caption="All three modules, showing the enclosures and internal components." %}

<details class="figure-details" markdown="1">
<summary>Individual modules</summary>

### Motion sensor

The passive infrared sensor converts changes in infrared radiation into a binary detection signal: motion detected or clear. The ESP32-C3 reports state transitions to the receiver. Three AAA cells and a regulator power the node, while the cover’s hood is designed to restrict the angular field of view toward a doorway.

A restricted field of view is intended to associate triggers with a particular doorway. Battery power allows placement without routing a power cable to each sensor.

{% include figure.html src="/assets/images/papaw-sensor-sequence.gif" poster="/assets/images/papaw-sensor-sequence.png" alt="Motion sensor CAD assembly with a faceted PIR lens, ESP32-C3 board, power regulator, and three AAA cells" caption="Motion sensor. HC-SR501, ESP32-C3, and three AAA cells in a directional enclosure." %}

### Door sensor

The door is represented as a two-state system: open or closed. Moving the door changes the separation between a magnet and reed switch, producing a state transition that the ESP32-C3 reports wirelessly. Three AAA cells power the sensor; the separate magnet is passive and needs no electrical power.

A magnetic contact gives a direct observation of door state. The passive magnet keeps one half of the assembly small and eliminates an electrical connection across the moving door joint.

{% include figure.html src="/assets/images/papaw-door-sequence.gif" poster="/assets/images/papaw-door-sequence.png" alt="Magnetic door sensor CAD assembly with an ESP32-C3, reed switch, three AAA cells, and a separate magnet pod" caption="Door sensor. A reed switch detects the separate magnet, and an ESP32-C3 reports door activity." %}

### Receiver

The USB-powered ESP32-C3 aggregates discrete sensor events and forwards them to the computer. Packet sequence numbers identify event order within each sensor’s stream, and the computer adds arrival timestamps for temporal analysis. The OLED displays node connectivity, recent activity, and error indicators for a quick local check.

Centralizing radio reception and computer communication keeps the sensor nodes focused on detection. The local display makes connection and activity checks accessible without opening the dashboard.

{% include figure.html src="/assets/images/papaw-receiver-sequence.gif" poster="/assets/images/papaw-receiver-sequence.png" alt="USB-powered receiver CAD assembly with an ESP32-C3 board, four-wire connection, and 0.96 inch OLED display" caption="Receiver. An ESP32-C3 receives sensor events and drives a local OLED display." %}

</details>
