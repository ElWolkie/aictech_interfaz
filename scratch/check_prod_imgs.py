import os
from PIL import Image

for root, dirs, files in os.walk('img/products'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg')):
            p = os.path.join(root, f)
            sz = os.path.getsize(p)
            if sz > 100000:
                print(f"{sz/1024:.1f} KB: {p}")

