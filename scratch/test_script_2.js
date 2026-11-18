
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

            const speedBar = document.getElementById('media-lightbox-speed-bar');
            if (video && speedBar) {
                speedBar.style.display = 'flex';
                speedBar.querySelectorAll('.speed-btn').forEach((b, idx) => {
                    if (idx === 0) b.classList.add('active');
                    else b.classList.remove('active');
                });
            } else if (speedBar) {
                speedBar.style.display = 'none';
            }
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
        // LIGHTBOX EXPAND ULTRA-OPTIMIZADO (REPRODUCCIÓN FLUIDA 60 FPS)
        // ==========================================
        window.isMediaLightboxOpen = false;

        
        window.setLightboxPlaybackRate = function(rate, btn) {
            const stage = document.getElementById('media-lightbox-stage');
            if (!stage) return;
            const v = stage.querySelector('video');
            if (v) {
                v.playbackRate = rate;
            }
            if (btn) {
                const bar = document.getElementById('media-lightbox-speed-bar');
                if (bar) {
                    bar.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active', 'btn-info', 'btn-warning'));
                    btn.classList.add('active');
                }
            }
        };

        window.expandCardMedia = function(target) {
            if (!target) return;

            window.isMediaLightboxOpen = true;

            // 1. Congelar inmediatamente el 100% de los videos en segundo plano
            document.querySelectorAll('video').forEach(function(v) {
                if (!v.paused) {
                    v.dataset.wasPlaying = 'true';
                    v.pause();
                }
            });

            const stage = document.getElementById('media-lightbox-stage');
            const titleElem = document.getElementById('media-lightbox-title');
            const modal = document.getElementById('media-lightbox-modal');
            if (!stage || !modal) return;

            stage.innerHTML = '';

            // 2. Encontrar el contenedor lógico
            const card = target.closest('.service-flip-card') 
                || target.closest('.featured-large-product-card') 
                || target.closest('.compact-product-card') 
                || target.closest('.center-split-card-wrapper') 
                || target.closest('.center-split-interior') 
                || target.closest('.service-video-wrap') 
                || target.closest('.row') 
                || target;

            let img = null;
            let video = null;

            const activeSlide = card ? card.querySelector('.card-slide-item.active') : null;
            if (activeSlide) {
                if (activeSlide.getAttribute('data-type') === 'image') {
                    img = activeSlide.querySelector('img');
                } else {
                    video = activeSlide.querySelector('video');
                }
            }

            if (!img && !video) {
                if (target.tagName === 'IMG') img = target;
                else if (target.tagName === 'VIDEO') video = target;
            }

            if (!img && !video && target.querySelector) {
                img = target.querySelector('img.featured-hero-img, img.compact-product-img, .center-split-interior img, img');
            }

            if (!img && !video && card) {
                video = card.querySelector('video');
            }

            if (!video && !img && card) {
                img = card.querySelector('img.card-slide-img, img.roxar-card-img, img.compact-product-img, img.featured-hero-img, img');
            }

            // Título técnico
            let title = '';
            if (img && img.getAttribute('alt') && img.getAttribute('alt').trim().length > 3) {
                title = img.getAttribute('alt').trim();
            }
            if (!title && card) {
                const titleNode = card.querySelector('.service-tech-title, .brand-card-title, .service-video-tag, .card-slide-caption, .service-front-title, .compact-title-bar div, h3, h4, h5, h6');
                if (titleNode) {
                    title = titleNode.innerText.replace(/[\r\n]+/g, ' ').trim();
                }
            }
            if (!title) {
                const tAttr = target.getAttribute('title') || (card && card.getAttribute('title'));
                if (tAttr && !tAttr.toLowerCase().includes('haga clic') && !tAttr.toLowerCase().includes('agrandar')) {
                    title = tAttr.trim();
                }
            }

            // Inyectar reproductor optimizado
            if (video) {
                try { video.pause(); } catch(e) {}
                const src = video.currentSrc || (video.querySelector('source') ? video.querySelector('source').src : video.src);

                const newVid = document.createElement('video');
                newVid.controls = true;
                newVid.autoplay = true;
                newVid.loop = true;
                newVid.playsInline = true;
                newVid.preload = 'auto';
                newVid.style.width = '100%';
                newVid.style.maxHeight = '75vh';
                newVid.style.objectFit = 'contain';
                newVid.style.borderRadius = '8px';
                newVid.style.background = '#000';
                newVid.src = src;

                stage.appendChild(newVid);

                const p = newVid.play();
                if (p !== undefined) {
                    p.catch(function() {
                        newVid.muted = true;
                        newVid.play().catch(function() {});
                    });
                }
            } else if (img) {
                const newImg = document.createElement('img');
                newImg.src = img.currentSrc || img.src;
                newImg.alt = title || 'Visualización en alta resolución';
                newImg.style.maxHeight = '78vh';
                newImg.style.maxWidth = '88vw';
                newImg.style.objectFit = 'contain';
                newImg.style.borderRadius = '8px';
                newImg.style.display = 'block';
                newImg.style.margin = '0 auto';
                newImg.style.background = '#ffffff';
                newImg.style.padding = '16px';
                newImg.style.boxShadow = '0 10px 40px rgba(0,0,0,0.6)';
                stage.appendChild(newImg);
            }

            if (titleElem) {
                titleElem.innerText = title || 'Visualización Técnica HD';
            }

            const speedBar = document.getElementById('media-lightbox-speed-bar');
            if (video && speedBar) {
                speedBar.style.display = 'flex';
                speedBar.querySelectorAll('.speed-btn').forEach((b, idx) => {
                    if (idx === 0) b.classList.add('active');
                    else b.classList.remove('active');
                });
            } else if (speedBar) {
                speedBar.style.display = 'none';
            }
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        };

        window.expandMediaFromElement = function(elem) {
            window.expandCardMedia(elem);
        };

        window.closeMediaLightbox = function() {
            window.isMediaLightboxOpen = false;
            const modal = document.getElementById('media-lightbox-modal');
            const stage = document.getElementById('media-lightbox-stage');
            if (stage) {
                const v = stage.querySelector('video');
                if (v) {
                    try {
                        v.pause();
                        v.removeAttribute('src');
                        v.load();
                    } catch(e) {}
                }
                stage.innerHTML = '';
            }

            if (modal) modal.classList.remove('active');
            document.body.style.overflow = '';

            // Restaurar videos visibles de forma ligera
            if (typeof updateVisibleServiceVideos === 'function') {
                setTimeout(updateVisibleServiceVideos, 150);
            }
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
    