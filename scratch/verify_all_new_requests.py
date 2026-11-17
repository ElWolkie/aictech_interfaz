# -*- coding: utf-8 -*-
import sys

errors = []

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Sidebar check
if 'id="emerson-nested-toggle"' not in html:
    errors.append("emerson-nested-toggle not found in index.html")
else:
    idx = html.find('id="emerson-nested-toggle"')
    chunk = html[idx:idx+400]
    if 'margin-right' not in chunk and 'me-2' not in chunk:
        errors.append("Emerson blue dot spacing (me-2 or margin-right) not found in emerson-nested-toggle")

if '.sidebar-nested-submenu' not in html:
    errors.append("sidebar-nested-submenu CSS not found in index.html")
else:
    css_idx = html.find('.sidebar-nested-submenu {')
    chunk = html[css_idx:css_idx+400]
    if 'display: none' not in chunk:
        errors.append("sidebar-nested-submenu does not have display: none by default")

if 'isSubmenuOpen5 && isAlreadyPage5' not in js:
    errors.append("js/templatemo-script.js does not have the improved toggle logic for #nav-link-productos")

# 2. Banners check
# Roxar
if 'id="producto-brand-roxar"' not in html:
    errors.append("producto-brand-roxar not found")
else:
    idx = html.find('id="producto-brand-roxar"')
    chunk = html[idx:idx+700]
    if 'object-fit: contain' not in chunk or 'scale(0.92)' not in chunk:
        errors.append("Roxar banner does not have object-fit: contain and scale(0.92)")

# Micro Motion
if 'id="producto-brand-micromotion"' not in html:
    errors.append("producto-brand-micromotion not found")
else:
    idx = html.find('id="producto-brand-micromotion"')
    chunk = html[idx:idx+700]
    if 'object-position: center 78%' not in chunk:
        errors.append("Micro Motion banner does not have object-position: center 78%")

# AMS Trex
if 'id="producto-brand-amstrex"' not in html:
    errors.append("producto-brand-amstrex not found")
else:
    idx = html.find('id="producto-brand-amstrex"')
    chunk = html[idx:idx+700]
    if 'object-position: center 25%' not in chunk:
        errors.append("AMS Trex banner does not have object-position: center 25%")

# Fluenta
if 'id="producto-brand-fluenta"' not in html:
    errors.append("producto-brand-fluenta not found")
else:
    idx = html.find('id="producto-brand-fluenta"')
    chunk = html[idx:idx+700]
    if 'object-fit: contain' not in chunk or 'scale(0.92)' not in chunk:
        errors.append("Fluenta banner does not have object-fit: contain and scale(0.92)")

# Kam
if 'id="producto-brand-kam"' not in html:
    errors.append("producto-brand-kam not found")
else:
    idx = html.find('id="producto-brand-kam"')
    chunk = html[idx:idx+700]
    if 'object-fit: contain' not in chunk or 'scale(0.85)' not in chunk:
        errors.append("Kam banner does not have object-fit: contain and scale(0.85)")

# 3. Service 3 (Flexim) check
if 'id="servicio-flexim"' not in html:
    errors.append("servicio-flexim not found")
else:
    idx = html.find('id="servicio-flexim"')
    end = html.find('id="servicio-echometer"', idx)
    chunk = html[idx:end]
    card_count = chunk.count('class="service-flip-card"')
    if card_count != 1:
        errors.append(f"Expected 1 service-flip-card in servicio-flexim, found {card_count}")
    if 'video/flexim-2.mp4' not in chunk:
        errors.append("video/flexim-2.mp4 not found in servicio-flexim")
    if 'Medición de Gas y Líquidos Clamp-On' not in chunk:
        errors.append("Title 'Medición de Gas y Líquidos Clamp-On' not found in servicio-flexim")
    if '0 horas de Parada' not in chunk or 'Instalación en pared exterior de la tubería sin cortar ni despresurizar el gasoducto.' not in chunk:
        errors.append("'0 horas de Parada: Instalación en pared exterior...' not found in servicio-flexim")
    if 'Autonomía en Campo.' not in chunk:
        errors.append("'Autonomía en Campo.' not found in servicio-flexim")
    if 'Verificación y Auditoría' not in chunk or 'Verificación y contraste de medidores en línea sin retirarlos.' not in chunk:
        errors.append("'Verificación y Auditoría...' not found in servicio-flexim")

if errors:
    print("VERIFICATION FAILED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
else:
    print("ALL VERIFICATIONS PASSED PERFECTLY!")
    print("1. Sidebar navigation, Emerson accordion & dot spacing: OK")
    print("2. Product banners Roxar, Micro Motion, AMS Trex, Fluenta, Kam: OK")
    print("3. Service 3 (Flexim) single large card with video 2 and text: OK")
