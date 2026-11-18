import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

orig_size = len(content)

# 1. Replace the inline <style>...</style> block with <link rel="stylesheet" href="css/custom-styles.css">
style_pattern = r'<!-- CSS PALETA CORTADA: MITAD AZUL / MITAD BLANCO INDUSTRIAL OPTIMIZADOS -->\s*<style>.*?</style>'
link_tag = '<!-- CSS Custom Modular y Optimizado (159KB cacheados) -->\n    <link rel="stylesheet" href="css/custom-styles.css">'

if re.search(style_pattern, content, re.DOTALL):
    content = re.sub(style_pattern, link_tag, content, count=1, flags=re.DOTALL)
else:
    content = re.sub(r'<style>.*?</style>', link_tag, content, count=1, flags=re.DOTALL)

# 2. Remove duplicate ambient blur videos
# e.g. <video ... class="roxar-card-video roxar-video-ambient-blur" ...> ... </video>
ambient_blur_pattern = r'<!-- Ambient video blur de fondo -->\s*<video[^>]*class="[^"]*roxar-video-ambient-blur[^"]*"[^>]*>.*?</video>'
content = re.sub(ambient_blur_pattern, '', content, flags=re.DOTALL)
# Any remaining ambient blur tags
content = re.sub(r'<video[^>]*class="[^"]*roxar-video-ambient-blur[^"]*"[^>]*>.*?</video>', '', content, flags=re.DOTALL)

# 3. Optimize video tags: remove autoplay from service videos, set preload="none"
def fix_video_tag(m):
    tag = m.group(0)
    if 'id="hero-main-video"' in tag or "id='hero-main-video'" in tag:
        tag = re.sub(r'preload="[^"]*"', 'preload="metadata"', tag)
        if 'preload=' not in tag:
            tag = tag.replace('<video ', '<video preload="metadata" ')
        return tag
    
    # Remove autoplay
    tag = re.sub(r'\bautoplay\b', '', tag)
    # Set preload="none"
    if 'preload=' in tag:
        tag = re.sub(r'preload="[^"]*"', 'preload="none"', tag)
    else:
        tag = tag.replace('<video ', '<video preload="none" ')
    
    # Normalize spaces
    tag = re.sub(r'\s+', ' ', tag)
    tag = tag.replace('<video ', '<video ')
    return tag

content = re.sub(r'<video[^>]*>', fix_video_tag, content)

# 4. Remove ghost / dead DOM elements:
# tech-particles-canvas
content = re.sub(r'<!-- Canvas de Fondo Interactivo[^>]*-->\s*<canvas id="tech-particles-canvas"></canvas>', '', content)
content = re.sub(r'<canvas id="tech-particles-canvas"></canvas>', '', content)

# globe-intro-overlay
content = re.sub(r'<!-- OVERLAY ANIMACIÓN DE ENTRADA: GLOBO 3D AICTECH -->\s*<div id="globe-intro-overlay"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="globe-intro-overlay" class="hidden">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# warp-5d-overlay
content = re.sub(r'<!-- OVERLAY DE SALTO HIPERESPACIAL 5D -->\s*<div id="warp-5d-overlay"></div>', '', content)
content = re.sub(r'<div id="warp-5d-overlay"></div>', '', content)

# 5. Add loading="lazy" decoding="async" to images (except top logo in sidebar/navbar)
def fix_img_tag(m):
    tag = m.group(0)
    if 'aictech_logo.png' in tag or 'navbar-brand' in tag or 'sidebar-heading' in tag:
        return tag
    if 'loading=' not in tag:
        tag = tag.replace('<img ', '<img loading="lazy" decoding="async" ')
    return tag

content = re.sub(r'<img[^>]*>', fix_img_tag, content)

# 6. Replace the video controller JS block
old_js_start = '// =========================================================================\n    // CONTROLADOR ULTRA-OPTIMIZADO DE VIDEOS EN SERVICIOS (ANTI-LAG RIGUROSO)'
old_js_end = '// CONTROLADOR DE CLIC EN 2 PASOS PARA TARJETAS DE SERVICIOS'

new_js = """// =========================================================================
    // CONTROLADOR ULTRA-EFICIENTE DE VIDEOS Y SCROLL (ANTI-LAG RIGUROSO)
    // =========================================================================
    let isVideoSyncScheduled = false;

    // Pausar o reproducir videos de acuerdo a la página activa
    function handlePageVideoPlayback(pageNo) {
        const heroVideo = document.getElementById('hero-main-video');
        const serviceVideos = document.querySelectorAll('video.service-video-elem, video.roxar-card-video');

        if (pageNo == 1) {
            // PANTALLA INICIAL: reproducir video de inicio y pausar todos los demás
            if (heroVideo) {
                heroVideo.muted = true;
                heroVideo.playsInline = true;
                heroVideo.play().catch(e => {});
            }
            serviceVideos.forEach(v => {
                if (!v.paused) v.pause();
            });
        } else {
            // OTRAS PANTALLAS: pausar video de portada
            if (heroVideo && !heroVideo.paused) {
                heroVideo.pause();
            }

            if (pageNo == 2) {
                // SERVICIOS: reproducir video del banner en pantalla y sincronizar
                const firstBanner = document.getElementById('roxar-main-video');
                if (firstBanner) {
                    firstBanner.muted = true;
                    firstBanner.playsInline = true;
                    firstBanner.play().catch(e => {});
                }
                syncServiceVideosOnPage();
                syncCardVideosOnPage();
            } else {
                // OTRAS PANTALLAS (3, 4, 5, 6): pausar absolutamente todos los videos
                serviceVideos.forEach(v => {
                    if (!v.paused) v.pause();
                });
            }
        }
    }

    // Sincronizar videos de banners de servicios: MÁXIMO 1 VIDEO DE BANNER ACTIVO
    function syncServiceVideosOnPage() {
        const page2 = document.querySelector('.cd-hero-slider > li[data-page-no="2"]');
        if (!page2 || !page2.classList.contains('selected') || document.hidden) {
            document.querySelectorAll('video.service-video-elem').forEach(v => {
                if (!v.paused) v.pause();
            });
            return;
        }

        const scrollWrapper = document.getElementById('page-content-wrapper');
        const containerRect = scrollWrapper 
            ? scrollWrapper.getBoundingClientRect() 
            : { top: 0, bottom: window.innerHeight, height: window.innerHeight };

        const serviceArticles = document.querySelectorAll('.roxar-showcase-container');
        let activeVideo = null;
        let maxVisiblePixels = 0;

        serviceArticles.forEach(article => {
            const banner = article.querySelector('.roxar-hero-banner');
            const video = article.querySelector('video.service-video-elem');
            if (!video || !banner) return;

            const rect = banner.getBoundingClientRect();
            const visibleTop = Math.max(containerRect.top, rect.top);
            const visibleBottom = Math.min(containerRect.bottom, rect.bottom);
            const visiblePixels = Math.max(0, visibleBottom - visibleTop);

            if (visiblePixels >= 80) {
                const bannerCenter = (rect.top + rect.bottom) / 2;
                const containerCenter = (containerRect.top + containerRect.bottom) / 2;
                const score = visiblePixels - Math.abs(bannerCenter - containerCenter) * 0.25;

                if (score > maxVisiblePixels) {
                    maxVisiblePixels = score;
                    activeVideo = video;
                }
            }
        });

        document.querySelectorAll('video.service-video-elem').forEach(video => {
            if (video === activeVideo && !document.hidden) {
                if (video.paused) {
                    video.muted = true;
                    video.playsInline = true;
                    video.play().catch(e => {});
                }
            } else {
                if (!video.paused) {
                    video.pause();
                }
            }
        });
    }

    // Control de rendimiento de tarjetas: Pausar videos que salen de pantalla para máximo ahorro de GPU/CPU
    function syncCardVideosOnPage() {
        const activeSlide = document.querySelector('.cd-hero-slider > li.selected');
        const isServiceOrProduct = activeSlide && (activeSlide.getAttribute('data-page-no') === '2' || activeSlide.getAttribute('data-page-no') === '5');
        const cardVideos = document.querySelectorAll('.roxar-card-video');
        if (!isServiceOrProduct || document.hidden) {
            cardVideos.forEach(v => {
                if (!v.paused) v.pause();
            });
            document.querySelectorAll('.service-flip-card.is-video-playing').forEach(c => {
                c.classList.remove('is-video-playing');
                const b = c.querySelector('.service-flip-hint-badge');
                if (b) b.innerHTML = '<i class="fas fa-rotate me-1"></i> Ver Detalles';
            });
            return;
        }

        const scrollWrapper = document.getElementById('page-content-wrapper');
        const containerRect = scrollWrapper 
            ? scrollWrapper.getBoundingClientRect() 
            : { top: 0, bottom: window.innerHeight };

        document.querySelectorAll('.service-flip-card.is-video-playing').forEach(card => {
            const rect = card.getBoundingClientRect();
            const isVisible = rect.top < containerRect.bottom && rect.bottom > containerRect.top;
            if (!isVisible) {
                card.classList.remove('is-video-playing');
                const vid = card.querySelector('video.roxar-card-video');
                if (vid && !vid.paused) vid.pause();
                const badge = card.querySelector('.service-flip-hint-badge');
                if (badge) badge.innerHTML = '<i class="fas fa-rotate me-1"></i> Ver Detalles';
            }
        });
    }

    // Handler de scroll de alto rendimiento acoplado a rAF
    function onScrollOptimized() {
        if (!isVideoSyncScheduled) {
            isVideoSyncScheduled = true;
            requestAnimationFrame(() => {
                syncServiceVideosOnPage();
                syncCardVideosOnPage();
                checkRevealElements();
                isVideoSyncScheduled = false;
            });
        }
    }

    // Efecto de revelado progresivo optimizado
    function checkRevealElements() {
        const reveals = document.querySelectorAll('.reveal-on-scroll:not(.is-revealed)');
        if (!reveals.length) return;
        const windowHeight = window.innerHeight;
        reveals.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top <= windowHeight - 30 && rect.bottom >= 0) {
                el.classList.add('is-revealed');
            }
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        // Enlazar scroll a contenedor y ventana con opciones pasivas
        const pageWrapper = document.getElementById('page-content-wrapper');
        if (pageWrapper) {
            pageWrapper.addEventListener('scroll', onScrollOptimized, { passive: true });
        }
        window.addEventListener('scroll', onScrollOptimized, { passive: true });

        checkRevealElements();

        """

# Replace the JS section
js_pattern = re.escape(old_js_start) + r'.*?' + re.escape(old_js_end)
if re.search(js_pattern, content, re.DOTALL):
    content = re.sub(js_pattern, new_js + old_js_end, content, count=1, flags=re.DOTALL)
    print("Replaced video controller JS successfully!")
else:
    print("WARNING: Could not find exact JS block via regex. Searching partial...")
    idx1 = content.find('// CONTROLADOR ULTRA-OPTIMIZADO DE VIDEOS EN SERVICIOS')
    idx2 = content.find('// CONTROLADOR DE CLIC EN 2 PASOS PARA TARJETAS DE SERVICIOS')
    if idx1 != -1 and idx2 != -1:
        content = content[:idx1] + new_js + content[idx2:]
        print("Replaced via index substring successfully!")
    else:
        print(f"Error finding indices: idx1={idx1}, idx2={idx2}")

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Original size: {orig_size/1024:.1f} KB")
print(f"Optimized size: {len(content)/1024:.1f} KB")
print(f"Reduction: {(orig_size - len(content))/1024:.1f} KB ({((orig_size - len(content))/orig_size)*100:.1f}%)")

