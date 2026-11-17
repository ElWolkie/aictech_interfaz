# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

p2_match = re.search(r'<li[^>]*data-page-no=[\'"]2[\'"]', html)
p3_match = re.search(r'<li[^>]*data-page-no=[\'"]3[\'"]', html)

sec2_html = html[p2_match.start():p3_match.start()]
videos = re.findall(r'<video[^>]+>', sec2_html)
print(f"Total videos in Section 2: {len(videos)}")
for i, v in enumerate(videos):
    print(f"{i+1}: {v}\n")
