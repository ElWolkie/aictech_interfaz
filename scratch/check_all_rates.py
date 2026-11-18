import cv2

videos_to_check = [
    'video/mantenimiento-1.mp4',
    'video/calibracion-1.mp4',
    'video/soldadura-1.mp4',
    'video/soldadura.mp4',
    'video/taller-1.mp4',
    'video/multifasico-campo.mp4',
    'video/flexim-2.mp4',
    'video/tanque-1.mp4',
    'video/trasegado-1.mp4'
]

for v in videos_to_check:
    cap = cv2.VideoCapture(v)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    dur = frames / fps if fps > 0 else 0
    print(f"{v:30s}: {frames:5.0f} frames, {fps:4.1f} fps, {dur:5.1f}s")
    cap.release()

