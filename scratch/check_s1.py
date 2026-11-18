with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
s1 = scripts[0]
lines = s1.split('\n')
print(f"Total lines in script 1: {len(lines)}")
for i in range(max(0, len(lines) - 30), len(lines)):
    print(f"{i+1}: {lines[i]}")

