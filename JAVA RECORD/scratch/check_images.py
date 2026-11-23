import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text)
missing = []
for img in imgs:
    # clean query params if any
    clean_src = img.split('?')[0]
    if not os.path.exists(clean_src):
        missing.append(img)

print(f"Total images in index.html: {len(imgs)}")
print(f"Missing images: {len(missing)} -> {missing[:5]}")

