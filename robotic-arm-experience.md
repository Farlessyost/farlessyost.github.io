---
layout: project
title: Robotic arm experience
permalink: /projects/robotic-arm-experience/
group: build
order: 3
category: Robotics
status: Undergraduate research · 2017–2020
description: ROS, Gazebo, and MoveIt integration for two undergraduate research projects in robotic manipulation.
summary: Brought a UR3e arm with an RG2 gripper into operation and integrated a Jenga robot with simulation and motion planning.
card_methods: ROS · Gazebo · MoveIt · Arm & gripper integration
cover: /assets/images/ur3e-rg2-simulation.jpg
cover_width: 1280
cover_height: 720
cover_alt: Gazebo simulation of a UR3e arm carrying an orange ball with an RG2-style gripper above a workbench
focus: Robot setup, simulation, and motion planning
methods: ROS, Gazebo, MoveIt, URDF, joint controllers
context: Two undergraduate research projects at UNC Asheville
next_url: /projects/lunabotics/
next_title: NASA Lunabotics
---
## My role

At UNC Asheville, I worked on two research platforms for robotic manipulation: a [UR3e arm with an RG2 gripper](#ur3e-rg2) and a [Jenga robot](#jenga-robot). **For both projects, I was responsible for ROS integration, Gazebo simulation, and MoveIt motion planning.** I connected robot models, control interfaces, and planning software so the arms and grippers could support manipulation experiments. The research teams developed the learning algorithms.

## UR3e arm and RG2 gripper
{: #ur3e-rg2 }

*Undergraduate research · August 2019–May 2020*

This project used a **Universal Robots UR3e arm with an RG2 gripper** as a platform for object sorting. The broader research investigated apprenticeship learning for sorting previously unseen objects. My work brought the arm and gripper into operation and integrated the software needed to command, plan, and simulate manipulation.

### Integration work

The arm and gripper needed a consistent robot description, joint configuration, and command interface. I integrated the RG2 into the ROS workflow and worked through gripper-controller, joint-transmission, and collision-model issues so it could operate alongside the arm.

- **ROS:** connected arm and gripper commands, joint state feedback, and launch configurations.
- **Gazebo:** integrated robot geometry, joints, collision models, and simulated controllers for testing manipulation.
- **MoveIt:** connected the robot model, kinematics, planning configuration, and controllers used to execute arm motions.

### Ball pickup and release

<figure class="project-video">
  <video controls playsinline preload="none" width="1280" height="720" poster="{{ '/assets/images/ur3e-rg2-simulation.jpg' | relative_url }}" aria-label="UR3e and RG2 Gazebo demonstration: pick up a ball, carry it to a tray, and release it" aria-describedby="ur3e-video-caption">
    <source src="{{ '/assets/videos/ur3e-rg2-ball-pick-and-drop.mp4' | relative_url }}" type="video/mp4">
    <p><a href="{{ '/assets/videos/ur3e-rg2-ball-pick-and-drop.mp4' | relative_url }}">Watch the UR3e ball pickup and release video</a>.</p>
  </video>
  <figcaption id="ur3e-video-caption">The UR3e grasps the ball, lifts it from the blue pad, and releases it into the green tray.</figcaption>
</figure>

## Jenga robot
{: #jenga-robot }

*Undergraduate research · September 2017–May 2019*

The Jenga robot used block manipulation as a platform for reinforcement-learning research. Its mechanical arrangement placed an **inverted WidowX arm on a turntable above a building platform**, with a gripper for handling individual blocks. My work connected the robot's models and control interfaces to ROS, Gazebo, and MoveIt for planning and executing manipulation.

### Integration work

The platform combined the arm, gripper, and turntable within one manipulation system. I worked on the interfaces between its robot description, simulated environment, and motion-planning configuration.

- **ROS:** connected block-pose information and the arm, gripper, and turntable control interfaces.
- **MoveIt:** worked on planning configuration, IKFast kinematics, collision objects, and gripper orientation for block handling.
- **Gazebo:** connected the robot model, simulated controllers, and grasp attachment behavior to test pickup and placement sequences.

### Building an orderly block stack

<figure class="project-video">
  <video controls playsinline preload="none" width="1280" height="720" poster="{{ '/assets/images/jenga-robot-simulation.jpg' | relative_url }}" aria-label="Jenga robot Gazebo demonstration: transfer six blocks from a supply stack into two perpendicular three-block layers" aria-describedby="jenga-video-caption">
    <source src="{{ '/assets/videos/jenga-stack-build.mp4' | relative_url }}" type="video/mp4">
    <p><a href="{{ '/assets/videos/jenga-stack-build.mp4' | relative_url }}">Watch the Jenga stack-building video</a>.</p>
  </video>
  <figcaption id="jenga-video-caption">The Jenga robot transfers six blocks from the supply stack to the building platform, placing them in two perpendicular layers of three.</figcaption>
</figure>
