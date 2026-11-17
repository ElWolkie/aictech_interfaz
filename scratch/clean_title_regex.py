path = r"c:\Users\Administrator\Desktop\Vessel\index.html"
with open(path, "r", encoding="utf-8", newline="") as f:
    lines = f.readlines()

clean = []
for line in lines:
    if line.strip().startswith("]+/g"):
        continue
    if "title = titleNode.innerText.replace(" in line:
        line = "                title = titleNode.innerText.replace(/[\\r\\n]+/g, ' ').trim();\n"
    clean.append(line)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.writelines(clean)
