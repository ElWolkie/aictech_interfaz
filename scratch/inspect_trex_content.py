import os
from PIL import Image

for f in ['AMS Trex Device Communicator wins Gold Award.jpeg', 'ams-trex-banner.jpg']:
    p = os.path.join('img', 'products', 'ams trex', f)
    with Image.open(p) as img:
        # sample colors
        colors = img.resize((10, 10)).getcolors(100)
        print(f, "Sample colors:", colors[:3])
