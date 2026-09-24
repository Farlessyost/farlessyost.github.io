---
layout: project
title: Wheel of Despair
permalink: /projects/wheel-of-despair/
group: build
order: 4
category: Feedback control
status: Controls lab project
description: Modeling, simulation, and laboratory testing of a controller for a pneumatically actuated pointer.
summary: Used nonlinear models and laboratory tests to tune a lead-compensator controller for pneumatic positioning.
card_methods: MATLAB · Simulink · Root locus · R
cover: /assets/images/wheel-of-despair-apparatus.png
cover_width: 568
cover_height: 599
cover_alt: Illustration of the Wheel of Despair with a central pointer, pneumatic thrusters, and three target sectors
focus: Angular position control
methods: Nonlinear modeling, root locus, experimental validation
context: MAE 435 final project, NC State University
next_url: /projects/drone-moving-base/
next_title: Drone landing on a moving base
---
## Overview

The Wheel of Despair turns a game of chance into a feedback-control problem. Pneumatic thrusters position a pointer on a board marked with letter grades. Our task was to hold it on an “A” at **100°, 180°, and 260°**, while limiting overshoot, response time, and steady-state error.

I collaborated on modeling the apparatus, designing controllers, and comparing simulation with physical tests. The project combined nonlinear dynamics, actuator modeling, root-locus design, and experimental troubleshooting.

{% include figure.html src="/assets/images/wheel-of-despair-apparatus.png" alt="Illustration of a wheel with three A-grade target sectors, a central pointer, and pneumatic thrusters near the pointer tip" caption="Pneumatic thrust controls the pointer's position at three target sectors." %}

## Modeling the plant

The pointer's motion depended on pneumatic thrust, rotational inertia, bearing friction, and gravity acting through an offset center of mass. With no thrust, gravity pulled the pointer toward its downward equilibrium. Holding another angle required a balancing actuator input as well as feedback to correct disturbances and motion.

The voltage-to-force relationship was also nonlinear. We used supplied experimental data to model the thrusters' steady-state behavior, with regression in R. Recorded free-motion data helped estimate the bearing damping by comparing simulated and measured responses. Simulink combined the actuator model with the pointer dynamics to simulate the nonlinear system.

<details class="figure-details"><summary>View the free-body diagram</summary>
{% include figure.html src="/assets/images/wheel-of-despair-free-body.png" alt="Free-body diagram showing the pointer angle, thrust force, weight, center-of-gravity offset, and distance from the pivot to the thrusters" caption="Free-body diagram used to model the pointer dynamics." %}
</details>

## Designing the controller

We linearized the plant around the three target angles and used MATLAB's `rltool` to examine the root loci. This gave us a way to choose controller poles, zeros, and gains before testing each design against the nonlinear Simulink model.

The final design process produced a lead compensator for each operating point. Reference-dependent voltage offsets supplied the nominal input needed to hold the requested angle; the feedback controller adjusted that input in response to position error. The actuator command was limited to **−10 V to +10 V**.

<details class="figure-details"><summary>View the lead-compensator design</summary>
{% include figure.html src="/assets/images/wheel-of-despair-root-locus.png" alt="MATLAB root-locus plot and linearized step response for the lead-compensated model at 180 degrees" caption="Root-locus design and simulated step response around the 180° operating point." %}
</details>

## Refining the controller through hardware tests

Our first high-gain controller looked promising in simulation, but produced sustained oscillation on the physical apparatus. The voltage trace revealed rapid switching between the two saturation limits. The initial simulation assumed an instantaneous force response and missed the effect of pneumatic delay.

We added a delay approximation to the nonlinear model and used further hardware tests to refine the controller. Lower-gain lead compensators improved the physical response.

The controller designed about **180°** gave the preferred laboratory response:

<div class="callout">
  <p><strong>C(s) = 1000 · (s + 1.75) / (s + 100)</strong></p>
  <p>This lead compensator was designed for the linearized model about 180°, then evaluated in nonlinear simulation and on the physical apparatus.</p>
</div>

## Results and lessons

The final controller produced a measured response that resembled the simulation in rise behavior and minimal overshoot. Performance depended on the operating point, with the strongest agreement around **180°**.

{% include figure.html src="/assets/images/wheel-of-despair-response.png" alt="Reference, measured, and simulated angle traces on the left; measured and simulated actuator voltage traces on the right" caption="Measured and simulated responses at 100°, 180°, and 260° position targets, with the corresponding actuator voltage." %}

The main lesson was to **compare actuator commands as well as position**. Inspecting the voltage traces made saturation and pneumatic delay visible during tuning, connecting controller design to the limits of the physical system.
