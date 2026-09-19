---
layout: project
title: TetherXYZ
permalink: /projects/tetherxyz/
group: build
order: 2
category: Robotics & control
status: In development
description: Cable-driven positioning for medical scanning, designed for local fabrication and repair.
summary: Cable-driven positioning for medical scanning, using printed parts and a timber frame designed for local fabrication and repair.
card_methods: MuJoCo · ROS 2 · ESP32 · FreeCAD
cover: /assets/images/tetherxyz-current-turntable.gif
cover_poster: /assets/images/tetherxyz-current-turntable.png
cover_alt: TetherXYZ CAD assembly with timber frame, cable mechanism, and servo wrist
focus: Medical-scanner positioning
methods: Kinematics, simulation, firmware, mechanical CAD
context: Independent engineering project
next_url: /climate-resilience-mfn.html
next_title: Climate resilience modeling
---
## Overview

TetherXYZ uses four cables to position a carriage and a two-axis wrist to orient the scanning tool. I’m developing the mechanism and embedded controls for a medical-scanning platform that can be made and maintained locally.

## Why I’m building it

Access to diagnostics is still limited in much of the world. The 2021 Lancet Commission on diagnostics estimated that **47% of the global population** had little or no access to diagnostics.[^diagnostic-access] For medical imaging specifically, the World Health Assembly’s 2025 resolution calls for affordable equipment, better access in rural and remote areas, and sustained investment in maintenance and trained staff.[^imaging-access]

I’m tackling one part of that problem: the mechanical platform that moves and orients a scanning tool. The aim is to reduce reliance on precision rails, custom-machined frames, and replacement parts that may be difficult to obtain. A frame made from local stock and smaller parts that can be printed or fabricated nearby could make the machine easier to build, repair, and adapt.

## Why this design

The larger structure can use wood or other readily available stock. Smaller parts can be 3D printed or fabricated locally, then fitted with standard motors, bearings, and electronics.

Cables separate the positioning mechanism from the frame that supports it. The idea is to measure the cable-anchor locations and calibrate the cable lengths, so the inverse-kinematics model uses the geometry of the assembled machine. This is how I intend to reduce dependence on building every frame member to an exact nominal dimension.

Cable stretch, backlash, and frame deflection contribute to positioning error. The design concentrates the critical fits in smaller parts that can be fabricated, checked, and replaced locally.

## Motion and surface tracking {#simulation-demo}

The four winches mount to a braced timber frame at different heights and angles. Each pulley head swivels to follow its cable while the motor and backplate stay fixed. The animation follows the bead-homing sequence, then the wrist traces “Hello” across a curved reference surface.

<figure class="project-video">
  <video controls playsinline preload="none" width="960" height="640" poster="{{ '/assets/images/tetherxyz-current-motion.png' | relative_url }}" aria-label="TetherXYZ homing and surface-tracking simulation">
    <source src="{{ '/assets/videos/tetherxyz-current-motion.mp4' | relative_url }}" type="video/mp4">
  </video>
  <figcaption>Homing at four times playback speed, followed by surface tracking at 24 times speed. The detail views show the tool path and the active swivel pulley. <a href="{{ '/assets/videos/tetherxyz-current-motion.mp4' | relative_url }}">Open video</a></figcaption>
</figure>

## Explore the math {#kinematics}

Choose a module and an equation group, then pause or scrub through the motion. The diagram runs through three mounting layouts and the same tool path. It connects the requested tool pose to rod and wrist angles, pulley tangency, cable length, and motor payout.

The calculations use measured mount coordinates and orientations. Homing establishes each cable’s length reference. Moving a mount changes the required cable lengths even when the tool follows the same path.

{% include tetherxyz-math.html %}

## My work

- **Mechanical design:** FreeCAD assembly with a timber frame, keyed guide, two-servo wrist, and stereo-camera mount.
- **Simulation:** Native-CAD motion playback, pulley-aware inverse kinematics, homing sequences, and surface tracking. Earlier MuJoCo work includes a ROS 2 interface for Cartesian target commands.
- **Controls:** ESP32-C3 firmware with motor-driver interfaces, acceleration limits, arming logic, and a watchdog.
- **Verification:** CAD interference checks, fit gauges, load calculations, and trajectory studies.

{% include turntable-controls.html %}

## Complete robot

Four motor-driven cables position the carriage with three translational degrees of freedom, expressed in Cartesian coordinates (x, y, z). Inverse kinematics maps a target carriage position to cable lengths. Because cables only pull, tension allocation must satisfy force equilibrium with positive cable tensions. The wrist adds two rotational degrees of freedom to orient the tool for scanning or marking.

Cable positioning reduces dependence on long precision rails. The guides, wrist, and cable-routing parts concentrate the important fits into smaller assemblies that can be fabricated and checked locally. The remaining positioning problem depends on cable-length calibration, cable compliance, and tension management.

{% include figure.html src="/assets/images/tetherxyz-current-turntable.gif" poster="/assets/images/tetherxyz-current-turntable.png" alt="Complete CAD assembly of the TetherXYZ cable-driven scanning platform" caption="Current TetherXYZ assembly: braced timber frame, four stationary winches with swivel pulley heads, overhead rod guide, and tool wrist." %}

## Tool wrist

Two servos control pitch and roll about orthogonal axes, giving the wrist two rotational degrees of freedom. Each drives an antagonistic tendon pair: one tendon pulls while the other pays out. The drum radii set the transmission ratio between servo rotation and joint rotation. Bearing-supported joints carry the tool holder and stereo-camera mount, setting their orientation relative to the working surface.

Local pitch and roll control lets the tool follow changes in the surface normal without requiring the entire carriage to rotate. Independently supported capstans carry tendon loads through bearings, reducing radial loading on the servo shafts.


## Swivel winches and cable homing

The motor and drum stay on a fixed backplate. A passive swivel head aligns the pulley with the outgoing cable, reducing side loading as the carriage moves. Each module sits against angled cleats on the timber frame; the model uses those mounting angles and heights directly.

Cable length is the sum of the incoming segment, the pulley arc, and the outgoing tangent span. Treating the pulley as a point would miss the change in wrap as the tool moves. The math explorer shows the wrap angle θ, swivel angle ψ, and the resulting length for each module.

During homing, a fixed bead approaches its receiver, trips the switch, backs off, and approaches again slowly to latch the reference. Subsequent motor payout is calculated relative to that reference: Δφ = (L − Lₕₒₘₑ) / Rᵈ, where Rᵈ is the drum radius.

## Overhead guide and keyed rod

The overhead guide lets the rod slide axially and tilt about two axes while constraining axial spin. This keeps the wrist orientation tied to a defined rod frame. Inverse kinematics accounts for the offsets between the cable collar, both wrist joints, and the tool tip, so a requested tip position is not treated as the collar position.

The timber frame carries the winches and guide as one connected structure. Braces and cross rails provide a practical assembly from standard stock, while the measured mount geometry enters the positioning equations. Precision is concentrated in the smaller guides, pulleys, bearings, and wrist joints.

## References and notes

[^diagnostic-access]: Kenneth A. Fleming et al. [“The Lancet Commission on diagnostics: transforming access to diagnostics.”](https://doi.org/10.1016/S0140-6736(21)00673-5) *The Lancet* 398, 1997 to 2050 (2021). The Commission estimates that 47% of the global population has little or no access to diagnostics. This concerns diagnostics overall, including laboratory testing.

[^imaging-access]: World Health Assembly. [*Strengthening medical imaging capacity*, resolution WHA78.13](https://apps.who.int/gb/ebwha/pdf_files/WHA78/A78_R13-en.pdf) (2025), especially paragraphs 1(2), 1(3), 1(5), and 1(7). Calls for sustainable investment in imaging equipment and maintenance, workforce training, access in rural and remote areas, and consideration of operating and maintenance costs before procurement.
