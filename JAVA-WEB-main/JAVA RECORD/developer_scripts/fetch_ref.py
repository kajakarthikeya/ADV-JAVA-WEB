import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    'https://sahelms.vrsiddhartha.ac.in/java/238W1A1275/',
    headers={'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(req, context=ctx, timeout=8) as response:
    html = response.read().decode('utf-8', errors='ignore')

with open('ref_index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Also fetch styles.css
req_css = urllib.request.Request(
    'https://sahelms.vrsiddhartha.ac.in/java/238W1A1275/styles.css',
    headers={'User-Agent': 'Mozilla/5.0'}
)
try:
    with urllib.request.urlopen(req_css, context=ctx, timeout=8) as response:
        css = response.read().decode('utf-8', errors='ignore')
        with open('ref_styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
    print("Saved ref_styles.css")
except Exception as e:
    print("CSS fetch error:", e)

print("Saved ref_index.html (Length:", len(html), ")")

# Extract sidebar and headers
m = re.search(r'(<aside[\s\S]*?</aside>|<div class="sidebar"[\s\S]*?</div>)', html)
if m:
    print("\n--- SIDEBAR STRUCTURE ---")
    print(m.group(0)[:1500])

print("\n--- HEADINGS ---")
for h in re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html)[:25]:
    print("  *", re.sub(r'<[^>]+>', '', h).strip())

