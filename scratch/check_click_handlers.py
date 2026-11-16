with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'\$\(document\)\.on\(\'click\',[^\n]+', text)
for m in matches:
    print(m.group(0))
