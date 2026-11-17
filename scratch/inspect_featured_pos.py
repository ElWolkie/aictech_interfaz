with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'featured-large-product-card', content)]
print(f"Total occurrences of featured-large-product-card: {len(matches)}")
for idx, m in enumerate(matches):
    print(f"Match {idx} at position {m}:")
    print(content[m-100:m+250])
    print('='*50)
