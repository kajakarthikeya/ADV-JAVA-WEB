with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("Authoritative Lab Source Code")
if pos != -1:
    print("Found 'Authoritative Lab Source Code' at:", pos)
    print(content[pos-100:pos+400])
else:
    print("Not found in index.html")

