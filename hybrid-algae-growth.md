---
layout: project
title: Hybrid algae-growth modeling
permalink: /hybrid-algae-growth.html
group: research
research_walkthrough: true
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

I developed a hybrid model of *Chlorella vulgaris* growth that combines a mechanistic growth equation with a correction learned from cultivation data. The base model describes temperature and light effects; the learned term uses temperature, light, and pH to account for the growth dynamics it misses.[^paper]

I compared predicted culture density with measurements, identified an equation for the changing error, and added that correction to the growth rate. This made the correction part of the model’s dynamics, so it changes the predicted growth trajectory over time.

## Why a hybrid model

Growth predictions inform how a cultivation process is sized and operated. A model that captures the general biological response can still miss the behavior of a particular culture or reactor, especially when moving between operating scales. Those errors affect estimates of how much biomass will be available and when.[^dissertation]

The existing model already contained useful knowledge about temperature and light. I wanted to keep that structure and use measurements to identify what was missing. A sparse correction gives an explicit equation that can be examined alongside the mechanistic model. In my dissertation, this addressed a different problem from building a surrogate from scratch: how to improve an existing process model with the data available from its operation.[^dissertation]

{% include research-walkthrough.html project="algae" %}

<div class="research-equation">
  <p class="equation" aria-label="The corrected density rate equals the mechanistic rate plus g of temperature, light, and pH">dx<sub>corrected</sub>/dt = f<sub>mech</sub>(T, I) + g(T, I, pH)</p>
  <p><strong>x</strong> is relative culture density, <strong>T</strong> is temperature, and <strong>I</strong> is light intensity. The mechanistic function gives the base growth rate. SINDy learns <strong>g</strong> from the rate of change of the prediction error. The two rates are added before integration to obtain a corrected density trajectory.</p>
</div>

That distinction is important: the correction changes how the model evolves, rather than shifting every prediction by a fixed offset. Its explicit equation also lets me inspect which environmental terms were retained.[^paper]

## My contribution

- Calculated errors between model predictions and measured growth.
- Used SINDy to learn error dynamics from temperature, light, and pH.
- Evaluated the corrected model with sequential cross-validation.

## Results

The corrected predictions followed measured growth more closely in the validation examples.[^paper] The evaluation used one cultivation batch; performance across other strains and reactors remains untested.

The dissertation results also show why validation matters here. Some learned corrections became unstable when integrated, particularly with limited training data. An improvement in selected growth curves does not mean the correction worked across every validation fold.[^dissertation]

{% include figure.html src="/B6.png" alt="Observed, original, and corrected algae growth curves alongside the learned error equation" caption="Compare the corrected curve with both the measurements and the original model. These examples show the effect of learning a changing growth-rate correction." %}

<details class="figure-details"><summary>Experiment and model details</summary>
{% include figure.html src="/B1.png" alt="Original four-step hybrid modeling workflow" caption="The workflow from the research presentation: mechanistic prediction, residual calculation, sparse error dynamics, and model update." %}
{% include figure.html src="/B3.png" alt="Photobioreactor used to collect the algae growth measurements" caption="The 60-liter photobioreactor used for data collection." %}
{% include figure.html src="/B4.png" alt="SINDy correction driven by temperature, light, and pH" caption="The physical drivers used to learn error dynamics." %}
</details>

## References and notes

[^paper]: William Farlessyost and Shweta Singh. [“Improving Mechanistic Model Accuracy with Machine Learning Informed Physics.”](https://doi.org/10.69997/sct.121371) *Systems and Control Transactions* 3, 275 to 282, FOCAPD (2024). Source for the hybrid model, growth measurements, and validation results.

[^dissertation]: William Blake Farlessyost. [*Modeling Material Flow Dynamics in Industrial-Natural Systems: Machine Learning and Causal Analysis for Resilience Evaluation and Sensor Minimization.*](https://doi.org/10.25394/PGS.28904861) Ph.D. dissertation, Purdue University (2025), Chapters 1 and 3, especially Sections 3.3.3 to 3.3.5 and 3.4.4. Describes the rate correction, sequential validation, and unstable prediction trajectories.
