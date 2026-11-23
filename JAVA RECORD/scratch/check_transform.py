with open('build_perfect_record.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if 'transform_week_content' in l or 'assemble_standalone_page' in l:
        print(f'{i+1}: {l}')
