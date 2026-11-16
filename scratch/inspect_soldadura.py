with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="servicio-soldadura-taller"')
print(text[idx:idx+2500])
