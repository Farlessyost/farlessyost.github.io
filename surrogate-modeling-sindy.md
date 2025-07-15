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
thumbnail: "soybean_flowsheet.png"
---

![Soybean-oil → biodiesel process flowsheet](/soybean_flowsheet.png)

## 1 Systems & data

| System | Data source | States / inputs used | Purpose |
|--------|-------------|----------------------|---------|
| **Soybean-diesel plant** | 200 h ASPEN Plus Dynamics run with PRBS on soybean-oil (u₁) and water (u₂) feeds | 6 material-flow states (x₁–x₆) | Build a fast twin for scenario + MPC studies |
| **North Fork Vermilion River** | Daily climate drivers (1950-2005) + USGS stream-flow gauge (1988-2005) | Q (stream-flow) \| P, R\_solar, T\_max, T\_min, VPD | Obtain a tractable stream-flow equation |

---

## 2 Modelling workflow (identical for both cases)

1. Numerical derivatives → \( \dot{x},\;\dot{u} \)  
2. Polynomial library (order ≤ 2); watershed variant also includes \( \dot{u} \) to capture hysteresis  
3. Sparse regression across λ values  
4. SQP refinement of retained coefficients (MATLAB `fmincon`, MAE objective)  
5. 5-fold CV → choose λ*  
6. Hold-out tests (plant: 50 h + 200 h)

---

## 3 Soybean-diesel plant test results

### 3.1 50 h hold-out

![50 h plant test](/plant_test_50h.png)

| Model | λ | Optimized? | MAE (avg x₁–x₆) | MAE (x₁ only) |
|-------|---|-----------|------------------|---------------|
| SINDy | 0.01 | ✖ | **0.152** | 0.167 |
| SINDy | 0.025 | ✖ | 0.473 | 0.662 |
| SINDy | 0.08 | ✖ | 0.268 | 0.392 |
| SINDy+SQP | 0.01 | ✔ | 0.604 | 0.885 |
| **SINDy+SQP** | **0.025** | **✔** | 0.537 | **0.757** |
| SINDy+SQP | 0.08 | ✔ | 0.295 | 0.442 |

*(values reproduced from Table 2, first block)*  

*Take-away: plain SINDy with λ = 0.01 is best on short unseen data.*

---

### 3.2 200 h hold-out

![200 h plant test](/plant_test_200h.png)

| Model | λ | Optimized? | MAE (avg x₁–x₆) | MAE (x₁ only) |
|-------|---|-----------|------------------|---------------|
| SINDy | 0.01 | ✖ | 5.324 | 8.556 |
| SINDy | 0.025 | ✖ | 2.193 | 3.366 |
| SINDy | 0.08 | ✖ | 1.344 | 0.723 |
| **SINDy+SQP** | **0.025** | **✔** | **0.252** | **0.295** |
| SINDy+SQP | 0.01 | ✔ | 0.526 | 0.752 |
| SINDy+SQP | 0.08 | ✔ | 1.266 | 0.592 |

*Optimization slashes long-horizon drift; λ = 0.025 + SQP gives lowest error.*

---

## 4 Watershed surrogate (single CV fold)

<!-- Optional image; comment out if not needed -->
<!-- ![Watershed validation plot](/watershed_validation.png) -->

*Best model (second-order + \( \dot{u} \), λ ≈ 0.00175) tracks seasonal peaks but under-predicts short spikes.  
Further work: spline up-sampling or higher-order terms.*

---

## 5 Key observations

* Linear library suffices for stoichiometric plant flows; watershed needs nonlinear + history terms.  
* SQP tuning improves stability without harming cross-validated MAE.  
* Data sparsity (5 589 points) limits watershed accuracy; more observations or synthetic augmentation required.

---

### Reference

Farlessyost W. & Singh S. (2021) *Reduced Order Dynamical Models for Complex Dynamics in Manufacturing and Natural Systems Using Machine Learning.* arXiv:2110.08313.
