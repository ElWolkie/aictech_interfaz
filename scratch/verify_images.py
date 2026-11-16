import os

# Script para construir el catálogo completo de productos
# Verificamos que todas las imágenes existen
images = [
    "img/products/roxar/2600.jpeg",
    "img/products/roxar/water-cut-meter.jpeg",
    "img/products/roxar/Multifasico-para-instalaciones-SubSea.jpeg",
    "img/products/roxar/Medidor de Wet Gas SubSea.jpeg",
    "img/products/roxar/Medidor de Salinidad (Complemento del 2600).jpeg",
    "img/products/roxar/roxar.png",
    "img/products/rosemount/Rosemount-New-Logo.jpeg",
    "img/products/rosemount/Rosemount™ 8800 Reducer Vortex Flow Meter.jpeg",
    "img/products/rosemount/Rosemount™ 8600 Vortex Flow Meters.jpeg",
    "img/products/rosemount/Rosemount™ 5300 Level Transmitter - Guided Wave Radar.jpeg",
    "img/products/rosemount/Transmisor de nivel Rosemount 5300 - Radar de onda guiada.jpeg",
    "img/products/micromotion/micromotion.jpg",
    "img/products/micromotion/Micro Motion™ 5700 Field-Mount Transmitter.jpeg",
    "img/products/flexim/Flexim-Logo.png",
    "img/products/flexim/Flexim™ FLUXUS F631 BA - Portable Liquid Clamp-on Ultrasonic Flow Meter.jpeg",
    "img/products/ams trex/ams-trex-banner.jpg",
    "img/products/ams trex/AMS Trex Device Communicator wins Gold Award.jpeg",
    "img/products/fluenta/Fluenta-blog-logo.png",
    "img/products/fluenta/Single-Path Configurations.jpeg",
    "img/products/fluenta/Dual-Path Configurations.jpeg",
    "img/products/fluenta/FlarePhase 250.jpeg",
    "img/products/fluenta/FlarePhase 350.jpeg",
    "img/products/fluenta/Fluenta TFS Ultrasonic Transducers.jpeg",
    "img/products/fluenta/Fluenta TFS-55.jpeg",
    "img/products/kam/kam_logo.png",
    "img/products/kam/OWD Watercut Meter.jpeg",
    "img/products/kam/KF Karl Fischer Moisture Analyzer.jpeg",
    "img/products/kam/ATD Automatic Tank Dewatering System.jpeg",
    "img/products/kam/IAS Isokinetic Automatic Sampler.jpeg",
    "img/products/kam/E-IAS Electric Isokinetic Automatic Sampler.jpeg",
    "img/products/kam/SMP Static Mixing Plate.jpeg",
    "img/products/kam/SMS Static Mixing Spool.jpeg"
]

missing = []
for img in images:
    if not os.path.exists(img):
        missing.append(img)

if missing:
    print(f"ERROR: {len(missing)} images missing:")
    for m in missing:
        print("  -", m)
else:
    print(f"SUCCESS: All {len(images)} images exist on disk!")
