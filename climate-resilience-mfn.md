---
layout: project
title: Climate resilience modeling
permalink: /climate-resilience-mfn.html
group: research
research_walkthrough: true
order: 4
category: Industrial ecology
status: Published research · 2025
description: Simulated climate effects on a soybean-to-biodiesel production network.
summary: Connected crop and industrial models to evaluate production, inventories, and imports under climate scenarios.
card_methods: Neural surrogates · Material-flow networks · Climate scenarios
focus: Agricultural and industrial systems
methods: LTC surrogates and dynamic material-flow simulation
context: Doctoral research, Purdue University
next_url: /projects/peepin-on-papaw/
next_title: Peepin on Papaw
---
## Overview

I built a dynamic model of a soybean-to-biodiesel production network, connecting crop growth, processing, material inventories, and production controls. The model follows how changes in agricultural supply affect downstream oil and biodiesel production, stored material, waste, and import requirements.[^paper]

I trained neural surrogate models using BioCro crop-growth and ASPEN process models, then connected them through material balances. Comparing climate scenarios and farm-area configurations made it possible to follow a disturbance from the agricultural part of the network through the industrial processes that depend on it.

## Why model the whole network

A processing plant depends on both the amount and timing of its feedstock supply. Changes in crop growth can therefore affect industrial production well beyond the farm. I wanted to understand how those disturbances propagate, and which parts of the network absorb them or become bottlenecks.[^dissertation]

A crop shortfall does not necessarily stop a plant immediately. Stored material can cover the gap, and imports can replace part of the missing supply. Annual production totals can hide that dependence: the same output may come from a steady harvest, depleted reserves, or increased imports. Tracking stocks and flows over time makes those differences visible and supports comparisons of land area, supply dependence, and production continuity.

This was the network-level application of my doctoral research. It brought the emphasis on compact process models into a coupled system, where resilience depends on the interactions between agriculture, storage, and manufacturing.[^dissertation]

{% include research-walkthrough.html project="climate" %}

<div class="research-equation">
  <p class="equation" aria-label="The rate of change of soybean stock equals harvest plus imports minus plant feed minus losses">dS/dt = H + M − F − L</p>
  <p>In this simplified soybean-stock balance, <strong>S</strong> is stored mass, <strong>H</strong> the incoming harvest rate, <strong>M</strong> imports, <strong>F</strong> withdrawal for processing, and <strong>L</strong> losses. All four flow rates have units of mass per time. Integrating the balance tracks the inventory available for later production.</p>
</div>

The stock balance connects processes operating on different time scales. Crop growth changes with weather and season; processing responds to feedstock and production targets. I used neural surrogate models to represent the individual processes, then coupled them through material stocks, flows, and controllers.[^dissertation]

## My contribution

- Built neural surrogate models of agricultural and industrial processes using ASPEN and BioCro references.
- Connected the models through material flows, inventories, and controllers.
- Compared climate scenarios and farm-area configurations.

## Results

The simulations showed how climate inputs and farm area affected output, material stocks, waste, and imports across the network.[^paper] These are scenario results, not forecasts of actual plant operations.

Read the output curves alongside the stock and import plots. Maintaining production by drawing down stored soybeans has a different implication from maintaining it with a steady supply. That is why resilience was evaluated across several network quantities rather than a single output total.

{% include figure.html src="/D6.png" alt="Simulated oil and biodiesel output under two climate scenarios" caption="Industrial throughput under the modeled climate scenarios. Curves represent different farm-area configurations." %}

<details class="figure-details"><summary>Model verification and material-flow results</summary>
{% include figure.html src="/D5.png" alt="Surrogate predictions compared with reference process and crop-growth trajectories" caption="Checking the surrogate trajectories against the detailed reference models." %}
{% include figure.html src="/D7.png" alt="Simulated cumulative waste and material stock under climate scenarios" caption="Stocks and waste reveal additional network constraints." %}
{% include figure.html src="/D8.png" alt="Soybean import requirements under two climate scenarios" caption="Import requirements change with climate assumptions and farm area." %}
</details>

## References and notes

[^paper]: William Farlessyost and Shweta Singh. [“Modeling material flow dynamics in coupled natural-industrial ecosystems for resilience to climate change: A case study on a soybean-based industrial ecosystem.”](https://doi.org/10.1111/jiec.70087) *Journal of Industrial Ecology* 29, 1882 to 1896 (2025). Figures shown here come from the original research presentation.

[^dissertation]: William Blake Farlessyost. [*Modeling Material Flow Dynamics in Industrial-Natural Systems: Machine Learning and Causal Analysis for Resilience Evaluation and Sensor Minimization.*](https://doi.org/10.25394/PGS.28904861) Ph.D. dissertation, Purdue University (2025), Chapters 1 and 5. Explains the resilience motivation and describes the process surrogates, material-flow coupling, and production controllers. The stock equation above summarizes one inventory balance; it is not the full network model.
