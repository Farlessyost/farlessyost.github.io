# William Farlessyost’s portfolio

A responsive Jekyll website for GitHub Pages, with engineering projects, research case studies, background, publications, and contact information. No JavaScript or external font/CDN dependency is required.

## Preview

With Ruby and Bundler installed:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open http://127.0.0.1:4000. To build without a server, use `bundle exec jekyll build`.

## Edit

- `index.md`: homepage.
- `about.md`, `contact.md`, `projects.md`: main pages.
- Project Markdown files: case-study content and metadata. `group: build` features independent engineering; `group: research` displays the research list. `order` controls position.
- `_layouts/` and `_includes/`: shared page structure.
- `assets/css/site.css`: typography, layout, responsive styles, and print styles.
- `_config.yml`: contact links and site metadata.
- `assets/images/`: clean views exported from the current engineering CAD models.
- Existing root research figures, headshot, and résumé are retained.

The four pre-existing research `.html` URLs, `/about/`, and `/projects/` are preserved. New pages include `/contact/`, `/projects/peepin-on-papaw/`, and `/projects/xyz-robot/`.

## Publication

This remains compatible with GitHub Pages’ Jekyll build from the repository root. Updating the live site requires publishing the reviewed changes to the branch configured in repository Settings → Pages. Work in the redesign branch does not change the live site.

See `CONTENT_NOTES.md` for source provenance and items to revisit when personal details or prototypes change.

## Engineering imagery

`scripts/render-portfolio.py` renders saved FreeCAD geometry through VTK, without screenshots, review annotations, or interface overlays. The current sources are Papaw’s installed AAA retrofit model and XYZ’s active V34 whole-robot assembly. Source SHA-256 hashes are recorded in `scripts/render-sources.json`. Neither the renderer nor its manifest is included in the public build.
