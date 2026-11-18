import os
from PIL import Image

targets = [
    'img/toldo-trailer.jpg',
    'img/home-img-1.jpg',
    'img/home-img-2.jpg',
    'img/jefe.jpg',
    'img/aicicon.jpg',
]

for p in targets:
    if not os.path.exists(p):
        continue
    orig_size = os.path.getsize(p)
    im = Image.open(p)
    w, h = im.size
    print(f"{p}: {w}x{h}, {orig_size/1024:.1f} KB, format={im.format}")

