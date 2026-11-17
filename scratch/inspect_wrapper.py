with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'#page-content-wrapper', c)]
for m in matches:
    print(c[max(0, m-50):min(len(c), m+300)])
    print('='*50)
