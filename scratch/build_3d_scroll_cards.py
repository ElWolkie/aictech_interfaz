# -*- coding: utf-8 -*-
"""
build_3d_scroll_cards.py
Generates the 3D Webflow-inspired presentation for Section 5 (Productos)
with dark obsidian glassmorphism, 3D perspective, brand glows, and zero harsh white.
"""

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def generate_section5_3d():
    brands = [
        {
            'id': 'producto-brand-roxar',
            'name': 'ROXAR™',
            'color': '#a855f7',
            'rgb': '168, 85, 247',
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
            'color': '#14b8a6',
            'rgb': '20, 184, 166',
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
                    'title': 'FLUXUS® G721 - Medición No Invasiva de Gases',
                    'cat': 'Gas Flow Clamp-On',
                    'desc': 'Medición ultrasónica permanente para gas natural, gases de proceso y aire comprimido a alta presión.',
                    'img': 'img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/flexim-fluxus-g721'
                }
            ]
        },
        {
            'id': 'producto-brand-amstrex',
            'name': 'AMS TREX™',
            'color': '#94a3b8',
            'rgb': '148, 163, 184',
            'logo': 'img/products/ams trex/ams-trex-banner.jpg',
            'logo_scale': 'scale(1.0)',
            'title': 'Comunicador Portátil Intrínsecamente Seguro',
            'desc': 'El estándar de la industria para configuración, diagnóstico y verificación de instrumentación inteligente HART y Foundation Fieldbus en áreas clasificadas sin permisos de trabajo en caliente.',
            'specs': [
                'Certificación de Seguridad Intrínseca (IS) para operar en atmósferas explosivas',
                'Alimentación directa de lazo para energizar transmisores y posicionadores de válvulas',
                'Pantalla táctil resistiva de alta resolución operable con guantes de trabajo',
                'Sincronización automática de datos con el software AMS Device Manager'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/ams-trex-device-communicator',
            'catalog_text': 'Ver Catálogo AMS Trex en Emerson',
            'products': [
                {
                    'title': 'AMS Trex™ Device Communicator',
                    'cat': 'Field Communicator',
                    'desc': 'Comunicador robusto intrínsecamente seguro para mantenimiento y calibración de instrumentos en campo.',
                    'img': 'img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/ams-trex-device-communicator'
                }
            ]
        },
        {
            'id': 'producto-brand-rosemount',
            'name': 'ROSEMOUNT™',
            'color': '#38bdf8',
            'rgb': '56, 189, 248',
            'logo': 'img/products/rosemount/Rosemount-New-Logo.png',
            'logo_scale': 'scale(1.1)',
            'title': 'Medición de Presión, Nivel, Caudal y Temperatura',
            'desc': 'La marca insignia de Emerson para control de procesos industriales. Transmisores de presión coplanares, radares de nivel de onda guiada y medidores de caudal vortex con confiabilidad operativa insuperable.',
            'specs': [
                'Transmisores de presión diferencial y manométrica con estabilidad garantizada a 15 años',
                'Radares de nivel serie 5300 con tecnología Direct Switch para medios de baja dieléctrica',
                'Medidores Vortex con sensor aislado para reemplazo seguro sin detener la línea',
                'Diagnósticos avanzados de integridad de lazo y detección de líneas de impulso tapadas'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/rosemount-5300',
            'catalog_text': 'Ver Catálogo Rosemount en Emerson',
            'products': [
                {
                    'title': 'Rosemount™ 5300 Level Transmitter - Guided Wave Radar',
                    'cat': 'Level Measurement',
                    'desc': 'Radar de nivel por onda guiada para medición precisa de interfase y nivel total en tanques y separadores.',
                    'img': 'img/products/rosemount/Rosemount™ 5300 Level Transmitter - Guided Wave Radar.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-5300'
                },
                {
                    'title': 'Rosemount™ 8800 Reducer Vortex Flow Meter',
                    'cat': 'Vortex Flow Meter',
                    'desc': 'Medidor vortex con reductor integrado para ampliar el rango de medición de caudal sin tuberías de transición.',
                    'img': 'img/products/rosemount/Rosemount™ 8800 Reducer Vortex Flow Meter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-8800'
                },
                {
                    'title': 'Rosemount™ 8600 Vortex Flow Meters',
                    'cat': 'Utility & Process Vortex',
                    'desc': 'Medición de caudal robusta y económica para aplicaciones generales de vapor, gas y líquidos limpios.',
                    'img': 'img/products/rosemount/Rosemount™ 8600 Vortex Flow Meters.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-8600'
                },
                {
                    'title': 'Transmisor de Nivel Rosemount 5300 de Alta Presión',
                    'cat': 'High Pressure / High Temp',
                    'desc': 'Versión reforzada para recipientes de proceso sometidos a alta presión y temperaturas extremas.',
                    'img': 'img/products/rosemount/Transmisor de nivel Rosemount 5300 - Radar de onda guiada.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/rosemount-5300'
                }
            ]
        },
        {
            'id': 'producto-brand-micromotion',
            'name': 'MICRO MOTION™',
            'color': '#94a3b8',
            'rgb': '148, 163, 184',
            'logo': 'img/products/micromotion/micromotion.png',
            'logo_scale': 'scale(1.15)',
            'title': 'Medidores de Flujo Másico Coriolis y Densidad',
            'desc': 'Referencia mundial en medición directa de flujo másico, flujo volumétrico, densidad y temperatura con precisión fiscal extrema para transferencia de custodia y control crítico de hidrocarburos.',
            'specs': [
                'Medición directa de masa y densidad sin requerir compensación por presión o temperatura',
                'Precisión de hasta ±0.05% en masa para transferencia de custodia fiscal',
                'Verificación de calibración en línea Smart Meter Verification en menos de 90 segundos',
                'Transmisores Serie 5700 con pantalla gráfica y registro de auditoría integrado'
            ],
            'catalog_link': 'https://www.emerson.com/es-es/catalog/micro-motion-5700-field-mount-transmitter',
            'catalog_text': 'Ver Catálogo Micro Motion en Emerson',
            'products': [
                {
                    'title': 'Micro Motion™ 5700 Field-Mount Transmitter',
                    'cat': 'Coriolis Transmitter',
                    'desc': 'Transmisor avanzado de montaje en campo con procesamiento de señal MVD y verificación de integridad.',
                    'img': 'img/products/micromotion/Micro Motion™ 5700 Field-Mount Transmitter.jpeg',
                    'link': 'https://www.emerson.com/es-es/catalog/micro-motion-5700-field-mount-transmitter'
                },
                {
                    'title': 'Micro Motion™ Coriolis ELITE Sensor',
                    'cat': 'Mass Flow & Density Sensor',
                    'desc': 'Sensor Coriolis de máximo rendimiento para las aplicaciones de hidrocarburos más exigentes.',
                    'img': 'img/products/micromotion/micromotion.jpg',
                    'link': 'https://www.emerson.com/es-es/catalog/micro-motion-elite-coriolis-flow-density-meters'
                }
            ]
        },
        {
            'id': 'producto-brand-fluenta',
            'name': 'FLUENTA™',
            'color': '#22c55e',
            'rgb': '34, 197, 94',
            'logo': 'img/products/fluenta/Fluenta-blog-logo.png',
            'logo_scale': 'scale(1.1)',
            'title': 'Medición Ultrasónica de Gas de Antorcha (Flare Gas)',
            'desc': 'Tecnología líder mundial para medición ultrasónica no intrusiva de gas de alivio y antorcha (flare gas). Cumplimiento riguroso de normativas ambientales y reducción de emisiones de gases de efecto invernadero.',
            'specs': [
                'Rango dinámico de velocidad ultra amplio: desde 0.1 m/s hasta más de 100 m/s',
                'Transductores de titanio FlarePhase de alta resistencia química a gases corrosivos con H2S',
                'Configuraciones Single-Path y Dual-Path para máxima confiabilidad operativa',
                'Certificaciones internacionales para reporte fiscal de emisiones y créditos de carbono'
            ],
            'catalog_link': 'https://www.fluenta.com',
            'catalog_text': 'Ver Catálogo Oficial Fluenta',
            'products': [
                {
                    'title': 'Fluenta FlarePhase™ 250 - Sensor de Antorcha',
                    'cat': 'Flare Gas Transducer',
                    'desc': 'Sensor ultrasónico de gas de antorcha para un amplio rango de velocidades y temperaturas.',
                    'img': 'img/products/fluenta/FlarePhase 250.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta FlarePhase™ 350 - Alta Temperatura',
                    'cat': 'High Temperature Flare Sensor',
                    'desc': 'Diseñado para antorchas de alta temperatura y atmósferas con alto contenido de azufre.',
                    'img': 'img/products/fluenta/FlarePhase 350.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta TFS Ultrasonic Transducers',
                    'cat': 'Acoustic Flare Transducers',
                    'desc': 'Transductores de tecnología acústica patentada para tuberías de descarga de antorcha.',
                    'img': 'img/products/fluenta/Fluenta TFS Ultrasonic Transducers.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta TFS-55 Flare Transducer',
                    'cat': 'Extreme Conditions Sensor',
                    'desc': 'Transductor ultrasónico especializado para condiciones de criogenia y gas húmedo.',
                    'img': 'img/products/fluenta/Fluenta TFS-55.jpeg',
                    'link': 'https://www.fluenta.com'
                },
                {
                    'title': 'Fluenta Dual-Path Flare Configuration',
                    'cat': 'Dual-Path Measurement',
                    'desc': 'Arreglo de doble trayectoria para máxima exactitud en perfiles de flujo asimétricos.',
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
        {
            'id': 'producto-brand-kam',
            'name': 'KAM CONTROLS™',
            'color': '#f97316',
            'rgb': '249, 115, 22',
            'logo': 'img/products/kam/kam_logo.png',
            'logo_scale': 'scale(1.15)',
            'title': 'Sistemas de Muestreo Automático y Corte de Agua',
            'desc': 'Especialista global en instrumentación de calidad de crudo. Muestreadores isocinéticos automáticos, analizadores de corte de agua (OWD), detectores de interfase y desaguado automático de tanques.',
            'specs': [
                'Muestreadores automáticos isocinéticos (IAS y E-IAS) bajo normas API 8.2 e ISO 3171',
                'Analizador OWD de corte de agua por microondas con exactitud de ±0.03%',
                'Sistema ATD para desaguado automático de tanques sin pérdida de hidrocarburo',
                'Mezcladores estáticos de flujo (SMP y SMS) para homogeneización previa a muestreo'
            ],
            'catalog_link': 'https://kam.com',
            'catalog_text': 'Ver Catálogo Oficial Kam Controls',
            'products': [
                {
                    'title': 'KAM® OWD Watercut Meter',
                    'cat': 'Watercut Measurement',
                    'desc': 'Medidor de corte de agua en línea por microondas para transferencia de custodia y producción.',
                    'img': 'img/products/kam/OWD Watercut Meter.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® KF Karl Fischer Moisture Analyzer',
                    'cat': 'Laboratory & Field Moisture',
                    'desc': 'Analizador coulombimétrico de humedad por titulación Karl Fischer para crudo.',
                    'img': 'img/products/kam/KF Karl Fischer Moisture Analyzer.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® IAS Isokinetic Automatic Sampler',
                    'cat': 'Custody Transfer Sampling',
                    'desc': 'Muestreador isocinético de inserción directa para tuberías de crudo de 2" a 48".',
                    'img': 'img/products/kam/IAS Isokinetic Automatic Sampler.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® E-IAS Electric Isokinetic Sampler',
                    'cat': 'Electric Sampler System',
                    'desc': 'Muestreador automático de accionamiento eléctrico para áreas remotas y pozos.',
                    'img': 'img/products/kam/E-IAS Electric Isokinetic Automatic Sampler.jpeg',
                    'link': 'https://kam.com'
                },
                {
                    'title': 'KAM® ATD Automatic Tank Dewatering System',
                    'cat': 'Tank Interface Detection',
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

    for idx, b in enumerate(brands):
        card_id = b['id']
        badge_name = b['name']
        brand_color = b['color']
        brand_rgb = b['rgb']
        title = b['title']
        desc = b['desc']
        cat_link = b['catalog_link']
        cat_text = b['catalog_text']

        specs_html = "".join([
            f'<li class="d-flex align-items-start gap-2"><i class="fas fa-check-circle mt-1" style="color: {brand_color}; font-size: 0.88rem; filter: drop-shadow(0 0 4px {brand_color});"></i><span style="color: #cbd5e1;">{s}</span></li>'
            for s in b['specs']
        ])

        logo_html = f'''<div class="brand-panel-logo-wrap rounded-4" style="height: 110px; background: rgba(255, 255, 255, 0.96); display: flex; align-items: center; justify-content: center; padding: 12px 24px; box-shadow: 0 12px 35px rgba(0,0,0,0.4), 0 0 25px rgba({brand_rgb}, 0.35); border: 1.5px solid rgba({brand_rgb}, 0.5); transform: translateZ(35px);">
                                <img src="{b['logo']}" alt="{badge_name}" style="max-height: 85px; max-width: 90%; object-fit: contain; transform: {b['logo_scale']}; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.12));">
                            </div>'''

        is_few_products = len(b['products']) <= 2
        col_class = "col-12" if len(b['products']) == 1 else "col-12 col-md-6"

        prod_items_html = []
        for p in b['products']:
            img_height = "220px" if is_few_products else "160px"
            prod_items_html.append(f'''
                                        <div class="{col_class}">
                                            <div class="emerson-product-card h-100" style="background: linear-gradient(145deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; overflow: hidden; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
                                                <div class="product-card-media-wrapper position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="height: {img_height}; background: radial-gradient(circle, rgba({brand_rgb}, 0.22) 0%, rgba(15, 23, 42, 0.45) 80%); display: flex; align-items: center; justify-content: center; cursor: pointer; overflow: hidden;">
                                                    <button type="button" class="product-expand-badge" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="{p['img']}" alt="{p['title']}" class="emerson-product-img" style="max-height: 88%; max-width: 88%; object-fit: contain; transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), filter 0.35s ease;">
                                                </div>
                                                <div class="product-card-body p-3 d-flex flex-column justify-content-between">
                                                    <div>
                                                        <span class="product-category-tag mb-1 d-inline-block" style="font-size: 0.72rem; color: {brand_color}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">{p['cat']}</span>
                                                        <h5 class="product-card-title fs-6 mb-2 fw-bold text-white" style="line-height: 1.35;">{p['title']}</h5>
                                                        <p class="product-card-desc small mb-3" style="font-size: 0.82rem; line-height: 1.5; color: #94a3b8;">{p['desc']}</p>
                                                    </div>
                                                    <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="emerson-details-btn mt-auto" onclick="event.stopPropagation();" style="background: rgba({brand_rgb}, 0.15); border: 1px solid rgba({brand_rgb}, 0.4); color: #ffffff; padding: 7px 14px; border-radius: 8px; font-size: 0.82rem; font-weight: 600; text-decoration: none; display: flex; align-items: center; justify-content: space-between; transition: all 0.25s ease;">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>''')

        products_grid_html = "".join(prod_items_html)

        card_html = f'''
                            <!-- ========================================================
                                 BRAND 3D CARD: {badge_name}
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="{card_id}">
                                <div class="brand-snapping-card-inner rounded-4 overflow-hidden" style="border: 1.5px solid rgba({brand_rgb}, 0.38); background: linear-gradient(145deg, rgba(15, 23, 42, 0.92) 0%, rgba(8, 15, 30, 0.96) 100%); backdrop-filter: blur(20px); box-shadow: 0 25px 65px rgba(0, 0, 0, 0.6), 0 0 35px rgba({brand_rgb}, 0.15);">
                                    <div class="row g-0 align-items-stretch">
                                        
                                        <!-- IZQUIERDA: SHOWCASE DE PRODUCTOS (FOTOS Y ESPECIFICACIONES) -->
                                        <div class="col-12 col-xl-7 p-3 p-lg-4 card-showcase-column" style="background: rgba(2, 6, 23, 0.58); border-right: 1px solid rgba(255, 255, 255, 0.08);">
                                            <div class="d-flex justify-content-between align-items-center mb-3 pb-2" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                                <div class="d-flex align-items-center gap-2">
                                                    <span class="badge px-3 py-1 fw-bold fs-6" style="background: {brand_color}; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba({brand_rgb}, 0.45);">{badge_name}</span>
                                                    <span class="small fw-semibold" style="color: #94a3b8;">Portafolio Especializado</span>
                                                </div>
                                                <span class="badge border px-2 py-1 small" style="background: rgba(30, 41, 59, 0.8); color: #cbd5e1; border-color: rgba(255, 255, 255, 0.12) !important;"><i class="fas fa-layer-group me-1" style="color: {brand_color};"></i> {len(b['products'])} Modelos</span>
                                            </div>

                                            <div class="showcase-scroll-gallery" style="max-height: 600px; overflow-y: auto; padding-right: 6px;">
                                                <div class="row g-3">
                                                    {products_grid_html}
                                                </div>
                                            </div>
                                        </div>

                                        <!-- DERECHA: PANEL DE IDENTIDAD DE MARCA CON LOGO Y ESPECIFICACIONES (3D DEPTH) -->
                                        <div class="col-12 col-xl-5 p-4 d-flex flex-column justify-content-between card-brand-column" style="background: linear-gradient(150deg, rgba(15, 23, 42, 0.7) 0%, rgba({brand_rgb}, 0.14) 100%);">
                                            <div>
                                                <!-- Logotipo de la marca con elevación 3D -->
                                                <div class="mb-4">
                                                    {logo_html}
                                                </div>

                                                <h3 class="fw-bold fs-4 text-white mb-2" style="line-height: 1.3; text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);">{title}</h3>
                                                <p class="small mb-4" style="line-height: 1.65; font-size: 0.92rem; color: #cbd5e1;">{desc}</p>

                                                <div class="brand-card-specs-box p-3 rounded-3 mb-4" style="background: rgba(2, 6, 23, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 8px 25px rgba(0,0,0,0.35);">
                                                    <h6 class="fw-bold text-uppercase small mb-2" style="color: {brand_color}; letter-spacing: 0.6px;"><i class="fas fa-shield-halved me-1"></i> Capacidades de Alto Rendimiento:</h6>
                                                    <ul class="list-unstyled mb-0 small d-flex flex-column gap-2" style="font-size: 0.85rem; line-height: 1.5;">
                                                        {specs_html}
                                                    </ul>
                                                </div>
                                            </div>

                                            <div class="pt-3" style="border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                <a href="{cat_link}" target="_blank" rel="noopener noreferrer" class="btn w-100 py-2 fw-bold text-white d-flex align-items-center justify-content-center gap-2 rounded-3" style="background: {brand_color}; box-shadow: 0 4px 20px rgba({brand_rgb}, 0.45); transition: all 0.25s ease;" onmouseover="this.style.opacity='0.9'; this.style.transform='translateY(-2px)';" onmouseout="this.style.opacity='1'; this.style.transform='none';">
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
    res = generate_section5_3d()
    with open('scratch/generated_section5_3d.html', 'w', encoding='utf-8') as f:
        f.write(res)
    print("Generated 3D Scroll Cards Section 5! Length:", len(res))
