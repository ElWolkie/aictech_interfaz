with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# 1. Update modal HTML with speed selector
old_modal_caption = """        <div class="media-lightbox-caption" id="media-lightbox-caption">
            <h4 class="media-lightbox-title" id="media-lightbox-title"></h4>
        </div>"""

new_modal_caption = """        <div class="media-lightbox-caption" id="media-lightbox-caption">
            <h4 class="media-lightbox-title" id="media-lightbox-title"></h4>
            <div id="media-lightbox-speed-bar" class="d-flex align-items-center justify-content-center gap-2 mt-2" style="display: none;">
                <span class="small text-white-50"><i class="fas fa-gauge-high text-info me-1"></i> Velocidad:</span>
                <button type="button" class="btn btn-sm btn-outline-info py-0 px-2 fw-bold speed-btn active" onclick="setLightboxPlaybackRate(1, this)">1x (Normal)</button>
                <button type="button" class="btn btn-sm btn-outline-info py-0 px-2 fw-bold speed-btn" onclick="setLightboxPlaybackRate(1.25, this)">1.25x</button>
                <button type="button" class="btn btn-sm btn-outline-warning py-0 px-2 fw-bold speed-btn" onclick="setLightboxPlaybackRate(1.5, this)">1.5x (Dinámico)</button>
                <button type="button" class="btn btn-sm btn-outline-warning py-0 px-2 fw-bold speed-btn" onclick="setLightboxPlaybackRate(2, this)">2x (Rápido)</button>
            </div>
        </div>"""

if old_modal_caption in text:
    text = text.replace(old_modal_caption, new_modal_caption)
    print("Updated modal caption HTML with speed controls!")
else:
    print("Could not find exact old_modal_caption, trying regex...")
    text = re.sub(r'<div class="media-lightbox-caption"[^>]*>.*?<h4[^>]*id="media-lightbox-title"[^>]*></h4>\s*</div>', new_modal_caption, text, flags=re.DOTALL)
    print("Replaced modal caption via regex!")

# 2. Add setLightboxPlaybackRate and toggle speed bar in expandCardMedia
js_helper = """
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
"""

# Add js_helper right above window.expandCardMedia
text = text.replace('window.expandCardMedia = function(target) {', js_helper + '\n        window.expandCardMedia = function(target) {')

# In expandCardMedia, show/hide speed bar based on media type
show_bar_code = """
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
"""

text = text.replace('modal.classList.add(\'active\');', show_bar_code.strip() + '\n            modal.classList.add(\'active\');')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html successfully!")

