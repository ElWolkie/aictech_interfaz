import cv2

cap = cv2.VideoCapture('video/mantenimiento-1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# Let's inspect what happens across the 27 seconds
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total seconds:", frames / fps)

# Let's check how long the man takes to walk
# Frame at 0s, 5s, 10s, 15s, 20s, 25s
for s in [0, 5, 10, 15, 20, 25]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(s * fps))
    ret, frame = cap.read()
    # Check average brightness and movement
    print(f"Second {s}: frame exists = {ret}")
cap.release()

