import io
import sys
from bs4 import BeautifulSoup

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

all_imgs = soup.find_all('img')
out.write(f"Total img tags: {len(all_imgs)}\n")

step_imgs = [img['src'] for img in all_imgs if 'step-' in img.get('src', '')]
out.write(f"Imgs with step- in src: {len(step_imgs)}\n")

from collections import defaultdict
grouped = defaultdict(list)
for p in sorted(set(step_imgs)):
    folder = "/".join(p.split("/")[:-1])
    grouped[folder].append(p.split("/")[-1])

for folder, files in sorted(grouped.items()):
    out.write(f"{folder} ({len(files)} files): {files[0]} .. {files[-1]}\n")

out.flush()

