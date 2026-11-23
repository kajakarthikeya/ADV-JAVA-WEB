import os
import glob
import re

def inspect_pages():
    pages = glob.glob('pages/*.html')
    relative_types = set()
    for p in pages:
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
        for m in matches:
            if not m.startswith('http') and not m.startswith('#') and not m.startswith('data:'):
                prefix = m.split('/')[0] if '/' in m else m
                relative_types.add(prefix)
    print('Relative types in pages/*.html:', relative_types)

if __name__ == '__main__':
    inspect_pages()

