with open('JAVA-WEB-main/index.html', 'r', encoding='utf-8') as f:
    inner_lines = f.readlines()

for i in range(50, 110):
    if i < len(inner_lines):
        print(f'{i+1}: {inner_lines[i].strip()}')

