import os

for s in range(0, 28, 2):
    fn = f'scratch/mant_{s:02d}s.jpg'
    sz = os.path.getsize(fn)
    print(f"{fn}: {sz} bytes")

