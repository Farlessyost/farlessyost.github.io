---
layout: default            # Uses _layouts/default.html (leave as-is)
title: "Home"
permalink: /
description: >
  Complex-systems PhD blending ML, control theory, and industrial ecology
  to turn nonlinear chaos into actionable insight for manufacturers.
---

<!-- HERO -->
<section class="hero-wrapper py-16 md:py-24 bg-blue-light/10">
  <div class="container mx-auto flex flex-col md:flex-row items-center gap-8 px-6">

    <!-- Head-shot lives right next to this file. -->
    <img 
    src="{{ '/headshot.jpg' | relative_url }}"
    alt="William Farlessyost smiling in a yellow shirt"
    width="10"  height="10"          <!-- 40 px ≈ Tailwind’s w-10/h-10 -->
    style="object-fit:cover;border-radius:9999px;box-shadow:0 2px 4px rgba(0,0,0,.15);" />


    <div>
      <h1 class="text-3xl md:text-4xl font-bold mb-4">
        Turning Nonlinear Chaos<br class="hidden md:block" />
        into Industrial <span class="text-orange">Insight</span>
      </h1>

      <p class="max-w-xl text-lg leading-relaxed mb-6">
        I’m <strong>William&nbsp;Farlessyost</strong>—a complex-systems modeler
        &amp; control-theory specialist who helps companies
        <em>diagnose</em>, <em>predict</em>, and <em>optimize</em>
        their toughest production and sustainability challenges.
      </p>

      <div class="flex flex-wrap gap-3">
        <a href="{{ '/projects/' | relative_url }}" class="btn-primary">
          View Projects
        </a>
        <a href="{{ '/resume.pdf' | relative_url }}" class="btn-outline">
          Download Résumé
        </a>
      </div>
    </div>
  </div>
</section>

<!-- PILLARS -->
<section class="py-16 md:py-20 bg-white">
  <div class="container mx-auto px-6">
    <h2 class="section-title">Expertise at a Glance</h2>

    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3 mt-10">
      {% assign pillars = 
        [
          { "title": "Complex Systems Modeling", "emoji": "🌀", "link": "/projects/#complex" },
          { "title": "Machine Learning & Control", "emoji": "🤖", "link": "/projects/#ml" },
          { "title": "System Identification", "emoji": "🛠️", "link": "/projects/#sysid" },
          { "title": "Industrial Ecology", "emoji": "🌱", "link": "/projects/#ecology" },
          { "title": "Consulting Services", "emoji": "💼", "link": "/consulting/" },
          { "title": "Weekly Blog Insights", "emoji": "✍️", "link": "/blog/" }
        ] %}

      {% for p in pillars %}
        <a href="{{ p.link | relative_url }}" class="card hover:shadow-lg transition">
          <div class="text-4xl mb-3">{{ p.emoji }}</div>
          <h3 class="font-semibold text-lg">{{ p.title }}</h3>
        </a>
      {% endfor %}
    </div>
  </div>
</section>

<!-- FEATURED PROJECTS -->
<section class="py-16 md:py-20 bg-blue-light/5">
  <div class="container mx-auto px-6">
    <h2 class="section-title">Featured Projects</h2>

    {% assign featured = site.pages
         | where_exp:"item","item.layout == 'project'"
         | sort: 'date' | reverse | slice: 0,3 %}

    {% if featured.size > 0 %}
      <div class="grid gap-8 md:grid-cols-3 mt-10">
        {% for project in featured %}
          <a href="{{ project.url | relative_url }}" class="project-tile group">
            {% if project.thumbnail %}
              <img src="{{ project.thumbnail | relative_url }}"
                   alt="{{ project.title }}"
                   class="rounded-lg mb-4 object-cover aspect-video group-hover:opacity-90 transition"
                   loading="lazy" />
            {% endif %}
            <h3 class="font-semibold text-lg mb-1">{{ project.title }}</h3>
            <p class="text-sm text-gray-600">{{ project.excerpt | strip_html | truncate: 90 }}</p>
          </a>
        {% endfor %}
      </div>
    {% else %}
      <p class="mt-6 text-gray-600">
        Project case studies coming soon—stay tuned!
      </p>
    {% endif %}
  </div>
</section>

<!-- LATEST BLOG POST -->
<section class="py-16 md:py-20 bg-white">
  <div class="container mx-auto px-6 text-center">
    <h2 class="section-title">Latest on the Blog</h2>

    {% assign latest_post = site.posts | first %}
    {% if latest_post %}
      <article class="mx-auto max-w-3xl mt-10">
        <h3 class="text-2xl font-bold mb-2">
          <a href="{{ latest_post.url | relative_url }}"
             class="hover:text-orange">
            {{ latest_post.title }}
          </a>
        </h3>
        <p class="text-gray-600 mb-4">
          <time datetime="{{ latest_post.date | date_to_xmlschema }}">
            {{ latest_post.date | date: "%B&nbsp;%d, %Y" }}
          </time>
        </p>
        <p class="leading-relaxed mb-6">
          {{ latest_post.excerpt | strip_html | truncate: 160 }}
        </p>
        <a href="{{ latest_post.url | relative_url }}" class="btn-outline">
          Continue Reading
        </a>
      </article>
    {% else %}
      <p class="mt-6 text-gray-600">
        No posts yet—first article drops soon.
      </p>
    {% endif %}
  </div>
</section>

<!-- CTA BANNER -->
<section class="py-14 bg-orange text-white text-center">
  <h2 class="text-2xl md:text-3xl font-semibold">
    Ready to Tame Your Toughest System?
  </h2>
  <p class="mt-2 mb-6 text-lg">
    Let’s talk models, controls, and measurable results.
  </p>
  <a href="{{ '/contact/' | relative_url }}" class="btn-primary-inverse">
    Contact&nbsp;Me
  </a>
</section>
