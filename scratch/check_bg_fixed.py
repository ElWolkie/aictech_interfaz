with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'([^{}]+{[^}]*background-attachment:\s*fixed[^}]*})', text)
print("background-attachment: fixed rules:", len(matches))
for m in matches:
    print(m)

