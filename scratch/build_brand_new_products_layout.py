# -*- coding: utf-8 -*-
"""
build_brand_new_products_layout.py
Generates the new Products layout requested:
1. Multi-product brands (Roxar, Rosemount, Fluenta, Kam Controls):
   - 1 Large Card on the left (with category, title, description, link)
   - Compact cards pegaditos on the right (2x2 / 2x3 grid, blur bar, title only)
   - Zero bulky sidebars / bullet points (everything in red from Photo 2 removed)
2. Single-product brands (Flexim, AMS Trex, Micro Motion):
   - Interactive 3D Flip 360 Double Gatefold Envelope Card (Photo 3 + code provided)
"""

def generate_section5_final():
    brands = [
        # 1. ROXAR
        {
            'id': 'producto-brand-roxar',
            'name': 'ROXAR™',
            'color': '#a855f7',
            'rgb': '168, 85, 247',
            'logo': 'img/products/roxar/roxar.png',
            'logo_scale': 'scale(1.15)',
            'catalog_link': 'https://www.emerson.com/es-es/catalog/roxar-2600',
            'catalog_text': 'Catálogo Roxar en Emerson',
            'is_single': False,
            'products': [
                {
                    'title': 'Roxar™ 2600 Multiphase Flow Meters',
                    'cat': 'Multiphase Measurement',
                    'desc': 'Medidor multifásico líder de la industria para caracterización cuantitativa continua en cabeza de pozo sin separación física.',
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
                    'title': 'Roxar™ Subsea Wetgas Meters',
                    'cat': 'Wetgas Reservoir Management',
                    'desc': 'Detección temprana y ultra precisa de agua de condensación y formación en pozos de gas.',
                    'img': 'img/products/roxar/Medidor de Wet Gas SubSea.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-subsea-wetgas-meter'
                },
                {
                    'title': 'Roxar™ Subsea Multiphase Flow Meter',
                    'cat': 'Deepwater & Subsea',
                    'desc': 'Medición multifásica de última generación para desarrollos submarinos de alta presión.',
                    'img': 'img/products/roxar/Multifasico-para-instalaciones-SubSea.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/roxar-subsea-multiphase-flow-meter'
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

        # 2. FLEXIM (SINGLE PRODUCT -> FLIP 360 ENVELOPE)
        {
            'id': 'producto-brand-flexim',
            'name': 'FLEXIM™',
            'color': '#14b8a6',
            'rgb': '20, 184, 166',
            'logo': 'img/products/flexim/Flexim-Logo.png',
            'logo_scale': 'scale(1.05)',
            'catalog_link': 'https://www.emerson.com/es-es/catalog/flexim-fluxus-f631',
            'catalog_text': 'Catálogo Flexim en Emerson',
            'is_single': True,
            'product': {
                'title': 'FLUXUS® F631 BA - Caudalímetro Portátil para Líquidos',
                'cat': 'Clamp-On Ultrasonic Flow Meter',
                'desc': 'Medidor de flujo ultrasónico portátil no invasivo clamp-on para líquidos y gases sin cortes de tubería ni paradas operativas.',
                'img': 'img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg',
                'link': 'https://www.emerson.com/es-es/catalog/flexim-fluxus-f631'
            }
        },

        # 3. AMS TREX (SINGLE PRODUCT -> FLIP 360 ENVELOPE)
        {
            'id': 'producto-brand-amstrex',
            'name': 'AMS TREX™',
            'color': '#94a3b8',
            'rgb': '148, 163, 184',
            'logo': 'img/products/ams trex/ams-trex-banner.jpg',
            'logo_scale': 'scale(1.0)',
            'catalog_link': 'https://www.emerson.com/es-es/catalog/ams-trex-device-communicator',
            'catalog_text': 'Catálogo AMS Trex en Emerson',
            'is_single': True,
            'product': {
                'title': 'AMS Trex™ Device Communicator',
                'cat': 'Intrinsically Safe Field Communicator',
                'desc': 'Comunicador de campo robusto con certificación de seguridad intrínseca (IS) para configuración y diagnóstico HART y Foundation Fieldbus en áreas clasificadas.',
                'img': 'img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg',
                'link': 'https://www.emerson.com/es-es/catalog/ams-trex-device-communicator'
            }
        },

        # 4. ROSEMOUNT
        {
            'id': 'producto-brand-rosemount',
            'name': 'ROSEMOUNT™',
            'color': '#38bdf8',
            'rgb': '56, 189, 248',
            'logo': 'img/products/rosemount/Rosemount-New-Logo.png',
            'logo_scale': 'scale(1.1)',
            'catalog_link': 'https://www.emerson.com/es-es/catalog/rosemount-5300',
            'catalog_text': 'Catálogo Rosemount en Emerson',
            'is_single': False,
            'products': [
                {
                    'title': 'Rosemount™ 5300 Level Transmitter - Guided Wave Radar',
                    'cat': 'Guided Wave Radar Level',
                    'desc': 'Radar de nivel por onda guiada para medición precisa de interfase y nivel total en tanques y separadores de proceso.',
                    'img': 'img/products/rosemount/Rosemount™ 5300 Level Transmitter - Guided Wave Radar.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-5300'
                },
                {
                    'title': 'Rosemount™ 8800 Reducer Vortex Flow Meter',
                    'cat': 'Reducer Vortex Meter',
                    'desc': 'Medidor vortex con reductor integrado para ampliar el rango de medición de caudal.',
                    'img': 'img/products/rosemount/Rosemount™ 8800 Reducer Vortex Flow Meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-8800'
                },
                {
                    'title': 'Rosemount™ 8600 Vortex Flow Meters',
                    'cat': 'Process Vortex Meter',
                    'desc': 'Medición confiable de caudal de vapor, gas y líquidos limpios.',
                    'img': 'img/products/rosemount/Rosemount™ 8600 Vortex Flow Meters.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-8600'
                },
                {
                    'title': 'Transmisor de Nivel Rosemount 5300 de Alta Presión',
                    'cat': 'High Pressure / Temp Radar',
                    'desc': 'Versión reforzada para recipientes de proceso sometidos a alta presión extrema.',
                    'img': 'img/products/rosemount/Transmisor de nivel Rosemount 5300 - Radar de onda guiada.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-5300'
                }
            ]
        },

        # 5. MICRO MOTION (SINGLE PRODUCT -> FLIP 360 ENVELOPE)
        {
            'id': 'producto-brand-micromotion',
            'name': 'MICRO MOTION™',
            'color': '#cbd5e1',
            'rgb': '203, 213, 225',
            'logo': 'img/products/micromotion/micromotion.png',
            'logo_scale': 'scale(1.15)',
            'catalog_link': 'https://www.emerson.com/es-es/catalog/micro-motion-5700-field-mount-transmitter',
            'catalog_text': 'Catálogo Micro Motion en Emerson',
            'is_single': True,
            'product': {
                'title': 'Micro Motion™ 5700 Field-Mount Transmitter',
                'cat': 'Coriolis Flow & Density Transmitter',
                'desc': 'Transmisor Coriolis avanzado de montaje en campo con tecnología MVD, diagnóstico de integridad y verificación de calibración en línea en 90 segundos.',
                'img': 'img/products/micromotion/Micro Motion™ 5700 Field-Mount Transmitter.jpeg',
                'link': 'https://www.emerson.com/es-es/catalog/micro-motion-5700-field-mount-transmitter'
            }
        },

        # 6. FLUENTA
        {
            'id': 'producto-brand-fluenta',
            'name': 'FLUENTA™',
            'color': '#22c55e',
            'rgb': '34, 197, 94',
            'logo': 'img/products/fluenta/Fluenta-blog-logo.png',
            'logo_scale': 'scale(1.1)',
            'catalog_link': 'https://www.fluenta.com',
            'catalog_text': 'Portal Oficial Fluenta',
            'is_single': False,
            'products': [
                {
                    'title': 'Fluenta FlarePhase™ 250 - Sensor de Antorcha',
                    'cat': 'Flare Gas Transducer',
                    'desc': 'Sensor ultrasónico de gas de antorcha para medición de caudal no intrusiva con amplio rango de velocidades.',
                    'img': 'img/products/fluenta/FlarePhase 250.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta FlarePhase™ 350 - Alta Temperatura',
                    'cat': 'High Temp Flare Sensor',
                    'desc': 'Sensor para antorchas de alta temperatura y atmósferas con alto contenido de azufre.',
                    'img': 'img/products/fluenta/FlarePhase 350.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta TFS Ultrasonic Transducers',
                    'cat': 'Acoustic Flare Transducers',
                    'desc': 'Transductores de tecnología acústica para líneas de descarga de antorcha.',
                    'img': 'img/products/fluenta/Fluenta TFS Ultrasonic Transducers.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta TFS-55 Flare Transducer',
                    'cat': 'Extreme Conditions Sensor',
                    'desc': 'Transductor ultrasónico para condiciones criogénicas y gas húmedo.',
                    'img': 'img/products/fluenta/Fluenta TFS-55.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta Dual-Path Flare Configuration',
                    'cat': 'Dual-Path Setup',
                    'desc': 'Configuración de doble trayectoria para máxima exactitud en perfiles asimétricos.',
                    'img': 'img/products/fluenta/Dual-Path Configurations.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta Single-Path Flare Configuration',
                    'cat': 'Single-Path Setup',
                    'desc': 'Configuración compacta para líneas de antorcha estándar con instalación rápida.',
                    'img': 'img/products/fluenta/Single-Path Configurations.jpeg',
                    'link': 'https://www.fluenta.com'
                }
            ]
        },

        # 7. KAM CONTROLS
        {
            'id': 'producto-brand-kam',
            'name': 'KAM CONTROLS™',
            'color': '#f97316',
            'rgb': '249, 115, 22',
            'logo': 'img/products/kam/kam_logo.png',
            'logo_scale': 'scale(1.15)',
            'catalog_link': 'https://kam.com',
            'catalog_text': 'Portal Oficial Kam Controls',
            'is_single': False,
            'products': [
                {
                    'title': 'KAM® OWD Watercut Meter',
                    'cat': 'Watercut Analyzer',
                    'desc': 'Medidor de corte de agua en línea por microondas para transferencia de custodia y producción con precisión de ±0.03%.',
                    'img': 'img/products/kam/OWD Watercut Meter.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® KF Karl Fischer Moisture Analyzer',
                    'cat': 'Karl Fischer Analyzer',
                    'desc': 'Analizador coulombimétrico de humedad por titulación Karl Fischer para crudo.',
                    'img': 'img/products/kam/KF Karl Fischer Moisture Analyzer.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® IAS Isokinetic Automatic Sampler',
                    'cat': 'Custody Sampler',
                    'desc': 'Muestreador isocinético de inserción directa bajo normas API 8.2 e ISO 3171.',
                    'img': 'img/products/kam/IAS Isokinetic Automatic Sampler.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® E-IAS Electric Isokinetic Sampler',
                    'cat': 'Electric Sampler',
                    'desc': 'Muestreador automático de accionamiento eléctrico para áreas remotas y pozos.',
                    'img': 'img/products/kam/E-IAS Electric Isokinetic Automatic Sampler.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® ATD Automatic Tank Dewatering System',
                    'cat': 'Tank Interface Dewatering',
                    'desc': 'Sistema óptico para purga automática de agua libre en fondo de tanques de crudo.',
                    'img': 'img/products/kam/ATD Automatic Tank Dewatering System.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® SMP Static Mixing Plate',
                    'cat': 'Pipeline Static Mixer',
                    'desc': 'Placa mezcladora de wafer para acondicionamiento y mezcla uniforme de flujo.',
                    'img': 'img/products/kam/SMP Static Mixing Plate.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® SMS Static Mixing Spool',
                    'cat': 'Flanged Mixing Spool',
                    'desc': 'Carrete de mezcla con bridas de alto corte para tuberías de oleoducto.',
                    'img': 'img/products/kam/SMS Static Mixing Spool.jpeg',
                    'link': 'https://kam.com'
                }
            ]
        }
    ]

    out = []
    out.append("""<li data-page-no="5" class="px-3">
                    <div class="page-width-1">
                        <div class="catalog-feed-wrapper">
                            
                            <!-- Header de la Sección (Directo sobre Fondo Oscuro, Sin Recuadro Blanco) -->
                            <div class="products-top-header mb-4 reveal-on-scroll reveal-up" id="producto-brand-emerson" style="border-bottom: 1px solid rgba(255, 255, 255, 0.12); padding-bottom: 20px; margin-bottom: 30px;">
                                <h1 class="fw-bold display-6 text-white mb-2" style="font-size: clamp(1.8rem, 3.2vw, 2.5rem); text-shadow: 0 2px 12px rgba(0, 0, 0, 0.95); letter-spacing: -0.02em;">
                                    Instrumentos de Medición y Servicios de Ingeniería
                                </h1>
                                <p class="fs-6 mb-0" style="line-height: 1.7; max-width: 950px; font-size: 1.02rem; color: #cbd5e1;">
                                    <strong style="color: #ffffff;">Representantes <span style="color: #38bdf8; font-weight: 800; text-shadow: 0 0 10px rgba(56, 189, 248, 0.4);">EMERSON</span> en <span class="venezuela-flag-text" style="font-weight: 800;">Venezuela</span></strong>, <strong style="color: #ffffff;">AIC TECH, C.A.</strong> suministra e integra instrumentación analítica y de medición de flujo para cada punto crítico de la cadena de valor petrolera con las marcas líderes mundiales.
                                </p>
                            </div>
""")

    for b in brands:
        card_id = b['id']
        name = b['name']
        color = b['color']
        rgb = b['rgb']
        logo = b['logo']
        logo_scale = b['logo_scale']
        cat_link = b['catalog_link']
        cat_text = b['catalog_text']

        # Brand header bar
        header_bar = f'''
                            <!-- ========================================================
                                 BRAND SECTION: {name}
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="{card_id}">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba({rgb}, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba({rgb}, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca: Logo + Nombre + Enlace Oficial -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba({rgb}, 0.35); border: 1px solid rgba({rgb}, 0.4);">
                                                <img src="{logo}" alt="{name}" style="max-height: 38px; max-width: 130px; object-fit: contain; transform: {logo_scale}; filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: {color}; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba({rgb}, 0.45);">{name}</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="{cat_link}" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba({rgb}, 0.18); border: 1px solid rgba({rgb}, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='{color}'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba({rgb}, 0.18)'; this.style.transform='none';">
                                                <span>{cat_text}</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>'''

        if b['is_single']:
            # FORMAT B: SINGLE PRODUCT WITH FLIP 360 ENVELOPE CARD (PHOTO 3)
            p = b['product']
            card_body = f'''
                                    <!-- FORMATO ENVELOPE FLIP 360 PARA PRODUCTO ÚNICO -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Tarjeta Flip 360 Double Gatefold Envelope -->
                                        <div class="col-12 col-lg-6 col-xl-5 d-flex justify-content-center">
                                            <div class="flip-360-wrapper" onclick="expandMediaFromElement(this);" title="Pasa el ratón para abrir el sobre o haz clic para pantalla completa">
                                                <div class="flip-360-container">
                                                    <div class="flip-pane flip-left">
                                                        <div class="front front-left" style="background: linear-gradient(135deg, {color} 0%, rgba({rgb}, 0.8) 100%);">
                                                            <div class="circle" style="border: 2px solid rgba({rgb}, 0.4);">
                                                                <i class="fas fa-box-open" style="color: {color}; font-size: 1.8rem; line-height: 100px;"></i>
                                                            </div>
                                                        </div>
                                                        <div class="back back-left">
                                                            <img src="{p['img']}" alt="{p['title']}">
                                                        </div>
                                                    </div>
                                                </div><div class="flip-360-container">
                                                    <div class="flip-pane flip-right">
                                                        <div class="front front-right" style="background: linear-gradient(225deg, {color} 0%, rgba({rgb}, 0.8) 100%);">
                                                            <div class="circle" style="border: 2px solid rgba({rgb}, 0.4);">
                                                                <i class="fas fa-box-open" style="color: {color}; font-size: 1.8rem; line-height: 100px;"></i>
                                                            </div>
                                                        </div>
                                                        <div class="back back-right">
                                                            <img src="{p['img']}" alt="{p['title']}">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Panel Descriptivo del Producto -->
                                        <div class="col-12 col-lg-6 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: {color}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">{p['cat']}</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">{p['title']}</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">{p['desc']}</p>
                                                
                                                <div class="d-flex flex-wrap gap-3 align-items-center">
                                                    <button type="button" class="btn btn-sm px-4 py-2 fw-bold text-white rounded-3 d-inline-flex align-items-center gap-2" style="background: {color}; box-shadow: 0 4px 15px rgba({rgb}, 0.4);" onclick="expandMediaFromElement(this.closest('.brand-showcase-shell'));">
                                                        <i class="fas fa-expand"></i> <span>Ver en Pantalla Completa</span>
                                                    </button>
                                                    <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-light px-3 py-2 rounded-3 d-inline-flex align-items-center gap-2">
                                                        <span>Ficha Técnica Oficial</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>'''
        else:
            # FORMAT A: 1 LARGE ON LEFT + COMPACTS PEGADITOS ON RIGHT (PHOTO 1)
            hero_p = b['products'][0]
            compact_p = b['products'][1:]

            # Compact items HTML
            compact_items_html = []
            for cp in compact_p:
                compact_items_html.append(f'''
                                                <div class="col-6 col-sm-6">
                                                    <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="height: 190px; background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer; transition: all 0.3s ease;">
                                                        <div class="compact-media-wrap h-100 w-100 d-flex align-items-center justify-content-center p-2" style="background: radial-gradient(circle, rgba({rgb}, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                            <img src="{cp['img']}" alt="{cp['title']}" class="compact-product-img" style="max-height: 85%; max-width: 85%; object-fit: contain; transition: transform 0.35s ease;">
                                                        </div>
                                                        <div class="compact-title-bar position-absolute bottom-0 start-0 end-0 p-2" style="background: rgba(2, 6, 23, 0.85); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                            <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="{cp['title']}">{cp['title']}</div>
                                                        </div>
                                                    </div>
                                                </div>''')

            compacts_grid = "".join(compact_items_html)

            card_body = f'''
                                    <!-- FORMATO WARNER/IGN (FOTO ADJUNTA 1): 1 GRANDE + COMPACTOS PEGADITOS -->
                                    <div class="row g-3 align-items-stretch">
                                        
                                        <!-- 1 GRANDE EN LA IZQUIERDA -->
                                        <div class="col-12 col-xl-6">
                                            <div class="featured-large-product-card rounded-3 overflow-hidden position-relative h-100 d-flex flex-column justify-content-between" style="min-height: 400px; background: rgba(2, 6, 23, 0.8); border: 1.5px solid rgba({rgb}, 0.45); box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                                                <div class="featured-media-stage position-relative flex-grow-1 d-flex align-items-center justify-content-center p-4" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: radial-gradient(circle, rgba({rgb}, 0.28) 0%, rgba(2, 6, 23, 0.6) 80%); cursor: pointer; min-height: 240px;">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="{hero_p['img']}" alt="{hero_p['title']}" class="featured-hero-img" style="max-height: 220px; max-width: 88%; object-fit: contain; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5)); transition: transform 0.35s ease;">
                                                </div>
                                                
                                                <!-- Overlay inferior con Blur, Título, Descripción y Enlace -->
                                                <div class="featured-bottom-info p-3 p-md-4" style="background: linear-gradient(0deg, rgba(2, 6, 23, 0.96) 0%, rgba(2, 6, 23, 0.85) 75%, transparent 100%); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                    <span class="badge mb-2 fw-bold" style="background: {color}; color: #ffffff; font-size: 0.72rem; letter-spacing: 0.5px;">{hero_p['cat']}</span>
                                                    <h4 class="fw-bold text-white mb-2 fs-5" style="line-height: 1.35;">{hero_p['title']}</h4>
                                                    <p class="small text-white-50 mb-3" style="font-size: 0.84rem; line-height: 1.5;">{hero_p['desc']}</p>
                                                    <div class="d-flex justify-content-between align-items-center">
                                                        <a href="{hero_p['link']}" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-bold text-white rounded-3 d-inline-flex align-items-center gap-2" style="background: rgba({rgb}, 0.25); border: 1px solid rgba({rgb}, 0.5); font-size: 0.80rem;">
                                                            <span>Ver detalles</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                                        </a>
                                                        <button type="button" class="btn btn-sm btn-link text-white-50 text-decoration-none small" onclick="expandMediaFromElement(this.closest('.featured-large-product-card'));">
                                                            <i class="fas fa-expand me-1"></i> Agrandar
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- COMPACTOS PEGADITOS EN LA DERECHA (CON BLUR Y SOLO TÍTULO) -->
                                        <div class="col-12 col-xl-6">
                                            <div class="row g-2 h-100 align-content-start">
                                                {compacts_grid}
                                            </div>
                                        </div>

                                    </div>'''

        footer_shell = """
                                </div>
                            </article>"""

        out.append(header_bar + card_body + footer_shell)

    out.append("""                        </div>
                    </div>
                </li>
""")
    return "\n".join(out)

if __name__ == '__main__':
    res = generate_section5_final()
    with open('scratch/generated_section5_final.html', 'w', encoding='utf-8') as f:
        f.write(res)
    print("Generated new Section 5 HTML! Length:", len(res))
