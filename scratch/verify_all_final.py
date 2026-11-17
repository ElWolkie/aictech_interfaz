# -*- coding: utf-8 -*-
"""
Verification script for all final fixes.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("=== VERIFYING FINAL FIXES ===")

# 1. card-multifasico-campo has no carousel pills
has_pills = 'card-slider-pills' in c[c.find('id="card-multifasico-campo"'):c.find('id="card-multifasico-campo"')+3000]
print(f"1. Carousel pills removed from card-multifasico-campo? {not has_pills}")
assert not has_pills, "Carousel pills still in card-multifasico-campo!"

has_toldo_text = 'Video en Campo' in c[c.find('id="card-multifasico-campo"'):c.find('id="card-multifasico-campo"')+3000]
print(f"   'Video en Campo' text removed? {not has_toldo_text}")
assert not has_toldo_text, "'Video en Campo' still present in card-multifasico-campo!"

# 2. No orphaned code in Script 4
has_orphaned = 'function onPointerUp()' in c
print(f"2. Orphaned globe code removed? {not has_orphaned}")
assert not has_orphaned, "Orphaned code still present!"

# 3. fluidNavigateTo scrolls page-content-wrapper
has_wrapper_scroll = 'page-content-wrapper' in c[c.find('window.fluidNavigateTo'):c.find('window.fluidNavigateTo')+800]
print(f"3. fluidNavigateTo scrolls page-content-wrapper? {has_wrapper_scroll}")
assert has_wrapper_scroll, "fluidNavigateTo missing page-content-wrapper scroll!"

# 4. Single products showcase format
has_flip360 = 'flip-360-wrapper' in c
has_single_flip3d = 'single-product-flip3d' in c
print(f"4. Buggy flip 360 removed? {not has_flip360 and not has_single_flip3d}")
assert not has_flip360 and not has_single_flip3d, "Buggy flip cards still present!"

# 5. Photos expanded with white background
pos_roxar = c.find('id="producto-brand-roxar"')
has_white_media = 'background: #ffffff' in c[pos_roxar:pos_roxar+5000]
print(f"5. Media stages have white background for full top/bottom expansion? {has_white_media}")
assert has_white_media, "Media stage missing white background!"

# 6. Service video click-to-expand
has_service_click = "'.service-flip-front, .service-video-wrap'" in c
print(f"6. Service flip front click handler registered? {has_service_click}")
assert has_service_click, "Missing service flip front click handler!"

print("\n=== ALL FINAL VERIFICATIONS PASSED 100%! ===")
