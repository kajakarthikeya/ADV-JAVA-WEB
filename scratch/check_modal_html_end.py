import io, sys
out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("id=\"studentProfileModal\"")
if pos != -1:
    out.write(content[pos+1500:pos+2500] + "\n")
out.flush()

