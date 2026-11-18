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
    test_out = 'scratch/opt_' + os.path.basename(p)
    if im.mode != 'RGB':
        im_rgb = im.convert('RGB')
    else:
        im_rgb = im
    im_rgb.save(test_out, format='JPEG', quality=84, optimize=True)
    new_size = os.path.getsize(test_out)
    print(f"{p}: {orig_size/1024:.1f} KB -> {new_size/1024:.1f} KB ({((new_size-orig_size)/orig_size)*100:.1f}%)")

