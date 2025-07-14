---
layout: project
title: "Sensor Minimization via Causality-Guided LTC Networks"
date: 2025-04-23
slug: sensor-minimization-ltc
excerpt: >
  A perturbation-based pruning algorithm that shrinks sensor sets for mechanical,
  chemical, and ecological systems—without sacrificing accuracy.
domain: [ml, control]
roles: [sensor-design, causality]
tags: [LTC-NN, Spring–Mass–Damper, CSTR, Predator-Prey]
thumbnail: ""
slides: "/Defense.pptx"
---

### Systems Evaluated  
* **Mechanical:** Spring–Mass–Damper  
* **Chemical:** Continuous Stirred-Tank Reactor (CSTR)  
* **Ecological:** Predator–Prey model

### Method  
1. Train full-state **Liquid Time-Constant (LTC) networks**.  
2. Quantify *dynamic causal influence* of each input via perturbation analysis.  
3. Iteratively prune the least-causal inputs until accuracy degrades.

### Results  
* Noise channels pruned first; interaction terms kept only when essential.  
* Achieved **minimal sensor sets** that still met accuracy targets across all testbeds.  
* Final selections aligned with known physics, boosting interpretability.

### Value Proposition  
Reduces hardware costs and computational load for soft-sensor deployment in manufacturing and environmental monitoring.
