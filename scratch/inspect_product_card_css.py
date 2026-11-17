# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
matches = re.findall(r'[^{}]*emerson-product-card[^{}]*\{[^}]*\}', h)
for m in matches:
    print(m)
