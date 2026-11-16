import re

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

initial_len = len(text)
print(f"Initial index.html.bak length: {initial_len} bytes")

# ------------------------------------------------------------------------------
# 1. LINK CSS & JS FOR SIDEBAR COLLAPSE
# ------------------------------------------------------------------------------
if 'css/sidebar-collapse.css' not in text:
    text = text.replace('</head>', '    <link rel="stylesheet" href="css/sidebar-collapse.css">\n</head>', 1)
    print("1. Linked css/sidebar-collapse.css")

if 'js/sidebar-collapse.js' not in text:
    text = text.replace('</body>', '    <script src="js/sidebar-collapse.js"></script>\n</body>', 1)
    print("1b. Linked js/sidebar-collapse.js")

# ------------------------------------------------------------------------------
# 2. ADD BUTTONS AFTER <body>
# ------------------------------------------------------------------------------
buttons_markup = """<body>
    <!-- BOTÓN GLOBAL PANTALLA COMPLETA (ESQUINA SUPERIOR DERECHA) -->
    <button id="btn-fullscreen-toggle" class="fullscreen-top-btn" onclick="toggleFullScreen();" title="Pantalla Completa">
        <i class="fas fa-expand me-1 text-info"></i> <span>Pantalla Completa</span>
    </button>

    <!-- BOTÓN GLOBAL PARA OCULTAR / MOSTRAR MENÚ LATERAL (DESKTOP) -->
    <button id="btn-sidebar-collapse" class="sidebar-collapse-toggle-btn" type="button" title="Ocultar Menú Lateral (Ctrl+B o [)">
        <i class="fas fa-chevron-left"></i>
    </button>
"""
if 'id="btn-fullscreen-toggle"' not in text:
    text = text.replace('<body>', buttons_markup, 1)
    print("2. Added buttons after <body>")

# ------------------------------------------------------------------------------
# 3. CSS ENHANCEMENTS
# ------------------------------------------------------------------------------
css_additions = """
        /* BOTÓN FLOTANTE PANTALLA COMPLETA */
        .fullscreen-top-btn {
            position: fixed;
            top: 14px;
            right: 20px;
            z-index: 1050;
            background: rgba(2, 12, 32, 0.85);
            border: 1px solid rgba(56, 182, 255, 0.45);
            color: #ffffff;
            padding: 7px 16px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            display: inline-flex;
            align-items: center;
            cursor: pointer;
            backdrop-filter: blur(8px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            transition: all 0.25s ease;
        }
        .fullscreen-top-btn:hover {
            background: rgba(14, 165, 233, 0.25);
            border-color: #38b6ff;
            box-shadow: 0 0 15px rgba(56, 182, 255, 0.5);
            transform: scale(1.03);
            color: #ffffff;
        }
        .fullscreen-top-btn.is-active {
            border-color: #f59e0b;
            background: rgba(30, 20, 5, 0.88);
        }

        /* RECUADRO / CÁPSULA BLANCA PARA EL LOGO AICTECH (MÁXIMO CONTRASTE Y LEGIBILIDAD) */
        .sidebar-brand-badge {
            background: #ffffff;
            border-radius: 10px;
            padding: 6px 14px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .sidebar-brand-badge:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(56, 182, 255, 0.4);
        }
        .sidebar-brand-logo {
            max-height: 44px;
            object-fit: contain;
            filter: drop-shadow(0 1px 2px rgba(0,0,0,0.15));
        }

        /* BOTÓN DE AGRANDAR PANTALLA COMPLETA EN VIDEOS Y FOTOS */
        .service-media-expand-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 15;
            background: rgba(2, 12, 32, 0.78);
            border: 1px solid rgba(255, 255, 255, 0.35);
            color: #ffffff;
            width: 32px;
            height: 32px;
            border-radius: 6px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.85rem;
            backdrop-filter: blur(6px);
            transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
        }
        .service-media-expand-btn:hover {
            background: #0284c7;
            border-color: #38bdf8;
            color: #ffffff;
            transform: scale(1.1);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
        }

        /* TAMAÑO UNIFORME PARA BOTONES "VER DETALLES" EN TARJETAS */
        .service-flip-hint-badge {
            min-width: 118px;
            height: 32px;
            justify-content: center;
            box-sizing: border-box;
            white-space: nowrap;
        }

        /* MODAL LIGHTBOX PARA VIDEOS Y FOTOS EN ALTA RESOLUCIÓN */
        .media-lightbox-overlay {
            position: fixed;
            inset: 0;
            z-index: 100050;
            background: rgba(2, 6, 18, 0.94);
            backdrop-filter: blur(14px);
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .media-lightbox-overlay.active {
            display: flex;
            opacity: 1;
        }
        .media-lightbox-container {
            position: relative;
            width: 100%;
            max-width: 1100px;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .media-lightbox-close {
            position: absolute;
            top: -46px;
            right: 0;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #ffffff;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.1rem;
            transition: all 0.2s ease;
        }
        .media-lightbox-close:hover {
            background: #ef4444;
            border-color: #ef4444;
            transform: scale(1.08);
        }
        .media-lightbox-stage {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            max-height: 80vh;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85), 0 0 30px rgba(56, 182, 255, 0.2);
            border: 1px solid rgba(56, 182, 255, 0.3);
            background: #000000;
        }
        .media-lightbox-stage video,
        .media-lightbox-stage img {
            max-width: 100%;
            max-height: 80vh;
            width: auto;
            height: auto;
            object-fit: contain;
            display: block;
        }
        .media-lightbox-caption {
            margin-top: 14px;
            text-align: center;
            color: #e2e8f0;
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 0.3px;
        }

        /* BOTÓN INDUSTRIAL PETROLERO .btn-89 CON GOTAS ANIMADAS */
        .btn-89 {
            width: 160px;
            height: 55px;
            transition: all 0.2s ease;
            position: relative;
            background: none;
            outline: none;
            border: none;
            font-family: inherit;
            cursor: pointer;
            text-decoration: none;
            user-select: none;
            padding: 0;
            display: inline-block;
        }
        .button_text_89 {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(8, 29, 61, 0.95), rgba(4, 15, 33, 0.98));
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35), inset 0 1px 1px rgba(56, 182, 255, 0.4);
            border: 1px solid rgba(56, 182, 255, 0.35);
            backdrop-filter: blur(10px);
            border-radius: 8px;
            display: flex;
            text-align: center;
            justify-content: center;
            align-items: center;
            font-size: 19px;
            font-weight: bold;
            color: #cbd5e1;
            letter-spacing: 0.5px;
            transition: all 0.25s ease;
        }
        .btn-89:hover .button_text_89 {
            color: #ffffff;
            border-color: #38bdf8;
            box-shadow: 0 6px 25px rgba(2, 132, 199, 0.4), inset 0 1px 2px rgba(255, 255, 255, 0.6);
            transform: translateY(-2px);
        }
        .circle_89 {
            width: 22px;
            height: 22px;
            background: radial-gradient(circle at 35% 35%, #0284c7, #030d1b);
            border-radius: 50%;
            position: absolute;
            animation: move_up_89 2.2s ease-in-out infinite alternate-reverse;
            box-shadow: 0 0 10px rgba(2, 132, 199, 0.5);
            pointer-events: none;
        }
        .circle_89:nth-child(1) {
            top: 6px;
            left: 6px;
        }
        .circle_89:nth-child(2) {
            bottom: -2px;
            right: -2px;
            animation-name: move_down_89;
        }
        @keyframes move_up_89 {
            100% {
                transform: translateY(-12px);
            }
        }
        @keyframes move_down_89 {
            100% {
                transform: translateY(8px);
            }
        }

        /* CONTENEDOR PETROLIA Y LOGO ANIMADO SUAVE */
        .petrolia-card-container {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .petrolia-card-container:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 50px rgba(2, 132, 199, 0.15) !important;
        }
        .petrolia-logo-animated {
            max-height: 88px;
            transition: transform 0.4s ease;
            filter: drop-shadow(0 4px 15px rgba(0, 0, 0, 0.08));
        }
        .petrolia-logo-animated:hover {
            transform: scale(1.04);
        }

        /* HERO SUBTITLE CLARIFICADO PARA MÁXIMA LEGIBILIDAD */
        .hero-slb-subtitle {
            color: #ffffff !important;
            font-size: 1.12rem !important;
            line-height: 1.7 !important;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95), 0 1px 3px rgba(0, 0, 0, 0.9) !important;
            max-width: 820px !important;
        }

        /* AMBIENT BLUR OPTIMIZADO PARA MÁXIMA FLUIDEZ DE VIDEO (HARDWARE ACCELERATED) */
        .service-flip-front video.roxar-video-ambient-blur {
            filter: blur(12px) brightness(0.65) !important;
            transform: scale(1.25) translate3d(0, 0, 0) !important;
            will-change: transform !important;
        }

        .hero-slb-panels {
            display: none !important;
        }
"""
text = text.replace('</style>', css_additions + '\n    </style>', 1)
print("3. Injected CSS additions")

# ------------------------------------------------------------------------------
# 4. LOGO BADGE IN SIDEBAR & MOBILE NAVBAR (Task 5)
# ------------------------------------------------------------------------------
old_sidebar_heading = """        <div class="sidebar-heading text-center pt-4 pb-2">
            <!-- LOGO AICTECH -->
            <a href="#0" class="d-block text-decoration-none tm-page-link" data-page-no="1" data-no="1" title="Ir a Inicio AICTECH" onclick="openPage(1); highlightMenu(1); return false;">
                <img src="img/aictech_logo.png" alt="AICTECH Logo" class="img-fluid" style="max-height: 48px; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.4));">
            </a>
        </div>"""

new_sidebar_heading = """        <div class="sidebar-heading text-center pt-4 pb-2">
            <!-- LOGO AICTECH CON RECUADRO BLANCO PARA MÁXIMA VISIBILIDAD -->
            <a href="#0" class="d-inline-block text-decoration-none tm-page-link" data-page-no="1" data-no="1" title="Ir a Inicio AICTECH" onclick="openPage(1); highlightMenu(1); return false;">
                <div class="sidebar-brand-badge">
                    <img src="img/aictech_logo.png" alt="AICTECH Logo" class="img-fluid sidebar-brand-logo">
                </div>
            </a>
        </div>"""

if old_sidebar_heading in text:
    text = text.replace(old_sidebar_heading, new_sidebar_heading, 1)
    print("4. Sidebar heading logo badge updated")

old_mobile_logo = '<img src="img/aictech_logo.png" alt="AICTECH Logo" style="max-height: 35px;">'
new_mobile_logo = '<div class="sidebar-brand-badge py-1 px-2" style="border-radius: 8px;"><img src="img/aictech_logo.png" alt="AICTECH Logo" style="max-height: 30px;"></div>'
if old_mobile_logo in text:
    text = text.replace(old_mobile_logo, new_mobile_logo, 1)
    print("4b. Mobile navbar logo badge updated")

# ------------------------------------------------------------------------------
# 5. SECTION 1 (INICIO): REMOVE 3 BOTTOM CARDS (Task 2)
# ------------------------------------------------------------------------------
p1_start = text.find('<!-- Bottom Industrial Capability Panels (Estilo SLB) -->')
p2_start = text.find('<!-- SECCIÓN 2: SERVICIOS', p1_start)
new_p1_end = """</div>
                    </div>
                </li>\n\n                """
text = text[:p1_start] + new_p1_end + text[p2_start:]
print("5. Removed Section 1 hero-slb-panels cleanly")

# ------------------------------------------------------------------------------
# 6. SECTION 2 (SERVICIOS): HEADER + MULTIFASICO BANNER + BACK SPECS
# ------------------------------------------------------------------------------
old_sec2_hdr = """                            <div class="services-feed-header reveal-on-scroll reveal-up">
                                <span class="service-feed-tag"><i class="fas fa-layer-group me-1"></i> SERVICIOS ESPECIALIZADOS DE CAMPO</span>
                                <h2>Soluciones Integrales de Medición & Diagnóstico</h2>
                                <p>Descubra nuestras capacidades operacionales diseñadas para optimizar yacimientos, cuantificar producción en tiempo real y maximizar la confiabilidad en superficie y fondo.</p>
                            </div>"""

new_sec2_hdr = """                            <!-- Header de la Sección (Container Blanco para Máxima Legibilidad) -->
                            <div class="catalog-hero-box reveal-on-scroll reveal-up mb-4" style="background: #ffffff; border-radius: 14px; padding: 24px 28px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25); border: 1px solid rgba(0, 0, 0, 0.08);">
                                <h1 class="fw-bold display-6 text-dark mb-2" style="font-size: clamp(1.8rem, 3.2vw, 2.4rem);">Soluciones Integrales de Medición &amp; Diagnóstico</h1>
                                <p class="text-muted fs-6 mb-0" style="line-height: 1.7; max-width: 950px;">
                                    Descubra nuestras capacidades operacionales diseñadas para optimizar yacimientos, cuantificar producción en tiempo real y maximizar la confiabilidad en superficie y fondo.
                                </p>
                            </div>"""

if old_sec2_hdr in text:
    text = text.replace(old_sec2_hdr, new_sec2_hdr, 1)
    print("6. Section 2 Header updated to white card")

# Banner Multifasico: restore roxar2600.mp4
idx_sec2 = text.find('id="servicio-multifasico"')
banner_start = text.find('<div class="roxar-hero-banner"', idx_sec2)
banner_end = text.find('<!-- Sección Inferior:', banner_start)
new_banner = """<div class="roxar-hero-banner" style="position: relative; overflow: hidden;">
                                    <video autoplay loop muted playsinline webkit-playsinline disablePictureInPicture preload="auto" class="roxar-video-bg service-video-elem" id="roxar-main-video">
                                        <source src="video/roxar2600.mp4" type="video/mp4">
                                        Su navegador no soporta video HTML5.
                                    </video>
                                    <div class="roxar-video-overlay" style="background: linear-gradient(135deg, rgba(2, 10, 26, 0.65) 0%, rgba(2, 15, 38, 0.40) 50%, rgba(2, 10, 26, 0.70) 100%);"></div>
                                    <div class="roxar-hero-content">
                                        <h2 class="roxar-title">Medidor Multifásico</h2>
                                        <p class="roxar-lead-text">
                                            Medición en línea de caudales de petróleo, agua y gas en tiempo real sin separación invasiva.
                                        </p>
                                    </div>
                                </div>\n\n                                """
text = text[:banner_start] + new_banner + text[banner_end:]
print("6b. Section 2 Multifasico banner updated to roxar2600.mp4")

# Card 1 back specs
c1_start = text.find('id="card-multifasico-campo"')
pos1 = text.find('<div class="service-flip-back">', c1_start)
pos1_end = text.find('<!-- Panel Derecho: Gemelo Digital Roxar -->', pos1)
new_c1_back = """<div class="service-flip-back">
                                                        <div>
                                                            <div class="d-flex justify-content-between align-items-center mb-2 pb-1 border-bottom">
                                                                <span class="roxar-panel-badge mb-0"><i class="fas fa-truck-pickup me-1"></i> DESPLIEGUE INTEGRAL EN CAMPO</span>
                                                            </div>
                                                            <h3 class="roxar-panel-title mb-2 fs-5">Well Testing con Medidor Multifásico Roxar</h3>
                                                            <p class="roxar-panel-desc mb-3 small text-secondary">
                                                                Servicio completo de prueba de pozo que cuenta con unidad móvil, trailer autosuficientes, toldo en campo y laboratorio en sitio.
                                                            </p>
                                                            <ul class="instrument-features mb-0 small text-secondary">
                                                                <li><strong>Medición en Línea Continua:</strong> Cuantificación en tiempo real de petróleo, agua y gas en boca de pozo sin separación física.</li>
                                                                <li><strong>Trailer autosuficiente con toldo en campo</strong></li>
                                                                <li><strong>Telemetría en tiempo Real:</strong> Transmisión instantanea de variable de producccion a interfaz gráfica para adquisición y analizis de datos.</li>
                                                            </ul>
                                                        </div>
                                                        <div>
                                                            <div class="service-flip-btn-back">
                                                                <i class="fas fa-arrow-rotate-left"></i> <span>Volver a la vista frontal</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>\n\n                                        """
text = text[:pos1] + new_c1_back + text[pos1_end:]
print("6c. Card 1 back specs updated")

# Card 2 back specs
c2_start = text.find('id="roxar-exe-trigger"')
pos2 = text.find('<div class="service-flip-back">', c2_start)
next_article = text.find('<!-- 2. SERVICIO:', pos2)
new_c2_back = """<div class="service-flip-back">
                                                        <div>
                                                            <div class="d-flex justify-content-between align-items-center mb-2 pb-1 border-bottom">
                                                                <span class="roxar-panel-badge mb-0"><i class="fas fa-vr-cardboard me-1"></i> SIMULADOR EN TIEMPO REAL</span>
                                                            </div>
                                                            <h3 class="roxar-panel-title mb-2 fs-5">Gemelo Digital Roxar</h3>
                                                            <p class="roxar-panel-desc mb-3 small text-secondary">
                                                                Ambiente de simulación interactiva que replica el comportamiento termodinámico, corte de agua (BS&amp;W) y relación gas-líquido.
                                                            </p>
                                                            <ul class="instrument-features mb-3 small text-secondary">
                                                                <li><strong>Simulación Dinámica:</strong> Simulación interactiva de caudal de flujo.</li>
                                                                <li><strong>Predicción Instantánea:</strong> Evualuar comportamiento de producción en base al caudal.</li>
                                                            </ul>
                                                            <a href="https://simulador.miku-celsius.ts.net/#mpfm" target="_blank" rel="noopener noreferrer" class="roxar-action-btn w-100 py-2 text-decoration-none text-center d-flex align-items-center justify-content-center" id="btn-activar-gemelo-link" onclick="event.stopPropagation();">
                                                                <i class="fas fa-cube me-2"></i> Abrir Simulador MPFM 3D
                                                            </a>
                                                        </div>
                                                        <div>
                                                            <div class="service-flip-btn-back">
                                                                <i class="fas fa-arrow-rotate-left"></i> <span>Volver al video</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>\n\n                                    </div>\n                                </div>\n                            </article>\n\n                            """
text = text[:pos2] + new_c2_back + text[next_article:]
print("6d. Card 2 back specs updated")

# Inject expand buttons
expand_btn_html = '<button type="button" class="service-media-expand-btn" title="Agrandar pantalla completa" onclick="event.stopPropagation(); expandCardMedia(this);"><i class="fas fa-expand"></i></button>\n                                    '
def inject_expand_btn(match):
    wrap_content = match.group(0)
    if 'service-media-expand-btn' in wrap_content:
        return wrap_content
    return '<div class="service-video-wrap">\n                                    ' + expand_btn_html

text = re.sub(r'<div class="service-video-wrap">\s*', inject_expand_btn, text)
print("6e. Injected expand buttons in all service-video-wrap elements")

# Preload metadata on all card videos
def set_preload_metadata(match):
    v = match.group(0)
    if 'id="hero-main-video"' in v or 'id="roxar-main-video"' in v:
        return v
    return v.replace('preload="auto"', 'preload="metadata"')

text = re.sub(r'<video\b[^>]*preload="auto"[^>]*>', set_preload_metadata, text)
print("6f. Optimized video preload attributes to metadata")

# ------------------------------------------------------------------------------
# 7. SECTION 3 (PETROLIA) (Task 1)
# ------------------------------------------------------------------------------
p3_start = text.find('<!-- SECCIÓN 3: PETROLIA')
p4_start = text.find('<!-- SECCIÓN 4:', p3_start)
new_p3 = """<!-- SECCIÓN 3: PETROLIA (CONSOLA SCADA INTERACTIVA PULCRA) -->
                <li data-page-no="3" class="px-3">
                    <div class="page-width-1 h-100 d-flex align-items-center justify-content-center">
                        <div class="p-4 p-md-5 text-center w-100 shadow-lg reveal-on-scroll reveal-up petrolia-card-container" style="max-width: 920px; background: #ffffff; border-radius: 18px; box-shadow: 0 15px 45px rgba(0, 0, 0, 0.12), 0 2px 10px rgba(0, 0, 0, 0.05); border: 1px solid rgba(226, 232, 240, 0.9);">
                            <div class="mb-4 text-center">
                                <img src="img/petrolia-img.png" alt="PetrolIA" class="img-fluid petrolia-logo-animated">
                            </div>
                            <h2 class="mb-3 fw-bold display-5 text-dark" style="color: #0b192c !important; font-weight: 800; letter-spacing: -0.5px;">PetrolIA</h2>
                            <p class="fs-5 mb-4 mx-auto" style="max-width: 820px; line-height: 1.7; color: #475569 !important;">
                                Ecosistema digital para monitoreo, adquisición y análisis continuo de pozos en tiempo real, integrando modelado predictivo de producción y telemetría de campo 24/7.
                            </p>
                            <!-- PUNTOS DESTACADOS EN CHIPS BLANCOS -->
                            <div class="d-flex flex-wrap justify-content-center gap-3 mb-4 py-2">
                                <div class="feature-chip"><i class="fas fa-map-location-dot text-primary"></i> Mapa Interactivo</div>
                                <div class="feature-chip"><i class="fas fa-satellite-dish text-primary"></i> Telemetría en Tiempo Real</div>
                                <div class="feature-chip"><i class="fas fa-brain text-info"></i> Algoritmos Predictivos de Producción</div>
                                <div class="feature-chip"><i class="fas fa-chart-line text-success"></i> Análisis de Curvas de Declinación</div>
                                <div class="feature-chip"><i class="fas fa-shield-halved text-warning"></i> Alertas Tempranas de Pozo</div>
                            </div>
                            <div class="mt-4 pt-2 d-flex justify-content-center">
                                <a href="https://petrolia-ia.miku-celsius.ts.net" target="_blank" rel="noopener noreferrer" class="btn-89" title="Acceder a PetrolIA">
                                    <span class="circle_89"></span>
                                    <span class="circle_89"></span>
                                    <span class="button_text_89">Acceder</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </li>\n\n                """
text = text[:p3_start] + new_p3 + text[p4_start:]
print("7. Section 3 PetrolIA updated (title, white chips, btn-89)")

# ------------------------------------------------------------------------------
# 8. SECTION 6 (QUIÉNES SOMOS & CONTACTO) (Task 4)
# ------------------------------------------------------------------------------
p6_start = text.find('<!-- SECCIÓN 6: EQUIPO Y CONTACTO')
p6_footer = text.find('<!-- FOOTER INTEGRADO', p6_start)
new_p6 = """<!-- SECCIÓN 6: QUIÉNES SOMOS & CONTACTO -->
                <li data-page-no="6" class="px-3">
                    <div class="page-width-1 h-100 d-flex align-items-center">
                        <div class="row g-4 w-100 justify-content-center align-items-stretch">
                            <div class="col-12 col-lg-6">
                                <div class="glass-card p-4 p-md-5 h-100 d-flex flex-column justify-content-between" style="background: rgba(2, 10, 26, 0.85); border: 1px solid rgba(56, 182, 255, 0.35); border-radius: 18px;">
                                    <div>
                                        <h3 class="mb-3 fw-bold display-6 fs-3 text-white">Quiénes Somos</h3>
                                        <p class="mb-2 fs-6 leading-relaxed" style="color: #cbd5e1;">
                                            Somos una empresa con visión de futuro, que combina la experticia de su personal con modernas instalaciones y herramientas tecnológicas de avanzada.
                                        </p>
                                        <p class="mb-3 fs-6 leading-relaxed" style="color: #94a3b8;">
                                            Dedicados integralmente a los servicios de ingeniería, construcción y soporte operativo en las áreas clave de la industria petrolera e industrial:
                                        </p>
                                        <div class="d-flex flex-column gap-2 mt-3">
                                            <div class="tech-list-item" style="border-left: 3px solid #38bdf8; background: rgba(56, 182, 255, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-layer-group text-info me-2"></i><strong>Prueba de producción de pozos petroleros con separador convencional y multifásico</strong></div>
                                            <div class="tech-list-item" style="border-left: 3px solid #0ea5e9; background: rgba(14, 165, 233, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-sliders text-primary me-2"></i><strong>Automatización, instrumentación y control industrial</strong></div>
                                            <div class="tech-list-item" style="border-left: 3px solid #eab308; background: rgba(234, 179, 8, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-bolt text-warning me-2"></i><strong>Electricidad y acondicionamiento electromecánico</strong></div>
                                            <div class="tech-list-item" style="border-left: 3px solid #f97316; background: rgba(249, 115, 22, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-radiation text-warning me-2"></i><strong>Compra, venta y distribución de fuentes radioactivas para servicios industriales</strong></div>
                                            <div class="tech-list-item" style="border-left: 3px solid #6366f1; background: rgba(99, 102, 241, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-key text-info me-2"></i><strong>Servicio llave en mano (Turnkey / EPC)</strong></div>
                                            <div class="tech-list-item" style="border-left: 3px solid #ec4899; background: rgba(236, 72, 153, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-wrench text-danger me-2"></i><strong>Reconstrucción y acondicionamiento de sistemas</strong></div>
                                            <div class="tech-list-item" style="border-left: 3px solid #8b5cf6; background: rgba(139, 92, 246, 0.08); padding: 9px 14px; border-radius: 6px;"><i class="fas fa-globe-americas text-primary me-2"></i><strong>Importación, exportación y comercialización de equipos</strong></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-lg-6">                  
                                <div class="glass-card p-4 p-md-5 h-100 d-flex flex-column" style="background: rgba(2, 10, 26, 0.85); border: 1px solid rgba(56, 182, 255, 0.35); border-radius: 18px;">
                                    <div>
                                        <h3 class="mb-3 fw-bold display-6 fs-3 text-white">Contacto Directo</h3>
                                        <p class="mb-2 fs-6 text-muted"><strong class="text-white"><i class="fas fa-location-dot text-primary me-2"></i>Oficina:</strong> Anaco - Anzoátegui, Venezuela</p>
                                        <p class="mb-2 fs-6 text-muted"><strong class="text-white"><i class="fas fa-envelope text-info me-2"></i>Email:</strong> <a href="mailto:ventas@aictech.net" class="text-primary fw-semibold text-decoration-none">ventas@aictech.net</a></p>
                                        <p class="mb-3 fs-6 text-muted"><strong class="text-white"><i class="fas fa-phone text-success me-2"></i>Línea de Atención:</strong> <a href="tel:+584148366073" class="text-primary fw-semibold text-decoration-none">+58 414 8366073</a></p>
                                        
                                        <div class="d-flex flex-wrap gap-2 mb-3">
                                            <a href="https://wa.me/584148366073" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-success px-3 py-1 text-decoration-none">
                                                <i class="fab fa-whatsapp me-1"></i> WhatsApp Directo
                                            </a>
                                            <a href="mailto:ventas@aictech.net" class="btn btn-sm btn-outline-info px-3 py-1 text-decoration-none">
                                                <i class="fas fa-paper-plane me-1"></i> Enviar Correo
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rounded-3 overflow-hidden border border-secondary shadow-sm mt-2 flex-grow-1" style="min-height: 280px;">
                                        <iframe width="100%" height="100%" id="gmap-canvas" style="min-height: 280px; width: 100%; border: 0;"
                                            src="https://maps.google.com/maps?q=9.447929573272631,-64.46658166186569&hl=es&z=15&output=embed"
                                            frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>\n\n        """
text = text[:p6_start] + new_p6 + text[p6_footer:]
print("8. Section 6 Quiénes Somos and Contact card updated (zero white gap)")

# ------------------------------------------------------------------------------
# 9. LIGHTBOX MODAL HTML AND GLOBAL JS
# ------------------------------------------------------------------------------
lightbox_markup = """
<!-- MODAL LIGHTBOX PARA VISUALIZACIÓN DE VIDEOS Y FOTOS EN ALTA RESOLUCIÓN -->
<div id="media-lightbox-modal" class="media-lightbox-overlay" onclick="if(event.target===this) closeMediaLightbox();">
    <div class="media-lightbox-container">
        <button type="button" class="media-lightbox-close" onclick="closeMediaLightbox();" title="Cerrar"><i class="fas fa-times"></i></button>
        <div class="media-lightbox-stage" id="media-lightbox-stage">
            <!-- Dinámico: Video o Imagen -->
        </div>
        <div class="media-lightbox-caption" id="media-lightbox-caption">
            <h4 class="media-lightbox-title" id="media-lightbox-title"></h4>
        </div>
    </div>
</div>
"""
if 'id="media-lightbox-modal"' not in text:
    text = text.replace('</body>', lightbox_markup + '\n</body>', 1)
    print("9. Added #media-lightbox-modal HTML")

js_functions = """
        // ==========================================
        // PANTALLA COMPLETA GLOBAL
        // ==========================================
        window.toggleFullScreen = function() {
            try {
                if (!document.fullscreenElement && !document.webkitFullscreenElement && !document.mozFullScreenElement && !document.msFullscreenElement) {
                    const elem = document.documentElement;
                    if (elem.requestFullscreen) {
                        elem.requestFullscreen();
                    } else if (elem.webkitRequestFullscreen) {
                        elem.webkitRequestFullscreen();
                    } else if (elem.mozRequestFullScreen) {
                        elem.mozRequestFullScreen();
                    } else if (elem.msRequestFullscreen) {
                        elem.msRequestFullscreen();
                    }
                } else {
                    if (document.exitFullscreen) {
                        document.exitFullscreen();
                    } else if (document.webkitExitFullscreen) {
                        document.webkitExitFullscreen();
                    } else if (document.mozCancelFullScreen) {
                        document.mozCancelFullScreen();
                    } else if (document.msExitFullscreen) {
                        document.msExitFullscreen();
                    }
                }
            } catch(e) {
                console.warn('Error al alternar pantalla completa:', e);
            }
        };

        function updateFullscreenButtonState() {
            const btn = document.getElementById('btn-fullscreen-toggle');
            if (!btn) return;
            const isFull = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
            if (isFull) {
                btn.innerHTML = '<i class="fas fa-compress me-1 text-warning"></i> <span>Salir Pantalla Completa</span>';
                btn.classList.add('is-active');
            } else {
                btn.innerHTML = '<i class="fas fa-expand me-1 text-info"></i> <span>Pantalla Completa</span>';
                btn.classList.remove('is-active');
            }
        }

        document.addEventListener('fullscreenchange', updateFullscreenButtonState);
        document.addEventListener('webkitfullscreenchange', updateFullscreenButtonState);
        document.addEventListener('mozfullscreenchange', updateFullscreenButtonState);
        document.addEventListener('MSFullscreenChange', updateFullscreenButtonState);

        // ==========================================
        // LIGHTBOX EXPAND PARA VIDEOS Y FOTOS HD (AISLADO PARA MÁXIMA FLUIDEZ)
        // ==========================================
        window.expandCardMedia = function(btn) {
            // Pausar todos los videos activos en la página para destinar el 100% de GPU/CPU al video expandido
            document.querySelectorAll('video').forEach(function(v) {
                if (!v.paused) {
                    v.dataset.wasPlaying = 'true';
                    v.pause();
                }
            });

            const card = btn.closest('.service-flip-card') || btn.closest('.catalog-brand-card') || btn.closest('.service-video-wrap');
            if (!card) return;

            const stage = document.getElementById('media-lightbox-stage');
            const titleElem = document.getElementById('media-lightbox-title');
            const modal = document.getElementById('media-lightbox-modal');
            if (!stage || !modal) return;

            stage.innerHTML = '';

            let title = '';
            const titleNode = card.querySelector('.service-tech-title, .brand-card-title, .service-video-tag, .card-slide-caption, .service-front-title');
            if (titleNode) {
                title = titleNode.innerText.replace(/[\\n\\r]+/g, ' ').trim();
            }

            const activeSlide = card.querySelector('.card-slide-item.active');
            const scope = activeSlide || card;

            const img = scope.querySelector('img.card-slide-img, img.roxar-card-img, img.catalog-brand-img, img');
            const fgVideo = scope.querySelector('video.roxar-card-video-foreground');
            const video = fgVideo || scope.querySelector('video:not(.roxar-video-ambient-blur)') || scope.querySelector('video');

            if (activeSlide && activeSlide.getAttribute('data-type') === 'image' && img) {
                const newImg = document.createElement('img');
                newImg.src = img.src;
                newImg.alt = title || 'Visualización en alta resolución';
                stage.appendChild(newImg);
            } else if (video) {
                const newVid = document.createElement('video');
                newVid.controls = true;
                newVid.autoplay = true;
                newVid.loop = true;
                newVid.playsInline = true;
                
                const srcElem = video.querySelector('source');
                const srcUrl = srcElem ? srcElem.src : video.src;
                newVid.src = srcUrl;
                newVid.currentTime = video.currentTime || 0;
                stage.appendChild(newVid);
                newVid.play().catch(() => {});
            } else if (img) {
                const newImg = document.createElement('img');
                newImg.src = img.src;
                newImg.alt = title || 'Visualización en alta resolución';
                stage.appendChild(newImg);
            }

            if (titleElem) {
                titleElem.textContent = title;
            }

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        };

        window.closeMediaLightbox = function() {
            const modal = document.getElementById('media-lightbox-modal');
            const stage = document.getElementById('media-lightbox-stage');
            if (!modal) return;

            if (stage) {
                const vid = stage.querySelector('video');
                if (vid) {
                    vid.pause();
                    vid.removeAttribute('src');
                    vid.load();
                }
                stage.innerHTML = '';
            }
            modal.classList.remove('active');
            document.body.style.overflow = '';
        };

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeMediaLightbox();
            }
        });
"""

new_flip_block = """$(document).on('click', '.service-flip-card', function(e) {
            // Evitar voltear si se hace clic en enlaces o controles de navegación del slider o botón de expandir
            if ($(e.target).closest('a[href], .card-slider-pills, .card-slider-arrow, .service-media-expand-btn').length) {
                return;
            }

            const card = this;
            const isFlipped = card.classList.contains('is-flipped');
            const isBackClick = !!$(e.target).closest('.service-flip-back').length;

            // PASO REVERSO: Si ya está volteada o se hizo clic en el botón de volver / reverso
            if (isFlipped || isBackClick) {
                card.classList.remove('is-flipped');
                return;
            }

            // Si se hace clic directamente en el badge "Ver Detalles", girar de inmediato a especificaciones
            if ($(e.target).closest('.service-flip-hint-badge').length) {
                card.classList.add('is-flipped');
                return;
            }

            // PASO FRONTAL:
            // Si la tarjeta tiene un carrusel y está mostrando una imagen estática, girar directamente
            const activeSlide = card.querySelector('.card-slide-item.active');
            if (activeSlide && activeSlide.getAttribute('data-type') === 'image') {
                card.classList.add('is-flipped');
                return;
            }

            // PRIORIDAD FOREGROUND: Buscar primero el video visible para no atrapar el blur ambiental
            const fgVideo = card.querySelector('video.roxar-card-video-foreground');
            const video = activeSlide ? (activeSlide.querySelector('video.roxar-card-video-foreground') || activeSlide.querySelector('video:not(.roxar-video-ambient-blur)') || activeSlide.querySelector('video')) : (fgVideo || card.querySelector('video:not(.roxar-video-ambient-blur)') || card.querySelector('video'));
            const ambientBlur = card.querySelector('video.roxar-video-ambient-blur');
            const isPlaying = card.classList.contains('is-video-playing') && video && !video.paused;

            if (!isPlaying) {
                // PRIMER CLIC: Reproducir video
                // Pausar cualquier otra tarjeta de servicio activa para optimizar recursos
                document.querySelectorAll('.service-flip-card.is-video-playing').forEach(otherCard => {
                    if (otherCard !== card) {
                        otherCard.classList.remove('is-video-playing');
                        const otherFg = otherCard.querySelector('video.roxar-card-video-foreground');
                        const otherVid = otherFg || otherCard.querySelector('video:not(.roxar-video-ambient-blur)') || otherCard.querySelector('video');
                        const otherBlur = otherCard.querySelector('video.roxar-video-ambient-blur');
                        if (otherVid && !otherVid.paused) otherVid.pause();
                        if (otherBlur && !otherBlur.paused) otherBlur.pause();
                        const otherBadge = otherCard.querySelector('.service-flip-hint-badge');
                        if (otherBadge) { otherBadge.innerHTML = '<i class="fas fa-rotate me-1"></i> Ver Detalles'; }
                    }
                });

                if (video) {
                    video.muted = true;
                    video.playsInline = true;
                    video.play().then(() => {
                        card.classList.add('is-video-playing');
                        if (ambientBlur) {
                            ambientBlur.muted = true;
                            ambientBlur.playsInline = true;
                            ambientBlur.currentTime = video.currentTime;
                            ambientBlur.play().catch(() => {});
                        }
                        const badge = card.querySelector('.service-flip-hint-badge');
                        if (badge) {
                            badge.innerHTML = '<i class="fas fa-rotate me-1"></i> Ver Detalles';
                        }
                    }).catch(err => {
                        console.log('Video play triggered fallback flip:', err);
                        card.classList.add('is-flipped');
                    });
                } else {
                    card.classList.add('is-flipped');
                }
            } else {
                // SEGUNDO CLIC: Ya se estaba reproduciendo, girar a las especificaciones
                card.classList.add('is-flipped');
            }
        });"""

idx_flip = text.find("$(document).on('click', '.service-flip-card'")
if idx_flip != -1:
    next_handler = text.find("$(document).on(", idx_flip + 50)
    text = text[:idx_flip] + js_functions + '\n        ' + new_flip_block + '\n\n        ' + text[next_handler:]
    print("9b. Updated flip card click handler and added lightbox functions using exact slicing")

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

final_len = len(text)
print(f"Final index.html length: {final_len} bytes, lines: {text.count(chr(10))}")
print("DIFF in bytes:", final_len - initial_len)
