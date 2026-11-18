with open('scratch/new_index_test.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
m = re.search(r'// =========================================================================\s*// CONTROLADOR ULTRA-OPTIMIZADO DE VIDEOS.*?(// CONTROLADOR DE CLIC EN 2 PASOS)', text, re.DOTALL)
if m:
    print("Found video controller block! Length:", len(m.group(0)))
    with open('scratch/current_video_js.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
else:
    print("Block not found by regex")

