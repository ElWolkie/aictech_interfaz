# -*- coding: utf-8 -*-
import re

# 1. Update js/templatemo-script.js
with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

old_toggle_logic = """      // Alternar (abrir/cerrar) submenú si ya estamos en Servicios
      if ($(this).attr('id') === 'nav-link-servicios') {
        var isAlreadyPage2 = $('.cd-hero-slider > li[data-page-no="2"]').hasClass('selected');
        if (isAlreadyPage2) {
          $("#servicios-submenu").toggleClass('is-open');
          $("#servicios-chevron").toggleClass('is-rotated');
          return;
        }
      }

      // Alternar (abrir/cerrar) submenú si ya estamos en Productos
      if ($(this).attr('id') === 'nav-link-productos') {
        var isAlreadyPage5 = $('.cd-hero-slider > li[data-page-no="5"]').hasClass('selected');
        if (isAlreadyPage5) {
          $("#productos-submenu").toggleClass('is-open');
          $("#productos-chevron").toggleClass('is-rotated');
          return;
        }
      }"""

new_toggle_logic = """      // Alternar (abrir/cerrar) submenú de Servicios
      if ($(this).attr('id') === 'nav-link-servicios') {
        var isSubmenuOpen2 = $("#servicios-submenu").hasClass('is-open');
        var isAlreadyPage2 = $('.cd-hero-slider > li[data-page-no="2"]').hasClass('selected');
        if (isSubmenuOpen2 && isAlreadyPage2) {
          $("#servicios-submenu").removeClass('is-open');
          $("#servicios-chevron").removeClass('is-rotated');
          return;
        } else {
          $("#servicios-submenu").addClass('is-open');
          $("#servicios-chevron").addClass('is-rotated');
          if (!isAlreadyPage2) {
            openPage(2);
            highlightMenu(2);
          }
          return;
        }
      }

      // Alternar (abrir/cerrar) submenú de Productos
      if ($(this).attr('id') === 'nav-link-productos') {
        var isSubmenuOpen5 = $("#productos-submenu").hasClass('is-open');
        var isAlreadyPage5 = $('.cd-hero-slider > li[data-page-no="5"]').hasClass('selected');
        if (isSubmenuOpen5 && isAlreadyPage5) {
          $("#productos-submenu").removeClass('is-open');
          $("#productos-chevron").removeClass('is-rotated');
          return;
        } else {
          $("#productos-submenu").addClass('is-open');
          $("#productos-chevron").addClass('is-rotated');
          if (!isAlreadyPage5) {
            openPage(5);
            highlightMenu(5);
          }
          return;
        }
      }"""

if old_toggle_logic in js_code:
    js_code = js_code.replace(old_toggle_logic, new_toggle_logic)
    with open('js/templatemo-script.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
    print("js/templatemo-script.js updated successfully!")
else:
    print("Could not find exact old_toggle_logic in js/templatemo-script.js")

# 2. In index.html, remove duplicate toggle handler on #nav-link-productos
with open('index.html', 'r', encoding='utf-8') as f:
    html_code = f.read()

# Pattern for the redundant listener in index.html
redundant_pat = r'// Toggle para el botón principal de Productos\s*\$\(document\)\.on\(\'click\',\s*\'#nav-link-productos\'[\s\S]*?\}\);\s*'
html_code = re.sub(redundant_pat, '', html_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("index.html cleaned of duplicate #nav-link-productos listener!")
