with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
# Find all comments with titles
titles = re.findall(r'/\*+[^\*]+\*+/', text)
for t in titles[:30]:
    clean_t = t.strip()
    if len(clean_t) < 100:
        print(clean_t)

