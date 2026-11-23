import os
import re

for p in ['pages/week-0.html', 'pages/week-1.html', 'pages/week-7.html']:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    
    tasks = re.findall(r'id=["\'](week-\d+-task-\d+)["\']', text)
    task_links = re.findall(r'href=["\'](#[^"\']+|week-\d+\.html#[^"\']+)["\']', text)
    galleries = re.findall(r'id=["\']step-gallery["\']', text)
    print(f"{p}:")
    print(f"  Tasks in page: {len(tasks)} -> {tasks}")
    print(f"  Step galleries: {len(galleries)}")
    print(f"  Task links count: {len(task_links)}")

