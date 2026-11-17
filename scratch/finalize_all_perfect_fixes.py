# -*- coding: utf-8 -*-
"""
finalize_all_perfect_fixes.py
Restores Service 1 hero banner, cleans video tags, ensures 60fps IntersectionObserver,
perfects Emerson accordion chevron, and guarantees smooth fluid navigation.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Initial length:", len(html))

# -------------------------------------------------------------------------
# 1. RESTORE SERVICE 1 HERO BANNER IN SECTION 2
# -------------------------------------------------------------------------
# Locate <div class="services-feed-wrapper"> in Section 2
target_sec2_top = '<div class="services-feed-wrapper">\n                            \n                            \n\n                                <!-- Sección Inferior: 2 Flip Cards'
replacement_sec2_top = """<div class="services-feed-wrapper">
                            
                            <!-- 1. SERVICIO: MEDIDOR MULTIFÁSICO ROXAR 2600 (VIDEO + MÓDULOS DUALES) -->
                            <article class="roxar-showcase-container reveal-on-scroll reveal-up" id="servicio-multifasico">
                                
                                <!-- Banner Superior con Video de Fondo (Cinemático) -->
                                <div class="roxar-hero-banner" style="position: relative; overflow: hidden; border-radius: 12px; margin-bottom: 24px;">
                                    <video autoplay loop muted playsinline webkit-playsinline disablePictureInPicture preload="auto" class="roxar-video-bg service-video-elem" id="roxar-main-video" style="width: 100%; height: 100%; object-fit: cover;">
                                        <source src="video/roxar2600.mp4" type="video/mp4">
                                        Su navegador no soporta video HTML5.
                                    </video>
                                    <div class="roxar-video-overlay" style="background: linear-gradient(135deg, rgba(2, 10, 26, 0.65) 0%, rgba(2, 15, 38, 0.40) 50%, rgba(2, 10, 26, 0.70) 100%); position: absolute; inset: 0;"></div>
                                    <div class="roxar-hero-content" style="position: relative; z-index: 2; padding: 36px 32px;">
                                        <h2 class="roxar-title" style="color: #ffffff !important; font-size: clamp(1.8rem, 3.2vw, 2.5rem); font-weight: 800; text-shadow: 0 2px 12px rgba(0,0,0,0.85); margin-bottom: 8px;">Well Testing con Medidores Multifásicos Roxar</h2>
                                        <p class="roxar-lead-text" style="color: #e2e8f0 !important; font-size: 1.05rem; text-shadow: 0 1px 8px rgba(0,0,0,0.8); margin-bottom: 0; max-width: 900px; line-height: 1.6;">
                                            Medición en línea de caudales de petróleo, agua y gas en tiempo real sin separación invasiva.
                                        </p>
                                    </div>
                                </div>

                                <!-- Sección Inferior: 2 Flip Cards"""

if target_sec2_top in html:
    html = html.replace(target_sec2_top, replacement_sec2_top, 1)
    print("1. Successfully restored Service 1 Hero Banner at top of Section 2.")
else:
    # Alternative match if whitespace differs slightly
    sec2_sub_pat = r'(<div class="services-feed-wrapper">\s*)(<!-- Sección Inferior: 2 Flip Cards)'
    if re.search(sec2_sub_pat, html):
        html = re.sub(
            sec2_sub_pat,
            r'\1<!-- 1. SERVICIO: MEDIDOR MULTIFÁSICO ROXAR 2600 (VIDEO + MÓDULOS DUALES) -->\n                            <article class="roxar-showcase-container reveal-on-scroll reveal-up" id="servicio-multifasico">\n                                \n                                <!-- Banner Superior con Video de Fondo (Cinemático) -->\n                                <div class="roxar-hero-banner" style="position: relative; overflow: hidden; border-radius: 12px; margin-bottom: 24px;">\n                                    <video autoplay loop muted playsinline webkit-playsinline disablePictureInPicture preload="auto" class="roxar-video-bg service-video-elem" id="roxar-main-video" style="width: 100%; height: 100%; object-fit: cover;">\n                                        <source src="video/roxar2600.mp4" type="video/mp4">\n                                        Su navegador no soporta video HTML5.\n                                    </video>\n                                    <div class="roxar-video-overlay" style="background: linear-gradient(135deg, rgba(2, 10, 26, 0.65) 0%, rgba(2, 15, 38, 0.40) 50%, rgba(2, 10, 26, 0.70) 100%); position: absolute; inset: 0;"></div>\n                                    <div class="roxar-hero-content" style="position: relative; z-index: 2; padding: 36px 32px;">\n                                        <h2 class="roxar-title" style="color: #ffffff !important; font-size: clamp(1.8rem, 3.2vw, 2.5rem); font-weight: 800; text-shadow: 0 2px 12px rgba(0,0,0,0.85); margin-bottom: 8px;">Well Testing con Medidores Multifásicos Roxar</h2>\n                                        <p class="roxar-lead-text" style="color: #e2e8f0 !important; font-size: 1.05rem; text-shadow: 0 1px 8px rgba(0,0,0,0.8); margin-bottom: 0; max-width: 900px; line-height: 1.6;">\n                                            Medición en línea de caudales de petróleo, agua y gas en tiempo real sin separación invasiva.\n                                        </p>\n                                    </div>\n                                </div>\n\n                                \2',
            html,
            count=1
        )
        print("1b. Restored Service 1 Hero Banner via regex.")

# -------------------------------------------------------------------------
# 2. CLEAN AND STANDARDIZE ALL VIDEO TAGS IN SECTION 2
# -------------------------------------------------------------------------
# In Section 2, all video tags must be clean, autoplay, loop, muted, playsinline, no controls bar
p2_m = re.search(r'<li[^>]*data-page-no=[\'"]2[\'"]', html)
p3_m = re.search(r'<li[^>]*data-page-no=[\'"]3[\'"]', html)

if p2_m and p3_m:
    p2_s = p2_m.start()
    p3_s = p3_m.start()
    sec2_body = html[p2_s:p3_s]

    # Clean up redundant attributes in <video ...>
    def clean_sec2_video(m):
        full_tag = m.group(0)
        # extract id
        id_m = re.search(r'id=[\'"]([^\'"]+)[\'"]', full_tag)
        id_str = f' id="{id_m.group(1)}"' if id_m else ''
        # extract class
        cls_m = re.search(r'class=[\'"]([^\'"]+)[\'"]', full_tag)
        cls_str = f' class="{cls_m.group(1)}"' if cls_m else ''
        # extract style
        sty_m = re.search(r'style=[\'"]([^\'"]+)[\'"]', full_tag)
        sty_str = f' style="{sty_m.group(1)}"' if sty_m else ''
        # aria-hidden
        aria_m = re.search(r'aria-hidden=[\'"]([^\'"]+)[\'"]', full_tag)
        aria_str = f' aria-hidden="{aria_m.group(1)}"' if aria_m else ''

        return f'<video autoplay loop muted playsinline webkit-playsinline disablePictureInPicture preload="auto"{cls_str}{id_str}{sty_str}{aria_str}>'

    sec2_cleaned = re.sub(r'<video[^>]+>', clean_sec2_video, sec2_body)
    html = html[:p2_s] + sec2_cleaned + html[p3_s:]
    print("2. Standardized all Section 2 video tags for pure 60fps autoplay without controls.")

# -------------------------------------------------------------------------
# 3. ENSURE CHEVRON ROTATION & EMERSON TOGGLE JS
# -------------------------------------------------------------------------
# Make sure .nested-chevron has inline-block and transform
chevron_css_rule = """
        .nested-chevron {
            display: inline-block !important;
            transition: transform 0.25s ease;
        }

        .nested-chevron.rotate-180,
        .nested-chevron.is-rotated {
            transform: rotate(180deg) !important;
        }
"""
if '.nested-chevron {' in html:
    html = re.sub(
        r'\.nested-chevron\s*\{[^}]*\}[\s\S]*?\.nested-chevron\.rotate-180[^{]*\{[^}]*\}',
        chevron_css_rule.strip(),
        html
    )
print("3. Chevron CSS enforced.")

# -------------------------------------------------------------------------
# 4. ROBUST INTERSECTION OBSERVER & 1-CLICK LIGHTBOX IN JAVASCRIPT
# -------------------------------------------------------------------------
# Update the bottom script block with the complete, highly performant video manager
new_js_block = """// ==========================================
        // NAVEGACIÓN FLUIDA, INTERSECTION OBSERVER 60FPS Y CONTROLES
        // ==========================================

        // Navegación ultra-fluida y rápida hacia cualquier sección
        window.fluidNavigateTo = function(targetId) {
            const el = document.getElementById(targetId);
            if (!el) return;

            const headerOffset = 20;
            const elementPosition = el.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });

            // Resalte temporal suave
            el.classList.remove('target-service-highlight');
            void el.offsetWidth;
            el.classList.add('target-service-highlight');
            setTimeout(() => {
                el.classList.remove('target-service-highlight');
            }, 1800);
        };

        // Toggle del Acordeón EMERSON (Flecha hacia arriba si abierto, hacia abajo si cerrado)
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
            }, 70);
        });

        // Navegación desde el submenú de Servicios (01 Multifásico, 02 Separadores, etc.)
        $(document).on('click', '#servicios-submenu a.submenu-link', function(e) {
            const href = $(this).attr('href');
            if (!href || href === '#' || href === '#0') return;
            const targetId = href.replace('#', '');
            if (!targetId) return;

            e.preventDefault();
            e.stopPropagation();

            openPage(2);
            highlightMenu(2);

            $('#servicios-submenu a.submenu-link').removeClass('active');
            $(this).addClass('active');

            setTimeout(function() {
                window.fluidNavigateTo(targetId);
            }, 70);
        });

        // Clic en Video de Servicio: Expansión inmediata a Lightbox HD en 1 clic
        $(document).on('click', '.service-video-wrap', function(e) {
            // Si el clic fue en el botón de ver detalles o controles de carrusel, no expandir a lightbox
            if ($(e.target).closest('.service-flip-hint-badge, .service-flip-btn-back, .card-slider-pills, .card-slider-arrow').length > 0) {
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
        window.activeServiceObserver = null;

        function updateServiceVideosPlayback() {
            const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
            const isPage2Active = page2 && page2.classList.contains('selected');

            if (!isPage2Active) {
                // Pausar absolutamente todos los videos de servicios si no estamos en la página 2
                document.querySelectorAll('.cd-hero-slider > li[data-page-no="2"] video').forEach(v => {
                    if (!v.paused) v.pause();
                });
                return;
            }

            const serviceArticles = document.querySelectorAll(
                '#servicio-multifasico, #servicio-bifasico-trifasico, #servicio-flexim, ' +
                '#servicio-echometer, #servicio-trasegado, #servicio-soldadura-taller, ' +
                '#servicio-asistencia-automatizacion'
            );

            const viewportHeight = window.innerHeight || document.documentElement.clientHeight;

            // Determinar qué servicio tiene mayor presencia en el viewport
            let bestArticle = null;
            let maxOverlap = 0;

            serviceArticles.forEach(art => {
                const rect = art.getBoundingClientRect();
                const overlap = Math.max(0, Math.min(rect.bottom, viewportHeight) - Math.max(rect.top, 0));
                if (overlap > maxOverlap) {
                    maxOverlap = overlap;
                    bestArticle = art;
                }
            });

            // Si hay un artículo visible predominante, reproducir solo sus videos y pausar el resto
            serviceArticles.forEach(art => {
                const vids = art.querySelectorAll('video');
                if (art === bestArticle && maxOverlap >= 80) {
                    vids.forEach(v => {
                        v.muted = true;
                        const p = v.play();
                        if (p !== undefined) p.catch(() => {});
                    });
                } else {
                    vids.forEach(v => {
                        if (!v.paused) v.pause();
                    });
                }
            });
        }

        (function initActiveSectionVideoObserver() {
            const serviceArticles = document.querySelectorAll(
                '#servicio-multifasico, #servicio-bifasico-trifasico, #servicio-flexim, ' +
                '#servicio-echometer, #servicio-trasegado, #servicio-soldadura-taller, ' +
                '#servicio-asistencia-automatizacion'
            );

            if ('IntersectionObserver' in window) {
                window.activeServiceObserver = new IntersectionObserver((entries) => {
                    const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
                    if (!page2 || !page2.classList.contains('selected')) return;
                    updateServiceVideosPlayback();
                }, {
                    root: null,
                    threshold: [0.15, 0.35, 0.55]
                });

                serviceArticles.forEach(art => window.activeServiceObserver.observe(art));
            }

            // Integrar con scroll throttled a 60fps usando requestAnimationFrame
            let ticking = false;
            window.addEventListener('scroll', function() {
                if (!ticking) {
                    window.requestAnimationFrame(function() {
                        const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
                        if (page2 && page2.classList.contains('selected')) {
                            updateServiceVideosPlayback();
                        }
                        ticking = false;
                    });
                    ticking = true;
                }
            }, { passive: true });
        })();
    </script>"""

# Replace in index.html
old_js_block_pat = r'// ==========================================\s*// NAVEGACIÓN FLUIDA, INTERSECTION OBSERVER 60FPS Y CONTROLES[\s\S]*?</script>'
if re.search(old_js_block_pat, html):
    html = re.sub(old_js_block_pat, new_js_block, html)
    print("4. Replaced JavaScript logic with refined 60fps manager and fluid navigation.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html fully updated. New length:", len(html))
