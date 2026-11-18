with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('window.expandCardMedia = function')
print(text[pos+1500:pos+3000])

