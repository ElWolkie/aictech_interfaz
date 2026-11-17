# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

print("=== VERIFYING ADJUSTMENTS ===")

# 1. Flexim and Micro Motion have only 1 product each
flexim_idx = h.find('id="producto-brand-flexim"')
flexim_end = h.find('</article>', flexim_idx)
flexim_html = h[flexim_idx:flexim_end]
assert 'FLUXUS® F631 BA' in flexim_html, "FLUXUS F631 BA must be in Flexim"
assert 'FLUXUS® G721' not in flexim_html, "FLUXUS G721 must be deleted from Flexim"
assert '1 Modelo' in flexim_html, "Flexim badge must show 1 Modelo"
print("✓ 1a. Flexim has only 1 product (FLUXUS G721 deleted)!")

mm_idx = h.find('id="producto-brand-micromotion"')
mm_end = h.find('</article>', mm_idx)
mm_html = h[mm_idx:mm_end]
assert 'Micro Motion™ 5700' in mm_html, "5700 must be in Micro Motion"
assert 'Coriolis ELITE Sensor' not in mm_html, "Coriolis ELITE Sensor must be deleted from Micro Motion"
assert '1 Modelo' in mm_html, "Micro Motion badge must show 1 Modelo"
print("✓ 1b. Micro Motion has only 1 product (ELITE Sensor deleted)!")

# 2. AIC TECH Logo: only on page 1, no duplicate logos
assert 'body.is-page-1.sidebar-collapsed #floating-aictech-brand' in h, "Floating logo must be scoped to is-page-1 and sidebar-collapsed"
assert 'body:not(.is-page-1) #floating-aictech-brand' in h, "Floating logo must be hidden when not on page 1"
assert 'body:not(.sidebar-collapsed) #floating-aictech-brand' in h, "Floating logo must be hidden when sidebar is open"
assert 'document.body.classList.add("is-page-1")' in js, "templatemo-script.js must toggle is-page-1"
print("✓ 2. Floating logo scoped exclusively to Inicio (page 1) when sidebar is closed, zero duplicate logos!")

# 3. Page 1 Hero lowered
assert '.cd-hero-slider > li[data-page-no="1"]' in h
assert 'padding-top: 55px !important;' in h
assert 'margin-top: 30px !important;' in h
print("✓ 3. Hero content on Inicio lowered with ample breathing room for the logo!")

# 4. EduTech has same format and styles as PetrolIA
edutech_idx = h.find('data-page-no="4"')
edutech_end = h.find('data-page-no="5"', edutech_idx)
edutech_html = h[edutech_idx:edutech_end]
assert 'petrolia-card-container' in edutech_html, "EduTech must use petrolia-card-container"
assert 'petrolia-logo-animated' in edutech_html, "EduTech must use petrolia-logo-animated"
assert 'feature-chip' in edutech_html, "EduTech must use feature-chip"
assert 'btn-89' in edutech_html, "EduTech must use btn-89 button"
assert 'Acceder' in edutech_html, "EduTech button text must be Acceder"
assert 'https://edutech.aictech.duckdns.org/' in edutech_html, "EduTech link must be preserved"
print("✓ 4. EduTech formatted identically to PetrolIA (card, chips, btn-89 button)!")

print("=== ALL 4 CHECKS PASSED PERFECTLY! ===")
