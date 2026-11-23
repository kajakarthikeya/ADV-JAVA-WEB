import shutil
import os

src_dir = "JAVA-WEB-main"
dst_dir = "."

# 1. Sync style.css, script.js, index.html, README.md
for fname in ["style.css", "script.js", "index.html", "README.md"]:
    src_file = os.path.join(src_dir, fname)
    dst_file = os.path.join(dst_dir, fname)
    if os.path.exists(src_file):
        shutil.copy2(src_file, dst_file)
        print(f"Copied {fname} to root")

# 2. Sync pages/
src_pages = os.path.join(src_dir, "pages")
dst_pages = os.path.join(dst_dir, "pages")
if os.path.exists(src_pages):
    for root, dirs, files in os.walk(src_pages):
        rel = os.path.relpath(root, src_pages)
        target_dir = os.path.join(dst_pages, rel)
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))
    print("Synced pages/ to root")

# 3. Sync assets/
src_assets = os.path.join(src_dir, "assets")
dst_assets = os.path.join(dst_dir, "assets")
if os.path.exists(src_assets):
    for root, dirs, files in os.walk(src_assets):
        rel = os.path.relpath(root, src_assets)
        target_dir = os.path.join(dst_assets, rel)
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))
    print("Synced assets/ to root")

print("All synchronized successfully!")

