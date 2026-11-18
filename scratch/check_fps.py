import cv2

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
duration = count / fps if fps > 0 else 0
print(f"FPS: {fps}, Frame count: {count}, Duration: {duration:.2f} seconds")

# Read a few timestamps
for i in range(10):
    ret, frame = cap.read()
    if not ret: break
    msec = cap.get(cv2.CAP_PROP_POS_MSEC)
    print(f"Frame {i}: timestamp {msec:.1f}ms")
cap.release()

