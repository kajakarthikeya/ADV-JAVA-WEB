import os
import re

def inspect():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print('style.css count:', content.count('style.css'))
    print('script.js count:', content.count('script.js'))
    print('href="pages/ count:', content.count('href="pages/'))
    print('src="assets/ count:', content.count('src="assets/'))
    print('href="assets/ count:', content.count('href="assets/'))
    print('href="index.html" count:', content.count('href="index.html"'))

    matches = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    unique_matches = sorted(list(set(matches)))
    others = []
    for m in unique_matches:
        if not m.startswith('http') and not m.startswith('#') and not m.startswith('data:'):
            if not (m.startswith('assets/') or m.startswith('pages/') or m in ['style.css', 'script.js', 'index.html']):
                others.append(m)
    print('Other non-http, non-hash relative links:', others)

if __name__ == '__main__':
    inspect()
