---
layout: project
title: Sensor selection
permalink: /sensor-minimization-ltc.html
group: research
research_walkthrough: true
order: 3
category: Sensing & machine learning
status: Research preprint · 2025
description: Neural observers that estimate system states using fewer measurement inputs.
summary: Neural state estimation with fewer measurement inputs, evaluated in mechanical, chemical, and ecological simulations.
card_methods: Liquid-time-constant networks · Observers · Causal analysis
focus: Sensor selection for state estimation
methods: Neural observers and perturbation-based pruning
context: Doctoral research, Purdue University
next_url: /climate-resilience-mfn.html
next_title: Climate resilience modeling
---
## Overview

I developed a method for selecting the measurement inputs a neural observer needs to estimate a system’s state. An observer acts as a soft sensor: it uses the history of available signals to estimate a quantity that is difficult to measure directly. I used liquid-time-constant (LTC) networks to learn those time-dependent relationships.[^paper]

The method trains an observer, perturbs each candidate input, and measures how its predicted trajectory changes. Inputs with little influence are removed, then the observer is retrained and checked against an error target. I applied the method to velocity estimation in a mechanical system, concentration estimation in a reactor, and population estimation in an ecological system.

## Why select the inputs

Every physical measurement adds installation, calibration, maintenance, and data-handling work. In a distributed agricultural or industrial system, measuring every variable may be impractical. The design question is which measurements provide enough information to reconstruct the states needed for monitoring and control.[^dissertation]

Two signals can be strongly correlated yet contribute different information about how a system evolves. I therefore examined the observer’s response to changes in each input over time, then tested the reduced input set through retraining. I used estimation error to decide which signals to collect and which states could be inferred from them.[^dissertation]

{% include research-walkthrough.html project="sensors" %}

<div class="research-equation">
  <p class="equation" aria-label="Delta y hat for input j equals the observer applied to the perturbed input sequence minus the observer applied to the original sequence">Δŷ<sub>j</sub> = F<sub>θ</sub>(u + δe<sub>j</sub>) − F<sub>θ</sub>(u)</p>
  <p><strong>F<sub>θ</sub></strong> is the fitted observer acting on an input sequence <strong>u</strong>. The offset <strong>δe<sub>j</sub></strong> changes only channel <strong>j</strong>. Comparing the resulting output trajectories measures sensitivity within the learned model. Retraining and validation determine whether removing that input is acceptable.</p>
</div>

The perturbations measure sensitivity within the fitted observer; they do not establish physical causality.[^paper]

## My contribution

- Trained observers using the full set of candidate measurements.
- Perturbed inputs to measure their effect on predictions, then removed less useful inputs.
- Evaluated reduced input sets on spring-mass-damper, reactor, and predator-prey simulations.

{% include figure.html src="/C2.png" alt="Mechanical, ecological, and chemical testbeds with candidate measurements" caption="Velocity, concentration, and population estimation test cases." %}

In the mechanical case, the target is velocity. In the chemical case, it is concentration. In the ecological case, it is predator population. These testbeds provide known underlying dynamics, so the estimated states can be checked against simulation ground truth.[^dissertation]

## Results

Smaller input sets met prediction-error targets in the synthetic test cases. Inputs containing only noise could be removed.[^paper] Hardware performance and behavior under real sensor drift have not been evaluated.

The selected set is specific to the trained observer and the data used to evaluate it. A derived feature, such as the product of two measured signals, is also different from a separate physical sensor. Reducing input count therefore does not establish the same reduction in hardware.

{% include figure.html src="/C5.png" alt="Comparison of the full observer and reduced sensor-network designs" caption="Reduced input sets met the prediction-error targets in the test systems." %}

<details class="figure-details"><summary>Method and prediction results</summary>
{% include figure.html src="/C4.png" alt="Iterative perturbation, scoring, and input-pruning algorithm" %}
{% include figure.html src="/C9.png" alt="Mechanical-system state predictions after sensor pruning compared with ground truth" caption="Velocity estimation with the reduced input set." %}
{% include figure.html src="/C10.png" alt="Predator-prey prediction results after sensor pruning" caption="Predator-population estimation with the reduced input set." %}
{% include figure.html src="/C11.png" alt="Chemical concentration predictions after sensor pruning" caption="Concentration estimation with the reduced input set." %}
</details>

## References and notes

[^paper]: William Farlessyost, Sebastian Oberst, and Shweta Singh. [“The power of dynamic causality in observer-based design for soft sensor applications.”](https://arxiv.org/abs/2509.11336) arXiv:2509.11336 (2025), preprint. Source for the perturbation-based pruning procedure and the three simulation testbeds.

[^dissertation]: William Blake Farlessyost. [*Modeling Material Flow Dynamics in Industrial-Natural Systems: Machine Learning and Causal Analysis for Resilience Evaluation and Sensor Minimization.*](https://doi.org/10.25394/PGS.28904861) Ph.D. dissertation, Purdue University (2025), Chapters 1 and 4. Explains the measurement-cost motivation and describes the mechanical, chemical, and ecological state-estimation examples shown in the research presentation.
