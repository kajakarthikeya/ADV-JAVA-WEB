with open('ref_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Lab Contents')
if pos != -1:
    print("Found 'Lab Contents' at:", pos)
    print(html[pos-100:pos+2500])
else:
    print("'Lab Contents' not found directly. Searching for sidebar tags:")
    import re
    for m in re.finditer(r'<[^>]+class="[^"]*sidebar[^"]*"[^>]*>', html):
        print("Match:", m.group(0))
        p = m.start()
        print(html[p:p+1000])
        break

