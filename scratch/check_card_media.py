with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
cards = re.findall(r'<div class="service-flip-card"[^>]*>.*?</div>\s*</div>\s*</div>', text, re.DOTALL)
print(f"Total service flip cards: {len(cards)}")
for i, c in enumerate(cards):
    title = re.search(r'service-front-title[^>]*>(.*?)</div>', c, re.DOTALL)
    title_str = title.group(1).strip() if title else 'NO_TITLE'
    vids = re.findall(r'<video[^>]*src="([^"]+)"', c)
    if not vids:
        vids = re.findall(r'<source[^>]*src="([^"]+)"', c)
    imgs = re.findall(r'<img[^>]*src="([^"]+)"', c)
    print(f"Card {i+1}: {title_str[:50]} | Videos: {vids} | Imgs: {imgs}")

