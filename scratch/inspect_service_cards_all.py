with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_p2 = c.find('data-page-no="2"')
pos_p3 = c.find('data-page-no="3"')
p2_html = c[pos_p2:pos_p3]

import re
video_tags = re.findall(r'<video[^>]*>', p2_html)
print(f"Total videos in Section 2: {len(video_tags)}")
for v in video_tags[:5]:
    print(v)

cards = re.findall(r'class="[^"]*(?:service-flip-card|service-video-wrap|roxar-card)[^"]*"', p2_html)
print(f"Cards found: {len(cards)}")
for card in cards[:8]:
    print(card)
