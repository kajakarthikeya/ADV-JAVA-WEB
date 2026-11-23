import re

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# Find all week containers / panels
week_panels = re.findall(r'<div[^>]*class=["\'][^"\']*week-container[^"\']*["\'][^>]*id=["\']([^"\']+)["\']', content)
if not week_panels:
    week_panels = re.findall(r'<div[^>]*id=["\'](week-\d+)["\']', content)
print("Week panels found:", week_panels)

# Find all image paths in index.html
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
print(f"Total image tags in index.html: {len(img_srcs)}")

# Let's inspect step cards and their images
step_cards = re.findall(r'<div class="step-card">.*?<h4 class="step-card-title">(.*?)</h4>.*?<img[^>]+src=["\']([^"\']+)["\']', content, re.DOTALL)
print(f"Total step cards with titles and images: {len(step_cards)}")

# Group by folder
from collections import defaultdict
grouped = defaultdict(list)
for title, src in step_cards:
    folder = "/".join(src.split("/")[:-1])
    grouped[folder].append((title, src))

for folder, items in sorted(grouped.items()):
    print(f"\nFolder: {folder} ({len(items)} steps)")
    for title, src in items[:4]:
        print(f"   {title} -> {src}")

