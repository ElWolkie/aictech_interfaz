with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(35, 75):
    print(f"{i+1}: {repr(lines[i])}")

