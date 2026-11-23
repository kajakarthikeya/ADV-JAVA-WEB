import sys
sys.path.insert(0, '.')
from build_sidebar_helpers import WEEKS_META

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for w in WEEKS_META:
    print(f"Week {w['num']} tasks:")
    for tid, title in w['tasks']:
        has_id = f'id="{tid}"' in text
        print(f"  {tid}: {'FOUND' if has_id else 'MISSING'} ({title})")
