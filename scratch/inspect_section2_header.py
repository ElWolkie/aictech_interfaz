# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="roxar-hero-content">[\s\S]*?</div>', text)
for i, m in enumerate(matches):
    print(f"=== HERO {i+1} ===")
    print(m)
