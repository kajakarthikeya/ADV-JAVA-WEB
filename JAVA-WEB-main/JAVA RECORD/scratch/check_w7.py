import os

for root, dirs, files in os.walk('assets/images/week-7'):
    for f in sorted(files):
        p = os.path.join(root, f)
        print(f"{p} ({os.path.getsize(p)} bytes)")
