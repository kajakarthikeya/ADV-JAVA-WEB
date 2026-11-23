with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

out = []
out.append('--- Modal in index.html ---')
pos = text.find('ssModal')
if pos != -1:
    out.append(text[pos-50:pos+600])

out.append('\n--- Downloads section in index.html ---')
pos2 = text.find('id="downloads"')
if pos2 != -1:
    out.append(text[pos2-50:pos2+600])

out.append('\n--- Search for zoom-modal or ss-modal ---')
out.append(f'zoom-modal in index.html: {"zoom-modal" in text}')
out.append(f'ss-modal in index.html: {"ss-modal" in text}')
out.append(f'ssModal in index.html: {"ssModal" in text}')

with open('scratch/output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Wrote output to scratch/output.txt")
