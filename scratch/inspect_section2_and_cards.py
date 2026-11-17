# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Check Section 2 Top
sec2_start = html.find('id="servicio-multifasico"')
print("=== SECTION 2 START ===")
print(html[sec2_start - 300:sec2_start + 600])

# Check Section 5 structure
print("\n=== SECTION 5 START ===")
sec5_start = html.find('id="producto-brand-roxar"')
print(html[sec5_start - 300:sec5_start + 600])

# Check videos in section 2
videos = re.findall(r'<video[^>]+>', html)
print(f"\nTotal video tags found in index.html: {len(videos)}")
controls_videos = [v for v in videos if 'controls' in v]
print(f"Videos with 'controls': {len(controls_videos)}")

# Check Emerson chevron and sidebar
emerson_idx = html.find('id="emerson-nested-toggle"')
print("\n=== SIDEBAR EMERSON ===")
print(html[emerson_idx - 100:emerson_idx + 800])
