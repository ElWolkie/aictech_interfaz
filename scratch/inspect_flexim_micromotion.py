# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re

for brand_id in ['producto-brand-flexim', 'producto-brand-micromotion']:
    idx = h.find(f'id="{brand_id}"')
    end_idx = h.find('</article>', idx)
    print(f"=== {brand_id} ===")
    print(h[idx:idx + 800])
