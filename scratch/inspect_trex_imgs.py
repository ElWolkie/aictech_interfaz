import os
from PIL import Image

for f in ['AMS Trex Device Communicator wins Gold Award.jpeg', 'ams-trex-banner.jpg']:
    p = os.path.join('img', 'products', 'ams trex', f)
    with Image.open(p) as img:
        print(f, img.size, img.format, img.mode)
