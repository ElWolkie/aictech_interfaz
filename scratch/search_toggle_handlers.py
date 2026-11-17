# -*- coding: utf-8 -*-
import re

for fn in ['index.html', 'js/templatemo-script.js']:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = [m.start() for m in re.finditer(r'emerson-nested-toggle', content)]
    print(f"{fn} has {len(matches)} occurrences of 'emerson-nested-toggle'")
    for pos in matches:
        print(content[pos-50:pos+120].strip())
        print("---")
