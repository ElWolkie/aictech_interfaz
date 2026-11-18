with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
print("Total characters in CSS:", len(text))
keyframes = re.findall(r'@keyframes\s+([^{]+)', text)
print(f"Total @keyframes ({len(keyframes)}):")
for k in keyframes:
    print(" -", k.strip())

