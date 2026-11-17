with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="card-multifasico-camp')
print(c[pos:pos+3500])
