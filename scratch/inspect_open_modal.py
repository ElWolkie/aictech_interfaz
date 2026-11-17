with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('openAictechIntroModal')
print(content[pos:pos+1200])
