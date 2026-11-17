# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
for fn in ['syncServiceVideosOnPage', 'syncCardVideosOnPage', 'handlePageVideoPlayback']:
    idx = h.find(fn)
    print(f"{fn} in index.html:", idx != -1)
    if idx != -1:
        print(h[idx:idx + 500])
