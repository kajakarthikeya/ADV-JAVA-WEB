import os
import re

matches = []
for root, dirs, files in os.walk('.'):
    if '.gemini' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.js', '.css', '.py')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    hits = []
                    if 'Replace' in content:
                        hits.append('Replace')
                    if 'Choose File' in content or 'type="file"' in content or "type='file'" in content:
                        hits.append('File input')
                    if 'Ubuntu Terminal' in content:
                        hits.append('Ubuntu Terminal')
                    if 'Windows CMD' in content:
                        hits.append('Windows CMD')
                    if hits:
                        matches.append(f"{p}: {', '.join(hits)}")
            except Exception as e:
                pass

with open('scratch/found_user_elements.txt', 'w', encoding='utf-8') as out:
    out.write("\n".join(matches))

print(f"Total files with hits: {len(matches)}")

