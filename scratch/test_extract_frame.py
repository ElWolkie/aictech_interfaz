import cv2
import os

video_path = 'video/multifasico-campo.mp4'
cap = cv2.VideoCapture(video_path)
success, frame = cap.read()
if success:
    os.makedirs('img/posters', exist_ok=True)
    out_path = 'img/posters/multifasico-campo.jpg'
    # Write at good quality
    cv2.imwrite(out_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
    print(f"Extracted frame successfully! Size: {os.path.getsize(out_path)/1024:.1f} KB")
else:
    print("Could not read frame")
cap.release()

