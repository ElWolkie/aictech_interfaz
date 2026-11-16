with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.expandMediaFromElement')
print("--- expandMediaFromElement function ---")
print(text[idx:idx+800])

idx2 = text.find('class="emerson-product-card"')
print("\n--- Product card sample ---")
print(text[idx2:idx2+600])
