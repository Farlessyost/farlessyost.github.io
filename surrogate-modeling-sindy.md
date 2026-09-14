---
layout: project
title: Reduced-order modeling
permalink: /surrogate-modeling-sindy.html
group: research
order: 1
category: System identification
status: Published research · 2022
description: Compact dynamical models for a biodiesel process and watershed streamflow.
summary: Built sparse equation models and evaluated their accuracy against process simulations and watershed data.
card_methods: SINDy · Differential equations · ASPEN Dynamics
focus: Reduced-order dynamical models
methods: Sparse regression and constrained optimization
context: Doctoral research, Purdue University
next_url: /hybrid-algae-growth.html
next_title: Hybrid algae-growth modeling
---
## Overview

I used Sparse Identification of Nonlinear Dynamics (SINDy) to build compact models of biodiesel production and watershed streamflow.

## My contribution

- Identified differential equations from process simulations and watershed data.
- Refined the industrial model with constrained optimization.
- Compared predictions with reference trajectories, including a 200-hour process test.

{% include figure.html src="/A5.png" alt="Learned biodiesel-process equations and six output trajectories compared with the ASPEN reference" caption="Industrial-system results: the standard and refined sparse models compared with reference trajectories over a 200-hour test." %}

## Results

The industrial model captured process dynamics with a small set of equations. Watershed predictions were less accurate and required nonlinear, history-dependent terms.

{% include figure.html src="/A6.png" alt="Watershed surrogate equations and streamflow validation plot" caption="The watershed case exposes a harder modeling problem and the limits of the available surrogate." %}

<details class="figure-details"><summary>Method and system diagrams</summary>
{% include figure.html src="/A1.png" alt="SINDy sparse identification workflow" caption="Sparse identification workflow." %}
{% include figure.html src="/A2.png" alt="Extended SINDy method with input-derivative terms" caption="Extending the candidate terms to represent forced-system dynamics." %}
{% include figure.html src="/A3.png" alt="ASPEN Dynamics biodiesel process flowsheet" caption="The industrial process used as the detailed modeling reference." %}
</details>

<p class="source-note">William Farlessyost and Shweta Singh. “Reduced order dynamical models for complex dynamics in manufacturing and natural systems using machine learning.” <em>Nonlinear Dynamics</em> 110, 1613 to 1631 (2022). <a href="https://doi.org/10.1007/s11071-022-07695-x">Read the publication</a>.</p>
