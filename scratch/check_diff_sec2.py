# -*- coding: utf-8 -*-
import subprocess

out = subprocess.check_output(['git', 'diff', '-U3', 'index.html'], encoding='utf-8')
lines = out.splitlines()
in_hunk = False
for line in lines:
    if 'servicio-multifasico' in line or 'catalog-hero-box' in line or 'Soluciones Integrales' in line:
        print("MATCH:", line[:120])
