# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
matches = [m.start() for m in re.finditer(r'function expandCardMedia|window\.expandCardMedia', h)]
print("Matches in index.html:", len(matches))
for m in matches:
    print(h[m:m+800])
    print("---")
