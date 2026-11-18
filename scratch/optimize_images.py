import os
import shutil
from PIL import Image

backup_dir = 'img/_orig_backup'
os.makedirs(backup_dir, exist_ok=True)

targets = [
    'img/toldo-trailer.jpg',
    'img/home-img-1.jpg',
    'img/home-img-2.jpg',
    'img/jefe.jpg',
    'img/aicicon.jpg',
]

for p in targets:
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(backup_dir, os.path.basename(p)))
        im = Image.open(p)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.save(p, format='JPEG', quality=83, optimize=True)
        print(f"Optimized {p}: {os.path.getsize(p)/1024:.1f} KB")

