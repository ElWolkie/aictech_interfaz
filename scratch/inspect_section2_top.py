# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

p2_match = re.search(r'<li[^>]*data-page-no=[\'"]2[\'"]', html)
p2_start = p2_match.start()
print(html[p2_start:p2_start + 1800])
