# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
p3_m = re.search(r'<li[^>]*data-page-no=[\'"]3[\'"]', h)
p4_m = re.search(r'<li[^>]*data-page-no=[\'"]4[\'"]', h)
p5_m = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', h)

print("=== SECTION 3: PETROLIA ===")
print(h[p3_m.start():p4_m.start()])

print("\n=== SECTION 4: EDUTECH ===")
print(h[p4_m.start():p5_m.start()])
