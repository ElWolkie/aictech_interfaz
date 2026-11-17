# -*- coding: utf-8 -*-
with open('scratch/generated_section5_cards.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="producto-brand-roxar"')
col_right = html.find('DERECHA: PANEL DE IDENTIDAD DE MARCA', idx)
print(html[col_right:col_right + 1800])
