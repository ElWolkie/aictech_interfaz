import cv2
import os

for f in sorted(os.listdir('video')):
    if f.endswith('.mp4'):
        p = os.path.join('video', f)
        cap = cv2.VideoCapture(p)
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frames / fps if fps > 0 else 0
        sz_mb = os.path.getsize(p) / (1024*1024)
        bitrate = (sz_mb * 8) / duration if duration > 0 else 0
        print(f"{f:30s} | {w}x{h} | {fps:.1f}fps | {duration:5.1f}s | {sz_mb:5.2f}MB | {bitrate:4.2f}Mbps")
        cap.release()

