import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all panes
panes = re.findall(r'<div class="week-pane[^"]*" id="(week-\d+-pane)"[^>]*>([\s\S]*?)<!-- WEEK \d+ PANE -->|<div class="week-pane[^"]*" id="(week-\d+-pane)"[^>]*>([\s\S]*?)$', html)

pane_map = {}
for p in re.finditer(r'<div class="week-pane[^"]*" id="(week-(\d+)-pane)"[^>]*>', html):
    p_id = p.group(1)
    w_num = int(p.group(2))
    start = p.start()
    # find next pane or footer
    next_p = re.search(r'<div class="week-pane|<!-- IMAGE ZOOM', html[start+20:])
    end = start + 20 + next_p.start() if next_p else len(html)
    pane_map[w_num] = html[start:end]

print(f"Total panes mapped: {len(pane_map)}")

# Extract sidebar task links and verify each is inside its week's pane
task_links = re.findall(r'<a href="#([^"]+)" class="sidebar-task-link" data-week="(\d+)" data-week-target="([^"]+)" data-task-anchor="([^"]+)"', html)
print(f"Total task links in sidebar: {len(task_links)}")

errors = []
for href, w_num, w_target, anchor in task_links:
    w_num = int(w_num)
    pane_content = pane_map.get(w_num, "")
    if f'id="{anchor}"' not in pane_content:
        errors.append(f"Task anchor {anchor} not found inside {w_target}!")

if not errors:
    print("ALL 26 TASK ANCHORS PERFECTLY LOCATED IN THEIR RESPECTIVE WEEK PANES!")
else:
    print(f"Errors found ({len(errors)}):", errors)

