# -*- coding: utf-8 -*-
from PIL import Image

files = {
    'roxar': 'img/products/roxar/roxar.png',
    'rosemount': 'img/products/rosemount/Rosemount-New-Logo.png',
    'micromotion': 'img/products/micromotion/micromotion.png',
    'flexim': 'img/products/flexim/Flexim-Logo.png',
    'fluenta': 'img/products/fluenta/Fluenta-blog-logo.png',
    'kam': 'img/products/kam/kam_logo.png',
}

for name, path in files.items():
    im = Image.open(path).convert('RGBA')
    # Get bounding box of non-transparent pixels
    bbox = im.getbbox()
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    print(f"{name:12}: full size={im.size}, content bbox={bbox}, content w={w}, h={h}, ratio={w/h:.2f}")
