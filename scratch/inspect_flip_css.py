with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'single-product-flip3d', c)]
print(f"Occurrences of single-product-flip3d: {len(matches)}")
for m in matches:
    print(c[max(0, m-50):min(len(c), m+150)])
    print('='*50)
