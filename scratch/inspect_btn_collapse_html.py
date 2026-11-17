# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
matches = [m.start() for m in re.finditer(r'btn-sidebar-collapse', h)]
print("Found matches in index.html:", len(matches))
for m in matches:
    print(h[m-50:m+250])
    print("---")
