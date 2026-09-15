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

I used Sparse Identification of Nonlinear Dynamics (SINDy) to build compact models of biodiesel production and watershed streamflow.[^paper]

## Why this approach

A detailed process model is useful for studying a plant, but cumbersome to run as one part of a larger production network. I wanted a smaller model that still captured how outputs respond over time. SINDy makes that model explicit: a set of differential equations whose terms and coefficients can be inspected.

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

{% include figure.html src="/A5.png" alt="Learned biodiesel-process equations and six output trajectories compared with the ASPEN reference" caption="Industrial-system results: the standard and refined sparse models compared with reference trajectories over a 200-hour test." %}

## Results

The industrial model captured process dynamics with a small set of equations. Watershed predictions were less accurate and required nonlinear, history-dependent terms.[^paper]

The difference matters. Rainfall alone does not describe a watershed’s condition: the same storm can produce different runoff after a drought or after several wet days. Adding input derivatives helped represent changing conditions, but did not fully recover the high and low streamflow extremes.[^dissertation]

{% include figure.html src="/A6.png" alt="Watershed surrogate equations and streamflow validation plot" caption="Streamflow validation: compare the timing and height of predicted peaks with the reference curve. Seasonal behavior is easier to recover than the extremes." %}

<details class="figure-details"><summary>Method and system diagrams</summary>
{% include figure.html src="/A1.png" alt="SINDy sparse identification workflow" caption="Sparse identification workflow." %}
{% include figure.html src="/A2.png" alt="Extended SINDy method with input-derivative terms" caption="Extending the candidate terms to represent forced-system dynamics." %}
{% include figure.html src="/A3.png" alt="ASPEN Dynamics biodiesel process flowsheet" caption="The industrial process used as the detailed modeling reference." %}
</details>

## References and notes

[^paper]: William Farlessyost and Shweta Singh. [“Reduced order dynamical models for complex dynamics in manufacturing and natural systems using machine learning.”](https://doi.org/10.1007/s11071-022-07695-x) *Nonlinear Dynamics* 110, 1613 to 1631 (2022). Source for the methods and results summarized on this page.

[^dissertation]: William Blake Farlessyost. [*Modeling Material Flow Dynamics in Industrial-Natural Systems: Machine Learning and Causal Analysis for Resilience Evaluation and Sensor Minimization.*](https://doi.org/10.25394/PGS.28904861) Ph.D. dissertation, Purdue University (2025), Chapter 2. Includes the function libraries, coefficient refinement, and industrial and watershed validation.
