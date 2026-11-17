with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('function openAictechIntroModal')
print(content[pos:pos+900])
