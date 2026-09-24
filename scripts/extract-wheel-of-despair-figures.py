"""Extract original Wheel of Despair report figures for the portfolio.

Usage: python scripts/extract-wheel-of-despair-figures.py path/to/report.pdf
Requires PyMuPDF. This extracts embedded images; it does not modify the PDF.
"""

import argparse
import hashlib
import json
from pathlib import Path

import pymupdf


FIGURES = (
    (3, 568, 599, "apparatus", "1"),
    (5, 312, 261, "free-body", "2"),
    (8, 1339, 420, "response", "3"),
    (12, 1006, 501, "root-locus", "6b"),
    (15, 1135, 345, "simulink", "7"),
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
        for page, width, height, name, figure in FIGURES:
            matches = [item for item in document[page - 1].get_images() if item[2:4] == (width, height)]
            if len(matches) != 1:
                raise ValueError(f"Expected one {width} x {height} image on PDF page {page}; found {len(matches)}")
            extracted = document.extract_image(matches[0][0])
            extension = "jpg" if extracted["ext"] == "jpeg" else extracted["ext"]
            target = output / f"wheel-of-despair-{name}.{extension}"
            target.write_bytes(extracted["image"])
            record["figures"].append({
                "path": target.relative_to(root).as_posix(),
                "pdf_page": page,
                "figure": figure,
                "width": width,
                "height": height,
                "sha256": hashlib.sha256(extracted["image"]).hexdigest(),
            })
            print(f"Extracted Figure {figure} on PDF page {page}: {target.name}")

    (root / "scripts" / "wheel-of-despair-media.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
