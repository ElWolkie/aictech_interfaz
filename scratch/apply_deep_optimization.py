import re
import os

print("=== STEP 1: OPTIMIZING INDEX.HTML ===")

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Remove #global-comets-bg entirely
comets_pattern = r'<!-- FONDO GLOBAL DE COMETAS Y ESTRELLAS PERMANENTES -->\s*<div id="global-comets-bg">.*?</div>\s*</div>'
html = re.sub(comets_pattern, '', html, flags=re.DOTALL)
html = re.sub(r'<div id="global-comets-bg">.*?</div>\s*</div>', '', html, flags=re.DOTALL)

# 2. Remove #oil-minigame-overlay entirely
minigame_pattern = r'<!-- OVERLAY MINIJUEGO DEL PETRÓLEO AICTECH -->\s*<div id="oil-minigame-overlay">.*?</div>\s*</div>'
html = re.sub(minigame_pattern, '', html, flags=re.DOTALL)
html = re.sub(r'<div id="oil-minigame-overlay">.*?</div>\s*</div>', '', html, flags=re.DOTALL)

# 3. Add poster="..." to all <video> tags based on their source
video_posters = {
    'presentacion-1.mp4': 'img/posters/presentacion-1.jpg',
    'roxar2600.mp4': 'img/posters/roxar2600.jpg',
    'multifasico-campo.mp4': 'img/posters/multifasico-campo.jpg',
    'gemelo_digital_video.mp4': 'img/posters/gemelo_digital_video.jpg',
    'separador-1.mp4': 'img/posters/separador-1.jpg',
    'bifasico.mp4': 'img/posters/bifasico.jpg',
    'trifasico-2.mp4': 'img/posters/trifasico-2.jpg',
    'flexim.mp4': 'img/posters/flexim.jpg',
    'flexim-2.mp4': 'img/posters/flexim-2.jpg',
    'echometer.mp4': 'img/posters/echometer.jpg',
    'echometer-1.mp4': 'img/posters/echometer-1.jpg',
    'echometer-2.mp4': 'img/posters/echometer-2.jpg',
    'tanque.mp4': 'img/posters/tanque.jpg',
    'trasegado-1.mp4': 'img/posters/trasegado-1.jpg',
    'tanque-1.mp4': 'img/posters/tanque-1.jpg',
    'soldadura-1.mp4': 'img/posters/soldadura-1.jpg',
    'soldadura.mp4': 'img/posters/soldadura.jpg',
    'taller-1.mp4': 'img/posters/taller-1.jpg',
    'aictech.mp4': 'img/posters/aictech.jpg',
    'calibracion-1.mp4': 'img/posters/calibracion-1.jpg',
    'mantenimiento-1.mp4': 'img/posters/mantenimiento-1.jpg',
    'presentacion-2.mp4': 'img/posters/presentacion-2.jpg',
    'inicio-aic.mp4': 'img/posters/inicio-aic.jpg',
}

# Find all <video ...> ... <source src="video/xyz.mp4"> ... </video> blocks
def add_poster_to_video(match):
    vblock = match.group(0)
    for mp4, poster in video_posters.items():
        if mp4 in vblock:
            # Check if poster already present
            if 'poster=' not in vblock:
                vblock = vblock.replace('<video ', f'<video poster="{poster}" ')
            break
    return vblock

html = re.sub(r'<video[^>]*>.*?</video>', add_poster_to_video, html, flags=re.DOTALL)

# 4. Clean up the JavaScript video manager to STOP aggressive scroll decoding
# In JS, handlePageVideoPlayback and scroll handlers:
new_clean_js = """// =========================================================================
    // CONTROLADOR DE VIDEOS ULTRA-LIVIANO (CERO LAG, MÁXIMA FLUIDEZ)
    // =========================================================================
    function handlePageVideoPlayback(pageNo) {
        const heroVideo = document.getElementById('hero-main-video');
        const allVideos = document.querySelectorAll('video');

        if (pageNo == 1) {
            // PANTALLA INICIAL: reproducir video de portada y pausar todos los demás
            if (heroVideo) {
                heroVideo.muted = true;
                heroVideo.playsInline = true;
                heroVideo.play().catch(e => {});
            }
            allVideos.forEach(v => {
                if (v !== heroVideo && !v.paused) v.pause();
            });
        } else {
            // OTRAS PANTALLAS: pausar video hero y todos los videos pesados
            allVideos.forEach(v => {
                if (!v.paused) v.pause();
            });
        }
    }

    // Funciones de sincronización mantenidas para compatibilidad pero ultralivianas
    function syncServiceVideosOnPage() {
        // No forzar decodificación en scroll: los posters brindan imagen nítida instantánea
    }

    function syncCardVideosOnPage() {
        // No forzar decodificación en scroll
    }

    function onScrollOptimized() {
        // Scroll 100% libre de sobrecarga
    }

    function checkRevealElements() {
        // Revelado progresivo rápido sin bloquear hilo principal
        const reveals = document.querySelectorAll('.reveal-on-scroll:not(.is-revealed)');
        reveals.forEach(el => el.classList.add('is-revealed'));
    }

    document.addEventListener('DOMContentLoaded', () => {
        checkRevealElements();
    """

js_block_pattern = r'// =========================================================================\s*// CONTROLADOR ULTRA-EFICIENTE DE VIDEOS Y SCROLL.*?(document\.addEventListener\(\'DOMContentLoaded\', \(\) => {)'
html = re.sub(js_block_pattern, new_clean_js, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Index.html updated successfully!")

print("\n=== STEP 2: OPTIMIZING CSS/CUSTOM-STYLES.CSS ===")

with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# 1. Remove background-attachment: fixed on body
css = re.sub(r'background-attachment:\s*fixed;', '/* background-attachment: fixed removed for 60fps scroll */', css)

# 2. Clean up body background to simple smooth color / non-fixed gradient
css = re.sub(r'background:\s*radial-gradient\(ellipse at 50% 25%, #0c204c 0%, #050d21 65%, #020610 100%\)\s*!important;', 'background: #030814 !important;', css)

# 3. Strip all real-time filters on videos
css = re.sub(r'filter:\s*brightness\(1\.06\)\s*contrast\(1\.05\)\s*saturate\(1\.08\);', '/* filter removed for direct GPU overlay */', css)
css = re.sub(r'filter:\s*brightness\(1\.05\)\s*contrast\(1\.08\);', '/* filter removed */', css)
css = re.sub(r'filter:\s*brightness\(1\.02\)\s*contrast\(1\.08\);', '/* filter removed */', css)
css = re.sub(r'filter:\s*drop-shadow\(0 8px 24px rgba\(0, 0, 0, 0\.7\)\);', '/* filter removed */', css)

# 4. Remove all backdrop-filter: blur(...) from cards and site components
css = re.sub(r'backdrop-filter:\s*blur\([^)]+\)[^;]*;', '/* backdrop-filter removed */', css)
css = re.sub(r'-webkit-backdrop-filter:\s*blur\([^)]+\)[^;]*;', '/* -webkit-backdrop-filter removed */', css)

# 5. Remove infinite comets and shooting stars CSS
css = re.sub(r'#global-comets-bg\s*{[^}]*}', '#global-comets-bg { display: none !important; }', css)
css = re.sub(r'\.shooting-star\s*{[^}]*}', '.shooting-star { display: none !important; }', css)
css = re.sub(r'\.bg-comet\s*{[^}]*}', '.bg-comet { display: none !important; }', css)
css = re.sub(r'\.stars\s*{[^}]*}', '.stars { display: none !important; }', css)

# 6. Simplify cards: remove heavy perspective / preserve-3d if causing GPU lag
css = re.sub(r'transform-style:\s*preserve-3d;', '/* transform-style */', css)

# 7. Add GPU acceleration and smooth scrolling enhancements
css += """

/* ==========================================================================
   TURBO SMOOTH SCROLL & GPU ACCELERATION
   ========================================================================== */
#page-content-wrapper {
    -webkit-overflow-scrolling: touch;
    scroll-behavior: smooth;
    will-change: scroll-position;
}

video {
    image-rendering: auto;
}

.service-flip-card {
    contain: layout style paint;
}
"""

with open('css/custom-styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("css/custom-styles.css updated successfully!")

