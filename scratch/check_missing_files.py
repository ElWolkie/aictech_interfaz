import re
import os

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Check all src and href
srcs = re.findall(r'src="([^"]+)"', text)
hrefs = re.findall(r'href="([^"]+)"', text)

missing = []
for p in srcs + hrefs:
    if p.startswith(('http:', 'https:', '#', 'data:', 'mailto:', 'tel:')):
        continue
    # clean anchor or params
    clean_p = p.split('?')[0].split('#')[0]
    if not clean_p:
        continue
    if not os.path.exists(clean_p):
        missing.append(clean_p)

print(f"Total local references checked: {len(srcs + hrefs)}")
print(f"Missing files ({len(missing)}):")
for m in set(missing):
    print(" - MISSING:", m)

