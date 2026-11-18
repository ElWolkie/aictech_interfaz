with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

speed_css = """
/* BOTONES DE VELOCIDAD EN LIGHTBOX */
.speed-btn {
    font-size: 0.78rem !important;
    border-radius: 4px !important;
    transition: all 0.2s ease !important;
}
.speed-btn.active {
    background: #38b6ff !important;
    color: #020813 !important;
    border-color: #38b6ff !important;
    font-weight: 800 !important;
}
"""

if '.speed-btn' not in css:
    css += speed_css
    with open('css/custom-styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added speed-btn CSS!")
else:
    print("speed-btn CSS already present")

