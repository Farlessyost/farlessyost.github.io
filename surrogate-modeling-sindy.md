---
layout: project
title: Reduced-order modeling
permalink: /surrogate-modeling-sindy.html
group: research
research_walkthrough: true
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

I developed compact dynamical models of biodiesel production and watershed streamflow using Sparse Identification of Nonlinear Dynamics (SINDy). The models learn a small set of differential equations from time-series data, describing how process outputs or streamflow change as inputs vary.[^paper]

The two cases tested the same idea in different settings: an industrial process with well-defined operating conditions, and a natural system whose response depends on weather and past conditions. My work covered equation discovery, coefficient refinement, and comparison of the resulting trajectories with process and watershed data.

## Why this approach

A detailed plant model describes individual reactors, separators, and recycle streams. When the question is how that plant responds to a change in supply, running every unit operation can make a wider network study cumbersome. I wanted to retain the dynamics that matter at the plant boundary in a model small enough to connect to other processes.[^dissertation]

SINDy provides explicit equations whose terms and coefficients can be inspected. That makes it possible to examine which inputs drive a response and where the model misses important behavior. The watershed case tested whether the same approach could capture changing water availability, where the timing and magnitude of streamflow matter as well as its average. This work addressed the process-level dynamics needed for a larger material-flow network.[^dissertation]

{% include research-walkthrough.html project="sindy" %}

<div class="research-equation">
  <p class="equation" aria-label="X dot is approximately Theta of X, U, and U dot, multiplied by Xi">Ẋ ≈ Θ(X, U, U̇) Ξ</p>
  <p><strong>X</strong> contains the recorded states, <strong>U</strong> the inputs, and <strong>Θ</strong> the candidate functions. Sparse regression leaves relatively few nonzero coefficients in <strong>Ξ</strong>. I also tested input derivatives, <strong>U̇</strong>, in the watershed model to help represent the response to changing weather inputs.</p>
</div>

Selecting an equation structure and fitting its coefficients are separate problems. After SINDy selected the industrial model’s terms, I refined the coefficients with constrained nonlinear optimization. The objective was to reduce error in the integrated trajectory, where small rate errors can accumulate.[^paper]

## My contribution

- Identified differential equations from process simulations and watershed data.
- Refined the industrial model with constrained optimization.
- Compared predictions with reference trajectories, including a 200-hour process test.

{% include figure.html src="/A5.png" alt="Learned biodiesel-process equations and six output trajectories compared with the ASPEN reference" caption="200-hour industrial-model test against the ASPEN reference." %}

## Results

The industrial model captured process dynamics with a small set of equations. Watershed predictions were less accurate and required nonlinear, history-dependent terms.[^paper]

Rainfall alone does not describe a watershed’s condition: the same storm can produce different runoff after a drought or after several wet days. Adding input derivatives helped represent changing conditions, but did not fully recover the high and low streamflow extremes.[^dissertation]

{% include figure.html src="/A6.png" alt="Watershed surrogate equations and streamflow validation plot" caption="The model recovered seasonal behavior more accurately than streamflow extremes." %}

<details class="figure-details"><summary>Method and system diagrams</summary>
{% include figure.html src="/A1.png" alt="SINDy sparse identification workflow" %}
{% include figure.html src="/A2.png" alt="Extended SINDy method with input-derivative terms" caption="Input derivatives add information about changing forcing." %}
{% include figure.html src="/A3.png" alt="ASPEN Dynamics biodiesel process flowsheet" caption="ASPEN Dynamics biodiesel reference model." %}
</details>

## References and notes

[^paper]: William Farlessyost and Shweta Singh. [“Reduced order dynamical models for complex dynamics in manufacturing and natural systems using machine learning.”](https://doi.org/10.1007/s11071-022-07695-x) *Nonlinear Dynamics* 110, 1613 to 1631 (2022). Source for the methods and results summarized on this page.

[^dissertation]: William Blake Farlessyost. [*Modeling Material Flow Dynamics in Industrial-Natural Systems: Machine Learning and Causal Analysis for Resilience Evaluation and Sensor Minimization.*](https://doi.org/10.25394/PGS.28904861) Ph.D. dissertation, Purdue University (2025), Chapters 1 and 2. Covers the research motivation and includes the function libraries, coefficient refinement, and industrial and watershed validation.
