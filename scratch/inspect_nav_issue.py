with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re

# Look for sidebar navigation handlers in JS
pos_nav = c.find('sidebar-brand-strip')
print("Snippet where sidebar-brand-strip is mentioned in JS or HTML:")
for m in re.finditer(r'sidebar-brand-strip', c):
    print(c[max(0, m.start()-50):min(len(c), m.end()+150)])
    print('='*50)
