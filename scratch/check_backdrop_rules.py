with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'([^{}]+{[^}]*backdrop-filter:[^}]*})', text)
print(f"Total rules with backdrop-filter: {len(matches)}")
for m in matches[:15]:
    sel = m.split('{')[0].strip()
    print(" -", sel)

