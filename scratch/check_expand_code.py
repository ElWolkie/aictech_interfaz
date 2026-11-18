with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
m = re.search(r'window\.expandCardMedia\s*=\s*function.*?(?=window\.closeMediaLightbox)', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("expandCardMedia not found")

