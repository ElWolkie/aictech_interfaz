with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_s = 355898 # Script 4 start
pos1 = c.find('function onPointerUp()')
print("From start of Script 4 to onPointerUp:")
print(c[pos_s:pos_s+1000])
