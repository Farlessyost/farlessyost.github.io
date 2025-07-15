---
layout: project
title: "Hybrid Mechanistic + ML Model for *Chlorella vulgaris* Growth"
date: 2025-04-23
slug: hybrid-algae-growth
excerpt: >
  Mechanistic CTMI kinetics corrected by a SINDy-learned error term
  delivers higher-fidelity algae-growth predictions without losing
  physical interpretability.
domain: [ml, control, ecology]
roles: [modeling, hybrid-ml]
tags: [SINDy, CTMI, Biology]
thumbnail: "B3.png"
---

### Overview
<p align="center">
  <img src="/B0.png" width="720"
       alt="Concept: update low-order mechanistic models with sparse-regression error terms" />
</p>

## Why a hybrid model?

A traditional Cardinal-Temperature/Light equation is fast but misses
multi-day oscillations and pH effects.  
An additive SINDy error ODE restores accuracy **without turning the whole
model into a black box.**

---

### Methodology
<p align="center">
  <img src="/B1.png" width="460"
       alt="Four-step workflow: fit mech model → compute error → learn error ODE → update" />
</p>

20-fold sequential cross-validation was run on a single 41 000 min batch.

---

### Mechanistic error vs. data
<p align="center">
  <img src="/B2.png" width="670"
       alt="Mechanistic prediction vs data and definition of the error signal" />
</p>

---

### Experimental setup
<p align="center">
  <img src="/B3.png" width="380"
       alt="60 L photobioreactor used for data collection" />
</p>

---

### Control-only SINDy block
<p align="center">
  <img src="/B4.png" width="540"
       alt="Control-only SINDy block—error ODE driven by T, light, pH" />
</p>

---

### Library functions
<p align="center">
  <img src="/B5.png" width="340"
       alt="Domain-specific functions added to the SINDy library" />
</p>

---

### Results
<p align="center">
  <img src="/B6.png" width="720"
       alt="Error ODE and validation-fold improvements" />
</p>

#### At a glance
* Hybrid curve (green/black on slide) hugs observed density far better than the blue baseline.  
* Physical drivers stay explicit—temperature, light, and pH appear clearly in the learned term.

---

#### Where next
* Broader data sets (different strains, reactors).  
* Online adaptation for continuous cultivation.  
* Ensemble error models to smooth early-batch noise sensitivity.

<small>
Source – Farlessyost W., Singh S. (2024) *Improving Mechanistic Model Accuracy with Machine-Learning-Informed Physics.*  
In: **Foundations of Computer Aided Process Design (FOCAPD 2024)**, Breckenridge CO, July 14-18.  
Peer-reviewed proceedings, PSEcommunity LAPSE:2024.1538, Syst Control Trans 3:275-282.  
<https://PSEcommunity.org/LAPSE:2024.1538>
</small>
