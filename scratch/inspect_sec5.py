with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('id="producto-brand-emerson"')
print("Snippet around producto-brand-emerson:")
print(content[max(0, pos-400):pos+600])
