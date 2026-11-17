with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('article', c.find('producto-brand-roxar', 200000) - 100)
print(c[pos+4500:pos+7500])
