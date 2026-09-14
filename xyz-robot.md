---
layout: project
title: XYZ robot
permalink: /projects/xyz-robot/
group: build
order: 2
category: Robotics & control
status: In development
description: An experimental cable-driven robot developed through mechanical CAD, motion simulation, and embedded control.
summary: Bringing a four-cable mechanism from kinematics and simulation into mechanical design, embedded control, and an evolving wrist assembly.
card_methods: MuJoCo · ROS 2 · ESP32 · FreeCAD
cover: /assets/images/xyz-robot-current.png
cover_alt: Current XYZ robot CAD assembly with timber frame, cable mechanism, and servo wrist
focus: Cable-driven motion and tool positioning
methods: Kinematics, simulation, firmware, mechanical CAD
context: Independent engineering project
next_url: /climate-resilience-mfn.html
next_title: Climate resilience across an industrial network
---
## A cable-driven robot

XYZ uses four cables to position a carriage within a frame. I’m developing its mechanical design, simulation, and embedded control system, with a servo wrist for tool positioning.

The current V34 design combines a timber frame, keyed sliding guide, two-servo wrist, and stereo-camera mounting geometry. FreeCAD models define the assembly and individual parts; MuJoCo supports motion studies.

## Medical scanner demonstration

<figure class="project-video">
  <video controls playsinline preload="none" width="1920" height="1080" poster="{{ '/assets/images/xyz-video-poster.jpg' | relative_url }}" aria-label="Medical scanner simulation demonstration" aria-describedby="scanner-video-caption">
    <source src="{{ '/assets/videos/xyz-medical-scanner-demo.mp4' | relative_url }}" type="video/mp4">
    <p>Your browser does not support embedded video. <a href="{{ '/assets/videos/xyz-medical-scanner-demo.mp4' | relative_url }}">Watch the demonstration as an MP4.</a></p>
  </video>
  <figcaption id="scanner-video-caption">A simulated writing demonstration showing the full mechanism, tool contact, stereo-camera views, and reconstructed surface. <span class="video-duration">5 min 43 sec.</span> <a href="{{ '/assets/videos/xyz-medical-scanner-demo.mp4' | relative_url }}">Open video</a></figcaption>
</figure>

{% include figure.html src="/assets/images/xyz-robot-current.png" alt="Complete V34 CAD assembly of the XYZ cable-driven robot" caption="Complete robot assembly, V34. September 2026 CAD design." %}

## From targets to motion

The simulation models cable routes and carriage movement through configurable targets. A ROS 2 interface and hardware bridge share Cartesian target commands, connecting the motion model to the control architecture.

The main-cable firmware uses two ESP32-C3 controllers: one for motion and one for the interface and ROS gateway. The design includes four motor-driver channels, an OLED and rotary encoder, CRC-protected serial commands, arming logic, acceleration limits, and a watchdog.

## Mechanical design

The current assembly uses a timber frame, four descending cables, a weighted rod, and a keyed sliding guide. A two-servo wrist and camera geometry extend the carriage into a more capable tool-positioning concept.

I use interference checks, fit gauges, load calculations, and trajectory studies to refine the assembly. The wrist uses bearing-supported capstans and adjustable tendon paths, while the keyed guide mechanically constrains rod rotation.

{% include figure.html src="/assets/images/xyz-wrist-current.png" alt="V34 two-servo wrist, bearing-supported capstans, tool holder, and stereo-camera mount" caption="V34 wrist assembly with two SG90-style servos, bearing-supported capstans, and the stereo-camera mount." %}

## Prototype progress

The project is an active mechanical and controls prototype. Motion simulations and selected CAD path checks are complete; physical fit, loaded performance, and positioning accuracy remain to be established.

The main-cable controller firmware and current wrist work are separate development stages. The V34 wrist command converter still needs hardware integration and physical testing.
