import os
import hashlib

def get_hash(path):
    if not os.path.exists(path):
        return "MISSING"
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

for w in range(0, 14):
    for t in [1, 2, 3]:
        folder = f"assets/images/week-{w}/task-{t}"
        if os.path.exists(folder):
            files = sorted([f for f in os.listdir(folder) if f.endswith('.png')])
            hashes = [get_hash(os.path.join(folder, f)) for f in files]
            unique_hashes = set(hashes)
            print(f"Week {w} Task {t}: {len(files)} files, {len(unique_hashes)} unique images")
            if len(files) != len(unique_hashes):
                print(f"  DUPLICATE DETECTED! ({len(files) - len(unique_hashes)} duplicates)")

