# Sweet Spring — A Chrome Theme

A soft pastel theme for Google Chrome. Sweet pink window frames, a fresh
light-green toolbar, calming blue background tabs, and a white-pink new tab
page bring a gentle spring mood to the whole browser.

## Features

- **Pink frames** — a warm, soft pink wraps every window and tab strip.
- **Fresh toolbar** — a light spring-green toolbar keeps things airy.
- **Calm tabs** — background tabs sit in a soothing blue.
- **White-pink NTP** — the new tab page is near-white with a faint pink tint.
- **Auto-tinted logos** — the Google logo and shortcut icons on the new tab
  page are tinted automatically from the NTP background, so they blend with the
  palette without any extra work.

## Palette

| Element | Color |
| --- | --- |
| Frame | Soft pink `#F9B2D7` |
| Toolbar | Light spring green `#F6FFDC` |
| Background tab | Calm blue `#CFECF3` |
| Button background | Mint `#DAF9DE` |
| New tab background | White pink `#FFFAFC` |
| NTP link | Rose `#A13F72` |

## Install (Load unpacked)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode** (top-right toggle).
4. Click **Load unpacked** and select the project folder.

The same folder can also be zipped and dragged onto the `chrome://extensions`
page, or uploaded to the Chrome Web Store as a theme package.

## Project structure

```
manifest.json          theme definition (colors, tints, properties)
logo/logo128.png       store icon (themes only need the 128px size)
store-assets/          promo tiles + screenshots for the Web Store listing
scripts/               asset-generation helpers (icons, store assets)
```

## Packaging

Run the helper to build the uploadable package and copy it to the default
output folder:

```bash
python scripts/build_zip.py
```

It produces `sweet-spring-theme-v<version>.zip` (the unpacked extension —
`manifest.json` + `logo/`) and copies it to
`D:\迅雷下载\vibe coding\`.

## License

Non-Commercial License. Licensed for personal, non-commercial use; sharing with
attribution is welcome.
