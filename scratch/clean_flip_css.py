with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_style_flip = c.find('/* TARJETAS 3D FLIP PARA PRODUCTO ÚNICO (FLEXIM, TREX, MICRO)')
if pos_style_flip != -1:
    pos_style_flip_start = c.rfind('/* ============================================================= */', 0, pos_style_flip)
    pos_style_flip_end = c.find('</style>', pos_style_flip)
    c = c[:pos_style_flip_start] + c[pos_style_flip_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Cleaned up unused flip3d CSS block!")
