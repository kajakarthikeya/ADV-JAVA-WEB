import os
import re

for root, dirs, files in os.walk('.'):
    if '.gemini' in root or 'scratch' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                txt = fp.read()
            if 'ss-actions' in txt:
                new_txt = re.sub(r'<div class="ss-actions">[\s\S]*?</div>', '', txt)
                new_txt = re.sub(r'<div class="step-card-actions">[\s\S]*?</div>', '', new_txt)
                new_txt = re.sub(r'<button class="[^"]*ss-replace-btn[^"]*">[\s\S]*?</button>', '', new_txt)
                new_txt = re.sub(r'<a class="[^"]*ss-download-btn[^"]*"[\s\S]*?</a>', '', new_txt)
                new_txt = re.sub(r'<input type="file"[^>]*>', '', new_txt)
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(new_txt)
                print(f"Cleaned {p}")

