with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
m = re.search(r'(<li[^>]*data-page-no="1"[^>]*>.*?</li>)', text, re.DOTALL)
if m:
    page1 = m.group(1)
    print("Page 1 length:", len(page1))
    print(page1[:1000])
else:
    print("Page 1 not found")

