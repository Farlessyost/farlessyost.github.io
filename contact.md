---
layout: page
title: Contact
permalink: /contact/
description: Email, LinkedIn, and résumé for William Farlessyost.
---
<section class="contact-page shell">
  <h1>Contact</h1>
  <div class="contact-layout"><div><p class="page-deck">Contact me about engineering roles, research opportunities, or my projects.</p></div>
  <div class="contact-links">{% if site.email and site.email != '' %}<a href="mailto:{{ site.email }}"><span><small>Email</small>{{ site.email }}</span><span aria-hidden="true">↗</span></a>{% endif %}<a href="{{ site.linkedin }}"><span>LinkedIn</span><span aria-hidden="true">↗</span></a><a href="{{ '/resume.pdf' | relative_url }}"><span>Résumé (PDF)</span><span aria-hidden="true">↗</span></a></div></div>
</section>
