# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="servicio-flexim"')
end = text.find('id="servicio-echometer"', idx)
print(text[idx:end])
