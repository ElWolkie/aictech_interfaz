with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'([^{}]+{[^}]*filter:[^}]*})', text)
print(f"Total rules with filter: {len(matches)}")
for m in matches[:15]:
    sel = m.split('{')[0].strip()
    rule = [r.strip() for r in m.split('{')[1].split(';') if 'filter' in r]
    print(f"{sel} => {rule}")

