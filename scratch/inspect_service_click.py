with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
pos_p2 = c.find('data-page-no="2"')
pos_p3 = c.find('data-page-no="3"')
p2 = c[pos_p2:pos_p3]

for m in re.finditer(r'<div class="service-flip-card"[^>]*>', p2):
    print("Found card:", p2[m.start():m.start()+300])
    # check inside
    sub = p2[m.start():m.start()+1200]
    has_wrap = 'service-video-wrap' in sub
    print(f"Has service-video-wrap: {has_wrap}")
    print('='*50)
