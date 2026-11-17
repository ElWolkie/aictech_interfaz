# -*- coding: utf-8 -*-
import os

for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for f in files:
        if f.endswith('.js') or f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
                if 'btn-sidebar-collapse' in txt or 'sidebar-collapsed' in txt:
                    print(f"Match in {p}")
