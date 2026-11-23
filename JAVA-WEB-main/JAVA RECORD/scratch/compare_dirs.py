import os
import hashlib

def file_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

files_to_check = [
    'index.html',
    'script.js',
    'style.css',
    'assets/css/topic-page.css',
    'pages/week-0.html',
    'pages/week-1.html',
    'pages/week-2.html'
]

for rel in files_to_check:
    h1 = file_hash(rel)
    h2 = file_hash(os.path.join('JAVA-WEB-main', rel))
    same = (h1 == h2)
    print(f'{rel}: {"MATCH" if same else "DIFF"} (root: {h1[:8] if h1 else "none"}, inner: {h2[:8] if h2 else "none"})')

