with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('proof-card')
if pos != -1:
    with open('scratch/proof_card.txt', 'w', encoding='utf-8') as out:
        out.write(text[pos-100:pos+800])
    print("Found proof-card, wrote to scratch/proof_card.txt")
else:
    print("proof-card not found")

