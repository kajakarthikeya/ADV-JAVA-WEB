import re
import io
import sys
from collections import defaultdict

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# Match all img tags with their src and alt or nearest data-title
items = re.findall(r'<div[^>]*class=["\'](?:step-img-wrap|ss-img-wrap)["\'][^>]*data-title=["\']([^"\']*)["\'][^>]*>\s*<img[^>]*src=["\']([^"\']+)["\']', content)

out.write("Found " + str(len(items)) + " img items with data-title.\n")

by_dir = defaultdict(list)
for title, src in items:
    folder = "/".join(src.split("/")[:-1])
    by_dir[folder].append((title, src))

for folder, step_list in sorted(by_dir.items()):
    out.write("\n=== " + folder + " (" + str(len(step_list)) + " images) ===\n")
    for t, s in step_list:
        out.write("  " + s.split("/")[-1] + " : " + t + "\n")

out.flush()

