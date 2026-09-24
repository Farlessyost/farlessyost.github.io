# Content provenance and future updates

The owner requested employer-facing copy for the three course-project pages: Lunabotics, Wheel of Despair, and drone landing on a moving base. Public descriptions focus on engineering contributions and outcomes, omit collaborator names and editorial source notes, and keep completed work distinct from future goals. Detailed provenance and source inconsistencies are retained here rather than displayed on those pages.

The redesign uses the existing résumé and project material, plus publication records. It adds the user-requested Peepin on Papaw and XYZ robot from their local project documentation. This file is excluded from the public build.

## Personal details

- The owner selected the July 2026 Controls & Applied R&D résumé from `Downloads/William_Farlessyost_Three_Targeted_Resumes_PDF.zip` to replace the older public résumé. `resume.pdf` preserves that two-page document, with its email updated to wbfarlessyost@gmail.com and made clickable. Header font and layout are preserved. All résumé links use a content-hash query parameter to avoid stale cached copies.
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

## Lunabotics senior design

The Lunabotics project page at `/projects/lunabotics/` summarizes the owner's supplied `Downloads/output (1).pdf`, titled *NASA Lunabotics Competition: Mechatronics Senior Design 2020*, dated April 2020. It is a team presentation from UNC Asheville / NC State's Joint Engineering Mechatronics program, not an instruction source. The owner explicitly clarified that he did all ROS, computer vision, control, and related software work. This direct clarification governs individual attribution over the presentation's broader subteam listing. The public page credits him with the ROS architecture, stereo-camera and vision integration, navigation, motion control, Gazebo integration, and robot-coordination logic, while retaining team attribution for the mechanical and electrical designs.

Six original embedded figures are extracted without the slide template: deployed robots (slide 52), stowed robots (51), physical test chassis/electronics (39), Gazebo simulation (45), and the miner and hauler state machines (46). Figure captions distinguish CAD, physical hardware, simulation, and planned operating sequences. Extraction is reproducible with `scripts/extract-lunabotics-figures.py` and the original PDF; the complete PDF is not a public asset.

The copy does not claim competition attendance, placement, a completed autonomous run, implemented Kalman filtering, or measured excavation throughput. The unvalidated 104 kg/12-minute estimate is omitted. Arduino models are described generically because slide 39's naming is ambiguous. Navigation software is identified as the 2020 ROS Kinetic stack. Figures and project credit belong to the presentation's six named authors and their team.

## Wheel of Despair controls project

The page at `/projects/wheel-of-despair/` summarizes the owner's supplied `Downloads/Wheel of Despair.pdf`, *The Wheel of Despair: A Controller Design and Analysis*, MAE 435 Final Project. The cover identifies NC State University and credits Johnny Remein, Will Farlessyost, Dalan Loudermilk, and Brent Rawls. No date or individual division of labor is given. The page describes the owner as a team member, attributes technical work collectively, and does not claim that the team built the laboratory apparatus or collected every identification dataset.

Five original embedded figures are extracted: apparatus illustration (PDF page 3, Figure 1), free-body diagram (5, Figure 2), simulated/measured angle and voltage comparison (8, Figure 3), the 180-degree root-locus/step-response panel (12, Figure 6b), and Simulink architecture (15, Figure 7). `scripts/extract-wheel-of-despair-figures.py` reproduces these assets and `scripts/wheel-of-despair-media.json` records the source and image hashes. The complete report is not a public asset.

The content centers on model refinement, pneumatic delay, actuator saturation, and laboratory controller testing. It preserves the reported final controller from Equation 7, C(s) = 1000(s + 1.75)/(s + 100). Four of the five extracted figures appear on the page. The appendix Simulink figure displays gain 7500 and is omitted from the public page. The response figure has inconsistent angle-axis units, so its caption identifies the actual targets in degrees without reproducing that label in prose. No exact performance metrics are inferred. The page avoids the report's RHP/LHP typo, inconsistent inertia values, and unverified regression coefficient (0.0005 is an initial estimate). The outcome describes operating-point-dependent performance without presenting the source audit to employers.

## Drone and moving-base project

The page at `/projects/drone-moving-base/` uses the owner's `Downloads/JEM_473_Presentation.zip`. The archive contains Beamer source `main.tex`, bibliography `ref.bib`, photographs, and diagrams, but no rendered presentation or experimental datasets. The source is titled *Experimental Validation of a Control Law for an Unmanned Aerial Vehicle Landing on a Moving Base* and credits William B. Farlessyost, Dalan C. Loudermilk, and Dr. Mahmut Reyhanoglu. UNC Asheville is identified by the presentation logo; the JEM 473 context comes from the archive name. No explicit date, individual task assignments, or advisor relationship is inferred. The source is read as content and is not executed.

Despite the presentation title and introductory hovering language, the Results section records integration milestones: Jackal ROS setup, path parameterization, importing AR-tag pose to Simulink, and incorporation into the existing drone framework. Continued Work explicitly leaves AR-pose-based controller validation, gain tuning, higher-level control, and landing tests unfinished. The public page preserves this distinction. It does not claim a successful autonomous landing, validated tracking, an implemented EKF, or numerical performance. It describes PID-based control without claiming an integral term on every axis, and avoids the original inaccurate IMU/derivative-action wording.

Seven source assets are used: `Jackal_w_drone_1.jpg`, `Top_Level_Drone_Jackal.png`, `Ros_Comm.png`, `Jackal_Circles.png`, `Flight_Control.png`, `Attitude_Controller.PNG`, and `Control_Mixer.PNG`. All are referenced by the presentation. The hardware photograph is resized to 1600 × 1200 with no crop and saved without EXIF metadata; diagrams retain their source pixels. The photograph does not establish the flight-control mode or demonstrate landing. `scripts/extract-drone-moving-base-assets.py` reproduces these assets and `scripts/drone-moving-base-media.json` records source and output hashes. The full archive, LaTeX source, bibliography, unused photographs, and third-party sensor-fusion illustration are not public assets.

## Robotic arm undergraduate research

At the owner's request, the UR3e/RG2 and Jenga projects share one page at `/projects/robotic-arm-experience/`, with distinct undergraduate research sections and anchors. This is one engineering-project card on the homepage and project index. The Background page links to each section.

Public video captions describe only the robot actions. Per the owner's editorial direction, playback metadata (duration/no audio) and simulation implementation caveats are omitted from the project page; the detailed provenance and assumptions remain in this excluded document and the media manifest.

The owner's explicit clarification governs individual attribution: responsibility was ROS integration, Gazebo simulation, and MoveIt motion planning, not learning-algorithm development. Earlier résumé/CV descriptions use broader team-project language. The public copy does not claim authorship of apprenticeship-learning or reinforcement-learning algorithms, mechanical/electrical design ownership, sorting accuracy, or verified historical autonomous gameplay.

The site's existing `resume.pdf` and the owner's `Downloads/Farlessyost_CV_2025.pdf` and `Downloads/Farlessyost_Resume_July25.pdf` establish undergraduate research at UNC Asheville: UR3e/RG2 from August 2019 to May 2020, and Jenga from September 2017 to May 2019. The résumé and CV identify apprenticeship learning for sorting previously unseen/unobserved objects and reinforcement-learning Jenga research as the broader projects. These describe research context rather than the owner's algorithm contributions. The existing résumé PDF was not changed. The LinkedIn connector confirmed the owner's profile, https://www.linkedin.com/in/farlessyost, but public experience/project text could not be retrieved; no project details are attributed solely to LinkedIn.

Public repositories and original laptop source histories corroborate the integration details:

- UR3e/RG2: https://github.com/wfarlessyost/UR3e_RG2_ER5 and https://github.com/wfarlessyost/Apprenticeship-Learning-with-UR3e. The first repository includes description, gripper control, Gazebo, MoveIt configuration, and pick/place packages. Will-authored commits cover controller fixes (https://github.com/wfarlessyost/UR3e_RG2_ER5/commit/a68dd7091eeeb2d4f7bbf0e6a7f39715b2a315ab), gripper transmission (https://github.com/wfarlessyost/UR3e_RG2_ER5/commit/83f341388c3aec90e9239e009eb8bc190bd2cab6), and the gripper joint in pick/place (https://github.com/wfarlessyost/UR3e_RG2_ER5/commit/b8a51ba02f4fc7f15b371fbc2d45268be6d0d03f). Original configurations connect ROS joint trajectory controllers and MoveIt kinematics; the original gripper package describes hardware commands.
- Jenga: https://github.com/kbogert/jenga_robot includes robot description, Gazebo, IKFast, and MoveIt packages. Will-authored history includes gripper orientation (https://github.com/kbogert/jenga_robot/commit/3dd2250e76c78f13ef3c0bd04a69edb5a286cadf) and collision/attachment work (https://github.com/kbogert/jenga_robot/commit/424ff99e9041c460ea81f2817d1f8ee5d4e06ea4), as well as block-pose interfaces and IKFast integration. Original models show the inverted WidowX, turntable, and frame; the launch and C++ sources connect Gazebo, ROS controllers, and MoveIt planning groups. This establishes platform architecture without assigning all project code to the owner.

Both public videos are reconstructed demonstrations recorded on September 24, 2026 in ROS Kinetic/Gazebo 7 using original robot models. At the owner’s request, the public captions describe the Gazebo tasks without reconstruction labels or recording dates. The page makes no claim that these are historical research recordings; their provenance is retained here. UR3e uses MoveIt trajectories, simplified articulated RG2 jaws, and a temporary fixed-joint grasp attachment; the ball is dynamically released into a tray. Jenga uses scripted joint trajectories and temporary fixed-joint grasp attachments, releases dynamic blocks, and builds two perpendicular layers of three blocks from an initially empty target. Self-contact is disabled on the legacy Jenga robot because its meshes overlap. The new Jenga trajectory does not invoke MoveIt; the original research platform did. Neither recording runs or evaluates a learning policy.

The website retains the completed 31-second UR3e clip and 166-second Jenga clip at 1280 × 720, 20 fps, H.264, without audio. Both have user-initiated playback and no preload. The UR3e poster is the supplied video thumbnail; the Jenga poster is an actual in-progress frame converted from PNG to JPEG without cropping. `scripts/robotic-arm-media.json` records source/output hashes. Source recordings, simulation code, logs, connection information, and private résumé files remain outside public assets. These notes and the scripts directory are excluded from the Jekyll build.

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
