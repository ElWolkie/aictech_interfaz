with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 285674
print(c[pos:pos+4000])
