import os

matches = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py') or f.endswith('.html') or f.endswith('.bak') or f.endswith('.old') or f.endswith('.js'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'zoom-modal' in c:
                    matches.append(p)

print('Files with zoom-modal:')
for m in matches:
    print(' ', m)

