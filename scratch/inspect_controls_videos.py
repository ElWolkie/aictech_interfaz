# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
videos = re.findall(r'<video[^>]+>', html)
for i, v in enumerate(videos):
    if 'controls' in v:
        print(f"Video {i}: {v}")
