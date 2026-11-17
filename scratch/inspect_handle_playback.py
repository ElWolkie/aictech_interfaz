# -*- coding: utf-8 -*-
with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('handlePageVideoPlayback')
if idx != -1:
    print(js[idx:idx + 1200])
else:
    print("handlePageVideoPlayback not found in templatemo-script.js")
