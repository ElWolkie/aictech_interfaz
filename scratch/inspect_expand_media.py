with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('window.expandCardMedia = function')
print(content[pos+2400:pos+3800])
