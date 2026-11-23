with open('build_all_step_screenshots.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if 'create_netbeans_ide' in l or 'create_sts_ide' in l:
        print(f"Line {i}: {l.strip()[:100]}")

