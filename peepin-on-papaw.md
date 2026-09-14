---
layout: project
title: Peepin on Papaw
permalink: /projects/peepin-on-papaw/
group: build
order: 1
category: Embedded systems
status: In development
description: A camera-free activity-sensing prototype connecting wireless sensor nodes, local event logging, and a caregiver-facing dashboard.
summary: Connecting small wireless sensors and a local dashboard to make everyday activity patterns easier to understand, without cameras.
card_methods: ESP32 · ESP-NOW · Python · SQLite · FreeCAD
cover: /assets/images/papaw-sensor-current.png
cover_alt: Current Peepin on Papaw sensor enclosure with its revised battery contact frame
focus: Connected sensing and activity interpretation
methods: Embedded firmware, event processing, enclosure CAD
context: Independent engineering project
next_url: /projects/xyz-robot/
next_title: XYZ robot
---
## Camera-free activity sensing

Peepin on Papaw uses motion and magnetic sensors to record activity around a home. I’m developing the sensor firmware, receiver, local dashboard, and printed enclosures as one system.

The design uses small wireless nodes rather than cameras. Events are logged locally so they can be reviewed as a sequence, with gaps and uncertain interpretations kept visible.

{% include figure.html src="/assets/images/papaw-sensor-current.png" alt="Exploded CAD view of the motion-sensor node with electronics and the revised three-AAA contact frame" caption="Motion-sensor enclosure with the revised three-AAA contact frame. September 2026 CAD design." %}

## Hardware and software

- **Sensing:** ESP32-C3 nodes read passive infrared motion sensors and magnetic reed switches, then transmit events over ESP-NOW to a USB-connected receiver.
- **Logging:** A Python serial workflow records events in a local SQLite database.
- **Interpretation:** A browser dashboard and Android-installable web app make the event history accessible. Scenario tools exercise packet loss, retriggers, visitors, sensor outages, and multiple occupants.
- **Packaging:** FreeCAD designs bring the electronics, batteries, and sensor openings into compact printable enclosures, with an OLED-equipped receiver.

## Interpreting sensor events

A single motion event does not establish direction or occupancy. The software uses event order and sensor adjacency to explore possible movement, while retaining ambiguity where the observations do not support a single answer.

I use the scenario lab to examine missed packets, repeated triggers, visitors, and sensor outages before relying on an interpretation in the dashboard.

{% include figure.html src="/assets/images/papaw-battery-current.png" alt="Three AAA cells held by the thin retaining frame with metal contacts and series wiring" caption="The latest battery retrofit uses the housing’s existing cradle with a thin retaining frame, separate metal contacts, and series wiring." %}

## Prototype progress

Sensor nodes are transmitting to the receiver, compact housings have been printed, and the local dashboard and scenario tools are implemented. The latest enclosure work adds a thin battery-contact frame to the existing printed housings.

The contact frame has been checked in CAD; physical fit and electrical testing are the next steps. The system remains an activity-sensing prototype.
