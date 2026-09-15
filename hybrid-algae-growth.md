---
layout: project
title: Hybrid algae-growth modeling
permalink: /hybrid-algae-growth.html
group: research
order: 2
category: Scientific machine learning
status: Conference proceedings · 2024
description: Improved algae-growth predictions by adding a learned correction to a mechanistic model.
summary: Used machine learning to correct an algae-growth model while keeping temperature, light, and pH explicit.
card_methods: Hybrid modeling · SINDy · Biological dynamics
focus: Chlorella vulgaris growth
methods: Mechanistic modeling and sparse residual dynamics
context: Doctoral research, Purdue University
next_url: /sensor-minimization-ltc.html
next_title: Sensor selection
---
## Overview

I combined a mechanistic model of *Chlorella vulgaris* growth with a learned correction for missing dynamics.[^paper]

## My contribution

- Calculated errors between model predictions and measured growth.
- Used SINDy to learn error dynamics from temperature, light, and pH.
- Evaluated the corrected model with sequential cross-validation.

{% include figure.html src="/B1.png" alt="Four-step hybrid modeling workflow from mechanistic prediction through error dynamics to corrected prediction" caption="The hybrid workflow: fit the mechanistic model, calculate its error, learn error dynamics, and update the prediction." %}

## Results

The corrected predictions followed measured growth more closely in the validation examples.[^paper] The evaluation used one cultivation batch; performance across other strains and reactors remains untested.

{% include figure.html src="/B6.png" alt="Observed, original, and corrected algae growth curves alongside the learned error equation" caption="Validation examples compare the original mechanistic predictions with the corrected model and observations." %}

<details class="figure-details"><summary>Experiment and model details</summary>
{% include figure.html src="/B3.png" alt="Photobioreactor used to collect the algae growth measurements" caption="The 60-liter photobioreactor used for data collection." %}
{% include figure.html src="/B4.png" alt="SINDy correction driven by temperature, light, and pH" caption="The physical drivers used to learn error dynamics." %}
</details>

## References and notes

[^paper]: William Farlessyost and Shweta Singh. [“Improving Mechanistic Model Accuracy with Machine Learning Informed Physics.”](https://doi.org/10.69997/sct.121371) *Systems and Control Transactions* 3, 275 to 282, FOCAPD (2024). Source for the hybrid model, growth measurements, and validation results.
