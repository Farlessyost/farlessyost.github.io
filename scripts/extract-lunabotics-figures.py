"""Extract the original Lunabotics presentation figures for the portfolio.

Usage: python scripts/extract-lunabotics-figures.py path/to/presentation.pdf
Requires PyMuPDF. This extracts embedded images; it does not modify the PDF.
"""

import argparse
import hashlib
import json
from pathlib import Path

import pymupdf


FIGURES = (
    (52, 1526, 861, "robots-deployed"),
    (51, 1526, 861, "robots-stowed"),
    (39, 1200, 1600, "test-chassis"),
    (45, 1116, 650, "gazebo"),
    (46, 1187, 417, "miner-states"),
    (46, 1176, 385, "hauler-states"),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = root / "assets" / "images"
    output.mkdir(parents=True, exist_ok=True)
    record = {"source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(), "figures": []}

    with pymupdf.open(args.source) as document:
        for page, width, height, name in FIGURES:
            matches = [item for item in document[page - 1].get_images() if item[2:4] == (width, height)]
            if len(matches) != 1:
                raise ValueError(f"Expected one {width} x {height} image on slide {page}; found {len(matches)}")
            extracted = document.extract_image(matches[0][0])
            extension = "jpg" if extracted["ext"] == "jpeg" else extracted["ext"]
            target = output / f"lunabotics-{name}.{extension}"
            target.write_bytes(extracted["image"])
            record["figures"].append({
                "path": target.relative_to(root).as_posix(),
                "slide": page,
                "width": width,
                "height": height,
                "sha256": hashlib.sha256(extracted["image"]).hexdigest(),
            })
            print(f"Extracted slide {page}: {target.name}")

    (root / "scripts" / "lunabotics-media.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
