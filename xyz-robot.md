---
layout: project
title: Skopeo
permalink: /projects/skopeo/
group: build
order: 2
category: Robotics & control
status: In development
description: A medical-scanning concept designed for local fabrication and repair.
summary: A medical-scanning concept designed for local fabrication and repair, using cable positioning, printed parts, and a timber frame.
card_methods: MuJoCo · ROS 2 · ESP32 · FreeCAD
cover: /assets/images/xyz-robot-sequence.gif
cover_poster: /assets/images/xyz-robot-sequence.png
cover_alt: Skopeo CAD assembly with timber frame, cable mechanism, and servo wrist
focus: Medical-scanner positioning
methods: Kinematics, simulation, firmware, mechanical CAD
context: Independent engineering project
next_url: /climate-resilience-mfn.html
next_title: Climate resilience modeling
---
## Overview

Skopeo uses four cables to position a carriage and a two-axis wrist to orient the scanning tool. I’m developing the mechanism, simulation, and embedded controls for a medical-scanning platform that can be made and maintained locally.

## Why I’m building it

Access to diagnostics is still limited in much of the world. The 2021 Lancet Commission on diagnostics estimated that **47% of the global population** had little or no access to diagnostics.[^diagnostic-access] For medical imaging specifically, the World Health Assembly’s 2025 resolution calls for affordable equipment, better access in rural and remote areas, and sustained investment in maintenance and trained staff.[^imaging-access]

I’m tackling one part of that problem: the mechanical platform that moves and orients a scanning tool. The aim is to reduce reliance on precision rails, custom-machined frames, and replacement parts that may be difficult to obtain. A frame made from local stock and smaller parts that can be printed or fabricated nearby could make the machine easier to build, repair, and adapt.

I’m currently evaluating positioning, tool contact, and surface reconstruction in simulation. Medical use would require validation of the complete scanning system.

## Why this design

The larger structure can use wood or other readily available stock. Smaller parts can be 3D printed or fabricated locally, then fitted with standard motors, bearings, and electronics.

Cables separate the positioning mechanism from the frame that supports it. The idea is to measure the cable-anchor locations and calibrate the cable lengths, so the inverse-kinematics model uses the geometry of the assembled machine. This is how I intend to reduce dependence on building every frame member to an exact nominal dimension.

The parts still need to fit properly, and the frame needs to be stiff under load. Cable stretch, backlash, and frame deflection all contribute to positioning error. I’m working toward a design that can meet its accuracy requirements with parts people can make, check, and replace locally.

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

Cable positioning reduces dependence on long precision rails. The guides, wrist, and cable-routing parts concentrate the important fits into smaller assemblies that can be fabricated and checked locally. The remaining positioning problem depends on cable-length calibration, cable compliance, and tension management.

{% include figure.html src="/assets/images/xyz-robot-sequence.gif" poster="/assets/images/xyz-robot-sequence.png" alt="Complete CAD assembly of the Skopeo cable-driven scanning platform" caption="Complete Skopeo assembly." %}

## Tool wrist

Two servos control pitch and roll about orthogonal axes, giving the wrist two rotational degrees of freedom. Each drives an antagonistic tendon pair: one tendon pulls while the other pays out. The drum radii set the transmission ratio between servo rotation and joint rotation. Bearing-supported joints carry the tool holder and stereo-camera mount, setting their orientation relative to the working surface.

Local pitch and roll control lets the tool follow changes in the surface normal without requiring the entire carriage to rotate. Independently supported capstans carry tendon loads through bearings, reducing radial loading on the servo shafts.

{% include figure.html src="/assets/images/xyz-wrist-sequence.gif" poster="/assets/images/xyz-wrist-sequence.png" alt="Two-servo wrist, bearing-supported capstans, tool holder, and stereo-camera mount" caption="Wrist assembly with two SG90-style servos, bearing-supported capstans, and the stereo-camera mount." %}

## Corner receiver

Two orthogonal revolute joints provide yaw and pitch so the head can follow the cable’s direction vector as the carriage moves. During homing, a bead fixed to the cable catches the orange paddle and actuates a microswitch. This discrete switching event is intended to establish a cable-length reference for position calibration.

Following the cable angle is intended to limit rubbing and off-axis paddle loading. The mechanical homing reference provides a way to re-establish the cable-length zero after setup or loss of position.

{% include figure.html src="/assets/images/xyz-corner-sequence.gif" poster="/assets/images/xyz-corner-sequence.png" alt="Exploded view and rotation of the gimballed corner receiver, mounting bracket, switch, and fasteners" caption="Corner receiver with its gimbal, switch, and mounting hardware." %}

## Rod and counterweight

The guide combines a prismatic joint for axial translation with a two-axis gimbal for angular motion. A square sleeve and fitted liners constrain rotation about the rod’s axis. The counterweight applies gravitational preload through the rope and pulleys, helping maintain positive cable tensions. Sizing uses quasi-static force and moment equilibrium; the pulley geometry determines mechanical advantage and how the load varies with carriage position.

The keyed guide constrains an unwanted rotational degree of freedom, making tool orientation better defined. Gravity provides passive preload without an additional force actuator, at the cost of added moving inertia and position-dependent loading.

{% include figure.html src="/assets/images/xyz-rod-weight-sequence.gif" poster="/assets/images/xyz-rod-weight-sequence.png" alt="Exploded view and rotation of the keyed rod, guide, pulleys, and counterweight assembly" caption="Keyed rod, guide, pulleys, and counterweight assembly." %}

## References and notes

[^diagnostic-access]: Kenneth A. Fleming et al. [“The Lancet Commission on diagnostics: transforming access to diagnostics.”](https://doi.org/10.1016/S0140-6736(21)00673-5) *The Lancet* 398, 1997 to 2050 (2021). The Commission estimates that 47% of the global population has little or no access to diagnostics. This concerns diagnostics overall, including laboratory testing.

[^imaging-access]: World Health Assembly. [*Strengthening medical imaging capacity*, resolution WHA78.13](https://apps.who.int/gb/ebwha/pdf_files/WHA78/A78_R13-en.pdf) (2025), especially paragraphs 1(2), 1(3), 1(5), and 1(7). Calls for sustainable investment in imaging equipment and maintenance, workforce training, access in rural and remote areas, and consideration of operating and maintenance costs before procurement.
