with open('video/mantenimiento-1.mp4', 'rb') as f:
    content = f.read(500000)
    has_audio = b'soun' in content or b'mp4a' in content
    print("Has audio track in header:", has_audio)

