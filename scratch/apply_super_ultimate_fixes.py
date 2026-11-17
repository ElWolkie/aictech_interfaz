# -*- coding: utf-8 -*-
"""
apply_super_ultimate_fixes.py
Applies all 5 requested updates:
1. Remove subtitle text under AICTECH logo in sidebar header
2. Fix AIC TECH intro video: remove controls, smooth entrance animation, then play cleanly
3. Drastically optimize video expansion to solid 60FPS with zero lag
4. Section 5: New layout (Foto 1: 1 large on left + compact pegaditos on right, Foto 2: red clutter removed)
   and Flip 360 double gatefold envelope for single products (Foto 3 + user code)
5. Sidenav (Foto 4): Watermark brand logos behind each product strip in sidebar
   (Emerson with emerson.png, AMS Trex with emerson.png in gray, and other brands with their logos)
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# =========================================================================
# 1. REMOVE SUBTITLE TEXT UNDER AICTECH LOGO IN SIDEBAR
# =========================================================================
html = re.sub(
    r'<div class="sidebar-subtitle">\s*INNOVACIÓN EN MEDICIÓN &amp; DIAGNÓSTICO\s*</div>',
    '',
    html
)
print("1. Removed subtitle text under AICTECH logo in sidebar.")

# =========================================================================
# 2. FIX AICTECH INTRO VIDEO: REMOVE CONTROLS, SMOOTH ANIMATION, CLEAN PLAY
# =========================================================================
html = re.sub(
    r'<video id="aictech-intro-video"[^>]*>',
    '<video id="aictech-intro-video" playsinline preload="auto" style="width: 100%; max-height: 80vh; display: block; object-fit: contain !important; cursor: pointer;" title="Haga clic para pausar / reanudar">',
    html
)

# Update openAictechIntroModal JS
old_aic_js = r'window\.openAictechIntroModal = function\(e\) \{[\s\S]*?video\.play\(\);[\s\S]*?\};'
new_aic_js = """window.openAictechIntroModal = function(e) {
            if (e) {
                e.preventDefault();
                e.stopPropagation();
            }

            // Pausar solo videos visibles que se estén reproduciendo
            document.querySelectorAll('video').forEach(function(v) {
                if (v.id !== 'aictech-intro-video' && !v.paused) {
                    v.dataset.wasPlaying = 'true';
                    v.pause();
                }
            });

            const modal = document.getElementById('aictech-intro-modal');
            const video = document.getElementById('aictech-intro-video');
            if (!modal || !video) return;

            // Abrir modal con animación fluida a 60fps
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            // Click en video para pausar / reproducir sin barras de herramientas
            video.onclick = function(ev) {
                ev.stopPropagation();
                if (video.paused) video.play();
                else video.pause();
            };

            // Iniciar video tras completar la animación de entrada (160ms) para cero lag
            setTimeout(function() {
                video.currentTime = 0;
                video.muted = false;
                const p = video.play();
                if (p !== undefined) {
                    p.catch(function() {
                        video.muted = true;
                        video.play().catch(function() {});
                    });
                }
            }, 160);
        };"""

html = re.sub(old_aic_js, new_aic_js, html, count=1)
print("2. AIC TECH intro video updated (no controls, 60fps entrance, clean play).")

# =========================================================================
# 3. DRASTICALLY OPTIMIZE VIDEO EXPANSION PERFORMANCE (SOLID 60FPS)
# =========================================================================
# Optimize expandCardMedia
old_expand_fn = r'window\.expandCardMedia = function\(btn\) \{[\s\S]*?newVid\.play\(\)\.catch[\s\S]*?\};\s*\}'
new_expand_fn = """window.expandCardMedia = function(btn) {
            // Pausar solo videos activos en segundo plano para destinar el 100% de GPU al video expandido
            const activeVids = document.querySelectorAll('video:not(#media-lightbox-stage video)');
            for (let i = 0; i < activeVids.length; i++) {
                if (!activeVids[i].paused) {
                    activeVids[i].dataset.wasPlaying = 'true';
                    activeVids[i].pause();
                }
            }

            const card = btn.closest('.service-flip-card') || btn.closest('.featured-large-product-card') || btn.closest('.compact-product-card') || btn.closest('.service-video-wrap') || btn;
            if (!card) return;

            const stage = document.getElementById('media-lightbox-stage');
            const titleElem = document.getElementById('media-lightbox-title');
            const modal = document.getElementById('media-lightbox-modal');
            if (!stage || !modal) return;

            stage.innerHTML = '';

            let title = '';
            const titleNode = card.querySelector('.service-tech-title, .brand-card-title, .service-video-tag, .card-slide-caption, .service-front-title, h4, h5, h6');
            if (titleNode) {
                title = titleNode.innerText.replace(/[\\n\\r]+/g, ' ').trim();
            }

            const activeSlide = card.querySelector('.card-slide-item.active');
            const scope = activeSlide || card;

            const img = scope.querySelector('img.card-slide-img, img.roxar-card-img, img.compact-product-img, img.featured-hero-img, img');
            const fgVideo = scope.querySelector('video.roxar-card-video-foreground');
            const video = fgVideo || scope.querySelector('video:not(.roxar-video-ambient-blur)') || scope.querySelector('video');

            if (activeSlide && activeSlide.getAttribute('data-type') === 'image' && img) {
                const newImg = document.createElement('img');
                newImg.src = img.src;
                newImg.alt = title || 'Visualización en alta resolución';
                stage.appendChild(newImg);
            } else if (video) {
                const newVid = document.createElement('video');
                newVid.controls = false;
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
                newVid.title = 'Haga clic para pausar / reanudar';

                newVid.addEventListener('click', function(e) {
                    e.stopPropagation();
                    if (newVid.paused) newVid.play();
                    else newVid.pause();
                });

                const src = video.currentSrc || (video.querySelector('source') ? video.querySelector('source').src : video.src);
                newVid.src = src;
                stage.appendChild(newVid);

                // Iniciar reproducción suave a 60fps con requestAnimationFrame
                requestAnimationFrame(() => {
                    newVid.play().catch(function() {
                        newVid.muted = true;
                        newVid.play().catch(function() {});
                    });
                });
            }

            if (titleElem) {
                titleElem.innerText = title || 'Visualización Técnica HD';
            }

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }"""

html = re.sub(old_expand_fn, new_expand_fn, html, count=1)
print("3. Lightbox video expansion optimized for solid 60FPS.")

# =========================================================================
# 4. REPLACE SECTION 5 WITH NEW FORMAT (1 LARGE + COMPACTS & FLIP 360)
# =========================================================================
with open('scratch/generated_section5_final.html', 'r', encoding='utf-8') as f:
    sec5_final_html = f.read()

p5_match = re.search(r'<li[^>]*data-page-no=[\'"]5[\'"]', html)
if not p5_match:
    raise ValueError("Could not find <li data-page-no=5 in index.html")
p5_start = p5_match.start()

p6_match = re.search(r'<li[^>]*data-page-no=[\'"]6[\'"]', html[p5_start:])
if not p6_match:
    raise ValueError("Could not find <li data-page-no=6 in index.html")
p6_start = p5_start + p6_match.start()

html = html[:p5_start] + sec5_final_html + "\n                " + html[p6_start:]
print("4. Section 5 replaced with new layout (Foto 1: 1 large + compacts, Foto 3: Flip 360 envelope).")

# =========================================================================
# 5. CSS: FLIP 360 ENVELOPE, COMPACT CARDS & WATERMARK BRAND LOGOS IN SIDENAV
# =========================================================================
new_custom_css = """
        /* ============================================================= */
        /* CSS - CARDS - FLIP 360 DOUBLE GATEFOLD ENVELOPE (FOTO 3)     */
        /* ============================================================= */
        .flip-360-wrapper {
            display: inline-block;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5), 0 0 25px rgba(56, 182, 255, 0.2);
            position: relative;
            cursor: pointer;
            user-select: none;
            border-radius: 14px;
            perspective: 1200px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .flip-360-wrapper:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.65), 0 0 35px rgba(56, 182, 255, 0.4);
        }

        .flip-360-container {
            display: inline-block;
            perspective: 1200px;
            vertical-align: top;
            width: 180px;
            height: 250px;
        }

        @media (min-width: 576px) {
            .flip-360-container {
                width: 215px;
                height: 290px;
            }
        }

        /* Giro de 180 grados al pasar el cursor o en hover táctil */
        .flip-360-wrapper:hover .flip-left,
        .flip-360-wrapper:active .flip-left,
        .flip-360-wrapper.is-open .flip-left {
            transform: rotateY(-180deg);
        }

        .flip-360-wrapper:hover .flip-right,
        .flip-360-wrapper:active .flip-right,
        .flip-360-wrapper.is-open .flip-right {
            transform: rotateY(180deg);
        }

        .flip-pane {
            transition: transform 0.65s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            position: relative;
            width: 100%;
            height: 100%;
        }

        .flip-pane .front,
        .flip-pane .back {
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .flip-pane .front {
            z-index: 2;
            transform: rotateY(0deg);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.35);
        }

        .flip-pane .front-left {
            border-radius: 14px 0 0 14px;
            border-right: 1px solid rgba(255, 255, 255, 0.25);
        }

        .flip-pane .front-right {
            border-radius: 0 14px 14px 0;
            border-left: 1px solid rgba(0, 0, 0, 0.25);
        }

        .front-left .circle {
            position: absolute;
            right: -50px;
            top: 50%;
            margin-top: -50px;
        }

        .front-right .circle {
            position: absolute;
            left: -50px;
            top: 50%;
            margin-top: -50px;
        }

        .circle {
            position: absolute;
            width: 100px;
            height: 100px;
            border-radius: 100%;
            background: #ffffff;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 5px 15px rgba(0, 0, 0, 0.25);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .flip-pane .back {
            background: #090e1a;
            transform: rotateY(180deg);
            overflow: hidden;
        }

        .flip-pane .back-left {
            border-radius: 14px 0 0 14px;
        }

        .flip-pane .back-right {
            border-radius: 0 14px 14px 0;
        }

        .flip-pane .back img {
            width: 360px;
            height: 250px;
            object-fit: contain;
            background: #0f172a;
        }

        @media (min-width: 576px) {
            .flip-pane .back img {
                width: 430px;
                height: 290px;
            }
        }

        .back-left img {
            position: absolute;
            left: 0;
            top: 0;
        }

        .back-right img {
            position: absolute;
            right: 0;
            top: 0;
        }

        /* ============================================================= */
        /* COMPACT CARDS & FEATURED LARGE (ESTILO FOTO 1)                */
        /* ============================================================= */
        .compact-product-card:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.6) !important;
            border-color: rgba(56, 182, 255, 0.6) !important;
        }
        .compact-product-card:hover .compact-product-img {
            transform: scale(1.1);
        }

        .featured-large-product-card:hover {
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7) !important;
            border-color: rgba(56, 182, 255, 0.7) !important;
        }
        .featured-large-product-card:hover .featured-hero-img {
            transform: scale(1.04);
        }

        /* ============================================================= */
        /* WATERMARK BRAND LOGOS EN EL SIDENAV (FOTO 4)                  */
        /* ============================================================= */
        .submenu-nested-header,
        .sidebar-nested-submenu .submenu-link,
        #productos-submenu > a.submenu-link {
            position: relative !important;
            overflow: hidden !important;
        }

        #emerson-nested-toggle::before {
            content: '';
            position: absolute;
            right: 30px;
            top: 50%;
            transform: translateY(-50%);
            width: 75px;
            height: 70%;
            background: url('img/products/emerson.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
            filter: brightness(1.2);
        }
        #emerson-nested-toggle:hover::before {
            opacity: 0.70;
            transform: translateY(-50%) scale(1.08);
        }

        .sidebar-brand-strip-roxar::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 68px;
            height: 65%;
            background: url('img/products/roxar/roxar.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .sidebar-brand-strip-flexim::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 65px;
            height: 65%;
            background: url('img/products/flexim/Flexim-Logo.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .sidebar-brand-strip-amstrex::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 70px;
            height: 65%;
            background: url('img/products/emerson.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
            filter: grayscale(1) brightness(1.4);
        }

        .sidebar-brand-strip-rosemount::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 68px;
            height: 65%;
            background: url('img/products/rosemount/Rosemount-New-Logo.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .sidebar-brand-strip-micromotion::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 72px;
            height: 65%;
            background: url('img/products/micromotion/micromotion.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .sidebar-brand-strip-fluenta::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 65px;
            height: 65%;
            background: url('img/products/fluenta/Fluenta-blog-logo.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .sidebar-brand-strip-kam::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            width: 60px;
            height: 65%;
            background: url('img/products/kam/kam_logo.png') right center / contain no-repeat;
            opacity: 0.35;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .submenu-link:hover::before {
            opacity: 0.70;
            transform: translateY(-50%) scale(1.08);
        }
"""

style_end = html.find('</style>')
if style_end != -1:
    html = html[:style_end] + new_custom_css + "\n    " + html[style_end:]
    print("5. Added custom CSS for Flip 360 Envelope, Compact cards and Sidenav Watermarks.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated! Final length:", len(html))
