# Script to build the updated articles for Flexim, AMS Trex, and Micro Motion
# with the card that opens from the center, colors matching the product,
# and strictly original text (no extra/invented bullet points).

css_to_add = """
        /* ============================================================= */
        /* TARJETAS QUE SE ABREN DESDE EL CENTRO (FLIP GATEFOLD DOORS)   */
        /* ============================================================= */
        .center-split-card-wrapper {
            position: relative;
            width: 100%;
            max-width: 360px;
            height: 270px;
            perspective: 1200px;
            border-radius: 14px;
            cursor: pointer;
            user-select: none;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin: 0 auto;
        }

        @media (min-width: 576px) {
            .center-split-card-wrapper {
                max-width: 410px;
                height: 295px;
            }
        }

        .center-split-card-wrapper:hover {
            transform: translateY(-4px);
            box-shadow: 0 22px 50px rgba(0, 0, 0, 0.75);
        }

        /* Interior: Foto de alta definición del producto sobre fondo blanco */
        .center-split-interior {
            position: absolute;
            inset: 0;
            background: #ffffff;
            border-radius: 14px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 18px;
            z-index: 1;
            box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }
        .center-split-interior img {
            max-width: 90%;
            max-height: 85%;
            object-fit: contain;
            transition: transform 0.4s ease;
        }
        .center-split-card-wrapper:hover .center-split-interior img {
            transform: scale(1.06);
        }

        /* Puertas que se abren desde el centro */
        .center-split-door {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            z-index: 5;
            transform-style: preserve-3d;
            transition: transform 0.7s cubic-bezier(0.34, 1.25, 0.64, 1);
            will-change: transform;
        }

        .center-split-door-left {
            left: 0;
            transform-origin: left center;
        }

        .center-split-door-right {
            right: 0;
            transform-origin: right center;
        }

        /* Cara frontal de las puertas */
        .door-face-front {
            position: absolute;
            inset: 0;
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
            overflow: hidden;
            box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.35);
        }

        .center-split-door-left .door-face-front {
            border-radius: 14px 0 0 14px;
            border-right: 1px solid rgba(255, 255, 255, 0.35);
        }

        .center-split-door-right .door-face-front {
            border-radius: 0 14px 14px 0;
            border-left: 1px solid rgba(0, 0, 0, 0.35);
        }

        /* Cara trasera de las puertas (vista al abrirse) */
        .door-face-back {
            position: absolute;
            inset: 0;
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
            transform: rotateY(180deg);
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
        }

        .center-split-door-left .door-face-back {
            border-radius: 14px 0 0 14px;
        }

        .center-split-door-right .door-face-back {
            border-radius: 0 14px 14px 0;
        }

        /* Animación de apertura desde el centro */
        .center-split-card-wrapper:hover .center-split-door-left,
        .center-split-card-wrapper.is-open .center-split-door-left {
            transform: rotateY(-140deg);
        }

        .center-split-card-wrapper:hover .center-split-door-right,
        .center-split-card-wrapper.is-open .center-split-door-right {
            transform: rotateY(140deg);
        }

        /* Colores exactos de las marcas */
        .door-bg-flexim {
            background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%);
        }
        .door-bg-amstrex {
            background: linear-gradient(135deg, #475569 0%, #334155 100%);
        }
        .door-bg-micromotion {
            background: linear-gradient(135deg, #94a3b8 0%, #64748b 100%);
        }

        /* Sello / Círculo central en las puertas */
        .center-split-seal-half-left {
            position: absolute;
            right: -48px;
            top: 50%;
            transform: translateY(-50%);
            width: 96px;
            height: 96px;
            border-radius: 50%;
            background: #ffffff;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            z-index: 10;
        }

        .center-split-seal-half-right {
            position: absolute;
            left: -48px;
            top: 50%;
            transform: translateY(-50%);
            width: 96px;
            height: 96px;
            border-radius: 50%;
            background: #ffffff;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            z-index: 10;
        }

        /* Indicador de toque / hover */
        .door-hint {
            position: absolute;
            bottom: 12px;
            color: rgba(255, 255, 255, 0.95);
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            text-shadow: 0 1px 4px rgba(0,0,0,0.5);
            white-space: nowrap;
        }
        .door-hint-left {
            right: 8px;
        }
        .door-hint-right {
            left: 8px;
        }
"""

flexim_html = """                            <!-- ========================================================
                                 2. FLEXIM (Aguamarina - Tarjeta que Abre desde el Centro)
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
                                    
                                    <!-- FORMATO TARJETA QUE ABRE DESDE EL CENTRO -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Columna Izquierda: Tarjeta que se abre desde el centro (Aguamarina) -->
                                        <div class="col-12 col-lg-5 col-xl-5 d-flex justify-content-center">
                                            <div class="center-split-card-wrapper" onclick="this.classList.toggle('is-open');" title="Pasa el ratón o toca para abrir desde el centro">
                                                <!-- Interior: Foto del equipo en alta definición -->
                                                <div class="center-split-interior" onclick="event.stopPropagation(); expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-2" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg" alt="FLUXUS® F631 BA - Caudalímetro Portátil para Líquidos">
                                                </div>
                                                <!-- Puerta Izquierda -->
                                                <div class="center-split-door center-split-door-left">
                                                    <div class="door-face-front door-bg-flexim">
                                                        <div class="center-split-seal-half-left">
                                                            <img src="img/products/flexim/Flexim-Logo.png" alt="FLEXIM™" style="max-height: 42px; max-width: 84px; object-fit: contain; transform: translateX(42px);">
                                                        </div>
                                                        <div class="door-hint door-hint-left">Toca o pasa el ratón</div>
                                                    </div>
                                                    <div class="door-face-back"></div>
                                                </div>
                                                <!-- Puerta Derecha -->
                                                <div class="center-split-door center-split-door-right">
                                                    <div class="door-face-front door-bg-flexim">
                                                        <div class="center-split-seal-half-right">
                                                            <img src="img/products/flexim/Flexim-Logo.png" alt="FLEXIM™" style="max-height: 42px; max-width: 84px; object-fit: contain; transform: translateX(-42px);">
                                                        </div>
                                                        <div class="door-hint door-hint-right">para abrir sobre</div>
                                                    </div>
                                                    <div class="door-face-back"></div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Columna Derecha: Panel Técnico Original (Sin textos inventados) -->
                                        <div class="col-12 col-lg-7 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: #14b8a6; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">Clamp-On Ultrasonic Flow Meter</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">FLUXUS® F631 BA - Caudalímetro Portátil para Líquidos</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">Medidor de flujo ultrasónico portátil no invasivo clamp-on para líquidos y gases sin cortes de tubería ni paradas operativas.</p>
                                                
                                                <div class="d-flex align-items-center">
                                                    <a href="https://www.emerson.com/es-es/catalog/flexim-fluxus-f631" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-4 py-2 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(20, 184, 166, 0.25); border: 1px solid rgba(20, 184, 166, 0.6); font-size: 0.85rem; transition: all 0.25s ease;" onmouseover="this.style.background='#14b8a6'; this.style.color='#ffffff'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(20, 184, 166, 0.25)'; this.style.color='#ffffff'; this.style.transform='none';">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>"""

amstrex_html = """                            <!-- ========================================================
                                 3. AMS TREX (Negrito claro - Tarjeta que Abre desde el Centro)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-amstrex">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(148, 163, 184, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(148, 163, 184, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(148, 163, 184, 0.35); border: 1px solid rgba(148, 163, 184, 0.4);">
                                                <img src="img/brands/emerson.png" alt="Emerson - AMS Trex" style="max-height: 38px; max-width: 130px; object-fit: contain; transform: scale(1.05); filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #475569; color: #ffffff; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(71, 85, 105, 0.45);">AMS TREX™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/ams-trex-device-communicator" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(148, 163, 184, 0.18); border: 1px solid rgba(148, 163, 184, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#475569'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(148, 163, 184, 0.18)'; this.style.transform='none';">
                                                <span>Catálogo AMS Trex en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO TARJETA QUE ABRE DESDE EL CENTRO -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Columna Izquierda: Tarjeta que se abre desde el centro (Negrito Claro) -->
                                        <div class="col-12 col-lg-5 col-xl-5 d-flex justify-content-center">
                                            <div class="center-split-card-wrapper" onclick="this.classList.toggle('is-open');" title="Pasa el ratón o toca para abrir desde el centro">
                                                <!-- Interior: Foto del equipo en alta definición -->
                                                <div class="center-split-interior" onclick="event.stopPropagation(); expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-2" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg" alt="AMS Trex™ Device Communicator">
                                                </div>
                                                <!-- Puerta Izquierda -->
                                                <div class="center-split-door center-split-door-left">
                                                    <div class="door-face-front door-bg-amstrex">
                                                        <div class="center-split-seal-half-left">
                                                            <img src="img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg" alt="AMS Trex" style="max-height: 72px; max-width: 72px; object-fit: contain; transform: translateX(36px);">
                                                        </div>
                                                        <div class="door-hint door-hint-left">Toca o pasa el ratón</div>
                                                    </div>
                                                    <div class="door-face-back"></div>
                                                </div>
                                                <!-- Puerta Derecha -->
                                                <div class="center-split-door center-split-door-right">
                                                    <div class="door-face-front door-bg-amstrex">
                                                        <div class="center-split-seal-half-right">
                                                            <img src="img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg" alt="AMS Trex" style="max-height: 72px; max-width: 72px; object-fit: contain; transform: translateX(-36px);">
                                                        </div>
                                                        <div class="door-hint door-hint-right">para abrir sobre</div>
                                                    </div>
                                                    <div class="door-face-back"></div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Columna Derecha: Panel Técnico Original (Sin textos inventados) -->
                                        <div class="col-12 col-lg-7 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">Field Communicator & Diagnostics</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">AMS Trex™ Device Communicator</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">Comunicador de campo de alta resistencia con pantalla táctil intuitiva y soporte para dispositivos HART y FOUNDATION Fieldbus con alimentación directa de lazo.</p>
                                                
                                                <div class="d-flex align-items-center">
                                                    <a href="https://www.emerson.com/es-es/catalog/ams-trex-device-communicator" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-4 py-2 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(148, 163, 184, 0.25); border: 1px solid rgba(148, 163, 184, 0.6); font-size: 0.85rem; transition: all 0.25s ease;" onmouseover="this.style.background='#475569'; this.style.color='#ffffff'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(148, 163, 184, 0.25)'; this.style.color='#ffffff'; this.style.transform='none';">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>"""

micromotion_html = """                            <!-- ========================================================
                                 5. MICRO MOTION (Gris - Tarjeta que Abre desde el Centro)
                                 ======================================================== -->
                            <article class="brand-snapping-card-section reveal-on-scroll reveal-up mb-5 is-3d-card" id="producto-brand-micromotion">
                                <div class="brand-showcase-shell p-3 p-lg-4 rounded-4" style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.94) 0%, rgba(8, 14, 26, 0.97) 100%); border: 1.5px solid rgba(203, 213, 225, 0.35); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(203, 213, 225, 0.15); backdrop-filter: blur(20px);">
                                    
                                    <!-- Barra Superior de Marca -->
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
                                        <div class="d-flex align-items-center gap-3">
                                            <div class="brand-header-logo-plate rounded-3 px-3 py-1 d-flex align-items-center justify-content-center" style="height: 52px; background: rgba(255, 255, 255, 0.96); box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 15px rgba(203, 213, 225, 0.35); border: 1px solid rgba(203, 213, 225, 0.4);">
                                                <img src="img/products/micromotion/micromotion.png" alt="Micro Motion" style="max-height: 38px; max-width: 130px; object-fit: contain; transform: scale(1.05); filter: drop-shadow(0 1px 4px rgba(0,0,0,0.15));">
                                            </div>
                                            <div>
                                                <span class="badge px-3 py-1 fw-bold fs-6" style="background: #94a3b8; color: #0f172a; letter-spacing: 0.8px; box-shadow: 0 0 16px rgba(148, 163, 184, 0.45);">MICRO MOTION™</span>
                                            </div>
                                        </div>
                                        <div class="mt-2 mt-md-0">
                                            <a href="https://www.emerson.com/es-es/catalog/micro-motion-5700" target="_blank" rel="noopener noreferrer" class="btn btn-sm py-2 px-3 fw-bold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(203, 213, 225, 0.18); border: 1px solid rgba(203, 213, 225, 0.5); font-size: 0.82rem; transition: all 0.25s ease;" onmouseover="this.style.background='#94a3b8'; this.style.color='#0f172a'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(203, 213, 225, 0.18)'; this.style.color='#ffffff'; this.style.transform='none';">
                                                <span>Catálogo Micro Motion en Emerson</span> <i class="fas fa-arrow-up-right-from-square"></i>
                                            </a>
                                        </div>
                                    </div>
                                    
                                    <!-- FORMATO TARJETA QUE ABRE DESDE EL CENTRO -->
                                    <div class="row g-4 align-items-center justify-content-center py-2">
                                        
                                        <!-- Columna Izquierda: Tarjeta que se abre desde el centro (Gris) -->
                                        <div class="col-12 col-lg-5 col-xl-5 d-flex justify-content-center">
                                            <div class="center-split-card-wrapper" onclick="this.classList.toggle('is-open');" title="Pasa el ratón o toca para abrir desde el centro">
                                                <!-- Interior: Foto del equipo en alta definición -->
                                                <div class="center-split-interior" onclick="event.stopPropagation(); expandMediaFromElement(this);" title="Haga clic para ver en pantalla completa">
                                                    <button type="button" class="product-expand-badge position-absolute top-0 end-0 m-2" title="Agrandar"><i class="fas fa-expand"></i></button>
                                                    <img src="img/products/micromotion/Micro Motion™ 5700 Field-Mount Transmitter.jpeg" alt="Micro Motion™ 5700 Field-Mount Transmitter">
                                                </div>
                                                <!-- Puerta Izquierda -->
                                                <div class="center-split-door center-split-door-left">
                                                    <div class="door-face-front door-bg-micromotion">
                                                        <div class="center-split-seal-half-left">
                                                            <img src="img/products/micromotion/micromotion.png" alt="Micro Motion" style="max-height: 42px; max-width: 84px; object-fit: contain; transform: translateX(42px);">
                                                        </div>
                                                        <div class="door-hint door-hint-left">Toca o pasa el ratón</div>
                                                    </div>
                                                    <div class="door-face-back"></div>
                                                </div>
                                                <!-- Puerta Derecha -->
                                                <div class="center-split-door center-split-door-right">
                                                    <div class="door-face-front door-bg-micromotion">
                                                        <div class="center-split-seal-half-right">
                                                            <img src="img/products/micromotion/micromotion.png" alt="Micro Motion" style="max-height: 42px; max-width: 84px; object-fit: contain; transform: translateX(-42px);">
                                                        </div>
                                                        <div class="door-hint door-hint-right">para abrir sobre</div>
                                                    </div>
                                                    <div class="door-face-back"></div>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Columna Derecha: Panel Técnico Original (Sin textos inventados) -->
                                        <div class="col-12 col-lg-7 col-xl-7">
                                            <div class="p-3 p-md-4 rounded-3" style="background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                                                <span class="product-category-tag mb-2 d-inline-block" style="font-size: 0.75rem; color: #cbd5e1; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">Coriolis Flow Transmitter</span>
                                                <h3 class="fw-bold fs-4 text-white mb-3" style="line-height: 1.3;">Micro Motion™ 5700 Field-Mount Transmitter</h3>
                                                <p class="mb-4" style="font-size: 0.95rem; line-height: 1.65; color: #cbd5e1;">Transmisor de caudal másico y densidad Coriolis para transferencia de custodia y procesos críticos.</p>
                                                
                                                <div class="d-flex align-items-center">
                                                    <a href="https://www.emerson.com/es-es/catalog/micro-motion-5700" target="_blank" rel="noopener noreferrer" class="btn btn-sm px-4 py-2 fw-semibold text-white rounded-pill d-inline-flex align-items-center gap-2" style="background: rgba(203, 213, 225, 0.25); border: 1px solid rgba(203, 213, 225, 0.6); font-size: 0.85rem; transition: all 0.25s ease;" onmouseover="this.style.background='#94a3b8'; this.style.color='#0f172a'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(203, 213, 225, 0.25)'; this.style.color='#ffffff'; this.style.transform='none';">
                                                        <span>Ver más detalles</span> <i class="fas fa-arrow-up-right-from-square small"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </article>"""

print("Lengths:")
print("CSS:", len(css_to_add))
print("Flexim:", len(flexim_html))
print("AMS Trex:", len(amstrex_html))
print("Micro Motion:", len(micromotion_html))
