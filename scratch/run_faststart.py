import os
import shutil
import qtfaststart.processor

videos = [
    'video/mantenimiento-1.mp4',
    'video/presentacion-1.mp4',
    'video/flexim-1.mp4'
]

for v in videos:
    if not os.path.exists(v):
        continue
    temp_out = v + '.faststart.mp4'
    try:
        qtfaststart.processor.process(v, temp_out)
        if os.path.exists(temp_out) and os.path.getsize(temp_out) > 0:
            shutil.move(temp_out, v)
            print(f"Successfully converted {v} to FastStart!")
    except Exception as e:
        print(f"Error processing {v}: {e}")
        if os.path.exists(temp_out):
            os.remove(temp_out)

