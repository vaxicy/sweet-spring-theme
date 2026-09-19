#!/usr/bin/env python3
"""Build the Chrome theme upload package and copy it to the default folder.

The package contains the unpacked extension (manifest.json + logo/), zipped
without a top-level folder so Chrome Web Store accepts it directly.

Output:
  <project>/sweet-spring-theme-v<version>.zip
  <default-folder>/sweet-spring-theme-v<version>.zip   (D:\\...\\vibe coding)
"""
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = Path(__file__).resolve().parents[3]  # D:\迅雷下载\vibe coding

with open(ROOT / "manifest.json", encoding="utf-8-sig") as f:
    version = json.load(f)["version"]

NAME = "sweet-spring-theme"
zname = f"{NAME}-v{version}.zip"
zpath = ROOT / zname

with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(ROOT / "manifest.json", "manifest.json")
    logo_dir = ROOT / "logo"
    for p in sorted(logo_dir.rglob("*")):
        if p.is_file():
            z.write(p, f"logo/{p.name}")

print("built ", zpath, zpath.stat().st_size, "bytes")

DEFAULT.mkdir(parents=True, exist_ok=True)
dst = DEFAULT / zname
shutil.copy(zpath, dst)
print("copied", dst, dst.stat().st_size, "bytes")

with zipfile.ZipFile(zpath) as z:
    print("contents:", z.namelist())
