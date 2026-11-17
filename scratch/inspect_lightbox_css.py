with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('.media-lightbox-overlay {')
print(c[pos:pos+1500])
