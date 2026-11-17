# -*- coding: utf-8 -*-
with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('btn-sidebar-collapse')
if idx != -1:
    print(js[idx-100:idx+600])
else:
    print("btn-sidebar-collapse not found in js")
