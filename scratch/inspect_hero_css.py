# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
matches = re.findall(r'[^{}]*hero-slb-content[^{}]*\{[^}]*\}', h)
for m in matches:
    print(m)
matches2 = re.findall(r'[^{}]*hero-slb-container[^{}]*\{[^}]*\}', h)
for m in matches2:
    print(m)
