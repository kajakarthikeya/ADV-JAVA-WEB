with open('ref_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('ref_styles_snippet.css', 'w', encoding='utf-8') as f:
    f.write(css[:4000])

print("Written ref_styles_snippet.css")

