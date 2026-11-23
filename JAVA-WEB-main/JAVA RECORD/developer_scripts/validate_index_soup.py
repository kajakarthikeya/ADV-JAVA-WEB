from bs4 import BeautifulSoup
import sys

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Parsing index.html with html.parser...")
soup = BeautifulSoup(html, "html.parser")
print("Successfully parsed index.html!")

# Check all panes
panes = soup.find_all("div", class_="week-pane")
print(f"Found {len(panes)} week panes.")
for p in panes:
    pid = p.get("id")
    display = p.get("style", "")
    print(f"  Pane {pid}: style='{display}'")

