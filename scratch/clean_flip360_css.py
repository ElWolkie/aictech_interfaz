with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_flip_start = c.find('/* ============================================================= */\n        /* TARJETAS 3D FLIP 360 (ENVELOPE / COMPUERTAS)                 */')
if pos_flip_start == -1:
    pos_flip_start = c.find('.flip-360-wrapper {')
    pos_flip_start = c.rfind('/*', 0, pos_flip_start)

pos_flip_end = c.find('/* ============================================================= */\n        /* COMPACT CARDS & FEATURED LARGE', pos_flip_start)
if pos_flip_end == -1:
    pos_flip_end = c.find('.compact-products-grid', pos_flip_start)
    pos_flip_end = c.rfind('/*', 0, pos_flip_end)

print("Found flip-360 CSS block to remove:")
print(c[pos_flip_start:pos_flip_start+150])
print("Ending before:")
print(c[pos_flip_end:pos_flip_end+150])

c = c[:pos_flip_start] + c[pos_flip_end:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Removed unused flip-360 CSS successfully!")
