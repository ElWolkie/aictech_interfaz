with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Check that extra bullets are gone from flexim, amstrex, micromotion
checks = [
    ("Verificación Smart Meter", False),
    ("0 horas de parada", False),
    ("Sin Pérdidas de Carga", False),
    ("Alimentación directa de lazo:", False),
    ("center-split-card-wrapper", True),
    ("door-bg-flexim", True),
    ("door-bg-amstrex", True),
    ("door-bg-micromotion", True),
    ("FLUXUS® F631 BA", True),
    ("AMS Trex™ Device Communicator", True),
    ("Micro Motion™ 5700 Field-Mount Transmitter", True)
]

print("=== VERIFICATION CHECKS ===")
all_ok = True
for string, should_exist in checks:
    count = text.count(string)
    exists = count > 0
    ok = (exists == should_exist)
    if not ok:
        all_ok = False
        print(f"FAILED: '{string}' should_exist={should_exist}, count={count}")
    else:
        print(f"PASSED: '{string}' (count={count})")

if all_ok:
    print("\nALL CHECKS PASSED PERFECTLY!")
else:
    print("\nSOME CHECKS FAILED!")
