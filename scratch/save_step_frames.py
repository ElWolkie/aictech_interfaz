import cv2

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# Let's save 1 frame every 2 seconds
for s in range(0, 28, 2):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(s * fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'scratch/mant_{s:02d}s.jpg', frame)

print("Saved frames every 2 seconds!")
cap.release()

