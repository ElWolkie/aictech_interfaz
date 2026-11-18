import cv2
import os

os.makedirs('img/posters', exist_ok=True)

video_files = [
    'video/presentacion-1.mp4',
    'video/roxar2600.mp4',
    'video/multifasico-campo.mp4',
    'video/gemelo_digital_video.mp4',
    'video/separador-1.mp4',
    'video/bifasico.mp4',
    'video/trifasico-2.mp4',
    'video/flexim.mp4',
    'video/flexim-2.mp4',
    'video/echometer.mp4',
    'video/echometer-1.mp4',
    'video/echometer-2.mp4',
    'video/tanque.mp4',
    'video/trasegado-1.mp4',
    'video/tanque-1.mp4',
    'video/soldadura-1.mp4',
    'video/soldadura.mp4',
    'video/taller-1.mp4',
    'video/aictech.mp4',
    'video/calibracion-1.mp4',
    'video/mantenimiento-1.mp4',
    'video/biblioteca/presentacion-2.mp4',
    'video/inicio-aic.mp4'
]

for vpath in video_files:
    if not os.path.exists(vpath):
        print(f"File not found: {vpath}")
        continue
    base = os.path.splitext(os.path.basename(vpath))[0]
    out_path = f'img/posters/{base}.jpg'
    
    cap = cv2.VideoCapture(vpath)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 100
    
    # Seek to 1 second or 15% of video
    target_frame = min(int(fps * 1.0), int(total_frames * 0.15))
    cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
    
    success, frame = cap.read()
    if not success:
        # fallback to frame 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, frame = cap.read()
    
    if success:
        # Resize to max width 960 for great sharpness & minimal size
        h, w = frame.shape[:2]
        if w > 960:
            new_w = 960
            new_h = int(h * (960 / w))
            frame = cv2.resize(frame, (new_w, new_h), interpolation=cv2.INTER_AREA)
        
        cv2.imwrite(out_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 82])
        print(f"Extracted {out_path}: {os.path.getsize(out_path)/1024:.1f} KB ({w}x{h} -> {frame.shape[1]}x{frame.shape[0]})")
    else:
        print(f"Failed to extract frame from {vpath}")
    cap.release()

