import re

with open('scratch/new_index_test.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

vids = re.findall(r'<video[^>]*>', text)
print(f'Total videos: {len(vids)}')
for i, v in enumerate(vids):
    print(f'{i+1}: {v}')

