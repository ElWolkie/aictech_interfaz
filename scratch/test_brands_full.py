with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

brands = [
    'producto-brand-roxar',
    'producto-brand-flexim',
    'producto-brand-amstrex',
    'producto-brand-rosemount',
    'producto-brand-micromotion',
    'producto-brand-fluenta',
    'producto-brand-kam'
]

for b in brands:
    pos = content.find(f'id="{b}"')
    if pos == -1:
        print(f"Brand {b} NOT FOUND")
        continue
    # find next brand or end
    next_pos = len(content)
    for b2 in brands:
        if b2 != b:
            p2 = content.find(f'id="{b2}"', pos + 1)
            if p2 != -1 and p2 < next_pos:
                next_pos = p2
    block = content[pos:next_pos]
    has_large = 'featured-large-product-card' in block
    has_flip = 'flip-360-wrapper' in block
    compact_count = block.count('compact-product-card')
    print(f"{b}: large={has_large}, flip={has_flip}, compacts={compact_count}, block_len={len(block)}")
