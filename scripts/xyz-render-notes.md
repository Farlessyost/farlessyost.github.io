# XYZ turntable appearance

The owner requested reasonably close component appearance for the portfolio. These additions are representative presentation geometry, not exact supplier CAD or a manufacturing fit check.

## Sources

- The active `wrist_integrated_v34/output/XYZ_V34_Whole_Robot.FCStd` supplies the machine, hardware placement, and tool pose.
- `XYZ_V34_Integrated_Wrist.FCStd` supplies the local SG90, encoder, and IMU reference positions.
- `esp32_print_mount_v33/output/AITRIP_Stereo_15mm_V33.FCStd` supplies the camera assembly, board envelopes, lens positions, and original component colors. The source design identifies the AITRIP ESP32-CAM kit, Amazon B097BLT24K.
- The [TowerPro SG90 reference](https://towerpro.com.tw/product/sg90-7/) supports the recognizable blue micro-servo appearance. Case details use the existing design's 12.2 mm width and 22.7 mm body length; seams, labels, screws, and lead tails are approximate.

## Presentation changes

- Separate blue servo case sections, rounded gearbox covers, mounting holes, screws, labels, and three colored lead tails.
- Camera PCBs, header pins, shield cans, antenna traces, SD sockets, connectors, and small surface-mounted parts.
- Dark lens barrels with focus grooves and coated glass, separated from the printed camera housing.
- Sensor boards with mounting holes, chips, and pads at the saved encoder and IMU positions.
- Original camera enclosure colors, differentiated metal and plastic finishes, and procedural timber grain.

The board footprints, component types, and assembly placements come from the design. Small electronic layouts and lead tails are illustrative. The renderer opens engineering documents read only and does not save modifications to them.

Each replaced part is registered from its source vertices to the corresponding saved assembly vertices. The renderer rejects topology mismatches and registration residuals above 0.00001 mm, and writes the measured residuals to the temporary review directory. Both full-machine and wrist views use the same detailed parts. Source hashes are retained in `render-sources.json`.
