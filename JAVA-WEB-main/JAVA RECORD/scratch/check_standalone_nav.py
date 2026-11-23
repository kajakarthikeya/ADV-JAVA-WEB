with open('build_perfect_record.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(480, min(525, len(lines))):
    print(f'{i+1}: {lines[i].strip()}')

