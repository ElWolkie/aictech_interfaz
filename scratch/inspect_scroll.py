# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('scrollIntoView')
while idx != -1:
    print("--- SCROLL INTO VIEW INSTANCE ---")
    print(text[max(0, idx-100):min(len(text), idx+200)])
    idx = text.find('scrollIntoView', idx+1)
