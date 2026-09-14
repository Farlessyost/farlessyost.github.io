---
layout: project
title: Learning what a mechanistic model misses
permalink: /hybrid-algae-growth.html
group: research
order: 2
category: Scientific machine learning
status: Conference proceedings · 2024
description: Combining a mechanistic algae-growth model with learned error dynamics to improve predictions while retaining interpretable physical drivers.
summary: Pairing biological growth equations with a learned correction that accounts for behavior missing from the original model.
card_methods: Hybrid modeling · SINDy · Biological dynamics
focus: Chlorella vulgaris growth
methods: Mechanistic modeling and sparse residual dynamics
context: Doctoral research, Purdue University
next_url: /sensor-minimization-ltc.html
next_title: Learning which sensors matter
---
## The question

A mechanistic model contains useful knowledge about a process, but it may leave out dynamics that appear in measured data. Can machine learning improve that model while keeping its physical structure understandable?

This study examined growth of the microalga *Chlorella vulgaris*, with temperature, light, and pH as important drivers.

## The approach

I started with a low-order mechanistic growth model and calculated the difference between its predictions and the observations. SINDy then learned a differential equation for that error, using candidate terms built from the system's physical drivers.

The learned correction was added back to the original prediction. This gives the mechanistic model a defined role while using data to represent dynamics it does not capture.

{% include figure.html src="/B1.png" alt="Four-step hybrid modeling workflow from mechanistic prediction through error dynamics to corrected prediction" caption="The hybrid workflow: fit the mechanistic model, calculate its error, learn error dynamics, and update the prediction." %}

## What the study showed

The hybrid predictions tracked observed growth more closely in the reported validation examples. Temperature, light, and pH remained explicit in the correction, making it possible to inspect what the learned model was using.

The evaluation used sequential cross-validation on a single cultivation batch. It demonstrates the approach on that dataset; testing across other strains, reactors, and operating conditions is a separate question.

{% include figure.html src="/B6.png" alt="Observed, original, and corrected algae growth curves alongside the learned error equation" caption="Validation examples compare the original mechanistic predictions with the corrected model and observations." %}

<details class="figure-details"><summary>Explore the experiment and model details</summary>
{% include figure.html src="/B3.png" alt="Photobioreactor used to collect the algae growth measurements" caption="The 60-liter photobioreactor used for data collection." %}
{% include figure.html src="/B4.png" alt="SINDy correction driven by temperature, light, and pH" caption="The physical drivers used to learn error dynamics." %}
</details>

<p class="source-note">William Farlessyost and Shweta Singh. “Improving Mechanistic Model Accuracy with Machine-Learning-Informed Physics.” <em>Systems and Control Transactions</em> 3, 275–282, FOCAPD (2024). <a href="https://doi.org/10.69997/sct.121371">Read the publication</a>.</p>
