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
cover: /assets/images/papaw-sensor-current.png
cover_alt: Current Peepin on Papaw sensor enclosure with its revised battery contact frame
focus: Camera-free activity sensing
methods: Embedded firmware, event processing, enclosure CAD
context: Independent engineering project
next_url: /projects/xyz-robot/
next_title: XYZ robot
---
## Overview

Peepin on Papaw records activity around a home using motion sensors and door switches. I’m developing the firmware, receiver, dashboard, and printed enclosures.

## My work

- **Firmware:** ESP32-C3 sensor nodes send events over ESP-NOW to a USB receiver.
- **Software:** Python and SQLite handle local logging. A browser dashboard displays the event history.
- **Mechanical design:** FreeCAD enclosures house the sensors, electronics, and AAA batteries.
- **Testing:** Scenario tools check missed packets, repeated triggers, visitors, and sensor outages. Uncertain movement estimates stay marked in the dashboard.

{% include figure.html src="/assets/images/papaw-sensor-current.png" alt="Exploded CAD view of the motion-sensor node with electronics and the revised three-AAA contact frame" caption="Motion-sensor enclosure with the revised three-AAA contact frame. September 2026 CAD design." %}

## Status

Sensor nodes transmit to the receiver, housings have been printed, and the dashboard is implemented. The latest battery-contact frame has been checked in CAD and awaits physical fit and electrical testing.

{% include figure.html src="/assets/images/papaw-battery-current.png" alt="Three AAA cells held by the thin retaining frame with metal contacts and series wiring" caption="The latest battery retrofit uses the housing’s existing cradle with a thin retaining frame, separate metal contacts, and series wiring." %}
