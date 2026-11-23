import re

with open('ref_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', html)
print('Script sources:', scripts)

inline_scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
print('Inline scripts:', len(inline_scripts))
for idx, s in enumerate(inline_scripts):
    print(f"Script {idx}: {len(s)} chars")
    with open(f"ref_script_{idx}.js", "w", encoding="utf-8") as out:
        out.write(s)

