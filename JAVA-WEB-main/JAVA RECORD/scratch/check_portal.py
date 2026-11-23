import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

panes = re.findall(r'id=["\'](week-\d+-pane)["\']', text)
weeks = re.findall(r'id=["\'](week-\d+)["\']', text)
tasks = re.findall(r'id=["\'](week-\d+-task-\d+)["\']', text)
task_links = re.findall(r'href=["\']#(week-\d+-task-\d+)["\']', text)

print(f"Panes found: {len(panes)} -> {panes}")
print(f"Week IDs found: {len(weeks)} -> {weeks}")
print(f"Task IDs found: {len(tasks)} -> {tasks}")
print(f"Task Links found: {len(task_links)} -> {task_links}")

# Check missing task IDs
missing = [t for t in set(task_links) if t not in set(tasks)]
print(f"MISSING TASK ANCHORS IN INDEX.HTML: {missing}")
