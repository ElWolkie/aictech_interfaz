import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("File length:", len(html))

# Check stylesheets
css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', html)
print(f"CSS Links ({len(css_links)}):")
for link in css_links:
    print(" -", link)

# Check videos
videos = re.findall(r'<video[^>]*>', html)
print(f"\nTotal video tags: {len(videos)}")
autoplay_videos = [v for v in videos if 'autoplay' in v]
preload_none_videos = [v for v in videos if 'preload="none"' in v]
preload_meta_videos = [v for v in videos if 'preload="metadata"' in v]

print(f"Videos with autoplay: {len(autoplay_videos)}")
for v in autoplay_videos:
    print("  ->", v)

print(f"Videos with preload='none': {len(preload_none_videos)}")
print(f"Videos with preload='metadata': {len(preload_meta_videos)}")

# Check duplicate ambient blur videos
ambient = re.findall(r'roxar-video-ambient-blur', html)
print(f"\nRemaining ambient blur video references in HTML: {len(ambient)}")

# Check ghost canvas & overlays
print("tech-particles-canvas exists?", 'tech-particles-canvas' in html)
print("globe-intro-overlay exists?", 'globe-intro-overlay' in html)
print("warp-5d-overlay exists?", 'warp-5d-overlay' in html)

# Check images
imgs = re.findall(r'<img[^>]*>', html)
print(f"\nTotal img tags: {len(imgs)}")
lazy_imgs = [img for img in imgs if 'loading="lazy"' in img]
print(f"Images with loading='lazy': {len(lazy_imgs)}")

# Check scripts
scripts = re.findall(r'<script[^>]*>', html)
print(f"\nScript tags: {len(scripts)}")

