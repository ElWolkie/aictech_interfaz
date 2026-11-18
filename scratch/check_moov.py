import os

def check_moov_atom(path):
    with open(path, 'rb') as f:
        # read first 100KB
        header = f.read(102400)
        has_moov_early = b'moov' in header
        f.seek(-102400, os.SEEK_END)
        tail = f.read(102400)
        has_moov_tail = b'moov' in tail
        
        pos_moov = "EARLY (FastStart OK)" if has_moov_early else ("TAIL (Slow / Non-Streamable)" if has_moov_tail else "UNKNOWN")
        print(f"{os.path.basename(path):30s}: moov is {pos_moov}")

for f in sorted(os.listdir('video')):
    if f.endswith('.mp4'):
        check_moov_atom(os.path.join('video', f))

