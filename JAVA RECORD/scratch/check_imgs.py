from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

imgs = soup.find_all('img')
print(f'Total imgs in index.html: {len(imgs)}')

no_src = [img for img in imgs if not img.get('src')]
print(f'Imgs with no src or empty src: {len(no_src)}')
for img in no_src:
    print('Empty img:', img)

parents = {}
for img in imgs:
    p = img.parent.get('class', ['no-class'])
    p_str = ' '.join(p)
    parents[p_str] = parents.get(p_str, 0) + 1

print('Img parent classes:')
for p, c in parents.items():
    print(f'  {p}: {c}')

