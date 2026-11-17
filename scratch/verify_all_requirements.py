# -*- coding: utf-8 -*-
"""
Verification script for all user requirements.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("=== VERIFYING REFINED PRODUCT CHANGES ===")

# 1. No 'Agrandar' button in featured cards
pos_li5 = c.find('<li data-page-no="5"')
pos_li6 = c.find('<li data-page-no="6"')
sec5 = c[pos_li5:pos_li6]

has_agrandar_btn = 'Agrandar</button>' in sec5 or 'i class="fas fa-expand me-1"></i> Agrandar' in sec5
print(f"1. 'Agrandar' button removed from featured cards? {not has_agrandar_btn}")
assert not has_agrandar_btn, "Agrandar button still present in section 5!"

# 2. No 'Ver en Pantalla Completa' button in single products
has_ver_pantalla_completa_btn = 'Ver en Pantalla Completa' in sec5
print(f"2. 'Ver en Pantalla Completa' button removed from single products? {not has_ver_pantalla_completa_btn}")
assert not has_ver_pantalla_completa_btn, "Ver en Pantalla Completa button still present!"

# 3. Compact cards use compact-products-grid
grid_count = sec5.count('class="compact-products-grid h-100"')
print(f"3. Number of compact-products-grid containers: {grid_count} (expected 4: Roxar, Rosemount, Fluenta, Kam)")
assert grid_count == 4, f"Expected 4 grids, found {grid_count}"

# 4. Centered odd cards in Rosemount, Fluenta, Kam
centered_count = sec5.count('compact-card-centered-odd')
print(f"4. Number of centered odd cards: {centered_count} (expected 3)")
assert centered_count == 3, f"Expected 3 centered cards, found {centered_count}"

# 5. Single products use single-product-flip3d
flip3d_count = sec5.count('class="single-product-flip3d"')
print(f"5. Number of single-product-flip3d cards: {flip3d_count} (expected 3: Flexim, AMS Trex, Micro Motion)")
assert flip3d_count == 3, f"Expected 3 flip3d cards, found {flip3d_count}"

# 6. AMS Trex does not use ams-trex-banner.jpg
has_trex_banner = 'ams-trex-banner.jpg' in sec5
print(f"6. ams-trex-banner.jpg removed from AMS Trex? {not has_trex_banner}")
assert not has_trex_banner, "ams-trex-banner.jpg still present in AMS Trex section!"

# 7. Sidenav #productos-submenu has no submenu-dot
pos_sub = c.find('id="productos-submenu"')
pos_sub_end = c.find('<!-- 2. SERVICIOS', pos_sub)
submenu = c[pos_sub:pos_sub_end]
has_dots = '<span class="submenu-dot' in submenu
print(f"7. Submenu dots removed from productos-submenu? {not has_dots}")
assert not has_dots, "Submenu dots still present in productos-submenu!"

# 8. Watermark logos have white luminous filter & mask fade
has_invert = 'filter: brightness(0) invert(1)' in c
has_mask = '-webkit-mask-image: linear-gradient(to left, rgba(0,0,0,1)' in c
print(f"8. Watermarks have white invert filter and mask fade? {has_invert and has_mask}")
assert has_invert and has_mask, "Watermarks missing white invert or mask fade!"

print("\n=== ALL 8 REQUIREMENTS 100% VERIFIED AND CONFIRMED! ===")
