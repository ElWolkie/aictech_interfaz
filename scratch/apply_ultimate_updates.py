# -*- coding: utf-8 -*-
"""
apply_ultimate_updates.py
Applies all requested updates:
1. Webflow-inspired Scroll Snapping Cards for Section 5 (Productos) in exact requested order:
   Roxar, Flexim, AMS Trex, Rosemount, Micro Motion, Fluenta, Kam Controls
2. Remove white header box in Section 2 (Servicios), set Service 1 title to 'Well Testing con Medidores Multifásicos Roxar' in white
3. Autoplay active service videos at 60fps, pausing off-screen videos, 1-click expand to lightbox, no play overlay buttons
4. Fix sidebar Emerson dropdown arrow and softly tint each brand color in sidebar
5. Fluid, fast smooth scrolling on sidebar navigation
"""

import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# =========================================================================
# 1. UPDATE SIDEBAR: EMERSON ORDER, CHEVRON & SOFT BRAND COLORS
# =========================================================================

# Old Emerson sidebar block pattern
old_emerson_block_pat = r'<div class="sidebar-nested-group">[\s\S]*?<!-- MARCAS INDEPENDIENTES FUERA DE EMERSON -->[\s\S]*?<a href="#producto-brand-kam"[\s\S]*?</a>'

new_emerson_sidebar = """<div class="sidebar-nested-group">
                        <a href="#producto-brand-emerson" class="submenu-nested-header d-flex align-items-center justify-content-between py-2 px-2" id="emerson-nested-toggle" title="Desplegar marcas Emerson" style="cursor: pointer; text-decoration: none; border-radius: 6px;">
                            <span class="d-flex align-items-center">
                                <span class="submenu-dot me-2" style="background: #38bdf8; margin-right: 8px;"></span>
                                <strong class="submenu-text" style="color: #38bdf8; letter-spacing: 0.5px;">EMERSON</strong>
                            </span>
                            <i class="fas fa-chevron-down nested-chevron small text-info rotate-180 is-rotated" id="emerson-chevron"></i>
                        </a>
                        <div class="sidebar-nested-submenu ps-3 show is-open" id="emerson-nested-menu">
                            <!-- 1. Roxar (Morado) -->
                            <a href="#producto-brand-roxar" class="submenu-link py-1" data-target="producto-brand-roxar">
                                <span class="submenu-dot" style="background: #c084fc; box-shadow: 0 0 6px rgba(192, 132, 252, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #e9d5ff;">Roxar</span>
                            </a>
                            <!-- 2. Flexim (Aguamarina) -->
                            <a href="#producto-brand-flexim" class="submenu-link py-1" data-target="producto-brand-flexim">
                                <span class="submenu-dot" style="background: #2dd4bf; box-shadow: 0 0 6px rgba(45, 212, 191, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #ccfbf1;">Flexim</span>
                            </a>
                            <!-- 3. AMS Trex (Negrito claro) -->
                            <a href="#producto-brand-amstrex" class="submenu-link py-1" data-target="producto-brand-amstrex">
                                <span class="submenu-dot" style="background: #94a3b8; box-shadow: 0 0 6px rgba(148, 163, 184, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #e2e8f0;">AMS Trex</span>
                            </a>
                            <!-- 4. Rosemount (Azul) -->
                            <a href="#producto-brand-rosemount" class="submenu-link py-1" data-target="producto-brand-rosemount">
                                <span class="submenu-dot" style="background: #60a5fa; box-shadow: 0 0 6px rgba(96, 165, 250, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #dbeafe;">Rosemount</span>
                            </a>
                            <!-- 5. Micro Motion (Gris) -->
                            <a href="#producto-brand-micromotion" class="submenu-link py-1" data-target="producto-brand-micromotion">
                                <span class="submenu-dot" style="background: #cbd5e1; box-shadow: 0 0 6px rgba(203, 213, 225, 0.6); margin-right: 8px;"></span>
                                <span class="submenu-text" style="color: #f1f5f9;">Micro Motion</span>
                            </a>
                        </div>
                    </div>

                    <!-- MARCAS INDEPENDIENTES FUERA DE EMERSON -->
                    <!-- 6. Fluenta (Verde) -->
                    <a href="#producto-brand-fluenta" class="submenu-link py-1 mt-1" data-target="producto-brand-fluenta">
                        <span class="submenu-dot" style="background: #4ade80; box-shadow: 0 0 6px rgba(74, 222, 128, 0.6); margin-right: 8px;"></span>
                        <span class="submenu-text" style="color: #dcfce7;">Fluenta</span>
                    </a>
                    <!-- 7. Kam Controls (Naranja) -->
                    <a href="#producto-brand-kam" class="submenu-link py-1" data-target="producto-brand-kam">
                        <span class="submenu-dot" style="background: #fb923c; box-shadow: 0 0 6px rgba(251, 146, 60, 0.6); margin-right: 8px;"></span>
                        <span class="submenu-text" style="color: #ffedd5;">Kam Controls</span>
                    </a>"""

html = re.sub(old_emerson_block_pat, new_emerson_sidebar, html)
print("1. Sidebar Emerson order and soft brand colors updated.")

# =========================================================================
# 2. SECTION 2 (SERVICIOS): REMOVE WHITE HEADER BOX & UPDATE HERO 1 TITLE
# =========================================================================

# Remove the white header box from Section 2
white_header_pat = r'<!-- Header de la Sección -->[\s\S]*?<div class="catalog-hero-box reveal-on-scroll reveal-up mb-4" style="background: #ffffff;[\s\S]*?</div>\s*</div>'
html = re.sub(white_header_pat, '', html)

# Update Hero 1 title in Service 1
hero1_title_pat = r'(<article[^>]*id="servicio-multifasico"[\s\S]*?<div class="roxar-hero-content">\s*<h2 class="roxar-title">)([^<]+)(</h2>)'
html = re.sub(
    hero1_title_pat,
    r'\g<1>Well Testing con Medidores Multifásicos Roxar\g<3>',
    html
)
print("2. Section 2 white header box removed and Hero 1 title updated.")

# Remove all centered play overlays from flip cards in Section 2
play_center_pat = r'<div class="service-card-play-center">[\s\S]*?</div>\s*</div>'
# Replace with just closing div of service-card-play-center parent
# Let's inspect play overlay structure:
# <div class="service-card-play-center">
#     <div class="service-card-play-icon">
#         <i class="fas fa-play"></i>
#     </div>
#     <span class="service-card-play-label">Reproducir Video</span>
# </div>
play_overlay_pat = r'<div class="service-card-play-center">\s*<div class="service-card-play-icon">\s*<i class="fas fa-play"></i>\s*</div>\s*<span class="service-card-play-label">Reproducir Video</span>\s*</div>'
count_removed = len(re.findall(play_overlay_pat, html))
html = re.sub(play_overlay_pat, '', html)
print(f"3. Removed {count_removed} play overlay buttons from service cards.")

# Ensure card videos have autoplay loop muted playsinline
card_video_pat = r'(<video[^>]*class="[^"]*roxar-card-video[^"]*")([^>]*)>'
def fix_video_tag(m):
    tag_start = m.group(1)
    rest = m.group(2)
    # Ensure autoplay muted loop playsinline are present
    attrs = ['autoplay', 'loop', 'muted', 'playsinline', 'webkit-playsinline', 'disablePictureInPicture', 'preload="auto"']
    for a in attrs:
        key = a.split('=')[0]
        if key not in rest:
            rest = f' {a}' + rest
    # Remove controls if present
    rest = re.sub(r'\bcontrols\b', '', rest)
    return f"{tag_start}{rest}>"

html = re.sub(card_video_pat, fix_video_tag, html)
print("4. Ensured all card videos are configured for smooth autoplay without controls.")

# =========================================================================
# 3. SECTION 5: REPLACE WITH SCROLL-SNAPPING CARDS (WEBFLOW STYLE)
# =========================================================================

with open('scratch/generated_section5_cards.html', 'r', encoding='utf-8') as f:
    cards_section5_html = f.read()

# Locate Section 5 li in html
p5_match = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', html)
if not p5_match:
    raise ValueError("Could not find <li data-page-no=5 in index.html")
p5_start = p5_match.start()

p6_match = re.search(r'<li[^>]*data-page-no=[\'"]6[\'"]', html[p5_start:])
if not p6_match:
    raise ValueError("Could not find <li data-page-no=6 in index.html")
p6_start = p5_start + p6_match.start()

html = html[:p5_start] + cards_section5_html + "\n                " + html[p6_start:]
print("5. Section 5 replaced with Webflow-style Scroll Snapping Cards.")

# =========================================================================
# 4. ADD CSS STYLES FOR SCROLL SNAPPING CARDS & FLUID ANIMATIONS
# =========================================================================

cards_css = """
        /* ============================================================= */
        /* WEBFLOW-STYLE SCROLL SNAPPING CARDS (SECCIÓN 5: PRODUCTOS)    */
        /* ============================================================= */
        .catalog-feed-wrapper {
            scroll-snap-type: y proximity;
            scroll-behavior: smooth !important;
            padding-bottom: 50px;
        }

        .brand-snapping-card-section {
            scroll-snap-align: start;
            scroll-snap-stop: normal;
            margin-bottom: 38px;
            scroll-margin-top: 20px;
        }

        .brand-snapping-card-inner {
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            border-radius: 20px !important;
        }

        .brand-snapping-card-inner:hover {
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.14) !important;
        }

        .showcase-scroll-gallery::-webkit-scrollbar {
            width: 5px;
        }
        .showcase-scroll-gallery::-webkit-scrollbar-track {
            background: #f1f5f9;
            border-radius: 4px;
        }
        .showcase-scroll-gallery::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        .showcase-scroll-gallery::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }

        /* RESALTE VISUAL FLUIDO AL NAVEGAR DESDE EL SIDEBAR */
        @keyframes targetFluidGlow {
            0% {
                box-shadow: 0 0 0 0 rgba(56, 182, 255, 0.6);
                border-color: rgba(56, 182, 255, 0.9);
            }
            50% {
                box-shadow: 0 0 35px 6px rgba(56, 182, 255, 0.45);
                border-color: #38b6ff;
            }
            100% {
                box-shadow: 0 0 0 0 rgba(56, 182, 255, 0);
            }
        }

        .target-service-highlight {
            animation: targetFluidGlow 1.6s ease-out forwards;
        }

        /* 60FPS OPTIMIZACIONES DE RENDERIZADO EN VIDEOS */
        video.roxar-video-bg,
        video.roxar-card-video {
            will-change: transform;
            transform: translateZ(0);
            backface-visibility: hidden;
        }
"""

# Insert CSS into <style>
style_end = html.find('</style>')
if style_end != -1:
    html = html[:style_end] + cards_css + "\n    " + html[style_end:]
    print("6. CSS for Scroll Snapping Cards and 60fps video optimizations added.")

# =========================================================================
# 5. UPDATE JAVASCRIPT: 60FPS OBSERVER, IMMEDIATE EXPAND, FLUID NAVIGATION
# =========================================================================

# Replace bottom script logic with new comprehensive handlers
js_update_pat = r'// ==========================================\s*// NAVEGACIÓN INTERACTIVA DEL CATÁLOGO POR MARCA Y SIDEBAR[\s\S]*?</script>'

new_js_code = """// ==========================================
        // NAVEGACIÓN FLUIDA, INTERSECTION OBSERVER 60FPS Y CONTROLES
        // ==========================================

        // Navegación rápida y ultra fluida hacia elementos objetivo
        window.fluidNavigateTo = function(targetId) {
            const el = document.getElementById(targetId);
            if (!el) return;

            const headerOffset = 15;
            const elementPosition = el.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });

            // Resalte suave
            el.classList.remove('target-service-highlight');
            void el.offsetWidth;
            el.classList.add('target-service-highlight');
            setTimeout(() => {
                el.classList.remove('target-service-highlight');
            }, 1800);
        };

        // Toggle del Acordeón EMERSON (Flecha hacia arriba al abrir, hacia abajo al cerrar)
        $(document).on('click', '#emerson-nested-toggle', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const $menu = $('#emerson-nested-menu');
            const $chev = $('#emerson-chevron');
            const isOpen = $menu.hasClass('show') || $menu.hasClass('is-open');

            if (isOpen) {
                $menu.removeClass('show is-open');
                $chev.removeClass('rotate-180 is-rotated');
            } else {
                $menu.addClass('show is-open');
                $chev.addClass('rotate-180 is-rotated');
            }
        });

        // Navegación desde el submenú de Productos
        $(document).on('click', '.sidebar-nested-submenu .submenu-link, .brand-menu-item, #productos-submenu > a.submenu-link', function(e) {
            const targetId = $(this).data('target') || $(this).attr('data-target');
            if (!targetId) return;

            e.preventDefault();
            e.stopPropagation();

            // Abrir Sección 5
            openPage(5);
            highlightMenu(5);

            $('.sidebar-nested-submenu .submenu-link, #productos-submenu a.submenu-link').removeClass('active');
            $(this).addClass('active');

            setTimeout(function() {
                window.fluidNavigateTo(targetId);
            }, 60);
        });

        // Clic directo en video de servicio: Expansión inmediata a Lightbox HD en 1 clic
        $(document).on('click', '.service-video-wrap', function(e) {
            // Si el clic fue en el botón de ver detalles/voltear, no expandir
            if ($(e.target).closest('.service-flip-hint-badge, .service-flip-btn-back').length > 0) {
                return;
            }
            e.preventDefault();
            e.stopPropagation();
            window.expandCardMedia(this);
        });

        // Volteo manual de tarjetas para ver especificaciones técnicas
        $(document).on('click', '.service-flip-hint-badge, .service-flip-btn-back', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const card = $(this).closest('.service-flip-card');
            card.toggleClass('is-flipped');
        });

        // =========================================================================
        // OBSERVADOR ACTIVO 60FPS: SOLO REPRODUCE VIDEOS DE LA SECCIÓN VISIBLE
        // Pausa automáticamente los videos de las demás secciones para máximo rendimiento
        // =========================================================================
        (function initActiveSectionVideoObserver() {
            const serviceArticles = document.querySelectorAll(
                '#servicio-multifasico, #servicio-bifasico-trifasico, #servicio-flexim, ' +
                '#servicio-echometer, #servicio-trasegado, #servicio-soldadura-taller, ' +
                '#servicio-asistencia-automatizacion'
            );

            if (!('IntersectionObserver' in window)) return;

            const observer = new IntersectionObserver((entries) => {
                const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
                const isPage2Active = page2 && page2.classList.contains('selected');
                if (!isPage2Active) return;

                entries.forEach(entry => {
                    const sectionVideos = entry.target.querySelectorAll('video');
                    if (entry.isIntersecting && entry.intersectionRatio >= 0.20) {
                        // Reproducir inmediatamente los videos de esta sección
                        sectionVideos.forEach(v => {
                            v.muted = true;
                            const p = v.play();
                            if (p !== undefined) p.catch(() => {});
                        });
                    } else if (!entry.isIntersecting || entry.intersectionRatio < 0.10) {
                        // Pausar inmediatamente videos de secciones fuera de pantalla
                        sectionVideos.forEach(v => {
                            if (!v.paused) v.pause();
                        });
                    }
                });
            }, {
                root: null,
                threshold: [0.10, 0.20, 0.40, 0.60]
            });

            serviceArticles.forEach(art => observer.observe(art));
        })();
    </script>"""

html = re.sub(js_update_pat, new_js_code, html)
print("7. JavaScript handlers for 60fps observer, 1-click expand, and fluid navigation updated.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully! Final length:", len(html))
