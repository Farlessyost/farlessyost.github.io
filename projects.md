---
layout: page               # Uses _layouts/page.html
title: "Projects"
permalink: /projects/
description: "Case studies spanning system identification, hybrid ML–physics models, sensor minimization, and network-level resilience analysis."
nav_weight: 3
---

## Portfolio

Below are four representative projects from my doctoral research work.  
Click any tile for a deep-dive write-up.

{% assign all_projects = site.pages | where_exp:"p","p.layout == 'project'" | sort: 'date' | reverse %}
<div class="grid gap-8 md:grid-cols-2 lg:grid-cols-2 mt-8">
  {% for proj in all_projects %}
    <a href="{{ proj.url | relative_url }}" class="card hover:shadow-lg transition group">
      {% if proj.thumbnail %}
        <img src="{{ proj.thumbnail | relative_url }}"
             alt="{{ proj.title }}"
             class="rounded-md mb-4 object-cover aspect-video group-hover:opacity-90 transition"
             loading="lazy" />
      {% endif %}
      <h3 class="font-semibold text-xl">{{ proj.title }}</h3>
      <p class="text-sm text-gray-600">{{ proj.excerpt | strip_html | truncate: 120 }}</p>
    </a>
  {% endfor %}
</div>
