# -*- coding: utf-8 -*-
"""
apply_final_v2_fixes.py
Applies all requested fixes to index.html:
1. Swap welding videos (soldadura-1 to main banner, soldadura to left card)
2. AICTECH intro modal with video/inicio-aic.mp4, triggered by clicking AICTECH logo
3. Replace Section 5 with generated_section5_v2.html (no duplicate Emerson banner, morado Roxar, azul Rosemount, aguamarina Flexim, negrito claro AMS Trex, verde Fluenta, naranja Kam, gris Micro Motion, bright white text, no icon boxes)
4. Fix lightbox script location (separate <script src="js/sidebar-collapse.js"></script> from inline <script>)
5. Fix lightbox CSS to contain images with white background and padding
6. Attach robust click handlers for product image expansion and AICTECH intro
"""

import sys
import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# ----------------------------------------------------
# 1. SWAP WELDING VIDEOS (SECCIÓN 2)
# ----------------------------------------------------
# Banner gets soldadura-1.mp4, left card gets soldadura.mp4
soldadura_section_idx = html.find('id="servicio-soldadura-taller"')
if soldadura_section_idx == -1:
    raise ValueError("Could not find servicio-soldadura-taller")

soldadura_section_end = html.find('id="servicio-asistencia-automatizacion"', soldadura_section_idx)
if soldadura_section_end == -1:
    soldadura_section_end = html.find('</li>', soldadura_section_idx)

soldadura_block = html[soldadura_section_idx:soldadura_section_end]

# Verify current sources in this block
if 'id="soldadura-main-video"' not in soldadura_block:
    raise ValueError("Could not find soldadura-main-video in soldadura_block")
if 'id="video-soldadura-1"' not in soldadura_block:
    raise ValueError("Could not find video-soldadura-1 in soldadura_block")

# Perform swap within soldadura_block
# 1) main video gets soldadura-1.mp4
# 2) card video gets soldadura.mp4
main_video_pat = r'(<video[^>]*id="soldadura-main-video"[^>]*>\s*<source src="video/)([^"]+)(")'
card_video_pat = r'(<video[^>]*id="video-soldadura-1"[^>]*>\s*<source src="video/)([^"]+)(")'

new_soldadura_block = re.sub(
    main_video_pat,
    r'\g<1>soldadura-1.mp4\g<3>',
    soldadura_block
)
new_soldadura_block = re.sub(
    card_video_pat,
    r'\g<1>soldadura.mp4\g<3>',
    new_soldadura_block
)

html = html[:soldadura_section_idx] + new_soldadura_block + html[soldadura_section_end:]
print("1. Welding videos swapped successfully.")

# ----------------------------------------------------
# 2. UPDATE AICTECH LOGOS TO TRIGGER INTRO MODAL
# ----------------------------------------------------
# Update sidebar logo link
sidebar_logo_pat = r'(<div class="sidebar-heading text-center pt-4 pb-2">\s*<!-- LOGO AICTECH -->\s*<a href=")[^"]*("[^>]*>)'
html = re.sub(
    sidebar_logo_pat,
    r'\g<1>#0" class="d-block text-decoration-none" title="Presentación AICTECH" onclick="openAictechIntroModal(event); return false;\g<2>',
    html
)

# Update mobile navbar logo
mobile_logo_pat = r'(<img src="img/aictech_logo\.png" alt="AICTECH Logo")([^>]*>)'
html = re.sub(
    mobile_logo_pat,
    r'\g<1> style="max-height: 35px; cursor: pointer;" onclick="openAictechIntroModal(event);"\g<2>',
    html
)
print("2. AICTECH logos wired to openAictechIntroModal.")

# ----------------------------------------------------
# 3. REPLACE SECTION 5 WITH GENERATED SECTION 5 V2
# ----------------------------------------------------
with open('scratch/generated_section5_v2.html', 'r', encoding='utf-8') as f:
    section5_html = f.read()

# Locate Section 5 li in html
p5_match = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', html)
if not p5_match:
    raise ValueError("Could not find <li data-page-no=5 in index.html")
p5_start = p5_match.start()

p6_match = re.search(r'<li[^>]*data-page-no=[\'"]6[\'"]', html[p5_start:])
if not p6_match:
    raise ValueError("Could not find <li data-page-no=6 in index.html")
p6_start = p5_start + p6_match.start()

html = html[:p5_start] + section5_html + "\n                " + html[p6_start:]
print("3. Section 5 replaced with generated_section5_v2.html.")

# ----------------------------------------------------
# 4. FIX LIGHTBOX CSS & ADD INTRO MODAL CSS
# ----------------------------------------------------
# Fix media lightbox stage img CSS to contain with white pad
old_css_rule = """.media-lightbox-stage video,
        .media-lightbox-stage img {
            max-width: 100%;
            max-height: 80vh;
            width: auto;
            height: auto;
            object-fit: cover !important;
            display: block;
        }"""

new_css_rule = """.media-lightbox-stage video {
            max-width: 100%;
            max-height: 80vh;
            width: auto;
            height: auto;
            object-fit: contain !important;
            display: block;
        }
        .media-lightbox-stage img {
            max-width: 90vw;
            max-height: 80vh;
            width: auto;
            height: auto;
            object-fit: contain !important;
            background: #ffffff;
            border-radius: 8px;
            padding: 16px;
            display: block;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }
        /* MODAL INTRO CINEMÁTICO AICTECH */
        .aictech-intro-overlay {
            position: fixed;
            inset: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.96);
            backdrop-filter: blur(10px);
            z-index: 100200;
            display: none;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .aictech-intro-overlay.active {
            display: flex;
            opacity: 1;
        }
        .aictech-intro-container {
            position: relative;
            max-width: 1100px;
            max-height: 88vh;
            width: 95%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .aictech-intro-close {
            position: absolute;
            top: -50px;
            right: 0;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #ffffff;
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.25rem;
            transition: all 0.2s ease;
        }
        .aictech-intro-close:hover {
            background: #ef4444;
            border-color: #ef4444;
            transform: scale(1.08);
        }
        .aictech-intro-video-wrapper {
            width: 100%;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba(56, 182, 255, 0.35);
            border: 1px solid rgba(56, 182, 255, 0.3);
            background: #000000;
        }
        .aictech-intro-video-wrapper video {
            width: 100%;
            max-height: 80vh;
            display: block;
            object-fit: contain !important;
            outline: none;
        }"""

if old_css_rule in html:
    html = html.replace(old_css_rule, new_css_rule)
    print("4. Lightbox and Intro modal CSS updated.")
else:
    print("Warning: old_css_rule exact string not matched, attempting regex replacement.")
    html = re.sub(
        r'\.media-lightbox-stage video,\s*\.media-lightbox-stage img\s*\{[^}]*\}',
        new_css_rule,
        html
    )
    print("4. Lightbox and Intro modal CSS regex replaced.")

# ----------------------------------------------------
# 5. INSERT AICTECH INTRO MODAL HTML
# ----------------------------------------------------
intro_modal_html = """<!-- MODAL INTRO CINEMÁTICO AICTECH (INICIO-AIC.MP4) -->
    <div id="aictech-intro-modal" class="aictech-intro-overlay" onclick="if(event.target===this) closeAictechIntroModal();">
        <div class="aictech-intro-container">
            <button type="button" class="aictech-intro-close" onclick="closeAictechIntroModal();" title="Cerrar Presentación"><i class="fas fa-times"></i></button>
            <div class="aictech-intro-video-wrapper">
                <video id="aictech-intro-video" playsinline controls preload="auto">
                    <source src="video/inicio-aic.mp4" type="video/mp4">
                    Tu navegador no soporta reproducción de video HTML5.
                </video>
            </div>
        </div>
    </div>
"""

# Check if intro modal already exists
if 'id="aictech-intro-modal"' not in html:
    # Insert right before media-lightbox-modal
    lb_idx = html.find('<!-- MODAL LIGHTBOX PARA VISUALIZACIÓN')
    if lb_idx == -1:
        lb_idx = html.find('<div id="media-lightbox-modal"')
    if lb_idx != -1:
        html = html[:lb_idx] + intro_modal_html + "\n    " + html[lb_idx:]
        print("5. AICTECH intro modal HTML inserted.")
    else:
        # Append before </body>
        b_idx = html.rfind('</body>')
        html = html[:b_idx] + intro_modal_html + "\n" + html[b_idx:]
        print("5. AICTECH intro modal HTML appended before </body>.")

# ----------------------------------------------------
# 6. FIX SCRIPTS AND JAVASCRIPT AT THE BOTTOM
# ----------------------------------------------------
# The bug was that inline scripts were inside <script src="js/sidebar-collapse.js">
# We must split them cleanly!

sidebar_script_match = re.search(r'<script src=[\'"]js/sidebar-collapse\.js[\'"]>([\s\S]*?)</script>', html)
if sidebar_script_match:
    old_script_block = sidebar_script_match.group(0)
    inner_js = sidebar_script_match.group(1)

    # Clean up and ensure functions are defined
    new_script_block = """<script src="js/sidebar-collapse.js"></script>
    <script>
        // ==========================================
        // PAUSA GLOBAL DE VIDEOS DE SEGUNDO PLANO
        // ==========================================
        window.pauseAllBackgroundVideos = function(excludeVideo) {
            document.querySelectorAll('video').forEach(function(v) {
                if (v !== excludeVideo && !v.paused) {
                    v.dataset.wasPlaying = 'true';
                    v.pause();
                }
            });
        };

        // ==========================================
        // MODAL INTRO CINEMÁTICO AICTECH
        // ==========================================
        window.openAictechIntroModal = function(e) {
            if (e && e.preventDefault) e.preventDefault();
            if (e && e.stopPropagation) e.stopPropagation();

            window.pauseAllBackgroundVideos();

            const modal = document.getElementById('aictech-intro-modal');
            const video = document.getElementById('aictech-intro-video');
            if (!modal || !video) return;

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            video.currentTime = 0;
            video.muted = false;
            const playPromise = video.play();
            if (playPromise !== undefined) {
                playPromise.catch(function() {
                    video.muted = true;
                    video.play();
                });
            }
        };

        window.closeAictechIntroModal = function() {
            const modal = document.getElementById('aictech-intro-modal');
            const video = document.getElementById('aictech-intro-video');
            if (video) {
                video.pause();
            }
            if (modal) {
                modal.classList.remove('active');
            }
            document.body.style.overflow = '';
        };

        // ==========================================
        // EXPANDIR FOTOS DE PRODUCTOS EN LIGHTBOX HD
        // ==========================================
        window.expandMediaFromElement = function(elem) {
            if (!elem) return;
            const card = elem.closest('.emerson-product-card') || elem.closest('.featured-product-card-large') || elem.parentElement;
            const img = elem.tagName === 'IMG' ? elem : elem.querySelector('img');
            if (!img) return;

            let title = '';
            if (card) {
                const titleElem = card.querySelector('.product-card-title, h4, h3');
                if (titleElem) title = titleElem.innerText.trim();
            }

            const stage = document.getElementById('media-lightbox-stage');
            const titleNode = document.getElementById('media-lightbox-title');
            const modal = document.getElementById('media-lightbox-modal');
            if (!stage || !modal) return;

            // Pausar cualquier video activo
            window.pauseAllBackgroundVideos();

            stage.innerHTML = '';
            const newImg = document.createElement('img');
            newImg.src = img.src;
            newImg.alt = title || img.alt || 'Producto en Alta Resolución';
            stage.appendChild(newImg);
            if (titleNode) titleNode.textContent = title || img.alt || 'Visualización en Alta Resolución';
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        };

        window.closeMediaLightbox = function() {
            const modal = document.getElementById('media-lightbox-modal');
            const stage = document.getElementById('media-lightbox-stage');
            if (!modal) return;

            if (stage) {
                const video = stage.querySelector('video');
                if (video) {
                    video.pause();
                }
                stage.innerHTML = '';
            }

            modal.classList.remove('active');
            document.body.style.overflow = '';
        };

        // ==========================================
        // DELEGATED EVENT LISTENERS
        // ==========================================
        $(document).on('click', '.product-card-media-wrapper, .product-expand-badge, .emerson-product-img', function(e) {
            e.preventDefault();
            e.stopPropagation();
            window.expandMediaFromElement(this);
        });

        $(document).on('click', '.sidebar-heading a, .sidebar-heading img', function(e) {
            e.preventDefault();
            e.stopPropagation();
            window.openAictechIntroModal(e);
        });

        $(document).on('keydown', function(e) {
            if (e.key === 'Escape') {
                window.closeMediaLightbox();
                window.closeAictechIntroModal();
            }
        });

        // ==========================================
        // NAVEGACIÓN INTERACTIVA DEL CATÁLOGO POR MARCA
        // ==========================================
        $(document).on('click', '#emerson-nested-toggle', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const nestedMenu = document.getElementById('emerson-nested-menu');
            const chevron = document.getElementById('emerson-chevron');
            if (nestedMenu) {
                nestedMenu.classList.toggle('show');
            }
            if (chevron) {
                chevron.classList.toggle('rotate-180');
            }
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

    html = html.replace(old_script_block, new_script_block)
    print("6. Script tags separated and updated with full interactive JS.")
else:
    print("Warning: Could not find <script src='js/sidebar-collapse.js'>...</script> block.")

# Write back to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully! Final length:", len(html))
