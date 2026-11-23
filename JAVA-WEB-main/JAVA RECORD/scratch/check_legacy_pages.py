import glob, re

for f in ["pages/crud.html", "pages/msaccess-dsn.html", "pages/mysql.html", "pages/resultset.html", "pages/statement.html"]:
    with open(f, encoding="utf-8") as fp:
        c = fp.read()
    m = re.search(r'<div class="header-student-pill".*?</div>\s*</div>', c, re.DOTALL)
    if m:
        print(f, "Found pill:", m.group(0)[:80])
    else:
        print(f, "No header-student-pill found")

