---
layout: project
title: NASA Lunabotics
permalink: /projects/lunabotics/
group: build
order: 4
category: Mobile robotics
status: Senior design · 2020
description: Navigation, stereo vision, and ROS integration for a two-robot lunar mining design.
summary: A two-robot mining and hauling design, with camera integration, ROS navigation, and Gazebo simulation.
card_methods: ROS · Stereo vision · Gazebo · Arduino
cover: /assets/images/lunabotics-robots-deployed.jpg
cover_width: 1526
cover_height: 861
cover_alt: CAD designs of the Lunabotics conveyor mining robot and separate dump truck
focus: Robot navigation and software integration
methods: Stereo vision, ROS Kinetic, URDF, Gazebo
context: UNC Asheville / NC State senior design, 2020
next_url: /projects/wheel-of-despair/
next_title: Wheel of Despair
---
## Overview

Our senior-design team designed a two-robot system for NASA's Lunabotics competition: a mining robot to excavate simulated lunar material and a dump truck to carry it to a collection bin. The project connected mechanical design, embedded electronics, perception, and motion control.

**I worked on the navigation and software subteam**, integrating cameras and developing ROS-based navigation for both robots in coordination with the mechanical and electrical teams.

{% include figure.html src="/assets/images/lunabotics-robots-deployed.jpg" alt="CAD view of the conveyor mining robot on the left and the dump truck with a receiving hopper on the right" caption="CAD design of the mining robot and dump truck in their deployed configuration." %}

## Why two robots

The competition task was to navigate an arena with obstacles, excavate material, and deliver it to a collector. Mass, stowed volume, energy use, communication bandwidth, dust protection, and autonomous operation all constrained the design.

Separating excavation from transport was intended to keep the miner working while the dump truck made delivery trips. The design paired a cup conveyor and temporary hopper with a separate hauling robot. Their coordination required navigation, docking, material transfer, and signals to begin the next cycle.

The team designed the pair to fit within a shared 1 × 1 × 0.5 m envelope before deployment.

<details class="figure-details"><summary>See the stowed robot layout</summary>
{% include figure.html src="/assets/images/lunabotics-robots-stowed.jpg" alt="CAD view of the two robots nested together with the mining conveyor folded horizontally" caption="Stowed CAD configuration for the team's 1 × 1 × 0.5 m packaging requirement." %}
</details>

## From perception to wheel commands

The software architecture used **ROS Kinetic on an NVIDIA Jetson TX2**, with Arduino microcontrollers connecting the high-level software to wheel control. ROS nodes and topics provided the interfaces between sensing, planning, and actuation.

### Stereo perception

Stereo cameras provided point clouds representing the space around the robots. These spatial measurements supported obstacle mapping and navigation through the arena.

### Planning a path

ROS navigation packages took obstacle maps, point clouds, odometry, and a destination as inputs. They produced a global route, local paths around newly detected obstacles, and velocity commands through `move_base`. Recovery behaviors addressed situations in which the robot became stuck.

### Turning commands into motion

A ROS controller translated those velocity commands into drive-motor speeds and steering-servo angles for **double-Ackermann steering**. Both front and rear wheels were independently steered, connecting the planned motion to the team's custom wheel assemblies.

{% include figure.html src="/assets/images/lunabotics-test-chassis.jpg" alt="Physical test chassis with a Jetson TX2, Arduino boards, wiring, drive wheels, and steering servos" caption="Test chassis integrating Jetson and Arduino electronics with independently steered wheels." %}

## Simulation and robot coordination

The team converted SolidWorks geometry into a Universal Robot Description Format (URDF) model. Its links and joints described the chassis components and their motion, allowing Gazebo to simulate the test platform.

{% include figure.html src="/assets/images/lunabotics-gazebo.png" alt="Gazebo simulation of the four-wheel test chassis on uneven terrain" caption="Gazebo simulation of the four-wheel test chassis." %}

Separate state-machine designs described the two robots' operating sequences. The miner would locate the mining zone, position itself, deploy the conveyor, and transfer material when the truck docked. The truck would travel to the miner, receive material, return to the collector, and deposit its load before repeating the cycle.

<details class="figure-details"><summary>View the robot state-machine designs</summary>
{% include figure.html src="/assets/images/lunabotics-miner-states.png" alt="Mining sequence: acquire an AR tag, plan and drive to the mining zone, position and deploy the apparatus, continue until the truck docks, empty the hopper, and wait for the truck to disengage" caption="Mining-robot state-machine design." %}
{% include figure.html src="/assets/images/lunabotics-hauler-states.png" alt="Hauling sequence: acquire an AR tag, plan and drive to the miner, dock, wait for the undocking signal, return to the collector, dock and deposit material, then repeat" caption="Dump-truck state-machine design." %}
</details>

## Project outcomes

The project produced paired robot designs, a physical test chassis, a Gazebo model, and a navigation and control architecture. Component testing covered drive motors, steering servos, the mining mechanism, and the truck's lift, including steering tests in a pulverized-limestone bed.

The resulting designs and software established a foundation for future teams to extend. My work connected camera data, motion planning, and embedded control within a shared robotics system.
