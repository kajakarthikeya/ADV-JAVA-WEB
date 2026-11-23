import io, sys
out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("class=\"student-details-grid\"")
if pos != -1:
    out.write(content[pos:pos+1500] + "\n")
out.flush()

