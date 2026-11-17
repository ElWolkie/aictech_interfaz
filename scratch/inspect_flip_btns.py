with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos_flexim = content.find('id="producto-brand-flexim"')
print(content[pos_flexim+6500:pos_flexim+8500])
