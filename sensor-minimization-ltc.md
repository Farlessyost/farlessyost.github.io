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
thumbnail: "C0.png"
---

### Concept
<p align="center">
  <img src="/C0.png" width="720"
       alt="Overall workflow: train full LTC observer, score inputs, prune, deploy minimal set" />
</p>

---

### From equations to data
<p align="center">
  <img src="/C1.png" width="540"
       alt="ODE templates used to generate synthetic trajectories for testing" />
</p>

---

### Testbeds
<p align="center">
  <img src="/C2.png" width="720"
       alt="Mechanical, ecological, chemical systems and their candidate sensors" />
</p>

* **Mechanical:** Spring–Mass–Damper  
* **Chemical:** Continuous Stirred-Tank Reactor (CSTR)  
* **Ecological:** Predator–Prey population dynamics  

---

### Liquid-Time-Constant observer core
<p align="center">
  <img src="/C3.png" width="540"
       alt="LTC differential neuron and MSE training loss" />
</p>

---

### Causal-score pruning loop
<p align="center">
  <img src="/C4.png" width="380"
       alt="Iterative perturb–score–prune algorithm to drop weak inputs" />
</p>

---

### Network layouts before & after pruning
<p align="center">
  <img src="/C5.png" width="540"
       alt="Full observer, single-channel lasso, and final minimal designs" />
</p>

---

## Results – Causal rankings (perturbation tests)

| Domain | Perturbed-input plots |
|--------|----------------------|
| Mechanical | <img src="/C6.png" width="720" alt="Velocity response to input perturbations"> |
| Ecological | <img src="/C7.png" width="420" alt="Predator–prey response to input perturbations"> |
| Chemical | <img src="/C8.png" width="720" alt="Concentration response to input perturbations"> |

---

## Results – Prediction quality with pruned sensors

| Domain | LTC output vs. ground-truth |
|--------|-----------------------------|
| Mechanical | <img src="/C9.png" width="720" alt="Predicted vs actual velocity after pruning"> |
| Ecological | <img src="/C10.png" width="420" alt="Predicted vs actual predator count after pruning"> |
| Chemical | <img src="/C11.png" width="720" alt="Predicted vs actual concentration after pruning"> |

---

### Key takeaways
* **Noise-only channels** vanish first; physics-critical signals survive.  
* Accuracy stays within target RMSE across all domains after pruning.  
* Final sensor sets match classical observability intuition — easy to justify on the plant floor.

### Value proposition
* Fewer transmitters, lower I/O cost, lighter edge inference.  
* Transparent causal rationale instead of opaque feature importance.

### Next steps
* Handle time-delay and >100-input systems.  
* Stress-test under real sensor dropout & drift.  
* Benchmark against QR-pivot & observability-rank placement methods.
