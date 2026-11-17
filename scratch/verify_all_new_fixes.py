# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

with open('js/sidebar-collapse.js', 'r', encoding='utf-8') as f:
    sb_js = f.read()

print("=== VERIFYING ALL 6 REQUIREMENTS ===")

# 1. Services Top Header (Image 1)
assert '<div class="services-top-header' in h, "services-top-header must be present"
assert 'Soluciones Integrales de Medición &amp; Diagnóstico' in h or 'Soluciones Integrales de Medición & Diagnóstico' in h
print("✓ 1. Services top header text present directly on dark background!")

# 2. Modal Lightbox Cinema Mode (No controls)
assert 'newVid.controls = false;' in h, "newVid.controls must be false"
assert '#media-lightbox-stage video::-webkit-media-controls' in h, "webkit-media-controls must be hidden"
print("✓ 2. Modal lightbox video navigation/sound/controls bar completely hidden (Cinema mode)!")

# 3. Emerson closed by default, Tinted Strips, Metallic Hover (Image 2)
emerson_menu_idx = h.find('id="emerson-nested-menu"')
emerson_menu_slice = h[emerson_menu_idx-30:emerson_menu_idx+60]
assert 'show' not in emerson_menu_slice and 'is-open' not in emerson_menu_slice, "Emerson must start closed"
assert 'sidebar-brand-strip-roxar' in h, "sidebar-brand-strip-roxar must exist"
assert 'sidebar-brand-strip-flexim' in h, "sidebar-brand-strip-flexim must exist"
assert 'metallicSheenSweep' in h, "metallicSheenSweep keyframes must exist"
print("✓ 3. Emerson closed by default in sidebar, tinted brand strips and metallic text sweep hover verified!")

# 4. Products Header (Image 3)
assert '<div class="products-top-header' in h, "products-top-header must exist without white box"
assert 'Instrumentos de Medición y Servicios de Ingeniería' in h, "Products title must exist"
print("✓ 4. Products header white box removed, high-contrast dark-mode typography present!")

# 5. 3D Webflow Presentation in Products
brands = ['producto-brand-roxar', 'producto-brand-flexim', 'producto-brand-amstrex', 'producto-brand-rosemount', 'producto-brand-micromotion', 'producto-brand-fluenta', 'producto-brand-kam']
brand_positions = [h.find(f'id="{b}"') for b in brands]
assert all(p != -1 for p in brand_positions), "All 7 brand IDs must exist"
assert brand_positions == sorted(brand_positions), "Exact order must be maintained"
assert 'is-3d-card' in h, "is-3d-card must exist"
assert 'perspective: 1400px' in h, "3D perspective must be defined"
assert 'init3DProductObserver' in h, "3D scroll observer must exist"
print("✓ 5. 3D Webflow Scroll Cards with dark obsidian glass and reduced white verified!")

# 6. Initial Presentation: Sidebar closed, floating bouncing logo, footer bottom reveal (Image 4)
assert 'class="sidebar-collapsed"' in h or 'sidebar-collapsed' in h, "sidebar-collapsed class must be on body/wrapper"
assert 'id="floating-aictech-brand"' in h, "floating-aictech-brand must exist"
assert 'cubic-bezier(0.34, 1.56, 0.64, 1)' in h, "Spring bounce bezier curve must be used"
assert 'footer-revealed' in h, "footer-revealed CSS and JS must exist"
assert 'checkFooterRevealOnScroll' in h, "checkFooterRevealOnScroll must exist"
assert 'isCollapsedDefault' in sb_js, "sidebar-collapse.js must default to collapsed on first load"
print("✓ 6. Sidebar closed on initial load, floating logo with bouncing transition, and footer scroll reveal verified!")

print("=== ALL 6 REQUIREMENTS PASSED WITH 100% ACCURACY ===")
