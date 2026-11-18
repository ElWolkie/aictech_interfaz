with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'([^{}]*media-lightbox[^{}]*{[^}]+})', text)
for m in matches:
    print(m)
    print('-'*50)

