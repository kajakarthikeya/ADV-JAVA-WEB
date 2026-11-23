import re
import io
import sys

out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("step-01.png")
if pos != -1:
    out.write("Context around step-01.png:\n")
    out.write(content[pos-200:pos+250] + "\n\n")

pos4 = content.find("assets/images/week-4")
if pos4 != -1:
    out.write("Context around assets/images/week-4:\n")
    out.write(content[pos4-200:pos4+350] + "\n")
out.flush()
