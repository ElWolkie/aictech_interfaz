code = open('scratch/generate_section5_v2.py', encoding='utf-8').read()
ids = [
    'producto-brand-roxar',
    'producto-brand-rosemount',
    'producto-brand-micromotion',
    'producto-brand-flexim',
    'producto-brand-amstrex',
    'producto-brand-fluenta',
    'producto-brand-kam'
]
for id_ in ids:
    idx = code.find(id_)
    banner_end = code.find('</div>\n                                    </div>', idx)
    print(f"=== {id_} ===")
    print(code[idx:idx+900])
    print("\n" + "="*50 + "\n")
