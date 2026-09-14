---
layout: project
title: Smaller models for complex dynamics
permalink: /surrogate-modeling-sindy.html
group: research
order: 1
category: System identification
status: Published research · 2022
description: Learning compact dynamical models for a biodiesel process and watershed streamflow—and testing where those models reach their limits.
summary: Using sparse equations to approximate industrial and natural dynamics, with a close look at interpretability and model limitations.
card_methods: SINDy · Differential equations · ASPEN Dynamics
focus: Reduced-order dynamical models
methods: Sparse regression and constrained optimization
context: Doctoral research, Purdue University
next_url: /hybrid-algae-growth.html
next_title: Learning what a mechanistic model misses
---
## The question

Detailed simulations can be difficult to integrate into a larger system model. Can a small set of learned differential equations retain enough of the dynamics to be useful?

I studied that question in two different settings: a soybean-oil-to-biodiesel process and the North Fork Vermilion River watershed. The contrast makes it possible to examine both the promise and the limits of the same modeling approach.

## The approach

Sparse Identification of Nonlinear Dynamics (SINDy) selects a small set of terms from a candidate function library to describe how a system changes over time. I used simulated process trajectories and watershed data to identify reduced models, then evaluated their behavior against reference trajectories.

For the industrial system, a sequential quadratic programming refinement helped improve the learned model's long-horizon behavior.

{% include figure.html src="/A5.png" alt="Learned biodiesel-process equations and six output trajectories compared with the ASPEN reference" caption="Industrial-system results: the standard and refined sparse models compared with reference trajectories over a 200-hour test." %}

## What the comparison revealed

The process-plant study supported compact models using a linear library. The watershed required nonlinear and history-dependent terms, and its state predictions remained less accurate.

That distinction matters: a successful surrogate for one system is not evidence that the same model class will work equally well for another. Model structure, available measurements, and the dynamics of the system all shape what can be learned.

{% include figure.html src="/A6.png" alt="Watershed surrogate equations and streamflow validation plot" caption="The watershed case exposes a harder modeling problem and the limits of the available surrogate." %}

<details class="figure-details"><summary>Explore the method and system diagrams</summary>
{% include figure.html src="/A1.png" alt="SINDy sparse identification workflow" caption="Sparse identification workflow." %}
{% include figure.html src="/A2.png" alt="Extended SINDy method with input-derivative terms" caption="Extending the candidate terms to represent forced-system dynamics." %}
{% include figure.html src="/A3.png" alt="ASPEN Dynamics biodiesel process flowsheet" caption="The industrial process used as the detailed modeling reference." %}
</details>

<p class="source-note">William Farlessyost and Shweta Singh. “Reduced order dynamical models for complex dynamics in manufacturing and natural systems using machine learning.” <em>Nonlinear Dynamics</em> 110, 1613–1631 (2022). <a href="https://doi.org/10.1007/s11071-022-07695-x">Read the publication</a>.</p>
