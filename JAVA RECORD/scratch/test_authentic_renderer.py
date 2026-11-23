import os
from PIL import Image, ImageDraw, ImageFont

base_template_path = 'C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794621013891_ce23636b.jpg'
template = Image.open(base_template_path).convert('RGB')
w, h = template.size
print(f"Template loaded: {w}x{h}")

# Create a copy
canvas = template.copy()
draw = ImageDraw.Draw(canvas)

# Clean code area: x from 276 to 1020, y from 55 to 460
draw.rectangle([276, 55, w - 5, h - 15], fill="#ffffff")

# Draw red margin line at column 80 (x ~ 770)
draw.line([(770, 55), (770, h - 15)], fill="#ffcccc", width=1)

# Gutter numbers: x from 245 to 275
draw.rectangle([245, 55, 275, h - 15], fill="#f5f6f7")
draw.line([(275, 55), (275, h - 15)], fill="#e0e0e0", width=1)

# Load font
try:
    font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
    font_num = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11)
    font_watermark = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    font_wm_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 9)
except:
    font_code = font_num = font_watermark = font_wm_sub = ImageFont.load_default()

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
    "                System.out.println(rs.getInt(1) + \" \" + rs.getString(2) + \" \" + rs.getString(3));",
    "            }",
    "            conn.close();",
    "        } catch (Exception e) {",
    "            e.printStackTrace();",
    "        }",
    "    }",
    "}"
]

keywords = {"package", "import", "public", "class", "static", "final", "void", "try", "catch", "while", "new", "throws", "return", "extends", "implements", "protected", "private"}

y = 65
for i, line in enumerate(test_code, 1):
    # Line number
    draw.text((252, y), f"{i:2d}", fill="#888888", font=font_num)
    
    # Syntax highlight line
    x = 285
    # tokenize line by spaces/punctuation
    words = line.split(" ")
    # simple word parser for realistic rendering
    line_trimmed = line
    # Render line with keyword coloring
    if line.strip().startswith("//"):
        draw.text((x, y), line, fill="#7f7f7f", font=font_code)
    elif line.strip().startswith("@"):
        draw.text((x, y), line, fill="#2e7d32", font=font_code)
    else:
        # draw tokens
        curr_x = x
        import re
        tokens = re.split(r'(\s+|[(){};,."\']|\b\w+\b)', line)
        in_string = False
        for tok in tokens:
            if not tok: continue
            if tok == '"':
                in_string = not in_string
                draw.text((curr_x, y), tok, fill="#ce7b00", font=font_code)
            elif in_string:
                draw.text((curr_x, y), tok, fill="#ce7b00", font=font_code)
            elif tok in keywords:
                draw.text((curr_x, y), tok, fill="#0000e6", font=font_code)
            elif tok in {"String", "System", "Class", "Connection", "DriverManager", "Statement", "ResultSet", "Exception"}:
                draw.text((curr_x, y), tok, fill="#000000", font=font_code)
            else:
                draw.text((curr_x, y), tok, fill="#000000", font=font_code)
            w_tok = draw.textsize(tok, font=font_code)[0] if hasattr(draw, 'textsize') else int(font_code.getlength(tok))
            curr_x += w_tok
            
    y += 18
    if y > h - 40:
        break

# Draw Windows watermark
draw.text((w - 210, h - 35), "Activate Windows", fill="#b0b0b0", font=font_watermark)
draw.text((w - 210, h - 20), "Go to Settings to activate Windows.", fill="#b0b0b0", font=font_wm_sub)

os.makedirs('scratch/test_out', exist_ok=True)
canvas.save('scratch/test_out/test_authentic_netbeans.png')
print("Saved authentic NetBeans test to scratch/test_out/test_authentic_netbeans.png")

