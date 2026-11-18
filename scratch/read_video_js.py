with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(6888, 7150):
    print(f"{i+1}: {lines[i]}", end='')

