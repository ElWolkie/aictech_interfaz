import cv2
import numpy as np

# Let's inspect the bounding box of the man across time
# Frame 0s to 10s: man walking through door
# Frame 10s to 27s: what is in frame?
for s in [0, 2, 4, 6, 8, 10, 14, 18, 22, 26]:
    im = cv2.imread(f'scratch/mant_{s:02d}s.jpg')
    # Let's get average color of center region
    h, w = im.shape[:2]
    crop = im[int(h*0.3):int(h*0.7), int(w*0.3):int(w*0.7)]
    mean_val = np.mean(crop, axis=(0,1))
    print(f"Time {s:02d}s: mean BGR={mean_val.astype(int)}")

