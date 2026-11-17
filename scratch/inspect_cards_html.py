with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('featured-bottom-info')
print("featured-bottom-info:")
print(content[pos:pos+900])

pos_c = content.find('compact-title-bar')
print("\ncompact-title-bar:")
print(content[pos_c:pos_c+600])
