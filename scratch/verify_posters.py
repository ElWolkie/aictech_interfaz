with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
videos = re.findall(r'<video[^>]*>', text)
print(f"Total videos in index.html: {len(videos)}")
with_poster = [v for v in videos if 'poster=' in v]
print(f"Videos with poster: {len(with_poster)}")
for i, v in enumerate(videos):
    poster = re.findall(r'poster="([^"]+)"', v)
    print(f"Video {i+1}: poster={poster[0] if poster else 'NONE'}")

