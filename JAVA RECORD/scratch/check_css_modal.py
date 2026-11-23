with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
matches = []
for i, l in enumerate(lines):
    if 'ss-modal' in l or 'ssModal' in l:
        matches.append((i+1, l))

for m in matches:
    print(f'{m[0]}: {m[1]}')

