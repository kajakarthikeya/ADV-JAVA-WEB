with open('ref_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Lab Contents')
with open('ref_sidebar.txt', 'w', encoding='utf-8') as f:
    f.write(html[pos-100:pos+3500])

print("Written ref_sidebar.txt")

