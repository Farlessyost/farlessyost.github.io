# Content provenance and future updates

The redesign uses the existing résumé and project material, plus publication records. It adds the user-requested Peepin on Papaw and XYZ robot from their local project documentation. This file is excluded from the public build.

## Personal details

- Education and fellowship history are supported by `resume.pdf`. Its contact email has been updated to the owner’s current address; other content is unchanged.
- Current employment is not inferred from the old résumé’s “Aug. 2020–Present” research-assistant entry. Website copy says “doctoral research at Purdue.”
- The email is maintained from the owner’s direct updates. LinkedIn comes from the résumé.
- The former business and GitHub profile links have been removed at the owner’s request.

## Publications

- Reduced-order models: https://doi.org/10.1007/s11071-022-07695-x
- Hybrid algae modeling: https://doi.org/10.69997/sct.121371
- Sensor minimization preprint: https://arxiv.org/abs/2509.11336
- Climate resilience, now published: https://doi.org/10.1111/jiec.70087

The original research presentation figures are preserved; wording avoids precise climate milestone dates that differ between presentation and publication. Quantitative performance and hardware-savings claims were not invented.

## Research method walkthroughs

Four interactive SVG walkthroughs explain the doctoral research methods. They were checked against the owner's `Downloads/Defense.pdf` (methodology pages 9, 20, 24, 30, and 43), `Downloads/Farlessyost_Thesis_5_6_compressed.pdf` (chapters 2 through 5), and the cited publications. The defense PDF contains presentation slides, not a spoken transcript. No defense transcript was located in the relevant folders. Academic records, private discussions, and manuscript review correspondence are not public website assets.

The diagrams illustrate the method, not reconstructed experimental data. Candidate-function tiles, sparse matrix positions, and sensitivity-bar lengths are schematic, without numerical results or claims that particular illustrated coefficients/channels were selected. Existing original presentation plots remain the source of displayed results. The algae correction is added at the derivative level before integration, as specified in the thesis. Copy acknowledges unstable folds rather than implying every correction improved validation. The sensor explanation distinguishes fitted-model sensitivity, derived features, and physical sensor counts. The stock equation is a simplified single-stock mass balance explaining the network, not a claim to reproduce its full set of governing equations. Original source files remain unchanged.

Walkthroughs use local HTML, SVG, CSS, and JavaScript. Playback is user-initiated, can be paused or stepped manually, stops at the end or when offscreen, and respects reduced-motion preferences. The full step explanations remain available without JavaScript and in print.

## Independent projects

The owner selected the public scanner name TetherXYZ, at `/projects/tetherxyz/`. The former `/projects/xyz-robot/`, `/projects/skopeo/`, and `/projects/tetherframe/` URLs redirect directly to it. Original project directories, CAD sources, scripts, and media filenames retain XYZ for continuity.

The owner requested that citations on the two independent-project pages support the human need and project motivation. Public footnotes now cite AARP's 2024 Home and Community Preferences Survey (75% of U.S. adults 50+ prefer to stay in their current home), AARP/NAC's Caregiving in the US 2025 (63 million U.S. family caregivers; seven in ten employed), Fleming et al.'s 2021 Lancet Commission on diagnostics (47% estimate for diagnostics overall), and World Health Assembly resolution WHA78.13 (2025), paragraphs 1(2), 1(3), 1(5), and 1(7). These sources support aging-at-home and caregiving needs, diagnostic access, and the relevance of affordable, maintainable equipment. They do not evaluate these prototypes or establish clinical effectiveness, caregiver outcomes, costs, or patient readiness. Technical explanations remain on the pages, with the general engineering reference footnotes removed. No personal diagnosis or family medical history is inferred.

Peepin on Papaw sources: `doorway-monitor/README.md`, Android pilot documentation, ultracompact enclosure documentation and AAA retrofit notes. Images show the motion sensor, magnetic door sensor with separate magnet pod, and OLED receiver. Current enclosure and battery-frame geometry is preserved. Electronic components use representative geometry based on the selected Amazon product photographs, with approximate small details as requested. These visualizations do not establish verified manufacturing fit. Source notes are in `scripts/papaw-hardware-audit.md`. No activity logs, household telemetry, private addresses, or credentials are included.

XYZ sources: MuJoCo/ROS simulation README, ESP32 Super Mini firmware README, active assembly metadata, and the V34 wrist README. Images use the September 14 active V34 whole-robot document, showing the complete machine and the wrist. Representative servo cases, camera boards, connectors, sensor boards, and lenses replace simple purchased-component envelopes in the presentation; the engineering source documents remain unchanged. Camera enclosure colors come from the native V33 camera model. Source notes and limitations are in `scripts/xyz-render-notes.md`. The older simulation image and annotated review sheet have been replaced. Main-cable firmware and the unimplemented current wrist hardware driver are distinguished.

Both projects are described as in development. Update prototype status and public links as hardware verification or publication progresses.

## Scanner video

The supplied `whoolookatmeimamedicalscanner.mp4` is a 5:43 simulation recording. The website keeps its full duration, 1080p resolution, 30 fps, and audio in a compressed H.264/AAC MP4 with progressive playback. The original file remains outside the repository. The poster is a frame from 00:30. The video is labeled as a simulation and contains the mechanism and stereo demonstration views.

## Assembly animations

Eight FreeCAD/LuxCore studio animations show the complete XYZ machine, wrist, corner receiver, rod and counterweight assembly, Papaw family, and three individual Papaw modules. Each 720 × 480 GIF rotates for 4.8 seconds, pauses, separates into components, holds the exploded view, and reassembles before rotation resumes. The complete loop is 9.3 seconds. The Papaw covers start fitted and lift away during separation. Purchased electronic modules remain intact while their surrounding parts separate.

The two XYZ close-ups use the active V34 geometry. Timber supports are cropped only in presentation copies to show the local mounting interfaces. The rod view includes its actual saved pulley and rope routes. Engineering source documents are unchanged. These are presentation animations, not validated assembly instructions.

Posters match the first assembled frame and support pause controls and reduced motion. The Status subsections remain removed. All three individual Papaw views are available in an expandable section.

Source hashes, rendering parameters, and animation phase checks are recorded in `scripts/photoreal-render-sources.json`. The local scene files, `build_sequence_scenes.py`, `render_assembly_sequences.py`, and `embed_sequences.py` are saved in `C:/Users/wbfar/Portfolio Renders/2026-09-14`. The wood material is Poly Haven's Coated Pine by Charlotte Baglioni and Rico Cilliers, under CC0: https://polyhaven.com/a/coated_pine and https://polyhaven.com/license.

## App prototype screenshots

The shared website style uses Newsreader headings and IBM Plex Sans body text, with ivory surfaces and dark green accents. Latin WOFF2 files are served locally from `assets/fonts`; their original SIL Open Font Licenses and download sources are included beside them. The redesign changes presentation and the SVG diagram palette. Project text, prototype screenshots, CAD renders, and the scanner video remain the existing assets.

The placement diagrams use SVG to illustrate a jamb-mounted PIR, a frame-mounted magnetic contact with its magnet on the door, and a receiver powered by a USB wall adapter. The owner clarified that the receiver goes at any outlet, so the public placement diagram and descriptions no longer show a computer connection. The original software documentation still records the USB logger used in the prototype; no new transport to the app is asserted. The field of view, door swing, and event timing explain operation rather than measured installation geometry. The diagrams use the existing module render thumbnails. Their buttons only animate the webpage; they do not connect to hardware or log household activity.

The Papaw app screenshots capture the existing `doorway-monitor/dashboard` interface through a separate local preview server with synthetic SQLite events. No household database, real device identifiers, or activity logs were used. The scenario and room-estimation explanations follow the dashboard implementation and README; duty cycling, debouncing, queueing, and duplicate suppression follow the sensor and receiver firmware. The original prototype files remain unchanged. Screenshot preparation is saved in `C:/Users/wbfar/Portfolio Renders/papaw-app-preview`.
