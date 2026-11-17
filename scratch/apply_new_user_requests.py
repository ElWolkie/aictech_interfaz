# -*- coding: utf-8 -*-
"""
apply_new_user_requests.py
Executes all 3 user requests:
1. Fix sidebar product submenu toggle and Emerson dot spacing
2. Adjust product banners: Roxar, Micro Motion, AMS Trex, Fluenta, Kam
3. Update Service 3 (Flexim) to have 1 single large card with video/flexim-2.mp4 and updated text
"""

import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Initial length of index.html:", len(html))

# =========================================================================
# 1. FIX SIDEBAR SUBMENU AND EMERSON ACCORDION
# =========================================================================

# A) Fix Emerson dot spacing in sidebar HTML
# Replace:
# <span class="submenu-dot" style="background: #38bdf8;"></span>
# with:
# <span class="submenu-dot me-2" style="background: #38bdf8;"></span>
old_emerson_header = """<a href="#producto-brand-emerson" class="submenu-link submenu-nested-header d-flex align-items-center justify-content-between py-2" data-target="producto-brand-emerson" id="emerson-nested-toggle" title="Desplegar marcas Emerson">
                            <span class="d-flex align-items-center">
                                <span class="submenu-dot" style="background: #38bdf8;"></span>
                                <strong class="submenu-text" style="color: #38bdf8; letter-spacing: 0.5px;">EMERSON</strong>
                            </span>
                            <i class="fas fa-chevron-down nested-chevron small text-info" id="emerson-chevron"></i>
                        </a>"""

new_emerson_header = """<a href="#producto-brand-emerson" class="submenu-nested-header d-flex align-items-center justify-content-between py-2 px-2" id="emerson-nested-toggle" title="Alternar marcas Emerson" style="cursor: pointer; text-decoration: none; border-radius: 6px;">
                            <span class="d-flex align-items-center">
                                <span class="submenu-dot me-2" style="background: #38bdf8; margin-right: 8px;"></span>
                                <strong class="submenu-text" style="color: #38bdf8; letter-spacing: 0.5px;">EMERSON</strong>
                            </span>
                            <i class="fas fa-chevron-down nested-chevron small text-info rotate-180 is-rotated" id="emerson-chevron"></i>
                        </a>"""

if old_emerson_header in html:
    html = html.replace(old_emerson_header, new_emerson_header)
    print("1A. Emerson header dot spacing and class updated.")
else:
    # Try regex replacement if whitespace differed
    pattern = r'<a href="#producto-brand-emerson"[^>]*id="emerson-nested-toggle"[^>]*>[\s\S]*?</a>'
    html = re.sub(pattern, new_emerson_header, html, count=1)
    print("1A. Emerson header dot spacing regex replaced.")

# Ensure emerson-nested-menu starts with show is-open
html = html.replace(
    'id="emerson-nested-menu"',
    'id="emerson-nested-menu" class="sidebar-nested-submenu ps-3 show is-open"'
)
# Clean up duplicate classes if any
html = html.replace(
    'class="sidebar-nested-submenu ps-3" class="sidebar-nested-submenu ps-3 show is-open"',
    'class="sidebar-nested-submenu ps-3 show is-open"'
)

# B) Update CSS for sidebar nested submenu and submenu dot
old_nested_css = """/* SUBMENÚ ANIDADO DE EMERSON EN EL SIDEBAR */
        .sidebar-nested-submenu {
            border-left: 2px solid rgba(56, 182, 255, 0.3);
            margin-left: 12px;
            margin-top: 4px;
            margin-bottom: 6px;
        }"""

new_nested_css = """/* SUBMENÚ ANIDADO DE EMERSON EN EL SIDEBAR */
        .sidebar-nested-submenu {
            border-left: 2px solid rgba(56, 182, 255, 0.3);
            margin-left: 12px;
            margin-top: 4px;
            margin-bottom: 6px;
            display: none;
            transition: all 0.25s ease;
        }
        .sidebar-nested-submenu.show,
        .sidebar-nested-submenu.is-open {
            display: block !important;
        }
        .nested-chevron {
            transition: transform 0.25s ease;
        }
        .nested-chevron.rotate-180,
        .nested-chevron.is-rotated {
            transform: rotate(180deg);
        }
        .submenu-dot {
            margin-right: 8px;
        }"""

if old_nested_css in html:
    html = html.replace(old_nested_css, new_nested_css)
    print("1B. Nested CSS updated with collapse support.")
else:
    # Append to existing
    html = re.sub(
        r'\.sidebar-nested-submenu\s*\{[^}]*\}',
        new_nested_css,
        html
    )
    print("1B. Nested CSS regex updated.")

# =========================================================================
# 2. PRODUCT BANNERS ADJUSTMENTS IN SECTION 5
# =========================================================================

# 1) ROXAR: Scale down and contain so full "ROXAR" text is visible like Rosemount
# Find roxar banner
roxar_old = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-roxar">
                                    <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18);">
                                        <img src="img/products/roxar/roxar.png" alt="Roxar Banner" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(0.60) contrast(1.1); position: absolute; top: 0; left: 0;">"""

roxar_new = """<article class="brand-showcase-section mb-5 reveal-on-scroll reveal-up" id="producto-brand-roxar">
                                    <div class="brand-section-banner rounded-3 overflow-hidden position-relative mb-4" style="height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;">
                                        <img src="img/products/roxar/roxar.png" alt="Roxar Banner" style="width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.92);">"""

if roxar_old in html:
    html = html.replace(roxar_old, roxar_new)
    print("2.1. Roxar banner updated (contain, scale 0.92, centered).")
else:
    # Regex fallback
    html = re.sub(
        r'(<article[^>]*id="producto-brand-roxar"[^>]*>\s*<div[^>]*class="brand-section-banner[^"]*"[^>]*style=")([^"]*)(">\s*<img src="img/products/roxar/roxar\.png"[^>]*style=")([^"]*)(")',
        r'\g<1>height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;\g<3>width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.65) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.92);\g<5>',
        html
    )
    print("2.1. Roxar banner regex updated.")

# 2) MICRO MOTION: Shift up to center vertically
html = re.sub(
    r'(<img src="img/products/micromotion/micromotion\.jpg"[^>]*style=")([^"]*)(")',
    r'\g<1>width: 100%; height: 100%; object-fit: cover; object-position: center 78%; filter: brightness(0.60) contrast(1.1); position: absolute; top: 0; left: 0;\g<3>',
    html
)
print("2.2. Micro Motion banner updated (object-position: center 78%).")

# 3) AMS TREX: Shift down and slightly scale so screen and text are in sweet spot
html = re.sub(
    r'(<img src="img/products/ams trex/ams-trex-banner\.jpg"[^>]*style=")([^"]*)(")',
    r'\g<1>width: 100%; height: 100%; object-fit: cover; object-position: center 25%; filter: brightness(0.60) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.96);\g<3>',
    html
)
print("2.3. AMS Trex banner updated (object-position: center 25%, scale 0.96).")

# 4) FLUENTA: Contain and scale so arrows are fully visible and text stays centered
fluenta_old_pat = r'(<article[^>]*id="producto-brand-fluenta"[^>]*>\s*<div[^>]*class="brand-section-banner[^"]*"[^>]*style=")([^"]*)(">\s*<img src="img/products/fluenta/Fluenta-blog-logo\.png"[^>]*style=")([^"]*)(")'
html = re.sub(
    fluenta_old_pat,
    r'\g<1>height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;\g<3>width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.60) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.92);\g<5>',
    html
)
print("2.4. Fluenta banner updated (contain, scale 0.92, arrows fully visible).")

# 5) KAM: Contain, scale and center so it's not cropped at top
kam_old_pat = r'(<article[^>]*id="producto-brand-kam"[^>]*>\s*<div[^>]*class="brand-section-banner[^"]*"[^>]*style=")([^"]*)(">\s*<img src="img/products/kam/kam_logo\.png"[^>]*style=")([^"]*)(")'
html = re.sub(
    kam_old_pat,
    r'\g<1>height: 175px; box-shadow: 0 4px 18px rgba(0,0,0,0.18); background: #ffffff;\g<3>width: 100%; height: 100%; object-fit: contain; object-position: center; filter: brightness(0.60) contrast(1.1); position: absolute; top: 0; left: 0; transform: scale(0.85);\g<5>',
    html
)
print("2.5. Kam banner updated (contain, scale 0.85, centered and legible).")

# =========================================================================
# 3. SERVICE 3 (FLEXIM): SINGLE LARGE CARD WITH VIDEO/FLEXIM-2.MP4
# =========================================================================

# Locate servicio-flexim
flexim_service_start = html.find('id="servicio-flexim"')
if flexim_service_start == -1:
    raise ValueError("id='servicio-flexim' not found in index.html")

flexim_dual_start = html.find('<div class="roxar-dual-section">', flexim_service_start)
flexim_service_end = html.find('</article>', flexim_dual_start)

new_flexim_cards_html = """<div class="roxar-dual-section">
                                    <div class="row g-4 justify-content-center">
                                        <!-- Panel Único en Grande: Medición de Gas y Líquidos Clamp-On -->
                                        <div class="col-12 reveal-on-scroll reveal-up">
                                            <div class="service-flip-card">
                                                <div class="service-flip-inner">
                                                    <div class="service-flip-front">
                                                        <div class="service-video-wrap">
                                                            <button type="button" class="service-media-expand-btn" title="Agrandar pantalla completa" onclick="event.stopPropagation(); expandCardMedia(this);"><i class="fas fa-expand"></i></button>
                                                            <!-- Ambient video blur de fondo -->
                                                            <video loop muted playsinline preload="metadata" class="roxar-card-video roxar-video-ambient-blur" aria-hidden="true">
                                                                <source src="video/flexim-2.mp4" type="video/mp4">
                                                            </video>
                                                            <!-- Video principal en primer plano 100% completo -->
                                                            <video loop muted playsinline preload="metadata" class="roxar-card-video roxar-card-video-foreground" id="video-flexim-2">
                                                                <source src="video/flexim-2.mp4" type="video/mp4">
                                                            </video>
                                                            <!-- Botón central interactivo para reproducir video -->
                                                            <div class="service-card-play-center">
                                                                <div class="service-card-play-icon">
                                                                    <i class="fas fa-play"></i>
                                                                </div>
                                                                <span class="service-card-play-label">Reproducir Video</span>
                                                            </div>
                                                            <div class="service-front-overlay">
                                                                <div class="service-front-title">
                                                                    <i class="fas fa-wave-pulse text-info"></i> MEDICIÓN DE GAS Y LÍQUIDOS CLAMP-ON
                                                                </div>
                                                                <span class="service-flip-hint-badge"><i class="fas fa-rotate me-1"></i> Ver Detalles</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="service-flip-back">
                                                        <div>
                                                            <div class="d-flex justify-content-between align-items-center mb-2 pb-1 border-bottom">
                                                                <span class="roxar-panel-badge mb-0"><i class="fas fa-shield-halved me-1"></i> ULTRASONIDO CLAMP-ON • FM CLASS I DIV 2 / ATEX</span>
                                                            </div>
                                                            <h3 class="roxar-panel-title mb-2 fs-5">Medición de Gas y Líquidos Clamp-On</h3>
                                                            <p class="roxar-panel-desc mb-3 small text-secondary">
                                                                Medición no invasiva clamp-on para gases y líquidos en condiciones operacionales exigentes sin cortes ni paradas.
                                                            </p>
                                                            <ul class="instrument-features mb-0 small text-secondary">
                                                                <li><strong>0 horas de Parada:</strong> Instalación en pared exterior de la tubería sin cortar ni despresurizar el gasoducto.</li>
                                                                <li><strong>Autonomía en Campo.</strong></li>
                                                                <li><strong>Verificación y Auditoría:</strong> Verificación y contraste de medidores en línea sin retirarlos.</li>
                                                            </ul>
                                                        </div>
                                                        <div>
                                                            <div class="service-flip-btn-back">
                                                                <i class="fas fa-arrow-rotate-left"></i> <span>Volver al video</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>"""

html = html[:flexim_dual_start] + new_flexim_cards_html + "\n                            " + html[flexim_service_end:]
print("3. Service 3 (Flexim) updated to 1 single large card with video/flexim-2.mp4 and new content.")

# =========================================================================
# 4. UPDATE INTERACTIVE JS FOR SUBMENU TOGGLING
# =========================================================================

# In the bottom script, ensure the navigation handlers for productos and emerson are robust:
old_brand_js_pat = r'// ==========================================\s*// NAVEGACIÓN INTERACTIVA DEL CATÁLOGO POR MARCA\s*// ==========================================[\s\S]*?</script>'

new_brand_js = """// ==========================================
        // NAVEGACIÓN INTERACTIVA DEL CATÁLOGO POR MARCA Y SIDEBAR
        // ==========================================
        // Toggle para el botón principal de Productos
        $(document).on('click', '#nav-link-productos', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const $submenu = $('#productos-submenu');
            const $chevron = $('#productos-chevron');
            const isPage5 = $('.cd-hero-slider > li[data-page-no="5"]').hasClass('selected');
            const isOpen = $submenu.hasClass('is-open');

            if (isPage5 && isOpen) {
                $submenu.removeClass('is-open');
                $chevron.removeClass('is-rotated');
            } else {
                $submenu.addClass('is-open');
                $chevron.addClass('is-rotated');
                if (!isPage5) {
                    openPage(5);
                    highlightMenu(5);
                }
            }
        });

        // Toggle para el acordeón anidado de EMERSON
        $(document).on('click', '#emerson-nested-toggle', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const $nestedMenu = $('#emerson-nested-menu');
            const $chevron = $('#emerson-chevron');
            
            $nestedMenu.toggleClass('show is-open');
            $chevron.toggleClass('rotate-180 is-rotated');
        });

        $(document).on('click', '.sidebar-nested-submenu .submenu-link, .brand-menu-item', function(e) {
            const targetId = $(this).data('target');
            if (!targetId) return;

            e.preventDefault();
            e.stopPropagation();

            // Abrir Sección 5
            openPage(5);
            highlightMenu(5);

            $('.sidebar-nested-submenu .submenu-link, .brand-menu-item').removeClass('active');
            $(this).addClass('active');

            setTimeout(function() {
                const targetElem = document.getElementById(targetId);
                if (targetElem) {
                    targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, 280);
        });
    </script>"""

html = re.sub(old_brand_js_pat, new_brand_js, html)
print("4. Bottom JS updated with clean independent toggles for Productos and Emerson.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html written successfully! Final length:", len(html))
