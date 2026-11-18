with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'([^{}]*video[^{}]*{[^}]*filter:[^}]*})', text)
print("Video filter rules:", len(matches))
for m in matches:
    print(m)

