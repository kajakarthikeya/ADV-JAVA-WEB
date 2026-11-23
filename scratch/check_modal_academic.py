import io, sys
out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("Academic Year")
if pos != -1:
    out.write(content[pos-50:pos+1200] + "\n")
out.flush()

