with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'(\.service-flip[^{]*{[^}]+})', text)
for m in matches[:10]:
    print(m)
    print('-'*40)

