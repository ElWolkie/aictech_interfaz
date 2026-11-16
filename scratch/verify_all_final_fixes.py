# -*- coding: utf-8 -*-
"""
verify_all_final_fixes.py
Comprehensive verification script for all user requirements.
"""

import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# 1. Welding video swap
soldadura_idx = html.find('id="servicio-soldadura-taller"')
if soldadura_idx == -1:
    errors.append("ERROR: servicio-soldadura-taller not found")
else:
    soldadura_block = html[soldadura_idx:soldadura_idx+3500]
    if 'id="soldadura-main-video"' not in soldadura_block:
        errors.append("ERROR: soldadura-main-video not found")
    elif 'video/soldadura-1.mp4' not in soldadura_block[:soldadura_block.find('id="video-soldadura-1"')]:
        errors.append("ERROR: soldadura-main-video does not have video/soldadura-1.mp4")

    if 'id="video-soldadura-1"' not in soldadura_block:
        errors.append("ERROR: video-soldadura-1 not found")
    else:
        card_part = soldadura_block[soldadura_block.find('id="video-soldadura-1"'):]
        if 'video/soldadura.mp4' not in card_part[:500]:
            errors.append("ERROR: video-soldadura-1 does not have video/soldadura.mp4")

# 2. AICTECH intro modal
if 'id="aictech-intro-modal"' not in html:
    errors.append("ERROR: aictech-intro-modal not found")
if 'video/inicio-aic.mp4' not in html:
    errors.append("ERROR: video/inicio-aic.mp4 not found in modal")
if 'openAictechIntroModal' not in html:
    errors.append("ERROR: openAictechIntroModal function not found")
if 'openAictechIntroModal(event)' not in html:
    errors.append("ERROR: openAictechIntroModal not wired to logo")

# 3. Lightbox script fix
# Verify expandMediaFromElement is inside a <script> without src
script_tags = re.findall(r'<script([^>]*)>([\s\S]*?)</script>', html)
found_valid_expand = False
for attrs, code in script_tags:
    if 'src=' not in attrs and 'expandMediaFromElement' in code:
        found_valid_expand = True
        break

if not found_valid_expand:
    errors.append("ERROR: expandMediaFromElement is NOT in a standalone <script> tag without src!")

# 4. Lightbox CSS
if '.media-lightbox-stage img' not in html:
    errors.append("ERROR: .media-lightbox-stage img rule not found in CSS")
else:
    css_idx = html.find('.media-lightbox-stage img')
    css_chunk = html[css_idx:css_idx+350]
    if 'object-fit: contain' not in css_chunk:
        errors.append("ERROR: .media-lightbox-stage img does not have object-fit: contain")
    if 'background: #ffffff' not in css_chunk:
        errors.append("ERROR: .media-lightbox-stage img does not have white background")

# 5. Section 5 checks
p5_idx = html.find('data-page-no="5"')
if p5_idx == -1:
    errors.append("ERROR: data-page-no=5 not found")
else:
    p6_idx = html.find('data-page-no="6"', p5_idx)
    s5_chunk = html[p5_idx:p6_idx]

    # Check duplicate banner is gone
    if 'Tecnología de Medición Avanzada • Roxar • Rosemount' in s5_chunk:
        errors.append("ERROR: Duplicate top banner is still present in Section 5!")

    # Check Roxar
    if 'producto-brand-roxar' not in s5_chunk:
        errors.append("ERROR: producto-brand-roxar not found")
    if '#7c3aed' not in s5_chunk:
        errors.append("ERROR: Roxar purple badge (#7c3aed) not found")
    if 'img/products/roxar/roxar.png' not in s5_chunk:
        errors.append("ERROR: img/products/roxar/roxar.png not found")

    # Check Rosemount
    if 'producto-brand-rosemount' not in s5_chunk:
        errors.append("ERROR: producto-brand-rosemount not found")
    if '#004b87' not in s5_chunk:
        errors.append("ERROR: Rosemount blue badge (#004b87) not found")

    # Check Flexim
    if 'producto-brand-flexim' not in s5_chunk:
        errors.append("ERROR: producto-brand-flexim not found")
    if '#0d9488' not in s5_chunk:
        errors.append("ERROR: Flexim aguamarina badge (#0d9488) not found")

    # Check AMS Trex
    if 'producto-brand-amstrex' not in s5_chunk:
        errors.append("ERROR: producto-brand-amstrex not found")
    if '#1e293b' not in s5_chunk:
        errors.append("ERROR: AMS Trex negrito claro badge (#1e293b) not found")

    # Check Fluenta
    if 'producto-brand-fluenta' not in s5_chunk:
        errors.append("ERROR: producto-brand-fluenta not found")
    if '#16a34a' not in s5_chunk:
        errors.append("ERROR: Fluenta green badge (#16a34a) not found")

    # Check Kam
    if 'producto-brand-kam' not in s5_chunk:
        errors.append("ERROR: producto-brand-kam not found")
    if '#ea580c' not in s5_chunk:
        errors.append("ERROR: Kam orange badge (#ea580c) not found")

    # Check Micro Motion
    if 'producto-brand-micromotion' not in s5_chunk:
        errors.append("ERROR: producto-brand-micromotion not found")
    if '#475569' not in s5_chunk:
        errors.append("ERROR: Micro Motion gray badge (#475569) not found")

    # Check banners have only 1 img (the background cover)
    banners = re.findall(r'<div class=[\'"]brand-section-banner[\s\S]*?</div>\s*</div>', s5_chunk)
    if len(banners) != 7:
        errors.append(f"ERROR: Expected 7 brand-section-banners, found {len(banners)}")
    for i, b in enumerate(banners):
        img_count = b.count('<img')
        if img_count != 1:
            errors.append(f"ERROR: Banner {i} has {img_count} images instead of 1 (background only)")

# Print results
if errors:
    print("VERIFICATION FAILED:")
    for err in errors:
        print("  - " + err)
    sys.exit(1)
else:
    print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")
    print(f"Total banners checked: {len(banners)}")
    print("Welding video swap: VERIFIED")
    print("AICTECH intro video: VERIFIED")
    print("Lightbox script isolation: VERIFIED")
    print("Lightbox contain styling: VERIFIED")
    print("All 7 Brand badges, banners and styles: VERIFIED")
