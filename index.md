---
layout: default
title: Engineering portfolio
permalink: /
description: William Farlessyost, Ph.D. Engineering experience in robotics, embedded systems, simulation, and machine learning.
---
<section class="hero shell" aria-labelledby="intro-title">
  <div class="hero-copy">
    <p class="eyebrow">William Farlessyost, Ph.D.</p>
    <h1 id="intro-title">Engineer &amp;<br>researcher.</h1>
    <p class="hero-intro">I develop robots, embedded sensing systems, and machine learning models. My background is in mechatronics, applied mathematics, and doctoral research at Purdue.</p>
    <div class="actions"><a class="button" href="{{ '/resume.pdf' | relative_url }}">View résumé <span aria-hidden="true">↗</span><span class="sr-only"> (PDF)</span></a><a class="text-link" href="{{ '/projects/' | relative_url }}">View projects</a></div>
  </div>
  <figure class="hero-portrait">
    <div class="portrait-frame"><img src="{{ '/headshot.jpg' | relative_url }}" alt="William Farlessyost" width="1492" height="2892" fetchpriority="high"></div>
    <figcaption>Robotics · Embedded systems · Machine learning</figcaption>
  </figure>
</section>
<div class="focus-strip shell" aria-label="Core skills"><span>Core skills</span><p>Python <span aria-hidden="true">/</span> C/C++ <span aria-hidden="true">/</span> ROS 2 <span aria-hidden="true">/</span> CAD <span aria-hidden="true">/</span> Simulation</p></div>
<section class="work-section shell" aria-labelledby="work-title">
  <div class="section-heading"><div><h2 id="work-title">Engineering projects</h2></div><p>Current work in embedded sensing and robotics.</p></div>
  {% include featured-builds.html %}
  <div class="research-heading"><h2>Research</h2></div>
  {% include work-list.html %}
  <div class="actions"><a class="text-link" href="{{ '/about/' | relative_url }}">Experience, education, and publications</a></div>
</section>
<section class="contact-band shell"><h2>Contact</h2><div><p>Contact me about engineering and research opportunities.</p><a class="button" href="{{ '/contact/' | relative_url }}">Contact details <span aria-hidden="true">↗</span></a></div></section>
