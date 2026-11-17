# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re

for brand_id in ['producto-brand-flexim', 'producto-brand-micromotion']:
    idx = h.find(f'id="{brand_id}"')
    end_idx = h.find('</article>', idx)
    brand_html = h[idx:end_idx]
    titles = re.findall(r'<h5[^>]*>(.*?)</h5>', brand_html)
    print(f"=== {brand_id} ===")
    print("Titles:", titles)
    badges = re.findall(r'Modelos', brand_html)
    print("Modelos mentions:", len(badges))
