with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('window.fluidNavigateTo =')
print("fluidNavigateTo:")
print(c[pos:pos+1500])

pos_open = c.find('function openPage(')
print("\nopenPage:")
print(c[pos_open:pos_open+1200])
