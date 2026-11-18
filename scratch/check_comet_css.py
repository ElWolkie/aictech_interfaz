with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'(/\*+[^\*]*COMETAS[^\*]*\*+/.*?)(?=/\*|$)', text, re.DOTALL)
for m in matches:
    print(m[:300])
    print('='*50)

