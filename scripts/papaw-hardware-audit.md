# Papaw component references

Updated 14 September 2026. These are selected references, not a record of purchases.

## Product photographs

| Part | Selected Amazon listing | Observed pack price |
| --- | --- | ---: |
| ESP32-C3 Super Mini, headers uninstalled | DWEII, https://www.amazon.com/dp/B0CW62PPZ1 | $11.99 / 3 |
| HC-SR501 PIR | Heexmkv, https://www.amazon.com/dp/B0FM2L4X5D | $3.98 / 2 |
| 5 V buck-boost module | Teyleten Robot, https://www.amazon.com/dp/B0GCW44FDL | $12.99 / 5 |
| 0.96 inch yellow/blue I2C OLED | Dorhea, https://www.amazon.com/dp/B07FK8GB8T | $5.99 / 1 |

Prices were checked on 14 September 2026 and exclude applicable tax and shipping. These are the lowest-cost suitable candidates found in the checked listings, not an exhaustive market comparison. The regulator photograph is marked XL63070 although the listing title says TPS63070.

## Visual representation

The owner requested reasonably close component models based on these product references. `papaw_components.py` constructs recognizable geometry: the ESP board's diagonal IC, ceramic antenna, crystal, switches, plated holes and hollow USB-C port; the PIR's faceted lens, trimmers and capacitors; the regulator's inductor, selector pads and components; and the OLED's glass, flex ribbon and four-pin connection.

Small component dimensions and lens geometry are approximations. No manufacturer CAD, supplier certification, or physical fit verification is claimed. The OLED uses the current enclosure's 27.6 mm PCB and 23.5 mm mounting pattern; the selected listing alone does not verify that pitch. The screen is shown unlit rather than with fictional activity data.

The printed geometry comes directly from the three `ultracompact_v1/output` FCStd documents. The sensor and door modules retain their respective current `aaa_retrofit/output` frames, cells, contacts, and series wiring. The source projects are read only. The door module includes its separate magnet pod and a modeled glass reed capsule with metal contacts.

## Module mapping

- Motion: HC-SR501, ESP32-C3, 5 V regulator, three AAA cells, directional enclosure.
- Door: reed switch and separate magnet pod, ESP32-C3, 5 V regulator, three AAA cells.
- Receiver: ESP32-C3, 0.96 inch OLED, USB power.

No downloaded third-party CAD models or product photographs are redistributed in the website. These source notes are excluded from the public Jekyll build.
