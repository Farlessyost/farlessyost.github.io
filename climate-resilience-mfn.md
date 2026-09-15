---
layout: project
title: Climate resilience modeling
permalink: /climate-resilience-mfn.html
group: research
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

I modeled how changes in crop growth affect supply and production across a soybean-to-biodiesel network.[^paper]

## My contribution

- Built neural surrogate models of agricultural and industrial processes using ASPEN and BioCro references.
- Connected the models through material flows, inventories, and controllers.
- Compared climate scenarios and farm-area configurations.

<figure class="process-diagram">
  <p class="eyebrow">Material-flow network</p>
  <ol><li><strong>Soybean growth</strong><span>Climate-dependent crop production</span></li><li><strong>Soybean stock</strong><span>Harvest, storage, and imports</span></li><li><strong>Oil plant</strong><span>Extraction and processing</span></li><li><strong>Biodiesel plant</strong><span>Conversion and product output</span></li></ol>
  <figcaption>Material flows from soybean production to biodiesel output.</figcaption>
</figure>

## Results

The simulations showed how climate inputs and farm area affected output, material stocks, waste, and imports across the network.[^paper] These are scenario results, not forecasts of actual plant operations.

{% include figure.html src="/D6.png" alt="Simulated oil and biodiesel output under two climate scenarios" caption="Industrial throughput under the modeled climate scenarios. Curves represent different farm-area configurations." %}

<details class="figure-details"><summary>Model verification and material-flow results</summary>
{% include figure.html src="/D5.png" alt="Surrogate predictions compared with reference process and crop-growth trajectories" caption="Checking the surrogate trajectories against the detailed reference models." %}
{% include figure.html src="/D7.png" alt="Simulated cumulative waste and material stock under climate scenarios" caption="Stocks and waste reveal additional network constraints." %}
{% include figure.html src="/D8.png" alt="Soybean import requirements under two climate scenarios" caption="Import requirements change with climate assumptions and farm area." %}
</details>

## References and notes

[^paper]: William Farlessyost and Shweta Singh. [“Modeling material flow dynamics in coupled natural-industrial ecosystems for resilience to climate change: A case study on a soybean-based industrial ecosystem.”](https://doi.org/10.1111/jiec.70087) *Journal of Industrial Ecology* 29, 1882 to 1896 (2025). Figures shown here come from the original research presentation.
