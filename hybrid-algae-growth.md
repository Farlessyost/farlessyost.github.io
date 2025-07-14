---
layout: project
title: "Hybrid Mechanistic + ML Model for *Chlorella vulgaris* Growth"
date: 2025-04-23
slug: hybrid-algae-growth
excerpt: >
  Integrating SINDy-derived error terms with a Cardinal Temperature Model
  to boost prediction accuracy for industrial-scale microalgae cultivation.
domain: [ml, control, ecology]
roles: [modeling, hybrid-ml]
tags: [SINDy, CTMI, Biology]
thumbnail: ""
slides: "/Defense.pptx"
---

### Objective  
Preserve mechanistic interpretability while **capturing complex growth behaviours** of *C. vulgaris* in batch reactors.

### Approach  
* Base model: Haldane + CTMI kinetics  
* Additive **SINDy correction term** trained on residuals  
* 20-fold sequential cross-validation for robustness

### Highlights  
* Hybrid model consistently out-performed the original, especially on oscillatory regimes.  
* Exposed data-sparsity limits and suggested richer experimental design.

### Why It Matters  
Accurate growth prediction unlocks **process optimization** and **energy balancing** for algae-based bioproducts without black-box loss of insight.
