# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('id="producto-brand-emerson"')
print(h[idx-100:idx+900])
