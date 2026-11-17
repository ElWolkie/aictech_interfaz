# -*- coding: utf-8 -*-
"""
Applies the refined section 5 and sidenav changes to index.html:
1. Replaces <li data-page-no="5"...>...</li> with scratch/generated_section5_v2.html.
2. Removes .submenu-dot from #productos-submenu.
3. Updates the watermark CSS to have white luminous logos with smooth mask gradient fade.
4. Adds CSS for .single-product-flip3d, .compact-products-grid, and .compact-card-centered-odd.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Section 5
pos_li5 = content.find('<li data-page-no="5"')
pos_li6 = content.find('<li data-page-no="6"')
assert pos_li5 != -1 and pos_li6 != -1, "Could not find li data-page-no=5 or 6"

with open('scratch/generated_section5_v2.html', 'r', encoding='utf-8') as f:
    new_sec5 = f.read()

content = content[:pos_li5] + new_sec5 + '\n\n                ' + content[pos_li6:]

# 2. Update Sidenav: Remove dots inside #productos-submenu
pos_submenu = content.find('id="productos-submenu"')
pos_end_submenu = content.find('<!-- 2. SERVICIOS', pos_submenu)
assert pos_submenu != -1 and pos_end_submenu != -1, "Could not find productos-submenu bounds"

submenu_html = content[pos_submenu:pos_end_submenu]
# Remove <span class="submenu-dot"...></span>
submenu_clean = re.sub(r'<span class="submenu-dot[^"]*"[^>]*></span>\s*', '', submenu_html)
content = content[:pos_submenu] + submenu_clean + content[pos_end_submenu:]

# 3. Update CSS in head: Replace watermark and card styles
old_watermark_marker = '/* ============================================================= */\n        /* WATERMARK BRAND LOGOS EN EL SIDENAV (FOTO 4)'
pos_wm = content.find(old_watermark_marker)
if pos_wm == -1:
    old_watermark_marker = '/* WATERMARK BRAND LOGOS EN EL SIDENAV (FOTO 4)'
    pos_wm = content.find(old_watermark_marker)

# Find the end of watermark / flip-360 CSS block before </style>
pos_style_end = content.find('</style>', pos_wm)
assert pos_wm != -1 and pos_style_end != -1, "Could not find CSS watermark block"

new_css = '''/* ============================================================= */
        /* WATERMARK BRAND LOGOS EN EL SIDENAV (BLANCO Y DESVANECIDO)    */
        /* ============================================================= */
        #productos-submenu .submenu-dot {
            display: none !important;
        }

        .submenu-nested-header,
        .sidebar-nested-submenu .submenu-link,
        #productos-submenu > a.submenu-link {
            position: relative !important;
            overflow: hidden !important;
            padding-left: 14px !important;
            padding-right: 14px !important;
        }

        #emerson-nested-toggle::before,
        .sidebar-brand-strip-roxar::before,
        .sidebar-brand-strip-flexim::before,
        .sidebar-brand-strip-amstrex::before,
        .sidebar-brand-strip-rosemount::before,
        .sidebar-brand-strip-micromotion::before,
        .sidebar-brand-strip-fluenta::before,
        .sidebar-brand-strip-kam::before {
            content: '';
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            height: 70%;
            width: 82px;
            background-repeat: no-repeat;
            background-position: right center;
            background-size: contain;
            filter: brightness(0) invert(1) drop-shadow(0 0 2px rgba(255, 255, 255, 0.4));
            opacity: 0.38;
            pointer-events: none;
            transition: opacity 0.25s ease, transform 0.25s ease;
            -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,1) 40%, rgba(0,0,0,0) 100%);
            mask-image: linear-gradient(to left, rgba(0,0,0,1) 40%, rgba(0,0,0,0) 100%);
        }

        #emerson-nested-toggle:hover::before,
        .sidebar-brand-strip-roxar:hover::before,
        .sidebar-brand-strip-flexim:hover::before,
        .sidebar-brand-strip-amstrex:hover::before,
        .sidebar-brand-strip-rosemount:hover::before,
        .sidebar-brand-strip-micromotion:hover::before,
        .sidebar-brand-strip-fluenta:hover::before,
        .sidebar-brand-strip-kam:hover::before {
            opacity: 0.85;
            transform: translateY(-50%) scale(1.06);
        }

        #emerson-nested-toggle::before {
            background-image: url('img/products/emerson.png');
            right: 32px;
        }
        .sidebar-brand-strip-roxar::before {
            background-image: url('img/products/roxar/roxar.png');
        }
        .sidebar-brand-strip-flexim::before {
            background-image: url('img/products/flexim/Flexim-Logo.png');
        }
        .sidebar-brand-strip-amstrex::before {
            background-image: url('img/products/emerson.png');
        }
        .sidebar-brand-strip-rosemount::before {
            background-image: url('img/products/rosemount/Rosemount-New-Logo.png');
        }
        .sidebar-brand-strip-micromotion::before {
            background-image: url('img/products/micromotion/micromotion.png');
        }
        .sidebar-brand-strip-fluenta::before {
            background-image: url('img/products/fluenta/Fluenta-blog-logo.png');
        }
        .sidebar-brand-strip-kam::before {
            background-image: url('img/products/kam/kam_logo.png');
        }

        /* ============================================================= */
        /* COMPACT CARDS & GRID EXPANDIDO HASTA ABAJO                    */
        /* ============================================================= */
        .compact-products-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            grid-auto-rows: 1fr;
            gap: 0.65rem;
            height: 100%;
        }

        .compact-card-centered-odd {
            grid-column: 1 / span 2;
            width: 60%;
            justify-self: center;
        }

        @media (max-width: 575px) {
            .compact-products-grid {
                grid-template-columns: 1fr;
                grid-auto-rows: auto;
            }
            .compact-card-centered-odd {
                grid-column: 1;
                width: 100%;
            }
        }

        .compact-product-card {
            height: 100% !important;
            min-height: 185px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease, border-color 0.3s ease;
        }

        .compact-product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6) !important;
            border-color: rgba(56, 182, 255, 0.6) !important;
        }

        .compact-product-card .compact-media-wrap {
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
        }

        .compact-product-card .compact-product-img {
            max-height: 120px;
            max-width: 85%;
            object-fit: contain;
            transition: transform 0.35s ease;
        }

        .compact-product-card:hover .compact-product-img {
            transform: scale(1.1);
        }

        .featured-large-product-card:hover {
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7) !important;
            border-color: rgba(56, 182, 255, 0.7) !important;
        }
        .featured-large-product-card:hover .featured-hero-img {
            transform: scale(1.04);
        }

        /* ============================================================= */
        /* TARJETAS 3D FLIP PARA PRODUCTO ÚNICO (FLEXIM, TREX, MICRO)   */
        /* ============================================================= */
        .single-product-flip3d {
            width: 100%;
            max-width: 420px;
            height: 330px;
            perspective: 1200px;
            cursor: pointer;
            user-select: none;
            margin: 0 auto;
        }

        @media (min-width: 576px) {
            .single-product-flip3d {
                height: 360px;
            }
        }

        .flip3d-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.65s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            border-radius: 16px;
        }

        .single-product-flip3d:hover .flip3d-inner,
        .single-product-flip3d.is-flipped .flip3d-inner {
            transform: rotateY(180deg);
        }

        .flip3d-front,
        .flip3d-back {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
            border: 1.5px solid rgba(255, 255, 255, 0.12);
        }

        .flip3d-front {
            z-index: 2;
            transform: rotateY(0deg);
        }

        .flip3d-back {
            transform: rotateY(180deg);
        }

        .flip3d-front .brand-emblem-plate {
            background: rgba(255, 255, 255, 0.96);
            padding: 16px 28px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35);
            max-width: 80%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease;
        }

        .single-product-flip3d:hover .brand-emblem-plate {
            transform: scale(1.05);
        }

        .flip3d-front .flip-hint-badge {
            position: absolute;
            bottom: 18px;
            font-size: 0.75rem;
            color: rgba(255, 255, 255, 0.65);
            background: rgba(255, 255, 255, 0.08);
            padding: 4px 12px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            letter-spacing: 0.5px;
        }

        .flip3d-back img {
            max-height: 85%;
            max-width: 90%;
            object-fit: contain;
            filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.6));
            transition: transform 0.35s ease;
        }

        .single-product-flip3d:hover .flip3d-back img {
            transform: scale(1.04);
        }
        '''

content = content[:pos_wm] + new_css + '\n    ' + content[pos_style_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied section 5 v2 and sidenav updates successfully! Total index.html size:", len(content))
