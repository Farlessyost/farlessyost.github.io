---
layout: project
title: "Surrogate Modeling with SINDy: Soybean Biodiesel Plant & Watershed Streamflow"
date: 2025-04-23
slug: surrogate-modeling-sindy
excerpt: >
  Applying an extended SINDy framework to derive low-order, interpretable ODE models
  for an industrial soybean-to-diesel process and a natural stream-flow system.
domain: [complex, sysid, ml]
roles: [modeling, system-id]
tags: [SINDy, Python, ODEs]
thumbnail: ""
slides: "/Defense.pptx"
---

### Objective  
Develop sparse, low-order surrogate models that **faithfully reproduce key dynamics** of two very different processes:

1. **Soybean-oil → diesel plant** (mechanistic simulation data)  
2. **Lake Vermilion watershed streamflow** (observational data)

### Methods  
* **Extended SINDy** with coefficient optimization  
* Function library: polynomials (up to 2) + selected input derivatives  
* Cross-validated on withheld trajectories

### Key Findings  
* Industrial process: achieved accurate *linear* ODEs aligned with mass-balance physics.  
* Natural system: derivatives helped capture hysteresis, but performance limited by data noise and chaos.  
* Optimization improved long-term stability for both cases.

### Impact  
Demonstrated that **sparse regression can down-scale high-fidelity simulations** into real-time, interpretable digital twins—laying groundwork for control and scenario analysis.

> **Code & data** coming soon on GitHub.
