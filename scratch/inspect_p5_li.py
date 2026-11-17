with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_li5 = c.find('<li data-page-no="5"')
pos_li6 = c.find('<li data-page-no="6"')

print("Li 5 at:", pos_li5, "Li 6 at:", pos_li6)
print(c[pos_li5:pos_li5+500])
