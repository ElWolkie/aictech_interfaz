# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('.hero-slb-container {')
print(h[idx:idx + 800])
