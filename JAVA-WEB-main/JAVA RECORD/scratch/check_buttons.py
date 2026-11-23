import re
import io
import sys

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

buttons = re.findall(r'<button[^>]*>(.*?)</button>', content, re.IGNORECASE)
out.write(f"Total buttons in index.html: {len(buttons)}\n")
for b in buttons:
    out.write(f"  Button: {b.strip()[:60]}\n")

links_dl = re.findall(r'<a[^>]*download[^>]*>(.*?)</a>', content, re.IGNORECASE)
out.write(f"Total download links: {len(links_dl)}\n")
for l in links_dl:
    out.write(f"  Download link: {l.strip()[:60]}\n")

out.flush()
