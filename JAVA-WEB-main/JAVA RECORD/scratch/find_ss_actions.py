import os
import re

for root, dirs, files in os.walk('.'):
    if '.gemini' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.py')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    c = content.count('ss-actions')
                    if c > 0:
                        print(f"{p}: {c} occurrences of ss-actions")
            except Exception as e:
                pass

