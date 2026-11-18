with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
print("Occurrences of minigame in index.html:")
for m in re.finditer(r'minigame', text):
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + 40)
    print(repr(text[start:end]))

print("\nOccurrences of globe in index.html:")
for m in re.finditer(r'globe', text):
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + 40)
    print(repr(text[start:end]))

