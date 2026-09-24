---
layout: project
title: TetherXYZ
permalink: /projects/tetherxyz/
group: build
order: 1
category: Robotics & control
status: In development
description: Cable-driven positioning for medical scanning, designed for local fabrication and repair.
summary: Cable-driven positioning for medical scanning, with independently placed winches and a frame designed for local fabrication and repair.
card_methods: MuJoCo · ROS 2 · ESP32 · FreeCAD
cover: /assets/images/tetherxyz-laser-stereo.png
cover_poster: /assets/images/tetherxyz-laser-stereo.png
cover_alt: TetherXYZ laser and stereo scan with a reconstructed surface
focus: Medical-scanner positioning
methods: Kinematics, simulation, firmware, mechanical CAD
context: Independent engineering project
next_url: /projects/peepin-on-papaw/
next_title: Peepin on Papaw
---
## Overview

TetherXYZ uses four cables to position a carriage and a two-axis wrist to orient the scanning tool. I’m developing the mechanism and embedded controls for a medical-scanning platform that can be made and maintained locally.

**The winches can be positioned independently around the working area.** They do not need matching heights, equal spacing, or a perfectly square frame. Their installed positions and angles become inputs to the inverse-kinematics model, allowing the layout to fit the available structure and space.

The uneven mounting in the homing test is deliberate. The same inverse-kinematics model handles different winch heights and tilts by using their measured positions. The current reinforced frame uses a regular layout to simplify its bracing and mounting hardware.

## Why I’m building it

Access to diagnostics is still limited in much of the world. The 2021 Lancet Commission on diagnostics estimated that **47% of the global population** had little or no access to diagnostics.[^diagnostic-access] For medical imaging specifically, the World Health Assembly’s 2025 resolution calls for affordable equipment, better access in rural and remote areas, and sustained investment in maintenance and trained staff.[^imaging-access]

I’m tackling one part of that problem: the mechanical platform that moves and orients a scanning tool. The aim is to reduce reliance on precision rails, custom-machined frames, and replacement parts that may be difficult to obtain. A frame made from local stock and smaller parts that can be printed or fabricated nearby could make the machine easier to build, repair, and adapt.

## Why this design

The larger structure can use wood or other readily available stock. Smaller parts can be 3D printed or fabricated locally, then fitted with standard motors, bearings, and electronics.

Cable-anchor measurements and cable-length calibration give the inverse-kinematics model the geometry of the assembled machine. That reduces dependence on building every frame member to an exact nominal dimension.

Flexible winch placement makes it easier to build around locally available materials and leave room for the patient, tool, and operator. Mount locations are chosen to give the cables clear paths and maintain tension throughout the intended workspace. When a winch is relocated, its position and orientation are updated in the model and its cable reference is re-established through homing.

Cable stretch, backlash, and frame deflection contribute to positioning error. The design concentrates the critical fits in smaller parts that can be fabricated, checked, and replaced locally.

## Motion and surface tracking {#simulation-demo}

To demonstrate flexible placement, this homing sequence uses deliberately uneven winch mounts on the timber frame. Their cable feed heights are 440, 480, 510, and 470 mm, with mounting tilts of −6°, +5°, +7°, and −4°. Those differences are inputs to the positioning equations. Each pulley head swivels to follow its cable while the motor and backplate stay fixed.

<figure class="project-video">
  <video controls playsinline preload="none" width="960" height="640" poster="{{ '/assets/images/tetherxyz-current-motion.png' | relative_url }}" aria-label="TetherXYZ homing and surface-tracking simulation">
    <source src="{{ '/assets/videos/tetherxyz-current-motion.mp4' | relative_url }}" type="video/mp4">
  </video>
  <figcaption>Homing at four times playback speed, followed by surface tracking at 24 times speed. <a href="{{ '/assets/videos/tetherxyz-current-motion.mp4' | relative_url }}">Open video</a></figcaption>
</figure>

## Laser-line surface scanning {#laser-stereo-scan}

The laser gives both cameras a clear line to follow on a surface that may have little natural texture. As the head moves, stereo vision measures the line in three dimensions and builds a surface mesh. This gives TetherXYZ a way to measure surface shape without touching it, using a compact camera pair and line projector carried by the same positioning system.

The cameras sit 30 mm apart. The laser sits on their centerline, with its aperture 24 mm behind the lens plane. Its beam passes through the gap between the camera boards and a slot in the reinforced saddle. Eleven overlapping sweeps, spaced 7 mm apart, carry the line across the forearm at 6 mm/s. The swivel pulleys have an 18 mm pitch radius.

<figure class="project-video">
  <video controls playsinline preload="none" width="1560" height="980" poster="{{ '/assets/images/tetherxyz-laser-stereo.png' | relative_url }}?v=structural" aria-label="TetherXYZ laser-line and stereo simulation with two camera views and a reconstructed surface">
    <source src="{{ '/assets/videos/tetherxyz-laser-stereo.mp4' | relative_url }}?v=structural" type="video/mp4">
    <p><a href="{{ '/assets/videos/tetherxyz-laser-stereo.mp4' | relative_url }}?v=structural">Watch the laser and stereo scan.</a></p>
  </video>
  <figcaption>Three times playback speed. The modeled raised area is 10 mm high; color measures height above the smooth reference surface. <a href="{{ '/assets/videos/tetherxyz-laser-stereo.mp4' | relative_url }}?v=structural">Open video</a></figcaption>
</figure>

For rectified stereo images, depth follows **Z = fB/d**, where **f** is focal length in pixels, **B** is the camera baseline, and **d** is the horizontal disparity between corresponding image points. The laser supplies the visible stripe; the two camera views supply the disparity. The head pose then transforms each reconstructed point into the robot’s coordinate system.

The camera model uses 640 × 480 images and samples the stripe at 30 Hz. Observations accumulate in 1 mm surface bins, and nearby samples form a triangular mesh. Overlapping sweeps help fill the steep sides of the raised area.

{% include turntable-controls.html %}

## Assembly details {#assembly-details}

{% include figure.html src="/assets/images/tetherxyz-assembly-grid.gif" poster="/assets/images/tetherxyz-assembly-grid.png" width="1280" height="1280" alt="Two by two grid of the winch, two-DOF arm, rod and guide, and stereo laser module rotating and exploding apart" caption="One winch design serves all four cable anchors." %}

| Assembly | What it does and why |
| --- | --- |
| Winch | Converts motor rotation into cable payout. Bearings support the drive shaft, while the passive swivel and grooved sheave align the outgoing cable with the carriage. |
| Two-DOF arm | Controls pitch and roll to orient the scanning head. Tendon-driven capstans and bearing-supported drums carry the tendon loads without putting them directly on the servo shafts. |
| Rod and guide | Allow axial travel and two-axis tilt while constraining spin. The nested guide axes let the carriage move while maintaining a defined orientation for the arm. |
| Stereo/laser module | Holds the cameras at a 30 mm baseline and locates the laser between them. The reinforced saddle and retaining bar maintain the optical arrangement while leaving a clear path for the projected line. |

[Watch the grid as a video]({{ '/assets/videos/tetherxyz-assembly-grid.mp4' | relative_url }}).

## Explore the math {#kinematics}

The calculations use measured mount coordinates and orientations. Homing establishes each cable’s length reference. Moving a mount changes the required cable lengths even when the tool follows the same path.

{% include tetherxyz-math.html %}

## My work

- **Mechanical design:** FreeCAD assembly with a timber frame, keyed guide, two-servo wrist, and stereo-camera mount.
- **Simulation:** Native-CAD motion playback, MuJoCo, pulley-aware inverse kinematics, homing sequences, and surface tracking. The current system integrates ROS 2 for Cartesian target commands.
- **Controls:** ESP32-C3 firmware with motor-driver interfaces, acceleration limits, arming logic, and a watchdog.
- **Verification:** CAD interference checks, fit gauges, load calculations, and trajectory studies.

## Cable positioning

Four motor-driven cables position the carriage with three translational degrees of freedom, expressed in Cartesian coordinates (x, y, z). Inverse kinematics maps a target carriage position to cable lengths. Because cables only pull, tension allocation must satisfy force equilibrium with positive cable tensions. The wrist adds two rotational degrees of freedom to orient the tool for scanning or marking.

## Tool wrist

Two servos control pitch and roll about orthogonal axes, giving the wrist two rotational degrees of freedom. Each drives an antagonistic tendon pair: one tendon pulls while the other pays out. The drum radii set the transmission ratio between servo rotation and joint rotation. Bearing-supported joints carry the tool holder and stereo-camera mount, setting their orientation relative to the working surface.

Local pitch and roll control lets the tool follow changes in the surface normal without requiring the entire carriage to rotate. Independently supported capstans carry tendon loads through bearings, reducing radial loading on the servo shafts.


## Swivel winches and cable homing

The motor and drum stay on a fixed backplate. A passive swivel head aligns the pulley with the outgoing cable, reducing side loading as the carriage moves. Each module bolts to the timber frame; the model uses its installed position and orientation directly.

Cable length is the sum of the incoming segment, the pulley arc, and the outgoing tangent span. Treating the pulley as a point would miss the change in wrap as the tool moves. Both the wrap angle θ and swivel angle ψ vary with carriage position.

During homing, a fixed bead approaches its receiver, trips the switch, backs off, and approaches again slowly to latch the reference. Subsequent motor payout is calculated relative to that reference: Δφ = (L − Lₕₒₘₑ) / Rᵈ, where Rᵈ is the drum radius.

## Overhead guide and keyed rod

The overhead guide lets the rod slide axially and tilt about two axes while constraining axial spin. This keeps the wrist orientation tied to a defined rod frame. Inverse kinematics accounts for the offsets between the cable collar, both wrist joints, and the tool tip, so a requested tip position is not treated as the collar position.

The timber braces and cross rails carry the winches and overhead guide. Critical fits stay in the smaller pulleys, bearings, and joints, where parts are easier to fabricate and replace.

## References and notes

[^diagnostic-access]: Kenneth A. Fleming et al. [“The Lancet Commission on diagnostics: transforming access to diagnostics.”](https://doi.org/10.1016/S0140-6736(21)00673-5) *The Lancet* 398, 1997 to 2050 (2021). The Commission estimates that 47% of the global population has little or no access to diagnostics. This concerns diagnostics overall, including laboratory testing.

[^imaging-access]: World Health Assembly. [*Strengthening medical imaging capacity*, resolution WHA78.13](https://apps.who.int/gb/ebwha/pdf_files/WHA78/A78_R13-en.pdf) (2025), especially paragraphs 1(2), 1(3), 1(5), and 1(7). Calls for sustainable investment in imaging equipment and maintenance, workforce training, access in rural and remote areas, and consideration of operating and maintenance costs before procurement.
