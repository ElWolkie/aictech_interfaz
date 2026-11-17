with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="main-sidebar-nav"')
print(c[pos:pos+3000])
