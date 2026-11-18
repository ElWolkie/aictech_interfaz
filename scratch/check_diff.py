import cv2
import numpy as np

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# Check frame differences between consecutive frames 1 second apart vs 1 frame apart
ret, f1 = cap.read()
cap.set(cv2.CAP_PROP_POS_FRAMES, 25)
ret, f2 = cap.read()
cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
ret, f3 = cap.read()

diff1 = np.mean(np.abs(f1.astype(float) - f2.astype(float)))
diff2 = np.mean(np.abs(f2.astype(float) - f3.astype(float)))
print(f"Mean pixel diff across 1 sec: {diff1:.2f}, {diff2:.2f}")

cap.release()

