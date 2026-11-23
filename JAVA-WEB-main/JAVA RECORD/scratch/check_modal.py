with open('index.html', encoding='utf-8') as f:
    content = f.read()

pos = content.find("id=\"zoom-modal\"")
if pos == -1:
    pos = content.find("class=\"zoom-modal\"")
if pos != -1:
    print(content[pos-100:pos+500])
else:
    print("Modal not found with zoom-modal")

