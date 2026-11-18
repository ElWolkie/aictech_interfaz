with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('id="media-lightbox-modal"')
print(text[pos:pos+600])

