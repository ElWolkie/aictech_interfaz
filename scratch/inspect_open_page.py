# -*- coding: utf-8 -*-
with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function openPage')
print(js[idx:idx + 1200])
