import re

with open('pages/week-0.html', encoding='utf-8') as f:
    c = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
print('Imgs in pages/week-0.html:', imgs[:3])

# Check css path in pages/week-0.html
links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', c)
print('CSS links in pages/week-0.html:', links[:3])
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', c)
print('Scripts in pages/week-0.html:', scripts[:3])

