with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pos_intro = content.find('aictech-intro-video')
print('Intro video tag snippet:', content[pos_intro-20:pos_intro+120])
print('Has flip-360 styles?', '.flip-360-wrapper' in content)
print('Has featured-large-product-card?', 'featured-large-product-card' in content)
print('Has compact-product-card?', 'compact-product-card' in content)
print('Count of flip wrappers:', content.count('flip-360-wrapper'))
print('Count of featured large cards:', content.count('featured-large-product-card'))
print('Count of compact cards:', content.count('compact-product-card'))
