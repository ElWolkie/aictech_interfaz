# -*- coding: utf-8 -*-
with open('scratch/generated_section5_3d.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('id="producto-brand-amstrex"')
end_idx = h.find('</article>', idx)
print(h[idx:end_idx])
