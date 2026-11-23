import os
import shutil
import zipfile
from PIL import Image

uploaded_dir = r"C:\Users\Vineeth Akkinapalli\.gemini\antigravity\brain\a42cb241-3a22-454c-98c5-085a0e293b02\.user_uploaded"
target_images_dir = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\assets\images\week-7"
target_docs_dir = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\assets\documents"

os.makedirs(target_images_dir, exist_ok=True)
os.makedirs(target_docs_dir, exist_ok=True)

# 1. Copy the docx to assets/documents/
docx_name = "media_1794587288775_4b1c0258.docx"
src_docx = os.path.join(uploaded_dir, docx_name)
dest_docx = os.path.join(target_docs_dir, "ADVANCED_JAVA_SERVLET_RECORD_24EU08161.docx")
shutil.copy2(src_docx, dest_docx)
print("Copied docx to assets/documents/ADVANCED_JAVA_SERVLET_RECORD_24EU08161.docx")

# 2. Extract the 13 images from the docx with clear descriptive names
image_map_docx = {
    "image1.png": "w7_web_app_setup.png",
    "image2.png": "w7_get_post_servlet_code.png",
    "image3.png": "w7_get_post_html_form_code.png",
    "image4.png": "w7_get_request_output.png",
    "image5.png": "w7_post_request_output.png",
    "image6.png": "w7_generic_servlet_code.png",
    "image7.png": "w7_generic_servlet_output.png",
    "image8.png": "w7_lifecycle_servlet_code.png",
    "image9.png": "w7_lifecycle_servlet_output.png",
    "image10.png": "w7_student_form_html_code.png",
    "image11.png": "w7_student_form_servlet_code.png",
    "image12.png": "w7_student_form_browser_input.png",
    "image13.png": "w7_student_form_browser_output.png"
}

with zipfile.ZipFile(src_docx, "r") as z:
    for orig, new_name in image_map_docx.items():
        zip_path = f"word/media/{orig}"
        if zip_path in z.namelist():
            out_path = os.path.join(target_images_dir, new_name)
            with open(out_path, "wb") as f:
                f.write(z.read(zip_path))
            print(f"Extracted {orig} -> {new_name}")

# 3. Save the individually uploaded images
individual_images = {
    "media_1794587219693_af9e4cf0.png": "w7_newservlet_code_24EU08161.png",
    "media_1794587232538_70738f5a.png": "w7_newservlet_browser_24EU08161.png",
    "media_1794587213550_0970eda3.jpg": "w7_newservlet_netbeans_ide.jpg",
    "media_1794587242321_2c509595.jpg": "w7_newservlet2_code.jpg",
    "media_1794587249461_656bb8df.png": "w7_newservlet2_browser.png",
    "media_1794587185755_2e63cbdd.jpg": "w7_web_app_ide.jpg"
}

for src_name, dest_name in individual_images.items():
    s = os.path.join(uploaded_dir, src_name)
    if os.path.exists(s):
        d = os.path.join(target_images_dir, dest_name)
        shutil.copy2(s, d)
        print(f"Copied individual image {src_name} -> {dest_name}")

print("All Week 7 images processed successfully!")
