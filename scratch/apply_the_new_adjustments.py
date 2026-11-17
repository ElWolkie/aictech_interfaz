# -*- coding: utf-8 -*-
"""
apply_the_new_adjustments.py
1. Flexim and Micro Motion: keep only 1 product each in Section 5 (delete additionals)
2. AIC TECH logo: only visible on Inicio (Page 1) when sidebar is closed, no duplicate logos
3. Lower Page 1 (Inicio) hero content so the logo is fully appreciated with ample breathing room
4. Format EduTech (Section 4) with the exact same structure, styling, chips and btn-89 button as PetrolIA
"""

import re

# =========================================================================
# 1. UPDATE index.html
# =========================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# --- Task 1: REPLACE SECTION 5 WITH V2 (1 product for Flexim, 1 for Micro Motion) ---
with open('scratch/generated_section5_3d_v2.html', 'r', encoding='utf-8') as f:
    sec5_v2_html = f.read()

p5_match = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', html)
if not p5_match:
    raise ValueError("Could not find <li data-page-no=5 in index.html")
p5_start = p5_match.start()

p6_match = re.search(r'<li[^>]*data-page-no=[\'"]6[\'"]', html[p5_start:])
if not p6_match:
    raise ValueError("Could not find <li data-page-no=6 in index.html")
p6_start = p5_start + p6_match.start()

html = html[:p5_start] + sec5_v2_html + "\n                " + html[p6_start:]
print("1. Section 5 replaced with v2 (Flexim and Micro Motion now have only 1 product each).")

# --- Task 4: FORMAT EDUTECH (SECTION 4) IDENTICAL TO PETROLIA ---
edutech_new_html = """<!-- SECCIÓN 4: EDUTECH (MISMO FORMATO Y ESTILOS DE PETROLIA) -->
                <li data-page-no="4" class="px-3">
                    <div class="page-width-1 h-100 d-flex align-items-center justify-content-center">
                        <div class="p-4 p-md-5 text-center w-100 shadow-lg reveal-on-scroll reveal-up petrolia-card-container" style="max-width: 920px; background: #ffffff; border-radius: 18px; box-shadow: 0 15px 45px rgba(0, 0, 0, 0.12), 0 2px 10px rgba(0, 0, 0, 0.05); border: 1px solid rgba(226, 232, 240, 0.9);">
                            <!-- Emblema Tecnológico Superior Idéntico a PetrolIA -->
                            <div class="mb-4 text-center d-flex justify-content-center">
                                <div class="petrolia-logo-animated d-inline-flex align-items-center justify-content-center px-4 py-2 rounded-3 shadow-sm" style="background: rgba(2, 132, 199, 0.06); border: 1.5px solid rgba(2, 132, 199, 0.22); gap: 12px;">
                                    <i class="fas fa-graduation-cap text-primary" style="font-size: 2.2rem;"></i>
                                    <span style="font-size: 1.75rem; font-weight: 800; color: #0b192c; letter-spacing: -0.5px;">Edu<span style="color: #0284c7;">TECH</span></span>
                                </div>
                            </div>
                            <h2 class="mb-3 fw-bold display-5 text-dark" style="color: #0b192c !important; font-weight: 800; letter-spacing: -0.5px;">EduTech</h2>
                            <p class="fs-5 mb-4 mx-auto" style="max-width: 820px; line-height: 1.7; color: #475569 !important;">
                                Centro de aprendizaje y certificación técnica continua diseñado para perfeccionar las competencias del personal de ingeniería y operaciones de campo.
                            </p>
                            <!-- PUNTOS DESTACADOS EN CHIPS BLANCOS (IDÉNTICO A PETROLIA) -->
                            <div class="d-flex flex-wrap justify-content-center gap-3 mb-4 py-2">
                                <div class="feature-chip"><i class="fas fa-certificate text-primary"></i> Certificación de Pruebas de Pozo</div>
                                <div class="feature-chip"><i class="fas fa-cubes text-info"></i> Simulaciones Interactivas 3D</div>
                                <div class="feature-chip"><i class="fas fa-book-bookmark text-success"></i> Manuales Operativos de Campo</div>
                                <div class="feature-chip"><i class="fas fa-award text-warning"></i> Formación Continua Certificada</div>
                            </div>
                            <!-- BOTÓN ACCEDER (MISMO BOTÓN .btn-89 DE PETROLIA) -->
                            <div class="mt-4 pt-2 d-flex justify-content-center">
                                <a href="https://edutech.aictech.duckdns.org/" target="_blank" rel="noopener noreferrer" class="btn-89" title="Acceder a EduTech">
                                    <span class="circle_89"></span>
                                    <span class="circle_89"></span>
                                    <span class="button_text_89">Acceder</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </li>"""

p4_match = re.search(r'<li[^>]*data-page-no=[\'"]4[\'"]', html)
if not p4_match:
    raise ValueError("Could not find <li data-page-no=4 in index.html")
p4_start = p4_match.start()

# find where section 4 ends (before section 5)
p5_new_match = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', html[p4_start:])
if not p5_new_match:
    raise ValueError("Could not find <li data-page-no=5 after section 4 in index.html")
p4_end = p4_start + p5_new_match.start()

html = html[:p4_start] + edutech_new_html + "\n\n                " + html[p4_end:]
print("2. Section 4 (EduTech) updated with identical formatting, chips and btn-89 button as PetrolIA.")

# --- Task 2: AICTECH LOGO ONLY ON INICIO (PAGE 1) AND NO DUPLICATE LOGOS ---
# Ensure body has is-page-1 class
html = re.sub(r'<body class="([^"]*)"', r'<body class="\1 is-page-1"', html)
html = html.replace('is-page-1 is-page-1', 'is-page-1')

# Ensure single stationary logo inside sidebar heading
sidebar_heading_new = """<div class="sidebar-heading text-center pt-4 pb-2">
            <!-- LOGO AICTECH OFICIAL SIDEBAR -->
            <a href="#0" class="d-block text-decoration-none tm-page-link" data-page-no="1" data-no="1" title="Ir a Inicio AICTECH" onclick="openPage(1); highlightMenu(1); return false;">
                <img src="img/aictech_logo.png" alt="AICTECH Logo" class="img-fluid" style="max-height: 42px; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.5)); cursor: pointer;">
            </a>
            <div class="sidebar-subtitle">
                INNOVACIÓN EN MEDICIÓN &amp; DIAGNÓSTICO
            </div>
        </div>"""

sidebar_heading_pat = r'<div class="sidebar-heading text-center pt-4 pb-2">[\s\S]*?</div>\s*</div>'
# Check exact heading block
if 'class="sidebar-heading text-center pt-4 pb-2"' in html:
    html = re.sub(
        r'<div class="sidebar-heading text-center pt-4 pb-2">[\s\S]*?<!-- BOTÓN DE INICIO',
        sidebar_heading_new + '\n        \n        <!-- BOTÓN DE INICIO',
        html,
        count=1
    )
    print("3. Sidebar heading restored with single stationary logo.")

# --- Task 2 & 3: CSS FOR LOGO ONLY ON PAGE 1 & LOWER HERO CONTENT ON PAGE 1 ---
new_css_rules = """
        /* ============================================================= */
        /* LOGO FLOTANTE CENTRAL: SOLO EN PÁGINA 1 Y SIDEBAR COLAPSADO  */
        /* ============================================================= */
        #floating-aictech-brand {
            position: fixed;
            top: 16px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1045;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.35s ease, transform 0.35s ease, visibility 0.35s ease;
            filter: drop-shadow(0 4px 18px rgba(56, 182, 255, 0.45));
            user-select: none;
        }

        #floating-aictech-brand .floating-brand-img {
            height: 48px;
            width: auto;
            object-fit: contain;
            transition: transform 0.25s ease;
        }

        #floating-aictech-brand:hover .floating-brand-img {
            transform: scale(1.06);
            filter: drop-shadow(0 0 16px rgba(56, 182, 255, 0.8));
        }

        /* SOLO se muestra en Página 1 (Inicio) y cuando el sidebar está cerrado */
        body.is-page-1.sidebar-collapsed #floating-aictech-brand {
            opacity: 1 !important;
            visibility: visible !important;
            pointer-events: auto !important;
            transform: translateX(-50%) scale(1);
        }

        /* En cualquier otra página o si el sidebar está abierto, queda totalmente oculto */
        body:not(.is-page-1) #floating-aictech-brand,
        body:not(.sidebar-collapsed) #floating-aictech-brand {
            opacity: 0 !important;
            visibility: hidden !important;
            pointer-events: none !important;
        }

        /* ============================================================= */
        /* BAJAR CONTENIDO DEL INICIO PARA DESPEJAR EL LOGO CENTRAL      */
        /* ============================================================= */
        .cd-hero-slider > li[data-page-no="1"] {
            padding-top: 55px !important;
        }

        body.sidebar-collapsed .hero-slb-container {
            margin-top: 30px !important;
            padding-top: 4.5rem !important;
        }

        .hero-slb-container {
            margin-top: 25px !important;
            padding-top: 4.5rem !important;
        }
"""

style_end = html.find('</style>')
if style_end != -1:
    html = html[:style_end] + new_css_rules + "\n    " + html[style_end:]
    print("4. Inserted CSS for Page 1 logo exclusivity and lowered hero content.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated! Final length:", len(html))

# =========================================================================
# 2. UPDATE js/templatemo-script.js TO TOGGLE is-page-1 ON openPage(no)
# =========================================================================
with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add body.is-page-1 toggle in openPage
if 'document.body.classList.toggle(\'is-page-1\'' not in js:
    open_page_pat = r'(function openPage\(no\) \{)'
    js = re.sub(
        open_page_pat,
        r'\1\n  if (document.body) {\n    if (no == 1) document.body.classList.add("is-page-1");\n    else document.body.classList.remove("is-page-1");\n  }',
        js,
        count=1
    )
    with open('js/templatemo-script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("5. js/templatemo-script.js updated to toggle body.is-page-1 on openPage.")

print("All tasks completed successfully!")
