import os

matches = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.js') or f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for idx, line in enumerate(fp.readlines()):
                    if 'open' in line and any(k in line for k in ['classList', 'modal', 'Modal']):
                        matches.append(f'{p}:{idx+1}: {line.strip()}')

with open('scratch/modal_open_calls.txt', 'w', encoding='utf-8') as out:
    for m in matches:
        out.write(m + '\n')

print(f'Total matches: {len(matches)}')

