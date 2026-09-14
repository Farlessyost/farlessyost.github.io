---
layout: project
title: XYZ robot
permalink: /projects/xyz-robot/
group: build
order: 2
category: Robotics & control
status: In development
description: A four-cable robot prototype for tool positioning, with a servo wrist and stereo-camera mount.
summary: Cable-driven robot with motion simulation, embedded controls, and a two-servo wrist.
card_methods: MuJoCo · ROS 2 · ESP32 · FreeCAD
cover: /assets/images/xyz-robot-current.png
cover_alt: Current XYZ robot CAD assembly with timber frame, cable mechanism, and servo wrist
focus: Cable-driven motion and tool positioning
methods: Kinematics, simulation, firmware, mechanical CAD
context: Independent engineering project
next_url: /climate-resilience-mfn.html
next_title: Climate resilience modeling
---
## Overview

XYZ uses four cables to move a carriage inside a frame. I’m developing the mechanical design, simulation, and embedded controls for a medical-scanner concept.

## Simulation demo

<figure class="project-video">
  <video controls playsinline preload="none" width="1920" height="1080" poster="{{ '/assets/images/xyz-video-poster.jpg' | relative_url }}" aria-label="Medical scanner simulation demonstration" aria-describedby="scanner-video-caption">
    <source src="{{ '/assets/videos/xyz-medical-scanner-demo.mp4' | relative_url }}" type="video/mp4">
    <p>Your browser does not support embedded video. <a href="{{ '/assets/videos/xyz-medical-scanner-demo.mp4' | relative_url }}">Watch the demonstration as an MP4.</a></p>
  </video>
  <figcaption id="scanner-video-caption">Simulation showing robot motion, tool contact, stereo-camera views, and surface reconstruction. <span class="video-duration">5 min 43 sec.</span> <a href="{{ '/assets/videos/xyz-medical-scanner-demo.mp4' | relative_url }}">Open video</a></figcaption>
</figure>

## My work

- **Mechanical design:** FreeCAD assembly with a timber frame, keyed guide, two-servo wrist, and stereo-camera mount.
- **Simulation:** MuJoCo motion studies and a ROS 2 interface for Cartesian target commands.
- **Controls:** ESP32-C3 firmware with motor-driver interfaces, acceleration limits, arming logic, and a watchdog.
- **Verification:** CAD interference checks, fit gauges, load calculations, and trajectory studies.

{% include figure.html src="/assets/images/xyz-robot-current.png" alt="Complete V34 CAD assembly of the XYZ cable-driven robot" caption="Complete robot assembly, V34. September 2026 CAD design." %}

{% include figure.html src="/assets/images/xyz-wrist-current.png" alt="V34 two-servo wrist, bearing-supported capstans, tool holder, and stereo-camera mount" caption="V34 wrist assembly with two SG90-style servos, bearing-supported capstans, and the stereo-camera mount." %}

## Status

The V34 assembly and motion simulation are in development. The wrist still needs hardware integration. Physical fit, loaded performance, and positioning accuracy remain to be tested.
