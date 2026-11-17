with open('js/templatemo-script.js', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('function openPage(')
print(c[pos:pos+2500])
