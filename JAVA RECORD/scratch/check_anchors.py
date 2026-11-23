with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

anchors = [
    'week-0-task-1', 'week-0-task-2', 'week-0-task-3', 'week-0-task-4', 'week-0-task-5',
    'week-1-task-1', 'week-2-task-1', 'week-3-task-1', 'week-4-task-1', 'week-5-task-1',
    'week-6-task-1', 'week-7-task-1', 'week-8-task-1', 'week-9-task-1', 'week-10-task-1'
]

for a in anchors:
    has_id = f'id="{a}"' in text
    print(f'{a}: {"FOUND" if has_id else "MISSING"}')

# Let's search what IDs exist for task sections
import re
section_ids = re.findall(r'<section[^>]*id="([^"]+)"', text)
print('\nFound section IDs:')
for sid in section_ids[:20]:
    print(' ', sid)
