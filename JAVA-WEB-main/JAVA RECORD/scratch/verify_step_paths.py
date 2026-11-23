import re
import io
import sys
from bs4 import BeautifulSoup

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

step_images = soup.find_all('img', class_='step-img')
out.write(f"Total step-img elements in index.html: {len(step_images)}\n")

step_paths = [img['src'] for img in step_images]
from collections import Counter
c = Counter(step_paths)
out.write(f"Unique step image paths: {len(c)}\n")

# Group by folder
from collections import defaultdict
grouped = defaultdict(list)
for p in sorted(c.keys()):
    folder = "/".join(p.split("/")[:-1])
    grouped[folder].append(p.split("/")[-1])

for folder, files in sorted(grouped.items()):
    out.write(f"\n{folder} ({len(files)} steps): {files[0]} .. {files[-1]}\n")

out.flush()

