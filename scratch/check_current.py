with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
for brand in ["flexim", "amstrex", "micromotion"]:
    m = re.search(r'(<article[^>]*id="producto-brand-' + brand + r'".*?</article>)', text, re.DOTALL)
    if m:
        print(f"=== FOUND {brand} ({len(m.group(1))} chars) ===")
    else:
        print(f"=== NOT FOUND {brand} ===")
