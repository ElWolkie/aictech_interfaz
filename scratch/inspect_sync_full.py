# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('function handlePageVideoPlayback')
print(h[idx:idx + 3500])
