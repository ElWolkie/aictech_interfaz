with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'data-no', c)]
for m in matches:
    if '<a ' not in c[m-30:m]:
        print(c[max(0, m-50):min(len(c), m+200)])
        print('='*50)
