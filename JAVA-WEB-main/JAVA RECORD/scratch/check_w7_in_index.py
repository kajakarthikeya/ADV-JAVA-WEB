import io
import sys
from bs4 import BeautifulSoup

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

all_imgs = soup.find_all('img')
w7_imgs = [img['src'] for img in all_imgs if 'week-7' in img.get('src', '')]
out.write(f"Week 7 images in index.html: {len(w7_imgs)}\n")
for src in sorted(set(w7_imgs)):
    out.write(f"  {src}\n")

out.flush()

