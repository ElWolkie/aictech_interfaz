import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if not m:
    raise Exception("Style tag not found!")

css = m.group(1)

# Fix relative image paths from css/ directory
# url('img/... -> url('../img/...
css = re.sub(r"url\((['\"]?)img/", r"url(\1../img/", css)

# Moderate excessive blur filters on backdrop-filter to prevent 60fps GPU frame drops on scroll
css = re.sub(r'backdrop-filter:\s*blur\(20px\)\s*saturate\(190%\)', 'backdrop-filter: blur(8px) saturate(140%)', css)
css = re.sub(r'-webkit-backdrop-filter:\s*blur\(20px\)\s*saturate\(190%\)', '-webkit-backdrop-filter: blur(8px) saturate(140%)', css)
css = re.sub(r'backdrop-filter:\s*blur\(16px\)\s*saturate\(180%\)', 'backdrop-filter: blur(8px) saturate(130%)', css)
css = re.sub(r'-webkit-backdrop-filter:\s*blur\(16px\)\s*saturate\(180%\)', '-webkit-backdrop-filter: blur(8px) saturate(130%)', css)

# Add performance optimizations at the end of custom CSS
perf_css = """

/* ==========================================================================
   PERFORMANCE ACCELERATION RULES (GPU & RENDERING OPTIMIZATIONS)
   ========================================================================== */
.roxar-showcase-container {
    content-visibility: auto;
    contain-intrinsic-size: 850px;
}

.service-video-wrap {
    box-shadow: 0 8px 25px rgba(0, 150, 255, 0.15);
    border-radius: 8px;
    overflow: hidden;
}

/* Reducción de coste GPU para cometas de fondo */
#global-comets-bg {
    pointer-events: none;
    opacity: 0.5;
}

.bg-comet {
    transform: translateZ(0);
}
"""

full_css = css + perf_css

with open('css/custom-styles.css', 'w', encoding='utf-8') as f:
    f.write(full_css)

print(f"Extracted css/custom-styles.css successfully! Length: {len(full_css)} characters.")

