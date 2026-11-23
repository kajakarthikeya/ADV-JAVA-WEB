import os
import re

total_pages = 0
all_missing = {}

for num in range(14):
    p = f"pages/week-{num}.html"
    if not os.path.exists(p):
        continue
    total_pages += 1
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text)
    missing = []
    for img in imgs:
        clean = img.split('?')[0]
        # in pages/, paths like ../assets/... resolve relative to pages/
        real_path = os.path.normpath(os.path.join('pages', clean))
        if not os.path.exists(real_path):
            missing.append(img)
    if missing:
        all_missing[p] = missing

print(f"Checked {total_pages} standalone pages.")
print(f"Pages with missing images: {len(all_missing)}")
for p, m in all_missing.items():
    print(f"  {p}: {len(m)} missing -> {m[:3]}")

