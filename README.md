# William Farlessyost’s portfolio

A responsive Jekyll website for GitHub Pages, with engineering projects, research case studies, background, publications, and contact information. No external font or CDN is required. A small optional script controls assembly rotation; the content and GIFs also work without JavaScript.

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
- Project Markdown files: case-study content and metadata. `group: build` features engineering projects; `group: research` displays the research list. `order` controls position.
- `_layouts/` and `_includes/`: shared page structure.
- `assets/css/site.css`: typography, layout, responsive styles, and print styles.
- `_config.yml`: contact links and site metadata.
- `assets/images/`: turntable GIFs and still frames exported from the current engineering CAD models.
- Existing root research figures, headshot, and résumé are retained.

The Lunabotics senior-design page is at `/projects/lunabotics/`. Its six original presentation figures can be extracted again with `python scripts/extract-lunabotics-figures.py path/to/presentation.pdf` (requires PyMuPDF). Source slides and image hashes are recorded in `scripts/lunabotics-media.json`.

The Wheel of Despair controls page is at `/projects/wheel-of-despair/`. Its report figures can be extracted with `python scripts/extract-wheel-of-despair-figures.py path/to/report.pdf` (requires PyMuPDF). The page uses four of the five extracted figures. Source pages and image hashes are recorded in `scripts/wheel-of-despair-media.json`.

The drone and moving-base project is at `/projects/drone-moving-base/`. Extract its seven presentation assets with `python scripts/extract-drone-moving-base-assets.py path/to/JEM_473_Presentation.zip` (requires Pillow). The photograph is resized for the web and the diagrams retain their original pixels. Provenance and hashes are recorded in `scripts/drone-moving-base-media.json`.

The four pre-existing research `.html` URLs, `/about/`, and `/projects/` are preserved. Project pages include `/projects/peepin-on-papaw/` and `/projects/tetherxyz/`. The former `/projects/xyz-robot/`, `/projects/skopeo/`, and `/projects/tetherframe/` URLs redirect directly to TetherXYZ, preserving query strings and section anchors when JavaScript is available. Engineering source and media filenames retain their existing names.

The shared robotic arm page is at `/projects/robotic-arm-experience/`, with separate undergraduate research sections for the UR3e/RG2 (`#ur3e-rg2`) and Jenga (`#jenga-robot`) projects. Edit `robotic-arm-experience.md` to update both. It attributes the owner's work to ROS, Gazebo, and MoveIt integration; learning algorithms belong to the wider research teams. The two native video players use reconstructed Gazebo demonstrations recorded in September 2026, with H.264 MP4 files in `assets/videos/` and matching JPEG posters in `assets/images/`. Media hashes and simulation assumptions are recorded in `scripts/robotic-arm-media.json`. Original research sources and attribution notes are in `CONTENT_NOTES.md`.

## Publication

This remains compatible with GitHub Pages’ Jekyll build from the repository root. Updating the live site requires publishing the reviewed changes to the branch configured in repository Settings → Pages. Work in the redesign branch does not change the live site.

See `CONTENT_NOTES.md` for source provenance and items to revisit when personal details or prototypes change.

## Engineering imagery

`scripts/render-portfolio.py` renders FreeCAD geometry through VTK, without screenshots, review annotations, or interface overlays. Papaw uses all three current ultracompact enclosures and the latest AAA retaining frames. `scripts/papaw_components.py` supplies representative electronics based on the selected product photographs; these are presentation models with approximate small details. XYZ uses its active V34 whole-robot assembly. `scripts/xyz_appearance.py` adds representative servo cases, camera electronics, lenses, and material finishes to that saved geometry. This original CAD renderer produces a full rotation in 9.6 seconds with a charcoal background; the photorealistic animations described below are the current website assets. Individual views are 960 × 640 pixels; the three-module card animation is 720 × 480. Static frames support pausing and reduced-motion preferences. Source SHA-256 hashes are recorded in `scripts/render-sources.json`. The scripts and their supporting notes are excluded from the public build.

To regenerate the turntables, run the renderer with FreeCAD’s Python runtime and supply `--papaw-cad`, `--xyz-cad`, `--output`, `--ffmpeg`, and a temporary `--review-dir`. The CAD arguments point to the ultracompact sensor and V34 wrist directories; output goes to `assets/images/`. Use `--only papaw` for the four Papaw views or `--only xyz` for the two XYZ views. Component lettering uses the Windows Arial font.

The renderer publishes completed files with atomic renames so the preview watcher cannot copy partially encoded animations. Turntable URLs include a build timestamp to refresh browser caches after updates.

## Photorealistic assembly animations

The eight project GIFs use FreeCAD/LuxCore studio renders at 720 × 480. Each 9.3 second loop rotates the assembled model, separates its components, reassembles it, and resumes rotation. Papaw begins with fitted covers. The individual modules appear in an expandable section. Matching first-frame posters support pause and reduced motion. Source hashes and phase validation are recorded in `scripts/photoreal-render-sources.json`.

The reusable scene files and `build_sequence_scenes.py`, `render_assembly_sequences.py`, and `embed_sequences.py` are in `C:/Users/wbfar/Portfolio Renders/2026-09-14`. The assembly renderer reuses unchanged XYZ rotation frames and reverses the separation frames for exact recombination. Completed GIFs and posters are copied atomically. Its filenames end in `-sequence`, so the original CAD renderer cannot overwrite them. All scripts and source records remain excluded from the public build.
