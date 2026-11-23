import io
import sys
from bs4 import BeautifulSoup

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for w in [2, 3]:
    section = soup.find(id=f"week-{w}-task-1")
    if not section:
        continue
    out.write(f"\n========================================\n")
    out.write(f"WEEK {w} TASK 1\n")
    out.write(f"========================================\n")
    cards = section.find_all('div', class_='step-card')
    for idx, card in enumerate(cards, 1):
        title_el = card.find('h4', class_='step-card-title') or card.find('div', class_='step-card-header')
        title = title_el.get_text(strip=True) if title_el else f"Step {idx}"
        img_el = card.find('img')
        img_src = img_el['src'] if img_el else "NO_IMG"
        out.write(f"{idx:02d}. [{img_src}] {title}\n")

out.flush()

