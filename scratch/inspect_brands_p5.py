with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pos_p5 = content.find('data-page-no="5"')
pos_p6 = content.find('data-page-no="6"')
sec5_html = content[pos_p5:pos_p6 if pos_p6 != -1 else len(content)]

brand_ids = re.findall(r'id=["\'](producto-brand-[^"\']+)["\']', sec5_html)
print("Brand IDs in Section 5:", brand_ids)

for b_id in brand_ids:
    pos_b = sec5_html.find(b_id)
    snippet = sec5_html[pos_b:pos_b+350]
    print(f"\n--- Brand: {b_id} ---")
    has_large = 'featured-large-product-card' in sec5_html[pos_b:pos_b+3000]
    has_flip = 'flip-360-wrapper' in sec5_html[pos_b:pos_b+3000]
    print(f"Has featured-large: {has_large}, Has flip-360: {has_flip}")
