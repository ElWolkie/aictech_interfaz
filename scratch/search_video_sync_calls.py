# -*- coding: utf-8 -*-
import re

for fn in ['index.html', 'js/templatemo-script.js']:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    for term in ['syncServiceVideosOnPage', 'syncCardVideosOnPage', 'handlePageVideoPlayback', 'initActiveSectionVideoObserver']:
        matches = [m.start() for m in re.finditer(re.escape(term), content)]
        print(f"{fn} -> {term}: {len(matches)} occurrences")
