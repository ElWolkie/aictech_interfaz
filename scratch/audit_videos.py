import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

vids = re.findall(r'<video[^>]*>.*?</video>', text, re.DOTALL)
print(f'Total video blocks: {len(vids)}')
for i, v in enumerate(vids):
    first_line = v.strip().split('\n')[0]
    src = re.findall(r'src="([^"]+)"', v)
    print(f'{i+1}: {src[0] if src else "NO_SRC"} | {first_line}')

