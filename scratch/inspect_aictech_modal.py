# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re

for term in ['openAictechIntroModal', 'aictech-intro-video', 'aictech-intro-modal']:
    idx = h.find(term)
    print(f"{term}:", idx != -1)
    if idx != -1:
        print(h[idx-100:idx+600])
        print("---")
