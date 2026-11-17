with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
for m in re.finditer(r'openAictechIntroModal', content):
    print(content[max(0, m.start()-100):min(len(content), m.end()+300)])
    print('='*50)
