with open('ref_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.side-nav')
with open('ref_nav_styles.css', 'w', encoding='utf-8') as f:
    f.write(css[pos:pos+4000])

print("Written ref_nav_styles.css")

