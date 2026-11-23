import re
import io
import sys

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('pages/week-0.html', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<header.*?</header>', content, re.DOTALL)
if match:
    out.write("Header in pages/week-0.html:\n")
    out.write(match.group(0) + "\n\n")

out.flush()

