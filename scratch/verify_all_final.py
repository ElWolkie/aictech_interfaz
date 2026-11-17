# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

print("=== CHECKING ALL REQUIREMENTS ===")

# 1. Section 5 Brands and Order
brands = [
    'producto-brand-roxar',
    'producto-brand-flexim',
    'producto-brand-amstrex',
    'producto-brand-rosemount',
    'producto-brand-micromotion',
    'producto-brand-fluenta',
    'producto-brand-kam'
]
brand_positions = [html.find(f'id="{b}"') for b in brands]
print("Brand positions in HTML:", brand_positions)
assert all(p != -1 for p in brand_positions), "All 7 brand IDs must exist in index.html"
assert brand_positions == sorted(brand_positions), "Brands must appear in exact order: Roxar, Flexim, AMS Trex, Rosemount, Micro Motion, Fluenta, Kam"
print("✓ Section 5 Brands exact order verified!")

# 2. Sidebar Emerson Order
emerson_idx = html.find('id="emerson-nested-menu"')
assert emerson_idx != -1, "Emerson nested menu must exist"
emerson_slice = html[emerson_idx:emerson_idx + 3500]
emerson_sub_positions = [emerson_slice.find(b) for b in brands[:5]]
print("Sidebar Emerson sub-item positions:", emerson_sub_positions)
assert all(p != -1 for p in emerson_sub_positions), "All 5 Emerson brands must exist in sidebar submenu"
assert emerson_sub_positions == sorted(emerson_sub_positions), "Sidebar brands must match order: Roxar, Flexim, AMS Trex, Rosemount, Micro Motion"
print("✓ Sidebar Emerson order verified!")

# 3. Check Section 2 Top & White Box
assert 'Soluciones Integrales de Medición & Diagnóstico' not in html, "White header box must be removed from Section 2"
assert 'Well Testing con Medidores Multifásicos Roxar' in html, "Service 1 title must be Well Testing con Medidores Multifásicos Roxar"
assert 'id="servicio-multifasico"' in html, "servicio-multifasico article must exist"
assert 'id="roxar-main-video"' in html, "roxar-main-video must exist in service 1"
print("✓ Section 2 Service 1 header verified!")

# 4. Check Section 2 Videos and Controls
p2_m = re.search(r'<li[^>]*data-page-no=[\'"]2[\'"]', html)
p3_m = re.search(r'<li[^>]*data-page-no=[\'"]3[\'"]', html)
sec2_html = html[p2_m.start():p3_m.start()]

sec2_videos = re.findall(r'<video[^>]+>', sec2_html)
print(f"Total videos in Section 2: {len(sec2_videos)}")
assert len(sec2_videos) >= 20, "Should have all videos in Section 2"
controls_in_sec2 = [v for v in sec2_videos if 'controls' in v]
print(f"Videos with controls in Section 2: {len(controls_in_sec2)}")
assert len(controls_in_sec2) == 0, "No preview video in Section 2 should have controls"

# Check play overlay button removed
assert 'Reproducir Video' not in sec2_html, "Reproducir Video overlay buttons must be removed"
print("✓ Section 2 videos have no controls bar and no overlay play buttons!")

# 5. Check 60FPS Video Observer & Click Handlers
assert 'initActiveSectionVideoObserver' in html, "initActiveSectionVideoObserver must exist in index.html"
assert 'updateServiceVideosPlayback' in html, "updateServiceVideosPlayback must exist"
assert 'fluidNavigateTo' in html, "fluidNavigateTo must exist for smooth navigation"
assert 'expandCardMedia' in html, "expandCardMedia must exist for 1-click video expand"
assert 'expandMediaFromElement' in html, "expandMediaFromElement must exist for 1-click product expand"

print("✓ All 60FPS Video Observers, 1-Click Expand, and Fluid Navigation handlers verified!")
print("=== ALL CHECKS PASSED PERFECTLY! ===")
