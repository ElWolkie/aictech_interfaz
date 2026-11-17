# -*- coding: utf-8 -*-
"""
Script to generate the refined Section 5 (Productos) with:
1. 1 Large Featured card on left (clean button 'Ver más detalles', 'Agrandar' removed).
2. Right compact cards stretching 100% to bottom, no white/dark gap.
3. Odd cards centered (Rosemount 3rd card, Fluenta 5th card, Kam 7th card).
4. Single products (Flexim, AMS Trex, Micro Motion):
   - 3D Flip Card with front brand logo (Flexim, Micro Motion) and AMS Trex photo for Trex.
   - Removed 'Ver en Pantalla Completa', leaving only compact 'Ver más detalles' button.
   - Removed 'ams-trex-banner.jpg' in AMS Trex, using Emerson brand plate.
"""

def generate_section5():
    html = []

    # Section wrapper
    html.append('''<li data-page-no="5" class="px-3">
                    <div class="page-width-1">
                        <div class="catalog-feed-wrapper">
                            
                            <!-- Header de la Sección (Directo sobre Fondo Oscuro, Sin Recuadro Blanco) -->
                            <div class="products-top-header mb-4 reveal-on-scroll reveal-up" id="producto-brand-emerson" style="border-bottom: 1px solid rgba(255, 255, 255, 0.12); padding-bottom: 20px; margin-bottom: 30px;">
                                <h1 class="fw-bold display-6 text-white mb-2" style="font-size: clamp(1.8rem, 3.2vw, 2.5rem); text-shadow: 0 2px 12px rgba(0, 0, 0, 0.95); letter-spacing: -0.02em;">
                                    Instrumentos de Medición y Servicios de Ingeniería
                                </h1>
                                <p class="fs-6 mb-0" style="line-height: 1.7; max-width: 950px; font-size: 1.02rem; color: #cbd5e1;">
                                    Soluciones integrales de medición de flujo, instrumentación analítica y diagnóstico predictivo para la optimización continua de activos de producción, transporte y refinación.
                                </p>
                            </div>''')

    # =========================================================================
    # 1. ROXAR (Morado #a855f7)
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: ROXAR™ (EMERSON AUTOMATION SOLUTIONS)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-roxar">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(168, 85, 247, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(168, 85, 247, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(168, 85, 247, 0.35); border: 1px solid rgba(168, 85, 247, 0.4);">
                                                <img src="img/products/roxar/roxar.png" alt="ROXAR™" style="max-height: 38px; max-width: 130px; object-fit: contain; transform: scale(1.15); filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #a855f7; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(168, 85, 247, 0.45);">ROXAR™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/roxar-2600" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(168, 85, 247, 0.18); border: 1px solid rgba(168, 85, 247, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#a855f7'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(168, 85, 247, 0.18)'; this.style.transform='none';">
                                                <span>Catálogo Roxar en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO WARNER/IGN: 1 GRANDE + COMPACTOS PEGADITOS -->
                                    <div class="row g-3 align-items-stretch">
                                        <!-- 1 GRANDE EN LA IZQUIERDA -->
                                        <div class="col-12 col-xl-6">
                                            <div class="featured-large-product-card rounded-3 overflow-hidden position-relative h-100 d-flex flex-column justify-content-between" style="min-height: 440px; background: rgba(2, 6, 23, 0.8); border: 1.5px solid rgba(168, 85, 247, 0.45); box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                                                <div class="featured-media-stage position-relative flex-grow-1 d-flex align-items-center justify-content-center p-4" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: radial-gradient(circle, rgba(168, 85, 247, 0.28) 0%, rgba(2, 6, 23, 0.6) 80%); cursor: pointer; min-height: 250px;">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/roxar/2600.jpeg" alt="Roxar™ 2600 Multiphase Flow Meters" class="featured-hero-img" style="max-height: 230px; max-width: 88%; object-fit: contain; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5)); transition: transform 0.35s ease;">
                                                </div>
                                                
                                                <!-- Overlay inferior con Blur, Título, Descripción y Enlace -->
                                                <div class="featured-bottom-info p-3 p-md-4" style="background: linear-gradient(0deg, rgba(2, 6, 23, 0.96) 0%, rgba(2, 6, 23, 0.85) 75%, transparent 100%); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                    <span class="badge mb-2 fw-bold" style="background: #a855f7; color: #ffffff; font-size: 0.72rem; letter-spacing: 0.5px;">Multiphase Measurement</span>
                                                    <h4 class="fw-bold text-white mb-2 fs-5" style="line-height: 1.35;">Roxar™ 2600 Multiphase Flow Meters</h4>
                                                    <p class="small text-white-50 mb-3" style="font-size: 0.84rem; line-height: 1.5;">Medidor multifásico líder de la industria para caracterización cuantitativa continua en cabeza de pozo sin separación física.</p>
                                                    <div class="d-flex align-items-center">
                                                        <a href="https://www.emerson.com/es-es/catalog/roxar-2600" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(168, 85, 247, 0.25); border: 1px solid rgba(168, 85, 247, 0.5); font-size: 0.80rem;">
                                                            <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- COMPACTOS PEGADITOS EN LA DERECHA (EXPANDIDOS HASTA ABAJO) -->
                                        <div class="col-12 col-xl-6">
                                            <div class="compact-products-grid h-100">
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(168, 85, 247, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/roxar/water-cut-meter.jpeg" alt="Roxar™ Watercut Meter" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Roxar™ Watercut Meter">Roxar™ Watercut Meter</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(168, 85, 247, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/roxar/Medidor de Wet Gas SubSea.jpeg" alt="Roxar™ Subsea Wetgas Meters" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Roxar™ Subsea Wetgas Meters">Roxar™ Subsea Wetgas Meters</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(168, 85, 247, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/roxar/Multifasico-para-instalaciones-SubSea.jpeg" alt="Roxar™ Subsea Multiphase Flow Meter" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Roxar™ Subsea Multiphase Flow Meter">Roxar™ Subsea Multiphase Flow Meter</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(168, 85, 247, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/roxar/Medidor de Salinidad (Complemento del 2600).jpeg" alt="Roxar™ Multiphase Salinity System" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Roxar™ Multiphase Salinity System">Roxar™ Multiphase Salinity System</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # =========================================================================
    # 2. FLEXIM (Aguamarina #14b8a6) - 3D FLIP CARD
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: FLEXIM™ (EMERSON AUTOMATION SOLUTIONS)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-flexim">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(20, 184, 166, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(20, 184, 166, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(20, 184, 166, 0.35); border: 1px solid rgba(20, 184, 166, 0.4);">
                                                <img src="img/products/flexim/Flexim-Logo.png" alt="FLEXIM™" style="max-height: 38px; max-width: 130px; object-fit: contain; transform: scale(1.05); filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #14b8a6; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(20, 184, 166, 0.45);">FLEXIM™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/flexim-fluxus-f631" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(20, 184, 166, 0.18); border: 1px solid rgba(20, 184, 166, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#14b8a6'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(20, 184, 166, 0.18)'; this.style.transform='none';">
                                                <span>Catálogo Flexim en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO 3D FLIP CARD ELEGANTE -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Tarjeta Flip 3D: Front = Logo Flexim / Back = Equipo -->
                                        <div class="col-12 col-lg-6 col-xl-5 d-flex justify-content-center">
                                            <div class="single-product-flip3d" onclick="this.classList.toggle('is-flipped');" title="Pasa el ratón o toca para girar la tarjeta">
                                                <div class="flip3d-inner" style="border: 1.5px solid rgba(20, 184, 166, 0.45); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 25px rgba(20, 184, 166, 0.25);">
                                                    <!-- Cara Frontal con Logo Propio -->
                                                    <div class="flip3d-front" style="background: linear-gradient(145deg, rgba(8, 28, 26, 0.96) 0%, rgba(2, 10, 15, 0.98) 100%);">
                                                        <div class="brand-emblem-plate mb-2" style="border: 2px solid rgba(20, 184, 166, 0.4);">
                                                            <img src="img/products/flexim/Flexim-Logo.png" alt="FLEXIM™" style="max-height: 48px; max-width: 160px; object-fit: contain;">
                                                        </div>
                                                        <div class="text-info small fw-semibold mt-2" style="color: #2dd4bf !important; letter-spacing: 0.5px;">Clamp-On Ultrasonic Flow</div>
                                                        <span class="flip-hint-badge"><i class="fas fa-sync-alt me-1"></i> Toca o pasa el ratón para ver equipo</span>
                                                    </div>
                                                    <!-- Cara Trasera con Foto de Producto -->
                                                    <div class="flip3d-back" onclick="event.stopPropagation(); expandMediaFromElement(this);" title="Haga clic para pantalla completa" style="background: radial-gradient(circle, rgba(20, 184, 166, 0.22) 0%, rgba(2, 6, 23, 0.98) 80%); cursor: pointer;">
                                                        <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                        <img src="img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg" alt="FLUXUS® F631 BA - Caudalímetro Portátil para Líquidos">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Panel Descriptivo del Producto -->
                                        <div class="col-12 col-lg-6 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: #14b8a6; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">Clamp-On Ultrasonic Flow Meter</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">FLUXUS® F631 BA - Caudalímetro Portátil para Líquidos</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">Medidor de flujo ultrasónico portátil no invasivo clamp-on para líquidos y gases sin cortes de tubería ni paradas operativas.</p>
                                                
                                                <div class="d-flex align-items-center">
                                                    <a href="https://www.emerson.com/es-es/catalog/flexim-fluxus-f631" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(20, 184, 166, 0.25); border: 1px solid rgba(20, 184, 166, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#14b8a6';" onmouseout="this.style.background='rgba(20, 184, 166, 0.25)';">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # =========================================================================
    # 3. AMS TREX (Negrito claro #94a3b8) - FOTO COMO PORTADA, SIN BANNER VIEJO
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: AMS TREX™ (EMERSON AUTOMATION SOLUTIONS)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-amstrex">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(148, 163, 184, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(148, 163, 184, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca: Logo Emerson + Nombre AMS TREX -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(148, 163, 184, 0.35); border: 1px solid rgba(148, 163, 184, 0.4);">
                                                <img src="img/products/emerson.png" alt="EMERSON" style="max-height: 38px; max-width: 130px; object-fit: contain; filter: grayscale(1) drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #94a3b8; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(148, 163, 184, 0.45);">AMS TREX™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/ams-trex-device-communicator" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(148, 163, 184, 0.18); border: 1px solid rgba(148, 163, 184, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#94a3b8'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(148, 163, 184, 0.18)'; this.style.transform='none';">
                                                <span>Catálogo AMS Trex en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO 3D FLIP CARD: FOTO COMO PORTADA DIRECTA -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Tarjeta Flip 3D -->
                                        <div class="col-12 col-lg-6 col-xl-5 d-flex justify-content-center">
                                            <div class="single-product-flip3d" onclick="this.classList.toggle('is-flipped');" title="Pasa el ratón o toca para girar la tarjeta">
                                                <div class="flip3d-inner" style="border: 1.5px solid rgba(148, 163, 184, 0.45); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 25px rgba(148, 163, 184, 0.25);">
                                                    <!-- Cara Frontal: Foto Principal del Comunicador -->
                                                    <div class="flip3d-front" style="background: radial-gradient(circle, rgba(148, 163, 184, 0.22) 0%, rgba(2, 6, 23, 0.98) 80%); padding: 16px;">
                                                        <img src="img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg" alt="AMS Trex™ Device Communicator" style="max-height: 80%; max-width: 88%; object-fit: contain; filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.6));">
                                                        <span class="flip-hint-badge mt-2"><i class="fas fa-sync-alt me-1"></i> Toca para ver en alta resolución</span>
                                                    </div>
                                                    <!-- Cara Trasera: Zoom Técnico -->
                                                    <div class="flip3d-back" onclick="event.stopPropagation(); expandMediaFromElement(this);" title="Haga clic para pantalla completa" style="background: radial-gradient(circle, rgba(148, 163, 184, 0.25) 0%, rgba(2, 6, 23, 0.98) 80%); cursor: pointer;">
                                                        <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                        <img src="img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg" alt="AMS Trex™ Device Communicator - HD" style="transform: scale(1.08);">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Panel Descriptivo del Producto -->
                                        <div class="col-12 col-lg-6 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">Field Communicator &amp; Diagnostics</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">AMS Trex™ Device Communicator</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">Comunicador de campo de alta resistencia con pantalla táctil intuitiva y soporte para dispositivos HART y FOUNDATION Fieldbus con alimentación directa de lazo.</p>
                                                
                                                <div class="d-flex align-items-center">
                                                    <a href="https://www.emerson.com/es-es/catalog/ams-trex-device-communicator" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(148, 163, 184, 0.25); border: 1px solid rgba(148, 163, 184, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#94a3b8';" onmouseout="this.style.background='rgba(148, 163, 184, 0.25)';">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # =========================================================================
    # 4. ROSEMOUNT (Azul #38bdf8) - 1 GRANDE + 3 COMPACTOS (3º CENTRADO)
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: ROSEMOUNT™ (EMERSON AUTOMATION SOLUTIONS)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-rosemount">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(56, 189, 248, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(56, 189, 248, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(56, 189, 248, 0.35); border: 1px solid rgba(56, 189, 248, 0.4);">
                                                <img src="img/products/rosemount/Rosemount-New-Logo.png" alt="ROSEMOUNT™" style="max-height: 38px; max-width: 130px; object-fit: contain; filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #38bdf8; color: #020617; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(56, 189, 248, 0.45);">ROSEMOUNT™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/rosemount-5300" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(56, 189, 248, 0.18); border: 1px solid rgba(56, 189, 248, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#38bdf8'; this.style.color='#020617'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(56, 189, 248, 0.18)'; this.style.color='#ffffff'; this.style.transform='none';">
                                                <span>Catálogo Rosemount en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO: 1 GRANDE + 3 COMPACTOS (EL 3º CENTRADO) -->
                                    <div class="row g-3 align-items-stretch">
                                        <!-- 1 GRANDE EN LA IZQUIERDA -->
                                        <div class="col-12 col-xl-6">
                                            <div class="featured-large-product-card rounded-3 overflow-hidden position-relative h-100 d-flex flex-column justify-content-between" style="min-height: 440px; background: rgba(2, 6, 23, 0.8); border: 1.5px solid rgba(56, 189, 248, 0.45); box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                                                <div class="featured-media-stage position-relative flex-grow-1 d-flex align-items-center justify-content-center p-4" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: radial-gradient(circle, rgba(56, 189, 248, 0.28) 0%, rgba(2, 6, 23, 0.6) 80%); cursor: pointer; min-height: 250px;">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/rosemount/Rosemount™ 5300 Level Transmitter - Guided Wave Radar.jpeg" alt="Rosemount™ 5300 Level Transmitter - Guided Wave Radar" class="featured-hero-img" style="max-height: 230px; max-width: 88%; object-fit: contain; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5)); transition: transform 0.35s ease;">
                                                </div>
                                                
                                                <!-- Overlay inferior con Blur, Título, Descripción y Enlace -->
                                                <div class="featured-bottom-info p-3 p-md-4" style="background: linear-gradient(0deg, rgba(2, 6, 23, 0.96) 0%, rgba(2, 6, 23, 0.85) 75%, transparent 100%); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                    <span class="badge mb-2 fw-bold" style="background: #38bdf8; color: #020617; font-size: 0.72rem; letter-spacing: 0.5px;">Level Measurement</span>
                                                    <h4 class="fw-bold text-white mb-2 fs-5" style="line-height: 1.35;">Rosemount™ 5300 Level Transmitter - Guided Wave Radar</h4>
                                                    <p class="small text-white-50 mb-3" style="font-size: 0.84rem; line-height: 1.5;">Medición continua y confiable de nivel e interfaz en líquidos, lodos y sólidos para condiciones extremas de proceso.</p>
                                                    <div class="d-flex align-items-center">
                                                        <a href="https://www.emerson.com/es-es/catalog/rosemount-5300" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(56, 189, 248, 0.25); border: 1px solid rgba(56, 189, 248, 0.5); font-size: 0.80rem;">
                                                            <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- COMPACTOS EN LA DERECHA (EXPANDIDOS HASTA ABAJO + 3º CENTRADO) -->
                                        <div class="col-12 col-xl-6">
                                            <div class="compact-products-grid h-100">
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(56, 189, 248, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/rosemount/Rosemount™ 8800 Reducer Vortex Flow Meter.jpeg" alt="Rosemount™ 8800 Reducer Vortex Flow Meter" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Rosemount™ 8800 Reducer Vortex Flow Meter">Rosemount™ 8800 Reducer Vortex Flow Meter</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(56, 189, 248, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/rosemount/Rosemount™ 8600 Vortex Flow Meters.jpeg" alt="Rosemount™ 8600 Vortex Flow Meters" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Rosemount™ 8600 Vortex Flow Meters">Rosemount™ 8600 Vortex Flow Meters</div>
                                                    </div>
                                                </div>
                                                
                                                <!-- TERCER PRODUCTO (IMPAR) CENTRADO CON EL ANCHO EXACTO -->
                                                <div class="compact-product-card compact-card-centered-odd rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(56, 189, 248, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/rosemount/Transmisor de nivel Rosemount 5300 - Radar de onda guiada.jpeg" alt="Transmisor de Nivel Rosemount 5300" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Transmisor de Nivel Rosemount 5300">Transmisor de Nivel Rosemount 5300</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # =========================================================================
    # 5. MICRO MOTION (Gris #cbd5e1) - 3D FLIP CARD
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: MICRO MOTION™ (EMERSON AUTOMATION SOLUTIONS)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-micromotion">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(203, 213, 225, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(203, 213, 225, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(203, 213, 225, 0.35); border: 1px solid rgba(203, 213, 225, 0.4);">
                                                <img src="img/products/micromotion/micromotion.png" alt="MICRO MOTION™" style="max-height: 38px; max-width: 130px; object-fit: contain; filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #cbd5e1; color: #0f172a; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(203, 213, 225, 0.45);">MICRO MOTION™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/micro-motion-5700" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(203, 213, 225, 0.18); border: 1px solid rgba(203, 213, 225, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#cbd5e1'; this.style.color='#0f172a'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(203, 213, 225, 0.18)'; this.style.color='#ffffff'; this.style.transform='none';">
                                                <span>Catálogo Micro Motion en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO 3D FLIP CARD ELEGANTE -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Tarjeta Flip 3D: Front = Logo Micro Motion / Back = Equipo -->
                                        <div class="col-12 col-lg-6 col-xl-5 d-flex justify-content-center">
                                            <div class="single-product-flip3d" onclick="this.classList.toggle('is-flipped');" title="Pasa el ratón o toca para girar la tarjeta">
                                                <div class="flip3d-inner" style="border: 1.5px solid rgba(203, 213, 225, 0.45); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 25px rgba(203, 213, 225, 0.25);">
                                                    <!-- Cara Frontal con Logo Propio -->
                                                    <div class="flip3d-front" style="background: linear-gradient(145deg, rgba(20, 26, 38, 0.96) 0%, rgba(2, 6, 23, 0.98) 100%);">
                                                        <div class="brand-emblem-plate mb-2" style="border: 2px solid rgba(203, 213, 225, 0.4);">
                                                            <img src="img/products/micromotion/micromotion.png" alt="MICRO MOTION™" style="max-height: 48px; max-width: 160px; object-fit: contain;">
                                                        </div>
                                                        <div class="text-secondary small fw-semibold mt-2" style="color: #cbd5e1 !important; letter-spacing: 0.5px;">Coriolis Flow &amp; Density Measurement</div>
                                                        <span class="flip-hint-badge"><i class="fas fa-sync-alt me-1"></i> Toca o pasa el ratón para ver equipo</span>
                                                    </div>
                                                    <!-- Cara Trasera con Foto de Producto -->
                                                    <div class="flip3d-back" onclick="event.stopPropagation(); expandMediaFromElement(this);" title="Haga clic para pantalla completa" style="background: radial-gradient(circle, rgba(203, 213, 225, 0.22) 0%, rgba(2, 6, 23, 0.98) 80%); cursor: pointer;">
                                                        <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                        <img src="img/products/micromotion/Micro Motion™ 5700 Field-Mount Transmitter.jpeg" alt="Micro Motion™ 5700 Field-Mount Transmitter">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Panel Descriptivo del Producto -->
                                        <div class="col-12 col-lg-6 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: #cbd5e1; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">Coriolis Flow Transmitter</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">Micro Motion™ 5700 Field-Mount Transmitter</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">Transmisor de caudal y densidad Coriolis de montaje en campo avanzado con verificación inteligente del medidor y registro de datos nativo.</p>
                                                
                                                <div class="d-flex align-items-center">
                                                    <a href="https://www.emerson.com/es-es/catalog/micro-motion-5700" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(203, 213, 225, 0.25); border: 1px solid rgba(203, 213, 225, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#cbd5e1'; this.style.color='#0f172a';" onmouseout="this.style.background='rgba(203, 213, 225, 0.25)'; this.style.color='#ffffff';">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # =========================================================================
    # 6. FLUENTA (Verde #22c55e) - 1 GRANDE + 5 COMPACTOS (5º CENTRADO)
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: FLUENTA™ (GAS FLARE MEASUREMENT)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-fluenta">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(34, 197, 94, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(34, 197, 94, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(34, 197, 94, 0.35); border: 1px solid rgba(34, 197, 94, 0.4);">
                                                <img src="img/products/fluenta/Fluenta-blog-logo.png" alt="FLUENTA™" style="max-height: 38px; max-width: 130px; object-fit: contain; filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #22c55e; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(34, 197, 94, 0.45);">FLUENTA™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.fluenta.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(34, 197, 94, 0.18); border: 1px solid rgba(34, 197, 94, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#22c55e'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(34, 197, 94, 0.18)'; this.style.transform='none';">
                                                <span>Portal Oficial Fluenta</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO: 1 GRANDE + 5 COMPACTOS (5º CENTRADO) -->
                                    <div class="row g-3 align-items-stretch">
                                        <!-- 1 GRANDE EN LA IZQUIERDA -->
                                        <div class="col-12 col-xl-6">
                                            <div class="featured-large-product-card rounded-3 overflow-hidden position-relative h-100 d-flex flex-column justify-content-between" style="min-height: 440px; background: rgba(2, 6, 23, 0.8); border: 1.5px solid rgba(34, 197, 94, 0.45); box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                                                <div class="featured-media-stage position-relative flex-grow-1 d-flex align-items-center justify-content-center p-4" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: radial-gradient(circle, rgba(34, 197, 94, 0.28) 0%, rgba(2, 6, 23, 0.6) 80%); cursor: pointer; min-height: 250px;">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/fluenta/Fluenta TFS Ultrasonic Transducers.jpeg" alt="Fluenta TFS Ultrasonic Transducers" class="featured-hero-img" style="max-height: 230px; max-width: 88%; object-fit: contain; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5)); transition: transform 0.35s ease;">
                                                </div>
                                                
                                                <!-- Overlay inferior con Blur, Título, Descripción y Enlace -->
                                                <div class="featured-bottom-info p-3 p-md-4" style="background: linear-gradient(0deg, rgba(2, 6, 23, 0.96) 0%, rgba(2, 6, 23, 0.85) 75%, transparent 100%); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                    <span class="badge mb-2 fw-bold" style="background: #22c55e; color: #ffffff; font-size: 0.72rem; letter-spacing: 0.5px;">Flare Gas Measurement</span>
                                                    <h4 class="fw-bold text-white mb-2 fs-5" style="line-height: 1.35;">Fluenta TFS Ultrasonic Transducers</h4>
                                                    <p class="small text-white-50 mb-3" style="font-size: 0.84rem; line-height: 1.5;">Transductores ultrasónicos de alta precisión para medición de gas de antorcha en condiciones químicas severas.</p>
                                                    <div class="d-flex align-items-center">
                                                        <a href="https://www.fluenta.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(34, 197, 94, 0.25); border: 1px solid rgba(34, 197, 94, 0.5); font-size: 0.80rem;">
                                                            <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- COMPACTOS EN LA DERECHA (EXPANDIDOS HASTA ABAJO + 5º CENTRADO) -->
                                        <div class="col-12 col-xl-6">
                                            <div class="compact-products-grid h-100">
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(34, 197, 94, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/fluenta/FlarePhase 250.jpeg" alt="FlarePhase 250" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="FlarePhase 250">FlarePhase 250</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(34, 197, 94, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/fluenta/FlarePhase 350.jpeg" alt="FlarePhase 350" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="FlarePhase 350">FlarePhase 350</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(34, 197, 94, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/fluenta/Fluenta TFS-55.jpeg" alt="Fluenta TFS-55" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Fluenta TFS-55">Fluenta TFS-55</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(34, 197, 94, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/fluenta/Single-Path Configurations.jpeg" alt="Single-Path Configurations" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Single-Path Configurations">Single-Path Configurations</div>
                                                    </div>
                                                </div>
                                                
                                                <!-- 5º PRODUCTO (IMPAR) CENTRADO -->
                                                <div class="compact-product-card compact-card-centered-odd rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(34, 197, 94, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/fluenta/Dual-Path Configurations.jpeg" alt="Dual-Path Configurations" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Dual-Path Configurations">Dual-Path Configurations</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # =========================================================================
    # 7. KAM CONTROLS (Naranja #f97316) - 1 GRANDE + 7 COMPACTOS (7º CENTRADO)
    # =========================================================================
    html.append('''
                            <!-- ========================================================
                                 BRAND SECTION: KAM CONTROLS™ (OPTICAL & WATERCUT SENSORS)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-kam">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(249, 115, 22, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(249, 115, 22, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(249, 115, 22, 0.35); border: 1px solid rgba(249, 115, 22, 0.4);">
                                                <img src="img/products/kam/kam_logo.png" alt="KAM CONTROLS™" style="max-height: 38px; max-width: 130px; object-fit: contain; filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #f97316; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(249, 115, 22, 0.45);">KAM CONTROLS™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://kam.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(249, 115, 22, 0.18); border: 1px solid rgba(249, 115, 22, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#f97316'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(249, 115, 22, 0.18)'; this.style.transform='none';">
                                                <span>Portal Oficial Kam Controls</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO: 1 GRANDE + 7 COMPACTOS (7º CENTRADO) -->
                                    <div class="row g-3 align-items-stretch">
                                        <!-- 1 GRANDE EN LA IZQUIERDA -->
                                        <div class="col-12 col-xl-6">
                                            <div class="featured-large-product-card rounded-3 overflow-hidden position-relative h-100 d-flex flex-column justify-content-between" style="min-height: 440px; background: rgba(2, 6, 23, 0.8); border: 1.5px solid rgba(249, 115, 22, 0.45); box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                                                <div class="featured-media-stage position-relative flex-grow-1 d-flex align-items-center justify-content-center p-4" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.28) 0%, rgba(2, 6, 23, 0.6) 80%); cursor: pointer; min-height: 250px;">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-3" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/kam/OWD Watercut Meter.jpeg" alt="OWD Watercut Meter" class="featured-hero-img" style="max-height: 230px; max-width: 88%; object-fit: contain; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5)); transition: transform 0.35s ease;">
                                                </div>
                                                
                                                <!-- Overlay inferior con Blur, Título, Descripción y Enlace -->
                                                <div class="featured-bottom-info p-3 p-md-4" style="background: linear-gradient(0deg, rgba(2, 6, 23, 0.96) 0%, rgba(2, 6, 23, 0.85) 75%, transparent 100%); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                    <span class="badge mb-2 fw-bold" style="background: #f97316; color: #ffffff; font-size: 0.72rem; letter-spacing: 0.5px;">Watercut &amp; BS&amp;W</span>
                                                    <h4 class="fw-bold text-white mb-2 fs-5" style="line-height: 1.35;">OWD Watercut Meter</h4>
                                                    <p class="small text-white-50 mb-3" style="font-size: 0.84rem; line-height: 1.5;">Medidor patentado de corte de agua en línea para transferencia de custodia y monitoreo de pozos con máxima precisión.</p>
                                                    <div class="d-flex align-items-center">
                                                        <a href="https://kam.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-3 py-1 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-1" style="background: rgba(249, 115, 22, 0.25); border: 1px solid rgba(249, 115, 22, 0.5); font-size: 0.80rem;">
                                                            <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small ms-1"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- COMPACTOS EN LA DERECHA (EXPANDIDOS HASTA ABAJO + 7º CENTRADO) -->
                                        <div class="col-12 col-xl-6">
                                            <div class="compact-products-grid h-100">
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/ATD Automatic Tank Dewatering System.jpeg" alt="ATD Automatic Tank Dewatering System" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="ATD Automatic Tank Dewatering System">ATD Automatic Tank Dewatering System</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/E-IAS Electric Isokinetic Automatic Sampler.jpeg" alt="E-IAS Electric Isokinetic Automatic Sampler" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="E-IAS Electric Isokinetic Automatic Sampler">E-IAS Electric Isokinetic Automatic Sampler</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/IAS Isokinetic Automatic Sampler.jpeg" alt="IAS Isokinetic Automatic Sampler" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="IAS Isokinetic Automatic Sampler">IAS Isokinetic Automatic Sampler</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/KF Karl Fischer Moisture Analyzer.jpeg" alt="KF Karl Fischer Moisture Analyzer" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="KF Karl Fischer Moisture Analyzer">KF Karl Fischer Moisture Analyzer</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/SMP Static Mixing Plate.jpeg" alt="SMP Static Mixing Plate" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="SMP Static Mixing Plate">SMP Static Mixing Plate</div>
                                                    </div>
                                                </div>
                                                
                                                <div class="compact-product-card rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/SMS Static Mixing Spool.jpeg" alt="SMS Static Mixing Spool" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="SMS Static Mixing Spool">SMS Static Mixing Spool</div>
                                                    </div>
                                                </div>
                                                
                                                <!-- 7º PRODUCTO (IMPAR) CENTRADO -->
                                                <div class="compact-product-card compact-card-centered-odd rounded-3 overflow-hidden position-relative" onclick="expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa" style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer;">
                                                    <div class="compact-media-wrap" style="background: radial-gradient(circle, rgba(249, 115, 22, 0.20) 0%, rgba(2, 6, 23, 0.5) 80%);">
                                                        <img src="img/products/kam/OWD Watercut Meter.jpeg" alt="Kam Controls Precision Sensor" class="compact-product-img">
                                                    </div>
                                                    <div class="compact-title-bar p-2" style="background: rgba(2, 6, 23, 0.88); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                                        <div class="text-white small fw-bold text-truncate" style="font-size: 0.80rem;" title="Kam Controls Precision Sensor">Kam Controls Precision Sensor</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>''')

    # Close wrappers
    html.append('''                        </div>
                    </div>
                </li>''')

    return "\n".join(html)

if __name__ == '__main__':
    content = generate_section5()
    with open('scratch/generated_section5_v2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated section 5 v2 successfully! Size:", len(content))
