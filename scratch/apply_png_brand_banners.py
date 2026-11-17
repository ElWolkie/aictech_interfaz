# -*- coding: utf-8 -*-
"""
apply_png_brand_banners.py
Applies the new PNG brand logos with white background, centered and balanced scaling across Section 5.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. ROXAR
roxar_old = re.search(r'<article[^>]*id="producto-brand-roxar"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', html)
if roxar_old:
    roxar_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-roxar">
                                    <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                        <img src="img/products/roxar/roxar.png" alt="Roxar Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(1.05);">
                                        <div class="position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center px-4" style="background: linear-gradient(90deg, rgba(30, 10, 60, 0.85) 0%, rgba(15, 23, 42, 0.65) 60%, rgba(15, 23, 42, 0.40) 100%); z-index: 2;">
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #7c3aed; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 10px rgba(124, 58, 237, 0.45);">ROXAR™</span>
                                            </div>
                                            <h2 class="text-white fw-bold fs-3 mt-2 mb-1" style="text-shadow: 0 2px 10px rgba(0,0,0,0.9); font-weight: 800;">Medidores Multifásicos y Analizadores Subsea &amp; Topside</h2>
                                            <p class="small mb-0" style="color: #f1f5f9 !important; text-shadow: 0 1px 6px rgba(0,0,0,0.9); font-size: 0.94rem; max-width: 900px;">Medición continua en línea de petróleo, agua y gas en boca de pozo sin separación física invasiva.</p>
                                        </div>
                                    </div>"""
    html = html.replace(roxar_old.group(0), roxar_new)
    print("1. Roxar banner updated (PNG, centered, scale 1.05).")

# 2. ROSEMOUNT
rosemount_old = re.search(r'<article[^>]*id="producto-brand-rosemount"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', html)
if rosemount_old:
    rosemount_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-rosemount">
                                    <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                        <img src="img/products/rosemount/Rosemount-New-Logo.png" alt="Rosemount Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(1.22);">
                                        <div class="position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center px-4" style="background: linear-gradient(90deg, rgba(0, 45, 95, 0.85) 0%, rgba(15, 23, 42, 0.65) 60%, rgba(15, 23, 42, 0.40) 100%); z-index: 2;">
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #004b87; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 10px rgba(0, 75, 135, 0.45);">ROSEMOUNT™</span>
                                            </div>
                                            <h2 class="text-white fw-bold fs-3 mt-2 mb-1" style="text-shadow: 0 2px 10px rgba(0,0,0,0.9); font-weight: 800;">Medición de Caudal Vortex y Nivel por Radar de Onda Guiada</h2>
                                            <p class="small mb-0" style="color: #f1f5f9 !important; text-shadow: 0 1px 6px rgba(0,0,0,0.9); font-size: 0.94rem; max-width: 900px;">Tecnología de referencia industrial de Emerson en instrumentación de proceso y seguridad SIL.</p>
                                        </div>
                                    </div>"""
    html = html.replace(rosemount_old.group(0), rosemount_new)
    print("2. Rosemount banner updated (PNG, centered, scale 1.22).")

# 3. MICRO MOTION
micromotion_old = re.search(r'<article[^>]*id="producto-brand-micromotion"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', html)
if micromotion_old:
    micromotion_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-micromotion">
                                    <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                        <img src="img/products/micromotion/micromotion.png" alt="Micro Motion Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(1.65);">
                                        <div class="position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center px-4" style="background: linear-gradient(90deg, rgba(30, 41, 59, 0.88) 0%, rgba(15, 23, 42, 0.65) 60%, rgba(15, 23, 42, 0.40) 100%); z-index: 2;">
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #475569; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 10px rgba(71, 85, 105, 0.45);">MICRO MOTION™</span>
                                            </div>
                                            <h2 class="text-white fw-bold fs-3 mt-2 mb-1" style="text-shadow: 0 2px 10px rgba(0,0,0,0.9); font-weight: 800;">Caudalímetros Másicos Coriolis y Densímetros de Precisión</h2>
                                            <p class="small mb-0" style="color: #f1f5f9 !important; text-shadow: 0 1px 6px rgba(0,0,0,0.9); font-size: 0.94rem; max-width: 900px;">Estándar mundial insuperable en transferencia de custodia LACT, caudal másico y densidad en tiempo real.</p>
                                        </div>
                                    </div>"""
    html = html.replace(micromotion_old.group(0), micromotion_new)
    print("3. Micro Motion banner updated (PNG, centered, scale 1.65).")

# 4. FLEXIM
flexim_old = re.search(r'<article[^>]*id="producto-brand-flexim"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', html)
if flexim_old:
    flexim_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-flexim">
                                    <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                        <img src="img/products/flexim/Flexim-Logo.png" alt="Flexim Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.95);">
                                        <div class="position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center px-4" style="background: linear-gradient(90deg, rgba(8, 51, 88, 0.85) 0%, rgba(13, 148, 136, 0.60) 60%, rgba(15, 23, 42, 0.40) 100%); z-index: 2;">
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #0d9488; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 10px rgba(13, 148, 136, 0.45);">FLEXIM™</span>
                                            </div>
                                            <h2 class="text-white fw-bold fs-3 mt-2 mb-1" style="text-shadow: 0 2px 10px rgba(0,0,0,0.9); font-weight: 800;">Medidores Ultrasónicos Clamp-On No Invasivos</h2>
                                            <p class="small mb-0" style="color: #f1f5f9 !important; text-shadow: 0 1px 6px rgba(0,0,0,0.9); font-size: 0.94rem; max-width: 900px;">Medición de flujo de líquidos y gases desde el exterior del ducto sin cortes, paradas ni pérdidas de carga.</p>
                                        </div>
                                    </div>"""
    html = html.replace(flexim_old.group(0), flexim_new)
    print("4. Flexim banner updated (PNG, centered, scale 0.95).")

# 5. FLUENTA
fluenta_old = re.search(r'<article[^>]*id="producto-brand-fluenta"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', html)
if fluenta_old:
    fluenta_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-fluenta">
                                <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                    <img src="img/products/fluenta/Fluenta-blog-logo.png" alt="Fluenta Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(1.30);">
                                    <div class="position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center px-4" style="background: linear-gradient(90deg, rgba(16, 60, 30, 0.88) 0%, rgba(22, 163, 74, 0.55) 60%, rgba(15, 23, 42, 0.40) 100%); z-index: 2;">
                                        <div>
                                            <span class="badge px-3 py-1 fw-bold fs-6" style="background: #16a34a; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 10px rgba(22, 163, 74, 0.45);">FLUENTA</span>
                                        </div>
                                        <h2 class="text-white fw-bold fs-3 mt-2 mb-1" style="text-shadow: 0 2px 10px rgba(0,0,0,0.9); font-weight: 800;">Medición Ultrasónica de Gas de Antorcha (Flare Gas) y Emisiones</h2>
                                        <p class="small mb-0" style="color: #f1f5f9 !important; text-shadow: 0 1px 6px rgba(0,0,0,0.9); font-size: 0.94rem; max-width: 900px;">Soluciones globales no invasivas y de inserción para cumplimiento ambiental y control de quemadores.</p>
                                    </div>
                                </div>"""
    html = html.replace(fluenta_old.group(0), fluenta_new)
    print("5. Fluenta banner updated (PNG, centered, scale 1.30).")

# 6. KAM CONTROLS
kam_old = re.search(r'<article[^>]*id="producto-brand-kam"[\s\S]*?<div class="brand-section-banner[\s\S]*?</div>\s*</div>', html)
if kam_old:
    kam_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-kam">
                                <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                    <img src="img/products/kam/kam_logo.png" alt="Kam Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.72);">
                                    <div class="position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center px-4" style="background: linear-gradient(90deg, rgba(80, 25, 0, 0.88) 0%, rgba(234, 88, 12, 0.60) 60%, rgba(15, 23, 42, 0.40) 100%); z-index: 2;">
                                        <div>
                                            <span class="badge px-3 py-1 fw-bold fs-6" style="background: #ea580c; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 10px rgba(234, 88, 12, 0.45);">KAM CONTROLS</span>
                                        </div>
                                        <h2 class="text-white fw-bold fs-3 mt-2 mb-1" style="text-shadow: 0 2px 10px rgba(0,0,0,0.9); font-weight: 800;">Analizadores de Crudo, Corte de Agua (OWD) y Muestreadores</h2>
                                        <p class="small mb-0" style="color: #f1f5f9 !important; text-shadow: 0 1px 6px rgba(0,0,0,0.9); font-size: 0.94rem; max-width: 900px;">Tecnología de referencia en transferencia de custodia LACT, corte de agua y control de procesos.</p>
                                    </div>
                                </div>"""
    html = html.replace(kam_old.group(0), kam_new)
    print("6. Kam banner updated (PNG, centered, scale 0.72).")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html written successfully! New length:", len(html))
