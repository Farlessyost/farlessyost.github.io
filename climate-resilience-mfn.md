---
layout: project
title: Climate resilience across an industrial network
permalink: /climate-resilience-mfn.html
group: research
order: 4
category: Industrial ecology
status: Published research · 2025
description: Connecting agricultural and industrial surrogate models to study how climate stress propagates through a soybean-to-biodiesel network.
summary: Simulating how changing crop production, material stocks, and industrial demand interact across a coupled network.
card_methods: Neural surrogates · Material-flow networks · Climate scenarios
focus: Coupled agricultural–industrial systems
methods: LTC surrogates and dynamic material-flow simulation
context: Doctoral research, Purdue University
next_url: /projects/peepin-on-papaw/
next_title: Peepin on Papaw
---
## The question

An industrial plant depends on systems beyond its own boundary. For biodiesel production, changes in crop growth can affect feedstock supply, stocks, imports, and production further down the network.

This research asks how those connected dynamics shape resilience when the network is exposed to different climate scenarios.

## The approach

I used node-specific liquid-time-constant neural-network surrogates to represent agricultural and industrial processes, then coupled them through material flows and controllers. The detailed process references included ASPEN and BioCro models.

The resulting simulation follows a soybean-to-biodiesel network through changing inputs and demand. Climate scenarios and farm-area configurations provide ways to investigate how the network responds under different assumptions.

<figure class="process-diagram">
  <p class="eyebrow">Material-flow network</p>
  <ol><li><strong>Soybean growth</strong><span>Climate-dependent crop production</span></li><li><strong>Soybean stock</strong><span>Harvest, storage, and imports</span></li><li><strong>Oil plant</strong><span>Extraction and processing</span></li><li><strong>Biodiesel plant</strong><span>Conversion and product output</span></li></ol>
  <figcaption>A simplified view of the material flows. Climate inputs, demand, stocks, and controllers shape the coupled dynamics.</figcaption>
</figure>

## What the network view reveals

The study explores how production shortfalls, accumulated material stocks, waste, and import requirements emerge from interactions among the nodes. A network can experience disruptions even when an individual process model appears well behaved.

The results provide a way to investigate resilience mechanisms and compare assumptions. They are scenario-based simulations, not predictions of actual plant outages or observed operational outcomes.

{% include figure.html src="/D6.png" alt="Simulated oil and biodiesel output under two climate scenarios" caption="Industrial throughput under the modeled climate scenarios. Curves represent different farm-area configurations." %}

<details class="figure-details"><summary>Explore model verification and material-flow results</summary>
{% include figure.html src="/D5.png" alt="Surrogate predictions compared with reference process and crop-growth trajectories" caption="Checking the surrogate trajectories against the detailed reference models." %}
{% include figure.html src="/D7.png" alt="Simulated cumulative waste and material stock under climate scenarios" caption="Stocks and waste reveal additional network constraints." %}
{% include figure.html src="/D8.png" alt="Soybean import requirements under two climate scenarios" caption="Import requirements change with climate assumptions and farm area." %}
</details>

<p class="source-note">“Resilience dynamics in coupled natural-industrial systems: A surrogate modeling approach for assessing climate-change impacts on industrial ecosystems.” <em>Journal of Industrial Ecology</em> (2025). <a href="https://doi.org/10.1111/jiec.70087">Read the published article</a>. Figures shown here come from the original research presentation.</p>
