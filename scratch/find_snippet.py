transcript_path = r"C:\Users\Administrator\.gemini\antigravity\brain\57c0b989-46be-416e-a452-3cf4519b81d9\.system_generated\logs\transcript.jsonl"
with open(transcript_path, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("<!-- CSS - Cards - Flip 360 -->")
if idx != -1:
    print(text[idx:idx+2500])
else:
    print("Not found in compact transcript, searching transcript_full.jsonl...")
    with open(r"C:\Users\Administrator\.gemini\antigravity\brain\57c0b989-46be-416e-a452-3cf4519b81d9\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f2:
        text2 = f2.read()
    idx2 = text2.find("<!-- CSS - Cards - Flip 360 -->")
    if idx2 != -1:
        print(text2[idx2:idx2+2500])
