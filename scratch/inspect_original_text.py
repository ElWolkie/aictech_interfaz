with open('scratch/generated_section5_final.html', 'r', encoding='utf-8') as f:
    c = f.read()

for b in ['producto-brand-flexim', 'producto-brand-amstrex', 'producto-brand-micromotion']:
    pos = c.find(f'id="{b}"')
    next_pos = c.find('</article>', pos)
    print(f'=== {b} ===')
    print(c[pos:next_pos+10])
