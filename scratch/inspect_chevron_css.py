# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
matches = re.findall(r'[^{}]*nested-chevron[^{}]*\{[^}]*\}', h)
for m in matches:
    print(m)

matches2 = re.findall(r'[^{}]*rotate-180[^{}]*\{[^}]*\}', h)
for m in matches2:
    print(m)
