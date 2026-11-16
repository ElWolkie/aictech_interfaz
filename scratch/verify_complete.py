with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = []

def check(name, condition, details=""):
    status = "PASS" if condition else "FAIL"
    checks.append((name, status, details))
    print(f"[{status}] {name} {details}")

# 1. Sidebar collapse CSS & JS
check("Sidebar collapse CSS linked", 'href="css/sidebar-collapse.css"' in text)
check("Sidebar collapse JS linked", 'src="js/sidebar-collapse.js"' in text)
check("Sidebar collapse button exists", 'id="btn-sidebar-collapse"' in text)
check("Fullscreen button exists", 'id="btn-fullscreen-toggle"' in text)

# 2. Logo badge
check("Sidebar logo wrapped in badge", 'class="sidebar-brand-badge"' in text)
check("Sidebar brand logo class exists", 'sidebar-brand-logo' in text)
check("Mobile logo wrapped in badge", text.count('sidebar-brand-badge') >= 2)

# 3. Section 1 (Inicio)
check("Hero SLB panels removed from Section 1", 'class="hero-slb-panels"' not in text[text.find('data-page-no="1"'):text.find('data-page-no="2"')])
check("Hero subtitle style injected", '.hero-slb-subtitle {' in text and 'color: #ffffff !important;' in text)

# 4. Section 2 (Servicios)
check("Section 2 header is white box", 'catalog-hero-box' in text[text.find('data-page-no="2"'):text.find('id="servicio-multifasico"')])
check("Multifasico banner has roxar2600.mp4", 'video/roxar2600.mp4' in text[text.find('id="servicio-multifasico"'):text.find('id="card-multifasico-campo"')])
check("Card 1 back has updated text", 'Trailer autosuficiente con toldo en campo' in text)
check("Card 2 back has MPFM 3D link", 'https://simulador.miku-celsius.ts.net/#mpfm' in text)
check("Expand buttons injected in all cards", text.count('class="service-media-expand-btn"') == 19)
check("Videos optimized to preload metadata", text.count('preload="metadata"') >= 19)

# 5. Section 3 (PetrolIA)
p3_text = text[text.find('data-page-no="3"'):text.find('data-page-no="4"')]
check("Section 3 title is PetrolIA", '<h2 class="mb-3 fw-bold display-5 text-dark" style="color: #0b192c !important; font-weight: 800; letter-spacing: -0.5px;">PetrolIA</h2>' in p3_text)
check("No blue badges in Section 3", 'PLATAFORMA SCADA & TELEMETRÍA PREDICTIVA' not in p3_text)
check("Mapa Interactivo in white chips", '<div class="feature-chip"><i class="fas fa-map-location-dot text-primary"></i> Mapa Interactivo</div>' in p3_text)
check("Button 89 in Section 3", 'class="btn-89"' in p3_text and 'Acceder' in p3_text and 'https://petrolia-ia.miku-celsius.ts.net' in p3_text)

# 6. Section 6 (Quiénes Somos & Contacto)
p6_text = text[text.find('data-page-no="6"'):text.find('<!-- FOOTER INTEGRADO')]
check("Section 6 title is Quiénes Somos", 'Quiénes Somos' in p6_text)
check("Section 6 has Turnkey & Radioactive sources", 'fuentes radioactivas' in p6_text and 'Servicio llave en mano' in p6_text)
check("Contact card has WhatsApp & Email buttons", 'WhatsApp Directo' in p6_text and 'Enviar Correo' in p6_text)
check("Map has flex-grow-1 (no white gap)", 'flex-grow-1' in p6_text)

# 7. Lightbox and Global JS
check("Lightbox modal HTML exists", 'id="media-lightbox-modal"' in text)
check("expandCardMedia function exists", 'window.expandCardMedia' in text)
check("closeMediaLightbox function exists", 'window.closeMediaLightbox' in text)
check("toggleFullScreen function exists", 'window.toggleFullScreen' in text)
check("Updated flip card click handler exists", 'service-media-expand-btn' in text[text.find("$(document).on('click', '.service-flip-card'"):text.find("$(document).on('click', '.service-flip-card'") + 1000])

# Summary
passed = sum(1 for c in checks if c[1] == "PASS")
total = len(checks)
print(f"\nTOTAL: {passed}/{total} checks passed.")
