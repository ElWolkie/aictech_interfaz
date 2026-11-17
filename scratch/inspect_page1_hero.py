# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
p1_m = re.search(r'<li[^>]*data-page-no=[\'"]1[\'"]', h)
print(h[p1_m.start():p1_m.start() + 1800])
