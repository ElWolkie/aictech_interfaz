with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('window.expandMediaFromElement = function(elem) {')
end_pos = content.find('window.closeMediaLightbox = function', pos)
print(content[pos:end_pos])
