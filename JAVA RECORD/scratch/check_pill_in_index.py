import io, sys
out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("header-student-pill")
if pos != -1:
    out.write(content[pos-50:pos+350] + "\n")
out.flush()
