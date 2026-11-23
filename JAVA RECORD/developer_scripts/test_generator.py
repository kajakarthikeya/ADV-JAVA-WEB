from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("test_img", exist_ok=True)

# Test creating a NetBeans IDE mockup
w, h = 960, 600
img = Image.new("RGB", (w, h), "#f0f0f0")
draw = ImageDraw.Draw(img)

# Title bar
draw.rectangle([0, 0, w, 32], fill="#005a9e")
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
    font_menu = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
    font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
except:
    font_title = font_menu = font_code = font_bold = ImageFont.load_default()

draw.text((10, 8), "NetBeans IDE 8.2 - JavaApplication_StudentCRUD", fill="white", font=font_title)

# Window buttons (Windows style)
draw.text((w - 70, 6), "-  [ ]  X", fill="white", font=font_title)

# Menu bar
draw.rectangle([0, 32, w, 58], fill="#f5f5f5")
draw.line([(0, 58), (w, 58)], fill="#dcdcdc", width=1)
draw.text((12, 38), "File    Edit    View    Navigate    Source    Refactor    Run    Debug    Profile    Tools    Window    Help", fill="#333333", font=font_menu)

# Left sidebar (Projects tree)
draw.rectangle([0, 59, 230, 420], fill="#ffffff")
draw.line([(230, 59), (230, 420)], fill="#dcdcdc", width=1)
draw.rectangle([0, 59, 230, 84], fill="#f0f4f8")
draw.text((10, 65), "Projects", fill="#1e293b", font=font_bold)
draw.text((10, 95), "[-] StudentCRUD_Project\n    [+] Source Packages\n        [-] com.karthik.crud\n            [#] StudentCRUD.java\n    [+] Libraries\n        [#] mysql-connector-j-8.0.jar", fill="#475569", font=font_code)

# Code Editor area
draw.rectangle([231, 59, w, 420], fill="#ffffff")
# Editor tab
draw.rectangle([231, 59, 380, 84], fill="#ffffff")
draw.line([(231, 84), (w, 84)], fill="#dcdcdc", width=1)
draw.text((245, 65), "[C] StudentCRUD.java  x", fill="#005a9e", font=font_bold)

# Code lines
code_sample = """ 1  package com.karthik.crud;
 2  import java.sql.*;
 3  
 4  public class StudentCRUD {
 5      static final String URL = "jdbc:mysql://localhost:3306/studentdb";
 6      static final String USER = "root";
 7      static final String PASS = "password";
 8  
 9      public static void main(String[] args) {
10          System.out.println("Roll Number: 24EU08161 - Student CRUD Operations");
11          // INSERT student record
12          String sql = "INSERT INTO Student VALUES ('24EU08161', 'Karthik', 'IT')";
13      }
14  }"""
draw.text((240, 95), code_sample, fill="#1e293b", font=font_code)

# Output Console panel
draw.rectangle([0, 420, w, h], fill="#1e1e1e")
draw.rectangle([0, 420, w, 442], fill="#2d2d2d")
draw.text((10, 424), "Output - JavaApplication_StudentCRUD (run)", fill="#cccccc", font=font_menu)
draw.text((10, 450), "run:\nConnected to studentdb successfully!\nInserted Student: Roll: 24EU08161 | Name: Karthik | Dept: IT\nBUILD SUCCESSFUL (total time: 1 second)", fill="#4ec9b0", font=font_code)

img.save("test_img/netbeans_sample.png")
print("Saved test_img/netbeans_sample.png successfully!")

