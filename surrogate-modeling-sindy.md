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

### Method overview

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
 

---

<!-- ------------------------------------------------------------------- -->
<!-- 1  INDUSTRIAL SYSTEM ------------------------------------------------ -->
<!-- ------------------------------------------------------------------- -->

## Industrial system: soybean-diesel plant

<p align="center">
  <img src="/A3.png" alt="ASPEN Dynamics flowsheet" width="600" />
</p>

*ASPEN Dynamics flowsheet showing six retained flows (x₁–x₆) and two PRBS-excited feeds (u₁ = soybean-oil, u₂ = water).*

<p align="center">
  <img src="/A5.png" alt="Plant test trajectories (200 h)" width="720" />
</p>

*Red = standard SINDy Blue = SQP-refined Black = ASPEN reference.*

---

<!-- ------------------------------------------------------------------- -->
<!-- 2  NATURAL SYSTEM --------------------------------------------------- -->
<!-- ------------------------------------------------------------------- -->

## Natural system: North Fork Vermilion watershed

<p align="center">
  <img src="/A4.png" alt="Watershed map and climate inputs" width="550" />
</p>


<p align="center">
  <img src="/A6.png" alt="Stream-flow surrogate equations and validation plot" width="720" />
</p>



---

<!-- ------------------------------------------------------------------- -->
<!-- 3  TAKE-AWAYS ------------------------------------------------------- -->
<!-- ------------------------------------------------------------------- -->

## Take-aways 

* Linear library was sufficient for the process-plant surrogates; chaotic watershed needed non-linear and history terms.  
* SQP post-processing improves long-horizon stability without harming cross-validated MAE.  
* Additional data or spline up-sampling is required to raise watershed accuracy.

---

<small>
Source — Farlessyost, William, and Shweta Singh. "Reduced order dynamical models for complex dynamics in manufacturing and natural systems using machine learning." Nonlinear Dynamics 110.2 (2022): 1613-1631. 
</small>
