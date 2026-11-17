# -*- coding: utf-8 -*-
import subprocess

raw = subprocess.check_output(['git', 'show', 'HEAD:index.html'], encoding='utf-8')
idx = raw.find('id="servicio-multifasico"')
print(raw[idx:idx + 1800])
