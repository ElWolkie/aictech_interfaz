with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'submenu-link', c)]
for m in matches:
    if 'class="' not in c[m-20:m+20]:
        print(c[max(0, m-100):min(len(c), m+400)])
        print('='*50)
