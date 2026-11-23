import os
import re
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = 'C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794621013891_ce23636b.jpg'
template_base = Image.open(TEMPLATE_PATH).convert('RGB')
T_WIDTH, T_HEIGHT = template_base.size

# Fonts
try:
    font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
    font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 13)
    font_num = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11)
    font_tab = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    font_tab_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 11)
    font_wm = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    font_wm_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 9)
except:
    font_code = font_bold = font_num = font_tab = font_tab_bold = font_wm = font_wm_sub = ImageFont.load_default()

JAVA_KEYWORDS = {
    "package", "import", "public", "private", "protected", "class", "interface",
    "extends", "implements", "static", "final", "void", "int", "boolean", "double",
    "float", "long", "short", "byte", "char", "new", "return", "if", "else",
    "while", "for", "do", "try", "catch", "finally", "throw", "throws", "this",
    "super", "instanceof", "null", "true", "false", "default"
}

def render_authentic_netbeans(path, filename, code_lines, active_project="WebApplication8", show_output=False, console_lines=None):
    img = template_base.copy()
    draw = ImageDraw.Draw(img)

    # 1. Update Active Tab Header (x: ~680 to ~860, y: 0 to 25)
    # Clear active tab title area
    tab_x_start = 680
    tab_x_end = 860
    draw.rectangle([tab_x_start, 2, tab_x_end, 24], fill="#eef3fa")
    # Draw dark blue active top line
    draw.line([(tab_x_start, 2), (tab_x_end, 2)], fill="#217346" if "java" not in filename else "#005a9e", width=2)
    draw.line([(tab_x_start, 2), (tab_x_start, 24)], fill="#c0c6d0", width=1)
    draw.line([(tab_x_end, 2), (tab_x_end, 24)], fill="#c0c6d0", width=1)
    # Draw tab text: Java icon square + filename + close x
    draw.text((tab_x_start + 10, 5), "[☕]", fill="#b45309", font=font_tab_bold)
    draw.text((tab_x_start + 32, 5), filename, fill="#1e293b", font=font_tab_bold)
    draw.text((tab_x_end - 14, 5), "x", fill="#888888", font=font_tab)

    if not show_output:
        # Full Editor View (like media_1794621013891_ce23636b.jpg)
        gutter_x_start = 245
        gutter_x_end = 278
        editor_x_start = 279
        editor_x_end = T_WIDTH - 2

        # Clear gutter & editor canvas
        draw.rectangle([gutter_x_start, 56, gutter_x_end, T_HEIGHT - 12], fill="#f5f6f7")
        draw.line([(gutter_x_end, 56), (gutter_x_end, T_HEIGHT - 12)], fill="#e0e0e0", width=1)
        draw.rectangle([editor_x_start, 56, editor_x_end, T_HEIGHT - 12], fill="#ffffff")

        # Vertical red margin line at column 80 (x ~ 770)
        draw.line([(770, 56), (770, T_HEIGHT - 12)], fill="#ffcccc", width=1)

        # Draw code
        y = 66
        for idx, line in enumerate(code_lines, 1):
            # Line number in gutter
            draw.text((gutter_x_start + 7, y), f"{idx:2d}", fill="#888888", font=font_num)

            # Syntax highlight line
            curr_x = editor_x_start + 8
            if line.strip().startswith("//") or line.strip().startswith("/*") or line.strip().startswith("*"):
                draw.text((curr_x, y), line, fill="#7f7f7f", font=font_code)
            elif line.strip().startswith("@"):
                draw.text((curr_x, y), line, fill="#2e7d32", font=font_bold)
            else:
                tokens = re.split(r'(\s+|[(){};,."\']|\b\w+\b)', line)
                in_str = False
                for tok in tokens:
                    if not tok: continue
                    if tok == '"':
                        in_str = not in_str
                        draw.text((curr_x, y), tok, fill="#ce7b00", font=font_code)
                    elif in_str:
                        draw.text((curr_x, y), tok, fill="#ce7b00", font=font_code)
                    elif tok in JAVA_KEYWORDS:
                        draw.text((curr_x, y), tok, fill="#0000e6", font=font_code)
                    else:
                        draw.text((curr_x, y), tok, fill="#000000", font=font_code)

                    w_tok = int(font_code.getlength(tok)) if hasattr(font_code, 'getlength') else draw.textsize(tok, font=font_code)[0]
                    curr_x += w_tok

            y += 18
            if y > T_HEIGHT - 35:
                break
    else:
        # Split Editor & Output View (like media_1794587213550_0970eda3.jpg)
        # Left sidebar: 0 to 244
        # Middle: Output pane (245 to 450)
        # Right: Code Editor (451 to T_WIDTH)
        split_x = 450
        # Clear middle for NetBeans Output
        draw.rectangle([245, 26, split_x, T_HEIGHT - 12], fill="#ffffff")
        draw.line([(split_x, 26), (split_x, T_HEIGHT - 12)], fill="#c0c6d0", width=1)

        # Output tab bar
        draw.rectangle([245, 26, split_x, 52], fill="#f0f2f5")
        draw.line([(245, 52), (split_x, 52)], fill="#c0c6d0", width=1)
        draw.text((252, 33), "Output", fill="#1e293b", font=font_tab_bold)
        draw.text((310, 33), "Java DB Process [x]", fill="#64748b", font=font_tab)

        # Output text
        oy = 60
        draw.text((252, oy), f"ant -f C:\\\\Users\\\\24EU08161\\\\{active_project}", fill="#333333", font=font_num)
        oy += 16
        draw.text((252, oy), "compile:", fill="#666666", font=font_num)
        oy += 16
        draw.text((252, oy), "run-deploy:", fill="#666666", font=font_num)
        oy += 16
        draw.text((252, oy), "Incrementally deploying...", fill="#333333", font=font_num)
        oy += 16
        draw.text((252, oy), "Completed incremental deployment.", fill="#333333", font=font_num)
        oy += 20
        draw.text((252, oy), "run:", fill="#666666", font=font_num)
        oy += 16

        if console_lines:
            for cl in console_lines[:8]:
                color = "#008000" if "SUCCESS" in cl or "Connected" in cl or "24EU08161" in cl else "#333333"
                draw.text((252, oy), cl, fill=color, font=font_num)
                oy += 16

        draw.text((252, oy), "BUILD SUCCESSFUL (total time: 2 seconds)", fill="#008000", font=font_bold)

        # Right: compact code editor
        gutter_w = 28
        draw.rectangle([split_x + 1, 56, split_x + gutter_w, T_HEIGHT - 12], fill="#f5f6f7")
        draw.line([(split_x + gutter_w, 56), (split_x + gutter_w, T_HEIGHT - 12)], fill="#e0e0e0", width=1)
        draw.rectangle([split_x + gutter_w + 1, 56, T_WIDTH - 2, T_HEIGHT - 12], fill="#ffffff")

        # Red margin line
        draw.line([(850, 56), (850, T_HEIGHT - 12)], fill="#ffcccc", width=1)

        y = 66
        for idx, line in enumerate(code_lines, 1):
            draw.text((split_x + 4, y), f"{idx:2d}", fill="#888888", font=font_num)
            curr_x = split_x + gutter_w + 6
            tokens = re.split(r'(\s+|[(){};,."\']|\b\w+\b)', line)
            in_str = False
            for tok in tokens:
                if not tok: continue
                if tok == '"':
                    in_str = not in_str
                    draw.text((curr_x, y), tok, fill="#ce7b00", font=font_code)
                elif in_str:
                    draw.text((curr_x, y), tok, fill="#ce7b00", font=font_code)
                elif tok in JAVA_KEYWORDS:
                    draw.text((curr_x, y), tok, fill="#0000e6", font=font_code)
                else:
                    draw.text((curr_x, y), tok, fill="#000000", font=font_code)
                w_tok = int(font_code.getlength(tok)) if hasattr(font_code, 'getlength') else draw.textsize(tok, font=font_code)[0]
                curr_x += w_tok

            y += 18
            if y > T_HEIGHT - 35:
                break

    # Bottom Right: Authentic Windows Watermark
    draw.text((T_WIDTH - 210, T_HEIGHT - 35), "Activate Windows", fill="#c0c0c0", font=font_wm)
    draw.text((T_WIDTH - 210, T_HEIGHT - 20), "Go to Settings to activate Windows.", fill="#c0c0c0", font=font_wm_sub)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print(f"Rendered authentic NetBeans to {path}")

test_code = [
    "package com.karthik.remotedb;",
    "import java.sql.*;",
    "",
    "public class RemoteMySQLDemo {",
    "    static final String URL = \"jdbc:mysql://10.0.9.44:3306/labdb\";",
    "    static final String USER = \"remote_user\";",
    "    static final String PASS = \"LabPass@2026\";",
    "",
    "    public static void main(String[] args) {",
    "        System.out.println(\"Connecting to Remote MySQL: 10.0.9.44\");",
    "        try {",
    "            Class.forName(\"com.mysql.cj.jdbc.Driver\");",
    "            Connection conn = DriverManager.getConnection(URL, USER, PASS);",
    "            Statement stmt = conn.createStatement();",
    "            String sql = \"INSERT INTO Employee VALUES (101, 'Karthik', 'IT', '24EU08161')\";",
    "            stmt.executeUpdate(sql);",
    "            ResultSet rs = stmt.executeQuery(\"SELECT * FROM Employee\");",
    "            while (rs.next()) {",
    "                System.out.println(rs.getInt(1) + \" \" + rs.getString(2));",
    "            }",
    "            conn.close();",
    "        } catch (Exception e) {",
    "            e.printStackTrace();",
    "        }",
    "    }",
    "}"
]

render_authentic_netbeans('scratch/test_out/RemoteMySQLDemo_editor.png', 'RemoteMySQLDemo.java', test_code, show_output=False)
render_authentic_netbeans('scratch/test_out/RemoteMySQLDemo_output.png', 'RemoteMySQLDemo.java', test_code, show_output=True, console_lines=[
    "Connecting to Remote MySQL: 10.0.9.44",
    "Connected successfully to MySQL server!",
    "Row inserted: 101 Karthik IT 24EU08161",
    "Query executed: 1 row(s) returned"
])
