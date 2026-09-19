#!/usr/bin/env python3
"""Generate 4 PIL-drawn logo candidates for the Sweet Spring Chrome theme."""
import math
import os
from PIL import Image, ImageDraw, ImageChops

OUT = os.path.join(os.path.dirname(__file__), "..", "store-assets", "icon-candidates")
SIZE = 512
RADIUS = 112  # rounded corner
PINK = (249, 178, 215)
GREEN = (246, 255, 220)
BLUE = (207, 236, 243)
WHITE_PINK = (255, 250, 252)
DEEP_GREEN = (190, 224, 168)
GREEN_LEAF = (186, 222, 158)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def new_canvas():
    return Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))


def rounded_mask(radius=RADIUS):
    m = Image.new("L", (SIZE, SIZE), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=radius, fill=255)
    return m


def base_shape(gradient=None, fill=None):
    """Return RGBA image with rounded-square shape filled with gradient/fill, rest transparent."""
    img = new_canvas()
    mask = rounded_mask()
    if gradient is not None:
        top, bottom = gradient
        grad = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        gd = ImageDraw.Draw(grad)
        for y in range(SIZE):
            t = y / (SIZE - 1)
            c = lerp(top, bottom, t)
            gd.line([(0, y), (SIZE, y)], fill=c + (255,))
        img.paste(grad, (0, 0), mask)
    else:
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=RADIUS, fill=fill + (255,))
    return img


def paste(img, layer):
    img.alpha_composite(layer)


# ---------- A: Blossom ----------
def make_blossom():
    img = base_shape(fill=WHITE_PINK)
    cx, cy = SIZE // 2, SIZE // 2 + 10
    d_center, pw, pl = 88, 112, 150
    # union of petal alphas -> single solid fill, no seams between petals
    mask = Image.new("L", (SIZE, SIZE), 0)
    for i in range(5):
        layer = Image.new("L", (SIZE, SIZE), 0)
        ld = ImageDraw.Draw(layer)
        ld.ellipse([cx - pw // 2, cy - d_center - pl // 2,
                    cx + pw // 2, cy - d_center + pl // 2], fill=255)
        layer = layer.rotate(i * 72, center=(cx, cy), resample=Image.BICUBIC)
        mask = ImageChops.lighter(mask, layer)
    pink = Image.new("RGBA", (SIZE, SIZE), PINK + (255,))
    img.paste(pink, (0, 0), mask)
    d = ImageDraw.Draw(img)
    d.ellipse([cx - 46, cy - 46, cx + 45, cy + 45], fill=GREEN + (255,))
    d.ellipse([cx - 24, cy - 24, cx + 23, cy + 23], fill=DEEP_GREEN + (255,))
    return img


# ---------- B: Sprout ----------
def make_sprout():
    img = base_shape(gradient=(PINK, GREEN))
    cx = SIZE // 2
    d = ImageDraw.Draw(img)
    # stem
    d.line([(cx, 360), (cx, 250)], fill=GREEN_LEAF + (255,), width=22, joint="curve")
    # left leaf
    leaf = Image.new("RGBA", (150, 90), (0, 0, 0, 0))
    ld = ImageDraw.Draw(leaf)
    ld.ellipse([0, 0, 149, 89], fill=GREEN_LEAF + (255,))
    leaf = leaf.rotate(-35, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(leaf, (cx - 150, 250))
    # right leaf
    leaf2 = leaf.transpose(Image.FLIP_LEFT_RIGHT)
    img.alpha_composite(leaf2, (cx + 10, 250))
    # bud
    d.ellipse([cx - 34, 205, cx + 33, 272], fill=PINK + (255,))
    return img


# ---------- C: Candy heart ----------
def heart_points(cx, cy, scale):
    pts = []
    for t in [i * math.pi / 60 for i in range(121)]:
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((int(cx + x * scale), int(cy - y * scale)))
    return pts


def make_candy():
    img = base_shape(gradient=(PINK, (255, 214, 235)))
    d = ImageDraw.Draw(img)
    pts = heart_points(SIZE // 2, SIZE // 2 + 30, 13)
    d.polygon(pts, fill=(235, 130, 185, 255))
    return img


# ---------- D: Split ----------
def make_split():
    full = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    fd = ImageDraw.Draw(full)
    fd.polygon([(0, 0), (SIZE, 0), (0, SIZE)], fill=PINK + (255,))
    fd.polygon([(SIZE, 0), (SIZE, SIZE), (0, SIZE)], fill=GREEN + (255,))
    img = new_canvas()
    img.paste(full, (0, 0), rounded_mask())  # clip to rounded corners
    d = ImageDraw.Draw(img)
    d.ellipse([SIZE // 2 - 60, SIZE // 2 - 60, SIZE // 2 + 59, SIZE // 2 + 59], fill=(255, 255, 255, 255))
    d.ellipse([SIZE // 2 - 36, SIZE // 2 - 36, SIZE // 2 + 35, SIZE // 2 + 35], fill=(255, 250, 252, 255))
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    makers = {"A-blossom": make_blossom, "B-sprout": make_sprout,
              "C-candy": make_candy, "D-split": make_split}
    for name, fn in makers.items():
        p = os.path.join(OUT, f"logo-{name}.png")
        fn().save(p)
        print("saved", os.path.abspath(p))


if __name__ == "__main__":
    main()
