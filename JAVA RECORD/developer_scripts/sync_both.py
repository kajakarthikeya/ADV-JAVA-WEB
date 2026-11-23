import shutil
import os

src_dir = "."
dst_dir = "JAVA-WEB-main"

print("Synchronizing root directory to JAVA-WEB-main inner directory...")

# Sync root files
for fname in ["style.css", "script.js", "index.html", "README.md", "validate_lab_record.py"]:
    if os.path.exists(fname):
        shutil.copy2(fname, os.path.join(dst_dir, fname))
        print(f"Copied {fname}")

# Sync pages/
src_pages = "pages"
dst_pages = os.path.join(dst_dir, "pages")
for root, dirs, files in os.walk(src_pages):
    rel = os.path.relpath(root, src_pages)
    target_dir = os.path.join(dst_pages, rel)
    os.makedirs(target_dir, exist_ok=True)
    for f in files:
        shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))
print("Synced pages/")

# Sync assets/
src_assets = "assets"
dst_assets = os.path.join(dst_dir, "assets")
for root, dirs, files in os.walk(src_assets):
    rel = os.path.relpath(root, src_assets)
    target_dir = os.path.join(dst_assets, rel)
    os.makedirs(target_dir, exist_ok=True)
    for f in files:
        shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))
print("Synced assets/")

print("Synchronization complete!")

