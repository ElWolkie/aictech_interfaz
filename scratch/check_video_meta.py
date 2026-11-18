import os, struct

def get_mp4_info(file_path):
    size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        # Search for mvhd / tkhd / avc1
        data = f.read(500000) # first 500KB
    print(f"{file_path}: {size/1024/1024:.2f} MB")

get_mp4_info('video/presentacion-1.mp4')

