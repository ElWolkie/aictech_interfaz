with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of index.html:', len(text))
print('sidebar-collapse.css in text:', 'sidebar-collapse.css' in text)
print('sidebar-collapse.js in text:', 'sidebar-collapse.js' in text)
print('btn-fullscreen-toggle in text:', 'btn-fullscreen-toggle' in text)
print('btn-sidebar-collapse in text:', 'btn-sidebar-collapse' in text)
print('btn-89 in text:', 'btn-89' in text)
print('roxar2600.mp4 in text:', 'roxar2600.mp4' in text)
print('media-lightbox in text:', 'media-lightbox' in text)
print('Quiénes Somos in text:', 'Quiénes Somos' in text)
sec1 = text[text.find('data-page-no="1"'):text.find('data-page-no="2"')]
print('hero-slb-panels in Section 1:', 'hero-slb-panels' in sec1)
print('https://simulador.miku-celsius.ts.net/#mpfm in text:', 'https://simulador.miku-celsius.ts.net/#mpfm' in text)
