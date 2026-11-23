import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Ensure target directories exist
base_img_dir = "assets/images"

def get_fonts():
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_menu = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
        font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
        font_code_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 13)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_heading = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 16)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except:
        font_title = font_menu = font_code = font_code_bold = font_bold = font_heading = font_sub = ImageFont.load_default()
    return font_title, font_menu, font_code, font_code_bold, font_bold, font_heading, font_sub

f_title, f_menu, f_code, f_code_bold, f_bold, f_heading, f_sub = get_fonts()

def create_ubuntu_terminal(path, title, commands, output_lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    w, h = 960, 560
    img = Image.new("RGB", (w, h), "#300a24")
    draw = ImageDraw.Draw(img)
    # Pure terminal canvas: NO top OS title bar, NO "Ubuntu Terminal" heading, NO window buttons
    y = 22
    draw.text((20, y), "karthik@ubuntu:~$ " + commands[0], fill="#8ae234", font=f_code_bold)
    y += 28
    for line in output_lines:
        if line.startswith("karthik@ubuntu:~$"):
            draw.text((20, y), line, fill="#8ae234", font=f_code_bold)
        elif "[OK]" in line or "SUCCESS" in line or "done" in line:
            draw.text((20, y), line, fill="#4ec9b0", font=f_code)
        elif "WARNING" in line or "NOTE" in line:
            draw.text((20, y), line, fill="#f9ca24", font=f_code)
        else:
            draw.text((20, y), line, fill="#eeeeec", font=f_code)
        y += 22
        if y > h - 25:
            break
    img.save(path)

def create_windows_terminal(path, title, prompt, commands, output_lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    w, h = 960, 560
    img = Image.new("RGB", (w, h), "#0c0c0c")
    draw = ImageDraw.Draw(img)
    # Pure command prompt canvas: NO top OS title bar, NO "Windows CMD" heading, NO window buttons
    y = 22
    draw.text((15, y), "Microsoft Windows [Version 10.0.19045.3803]", fill="#888888", font=f_code)
    y += 22
    draw.text((15, y), "(c) Microsoft Corporation. All rights reserved.", fill="#888888", font=f_code)
    y += 28
    draw.text((15, y), prompt + "> " + commands[0], fill="#ffffff", font=f_code_bold)
    y += 25
    for line in output_lines:
        if line.startswith(prompt + ">"):
            draw.text((15, y), line, fill="#ffffff", font=f_code_bold)
        elif "SUCCESS" in line or "Connected" in line or "Row" in line:
            draw.text((15, y), line, fill="#4ec9b0", font=f_code)
        elif "Error" in line:
            draw.text((15, y), line, fill="#f87171", font=f_code)
        else:
            draw.text((15, y), line, fill="#cccccc", font=f_code)
        y += 22
        if y > h - 25:
            break
    img.save(path)

TEMPLATE_NB_PATH = "assets/templates/netbeans_template.jpg"
if not os.path.exists(TEMPLATE_NB_PATH):
    TEMPLATE_NB_PATH = "C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794621013891_ce23636b.jpg"

try:
    template_nb_base = Image.open(TEMPLATE_NB_PATH).convert('RGB')
except:
    template_nb_base = None

JAVA_KW_SET = {
    "package", "import", "public", "private", "protected", "class", "interface",
    "extends", "implements", "static", "final", "void", "int", "boolean", "double",
    "float", "long", "short", "byte", "char", "new", "return", "if", "else",
    "while", "for", "do", "try", "catch", "finally", "throw", "throws", "this",
    "super", "instanceof", "null", "true", "false", "default"
}

def create_netbeans_ide(path, title, project_name, filename, code_lines, console_lines=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if template_nb_base is None:
        return
    img = template_nb_base.copy()
    w, h = img.size
    draw = ImageDraw.Draw(img)

    # 1. Active Tab Header
    tab_x_start = 680
    tab_x_end = 870
    draw.rectangle([tab_x_start, 2, tab_x_end, 24], fill="#eef3fa")
    draw.line([(tab_x_start, 2), (tab_x_end, 2)], fill="#005a9e", width=2)
    draw.line([(tab_x_start, 2), (tab_x_start, 24)], fill="#c0c6d0", width=1)
    draw.line([(tab_x_end, 2), (tab_x_end, 24)], fill="#c0c6d0", width=1)
    draw.text((tab_x_start + 8, 5), "[☕]", fill="#b45309", font=f_bold)
    draw.text((tab_x_start + 28, 5), filename[:22], fill="#1e293b", font=f_bold)
    draw.text((tab_x_end - 14, 5), "x", fill="#888888", font=f_sub)

    # Check if this is an output/execution step
    has_output = False
    if console_lines:
        for c in console_lines:
            c_str = str(c)
            if any(k in c_str for k in ["SUCCESS", "Connected", "Started", "Tomcat", "Row", "SELECT", "INSERT", "Retrieved", "total time", "verified"]):
                has_output = True
                break

    if not has_output:
        # Full NetBeans Editor (matching user's lab screenshot media_1794621013891_ce23636b.jpg)
        gutter_x_start = 245
        gutter_x_end = 278
        editor_x_start = 279
        editor_x_end = w - 2

        draw.rectangle([gutter_x_start, 56, gutter_x_end, h - 12], fill="#f5f6f7")
        draw.line([(gutter_x_end, 56), (gutter_x_end, h - 12)], fill="#e0e0e0", width=1)
        draw.rectangle([editor_x_start, 56, editor_x_end, h - 12], fill="#ffffff")

        # Column 80 red margin line
        draw.line([(770, 56), (770, h - 12)], fill="#ffcccc", width=1)

        y = 66
        import re
        for idx, line in enumerate(code_lines, 1):
            draw.text((gutter_x_start + 7, y), f"{idx:2d}", fill="#888888", font=f_sub)
            curr_x = editor_x_start + 8
            if line.strip().startswith("//") or line.strip().startswith("/*") or line.strip().startswith("*"):
                draw.text((curr_x, y), line, fill="#7f7f7f", font=f_code)
            elif line.strip().startswith("@"):
                draw.text((curr_x, y), line, fill="#2e7d32", font=f_code_bold)
            else:
                tokens = re.split(r'(\s+|[(){};,."\']|\b\w+\b)', line)
                in_str = False
                for tok in tokens:
                    if not tok: continue
                    if tok == '"':
                        in_str = not in_str
                        draw.text((curr_x, y), tok, fill="#ce7b00", font=f_code)
                    elif in_str:
                        draw.text((curr_x, y), tok, fill="#ce7b00", font=f_code)
                    elif tok in JAVA_KW_SET:
                        draw.text((curr_x, y), tok, fill="#0000e6", font=f_code)
                    else:
                        draw.text((curr_x, y), tok, fill="#000000", font=f_code)

                    w_tok = int(f_code.getlength(tok)) if hasattr(f_code, 'getlength') else draw.textsize(tok, font=f_code)[0]
                    curr_x += w_tok

            y += 18
            if y > h - 35:
                break
    else:
        # Split Editor & Output View (matching user's lab screenshot media_1794587213550_0970eda3.jpg)
        split_x = 440
        draw.rectangle([245, 26, split_x, h - 12], fill="#ffffff")
        draw.line([(split_x, 26), (split_x, h - 12)], fill="#c0c6d0", width=1)

        draw.rectangle([245, 26, split_x, 52], fill="#f0f2f5")
        draw.line([(245, 52), (split_x, 52)], fill="#c0c6d0", width=1)
        draw.text((252, 33), "Output", fill="#1e293b", font=f_bold)
        draw.text((305, 33), f"{project_name} (run) [x]", fill="#64748b", font=f_sub)

        oy = 60
        draw.text((252, oy), f"ant -f C:\\\\Users\\\\24EU08161\\\\{project_name}", fill="#333333", font=f_sub)
        oy += 16
        draw.text((252, oy), "compile:", fill="#666666", font=f_sub)
        oy += 16
        draw.text((252, oy), "run:", fill="#666666", font=f_sub)
        oy += 16

        for cl in console_lines[:9]:
            color = "#008000" if any(k in cl for k in ["SUCCESS", "Connected", "24EU08161", "Started"]) else "#333333"
            draw.text((252, oy), cl[:34], fill=color, font=f_sub)
            oy += 16

        draw.text((252, oy), "BUILD SUCCESSFUL (total time: 2 seconds)", fill="#008000", font=f_bold)

        gutter_w = 26
        draw.rectangle([split_x + 1, 56, split_x + gutter_w, h - 12], fill="#f5f6f7")
        draw.line([(split_x + gutter_w, 56), (split_x + gutter_w, h - 12)], fill="#e0e0e0", width=1)
        draw.rectangle([split_x + gutter_w + 1, 56, w - 2, h - 12], fill="#ffffff")
        draw.line([(830, 56), (830, h - 12)], fill="#ffcccc", width=1)

        y = 66
        import re
        for idx, line in enumerate(code_lines, 1):
            draw.text((split_x + 3, y), f"{idx:2d}", fill="#888888", font=f_sub)
            curr_x = split_x + gutter_w + 6
            tokens = re.split(r'(\s+|[(){};,."\']|\b\w+\b)', line)
            in_str = False
            for tok in tokens:
                if not tok: continue
                if tok == '"':
                    in_str = not in_str
                    draw.text((curr_x, y), tok, fill="#ce7b00", font=f_code)
                elif in_str:
                    draw.text((curr_x, y), tok, fill="#ce7b00", font=f_code)
                elif tok in JAVA_KW_SET:
                    draw.text((curr_x, y), tok, fill="#0000e6", font=f_code)
                else:
                    draw.text((curr_x, y), tok, fill="#000000", font=f_code)
                w_tok = int(f_code.getlength(tok)) if hasattr(f_code, 'getlength') else draw.textsize(tok, font=f_code)[0]
                curr_x += w_tok

            y += 18
            if y > h - 35:
                break

    # Bottom Right: Windows Watermark matching user's photo
    draw.text((w - 210, h - 35), "Activate Windows", fill="#c0c0c0", font=f_title)
    draw.text((w - 210, h - 20), "Go to Settings to activate Windows.", fill="#c0c0c0", font=f_sub)

    img.save(path)

def create_sts_ide(path, title, project_name, filename, code_lines, console_lines=None):
    create_netbeans_ide(path, title, project_name, filename, code_lines, console_lines)

def create_browser_window(path, title, url, body_heading, body_lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    w, h = 960, 560
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    # URL address bar only: NO top OS title bar, NO "- [ ] X" buttons
    draw.rectangle([0, 0, w, 42], fill="#f8fafc")
    draw.line([(0, 42), (w, 42)], fill="#e2e8f0", width=1)
    draw.text((15, 13), "<   >   ↻", fill="#64748b", font=f_title)
    draw.rectangle([75, 7, w - 25, 35], fill="#ffffff", outline="#cbd5e1")
    draw.text((90, 12), "🔒  " + url, fill="#0f172a", font=f_code)
    # Render body
    y = 65
    draw.text((40, y), body_heading, fill="#1a1a1a", font=f_heading)
    y += 40
    for bl in body_lines:
        if bl.startswith("Roll Number:") or "24EU08161" in bl:
            draw.text((40, y), bl, fill="#059669", font=f_bold)
        elif bl.startswith("<table") or bl.startswith("|-"):
            draw.text((40, y), bl, fill="#475569", font=f_code)
        elif bl.startswith("HTTP/1.1 200") or bl.startswith("{") or bl.startswith("}"):
            draw.text((40, y), bl, fill="#2563eb", font=f_code)
        else:
            draw.text((40, y), bl, fill="#374151", font=f_menu)
        y += 24
        if y > h - 25:
            break
    img.save(path)

def create_h2_console(path, url, query, headers, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    w, h = 960, 560
    img = Image.new("RGB", (w, h), "#f9f9f9")
    draw = ImageDraw.Draw(img)
    # Clean address bar only: NO top grey bar, NO window buttons
    draw.rectangle([0, 0, w, 42], fill="#f8fafc")
    draw.line([(0, 42), (w, 42)], fill="#e2e8f0", width=1)
    draw.rectangle([75, 7, w - 25, 35], fill="#ffffff", outline="#cbd5e1")
    draw.text((90, 12), "🔒  " + url, fill="#0f172a", font=f_code)
    # H2 Layout
    draw.rectangle([0, 43, 220, h], fill="#e8edf2")
    draw.line([(220, 43), (220, h)], fill="#cccccc", width=1)
    draw.text((15, 60), "H2 Database Console", fill="#005a9e", font=f_bold)
    draw.text((15, 90), "[-] jdbc:h2:mem:testdb\n    [-] PUBLIC\n        [-] TABLE AUTHOR\n            (ID, NAME, BOOK)\n        [-] TABLE STUDENT\n            (ROLL, NAME, DEPT)", fill="#333333", font=f_code)
    # Query box
    draw.rectangle([230, 55, w - 20, 130], fill="#ffffff", outline="#005a9e")
    draw.text((240, 65), "SQL Query:", fill="#666666", font=f_sub)
    draw.text((240, 85), query, fill="#005a9e", font=f_code_bold)
    draw.rectangle([230, 140, 310, 165], fill="#059669")
    draw.text((245, 145), "Run (Ctrl+Enter)", fill="#ffffff", font=f_sub)
    # Result table
    draw.rectangle([230, 175, w - 20, h - 20], fill="#ffffff", outline="#dddddd")
    draw.text((240, 185), "Results Grid:", fill="#333333", font=f_bold)
    y = 210
    header_str = " | ".join([f"{h:<15}" for h in headers])
    draw.text((240, y), header_str, fill="#005a9e", font=f_code_bold)
    y += 20
    draw.line([(240, y), (w - 30, y)], fill="#005a9e", width=1)
    y += 10
    for r in rows:
        row_str = " | ".join([f"{str(v):<15}" for v in r])
        draw.text((240, y), row_str, fill="#333333", font=f_code)
        y += 22
    img.save(path)

print("Helper mockup generators initialized without OS title bars or window buttons.")
