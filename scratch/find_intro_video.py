with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'<video[^>]*id=["\']aictech-intro-video["\']', content)]
for m in matches:
    print(content[m:m+250])
