with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'<div[^>]*flip-360-wrapper[^>]*>', content)
print("Flip wrapper tags:", matches)
