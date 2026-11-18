with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Replace everything between </button>\s*<!-- BOTÓN GLOBAL PARA OCULTAR / MOSTRAR MENÚ LATERAL (DESKTOP) -->\s*<button id="btn-sidebar-collapse"[^>]*>.*?</button>
# and <div class="d-flex" id="wrapper">
marker1 = '</button>'
btn_collapse = '<!-- BOTÓN GLOBAL PARA OCULTAR / MOSTRAR MENÚ LATERAL (DESKTOP) -->'
wrapper = '<div class="d-flex" id="wrapper">'

pos_btn = text.find(btn_collapse)
if pos_btn != -1:
    pos_end_btn = text.find('</button>', pos_btn) + len('</button>')
    pos_wrapper = text.find(wrapper)
    if pos_end_btn != -1 and pos_wrapper != -1:
        print("Slice to remove:")
        print(repr(text[pos_end_btn:pos_wrapper]))
        text = text[:pos_end_btn] + '\n\n' + text[pos_wrapper:]
        with open('index.html', 'w', encoding='utf-8') as out:
            out.write(text)
        print("Removed orphaned minigame & globe intro elements successfully!")
    else:
        print("Could not find end button or wrapper")
else:
    print("Could not find btn_collapse marker")

