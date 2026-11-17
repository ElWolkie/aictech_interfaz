# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('id="aictech-intro-video"')
print(h[idx-100:idx+400])
