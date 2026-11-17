# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for b in ['micromotion', 'flexim', 'amstrex']:
    idx = text.find(f'id="producto-brand-{b}"')
    end = text.find('</article>', idx)
    print(f"=== {b} ===")
    print(text[idx:end])
