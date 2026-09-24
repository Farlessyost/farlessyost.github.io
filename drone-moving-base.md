---
layout: project
title: Drone landing on a moving base
permalink: /projects/drone-moving-base/
group: build
order: 6
category: Aerial & ground robotics
status: Research project
description: ROS and Simulink integration toward landing a Parrot Mambo drone on a moving Clearpath Jackal.
summary: Connected visual pose data from a ground robot to a drone control framework as a foundation for tracking and landing on a moving platform.
card_methods: ROS · Simulink · AR tags · Flight control
cover: /assets/images/drone-moving-base-platform.jpg
cover_width: 1600
cover_height: 1200
cover_alt: Parrot Mambo flying above a Clearpath Jackal with a stereo camera in the laboratory
focus: Relative localization and robot integration
methods: Fiducial tracking, ROS communication, Simulink control
context: JEM 473 project, UNC Asheville
next_url: /climate-resilience-mfn.html
next_title: Climate resilience modeling
---
## Overview

Landing on a moving platform requires a drone to follow a destination that keeps changing position. I worked on a team developing a system for a **Parrot Mambo quadcopter** and a **Clearpath Jackal ground robot**, with a stereo camera on the Jackal observing a marker on the drone.

The project connected visual localization, ROS communication, and Simulink flight control. Its goal was to keep the drone aligned with the moving robot and support an eventual landing on the platform.

{% include figure.html src="/assets/images/drone-moving-base-platform.jpg" alt="Parrot Mambo in flight above a Clearpath Jackal ground robot with a front-mounted stereo camera in a laboratory" caption="Parrot Mambo in flight above the Clearpath Jackal test platform." %}

## Robot and software architecture

The Jackal provided the moving base, with a ZED stereo camera, an inertial measurement unit, and wheel encoders. ROS supported the ground robot's motor control and the processing of visual markers. The Mambo supplied the aerial platform and an existing Simulink flight-control framework.

The system connected ROS on the Jackal to a local ROS environment and then to Simulink. This made the marker pose available alongside the drone's inertial data, linking the ground robot's view of the drone to the software used for flight control.

{% include figure.html src="/assets/images/drone-moving-base-architecture.png" alt="System diagram linking ROS on the Jackal to local ROS, AR-tag pose to local Simulink, and the Mambo's deployed Simulink model to motor commands and IMU data" caption="System architecture connecting the ground robot, local processing, and drone control." %}

## Relative localization

An **AR tag on the underside of the drone** served as a visual reference. Its known geometry allowed the camera system to estimate the tag's position and orientation relative to the observing camera. The localization design brought this visual reference together with the drone's inertial measurements.

Simulink subscribed to `/zed/ar_pose_marker` and extracted position and orientation from the marker message. The processing blocks converted quaternion orientation into ZYX angles, giving the flight-control model separate position and orientation inputs.

{% include figure.html src="/assets/images/drone-moving-base-ros.png" alt="Simulink ROS subscriber for the AR pose marker topic, with branches extracting position and converting quaternion orientation to ZYX angles" caption="ROS pose messages converted into position and orientation signals in Simulink." %}

## Configurable ground-robot motion

The Jackal's path was parameterized as a sequence of figure eights. Radius, completion time, and iteration count defined the trajectory, making the ground robot's motion configurable for tracking tests.

<details class="figure-details"><summary>View the ground-robot path</summary>
{% include figure.html src="/assets/images/drone-moving-base-path.png" alt="Paired circular loops with arrows indicating the Jackal's figure-eight path directions" caption="Figure-eight paths defined by radius, completion time, and iteration count." %}
</details>

## Flight-control integration

We integrated AR-tag pose information into an **existing drone control framework**. The Simulink model accepted ROS position and orientation inputs alongside reference commands, sensor measurements, and image-processing data.

The framework included separate attitude, altitude, and yaw controllers. Roll and pitch control used proportional and integral terms with angular-rate feedback. A control mixer mapped requested thrust and body torques to individual motor thrust commands.

{% include figure.html src="/assets/images/drone-moving-base-flight-control.png" alt="Top-level flight-control diagram receiving reference commands, sensors, image data, ROS position, and ROS orientation, and producing motor commands" caption="ROS position and orientation inputs in the Simulink flight-control framework." %}

<details class="figure-details"><summary>View the attitude controller and motor mixer</summary>
{% include figure.html src="/assets/images/drone-moving-base-attitude.png" alt="Roll and pitch controller with attitude error, proportional and integral branches, angular-rate feedback, and pitch and roll torque outputs" caption="Roll and pitch control with attitude-error and angular-rate feedback." %}
{% include figure.html src="/assets/images/drone-moving-base-mixer.png" alt="Control mixer combining total thrust and yaw, pitch, and roll torques through a matrix multiplication to produce per-motor thrust commands" caption="The control mixer translates thrust and torque requests into individual motor commands." %}
</details>

## Project outcomes

The project established the main interfaces between the two robots:

- Set up the Clearpath Jackal ROS environment.
- Parameterized the ground robot's path.
- Read AR-tag pose messages from ROS into Simulink.
- Incorporated the pose into the existing drone Simulink framework.

This integration provided a foundation for coordinated ground and aerial robotics. The next stage was closed-loop validation using AR-tag pose, gain tuning, and landing trials.
