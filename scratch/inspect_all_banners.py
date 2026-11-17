# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
articles = re.findall(r'<article[^>]*id="producto-brand-[^"]*"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', text)
for a in articles:
    banner_match = re.search(r'<div class="brand-section-banner[\s\S]*?</div>\s*</div>', a)
    id_match = re.search(r'id="([^"]+)"', a)
    if id_match and banner_match:
        print(f"=== {id_match.group(1)} ===")
        print(banner_match.group(0))
        print("="*50)
