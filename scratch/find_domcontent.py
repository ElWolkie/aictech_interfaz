with open('index.html.bak', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_open = text.rfind("document.addEventListener('DOMContentLoaded',", 0, text.find('window.renderShowroomPlaylist = renderShowroomPlaylist;'))
print(repr(text[pos_open:pos_open+150]))

