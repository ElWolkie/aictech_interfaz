import re
import subprocess

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
print(f"Testing {len(scripts)} inline script blocks...")

for i, s in enumerate(scripts):
    test_path = f'scratch/test_script_{i}.js'
    with open(test_path, 'w', encoding='utf-8') as sf:
        sf.write(s)
    
    res = subprocess.run(['node', '--check', test_path], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Script block {i+1}: Syntax OK")
    else:
        print(f"Script block {i+1}: SYNTAX ERROR:\n{res.stderr}")

