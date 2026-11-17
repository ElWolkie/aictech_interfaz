# -*- coding: utf-8 -*-
"""
Applies all requested fixes to index.html:
1. Replaces Section 5 with generated_section5_v3.html (expanded photos, clean 2-column showcase for single products, centered odds, no bugs).
2. Removes carousel from card-multifasico-campo in Section 2 (removes 'Video en Campo' & 'Toldo y Tráiler' pills, arrows, second slide).
3. Fixes broken orphaned globe script block that was causing ReferenceError and killing JS execution.
4. Fixes fluidNavigateTo to scroll #page-content-wrapper.
5. Fixes sidebar navigation for #productos-submenu and #servicios-submenu.
6. Fixes service video click-to-expand in fullscreen.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Section 5
pos_li5 = content.find('<li data-page-no="5"')
pos_li6 = content.find('<li data-page-no="6"')
assert pos_li5 != -1 and pos_li6 != -1, "Could not find li 5 or 6"

with open('scratch/generated_section5_v3.html', 'r', encoding='utf-8') as f:
    new_sec5 = f.read()

content = content[:pos_li5] + new_sec5 + '\n\n                ' + content[pos_li6:]

# 2. Remove carousel in card-multifasico-campo
# Find card-multifasico-campo
pos_card = content.find('id="card-multifasico-campo"')
assert pos_card != -1, "Could not find card-multifasico-campo"

# Look for <div class="card-slider-wrap"> and ending </div> of card-slider-wrap
pos_slider_wrap = content.find('<div class="card-slider-wrap">', pos_card)
pos_slider_end = content.find('</div>\n                                                    </div>\n                                                    <div class="service-flip-back">', pos_card)
if pos_slider_end == -1:
    pos_slider_end = content.find('<div class="service-flip-back">', pos_card)
    # find the </div> before it
    pos_front_end = content.rfind('</div>', pos_card, pos_slider_end)
    pos_slider_end = content.rfind('</div>', pos_card, pos_front_end)

# Let's inspect the exact substring in card-multifasico-campo
pos_front_start = content.find('<div class="service-flip-front">', pos_card)
pos_back_start = content.find('<div class="service-flip-back">', pos_card)
assert pos_front_start != -1 and pos_back_start != -1, "Could not find front/back bounds in multifasico"

clean_multifasico_front = '''<div class="service-flip-front">
                                                        <div class="service-video-wrap">
                                                            <button type="button" class="service-media-expand-btn" title="Agrandar pantalla completa" onclick="event.stopPropagation(); expandCardMedia(this);"><i class="fas fa-expand"></i></button>
                                                            <video autoplay loop muted playsinline webkit-playsinline disablePictureInPicture preload="auto" class="roxar-card-video" id="video-multifasico-campo">
                                                                <source src="video/multifasico-campo.mp4" type="video/mp4">
                                                            </video>
                                                            <div class="service-front-overlay">
                                                                <div class="service-front-title">
                                                                    <i class="fas fa-satellite-dish text-info"></i> WELL TESTING CON MEDIDOR MULTIFÁSICO ROXAR
                                                                </div>
                                                                <span class="service-flip-hint-badge"><i class="fas fa-rotate me-1"></i> Ver Detalles</span>
                                                            </div>
                                                        </div>
                                                    </div>'''

content = content[:pos_front_start] + clean_multifasico_front + '\n                                                    ' + content[pos_back_start:]

# 3. Clean up the broken orphaned globe code in Script 4
pos_orphaned_start = content.find('function onPointerUp() {')
if pos_orphaned_start != -1:
    pos_orphaned_end = content.find('</script>', pos_orphaned_start)
    assert pos_orphaned_end != -1, "Could not find script close after orphaned code"
    # Replace the orphaned code with clean closing
    content = content[:pos_orphaned_start] + '\n' + content[pos_orphaned_end:]

# 4. Update the bottom script with robust navigation and click-to-expand
pos_last_script = content.rfind('<script>')
assert pos_last_script != -1, "Could not find last script tag"

clean_bottom_script = '''<script>
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
            if (e) {
                e.preventDefault();
                e.stopPropagation();
            }

            document.querySelectorAll('video').forEach(function(v) {
                if (v.id !== 'aictech-intro-video' && !v.paused) {
                    v.dataset.wasPlaying = 'true';
                    v.pause();
                }
            });

            const modal = document.getElementById('aictech-intro-modal');
            const video = document.getElementById('aictech-intro-video');
            if (!modal || !video) return;

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            video.onclick = function(ev) {
                ev.stopPropagation();
                if (video.paused) video.play();
                else video.pause();
            };

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
        };

        window.closeAictechIntroModal = function() {
            const modal = document.getElementById('aictech-intro-modal');
            const video = document.getElementById('aictech-intro-video');
            if (video) {
                video.pause();
                video.currentTime = 0;
            }
            if (modal) modal.classList.remove('active');
            document.body.style.overflow = '';

            document.querySelectorAll('video').forEach(function(v) {
                if (v.dataset.wasPlaying === 'true') {
                    delete v.dataset.wasPlaying;
                    v.play().catch(function() {});
                }
            });
        };

        // ==========================================
        // EXPANDIR VIDEO / FOTO A PANTALLA COMPLETA (60FPS LIGHTBOX)
        // ==========================================
        window.expandCardMedia = function(target) {
            if (!target) return;
            const card = target.closest('.service-flip-card') || target.closest('.featured-large-product-card') || target.closest('.compact-product-card') || target.closest('.service-video-wrap') || target;
            if (!card) return;

            const stage = document.getElementById('media-lightbox-stage');
            const titleElem = document.getElementById('media-lightbox-title');
            const modal = document.getElementById('media-lightbox-modal');
            if (!stage || !modal) return;

            window.pauseAllBackgroundVideos();
            stage.innerHTML = '';

            let title = '';
            const titleNode = card.querySelector('.service-front-title, .service-tech-title, .brand-card-title, .service-video-tag, h3, h4, h5, h6');
            if (titleNode) {
                title = titleNode.innerText.replace(/[\\r\\n]+/g, ' ').trim();
            }

            const activeSlide = card.querySelector('.card-slide-item.active');
            const scope = activeSlide || card;

            const img = scope.querySelector('img.card-slide-img, img.compact-product-img, img.featured-hero-img, img');
            const video = scope.querySelector('video:not(.roxar-video-ambient-blur)') || scope.querySelector('video');

            if (activeSlide && activeSlide.getAttribute('data-type') === 'image' && img) {
                const newImg = document.createElement('img');
                newImg.src = img.src;
                newImg.alt = title || 'Visualización en alta resolución';
                newImg.style.maxHeight = '85vh';
                newImg.style.maxWidth = '90vw';
                newImg.style.objectFit = 'contain';
                newImg.style.borderRadius = '12px';
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
                newVid.style.maxHeight = '85vh';
                newVid.style.objectFit = 'contain';
                newVid.style.borderRadius = '12px';
                newVid.style.cursor = 'pointer';
                newVid.title = 'Haga clic para pausar / reanudar';

                newVid.addEventListener('click', function(ev) {
                    ev.stopPropagation();
                    if (newVid.paused) newVid.play();
                    else newVid.pause();
                });

                const src = video.currentSrc || (video.querySelector('source') ? video.querySelector('source').src : video.src);
                newVid.src = src;
                stage.appendChild(newVid);

                requestAnimationFrame(() => {
                    newVid.play().catch(function() {
                        newVid.muted = true;
                        newVid.play().catch(function() {});
                    });
                });
            } else if (img) {
                const newImg = document.createElement('img');
                newImg.src = img.src;
                newImg.alt = title || 'Visualización en alta resolución';
                newImg.style.maxHeight = '85vh';
                newImg.style.maxWidth = '90vw';
                newImg.style.objectFit = 'contain';
                newImg.style.borderRadius = '12px';
                stage.appendChild(newImg);
            }

            if (titleElem) {
                titleElem.innerText = title || 'Visualización Técnica HD';
            }

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        };

        window.expandMediaFromElement = function(elem) {
            window.expandCardMedia(elem);
        };

        window.closeMediaLightbox = function() {
            const modal = document.getElementById('media-lightbox-modal');
            const stage = document.getElementById('media-lightbox-stage');
            if (stage) {
                const v = stage.querySelector('video');
                if (v) {
                    v.pause();
                    v.src = '';
                }
                stage.innerHTML = '';
            }

            if (modal) modal.classList.remove('active');
            document.body.style.overflow = '';
        };

        // ==========================================
        // NAVEGACIÓN FLUIDA EN SIDEBAR (#page-content-wrapper)
        // ==========================================
        window.fluidNavigateTo = function(targetId) {
            if (!targetId) return;
            const el = document.getElementById(targetId);
            if (!el) return;

            const wrapper = document.getElementById('page-content-wrapper');
            if (wrapper) {
                const elRect = el.getBoundingClientRect();
                const wrapperRect = wrapper.getBoundingClientRect();
                const scrollPos = wrapper.scrollTop + (elRect.top - wrapperRect.top) - 15;
                wrapper.scrollTo({
                    top: Math.max(0, scrollPos),
                    behavior: 'smooth'
                });
            } else {
                el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }

            el.classList.remove('target-service-highlight');
            void el.offsetWidth;
            el.classList.add('target-service-highlight');
            setTimeout(() => {
                el.classList.remove('target-service-highlight');
            }, 1800);
        };

        // Toggle del Acordeón EMERSON
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

        // Navegación desde el submenú de Productos (Roxar, Flexim, AMS Trex, Rosemount, Micro Motion, Fluenta, Kam)
        $(document).on('click', '#productos-submenu a.submenu-link, .sidebar-nested-submenu a.submenu-link', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const targetId = $(this).data('target') || $(this).attr('data-target') || ($(this).attr('href') ? $(this).attr('href').replace('#', '') : '');
            if (!targetId) return;

            openPage(5);
            highlightMenu(5);

            $('#productos-submenu a.submenu-link, .sidebar-nested-submenu a.submenu-link').removeClass('active');
            $(this).addClass('active');

            setTimeout(function() {
                window.fluidNavigateTo(targetId);
            }, 100);
        });

        // Navegación desde el submenú de Servicios (01 Multifásico, 02 Separadores, etc.)
        $(document).on('click', '#servicios-submenu a.submenu-link', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const href = $(this).attr('href');
            const targetId = $(this).data('target') || $(this).attr('data-target') || (href ? href.replace('#', '') : '');
            if (!targetId) return;

            openPage(2);
            highlightMenu(2);

            $('#servicios-submenu a.submenu-link').removeClass('active');
            $(this).addClass('active');

            setTimeout(function() {
                window.fluidNavigateTo(targetId);
            }, 100);
        });

        // CLIC EN VIDEO DE SERVICIOS: Expansión inmediata a Lightbox HD en 1 clic
        $(document).on('click', '.service-flip-front, .service-video-wrap', function(e) {
            // Si el clic fue en el botón de ver detalles al dorso, voltear la tarjeta y no abrir modal
            if ($(e.target).closest('.service-flip-hint-badge, .service-flip-btn-back, a, button:not(.service-media-expand-btn)').length > 0) {
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
    </script>'''

content = content[:pos_last_script] + clean_bottom_script + '\n\n' + content[content.find('<!-- MODAL INTRO CINEMÁTICO', pos_last_script):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied all fixes final successfully! Size:", len(content))
