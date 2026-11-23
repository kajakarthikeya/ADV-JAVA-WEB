import re
import io
import sys
from bs4 import BeautifulSoup

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

weeks_to_check = [4, 5, 6, 8, 9, 10, 11, 12, 13]

for w in weeks_to_check:
    for t in [1, 2, 3]:
        section = soup.find(id=f"week-{w}-task-{t}")
        if not section:
            continue
        out.write(f"\n========================================\n")
        out.write(f"WEEK {w} TASK {t}\n")
        out.write(f"========================================\n")
        cards = section.find_all('div', class_='step-card')
        for idx, card in enumerate(cards, 1):
            title_el = card.find('h4', class_='step-card-title') or card.find('div', class_='step-card-header')
            title = title_el.get_text(strip=True) if title_el else f"Step {idx}"
            img_el = card.find('img')
            img_src = img_el['src'] if img_el else "NO_IMG"
            desc_el = card.find('p', class_='step-card-desc') or card.find('div', class_='step-card-body')
            desc = desc_el.get_text(strip=True)[:100] if desc_el else ""
            out.write(f"{idx:02d}. [{img_src}] {title} :: {desc}\n")

out.flush()

