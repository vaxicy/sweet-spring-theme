#!/usr/bin/env python3
"""Resize the chosen blossom candidate into the 128px theme icon (logo/).

Chrome themes only use the 128px icon, so no other sizes are generated.
"""
import os
from PIL import Image

ROOT = os.path.join(os.path.dirname(__file__), "..")
SRC = os.path.join(ROOT, "store-assets", "icon-candidates", "logo-A-blossom.png")
OUT_DIR = os.path.join(ROOT, "logo")
os.makedirs(OUT_DIR, exist_ok=True)

with Image.open(SRC) as img:
    assert img.size == (512, 512), f"source must be 512x512, got {img.size}"
    for size in (128,):
        out = img.resize((size, size), Image.LANCZOS)
        path = os.path.join(OUT_DIR, f"logo{size}.png")
        out.save(path)
        print("saved", os.path.abspath(path))
