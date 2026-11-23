import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

for word in ['fetch(', 'XMLHttpRequest', 'location.href', 'window.open', '.src', '.href']:
    matches = [line.strip() for line in js.splitlines() if word in line]
    print(f'Matches for {word}: {len(matches)}')
    for m in matches[:5]:
        print('  ', m)

