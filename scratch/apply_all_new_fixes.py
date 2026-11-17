# -*- coding: utf-8 -*-
"""
apply_all_new_fixes.py
Applies all 6 new requested changes:
1. Re-add Services top text (Soluciones Integrales...) directly on dark background (Image 1)
2. Hide video controls/navigation bar in services modal lightbox (cinema mode)
3. Emerson starts closed by default in sidebar, soft brand strip colors, metallic sweep hover (Image 2)
4. Remove white box from Products header, high-contrast text on dark background (Image 3)
5. Webflow 3D Scroll Presentation for Products (dark glass, glowing pedestals, 3D tilt, reduced white)
6. Sidebar closed on initial load, centered AIC TECH logo with round spring-bounce transition (Image 4),
   footer revealed only on bottom scroll
"""

import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# =========================================================================
# 1. SECTION 2: ADD TOP HEADER TEXT DIRECTLY ON DARK BACKGROUND (IMAGE 1)
# =========================================================================
sec2_top_header = """<div class="services-feed-wrapper">
                            
                            <!-- Header Superior de Servicios (Directo sobre Fondo Oscuro, Estilo Imagen 1) -->
                            <div class="services-top-header mb-4 reveal-on-scroll reveal-up" style="border-bottom: 1px solid rgba(255, 255, 255, 0.12); padding-bottom: 22px; margin-bottom: 28px;">
                                <h1 class="fw-bold display-6 text-white mb-2" style="font-size: clamp(1.8rem, 3.2vw, 2.5rem); text-shadow: 0 2px 12px rgba(0, 0, 0, 0.95); letter-spacing: -0.02em;">
                                    Soluciones Integrales de Medición &amp; Diagnóstico
                                </h1>
                                <p class="fs-6 mb-0" style="line-height: 1.7; max-width: 950px; font-size: 1.02rem; color: #94a3b8 !important;">
                                    Descubra nuestras capacidades operacionales diseñadas para optimizar yacimientos, cuantificar producción en tiempo real y maximizar la confiabilidad en superficie y fondo.
                                </p>
                            </div>"""

# Replace in index.html right after <div class="services-feed-wrapper">
if '<div class="services-top-header' not in html:
    html = re.sub(
        r'<div class="services-feed-wrapper">\s*(<!-- 1\. SERVICIO: MEDIDOR MULTIFÁSICO)',
        sec2_top_header + '\n\n                            \\1',
        html,
        count=1
    )
    print("1. Added Services top header on dark background (Image 1).")

# =========================================================================
# 2. HIDE VIDEO CONTROLS / NAVIGATION BAR IN MODAL LIGHTBOX (CINEMA MODE)
# =========================================================================
old_vid_expand = r'const newVid = document\.createElement\(\'video\'\);[\s\S]*?stage\.appendChild\(newVid\);'
new_vid_expand = """const newVid = document.createElement('video');
                newVid.controls = false; // Sin barra de navegación, progreso ni sonido nativo
                newVid.autoplay = true;
                newVid.loop = true;
                newVid.playsInline = true;
                newVid.muted = false;
                newVid.setAttribute('playsinline', '');
                newVid.setAttribute('webkit-playsinline', '');
                newVid.setAttribute('disablePictureInPicture', '');
                newVid.style.width = '100%';
                newVid.style.height = '100%';
                newVid.style.objectFit = 'contain';
                newVid.style.borderRadius = '12px';
                newVid.style.cursor = 'pointer';
                newVid.title = 'Haga clic en el video para pausar o reanudar';

                // Pausar / reanudar al hacer clic en cualquier parte del video
                newVid.addEventListener('click', function(e) {
                    e.stopPropagation();
                    if (newVid.paused) {
                        newVid.play();
                    } else {
                        newVid.pause();
                    }
                });

                const src = video.currentSrc || (video.querySelector('source') ? video.querySelector('source').src : video.src);
                newVid.src = src;
                stage.appendChild(newVid);
                newVid.play().catch(function() {
                    newVid.muted = true;
                    newVid.play().catch(function() {});
                });"""

if 'newVid.controls = true;' in html:
    html = re.sub(old_vid_expand, new_vid_expand, html, count=1)
    print("2. Video controls/navigation bar removed from modal lightbox (Cinema Mode).")

# =========================================================================
# 3. SIDEBAR: EMERSON CLOSED BY DEFAULT, TINTED STRIPS, METALLIC HOVER
# =========================================================================
# Replace sidebar Emerson block with closed menu by default and soft tinted strips
new_sidebar_emerson = """<div class="sidebar-nested-group">
                        <a href="#producto-brand-emerson" class="submenu-nested-header d-flex align-items-center justify-content-between py-2 px-2" id="emerson-nested-toggle" title="Desplegar marcas Emerson" style="cursor: pointer; text-decoration: none; border-radius: 6px;">
                            <span class="d-flex align-items-center">
                                <span class="submenu-dot me-2" style="background: #38bdf8; margin-right: 8px;"></span>
                                <strong class="submenu-text" style="color: #38bdf8; letter-spacing: 0.5px;">EMERSON</strong>
                            </span>
                            <i class="fas fa-chevron-down nested-chevron small text-info" id="emerson-chevron"></i>
                        </a>
                        <!-- Emerson cerrado por defecto en primer ingreso -->
                        <div class="sidebar-nested-submenu ps-3" id="emerson-nested-menu">
                            <!-- 1. Roxar (Morado) -->
                            <a href="#producto-brand-roxar" class="submenu-link py-1 sidebar-brand-strip-roxar" data-target="producto-brand-roxar">
                                <span class="submenu-dot" style="background: #c084fc; box-shadow: 0 0 6px rgba(192, 132, 252, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #e9d5ff;">Roxar</span>
                            </a>
                            <!-- 2. Flexim (Aguamarina) -->
                            <a href="#producto-brand-flexim" class="submenu-link py-1 sidebar-brand-strip-flexim" data-target="producto-brand-flexim">
                                <span class="submenu-dot" style="background: #2dd4bf; box-shadow: 0 0 6px rgba(45, 212, 191, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #ccfbf1;">Flexim</span>
                            </a>
                            <!-- 3. AMS Trex (Negrito claro) -->
                            <a href="#producto-brand-amstrex" class="submenu-link py-1 sidebar-brand-strip-amstrex" data-target="producto-brand-amstrex">
                                <span class="submenu-dot" style="background: #94a3b8; box-shadow: 0 0 6px rgba(148, 163, 184, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #e2e8f0;">AMS Trex</span>
                            </a>
                            <!-- 4. Rosemount (Azul) -->
                            <a href="#producto-brand-rosemount" class="submenu-link py-1 sidebar-brand-strip-rosemount" data-target="producto-brand-rosemount">
                                <span class="submenu-dot" style="background: #60a5fa; box-shadow: 0 0 6px rgba(96, 165, 250, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #dbeafe;">Rosemount</span>
                            </a>
                            <!-- 5. Micro Motion (Gris) -->
                            <a href="#producto-brand-micromotion" class="submenu-link py-1 sidebar-brand-strip-micromotion" data-target="producto-brand-micromotion">
                                <span class="submenu-dot" style="background: #cbd5e1; box-shadow: 0 0 6px rgba(203, 213, 225, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #f1f5f9;">Micro Motion</span>
                            </a>
                        </div>
                    </div>

                    <!-- MARCAS INDEPENDIENTES FUERA DE EMERSON -->
                    <!-- 6. Fluenta (Verde) -->
                    <a href="#producto-brand-fluenta" class="submenu-link py-1 mt-1 sidebar-brand-strip-fluenta" data-target="producto-brand-fluenta">
                        <span class="submenu-dot" style="background: #4ade80; box-shadow: 0 0 6px rgba(74, 222, 128, 0.6); margin-right: 8px;"></span>
                        <span class="submenu-text" style="color: #dcfce7;">Fluenta</span>
                    </a>
                    <!-- 7. Kam Controls (Naranja) -->
                    <a href="#producto-brand-kam" class="submenu-link py-1 sidebar-brand-strip-kam" data-target="producto-brand-kam">
                        <span class="submenu-dot" style="background: #fb923c; box-shadow: 0 0 6px rgba(251, 146, 60, 0.6); margin-right: 8px;"></span>
                        <span class="submenu-text" style="color: #ffedd5;">Kam Controls</span>
                    </a>"""

old_emerson_block_pat = r'<div class="sidebar-nested-group">[\s\S]*?<!-- MARCAS INDEPENDIENTES FUERA DE EMERSON -->[\s\S]*?<a href="#producto-brand-kam"[\s\S]*?</a>'
html = re.sub(old_emerson_block_pat, new_sidebar_emerson, html, count=1)
print("3. Sidebar Emerson set to closed by default with tinted brand strips.")

# =========================================================================
# 4 & 5. REPLACE SECTION 5 WITH 3D WEBFLOW SCROLL PRESENTATION
# =========================================================================
with open('scratch/generated_section5_3d.html', 'r', encoding='utf-8') as f:
    cards_section5_3d_html = f.read()

# Locate Section 5 li in html
p5_match = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', html)
if not p5_match:
    raise ValueError("Could not find <li data-page-no=5 in index.html")
p5_start = p5_match.start()

p6_match = re.search(r'<li[^>]*data-page-no=[\'"]6[\'"]', html[p5_start:])
if not p6_match:
    raise ValueError("Could not find <li data-page-no=6 in index.html")
p6_start = p5_start + p6_match.start()

html = html[:p5_start] + cards_section5_3d_html + "\n                " + html[p6_start:]
print("4 & 5. Section 5 replaced with Webflow 3D Scroll Presentation (dark obsidian glass).")

# =========================================================================
# 6. INITIAL PRESENTATION: SIDEBAR CLOSED, FLOATING LOGO, FOOTER REVEAL
# =========================================================================
# Add floating brand logo right above #wrapper in body
floating_logo_html = """
    <!-- LOGO FLOTANTE DE ENTRADA / ARRASTRE DINÁMICO AICTECH (CENTRAL A LATERAL) -->
    <div id="floating-aictech-brand" class="floating-brand-logo" onclick="openAictechIntroModal(event); return false;" title="Presentación AICTECH (Clic para reproducir video)">
        <img src="img/aictech_logo.png" alt="AICTECH Logo" class="floating-brand-img">
    </div>
"""

if '<div id="floating-aictech-brand"' not in html:
    html = re.sub(
        r'(<body[^>]*>)',
        r'\1\n' + floating_logo_html,
        html,
        count=1
    )
    print("6a. Floating AIC TECH brand logo inserted into body.")

# Ensure <body> has sidebar-collapsed by default
if 'class="sidebar-collapsed"' not in html:
    html = re.sub(r'<body>', '<body class="sidebar-collapsed">', html, count=1)
if 'id="wrapper" class="d-flex"' in html:
    html = html.replace('id="wrapper" class="d-flex"', 'id="wrapper" class="d-flex sidebar-collapsed"')
if 'id="btn-sidebar-collapse" class="sidebar-collapse-toggle-btn"' in html:
    html = html.replace(
        'id="btn-sidebar-collapse" class="sidebar-collapse-toggle-btn"',
        'id="btn-sidebar-collapse" class="sidebar-collapse-toggle-btn is-collapsed"'
    )
    html = html.replace(
        '<button id="btn-sidebar-collapse" class="sidebar-collapse-toggle-btn is-collapsed" type="button" title="Ocultar Menú Lateral (Ctrl+B o [)">\n        <i class="fas fa-chevron-left"></i>',
        '<button id="btn-sidebar-collapse" class="sidebar-collapse-toggle-btn is-collapsed" type="button" title="Mostrar Menú Lateral (Ctrl+B o [)">\n        <i class="fas fa-bars"></i>'
    )
print("6b. Body, wrapper and toggle button initialized in collapsed state.")

# Hide duplicate logo in sidebar header so floating logo acts as the dynamic anchor
sidebar_heading_pat = r'(<div class="sidebar-heading text-center pt-4 pb-2">)([\s\S]*?)(<div class="sidebar-subtitle)'
def hide_static_logo(m):
    return f'{m.group(1)}\n            <div style="height: 48px; width: 100%;" class="sidebar-logo-spacer" aria-hidden="true"></div>\n            {m.group(3)}'

if '<div style="height: 48px; width: 100%;" class="sidebar-logo-spacer"' not in html:
    html = re.sub(sidebar_heading_pat, hide_static_logo, html, count=1)
    print("6c. Replaced static sidebar logo with transparent anchor spacer.")

# =========================================================================
# CSS: 3D SCROLL, METALLIC SWEEP, FLOATING LOGO, FOOTER REVEAL
# =========================================================================
ultimate_css = """
        /* ============================================================= */
        /* 1. ANIMACIÓN DE LOGO FLOTANTE CON ARRASTRE Y REBOTE DINÁMICO  */
        /* ============================================================= */
        #floating-aictech-brand {
            position: fixed;
            top: 14px;
            left: 50%;
            transform: translateX(-50%) scale(1);
            z-index: 1065;
            cursor: pointer;
            transition: left 0.7s cubic-bezier(0.34, 1.56, 0.64, 1),
                        top 0.7s cubic-bezier(0.34, 1.56, 0.64, 1),
                        transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1),
                        filter 0.4s ease;
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
            transform: scale(1.08) rotate(1deg);
            filter: drop-shadow(0 0 16px rgba(56, 182, 255, 0.8));
        }

        /* Cuando el Sidebar se abre (not collapsed): el logo se arrastra con rebote hacia el sidebar */
        body:not(.sidebar-collapsed) #floating-aictech-brand {
            left: 130px;
            top: 24px;
            transform: translateX(-50%) scale(0.92);
            filter: drop-shadow(0 2px 10px rgba(56, 182, 255, 0.35));
        }

        @media (max-width: 991.98px) {
            #floating-aictech-brand {
                left: 50% !important;
                top: 14px !important;
                transform: translateX(-50%) scale(0.85) !important;
            }
        }

        /* ============================================================= */
        /* 2. FRANJAS TINTADAS DE PRODUCTOS Y BARRIDO METÁLICO EN TEXTO  */
        /* ============================================================= */
        .sidebar-brand-strip-roxar {
            background: rgba(168, 85, 247, 0.08) !important;
            border-left: 3px solid #a855f7 !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }
        .sidebar-brand-strip-flexim {
            background: rgba(20, 184, 166, 0.08) !important;
            border-left: 3px solid #14b8a6 !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }
        .sidebar-brand-strip-amstrex {
            background: rgba(148, 163, 184, 0.08) !important;
            border-left: 3px solid #94a3b8 !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }
        .sidebar-brand-strip-rosemount {
            background: rgba(56, 189, 248, 0.08) !important;
            border-left: 3px solid #38bdf8 !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }
        .sidebar-brand-strip-micromotion {
            background: rgba(203, 213, 225, 0.08) !important;
            border-left: 3px solid #cbd5e1 !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }
        .sidebar-brand-strip-fluenta {
            background: rgba(34, 197, 94, 0.08) !important;
            border-left: 3px solid #22c55e !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }
        .sidebar-brand-strip-kam {
            background: rgba(249, 115, 22, 0.08) !important;
            border-left: 3px solid #f97316 !important;
            border-radius: 4px;
            margin-bottom: 3px;
        }

        @keyframes metallicSheenSweep {
            0% {
                background-position: -200% center;
            }
            100% {
                background-position: 200% center;
            }
        }

        .sidebar-nested-submenu .submenu-link:hover .submenu-text,
        #productos-submenu > a.submenu-link:hover .submenu-text {
            background: linear-gradient(
                90deg,
                currentColor 0%,
                #ffffff 35%,
                #f1f5f9 50%,
                #93c5fd 65%,
                currentColor 100%
            );
            background-size: 250% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: metallicSheenSweep 1.6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.45);
        }

        .sidebar-nested-submenu .submenu-link,
        #productos-submenu > a.submenu-link {
            transition: transform 0.25s ease, filter 0.25s ease, background 0.25s ease;
        }

        .sidebar-nested-submenu .submenu-link:hover,
        #productos-submenu > a.submenu-link:hover {
            transform: translateX(4px);
            filter: brightness(1.25);
        }

        /* ============================================================= */
        /* 3. WEBFLOW 3D SCROLL ANIMATION EN PRODUCTOS                   */
        /* ============================================================= */
        .catalog-feed-wrapper {
            perspective: 1400px;
            perspective-origin: 50% 25%;
            transform-style: preserve-3d;
            scroll-behavior: smooth !important;
            padding-bottom: 60px;
        }

        .brand-snapping-card-section {
            transform-style: preserve-3d;
            transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.65s ease, filter 0.65s ease;
            margin-bottom: 45px;
            scroll-margin-top: 30px;
        }

        .brand-snapping-card-section:not(.is-3d-active) {
            transform: perspective(1400px) rotateX(4deg) scale(0.975) translateZ(-25px);
            opacity: 0.90;
        }

        .brand-snapping-card-section.is-3d-active {
            transform: perspective(1400px) rotateX(0deg) scale(1) translateZ(0);
            opacity: 1;
        }

        .emerson-product-card:hover {
            transform: translateY(-8px) scale(0.985);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.5) !important;
            border-color: rgba(56, 182, 255, 0.6) !important;
        }

        .emerson-product-card:hover .emerson-product-img {
            transform: scale(0.88);
            filter: drop-shadow(0 8px 20px rgba(56, 182, 255, 0.35));
        }

        .emerson-product-card:active .emerson-product-img {
            transform: scale(0.82);
        }

        /* ============================================================= */
        /* 4. FOOTER CRISTALINO OCULTO: REVELADO SOLO AL FONDO           */
        /* ============================================================= */
        footer.site-footer {
            position: relative !important;
            width: 100%;
            margin-top: auto;
            background: rgba(10, 20, 40, 0.92) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            border-top: 1px solid rgba(56, 182, 255, 0.25) !important;
            color: #94a3b8 !important;
            opacity: 0 !important;
            visibility: hidden !important;
            transform: translateY(30px) !important;
            transition: opacity 0.55s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.55s cubic-bezier(0.16, 1, 0.3, 1),
                        visibility 0.55s !important;
            pointer-events: none !important;
            z-index: 10;
        }

        footer.site-footer.footer-revealed {
            opacity: 1 !important;
            visibility: visible !important;
            transform: translateY(0) !important;
            pointer-events: auto !important;
        }

        /* Ocultar barra de controles en el modal lightbox */
        #media-lightbox-stage video::-webkit-media-controls {
            display: none !important;
        }
        #media-lightbox-stage video::-webkit-media-controls-enclosure {
            display: none !important;
        }
        #media-lightbox-stage video::-webkit-media-controls-panel {
            display: none !important;
        }
"""

style_end = html.find('</style>')
if style_end != -1:
    html = html[:style_end] + ultimate_css + "\n    " + html[style_end:]
    print("7. Inserted modern CSS for 3D Scroll, Metallic Sheen, Floating Logo, and Footer Reveal.")

# =========================================================================
# JAVASCRIPT: 3D SCROLL OBSERVER & REVEAL FOOTER ON BOTTOM SCROLL
# =========================================================================
extra_js = """
        // =========================================================================
        // REVELADO INTELIGENTE DEL FOOTER AL LLEGAR AL FINAL DEL SCROLL
        // =========================================================================
        function checkFooterRevealOnScroll() {
            const footer = document.querySelector('footer.site-footer');
            if (!footer) return;

            const scrollY = window.pageYOffset || document.documentElement.scrollTop;
            const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
            const docHeight = Math.max(
                document.body.scrollHeight, document.documentElement.scrollHeight,
                document.body.offsetHeight, document.documentElement.offsetHeight,
                document.body.clientHeight, document.documentElement.clientHeight
            );

            const distFromBottom = docHeight - (scrollY + viewportHeight);
            if (distFromBottom <= 90) {
                footer.classList.add('footer-revealed');
            } else {
                footer.classList.remove('footer-revealed');
            }
        }

        window.addEventListener('scroll', checkFooterRevealOnScroll, { passive: true });

        // =========================================================================
        // OBSERVADOR DE PROFUNDIDAD 3D WEBFLOW EN SECCIÓN 5 (PRODUCTOS)
        // =========================================================================
        (function init3DProductObserver() {
            const cards = document.querySelectorAll('.brand-snapping-card-section.is-3d-card');
            if (!cards.length || !('IntersectionObserver' in window)) return;

            const observer3d = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && entry.intersectionRatio >= 0.25) {
                        entry.target.classList.add('is-3d-active');
                    } else if (!entry.isIntersecting || entry.intersectionRatio < 0.15) {
                        entry.target.classList.remove('is-3d-active');
                    }
                });
            }, {
                root: null,
                threshold: [0.15, 0.25, 0.50]
            });

            cards.forEach(card => observer3d.observe(card));
        })();
"""

script_end_idx = html.rfind('</script>')
if script_end_idx != -1:
    html = html[:script_end_idx] + extra_js + "\n    " + html[script_end_idx:]
    print("8. Added JS for Footer Bottom Reveal and 3D Product Depth Observer.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated! Final length:", len(html))

# =========================================================================
# UPDATE js/sidebar-collapse.js FOR DEFAULT COLLAPSED FIRST LOAD
# =========================================================================
with open('js/sidebar-collapse.js', 'r', encoding='utf-8') as f:
    sb_js = f.read()

# Make default collapsed on first load if no saved state
sb_old_check = "const savedState = localStorage.getItem('aictech_sidebar_collapsed');\n        if (savedState === 'true' && window.innerWidth >= 992) {"
sb_new_check = "const savedState = localStorage.getItem('aictech_sidebar_collapsed');\n        const isCollapsedDefault = (savedState === null) ? true : (savedState === 'true');\n        if (isCollapsedDefault && window.innerWidth >= 992) {"

if sb_old_check in sb_js:
    sb_js = sb_js.replace(sb_old_check, sb_new_check, 1)
    with open('js/sidebar-collapse.js', 'w', encoding='utf-8') as f:
        f.write(sb_js)
    print("9. js/sidebar-collapse.js updated so sidebar defaults to closed on first load.")
else:
    # Alternative check
    sb_js = re.sub(
        r'const savedState = localStorage\.getItem\(\'aictech_sidebar_collapsed\'\);\s*if\s*\([^)]*\)\s*\{',
        "const savedState = localStorage.getItem('aictech_sidebar_collapsed');\n        const isCollapsedDefault = (savedState === null) ? true : (savedState === 'true');\n        if (isCollapsedDefault && window.innerWidth >= 992) {",
        sb_js,
        count=1
    )
    with open('js/sidebar-collapse.js', 'w', encoding='utf-8') as f:
        f.write(sb_js)
    print("9b. js/sidebar-collapse.js updated via regex.")

print("All updates applied cleanly!")
