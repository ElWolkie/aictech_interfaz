# -*- coding: utf-8 -*-
import sys
import re

errors = []

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

expected_banners = {
    'roxar': {
        'img': 'img/products/roxar/roxar.png',
        'scale': 'scale(1.05)',
        'color': '#7c3aed'
    },
    'rosemount': {
        'img': 'img/products/rosemount/Rosemount-New-Logo.png',
        'scale': 'scale(1.22)',
        'color': '#004b87'
    },
    'micromotion': {
        'img': 'img/products/micromotion/micromotion.png',
        'scale': 'scale(1.65)',
        'color': '#475569'
    },
    'flexim': {
        'img': 'img/products/flexim/Flexim-Logo.png',
        'scale': 'scale(0.95)',
        'color': '#0d9488'
    },
    'fluenta': {
        'img': 'img/products/fluenta/Fluenta-blog-logo.png',
        'scale': 'scale(1.30)',
        'color': '#16a34a'
    },
    'kam': {
        'img': 'img/products/kam/kam_logo.png',
        'scale': 'scale(0.72)',
        'color': '#ea580c'
    },
}

for brand, cfg in expected_banners.items():
    m = re.search(r'<article[^>]*id=["\']producto-brand-' + brand + r'["\'][\s\S]*?<div class=["\']brand-section-banner[\s\S]*?</div>\s*</div>', html)
    if not m:
        errors.append(f"Brand section {brand} article banner not found")
        continue
    chunk = m.group(0)
    
    # Check background: #ffffff
    if 'background: #ffffff;' not in chunk:
        errors.append(f"Banner {brand} does not have background: #ffffff;")
    
    # Check image path
    if cfg['img'] not in chunk:
        errors.append(f"Banner {brand} does not have image {cfg['img']}")
        
    # Check object-fit: contain & object-position: center
    if 'object-fit: contain' not in chunk or 'object-position: center' not in chunk:
        errors.append(f"Banner {brand} is not object-fit: contain; object-position: center")
        
    # Check scale
    if cfg['scale'] not in chunk:
        errors.append(f"Banner {brand} does not have expected scale {cfg['scale']}")
        
    # Check color
    if cfg['color'] not in chunk:
        errors.append(f"Banner {brand} does not have expected badge color {cfg['color']}")

if errors:
    print("VERIFICATION FAILED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
else:
    print("ALL 6 PNG BRAND BANNERS VERIFIED PERFECTLY!")
    for b in expected_banners:
        print(f"  [OK] {b.upper()}: White background, PNG logo, centered, proportional scaling, color badge")
