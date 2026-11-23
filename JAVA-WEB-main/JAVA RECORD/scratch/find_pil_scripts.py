import os

for root, dirs, files in os.walk('.'):
    if '.gemini' in root:
        continue
    for f in files:
        if f.endswith('.py'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
                if 'ImageDraw' in txt or 'PIL' in txt:
                    print(f"PIL/ImageDraw found in: {p}")

