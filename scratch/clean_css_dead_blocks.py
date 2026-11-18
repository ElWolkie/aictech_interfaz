with open('css/custom-styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
# Remove globe intro CSS block
text = re.sub(r'/\* ===== ANIMACIÓN INTRO: GLOBO 3D OPTIMIZADO ===== \*/.*?(?=/\* =====|$)', '', text, flags=re.DOTALL)
# Remove minigame CSS block
text = re.sub(r'/\* ===== MINIJUEGO DEL PETRÓLEO AICTECH ===== \*/.*?(?=/\*|$)', '', text, flags=re.DOTALL)

with open('css/custom-styles.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleaned CSS dead blocks successfully!")

