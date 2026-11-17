with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Occurrences of expandMediaFromElement:", content.count('expandMediaFromElement'))
pos = content.find('expandMediaFromElement')
if pos != -1:
    print(content[pos-50:pos+200])
