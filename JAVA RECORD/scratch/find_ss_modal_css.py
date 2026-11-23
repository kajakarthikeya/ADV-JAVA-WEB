import os

matches = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.css') or f.endswith('.py') or f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if '.ss-modal' in c:
                    matches.append(p)

print('Files with .ss-modal:')
for m in matches:
    print(' ', m)

