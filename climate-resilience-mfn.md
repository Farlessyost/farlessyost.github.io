---
layout: project
title: "Network-Level Simulation for Climate Resilience in Illinois Soybean Biodiesel MFN"
date: 2025-04-23
slug: climate-resilience-mfn
excerpt: >
  Node-specific LTC surrogates power a bottom-up material-flow simulation,
  revealing tipping points and recovery dynamics under RCP 4.5 vs 8.5.
domain: [ecology, complex]
roles: [simulation, resilience]
tags: [LTC-NN, Industrial Ecology, Climate Scenarios]
thumbnail: ""
slides: "/Defense.pptx"
---

### Scenario & Scope  
Coupled natural-industrial system around **Champaign County, IL** comprising:

* Soybean growth (agricultural node)  
* Oil extraction plant  
* Biodiesel processing plant

### Method  
* Train LTC models for each node using ASPEN Plus & BioCro data.  
* Run Monte-Carlo simulations under **RCP 4.5 and 8.5** climate projections.  
* Evaluate resilience metrics: production failures, recovery time, import dependency.

### Findings  
* RCP 8.5 caused **earlier & more frequent failures**; 500-ha farms hit stock tipping points ≈ 2050.  
* Smaller farms (450 ha) showed highest import dependency; larger farms buffered but still vulnerable.  
* Non-linear waste accumulation patterns uncovered hidden dependencies.

### Takeaway  
Combining **ML surrogates with network simulation** offers actionable insight for climate-adaptation strategies in bio-industrial supply chains.
