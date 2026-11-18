import cv2
import os

def check_video(path):
    if not os.path.exists(path):
        print(f"Missing: {path}")
        return
    cap = cv2.VideoCapture(path)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frames / fps if fps > 0 else 0
    size_mb = os.path.getsize(path) / (1024*1024)
    bitrate_mbps = (size_mb * 8) / duration if duration > 0 else 0
    codec = int(cap.get(cv2.CAP_PROP_FOURCC))
    fourcc = "".join([chr((codec >> 8 * i) & 0xFF) for i in range(4)])
    print(f"{path}: {w}x{h} @ {fps:.1f}fps, {duration:.1f}s, {size_mb:.2f} MB, ~{bitrate_mbps:.2f} Mbps, codec={fourcc}")
    cap.release()

check_video('video/mantenimiento-1.mp4')
check_video('video/calibracion-1.mp4')
check_video('video/gemelo_digital_video.mp4')
check_video('video/multifasico-campo.mp4')
check_video('video/soldadura-1.mp4')
check_video('video/echometer.mp4')

