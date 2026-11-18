import cv2

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Sample 10 frames across the video and check what's happening
for sec in [1, 3, 5, 8, 12, 16, 20, 24]:
    f_num = int(sec * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_num)
    ret, frame = cap.read()
    if ret:
        print(f"Sec {sec}: Frame {f_num} read successfully")
cap.release()

