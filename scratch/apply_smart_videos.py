with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

new_smart_js = """// =========================================================================
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

                if (entry.isIntersecting && isPage2 && !document.hidden) {
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
        if (!page2 || !page2.classList.contains('selected')) return;

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
    """

# Replace the controller block in index.html
old_marker = "// =========================================================================\n    // CONTROLADOR DE VIDEOS ULTRA-LIVIANO"
end_marker = "document.addEventListener('DOMContentLoaded', () => {\n        checkRevealElements();"

idx1 = text.find(old_marker)
idx2 = text.find(end_marker)
if idx1 != -1 and idx2 != -1:
    text = text[:idx1] + new_smart_js + text[idx2 + len(end_marker):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Applied Smart 3-Video Active Window controller successfully!")
else:
    print(f"Indices not found: idx1={idx1}, idx2={idx2}")

