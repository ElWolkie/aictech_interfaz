
    function openModal(id) {
        document.getElementById(id).classList.add('active');
    }

    function closeModal(id) {
        document.getElementById(id).classList.remove('active');
    }

    function scrollToService(serviceId) {
        if (typeof openPage === 'function') {
            openPage(2);
        }
        if (typeof highlightMenu === 'function') {
            highlightMenu(2);
        }
        setTimeout(() => {
            const el = document.getElementById(serviceId);
            if (el) {
                el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            if (typeof checkRevealElements === 'function') {
                checkRevealElements();
            }
        }, 250);
    }

    // =========================================================================
    // GESTOR INTELIGENTE DE REPRODUCCIÓN (MÁXIMO 3 VIDEOS ACTIVOS EN PANTALLA)
    // =========================================================================
    let activeSectionObserver = null;

    function handlePageVideoPlayback(pageNo) {
        const heroVideo = document.getElementById('hero-main-video');
        const allServiceVideos = document.querySelectorAll('.roxar-showcase-container video, video.service-video-elem, video.roxar-card-video');

        if (pageNo == 1) {
            // PANTALLA INICIAL: solo video de portada
            if (heroVideo) {
                heroVideo.muted = true;
                heroVideo.playsInline = true;
                heroVideo.play().catch(e => {});
            }
            allServiceVideos.forEach(v => {
                if (!v.paused) v.pause();
            });
        } else if (pageNo == 2) {
            // SERVICIOS: pausar video de inicio y activar solo la sección visible actual
            if (heroVideo && !heroVideo.paused) heroVideo.pause();
            if (!activeSectionObserver) {
                initSmartVideoObserver();
            } else {
                updateVisibleServiceVideos();
            }
        } else {
            // OTRAS PANTALLAS: pausar todos los videos para máximo ahorro
            if (heroVideo && !heroVideo.paused) heroVideo.pause();
            allServiceVideos.forEach(v => {
                if (!v.paused) v.pause();
            });
        }
    }

    // Inicializar IntersectionObserver para controlar exactamente 1 sección (máx 3 videos)
    function initSmartVideoObserver() {
        const scrollContainer = document.getElementById('page-content-wrapper') || null;
        const sections = document.querySelectorAll('.roxar-showcase-container');
        if (!sections.length) return;

        activeSectionObserver = new IntersectionObserver((entries) => {
            const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
            const isPage2 = page2 && page2.classList.contains('selected');

            entries.forEach(entry => {
                const section = entry.target;
                const vids = section.querySelectorAll('video');

                if (entry.isIntersecting && isPage2 && !document.hidden && !window.isMediaLightboxOpen) {
                    // Esta sección está activa: reproducir solo sus videos (máx 3 en simultáneo)
                    vids.forEach(v => {
                        v.muted = true;
                        v.playsInline = true;
                        if (v.paused) {
                            const p = v.play();
                            if (p !== undefined) p.catch(() => {});
                        }
                    });
                } else {
                    // Salió de la vista: pausar de inmediato para liberar GPU y decodificadores
                    vids.forEach(v => {
                        if (!v.paused) v.pause();
                    });
                }
            });
        }, {
            root: scrollContainer,
            threshold: 0.15 // Se activa al mostrarse al menos 15% de la sección
        });

        sections.forEach(sec => activeSectionObserver.observe(sec));
    }

    function updateVisibleServiceVideos() {
        const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
        if (!page2 || !page2.classList.contains('selected') || window.isMediaLightboxOpen) return;

        const container = document.getElementById('page-content-wrapper');
        const containerRect = container ? container.getBoundingClientRect() : { top: 0, bottom: window.innerHeight };

        document.querySelectorAll('.roxar-showcase-container').forEach(section => {
            const rect = section.getBoundingClientRect();
            const isVisible = rect.top < containerRect.bottom - 60 && rect.bottom > containerRect.top + 60;
            const vids = section.querySelectorAll('video');
            if (isVisible) {
                vids.forEach(v => {
                    v.muted = true;
                    v.playsInline = true;
                    if (v.paused) v.play().catch(() => {});
                });
            } else {
                vids.forEach(v => {
                    if (!v.paused) v.pause();
                });
            }
        });
    }

    function syncServiceVideosOnPage() {
        updateVisibleServiceVideos();
    }

    function syncCardVideosOnPage() {
        // Manejado automáticamente por el observador de sección
    }

    function onScrollOptimized() {
        // Con IntersectionObserver el scroll es nativo y sin sobrecarga
    }

    function checkRevealElements() {
        const reveals = document.querySelectorAll('.reveal-on-scroll:not(.is-revealed)');
        reveals.forEach(el => el.classList.add('is-revealed'));
    }

    document.addEventListener('DOMContentLoaded', () => {
        initSmartVideoObserver();
        checkRevealElements();
    
    
        // Enlazar scroll a contenedor y ventana con opciones pasivas
        const pageWrapper = document.getElementById('page-content-wrapper');
        if (pageWrapper) {
            pageWrapper.addEventListener('scroll', onScrollOptimized, { passive: true });
        }
        window.addEventListener('scroll', onScrollOptimized, { passive: true });

        checkRevealElements();

        // CONTROLADOR DE CLIC EN 2 PASOS PARA TARJETAS DE SERVICIOS (Ahorro de recursos y UX interactiva)
        // 1er Clic: Inicia la reproducción del video manteniéndose al frente
        // 2do Clic: Gira la tarjeta a la cara posterior (especificaciones)
        // Clic en el reverso: Vuelve a girar al frente
        // FUNCIONES DE CONTROL PARA EL CARRUSEL DE LA TARJETA (MULTIFÁSICO)
        window.setCardSlide = function(elem, targetIndex) {
            const wrap = elem.closest('.card-slider-wrap');
            if (!wrap) return;
            const card = elem.closest('.service-flip-card');
            const slides = wrap.querySelectorAll('.card-slide-item');
            const pills = wrap.querySelectorAll('.card-slider-pill');
            
            // Pausar cualquier otra tarjeta activa para optimizar recursos de GPU y CPU
            if (card) {
                document.querySelectorAll('.service-flip-card.is-video-playing').forEach(otherCard => {
                    if (otherCard !== card) {
                        otherCard.classList.remove('is-video-playing');
                        const otherVid = otherCard.querySelector('video.roxar-card-video-foreground, video.roxar-card-video');
                        const otherBlur = otherCard.querySelector('video.roxar-video-ambient-blur');
                        if (otherVid && !otherVid.paused) otherVid.pause();
                        if (otherBlur && !otherBlur.paused) otherBlur.pause();
                    }
                });
            }

            slides.forEach((s, idx) => {
                const v = s.querySelector('video');
                if (idx === targetIndex) {
                    s.classList.add('active');
                    if (v) {
                        v.muted = true;
                        v.playsInline = true;
                        // Iniciar video inmediatamente al seleccionar slide (1 solo clic)
                        const playPromise = v.play();
                        if (playPromise !== undefined) {
                            playPromise.then(() => {
                                if (card) card.classList.add('is-video-playing');
                            }).catch(err => {
                                console.log('Carousel slide video autoplay handled:', err);
                            });
                        }
                    } else {
                        // Diapositiva de imagen estática
                        if (card) card.classList.remove('is-video-playing');
                    }
                } else {
                    s.classList.remove('active');
                    if (v && !v.paused) v.pause();
                }
            });

            pills.forEach((p, idx) => {
                if (idx === targetIndex) {
                    p.classList.add('active');
                } else {
                    p.classList.remove('active');
                }
            });
        };

        window.changeCardSlide = function(btn, direction) {
            const wrap = btn.closest('.card-slider-wrap');
            if (!wrap) return;
            const slides = wrap.querySelectorAll('.card-slide-item');
            let currentIndex = 0;
            slides.forEach((s, idx) => {
                if (s.classList.contains('active')) currentIndex = idx;
            });

            let newIndex = currentIndex + direction;
            if (newIndex < 0) newIndex = slides.length - 1;
            if (newIndex >= slides.length) newIndex = 0;

            const pill = wrap.querySelectorAll('.card-slider-pill')[newIndex];
            if (pill) {
                setCardSlide(pill, newIndex);
            }
        };

        
        // =========================================================================
        // PANTALLA COMPLETA ROBUSTA (CON FALLBACK PSEUDO-FULLSCREEN PARA IFRAMES/WEBVIEWS)
        // =========================================================================
        function toggleFullScreen() {
            try {
                const doc = window.document;
                const docEl = doc.documentElement;

                const isNativeFull = !!(doc.fullscreenElement || doc.webkitFullscreenElement || doc.mozFullScreenElement || doc.msFullscreenElement);
                const isPseudoFull = document.body.classList.contains('is-pseudo-fullscreen') || docEl.classList.contains('is-pseudo-fullscreen');

                if (isNativeFull) {
                    const exit = doc.exitFullscreen || doc.webkitExitFullscreen || doc.mozCancelFullScreen || doc.msExitFullscreen;
                    if (exit) {
                        const p = exit.call(doc);
                        if (p && p.catch) p.catch(() => {});
                    }
                    updateFullscreenButtonState(false);
                } else if (isPseudoFull) {
                    document.body.classList.remove('is-pseudo-fullscreen');
                    docEl.classList.remove('is-pseudo-fullscreen');
                    updateFullscreenButtonState(false);
                } else {
                    const req = docEl.requestFullscreen || docEl.webkitRequestFullscreen || docEl.mozRequestFullScreen || docEl.msRequestFullscreen;
                    let requestedNative = false;

                    if (req && (doc.fullscreenEnabled !== false && doc.webkitFullscreenEnabled !== false)) {
                        try {
                            const p = req.call(docEl);
                            if (p && p.then) {
                                p.then(() => {
                                    updateFullscreenButtonState(true);
                                }).catch(() => {
                                    // Si el navegador deniega el permiso nativo (ej. iframe sin permisos), activar modo pseudo-pantalla completa
                                    enablePseudoFullscreen();
                                });
                                requestedNative = true;
                            } else {
                                updateFullscreenButtonState(true);
                                requestedNative = true;
                            }
                        } catch (err) {
                            requestedNative = false;
                        }
                    }

                    if (!requestedNative) {
                        enablePseudoFullscreen();
                    }
                }
            } catch (e) {
                console.warn('Error alternando pantalla completa:', e);
                enablePseudoFullscreen();
            }
        }

        function enablePseudoFullscreen() {
            document.body.classList.add('is-pseudo-fullscreen');
            document.documentElement.classList.add('is-pseudo-fullscreen');
            updateFullscreenButtonState(true);
        }

        function updateFullscreenButtonState(forceState) {
            const btn = document.getElementById('btn-fullscreen-toggle');
            if (!btn) return;
            const isFull = (typeof forceState === 'boolean')
                ? forceState
                : !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement || document.body.classList.contains('is-pseudo-fullscreen'));

            if (isFull) {
                btn.innerHTML = '<i class="fas fa-compress me-1 text-warning"></i> <span>Salir Pantalla Completa</span>';
                btn.classList.add('is-active');
                btn.setAttribute('title', 'Salir de Pantalla Completa (Esc)');
            } else {
                btn.innerHTML = '<i class="fas fa-expand me-1 text-info"></i> <span>Pantalla Completa</span>';
                btn.classList.remove('is-active');
                btn.setAttribute('title', 'Pantalla Completa');
            }
        }

        window.toggleFullScreen = toggleFullScreen;

        document.addEventListener('fullscreenchange', () => updateFullscreenButtonState());
        document.addEventListener('webkitfullscreenchange', () => updateFullscreenButtonState());
        document.addEventListener('mozfullscreenchange', () => updateFullscreenButtonState());
        document.addEventListener('MSFullscreenChange', () => updateFullscreenButtonState());

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                if (document.body.classList.contains('is-pseudo-fullscreen')) {
                    toggleFullScreen();
                }
                const showroomModal = document.getElementById('video-modal-slb');
                if (showroomModal && showroomModal.classList.contains('active')) {
                    closeShowroomModal();
                }
            }
        });

        // Asegurar que el botón ejecute la función aunque se use addEventListener
        document.addEventListener('DOMContentLoaded', function() {
            const fsBtn = document.getElementById('btn-fullscreen-toggle');
            if (fsBtn) {
                fsBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    toggleFullScreen();
                });
            }

            const slbBtn = document.getElementById('open-slb-video-btn');
            if (slbBtn) {
                slbBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    openShowroomModal();
                });
            }
        });

        // =========================================================================
        // CONTROLADOR SHOWROOM TECNOLÓGICO / VIDEOTECA TÉCNICA EMERSON & AIC TECH
        // =========================================================================
        const showroomPlaylist = [
            {
                id: "presentacion_oficial",
                title: "Video de Presentación Corporativa AIC TECH, C.A.",
                subtitle: "Alta Ingeniería, Automatización & Telemetría en Tiempo Real",
                desc: "Recorrido integral por las capacidades tecnológicas, infraestructura en Anaco, instrumentación Emerson y servicios especializados de campo de AIC TECH para la industria petrolera.",
                category: "PRESENTACIÓN CORPORATIVA",
                badge: "AIC TECH OFICIAL",
                icon: "fa-film",
                src: "video/biblioteca/presentacion-2.mp4"
            },
            {
                id: "emerson_goboldly",
                title: "Emerson - Go Boldly: Innovación Tecnológica Global",
                subtitle: "Liderazgo Mundial en Automatización Industrial y Sostenibilidad",
                desc: "Visión global de automatización de vanguardia para transformar la industria energética hacia operaciones más inteligentes, seguras y eficientes.",
                category: "VISIÓN CORPORATIVA",
                badge: "GO BOLDLY",
                icon: "fa-globe",
                src: "video/biblioteca/emerson-go-boldly-innovacion.mp4"
            },
            {
                id: "xwell",
                title: "Tecnología Rosemount™ X-well: Medición No Intrusiva de Temperatura",
                subtitle: "Medición Precisa en Superficie de Tubería sin Termopozos",
                desc: "Algoritmo termodinámico avanzado que calcula la temperatura interna del proceso a través de la pared de la tubería, eliminando riesgos de fugas y paradas operacionales.",
                category: "TEMPERATURA & PROCESO",
                badge: "X-WELL™",
                icon: "fa-temperature-half",
                src: "video/biblioteca/rosemount-xwell-temperatura.mp4"
            },
            {
                id: "gas928",
                title: "Monitor Inalámbrico de Gas Tóxico Rosemount™ 928 Wireless",
                subtitle: "Detección Continua de H₂S y Gases Peligrosos en Cabezal de Pozo",
                desc: "Transmisor de gas inalámbrico WirelessHART® con sensor electroquímico intercambiable 'inteligente' para monitoreo temprano de sulfuro de hidrógeno sin cables.",
                category: "SEGURIDAD INDUSTRIAL",
                badge: "928 WIRELESS",
                icon: "fa-shield-halved",
                src: "video/biblioteca/rosemount-928-monitor-gas-inalambrico.mp4"
            },
            {
                id: "fuego_calidad",
                title: "Detección de Fuego y Gas Rosemount™: Estándares de Alta Calidad",
                subtitle: "Detectores Ópticos de Llama UV/IR y Sensores de Gas Certificados SIL",
                desc: "Ingeniería de máxima confiabilidad para protección perimetral en refinerías, plantas compresoras y patios de tanques bajo severas condiciones climáticas.",
                category: "FUEGO Y GAS (F&G)",
                badge: "ALTA CALIDAD",
                icon: "fa-fire-burner",
                src: "video/biblioteca/rosemount-fuego-gas-calidad.mp4"
            },
            {
                id: "fuego_disponibilidad",
                title: "Detección de Fuego y Gas Rosemount™: Disponibilidad Inmediata",
                subtitle: "Suministro Rápido y Despliegue en Instalaciones Críticas",
                desc: "Disponibilidad estratégica de sensores de llama y gas listos para montaje, garantizando reemplazo inmediato y continuidad operativa en campo.",
                category: "DISPONIBILIDAD INMEDIATA",
                badge: "SUMINISTRO",
                icon: "fa-truck-fast",
                src: "video/biblioteca/rosemount-fuego-gas-disponibilidad.mp4"
            },
            {
                id: "fuego_soporte",
                title: "Detección de Fuego y Gas Rosemount™: Soporte al Cliente Superior",
                subtitle: "Asistencia de Expertos en Sistemas Instrumentados de Seguridad",
                desc: "Respaldo técnico de ingeniería, comisionamiento y calibración certificada por especialistas de AIC TECH y Emerson para protección de activos 24/7.",
                category: "SOPORTE TÉCNICO",
                badge: "SOPORTE 24/7",
                icon: "fa-headset",
                src: "video/biblioteca/rosemount-fuego-gas-soporte.mp4"
            },
            {
                id: "ph_pureza",
                title: "Medición Analítica de pH en Agua de Alta Pureza",
                subtitle: "Soluciones de Sensores Rosemount para Aguas de Alimentación y Calderas",
                desc: "Superación de fluctuaciones de lectura e interferencias en aguas de conductividad ultra baja para optimizar la eficiencia térmica y prevenir incrustaciones.",
                category: "MEDICIÓN ANALÍTICA",
                badge: "ANALYTICAL",
                icon: "fa-droplet",
                src: "video/biblioteca/medicion-ph-agua-alta-pureza.mp4"
            },
            {
                id: "presion_gas",
                title: "Lecturas de Presión Estables en Compresión de Gas Combustible",
                subtitle: "Transmisores Rosemount Coplanar™ Inmunes a Pulsaciones y Vibración",
                desc: "Estabilidad inalterable de medición de presión en compresores reciprocantes y turbocompresores para máxima confiabilidad en inyección y transporte.",
                category: "TRANSMISIÓN DE PRESIÓN",
                badge: "ROSEMOUNT 3051",
                icon: "fa-gauge-high",
                src: "video/biblioteca/lectura-presion-compresion-gas.mp4"
            },
            {
                id: "vibracion",
                title: "Innovación en Monitoreo Inalámbrico de Vibración",
                subtitle: "Sensores Rosemount Wireless de Vibración para Mantenimiento Predictivo",
                desc: "Detección temprana de fallas en rodamientos, desalineación y desbalance en bombas y motores sin cables, reduciendo paradas no programadas.",
                category: "CONFIABILIDAD PREDICTIVA",
                badge: "VIBRACIÓN",
                icon: "fa-wave-square",
                src: "video/biblioteca/innovacion-vibracion-inalambrica.mp4"
            }
        ];

        let currentShowroomIndex = 0;

        function renderShowroomPlaylist() {
            const container = document.getElementById('showroom-playlist-container');
            if (!container) return;
            
            container.innerHTML = '';
            showroomPlaylist.forEach((item, index) => {
                const card = document.createElement('div');
                card.className = `showroom-thumb-card ${index === currentShowroomIndex ? 'active' : ''}`;
                card.setAttribute('data-index', index);
                card.onclick = function() { loadShowroomVideo(index, true); };

                card.innerHTML = `
                    <div class="showroom-thumb-box">
                        <i class="fas ${item.icon}"></i>
                        <span class="thumb-badge">${index + 1}</span>
                    </div>
                    <div class="showroom-card-meta">
                        <div class="showroom-card-cat">${item.category}</div>
                        <div class="showroom-card-title">${item.title}</div>
                    </div>
                `;
                container.appendChild(card);
            });

            const totalEl = document.getElementById('showroom-total-count');
            if (totalEl) totalEl.innerText = `${showroomPlaylist.length} Videos`;
        }

        function loadShowroomVideo(index, autoplay = true) {
            if (index < 0) index = showroomPlaylist.length - 1;
            if (index >= showroomPlaylist.length) index = 0;
            currentShowroomIndex = index;

            const videoData = showroomPlaylist[index];
            const mainVideo = document.getElementById('showroom-main-video');
            
            // Actualizar textos
            const titleEl = document.getElementById('showroom-curr-title');
            const subEl = document.getElementById('showroom-curr-subtitle');
            const descEl = document.getElementById('showroom-curr-desc');
            const tagEl = document.getElementById('showroom-curr-tag');
            const counterEl = document.getElementById('showroom-counter-badge');

            if (titleEl) titleEl.innerText = videoData.title;
            if (subEl) subEl.innerText = videoData.subtitle;
            if (descEl) descEl.innerText = videoData.desc;
            if (tagEl) tagEl.innerText = videoData.category;
            if (counterEl) counterEl.innerHTML = `<i class="fas fa-play-circle me-1"></i> Video ${index + 1} de ${showroomPlaylist.length}`;

            // Resaltar en la lista
            document.querySelectorAll('.showroom-thumb-card').forEach((card, idx) => {
                if (idx === index) {
                    card.classList.add('active');
                    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                } else {
                    card.classList.remove('active');
                }
            });

            // Cargar video
            if (mainVideo) {
                mainVideo.pause();
                mainVideo.src = videoData.src;
                mainVideo.load();
                if (autoplay) {
                    mainVideo.play().catch(e => {
                        console.log('Autoplay interactivo:', e);
                    });
                }
            }
        }

        function showroomNextVideo() {
            loadShowroomVideo(currentShowroomIndex + 1, true);
        }

        function showroomPrevVideo() {
            loadShowroomVideo(currentShowroomIndex - 1, true);
        }

        function openShowroomModal() {
            const modal = document.getElementById('video-modal-slb');
            const heroVideo = document.getElementById('hero-main-video');

            // Pausar video de fondo inicial
            if (heroVideo) {
                try { heroVideo.pause(); } catch(e) {}
            }

            if (modal) {
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
                renderShowroomPlaylist();
                loadShowroomVideo(currentShowroomIndex, true);
            }
        }

        function closeShowroomModal() {
            const modal = document.getElementById('video-modal-slb');
            const mainVideo = document.getElementById('showroom-main-video');
            const heroVideo = document.getElementById('hero-main-video');

            if (modal) {
                modal.classList.remove('active');
                if (mainVideo) {
                    mainVideo.pause();
                }
            }

            // Reanudar video de fondo si seguimos en la página 1
            const page1 = document.querySelector('.cd-hero-slider > li[data-page-no="1"]');
            if (page1 && page1.classList.contains('selected') && heroVideo) {
                heroVideo.play().catch(e => console.log(e));
            }
        }

        window.openShowroomModal = openShowroomModal;
        window.closeShowroomModal = closeShowroomModal;
        window.openSlbVideoModal = openShowroomModal;
        window.closeSlbVideoModal = closeShowroomModal;
        window.showroomNextVideo = showroomNextVideo;
        window.showroomPrevVideo = showroomPrevVideo;
        window.loadShowroomVideo = loadShowroomVideo;
        window.renderShowroomPlaylist = renderShowroomPlaylist;
    }); // end DOMContentLoaded
