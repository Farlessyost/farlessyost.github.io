---
layout: project
title: "Network-Level Simulation for Climate Resilience in Illinois Soybean-Biodiesel MFN"
date: 2025-04-23
slug: climate-resilience-mfn
excerpt: >
  Node-specific LTC surrogates drive a bottom-up material-flow simulation that
  reveals tipping points and recovery dynamics for the region’s biodiesel
  network under RCP 4.5 vs 8.5.
domain: [ecology, complex]
roles: [simulation, resilience]
tags: [LTC-NN, Industrial Ecology, Climate Scenarios]
thumbnail: "D5.png"
slides: "/Defense.pptx"
---

<!-- overview -->
<p align="center">
  <img src="/D0.png" width="720"
       alt="Coupled agricultural–industrial material-flow network with climate and demand drivers" />
</p>

---

### Methodological flow
<p align="center">
  <img src="/D1.png" width="540"
       alt="Three-step workflow: build node surrogates → couple flows & controllers → analyze resilience" />
</p>

---

### System boundary & data pipeline
<p align="center">
  <img src="/D2.png" width="720"
       alt="MFN nodes (soy growth, oil plant, diesel plant) with exogenous climate drivers and controllers" />
</p>

---

### Algorithmic controllers for coupled plants
<p align="center">
  <img src="/D3.png" width="540"
       alt="Controller LTC nets wrapped around frozen plant surrogates" />
</p>

---

### LTC network architectures (oil vs. diesel nodes)
<p align="center">
  <img src="/D4.png" width="600"
       alt="Liquid-time-constant neuron graphs for the two industrial nodes" />
</p>

---

## Verification – LTC vs. ASPEN/BioCro trajectories
<p align="center">
  <img src="/D5.png" width="640"
       alt="Surrogate predictions match test trajectories for diesel, oil, and soybean growth" />
</p>

---

## Climate-scenario results

| Metric block | RCP 4.5  | RCP 8.5 |
|--------------|----------|---------|
| **Industrial throughput** | <img src="/D6.png" width="420" alt="Oil & diesel hourly output (4.5)"> | <img src="/D6.png#right" width="420" alt="Oil & diesel hourly output (8.5)"> |
| **Stock & waste accumulation** | <img src="/D7.png" width="420" alt="Cumulative waste and seasonal stock trends (4.5)"> | <img src="/D7.png#right" width="420" alt="Cumulative waste and seasonal stock trends (8.5)"> |
| **Import to sustain operation** | <img src="/D8.png" width="420" alt="Soy imports required (4.5)"> | <img src="/D8.png#right" width="420" alt="Soy imports required (8.5)"> |

<small>*Blue = 450 ha, Green = 500 ha, Red = 550 ha farm size*</small>

---

### Key insights
* **Earlier & more frequent production shortfalls** under RCP 8.5; first outages appear ≈ 2040 for 500 ha farms.  
* 450 ha configuration relies on imports after ≈ 2025 in both scenarios; 550 ha buffers longer but eventually stalls under extreme-heat years.  
* Waste build-up (red curves) exposes hidden storage bottlenecks that accelerate shutdown cascades.  

### Why it matters
A **node-level hybrid (physics + ML) approach** surfaces nonlinear resilience thresholds that aggregated IAMs miss.  
Findings guide acreage strategy, storage sizing, and climate-adaptation road-maps for Midwestern biofuels.

---

### Next on the roadmap
* Extend boundary to rail transport & glycerol co-product valorisation.  
* Couple to watershed & groundwater models for water-stress feedbacks.  
* Embed agent-based economic layer to test policy levers (RFS credits, crop insurance).

