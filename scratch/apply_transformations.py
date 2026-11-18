import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

orig_len = len(content)

# 1. Replace the inline <style>...</style> block with <link rel="stylesheet" href="css/custom-styles.css">
style_pattern = r'<!-- CSS PALETA CORTADA: MITAD AZUL / MITAD BLANCO INDUSTRIAL OPTIMIZADOS -->\s*<style>.*?</style>'
link_tag = '<!-- CSS Custom Optimizado y Modularizado -->\n    <link rel="stylesheet" href="css/custom-styles.css">'

if re.search(style_pattern, content, re.DOTALL):
    content = re.sub(style_pattern, link_tag, content, count=1, flags=re.DOTALL)
    print("Replaced <style> with <link rel='stylesheet' href='css/custom-styles.css'>")
else:
    # Try generic <style>...</style> in head
    content = re.sub(r'<style>.*?</style>', link_tag, content, count=1, flags=re.DOTALL)
    print("Replaced generic <style> with <link>")

# 2. Remove duplicate ambient blur videos
# e.g. <video ... class="roxar-card-video roxar-video-ambient-blur" ...> ... </video>
ambient_blur_pattern = r'<!-- Ambient video blur de fondo -->\s*<video[^>]*class="[^"]*roxar-video-ambient-blur[^"]*"[^>]*>.*?</video>'
ambient_matches = len(re.findall(ambient_blur_pattern, content, re.DOTALL))
print(f"Found {ambient_matches} ambient blur video blocks to remove")
content = re.sub(ambient_blur_pattern, '', content, flags=re.DOTALL)

# Also check for any remaining roxar-video-ambient-blur video tags
remaining_ambient = r'<video[^>]*class="[^"]*roxar-video-ambient-blur[^"]*"[^>]*>.*?</video>'
rem_count = len(re.findall(remaining_ambient, content, re.DOTALL))
if rem_count > 0:
    print(f"Removing {rem_count} additional ambient blur videos")
    content = re.sub(remaining_ambient, '', content, flags=re.DOTALL)

# 3. Optimize all service and card videos (remove autoplay, set preload="none")
def optimize_video_tag(match):
    tag = match.group(0)
    # Don't touch hero-main-video autoplay
    if 'id="hero-main-video"' in tag or "id='hero-main-video'" in tag:
        # ensure preload="metadata"
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
    
    # Clean up double spaces
    tag = re.sub(r'\s+', ' ', tag)
    tag = tag.replace('<video ', '<video ')
    return tag

content = re.sub(r'<video[^>]*>', optimize_video_tag, content)

# 4. Remove ghost / dead elements:
# tech-particles-canvas
content = re.sub(r'<!-- Canvas de Fondo Interactivo[^>]*-->\s*<canvas id="tech-particles-canvas"></canvas>', '', content)
content = re.sub(r'<canvas id="tech-particles-canvas"></canvas>', '', content)

# globe-intro-overlay
globe_overlay_pattern = r'<!-- OVERLAY ANIMACIÓN DE ENTRADA: GLOBO 3D AICTECH -->\s*<div id="globe-intro-overlay"[^>]*>.*?</div>\s*</div>'
content = re.sub(r'<div id="globe-intro-overlay" class="hidden">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# warp-5d-overlay
content = re.sub(r'<!-- OVERLAY DE SALTO HIPERESPACIAL 5D -->\s*<div id="warp-5d-overlay"></div>', '', content)
content = re.sub(r'<div id="warp-5d-overlay"></div>', '', content)

# 5. Add loading="lazy" decoding="async" to images (except top logo in sidebar/navbar)
def optimize_img_tag(match):
    tag = match.group(0)
    # Skip navbar or sidebar logos
    if 'aictech_logo.png' in tag or 'navbar-brand' in tag or 'sidebar-heading' in tag:
        return tag
    if 'loading=' not in tag:
        tag = tag.replace('<img ', '<img loading="lazy" decoding="async" ')
    return tag

content = re.sub(r'<img[^>]*>', optimize_img_tag, content)

# 6. Check size difference
print(f"Original size: {orig_len} bytes")
print(f"New size: {len(content)} bytes")
print(f"Size reduction: {(orig_len - len(content))/1024:.1f} KB")

with open('scratch/new_index_test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved test file to scratch/new_index_test.html")

