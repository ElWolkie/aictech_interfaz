# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'sidebar-heading' in l:
        for j in range(max(0, i-2), min(i+25, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
        break
