import os

matches = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'generate' in f.lower() or 'image' in f.lower() or 'step-01' in c:
                    matches.append((p, f))

print('Matching files:')
for p, f in matches:
    print(f'  {p}')
