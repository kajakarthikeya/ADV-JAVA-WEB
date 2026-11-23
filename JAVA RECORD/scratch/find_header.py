import re
import io
import sys

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<header.*?</header>', content, re.DOTALL)
if match:
    out.write("Header in index.html:\n")
    out.write(match.group(0) + "\n\n")

pos = content.find("Venkata Sai Karthikeya Kaja")
if pos != -1:
    out.write("Snippet around Venkata Sai Karthikeya Kaja:\n")
    out.write(content[pos-200:pos+300] + "\n")

out.flush()

