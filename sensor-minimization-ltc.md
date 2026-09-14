---
layout: project
title: Sensor selection
permalink: /sensor-minimization-ltc.html
group: research
order: 3
category: Sensing & machine learning
status: Research preprint · 2025
description: Neural observers that estimate system states using fewer measurement inputs.
summary: Reduced measurement inputs while meeting prediction-error targets in mechanical, chemical, and ecological simulations.
card_methods: Liquid-time-constant networks · Observers · Causal analysis
focus: Sensor selection for state estimation
methods: Neural observers and perturbation-based pruning
context: Doctoral research, Purdue University
next_url: /climate-resilience-mfn.html
next_title: Climate resilience modeling
---
## Overview

I studied which measurements a neural observer needs to estimate a system’s state, using liquid-time-constant (LTC) networks.

## My contribution

- Trained observers using the full set of candidate measurements.
- Perturbed inputs to measure their effect on predictions, then removed less useful inputs.
- Evaluated reduced input sets on spring-mass-damper, reactor, and predator-prey simulations.

{% include figure.html src="/C2.png" alt="Mechanical, ecological, and chemical testbeds with candidate measurements" caption="Three different kinds of dynamics provide test cases for the sensor-selection approach." %}

## Results

Smaller input sets met prediction-error targets in the synthetic test cases. Inputs containing only noise could be removed. Hardware performance and behavior under real sensor drift have not been evaluated.

{% include figure.html src="/C5.png" alt="Comparison of the full observer and reduced sensor-network designs" caption="Observer designs before and after input selection." %}

<details class="figure-details"><summary>Method and prediction results</summary>
{% include figure.html src="/C4.png" alt="Iterative perturbation, scoring, and input-pruning algorithm" caption="The input-pruning loop." %}
{% include figure.html src="/C9.png" alt="Mechanical-system state predictions after sensor pruning compared with ground truth" caption="Mechanical-system prediction results using the reduced input set." %}
{% include figure.html src="/C10.png" alt="Predator-prey prediction results after sensor pruning" caption="Ecological-system prediction results." %}
{% include figure.html src="/C11.png" alt="Chemical concentration predictions after sensor pruning" caption="Chemical-system prediction results." %}
</details>

<p class="source-note">Research with Sebastian Oberst and Shweta Singh. <a href="https://arxiv.org/abs/2509.11336">Read the 2025 preprint</a>.</p>
