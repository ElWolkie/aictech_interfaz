with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = []
def check(name, condition, details=""):
    status = "PASS" if condition else "FAIL"
    checks.append((name, status, details))
    print(f"[{status}] {name} {details}")

# 1. Emerson accordion in sidebar
check("Emerson nested toggle exists", 'id="emerson-nested-toggle"' in text)
check("Emerson nested menu exists", 'id="emerson-nested-menu"' in text)
check("Roxar in Emerson menu", 'href="#producto-brand-roxar"' in text)
check("Rosemount in Emerson menu", 'href="#producto-brand-rosemount"' in text)
check("Micro Motion in Emerson menu", 'href="#producto-brand-micromotion"' in text)
check("Flexim in Emerson menu", 'href="#producto-brand-flexim"' in text)
check("AMS Trex in Emerson menu", 'href="#producto-brand-amstrex"' in text)
check("Fluenta outside Emerson", 'href="#producto-brand-fluenta"' in text)
check("Kam outside Emerson", 'href="#producto-brand-kam"' in text)

# 2. Section 5 Products Brands
p5_text = text[text.find('data-page-no="5"'):text.find('data-page-no="6"')]
check("Roxar section in Page 5", 'id="producto-brand-roxar"' in p5_text)
check("Rosemount section in Page 5", 'id="producto-brand-rosemount"' in p5_text)
check("Micro Motion section in Page 5", 'id="producto-brand-micromotion"' in p5_text)
check("Flexim section in Page 5", 'id="producto-brand-flexim"' in p5_text)
check("AMS Trex section in Page 5", 'id="producto-brand-amstrex"' in p5_text)
check("Fluenta section in Page 5", 'id="producto-brand-fluenta"' in p5_text)
check("Kam section in Page 5", 'id="producto-brand-kam"' in p5_text)

# 3. Product Cards & Counts
check("Roxar 5 products exist", p5_text.count('img/products/roxar/') >= 6) # 5 products + logo
check("Rosemount 4 products exist", p5_text.count('img/products/rosemount/') >= 5) # 4 products + banner
check("Micro Motion 5700 exists", 'Micro Motion™ 5700 Field-Mount Transmitter' in p5_text)
check("Flexim F631 exists", 'FLUXUS® F631 BA' in p5_text)
check("AMS Trex exists", 'AMS Trex™ Device Communicator' in p5_text)
check("Fluenta 6 products exist", p5_text.count('img/products/fluenta/') >= 7) # 6 products + logo
check("Kam 7 products exist", p5_text.count('img/products/kam/') >= 8) # 7 products + logo
check("Kam logo has clean white wrapper", 'bg-white rounded-2 px-3 py-1 shadow-sm' in p5_text and 'img/products/kam/kam_logo.png' in p5_text)

# 4. Playful hover CSS & details buttons
check("Playful hover CSS scale(0.88)", 'transform: scale(0.88);' in text)
check("Ver más detalles buttons exist", p5_text.count('emerson-details-btn') >= 24)

# 5. Logo restoration in sidebar and mobile header
sidebar_head = text[text.find('class="sidebar-heading'):text.find('id="main-sidebar-nav"')]
check("Sidebar logo has no white badge", 'sidebar-brand-badge' not in sidebar_head)
navbar_mobile = text[text.find('id="menu-toggle"')-200:text.find('id="menu-toggle"')]
check("Mobile logo has no white badge", 'sidebar-brand-badge' not in navbar_mobile)

# 6. Blue pills & Certifications removed from Section 5 header
check("No ALIANZA ESTRATÉGICA pill in Section 5 header", 'class="emerson-badge-pill"' not in p5_text)
check("No Certificaciones text in Section 5 header", 'Certificaciones ATEX' not in p5_text)

# 7. Blue blocks removed from all service card backs
p2_text = text[text.find('data-page-no="2"'):text.find('data-page-no="3"')]
check("Zero blue badge blocks in Section 2 card backs", 'bg-primary bg-opacity-10 text-primary' not in p2_text)

# 8. Hero video object-fit cover
check("Hero video has object-fit cover", 'object-fit: cover !important;' in text)

# 9. Sidebar collapse fluid expansion in CSS
with open('css/sidebar-collapse.css', 'r', encoding='utf-8') as f:
    collapse_css = f.read()
check("Sidebar collapse CSS expands services and catalog wrappers", 'body.sidebar-collapsed .services-feed-wrapper' in collapse_css)
check("Sidebar collapse CSS expands hero container", 'body.sidebar-collapsed .hero-slb-container' in collapse_css)

# 10. JS functions
check("expandMediaFromElement function exists", 'window.expandMediaFromElement' in text)
check("pauseAllBackgroundVideos function exists", 'window.pauseAllBackgroundVideos' in text)

passed = sum(1 for c in checks if c[1] == "PASS")
total = len(checks)
print(f"\n==========================================")
print(f"RESULT: {passed}/{total} CHECKS PASSED!")
print(f"==========================================")
