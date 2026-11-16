import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

initial_len = len(text)
print(f"Initial index.html length: {initial_len} bytes")

# ------------------------------------------------------------------------------
# 1. RESTORE ORIGINAL AIC TECH LOGO IN SIDEBAR & MOBILE NAVBAR (Point 10)
# ------------------------------------------------------------------------------
old_sidebar_heading = """        <div class="sidebar-heading text-center pt-4 pb-2">
            <!-- LOGO AICTECH CON RECUADRO BLANCO PARA MÁXIMA VISIBILIDAD -->
            <a href="#0" class="d-inline-block text-decoration-none tm-page-link" data-page-no="1" data-no="1" title="Ir a Inicio AICTECH" onclick="openPage(1); highlightMenu(1); return false;">
                <div class="sidebar-brand-badge">
                    <img src="img/aictech_logo.png" alt="AICTECH Logo" class="img-fluid sidebar-brand-logo">
                </div>
            </a>
        </div>"""

new_sidebar_heading = """        <div class="sidebar-heading text-center pt-4 pb-2">
            <!-- LOGO AICTECH -->
            <a href="#0" class="d-block text-decoration-none tm-page-link" data-page-no="1" data-no="1" title="Ir a Inicio AICTECH" onclick="openPage(1); highlightMenu(1); return false;">
                <img src="img/aictech_logo.png" alt="AICTECH Logo" class="img-fluid" style="max-height: 48px; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.4));">
            </a>
        </div>"""

if old_sidebar_heading in text:
    text = text.replace(old_sidebar_heading, new_sidebar_heading, 1)
    print("1. Restored original sidebar logo")

old_mobile_logo = '<div class="sidebar-brand-badge py-1 px-2" style="border-radius: 8px;"><img src="img/aictech_logo.png" alt="AICTECH Logo" style="max-height: 30px;"></div>'
new_mobile_logo = '<img src="img/aictech_logo.png" alt="AICTECH Logo" style="max-height: 35px;">'
if old_mobile_logo in text:
    text = text.replace(old_mobile_logo, new_mobile_logo, 1)
    print("1b. Restored original mobile logo")

# ------------------------------------------------------------------------------
# 2. REMOVE BLUE BLOCKS FROM SERVICE CARD BACKS (Point 12)
# ------------------------------------------------------------------------------
blue_badges_pattern = r'\s*<span class="badge bg-primary bg-opacity-10 text-primary px-2 py-1"[^>]*>.*?</span>'
count_blue_badges = len(re.findall(blue_badges_pattern, text))
text = re.sub(blue_badges_pattern, '', text)
print(f"2. Removed {count_blue_badges} blue badges from card backs")

# ------------------------------------------------------------------------------
# 3. FIX HERO VIDEO OBJECT-FIT COVER (Points 13 & 14)
# ------------------------------------------------------------------------------
text = text.replace('object-fit: contain;', 'object-fit: cover !important;')
print("3. Fixed hero-video-bg object-fit to cover")

# ------------------------------------------------------------------------------
# 4. UPDATE SIDEBAR NAVIGATION FOR PRODUCTOS WITH EMERSON ACCORDION (Point 1)
# ------------------------------------------------------------------------------
old_nav_start = text.find('<div class="sidebar-item-group" id="productos-nav-group">')
old_nav_end = text.find('<!-- 2. SERVICIOS', old_nav_start)

new_nav_productos = """<div class="sidebar-item-group" id="productos-nav-group">
                <a href="#0" class="list-group-item list-group-item-action bg-transparent text-white fw-bold py-3 px-4 d-flex align-items-center nav-link" data-no="5" id="nav-link-productos">
                    <i class="fas fa-boxes me-3 fs-5"></i>
                    <span>Productos</span>
                    <i class="fas fa-chevron-down ms-auto submenu-chevron" id="productos-chevron"></i>
                </a>

                <!-- Submenú desplegable de Marcas organizado por Emerson y marcas independientes -->
                <div class="sidebar-submenu" id="productos-submenu">
                    <!-- ACORDEÓN / ABANICO EMERSON -->
                    <div class="sidebar-nested-group">
                        <a href="#producto-brand-emerson" class="submenu-link submenu-nested-header d-flex align-items-center justify-content-between py-2" data-target="producto-brand-emerson" id="emerson-nested-toggle" title="Desplegar marcas Emerson">
                            <span class="d-flex align-items-center">
                                <span class="submenu-dot" style="background: #38bdf8;"></span>
                                <strong class="submenu-text" style="color: #38bdf8; letter-spacing: 0.5px;">EMERSON</strong>
                            </span>
                            <i class="fas fa-chevron-down nested-chevron small text-info" id="emerson-chevron"></i>
                        </a>
                        <div class="sidebar-nested-submenu ps-3" id="emerson-nested-menu">
                            <a href="#producto-brand-roxar" class="submenu-link py-1" data-target="producto-brand-roxar">
                                <span class="submenu-dot"></span>
                                <span class="submenu-text">Roxar</span>
                            </a>
                            <a href="#producto-brand-rosemount" class="submenu-link py-1" data-target="producto-brand-rosemount">
                                <span class="submenu-dot"></span>
                                <span class="submenu-text">Rosemount</span>
                            </a>
                            <a href="#producto-brand-micromotion" class="submenu-link py-1" data-target="producto-brand-micromotion">
                                <span class="submenu-dot"></span>
                                <span class="submenu-text">Micro Motion</span>
                            </a>
                            <a href="#producto-brand-flexim" class="submenu-link py-1" data-target="producto-brand-flexim">
                                <span class="submenu-dot"></span>
                                <span class="submenu-text">Flexim</span>
                            </a>
                            <a href="#producto-brand-amstrex" class="submenu-link py-1" data-target="producto-brand-amstrex">
                                <span class="submenu-dot"></span>
                                <span class="submenu-text">AMS Trex</span>
                            </a>
                        </div>
                    </div>

                    <!-- MARCAS INDEPENDIENTES FUERA DE EMERSON -->
                    <a href="#producto-brand-fluenta" class="submenu-link" data-target="producto-brand-fluenta">
                        <span class="submenu-dot"></span>
                        <span class="submenu-text">Fluenta</span>
                    </a>
                    <a href="#producto-brand-kam" class="submenu-link" data-target="producto-brand-kam">
                        <span class="submenu-dot"></span>
                        <span class="submenu-text">Kam Controls</span>
                    </a>
                </div>
            </div>

            """

if old_nav_start != -1 and old_nav_end != -1:
    text = text[:old_nav_start] + new_nav_productos + text[old_nav_end:]
    print("4. Updated sidebar navigation for Productos with Emerson accordion")

# ------------------------------------------------------------------------------
# 5. REPLACE SECTION 5 (PRODUCTOS) COMPLETELY (Points 1, 2, 3, 4, 5, 6, 7, 8, 9, 11)
# ------------------------------------------------------------------------------
with open('scratch/generated_section5.html', 'r', encoding='utf-8') as f:
    new_section5_html = f.read()

p5_start = text.find('<li data-page-no="5"')
p6_start = text.find('<li data-page-no="6"', p5_start)

if p5_start != -1 and p6_start != -1:
    text = text[:p5_start] + new_section5_html + text[p6_start:]
    print("5. Replaced Section 5 completely with new Emerson, Fluenta, and Kam catalog")

# ------------------------------------------------------------------------------
# 6. INJECT CSS FOR EMERSON PRODUCTS AND PLAYFUL HOVER (Point 2)
# ------------------------------------------------------------------------------
catalog_css = """
        /* ==========================================================================
           PRODUCTOS POR MARCA & INTERACCIÓN LÚDICA ESTILO EMERSON
           ========================================================================== */
        .emerson-products-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
            margin-top: 1.5rem;
        }
        @media (max-width: 768px) {
            .emerson-products-grid {
                grid-template-columns: 1fr;
            }
        }

        .emerson-product-card {
            background: #ffffff;
            border-radius: 14px;
            border: 1px solid rgba(226, 232, 240, 0.95);
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease;
        }
        .emerson-product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.12);
            border-color: rgba(56, 182, 255, 0.5);
        }

        .product-card-media-wrapper {
            position: relative;
            background: #f8fafc;
            border-bottom: 1px solid #f1f5f9;
            padding: 24px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 250px;
            cursor: pointer;
            overflow: hidden;
        }

        /* EFECTO EMERSON DIVERTIDO: LA IMAGEN SE COMPRIME/ACHICA SUAVEMENTE AL PASAR EL CURSOR */
        .product-card-media-wrapper .emerson-product-img {
            max-height: 200px;
            max-width: 90%;
            object-fit: contain;
            transition: transform 0.32s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.3s ease;
            filter: drop-shadow(0 6px 14px rgba(0, 0, 0, 0.08));
            will-change: transform;
        }
        .emerson-product-card:hover .product-card-media-wrapper .emerson-product-img,
        .product-card-media-wrapper:hover .emerson-product-img {
            transform: scale(0.88); /* Achicado lúdico */
            filter: drop-shadow(0 8px 20px rgba(2, 132, 199, 0.22));
        }
        .product-card-media-wrapper:active .emerson-product-img {
            transform: scale(0.82);
        }

        .product-expand-badge {
            position: absolute;
            top: 12px;
            right: 12px;
            background: rgba(2, 10, 26, 0.72);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            cursor: pointer;
            backdrop-filter: blur(4px);
            transition: all 0.25s ease;
            z-index: 5;
            opacity: 0.85;
        }
        .product-card-media-wrapper:hover .product-expand-badge {
            opacity: 1;
            background: #0284c7;
            border-color: #38bdf8;
            transform: scale(1.08);
        }

        .product-card-body {
            padding: 22px 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .product-category-tag {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #0284c7;
            margin-bottom: 6px;
            display: inline-block;
        }

        .product-card-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #0b192c;
            margin-bottom: 10px;
            line-height: 1.35;
        }

        .product-card-desc {
            font-size: 0.88rem;
            line-height: 1.6;
            color: #64748b;
            margin-bottom: 16px;
        }

        .emerson-details-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: #f1f5f9;
            color: #0369a1;
            font-weight: 700;
            font-size: 0.86rem;
            padding: 10px 18px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            text-decoration: none;
            transition: all 0.25s ease;
            width: 100%;
        }
        .emerson-details-btn:hover {
            background: #0284c7;
            color: #ffffff;
            border-color: #0284c7;
            box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);
            transform: translateY(-1px);
        }

        /* TARJETA DESTACADA GRANDE (PARA PRODUCTOS ÚNICOS) */
        .featured-product-card-large {
            background: #ffffff;
            border-radius: 16px;
            border: 1px solid rgba(226, 232, 240, 0.95);
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            margin-top: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .featured-product-card-large:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.12);
        }

        /* ESTILOS DEL SUBMENÚ ANIDADO DE EMERSON EN EL SIDEBAR */
        .sidebar-nested-submenu {
            border-left: 2px solid rgba(56, 182, 255, 0.3);
            margin-left: 12px;
            margin-top: 4px;
            margin-bottom: 6px;
        }
        .sidebar-nested-header {
            cursor: pointer;
            border-radius: 6px;
            transition: background 0.2s ease;
        }
        .sidebar-nested-header:hover {
            background: rgba(56, 182, 255, 0.12);
        }
"""
text = text.replace('</style>', catalog_css + '\n    </style>', 1)
print("6. Injected catalog CSS")

# ------------------------------------------------------------------------------
# 7. INJECT JS HANDLERS FOR BRAND NAVIGATION & VIDEO PAUSE (Points 1, 13)
# ------------------------------------------------------------------------------
catalog_js = """
        // ==========================================
        // PAUSA GLOBAL DE VIDEOS DE SEGUNDO PLANO
        // ==========================================
        window.pauseAllBackgroundVideos = function(excludeVideo) {
            document.querySelectorAll('video').forEach(function(v) {
                if (v !== excludeVideo && !v.paused) {
                    v.dataset.wasPlaying = 'true';
                    v.pause();
                }
            });
        };

        // ==========================================
        // EXPANDIR FOTOS DE PRODUCTOS EN LIGHTBOX HD
        // ==========================================
        window.expandMediaFromElement = function(elem) {
            if (!elem) return;
            const card = elem.closest('.emerson-product-card') || elem.closest('.featured-product-card-large') || elem.parentElement;
            const img = elem.tagName === 'IMG' ? elem : elem.querySelector('img');
            if (!img) return;

            let title = '';
            if (card) {
                const titleElem = card.querySelector('.product-card-title, h4, h3');
                if (titleElem) title = titleElem.innerText.trim();
            }

            const stage = document.getElementById('media-lightbox-stage');
            const titleNode = document.getElementById('media-lightbox-title');
            const modal = document.getElementById('media-lightbox-modal');
            if (!stage || !modal) return;

            // Pausar cualquier video activo
            window.pauseAllBackgroundVideos();

            stage.innerHTML = '';
            const newImg = document.createElement('img');
            newImg.src = img.src;
            newImg.alt = title || img.alt || 'Producto en Alta Resolución';
            stage.appendChild(newImg);
            if (titleNode) titleNode.textContent = title || img.alt || 'Visualización en Alta Resolución';
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        };

        // ==========================================
        // NAVEGACIÓN INTERACTIVA DEL CATÁLOGO POR MARCA
        // ==========================================
        $(document).on('click', '#emerson-nested-toggle', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const nestedMenu = document.getElementById('emerson-nested-menu');
            const chevron = document.getElementById('emerson-chevron');
            if (nestedMenu) {
                const isHidden = $(nestedMenu).is(':hidden');
                $(nestedMenu).slideToggle(200);
                if (chevron) {
                    chevron.classList.toggle('fa-chevron-down', !isHidden);
                    chevron.classList.toggle('fa-chevron-up', isHidden);
                }
            }
            
            // Navegar a página 5 si no estamos en ella
            const activePage = document.querySelector('.cd-hero-slider > li.selected');
            const currentPageNo = activePage ? activePage.getAttribute('data-page-no') : null;
            if (currentPageNo !== '5') {
                if (typeof openPage === 'function') openPage(5);
                if (typeof highlightMenu === 'function') highlightMenu(5);
            }
            setTimeout(function() {
                const targetElem = document.getElementById('producto-brand-emerson');
                if (targetElem) targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 260);
        });

        $(document).on('click', '#productos-submenu a[data-target]', function(e) {
            if ($(this).attr('id') === 'emerson-nested-toggle') return;
            e.preventDefault();
            const targetId = $(this).attr('data-target');

            const activePage = document.querySelector('.cd-hero-slider > li.selected');
            const currentPageNo = activePage ? activePage.getAttribute('data-page-no') : null;
            if (currentPageNo !== '5') {
                if (typeof openPage === 'function') openPage(5);
                if (typeof highlightMenu === 'function') highlightMenu(5);
            }

            // Marcar enlace activo
            $('#productos-submenu a').removeClass('active');
            $(this).addClass('active');

            setTimeout(function() {
                const targetElem = document.getElementById(targetId);
                if (targetElem) {
                    targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, 280);
        });
"""

idx_script_end = text.rfind('</script>')
if idx_script_end != -1:
    text = text[:idx_script_end] + catalog_js + '\n' + text[idx_script_end:]
    print("7. Injected catalog JS handlers")

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

final_len = len(text)
print(f"Final index.html length: {final_len} bytes, lines: {text.count(chr(10))}")
print("DIFF in bytes:", final_len - initial_len)
