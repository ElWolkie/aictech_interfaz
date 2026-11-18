with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
pos = text.find('window.expandCardMedia = function')
print(text[pos:pos+1500])

