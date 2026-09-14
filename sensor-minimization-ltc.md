---
layout: project
title: Learning which sensors matter
permalink: /sensor-minimization-ltc.html
group: research
order: 3
category: Sensing & machine learning
status: Research preprint · 2025
description: Using continuous-time neural observers and controlled input perturbations to investigate smaller measurement sets for dynamic systems.
summary: Exploring how a model can retain useful state estimates with fewer inputs across mechanical, chemical, and ecological testbeds.
card_methods: Liquid-time-constant networks · Observers · Causal analysis
focus: Sensor selection for state estimation
methods: Neural observers and perturbation-based pruning
context: Doctoral research, Purdue University
next_url: /climate-resilience-mfn.html
next_title: Climate resilience across an industrial network
---
## The question

A system can have many available measurements without needing all of them to estimate the state of interest. Which signals carry essential information, and which can be removed?

I investigated that question with liquid-time-constant (LTC) neural networks, using mechanical, chemical, and ecological test systems.

## The approach

An LTC observer first learns to estimate a target state from the full set of candidate inputs. Controlled perturbations then test how changes to individual inputs affect its predictions. Those responses guide an iterative pruning process, with the reduced input set evaluated against a prediction-error target.

The testbeds include a spring–mass–damper system, a continuous stirred-tank reactor, and predator–prey population dynamics.

{% include figure.html src="/C2.png" alt="Mechanical, ecological, and chemical testbeds with candidate measurements" caption="Three different kinds of dynamics provide test cases for the sensor-selection approach." %}

## What the experiments showed

The reported synthetic test cases supported smaller input sets while meeting their prediction-error targets. Inputs containing only noise could be removed, while signals important to the modeled dynamics remained.

The useful result is a more inspectable basis for deciding which measurements support an observer. It does not establish field performance, hardware cost savings, or behavior under real sensor drift.

{% include figure.html src="/C5.png" alt="Comparison of the full observer and reduced sensor-network designs" caption="Observer designs before and after input selection." %}

<details class="figure-details"><summary>Explore the pruning method and prediction results</summary>
{% include figure.html src="/C4.png" alt="Iterative perturbation, scoring, and input-pruning algorithm" caption="The input-pruning loop." %}
{% include figure.html src="/C9.png" alt="Mechanical-system state predictions after sensor pruning compared with ground truth" caption="Mechanical-system prediction results using the reduced input set." %}
{% include figure.html src="/C10.png" alt="Predator-prey prediction results after sensor pruning" caption="Ecological-system prediction results." %}
{% include figure.html src="/C11.png" alt="Chemical concentration predictions after sensor pruning" caption="Chemical-system prediction results." %}
</details>

<p class="source-note">Research with Sebastian Oberst and Shweta Singh. <a href="https://arxiv.org/abs/2509.11336">Read the 2025 preprint</a>. This link identifies the preprint version of the work.</p>
