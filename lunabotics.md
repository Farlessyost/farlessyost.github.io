---
layout: project
title: NASA Lunabotics
permalink: /projects/lunabotics/
group: build
order: 4
category: Mobile robotics
status: Senior design · 2020
description: I developed the ROS software, computer vision, navigation, and motion control for a two-robot lunar mining design.
summary: I developed the ROS software, computer vision, and motion control for a two-robot mining and hauling system.
card_methods: ROS · Stereo vision · Gazebo · Arduino
cover: /assets/images/lunabotics-robots-deployed.jpg
cover_width: 1526
cover_height: 861
cover_alt: CAD designs of the Lunabotics conveyor mining robot and separate dump truck
focus: ROS, computer vision, navigation, and control
methods: Stereo vision, ROS Kinetic, motion control, URDF, Gazebo
context: UNC Asheville / NC State senior design, 2020
next_url: /projects/wheel-of-despair/
next_title: Wheel of Despair
---
## Overview

Our senior-design team designed a two-robot system for NASA's Lunabotics competition: a mining robot to excavate simulated lunar material and a dump truck to carry it to a collection bin. The project connected mechanical design, embedded electronics, perception, and motion control.

**I was responsible for all ROS development, computer vision, navigation, and motion control for both robots.** I integrated the stereo cameras, configured the navigation stack, and developed the controllers that translated planned motion into wheel speeds and steering angles, working with the mechanical and electrical teams to connect the software to the hardware.

{% include figure.html src="/assets/images/lunabotics-robots-deployed.jpg" alt="CAD view of the conveyor mining robot on the left and the dump truck with a receiving hopper on the right" caption="CAD design of the mining robot and dump truck in their deployed configuration." %}

## Why two robots

The competition task was to navigate an arena with obstacles, excavate material, and deliver it to a collector. Mass, stowed volume, energy use, communication bandwidth, dust protection, and autonomous operation all constrained the design.

Separating excavation from transport was intended to keep the miner working while the dump truck made delivery trips. The design paired a cup conveyor and temporary hopper with a separate hauling robot. Their coordination required navigation, docking, material transfer, and signals to begin the next cycle.

The team designed the pair to fit within a shared 1 × 1 × 0.5 m envelope before deployment.

<details class="figure-details"><summary>See the stowed robot layout</summary>
{% include figure.html src="/assets/images/lunabotics-robots-stowed.jpg" alt="CAD view of the two robots nested together with the mining conveyor folded horizontally" caption="Stowed CAD configuration for the team's 1 × 1 × 0.5 m packaging requirement." %}
</details>

## From perception to wheel commands

I built the software architecture around **ROS Kinetic on an NVIDIA Jetson TX2**, with Arduino microcontrollers connecting the high-level software to wheel control. I used ROS nodes and topics to connect sensing, planning, and actuation across both robots.

### Stereo perception

I integrated the stereo cameras and computer-vision processing to provide point clouds representing the space around the robots. These spatial measurements supported obstacle mapping and navigation through the arena.

### Planning a path

I configured the ROS navigation stack to use obstacle maps, point clouds, odometry, and a destination to plan motion. The stack produced a global route, local paths around newly detected obstacles, and velocity commands through `move_base`, with recovery behaviors for situations in which the robot became stuck.

### Turning commands into motion

I developed the ROS controller that translated those velocity commands into drive-motor speeds and steering-servo angles for **double-Ackermann steering**. Both front and rear wheels were independently steered, connecting my navigation and control software to the team's custom wheel assemblies.

{% include figure.html src="/assets/images/lunabotics-test-chassis.jpg" alt="Physical test chassis with a Jetson TX2, Arduino boards, wiring, drive wheels, and steering servos" caption="Test chassis integrating Jetson and Arduino electronics with independently steered wheels." %}

## Simulation and robot coordination

I brought the team's SolidWorks geometry into a Universal Robot Description Format (URDF) model for Gazebo simulation. Its links and joints described the chassis components and their motion, connecting the mechanical design to the software test platform.

{% include figure.html src="/assets/images/lunabotics-gazebo.png" alt="Gazebo simulation of the four-wheel test chassis on uneven terrain" caption="Gazebo simulation of the four-wheel test chassis." %}

I designed separate state machines to coordinate the two robots' operating sequences. The miner would locate the mining zone, position itself, deploy the conveyor, and transfer material when the truck docked. The truck would travel to the miner, receive material, return to the collector, and deposit its load before repeating the cycle.

<details class="figure-details"><summary>View the robot state-machine designs</summary>
{% include figure.html src="/assets/images/lunabotics-miner-states.png" alt="Mining sequence: acquire an AR tag, plan and drive to the mining zone, position and deploy the apparatus, continue until the truck docks, empty the hopper, and wait for the truck to disengage" caption="Mining-robot state-machine design." %}
{% include figure.html src="/assets/images/lunabotics-hauler-states.png" alt="Hauling sequence: acquire an AR tag, plan and drive to the miner, dock, wait for the undocking signal, return to the collector, dock and deposit material, then repeat" caption="Dump-truck state-machine design." %}
</details>

## Project outcomes

The project produced paired robot designs, a physical test chassis, a Gazebo model, and a navigation and control architecture. Component testing covered drive motors, steering servos, the mining mechanism, and the truck's lift, including steering tests in a pulverized-limestone bed.

My contribution covered the complete software path from stereo-camera data through navigation to wheel control, along with the Gazebo model and robot-coordination logic. This connected the team's mechanical and electrical designs into a shared robotics system.
