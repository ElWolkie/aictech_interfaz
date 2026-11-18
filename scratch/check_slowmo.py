import cv2
import numpy as np

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# Let's save a collage of 6 frames (sec 1, 3, 6, 10, 15, 20) to inspect what is actually happening in the video
frames_to_save = []
for sec in [1, 4, 8, 12, 16, 20]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(sec * fps))
    ret, frame = cap.read()
    if ret:
        small = cv2.resize(frame, (320, 180))
        cv2.putText(small, f"{sec}s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        frames_to_save.append(small)
cap.release()

if len(frames_to_save) == 6:
    row1 = np.hstack(frames_to_save[:3])
    row2 = np.hstack(frames_to_save[3:])
    grid = np.vstack([row1, row2])
    cv2.imwrite('scratch/mantenimiento_sequence.jpg', grid)
    print("Saved scratch/mantenimiento_sequence.jpg")

