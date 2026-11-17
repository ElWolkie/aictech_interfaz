with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('/* WATERMARK BRAND LOGOS EN EL SIDENAV')
print(c[pos+2000:pos+4000])
