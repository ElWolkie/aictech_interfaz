with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('// Inyectar reproductor optimizado')
print(text[pos:pos+1500])

