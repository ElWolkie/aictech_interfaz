# -*- coding: utf-8 -*-
import subprocess

raw = subprocess.check_output(['git', 'show', 'HEAD:index.html'], encoding='utf-8')
p2_idx = raw.find('data-page-no="2"')
print(raw[p2_idx:p2_idx + 3500])
