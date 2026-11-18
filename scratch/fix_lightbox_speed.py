with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

# 1. Remove duplicate expandCardMedia block between line 2478 and line 2636
# It starts around '// LIGHTBOX EXPAND PARA VIDEOS Y FOTOS HD' and ends before '<!-- MODAL DE VIDEO ECHOMETER'
dup_pattern = r'// ==========================================\s*// LIGHTBOX EXPAND PARA VIDEOS Y FOTOS HD \(AISLADO PARA MÁXIMA FLUIDEZ\)\s*window\.expandCardMedia = function\(target\) {.*?}\s*;\s*}\);\s*// end DOMContentLoaded'
m = re.search(dup_pattern, text, re.DOTALL)
if m:
    text = text[:m.start()] + text[m.end():]
    print("Removed duplicate expandCardMedia block 1 successfully!")
else:
    print("Could not find duplicate expandCardMedia block by exact regex, searching substring...")
    pos1 = text.find('window.loadShowroomVideo = loadShowroomVideo;')
    pos2 = text.find('<!-- MODAL DE VIDEO ECHOMETER PANTALLA COMPLETA -->')
    if pos1 != -1 and pos2 != -1:
        sub = text[pos1:pos2]
        if 'window.expandCardMedia' in sub:
            # find where expandCardMedia starts
            start_exp = sub.find('// LIGHTBOX EXPAND')
            if start_exp != -1:
                end_script = sub.rfind('</script>')
                text = text[:pos1 + start_exp] + text[pos1 + end_script:]
                print("Removed duplicate block by slice successfully!")

# 2. Update the main expandCardMedia and closeMediaLightbox implementation
lightbox_logic = """
        // ==========================================
        // LIGHTBOX EXPAND ULTRA-OPTIMIZADO (REPRODUCCIÓN FLUIDA 60 FPS)
        // ==========================================
        window.isMediaLightboxOpen = false;

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
                    title = titleNode.innerText.replace(/[\\r\\n]+/g, ' ').trim();
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
"""

# Replace the second expandCardMedia block
main_exp_pattern = r'// ==========================================\s*// LIGHTBOX EXPAND PARA VIDEOS Y FOTOS HD.*?window\.closeMediaLightbox = function\(.*?};'
m2 = re.search(main_exp_pattern, text, re.DOTALL)
if m2:
    text = text[:m2.start()] + lightbox_logic.strip() + text[m2.end():]
    print("Replaced main expandCardMedia logic successfully!")
else:
    print("Could not find main expandCardMedia by regex")

# 3. Ensure initSmartVideoObserver checks window.isMediaLightboxOpen
text = text.replace("if (entry.isIntersecting && isPage2 && !document.hidden) {", "if (entry.isIntersecting && isPage2 && !document.hidden && !window.isMediaLightboxOpen) {")
text = text.replace("if (!page2 || !page2.classList.contains('selected')) return;", "if (!page2 || !page2.classList.contains('selected') || window.isMediaLightboxOpen) return;")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("index.html updated successfully!")

# 4. Remove the rule hiding controls in css/custom-styles.css
with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

css = re.sub(r'/\* Ocultar barra de controles en el modal lightbox \*/.*?#media-lightbox-stage video::-webkit-media-controls-panel\s*{[^}]*}', '/* Controles nativos habilitados para máxima fluidez */', css, flags=re.DOTALL)
with open('css/custom-styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("css/custom-styles.css updated successfully!")

