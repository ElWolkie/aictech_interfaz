with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'(\.flip[^{]*\{[^}]*\})', text)
print("FLIP CSS:")
for m in matches[:10]:
    print(m)

matches2 = re.findall(r'(\.center-split[^{]*\{[^}]*\})', text)
print("\nCENTER SPLIT CSS:")
for m in matches2:
    print(m)

matches3 = re.findall(r'(\.single-product-flip[^{]*\{[^}]*\})', text)
print("\nSINGLE PRODUCT FLIP CSS:")
for m in matches3:
    print(m)
