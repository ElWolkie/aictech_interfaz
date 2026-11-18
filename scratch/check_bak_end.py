with open('index.html.bak', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('<!-- MODAL DE VIDEO ECHOMETER PANTALLA COMPLETA -->')
print(repr(text[pos-200:pos]))

