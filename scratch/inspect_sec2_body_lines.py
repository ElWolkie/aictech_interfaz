# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<div class="services-feed-wrapper">' in line:
        print(f"Found services-feed-wrapper in body at line {i+1}")
        for j in range(i, min(i + 50, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
        break
