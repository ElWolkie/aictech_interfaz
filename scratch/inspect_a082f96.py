import subprocess

cmd = ["git", "show", "1c98ce9:index.html"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
content = res.stdout

import re
m = re.search(r'(<article[^>]*id="producto-brand-flexim".*?</article>)', content, re.DOTALL)
if m:
    print(m.group(1))
