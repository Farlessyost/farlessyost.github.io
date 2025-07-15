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

### Overview
<p align="center">
  <img src="/C0.png" width="720"
       alt="Concept schematic: causal pruning of Liquid-Time-Constant observers" />
</p>

---

### Benchmarks
<p align="center">
  <img src="/C2.png" width="720"
       alt="Three mechanistic systems exercised: mechanical, ecological, chemical" />
</p>

* **Mechanical:** Spring–Mass–Damper  
* **Chemical:** Continuous Stirred-Tank Reactor (CSTR)  
* **Ecological:** Predator–Prey model  

---

### Liquid Time-Constant (LTC) observer
<p align="center">
  <img src="/C3.png" width="540"
       alt="Differential equation and MSE loss for the LTC recurrent block" />
</p>

---

### Causality-guided pruning loop
<p align="center">
  <img src="/C4.png" width="380"
       alt="Iterative perturb-score-prune procedure to drop weakly causal inputs" />
</p>

---

### Network architecture
<p align="center">
  <img src="/C5.png" width="540"
       alt="Full vs. pruned observer layouts and resulting signal channels" />
</p>

---

### Results – Mechanical
<p align="center">
  <img src="/C6.png" width="720"
       alt="Velocity tracking plots before/after pruning—spring–mass–damper" />
</p>

---

### Results – Ecological
<p align="center">
  <img src="/C7.png" width="420"
       alt="Predator–prey tracking and causal-score ranking" />
</p>

---

### Results – Chemical
<p align="center">
  <img src="/C8.png" width="720"
       alt="Concentration tracking in CSTR across four scenarios" />
</p>

---

#### Key takeaways
* Noise-only channels are discarded first; physics-critical signals persist.  
* **Accuracy maintained** within target RMSE for all three domains after pruning.  
* Selected sensors line up with textbook observability arguments—helping adoption by controls engineers.

---

#### Value proposition
* Cuts hardware & I/O costs for soft-sensor deployments.  
* Lowers inference load for embedded edge controllers.  
* Delivers a **transparent causal rationale** instead of opaque feature ranking.

---

#### Where next
* Extend to systems with time delays and >100 candidate inputs.  
* Stress-test under real sensor dropouts and drift.  
* Benchmark against traditional observability-rank and QR pivoting schemes.

