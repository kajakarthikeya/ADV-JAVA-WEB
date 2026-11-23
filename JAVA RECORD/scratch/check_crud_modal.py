with open('pages/crud.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('zoom-modal')
if pos != -1:
    with open('scratch/crud_modal.txt', 'w', encoding='utf-8') as out:
        out.write(text[pos-50:pos+600])
    print("Found zoom-modal in pages/crud.html")
else:
    print("Not found")

