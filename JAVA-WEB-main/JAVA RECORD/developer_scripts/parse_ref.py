import re

with open('ref_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the top header
header = re.search(r'<header[\s\S]*?</header>', html)
if header:
    with open('ref_header_snippet.html', 'w', encoding='utf-8') as f:
        f.write(header.group(0))

# Let's inspect sidebar
sidebar = re.search(r'<div class="sidebar"[\s\S]*?</div>\s*<!-- Main Content', html)
if not sidebar:
    sidebar = re.search(r'<aside[\s\S]*?</aside>', html)
if not sidebar:
    sidebar = re.search(r'<div class="sidebar"[\s\S]*?</nav>', html)

if sidebar:
    with open('ref_sidebar_snippet.html', 'w', encoding='utf-8') as f:
        f.write(sidebar.group(0)[:5000])

# Let's inspect one of the experiment/week sections in the main content
exp = re.search(r'(<div class="content-section" id="week[\s\S]*?</div>\s*<div class="content-section")', html)
if not exp:
    exp = re.search(r'(<section[\s\S]*?</section>)', html)

if exp:
    with open('ref_section_snippet.html', 'w', encoding='utf-8') as f:
        f.write(exp.group(0)[:5000])

print("Extracted snippets to files.")

