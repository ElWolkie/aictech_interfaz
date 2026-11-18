with open('index.html.bak', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
pos = text.find('window.renderShowroomPlaylist = renderShowroomPlaylist;')
print(repr(text[pos:pos+400]))

