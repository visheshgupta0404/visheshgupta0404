"""Build the GitHub profile's floating banner and a still version.

Requires Python 3.10+ and Pillow (pip install Pillow).
Run from anywhere: python scripts/build_banner.py
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
WIDTH, HEIGHT = 1200, 280
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')

def font(size, bold=False, mono=False):
    name = 'DejaVuSansMono.ttf' if mono else 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    for path in [FONT_DIR / name, Path(name), Path('/Library/Fonts/Arial.ttf'), Path('C:/Windows/Fonts/arial.ttf')]:
        try:
            return ImageFont.truetype(str(path), size)
        except OSError:
            pass
    return ImageFont.load_default(size=size)

def frame(index):
    image = Image.new('RGB', (WIDTH, HEIGHT), '#101828')
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((1, 1, WIDTH-2, HEIGHT-2), radius=20, outline='#344054', width=2)
    d.line((44, 57, 75, 57), fill='#8b9aff', width=4)
    d.text((88, 44), 'DEVELOPER PROFILE', font=font(15, mono=True), fill='#a6b3ce')
    d.text((42, 87), 'Vishesh Gupta', font=font(44, bold=True), fill='#f2f4f7')
    d.text((44, 152), 'B.Tech Computer Science  /  Third year', font=font(20), fill='#c8d1e0')
    d.text((44, 212), 'BACKEND DEVELOPMENT   ·   WEB PROJECTS   ·   PROBLEM SOLVING', font=font(12, mono=True), fill='#a6b3ce')
    for x in range(800, 1160, 24):
        for y in range(48, 240, 24):
            d.ellipse((x, y, x+2, y+2), fill='#29354a')
    t = index / 48 * math.tau
    cards = [(838, 65, 112, '</>', '#97a6ff', 0), (1007, 124, 116, '{ }', '#8ed1ce', 2.1), (900, 180, 68, '01', '#c1c9da', 4.2)]
    centers = []
    for x, y, size, text, color, phase in cards:
        y += round(math.sin(t+phase)*7)
        centers.append((x+size/2, y+size/2))
    d.line((centers[0], centers[1]), fill='#3c4961', width=2)
    d.line((centers[1], centers[2]), fill='#3c4961', width=2)
    for (x, y, size, text, color, phase), center in zip(cards, centers):
        y = center[1] - size/2
        d.rounded_rectangle((x+4, y+7, x+size+4, y+size+7), radius=15, fill='#0b1220')
        d.rounded_rectangle((x, y, x+size, y+size), radius=15, fill='#1d2939', outline='#475467', width=2)
        d.text(center, text, font=font(28 if size>80 else 18, mono=True), fill=color, anchor='mm')
    return image

frames = [frame(i) for i in range(48)]
frames[0].save(ASSETS / 'profile-banner.png', optimize=True)
# A single shared palette keeps colours stable between animation frames.
palette = frames[0].quantize(colors=96)
frames = [image.quantize(palette=palette, dither=Image.Dither.NONE) for image in frames]
frames[0].save(ASSETS / 'profile-banner.gif', save_all=True, append_images=frames[1:], duration=100, loop=0, optimize=True, disposal=1)
print(f'Created floating banner: {(ASSETS / "profile-banner.gif").stat().st_size:,} bytes')
