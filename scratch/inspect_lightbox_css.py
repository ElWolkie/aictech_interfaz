with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'\.media-lightbox[^{]*\{[^}]*\}', text)
for m in matches:
    print(m.group(0))
