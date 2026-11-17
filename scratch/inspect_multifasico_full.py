with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_card = c.find('id="card-multifasico-campo"')
pos_end_card = c.find('<!-- Panel Derecho', pos_card)
if pos_end_card == -1:
    pos_end_card = c.find('id="roxar-exe-trigger"', pos_card)
print(c[pos_card:pos_end_card])
