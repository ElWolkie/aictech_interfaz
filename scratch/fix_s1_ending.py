with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

marker = 'window.renderShowroomPlaylist = renderShowroomPlaylist;'
pos = text.find(marker)
end_tag = text.find('<!-- MODAL DE VIDEO ECHOMETER PANTALLA COMPLETA -->', pos)

fixed_ending = "window.renderShowroomPlaylist = renderShowroomPlaylist;\n    }); // end DOMContentLoaded\n</script>\n\n"
text = text[:pos] + fixed_ending + text[end_tag:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Closed DOMContentLoaded properly!")

