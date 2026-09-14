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
cover: /assets/images/xyz-robot-sequence.gif
cover_poster: /assets/images/xyz-robot-sequence.png
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

{% include turntable-controls.html %}

## Complete robot

Four motor-driven cables position the carriage with three translational degrees of freedom, expressed in Cartesian coordinates (x, y, z). Inverse kinematics maps a target carriage position to cable lengths. Because cables only pull, tension allocation must satisfy force equilibrium with positive cable tensions. The wrist adds two rotational degrees of freedom to orient the tool for scanning or marking.

{% include figure.html src="/assets/images/xyz-robot-sequence.gif" poster="/assets/images/xyz-robot-sequence.png" alt="Complete CAD assembly of the XYZ cable-driven robot" caption="Complete robot assembly." %}

## Tool wrist

Two servos control pitch and roll about orthogonal axes, giving the wrist two rotational degrees of freedom. Each drives an antagonistic tendon pair: one tendon pulls while the other pays out. The drum radii set the transmission ratio between servo rotation and joint rotation. Bearing-supported joints carry the tool holder and stereo-camera mount, setting their orientation relative to the working surface.

{% include figure.html src="/assets/images/xyz-wrist-sequence.gif" poster="/assets/images/xyz-wrist-sequence.png" alt="Two-servo wrist, bearing-supported capstans, tool holder, and stereo-camera mount" caption="Wrist assembly with two SG90-style servos, bearing-supported capstans, and the stereo-camera mount." %}

## Corner receiver

Two orthogonal revolute joints provide yaw and pitch so the head can follow the cable’s direction vector as the carriage moves. During homing, a bead fixed to the cable catches the orange paddle and actuates a microswitch. This discrete switching event is intended to establish a cable-length reference for position calibration.

{% include figure.html src="/assets/images/xyz-corner-sequence.gif" poster="/assets/images/xyz-corner-sequence.png" alt="Exploded view and rotation of the gimballed corner receiver, mounting bracket, switch, and fasteners" caption="Corner receiver with its gimbal, switch, and mounting hardware." %}

## Rod and counterweight

The guide combines a prismatic joint for axial translation with a two-axis gimbal for angular motion. A square sleeve and fitted liners constrain rotation about the rod’s axis. The counterweight applies gravitational preload through the rope and pulleys, helping maintain positive cable tensions. Sizing uses quasi-static force and moment equilibrium; the pulley geometry determines mechanical advantage and how the load varies with carriage position.

{% include figure.html src="/assets/images/xyz-rod-weight-sequence.gif" poster="/assets/images/xyz-rod-weight-sequence.png" alt="Exploded view and rotation of the keyed rod, guide, pulleys, and counterweight assembly" caption="Keyed rod, guide, pulleys, and counterweight assembly." %}
