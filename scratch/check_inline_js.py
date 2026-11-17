import re

html = open(r"c:\Users\Administrator\Desktop\Vessel\index.html", "r", encoding="utf-8").read()
blocks = re.findall(r"<script(?:[^>]*)>([\s\S]*?)</script>", html, re.I)

for index, block in enumerate(blocks, 1):
    stack = []
    line = 1
    state = "code"
    i = 0

    while i < len(block):
        c = block[i]
        n = block[i + 1] if i + 1 < len(block) else ""
        if c == "\n":
            line += 1

        if state == "line":
            if c == "\n":
                state = "code"
        elif state == "block":
            if c == "*" and n == "/":
                state = "code"
                i += 1
        elif state == "single":
            if c == "\\":
                i += 1
            elif c == "'":
                state = "code"
        elif state == "double":
            if c == "\\":
                i += 1
            elif c == '"':
                state = "code"
        elif state == "template":
            if c == "\\":
                i += 1
            elif c == "`":
                state = "code"
        elif state == "regex":
            if c == "\\":
                i += 1
            elif c == "/":
                state = "code"
            elif c == "\n":
                state = "code"
        else:
            if c == "/" and n == "/":
                state = "line"
                i += 1
            elif c == "/" and n == "*":
                state = "block"
                i += 1
            elif c == "'":
                state = "single"
            elif c == '"':
                state = "double"
            elif c == "`":
                state = "template"
            elif c in "{([":
                stack.append((c, line))
            elif c in "})]":
                pairs = {"}": "{", ")": "(", "]": "["}
                if stack and stack[-1][0] == pairs[c]:
                    stack.pop()
                else:
                    print(f"MISMATCH block {index}: unexpected {c} at line {line}; stack={stack[-3:]}")
        i += 1

    print(f"Block {index}: remaining={stack[-8:]}, state={state}, lines={line}")
