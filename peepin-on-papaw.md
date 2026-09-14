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
cover: /assets/images/papaw-family-current.gif
cover_poster: /assets/images/papaw-family-current.png
cover_alt: Motion sensor, magnetic door sensor, and OLED receiver CAD assemblies
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

{% include figure.html src="/assets/images/papaw-sensor-current.gif" poster="/assets/images/papaw-sensor-current.png" alt="Motion sensor CAD assembly with a faceted PIR lens, ESP32-C3 board, power regulator, and three AAA cells" caption="Motion sensor. HC-SR501, ESP32-C3, and three AAA cells in a directional enclosure." %}

{% include figure.html src="/assets/images/papaw-door-current.gif" poster="/assets/images/papaw-door-current.png" alt="Magnetic door sensor CAD assembly with an ESP32-C3, reed switch, three AAA cells, and a separate magnet pod" caption="Door sensor. A reed switch detects the separate magnet, and an ESP32-C3 reports door activity." %}

{% include figure.html src="/assets/images/papaw-receiver-current.gif" poster="/assets/images/papaw-receiver-current.png" alt="USB-powered receiver CAD assembly with an ESP32-C3 board, four-wire connection, and 0.96 inch OLED display" caption="Receiver. An ESP32-C3 receives sensor events and drives a local OLED display." %}
