# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="servicio-bifasico-trifasico"' in line:
        print(f"Found servicio-bifasico-trifasico at line {i+1}")
        for j in range(max(0, i - 15), i + 5):
            print(f"{j+1}: {lines[j]}", end='')
        break
