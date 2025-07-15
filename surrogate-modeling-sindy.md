---
layout: project
title: "Surrogate Models via SINDy: Soybean-Diesel Plant & Lake-Watershed Streamflow"
date: 2025-04-23
slug: surrogate-modeling-sindy
excerpt: >
  Sparse Identification of Non-linear Dynamics (SINDy) produced low-order ODE
  surrogates for a continuous soybean-oil-to-biodiesel process and the North
  Fork Vermilion River watershed.
domain: [complex, sysid, ml]
roles: [modeling, system-id]
tags: [SINDy, Python, ODEs]
thumbnail: "1a44eb4d-0048-479b-9a96-20a253842e89.png"
---

<!-- ------------------------------------------------------------------- -->
<!-- 0  METHOD OVERVIEW ------------------------------------------------- -->
<!-- ------------------------------------------------------------------- -->

### 0 Method overview

<p align="center">
  <img src="/A0.png"
       alt="Overview: sparse-regression surrogates for industrial & natural nodes"
       width="720" />
</p>

<p align="center">
  <img src="/A1.png" alt="Classic SINDy workflow schematic" width="700" />
</p>

<p align="center">
  <img src="/A2.png" alt="Extended SINDy with input-derivative terms" width="700" />
</p>
 
Key steps common to both case studies:

1. Time-series → finite-difference \( \dot x,\;\dot u \)  
2. Build polynomial library Θ (order ≤ 2; watershed also uses \( \dot u \))  
3. Sparse regression across λ values  
4. Sequential Quadratic Programming (SQP) on retained coefficients (paper §2.2)  
5. Five-fold cross-validation → select λ*  
6. Hold-out tests (50 h + 200 h for the plant)

---

<!-- ------------------------------------------------------------------- -->
<!-- 1  INDUSTRIAL SYSTEM ------------------------------------------------ -->
<!-- ------------------------------------------------------------------- -->

## 1 Industrial system: soybean-diesel plant

<p align="center">
  <img src="/A3.png" alt="ASPEN Dynamics flowsheet" width="600" />
</p>

*ASPEN Dynamics flowsheet showing six retained flows (x₁–x₆) and two PRBS-excited feeds (u₁ = soybean-oil, u₂ = water).*

**Training data** – 200 h simulation, Δt = 0.02 h  
**Test data**   – 50 h continuation + independent 200 h run (different PRBS seed)

### 1.1 50 h hold-out results

| Model | λ | SQP? | MAE (avg x₁–x₆) | MAE (x₁) |
|-------|---|------|-----------------|----------|
| SINDy | 0.01 | ✖ | **0.152** | 0.167 |
| SINDy+SQP | 0.025 | ✔ | 0.537 | **0.757** |

*(Table values reproduced from paper Table 2.)*

<p align="center">
  <img src="/A5.png" alt="Plant test trajectories (200 h)" width="720" />
</p>

*Red = standard SINDy Blue = SQP-refined Black = ASPEN reference.*

### 1.2 200 h hold-out results

| Model | λ | SQP? | MAE (avg x₁–x₆) | MAE (x₁) |
|-------|---|------|-----------------|----------|
| SINDy+SQP | 0.025 | ✔ | **0.252** | **0.295** |
| SINDy     | 0.01  | ✖ | 5.324 | 8.556 |

*SQP tuning suppresses long-horizon drift (paper §3.2.2).*

---

<!-- ------------------------------------------------------------------- -->
<!-- 2  NATURAL SYSTEM --------------------------------------------------- -->
<!-- ------------------------------------------------------------------- -->

## 2 Natural system: North Fork Vermilion watershed

<p align="center">
  <img src="/A4.png" alt="Watershed map and climate inputs" width="550" />
</p>

*5589 daily records (1988-2005) — stream-flow **Q** and five climate drivers (P, R<sub>solar</sub>, T<sub>max</sub>, T<sub>min</sub>, VPD).*

*Best CV performance*: λ ≈ 0.00175, second-order library + \( \dot u \) terms.

<p align="center">
  <img src="/A6.png" alt="Stream-flow surrogate equations and validation plot" width="720" />
</p>

*Blue = SQP-refined surrogate Red = standard SINDy Black = validation data.*

*Observation (paper §3.5): model captures seasonal peaks but under-predicts short spikes; limited data length is a key bottleneck.*

---

<!-- ------------------------------------------------------------------- -->
<!-- 3  TAKE-AWAYS ------------------------------------------------------- -->
<!-- ------------------------------------------------------------------- -->

## 3 Take-aways 

* Linear library was sufficient for the process-plant surrogates; chaotic watershed needed non-linear and history terms.  
* SQP post-processing improves long-horizon stability without harming cross-validated MAE.  
* Additional data or spline up-sampling is required to raise watershed accuracy.

---

<small>
Source — Farlessyost, William, and Shweta Singh. "Reduced order dynamical models for complex dynamics in manufacturing and natural systems using machine learning." Nonlinear Dynamics 110.2 (2022): 1613-1631. 
</small>
