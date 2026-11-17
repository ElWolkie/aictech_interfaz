with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_p5 = c.find('data-page-no="5"')
pos_p6 = c.find('data-page-no="6"')

print("Length of section 5:", pos_p6 - pos_p5)
print("Section 5 start:")
print(c[pos_p5:pos_p5+500])
