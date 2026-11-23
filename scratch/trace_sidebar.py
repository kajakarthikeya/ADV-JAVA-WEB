with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for i in range(564, 775):
    line = lines[i]
    clean = line.split('//')[0]
    depth += clean.count('{') - clean.count('}')
    print(f"{i+1:3d} (depth {depth}): {line.strip()}")
