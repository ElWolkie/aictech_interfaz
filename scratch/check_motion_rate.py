import cv2
import numpy as np

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

ret, prev = cap.read()
gray_prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

speeds = []
for i in range(1, 200):
    ret, curr = cap.read()
    if not ret: break
    gray_curr = cv2.cvtColor(curr, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray_prev, gray_curr)
    speeds.append(np.mean(diff))
    gray_prev = gray_curr

cap.release()
print(f"Average frame-to-frame diff: {np.mean(speeds):.3f}")
