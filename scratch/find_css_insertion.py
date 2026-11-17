with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'/\*.*COMPACT CARDS & FEATURED LARGE.*?\*/', text)
if m:
    print("Found COMPACT CARDS CSS at position:", m.start())
    print(text[m.start():m.start()+300])
else:
    print("Not found COMPACT CARDS CSS")
