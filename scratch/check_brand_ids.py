with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for b in ['producto-brand-emerson', 'producto-brand-roxar', 'producto-brand-flexim', 'producto-brand-amstrex', 'producto-brand-rosemount', 'producto-brand-micromotion', 'producto-brand-fluenta', 'producto-brand-kam']:
    pos = c.find(f'id="{b}"')
    print(f"ID {b} exists? {pos != -1} at pos {pos}")
