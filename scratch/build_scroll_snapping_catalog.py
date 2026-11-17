# -*- coding: utf-8 -*-
"""
build_scroll_snapping_catalog.py
Generates the Webflow-inspired Scroll Snapping Cards for Section 5 (Productos).
Order inside Emerson:
1. Roxar
2. Flexim
3. AMS Trex
4. Rosemount
5. Micro Motion
Outside Emerson:
6. Fluenta
7. Kam Controls
"""

def generate_section5():
    brands = [
        {
            'id': 'producto-brand-roxar',
            'name': 'ROXAR™',
            'color': '#7c3aed',
            'soft_bg': 'rgba(124, 58, 237, 0.06)',
            'border_color': 'rgba(124, 58, 237, 0.25)',
            'logo': 'img/products/roxar/roxar.png',
            'logo_scale': 'scale(1.15)',
            'title': 'Medidores Multifásicos y Analizadores Subsea & Topside',
            'desc': 'Líder global en caracterización de flujo multifásico en tiempo real en boca de pozo. Medición cuantitativa continua de petróleo, agua y gas sin separación física ni paradas operativas.',
            'specs': [
                'Medición continua multifásica en tiempo real (Petróleo, Agua, Gas)',
                'Tecnología de microondas y rayos gamma para corte de agua de alta precisión',
                'Modelos Topside para tierra/mar y Subsea con confiabilidad calificada de 25 años',
                'Certificaciones ATEX, IECEx, SIL 2 / SIL 3 para áreas clasificadas'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/roxar-2600',
            'catalog_text': 'Ver Catálogo Roxar en Emerson',
            'products': [
                {
                    'title': 'Roxar™ 2600 Multiphase Flow Meters',
                    'cat': 'Multiphase Measurement',
                    'desc': 'Medidor multifásico líder de la industria para caracterización cuantitativa continua en cabeza de pozo.',
                    'img': 'img/products/roxar/2600.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-2600'
                },
                {
                    'title': 'Roxar™ Watercut Meter',
                    'cat': 'Water-in-Oil Analyzer',
                    'desc': 'Medidor de corte de agua full-bore de alta precisión basado en resonancia de microondas.',
                    'img': 'img/products/roxar/water-cut-meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-watercut-meter'
                },
                {
                    'title': 'Roxar™ Subsea Multiphase Flow Meter',
                    'cat': 'Deepwater & Subsea',
                    'desc': 'Medición multifásica de última generación para desarrollos submarinos de alta presión.',
                    'img': 'img/products/roxar/Multifasico-para-instalaciones-SubSea.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-subsea-multiphase-flow-meter'
                },
                {
                    'title': 'Roxar™ Subsea Wetgas Meters',
                    'cat': 'Wetgas Reservoir Management',
                    'desc': 'Detección temprana y ultra precisa de agua de condensación y agua de formación en pozos de gas.',
                    'img': 'img/products/roxar/Medidor de Wet Gas SubSea.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-subsea-wetgas-meter'
                },
                {
                    'title': 'Roxar™ Multiphase Salinity System',
                    'cat': 'Real-time Salinity Sensor',
                    'desc': 'Sensor de salinidad dedicado en línea para monitoreo de intrusión de acuífero y optimización química.',
                    'img': 'img/products/roxar/Medidor de Salinidad (Complemento del 2600).jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-multiphase-salinity-system'
                }
            ]
        },
        {
            'id': 'producto-brand-flexim',
            'name': 'FLEXIM™',
            'color': '#0d9488',
            'soft_bg': 'rgba(13, 148, 136, 0.06)',
            'border_color': 'rgba(13, 148, 136, 0.25)',
            'logo': 'img/products/flexim/Flexim-Logo.png',
            'logo_scale': 'scale(1.05)',
            'title': 'Medidores Ultrasónicos Clamp-On No Invasivos',
            'desc': 'Tecnología ultrasónica pionera de sujeción exterior (clamp-on). Aforo preciso de líquidos y gases en condiciones operativas extremas sin cortar la tubería, sin paradas de proceso y con cero caída de presión.',
            'specs': [
                'Instalación 100% no invasiva en pared exterior sin interrupción de flujo',
                'Apto para hidrocarburos pesados, vapor, gas natural comprimido y químicos',
                'Rango de tuberías desde 1/2 pulgada hasta más de 100 pulgadas',
                'Homologado para zonas explosivas Clase I Div 1 / Div 2 y ATEX Zona 1'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/flexim-fluxus-f631',
            'catalog_text': 'Ver Catálogo Flexim en Emerson',
            'products': [
                {
                    'title': 'FLUXUS® F631 BA - Caudalímetro Portátil para Líquidos',
                    'cat': 'Portable Ultrasonic Flow Meter',
                    'desc': 'Equipo portátil de alta autonomía para auditorías, verificación de medidores fiscales y pruebas temporales en campo.',
                    'img': 'img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/flexim-fluxus-f631'
                },
                {
                    'title': 'FLUXUS® F721 - Medición Permanente de Alto Rendimiento',
                    'cat': 'Stationary Flow Meter',
                    'desc': 'Transmisor estacionario de doble canal para aforo continuo de líquidos corrosivos, crudos y gasoductos.',
                    'img': 'img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/flexim-fluxus-f721'
                }
            ]
        },
        {
            'id': 'producto-brand-amstrex',
            'name': 'AMS TREX™',
            'color': '#1e293b',
            'soft_bg': 'rgba(30, 41, 59, 0.06)',
            'border_color': 'rgba(30, 41, 59, 0.25)',
            'logo': 'img/products/ams trex/ams-trex-banner.jpg',
            'logo_scale': 'scale(1.0)',
            'is_photo_logo': True,
            'title': 'Comunicador de Dispositivos y Calibrador Inteligente de Campo',
            'desc': 'El estándar mundial definitivo en mantenimiento, configuración y puesta en marcha de instrumentación inteligente. Energiza lazos de corriente directamente en campo sin requerir fuentes de poder auxiliares.',
            'specs': [
                'Pantalla táctil resistiva a color de 5.7" operable con guantes industriales',
                'Función Power the Loop para alimentar transmisores en banco o en campo',
                'Soporte completo para protocolos HART y Foundation Fieldbus',
                'Certificación Intrínsecamente Segura (IS) para Clase I Div 1 y ATEX Zona 0'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/ams-trex',
            'catalog_text': 'Ver Catálogo AMS Trex en Emerson',
            'products': [
                {
                    'title': 'AMS Trex™ Device Communicator (Edición Galardonada)',
                    'cat': 'Field Maintenance & Diagnostics',
                    'desc': 'Comunicador robusto para configuración rápida, diagnóstico de válvulas y resolución de problemas en sitio.',
                    'img': 'img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/ams-trex'
                }
            ]
        },
        {
            'id': 'producto-brand-rosemount',
            'name': 'ROSEMOUNT™',
            'color': '#004b87',
            'soft_bg': 'rgba(0, 75, 135, 0.06)',
            'border_color': 'rgba(0, 75, 135, 0.25)',
            'logo': 'img/products/rosemount/Rosemount-New-Logo.png',
            'logo_scale': 'scale(1.25)',
            'title': 'Medición de Caudal Vortex y Nivel por Radar de Onda Guiada',
            'desc': 'Instrumentación de proceso de referencia mundial. Medidores de caudal vortex sin juntas para máxima contención de fugas y transmisores de nivel por radar de onda guiada para tanques y separadores críticos.',
            'specs': [
                'Caudalímetros Vortex 8800 sin puertos ni sellos propensos a obstrucciones',
                'Diseño Reducer integrado que ahorra costos de tuberías y conexiones bridadas',
                'Radares 5300 con tecnología Direct Switch para constante dieléctrica ultra baja',
                'Diseñados según normas SIL 2 y SIL 3 con verificación de salud del sensor'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/rosemount-8800',
            'catalog_text': 'Ver Catálogo Rosemount en Emerson',
            'products': [
                {
                    'title': 'Rosemount™ 8800 Reducer Vortex Flow Meter',
                    'cat': 'Vortex Flow Measurement',
                    'desc': 'Medidor vortex con reducción de diámetro integrada para ampliar el rango de medición sin reducciones externas.',
                    'img': 'img/products/rosemount/Rosemount™ 8800 Reducer Vortex Flow Meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-8800'
                },
                {
                    'title': 'Rosemount™ 8600 Vortex Flow Meters',
                    'cat': 'Utility & Process Vortex',
                    'desc': 'Solución compacta y confiable para servicios generales, vapor saturado y fluidos industriales limpios.',
                    'img': 'img/products/rosemount/Rosemount™ 8600 Vortex Flow Meters.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-8600'
                },
                {
                    'title': 'Rosemount™ 5300 Level Transmitter (Radar de Onda Guiada)',
                    'cat': 'Guided Wave Radar Level',
                    'desc': 'Transmisor de nivel e interfase líder para separadores bifásicos/trifásicos y recipientes a alta presión.',
                    'img': 'img/products/rosemount/Rosemount™ 5300 Level Transmitter - Guided Wave Radar.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-5300'
                },
                {
                    'title': 'Transmisor de Nivel Rosemount 5300 con Sonda Coaxial',
                    'cat': 'Liquid & Interface Measurement',
                    'desc': 'Sonda coaxial de alto rendimiento para mediciones estables en líquidos de baja constante dieléctrica y turbulencia.',
                    'img': 'img/products/rosemount/Transmisor de nivel Rosemount 5300 - Radar de onda guiada.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-5300'
                }
            ]
        },
        {
            'id': 'producto-brand-micromotion',
            'name': 'MICRO MOTION™',
            'color': '#475569',
            'soft_bg': 'rgba(71, 85, 105, 0.06)',
            'border_color': 'rgba(71, 85, 105, 0.25)',
            'logo': 'img/products/micromotion/micromotion.png',
            'logo_scale': 'scale(1.70)',
            'title': 'Caudalímetros Másicos Coriolis y Densímetros de Precisión',
            'desc': 'La máxima referencia mundial en medición másica Coriolis directa y transferencia de custodia fiscal (LACT). Medición simultánea de flujo másico, flujo volumétrico, densidad y temperatura con precisión insuperable.',
            'specs': [
                'Precisión fiscal de hasta ±0.05% en caudal másico de líquidos y crudos',
                'Smart Meter Verification™ en línea para certificar el medidor en menos de 90 segundos',
                'Transmisor 5700 con pantalla gráfica, registro de datos y diagnósticos avanzados',
                'Aprobaciones fiscales internacionales OIML R117, API MPMS y MID'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/micro-motion-5700',
            'catalog_text': 'Ver Catálogo Micro Motion en Emerson',
            'products': [
                {
                    'title': 'Micro Motion™ 5700 Field-Mount Transmitter',
                    'cat': 'Coriolis Mass Flow & Density',
                    'desc': 'Transmisor de tecnología Coriolis de vanguardia con verificación inteligente del tubo sensor sin detener el flujo.',
                    'img': 'img/products/micromotion/Micro Motion™ 5700 Field-Mount Transmitter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/micro-motion-5700'
                }
            ]
        },
        {
            'id': 'producto-brand-fluenta',
            'name': 'FLUENTA',
            'color': '#16a34a',
            'soft_bg': 'rgba(22, 163, 74, 0.06)',
            'border_color': 'rgba(22, 163, 74, 0.25)',
            'logo': 'img/products/fluenta/Fluenta-blog-logo.png',
            'logo_scale': 'scale(1.35)',
            'title': 'Medición Ultrasónica de Gas de Antorcha (Flare Gas) y Emisiones',
            'desc': 'Líder mundial indiscutido en medición ultrasónica de gas de alivio, antorchas y venteos. Soluciones de tiempo de tránsito para monitoreo ambiental estricto, balances de planta y reducción de huella de carbono.',
            'specs': [
                'Medición en amplio rango dinámico con velocidades desde 0.03 m/s hasta más de 100 m/s',
                'Transductores piezoeléctricos de titanio TFS con aislamiento acústico patentado',
                'Configuraciones mono-trayectoria y doble trayectoria para optimizar la precisión',
                'Cumplimiento de normativas ambientales internacionales EPA 40 CFR 60 / EU ETS'
            ],
            'catalog_link': 'https://www.fluenta.com/products/',
            'catalog_text': 'Ver Catálogo Oficial Fluenta',
            'products': [
                {
                    'title': 'Fluenta TFS Ultrasonic Transducers',
                    'cat': 'Flare Gas Transducers',
                    'desc': 'Transductores ultrasónicos de titanio capaces de operar en gases corrosivos y temperaturas extremas.',
                    'img': 'img/products/fluenta/Fluenta TFS Ultrasonic Transducers.jpeg',
                    'link': 'https://www.fluenta.com/products/tfs/'
                },
                {
                    'title': 'FlarePhase 250 & 350 Transducers',
                    'cat': 'High-Velocity Sensors',
                    'desc': 'Transductores de última generación para tuberías de gran diámetro y condiciones de antorcha severas.',
                    'img': 'img/products/fluenta/FlarePhase 250.jpeg',
                    'link': 'https://www.fluenta.com/products/flarephase/'
                },
                {
                    'title': 'Dual-Path Flow Configurations',
                    'cat': 'Fiscal & Environmental Setup',
                    'desc': 'Arquitectura de doble haz acústico para verificación cruzada de flujo y máxima certidumbre metrológica.',
                    'img': 'img/products/fluenta/Dual-Path Configurations.jpeg',
                    'link': 'https://www.fluenta.com/products/'
                },
                {
                    'title': 'Single-Path Flow Configurations',
                    'cat': 'Compact Flare Metering',
                    'desc': 'Instalación económica y robusta para líneas de antorcha secundarias y plantas de procesamiento.',
                    'img': 'img/products/fluenta/Single-Path Configurations.jpeg',
                    'link': 'https://www.fluenta.com/products/'
                },
                {
                    'title': 'Fluenta TFS-55 Transducers',
                    'cat': 'Extreme Temperature Range',
                    'desc': 'Transductores de alta frecuencia para condiciones criogénicas de GNL y gases de chimenea calientes.',
                    'img': 'img/products/fluenta/Fluenta TFS-55.jpeg',
                    'link': 'https://www.fluenta.com/products/tfs-55/'
                }
            ]
        },
        {
            'id': 'producto-brand-kam',
            'name': 'KAM CONTROLS',
            'color': '#ea580c',
            'soft_bg': 'rgba(234, 88, 12, 0.06)',
            'border_color': 'rgba(234, 88, 12, 0.25)',
            'logo': 'img/products/kam/kam_logo.png',
            'logo_scale': 'scale(0.75)',
            'title': 'Analizadores de Crudo, Corte de Agua (OWD) y Muestreadores',
            'desc': 'Especialistas reconocidos en instrumentación analítica y muestreo automático isocinético para transferencia de custodia fiscal, terminales de almacenamiento, oleoductos y deshidratación de tanques.',
            'specs': [
                'Medidores de corte de agua OWD por microondas con exactitud de ±0.03% en crudo',
                'Muestreadores automáticos isocinéticos API 8.2 e ISO 3171 para crudo y condensados',
                'Sistemas de purga automática de agua en tanques (ATD) para evitar pérdidas de producto',
                'Analizador Karl Fischer KF para determinación de agua en ppm en laboratorio y campo'
            ],
            'catalog_link': 'https://kam.com/products/',
            'catalog_text': 'Ver Catálogo Oficial Kam Controls',
            'products': [
                {
                    'title': 'Kam OWD® Optical Watercut Meter',
                    'cat': 'Water-in-Oil Meter',
                    'desc': 'El medidor de corte de agua de mayor precisión de la industria en rangos bajos y medios (0-5% y 0-100%).',
                    'img': 'img/products/kam/OWD Watercut Meter.jpeg',
                    'link': 'https://kam.com/products/water-cut-meter/'
                },
                {
                    'title': 'Kam ATD™ Automatic Tank Dewatering System',
                    'cat': 'Tank Drainage Automation',
                    'desc': 'Sistema inteligente que detecta la interfase crudo-agua y drena tanques automáticamente sin derrame.',
                    'img': 'img/products/kam/ATD Automatic Tank Dewatering System.jpeg',
                    'link': 'https://kam.com/products/automatic-tank-dewatering/'
                },
                {
                    'title': 'Kam IAS™ Isokinetic Automatic Sampler',
                    'cat': 'Fiscal Sampling System',
                    'desc': 'Muestreador representativo proporcional al caudal para transferencia de custodia según API MPMS 8.2.',
                    'img': 'img/products/kam/IAS Isokinetic Automatic Sampler.jpeg',
                    'link': 'https://kam.com/products/isokinetic-automatic-sampler/'
                },
                {
                    'title': 'Kam E-IAS™ Electric Isokinetic Sampler',
                    'cat': 'Electric Sampling Technology',
                    'desc': 'Muestreo automático accionado eléctricamente sin necesidad de suministro de aire comprimido.',
                    'img': 'img/products/kam/E-IAS Electric Isokinetic Automatic Sampler.jpeg',
                    'link': 'https://kam.com/products/electric-isokinetic-sampler/'
                },
                {
                    'title': 'Kam KF Karl Fischer Moisture Analyzer',
                    'cat': 'Laboratory & Field Titration',
                    'desc': 'Titulador culombimétrico Karl Fischer de alta portabilidad para cuantificar agua disuelta en crudos.',
                    'img': 'img/products/kam/KF Karl Fischer Moisture Analyzer.jpeg',
                    'link': 'https://kam.com/products/karl-fischer-moisture-analyzer/'
                },
                {
                    'title': 'Kam SMP™ Static Mixing Plate & Spool',
                    'cat': 'Pipeline Flow Conditioning',
                    'desc': 'Placas mezcladoras estáticas diseñadas para homogeneizar crudo y agua antes de la toma de muestra.',
                    'img': 'img/products/kam/SMP Static Mixing Plate.jpeg',
                    'link': 'https://kam.com/products/static-mixing-plate/'
                }
            ]
        }
    ]

    # Generate HTML
    out = []
    out.append("""<!-- SECCIÓN 5: PRODUCTOS & CATÁLOGO POR MARCA (SCROLL SNAPPING CARDS WEBFLOW STYLE) -->
                <li data-page-no="5" class="px-3">
                    <div class="page-width-1 h-100">
                        <div class="catalog-feed-wrapper" id="catalog-scroll-container">

                            <!-- ENCABEZADO INSTITUCIONAL -->
                            <div class="catalog-hero-box reveal-on-scroll reveal-up mb-4" id="producto-brand-emerson">
                                <h1 class="fw-bold display-6 text-dark mb-2">Instrumentos de Medición y Servicios de Ingeniería</h1>
                                <p class="text-muted fs-6 mb-0" style="line-height: 1.7; max-width: 950px;">
                                    <strong>Representantes <span style="color: #0d6efd; font-weight: 800;">EMERSON</span> en <span class="venezuela-flag-text">Venezuela</span></strong><strong>, AIC TECH, C.A.</strong> suministra e integra instrumentación analítica y de medición de flujo para cada punto crítico de la cadena de valor petrolera con las marcas líderes mundiales.
                                </p>
                            </div>
""")

    for b in brands:
        card_id = b['id']
        brand_color = b['color']
        brand_soft = b['soft_bg']
        border_col = b['border_color']
        badge_name = b['name']
        title = b['title']
        desc = b['desc']
        specs_html = "".join([f'<li><i class="fas fa-circle-check me-2" style="color: {brand_color};"></i>{s}</li>' for s in b['specs']])
        cat_link = b['catalog_link']
        cat_text = b['catalog_text']

        # Logo handling
        if b.get('is_photo_logo'):
            logo_html = f'''<div class="brand-panel-logo-wrap rounded-3 shadow-sm overflow-hidden" style="height: 110px; background: #0f172a; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.15);">
                                <img src="{b['logo']}" alt="{badge_name}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 25%; filter: brightness(0.9);">
                            </div>'''
        else:
            logo_html = f'''<div class="brand-panel-logo-wrap rounded-3" style="height: 110px; background: #ffffff; display: flex; align-items: center; justify-content: center; padding: 10px 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid {border_col};">
                                <img src="{b['logo']}" alt="{badge_name}" style="max-height: 85px; max-width: 90%; object-fit: contain; transform: {b['logo_scale']}; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.08));">
                            </div>'''

        # Products showcase (Left Column)
        prod_items_html = []
        is_few_products = len(b['products']) <= 2
        col_class = "col-12" if is_few_products else "col-12 col-md-6"

        for p in b['products']:
            img_height = "220px" if is_few_products else "160px"
            prod_items_html.append(f'''
                                        <div class="{col_class}">
                                            <div class="emerson-product-card h-100">
                                                <div class="product-card-media-wrapper" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="height: {img_height};">
                                                    <button type="button" class="product-expand-badge" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="{p['img']}" alt="{p['title']}" class="emerson-product-img">
                                                </div>
                                                <div class="product-card-body p-3 d-flex flex-column justify-content-between">
                                                    <div>
                                                        <span class="product-category-tag mb-1" style="font-size: 0.72rem; color: {brand_color}; font-weight: 700;">{p['cat']}</span>
                                                        <h5 class="product-card-title fs-6 mb-2 fw-bold text-dark">{p['title']}</h5>
                                                        <p class="product-card-desc small text-muted mb-3" style="font-size: 0.82rem; line-height: 1.5;">{p['desc']}</p>
                                                    </div>
                                                    <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="emerson-details-btn mt-auto" onclick="event.stopPropagation();">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>''')

        products_grid_html = "".join(prod_items_html)

        card_html = f'''
                            <!-- ========================================================
                                 BRAND SNAP CARD: {badge_name}
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5" id="{card_id}">
                                <div class="brand-snapping-card-inner rounded-4 overflow-hidden shadow-lg" style="border: 1px solid {border_col}; background: #ffffff;">
                                    <div class="row g-0 align-items-stretch">
                                        
                                        <!-- IZQUIERDA: SHOWCASE DE PRODUCTOS (FOTOS Y ESPECIFICACIONES) -->
                                        <div class="col-12 col-xl-7 p-3 p-lg-4 card-showcase-column" style="background: #f8fafc; border-right: 1px solid rgba(226, 232, 240, 0.9);">
                                            <div class="d-flex justify-content-between align-items-center mb-3 pb-2 border-bottom border-light-subtle">
                                                <div class="d-flex align-items-center gap-2">
                                                    <span class="badge px-3 py-1 fw-bold fs-6" style="background: {brand_color}; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 2px 8px {border_col};">{badge_name}</span>
                                                    <span class="text-secondary small fw-semibold">Portafolio Especializado</span>
                                                </div>
                                                <span class="badge bg-white text-secondary border px-2 py-1 small"><i class="fas fa-layer-group me-1"></i> {len(b['products'])} Modelos</span>
                                            </div>

                                            <div class="showcase-scroll-gallery" style="max-height: 600px; overflow-y: auto; padding-right: 6px;">
                                                <div class="row g-3">
                                                    {products_grid_html}
                                                </div>
                                            </div>
                                        </div>

                                        <!-- DERECHA: PANEL DE IDENTIDAD DE MARCA CON LOGO Y ESPECIFICACIONES -->
                                        <div class="col-12 col-xl-5 p-4 d-flex flex-column justify-content-between card-brand-column" style="background: linear-gradient(150deg, #ffffff 0%, {brand_soft} 100%);">
                                            <div>
                                                <!-- Logotipo de la marca -->
                                                <div class="mb-4">
                                                    {logo_html}
                                                </div>

                                                <h3 class="fw-bold fs-4 text-dark mb-2" style="line-height: 1.3;">{title}</h3>
                                                <p class="text-secondary small mb-4" style="line-height: 1.65; font-size: 0.92rem;">{desc}</p>

                                                <div class="brand-card-specs-box p-3 rounded-3 mb-4" style="background: #ffffff; border: 1px solid {border_col}; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
                                                    <h6 class="fw-bold text-uppercase small mb-2" style="color: {brand_color}; letter-spacing: 0.6px;"><i class="fas fa-shield-halved me-1"></i> Capacidades de Alto Rendimiento:</h6>
                                                    <ul class="list-unstyled mb-0 small text-secondary d-flex flex-column gap-2" style="font-size: 0.85rem; line-height: 1.5;">
                                                        {specs_html}
                                                    </ul>
                                                </div>
                                            </div>

                                            <div class="pt-2 border-top">
                                                <a href="{cat_link}" target="_blank" rel="noopener noreferrer" class="btn w-100 py-2 fw-bold text-white d-flex align-items-center justify-content-center gap-2 rounded-3 shadow-sm" style="background: {brand_color}; transition: all 0.25s ease;" onmouseover="this.style.opacity='0.9'; this.style.transform='translateY(-2px)';" onmouseout="this.style.opacity='1'; this.style.transform='none';">
                                                    <span>{cat_text}</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                                </a>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>'''
        out.append(card_html)

    out.append("""                        </div>
                    </div>
                </li>
""")
    return "\n".join(out)

if __name__ == '__main__':
    res = generate_section5()
    with open('scratch/generated_section5_cards.html', 'w', encoding='utf-8') as f:
        f.write(res)
    print("Generated Scroll Snapping Cards Section 5! Length:", len(res))
