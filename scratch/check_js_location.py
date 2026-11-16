with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.expandMediaFromElement')
print("Surrounding 300 chars before:")
print(text[idx-300:idx])
print("\nSurrounding 400 chars after:")
print(text[idx:idx+400])
