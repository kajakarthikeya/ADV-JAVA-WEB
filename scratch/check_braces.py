with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for idx, line in enumerate(lines, 1):
    open_c = line.count('{')
    close_c = line.count('}')
    # simplistic, ignore comments/strings for quick check
    depth += (open_c - close_c)
    if 'function initPortalSidebar' in line:
        sidebar_start = idx
        sidebar_depth = depth - 1

print(f"Final depth at end of file: {depth}")
print(f"Sidebar start line: {sidebar_start}")

# Trace depth from sidebar_start
depth = 0
for idx in range(sidebar_start - 1, len(lines)):
    line = lines[idx]
    # strip line comments
    clean = line.split('//')[0]
    depth += clean.count('{') - clean.count('}')
    if 'function copyCode' in line:
        print(f"Depth before function copyCode (line {idx+1}): {depth}")
        break
