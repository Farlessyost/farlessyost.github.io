"""Prepare selected JEM 473 presentation assets without executing its source.

Usage: python scripts/extract-drone-moving-base-assets.py path/to/presentation.zip
Requires Pillow. Only the explicitly listed members are read from the archive.
"""

import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile

from PIL import Image, ImageOps


ASSETS = (
    ("Jackal_w_drone_1.jpg", "platform.jpg"),
    ("Top_Level_Drone_Jackal.png", "architecture.png"),
    ("Ros_Comm.png", "ros.png"),
    ("Jackal_Circles.png", "path.png"),
    ("Flight_Control.png", "flight-control.png"),
    ("Attitude_Controller.PNG", "attitude.png"),
    ("Control_Mixer.PNG", "mixer.png"),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = root / "assets" / "images"
    output.mkdir(parents=True, exist_ok=True)
    record = {"source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(), "assets": []}

    with ZipFile(args.source) as archive:
        for member, name in ASSETS:
            if archive.getinfo(member).file_size > 25_000_000:
                raise ValueError(f"Unexpected image size: {member}")
            original = archive.read(member)
            target = output / f"drone-moving-base-{name}"
            with Image.open(io.BytesIO(original)) as source_image:
                source_size = source_image.size
                if target.suffix == ".jpg":
                    photo = ImageOps.exif_transpose(source_image).convert("RGB")
                    photo.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                    photo.save(target, quality=88, optimize=True, progressive=True, exif=b"")
                    size = photo.size
                else:
                    target.write_bytes(original)
                    size = source_size
            record["assets"].append({
                "member": member,
                "source_sha256": hashlib.sha256(original).hexdigest(),
                "source_dimensions": source_size,
                "path": target.relative_to(root).as_posix(),
                "dimensions": size,
                "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                "processing": "resized JPEG, no crop, EXIF omitted" if target.suffix == ".jpg" else "original bytes",
            })
            print(f"Prepared {target.name}: {size[0]} x {size[1]}")

    (root / "scripts" / "drone-moving-base-media.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
