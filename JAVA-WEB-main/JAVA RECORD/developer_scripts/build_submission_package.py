import os
import shutil
import re
import zipfile

def create_24eu08161_html(source_index_path, target_html_path, folder_prefix="JAVA RECORD/"):
    with open(source_index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Rewrite style.css
    html = re.sub(r'href=["\']style\.css["\']', f'href="{folder_prefix}style.css"', html)
    # Rewrite script.js
    html = re.sub(r'src=["\']script\.js["\']', f'src="{folder_prefix}script.js"', html)
    # Rewrite pages/
    html = re.sub(r'href=["\']pages/', f'href="{folder_prefix}pages/', html)
    # Rewrite assets/
    html = re.sub(r'src=["\']assets/', f'src="{folder_prefix}assets/', html)
    html = re.sub(r'href=["\']assets/', f'href="{folder_prefix}assets/', html)
    # Rewrite brand/home link index.html to 24EU08161.html
    html = re.sub(r'href=["\']index\.html["\']', 'href="24EU08161.html"', html)

    with open(target_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {target_html_path} ({len(html)} bytes)")

def update_page_home_links(pages_dir):
    for fname in os.listdir(pages_dir):
        if fname.endswith('.html'):
            fpath = os.path.join(pages_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update Home links to point to ../../24EU08161.html with fallback
            updated = re.sub(r'href=["\']\.\./index\.html["\']', 'href="../../24EU08161.html"', content)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(updated)
    print(f"Updated home links in {pages_dir}")

def build_package():
    workspace = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main"
    parent_dir = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK"
    
    # 1. Target inside JAVA-WEB-main
    jw_record = os.path.join(workspace, "JAVA RECORD")
    if os.path.exists(jw_record):
        shutil.rmtree(jw_record)
    os.makedirs(jw_record, exist_ok=True)
    
    # Copy assets, pages, style.css, script.js, index.html, README.md, validate_lab_record.py
    shutil.copytree(os.path.join(workspace, "assets"), os.path.join(jw_record, "assets"))
    shutil.copytree(os.path.join(workspace, "pages"), os.path.join(jw_record, "pages"))
    shutil.copy2(os.path.join(workspace, "style.css"), os.path.join(jw_record, "style.css"))
    shutil.copy2(os.path.join(workspace, "script.js"), os.path.join(jw_record, "script.js"))
    shutil.copy2(os.path.join(workspace, "index.html"), os.path.join(jw_record, "index.html"))
    shutil.copy2(os.path.join(workspace, "README.md"), os.path.join(jw_record, "README.md"))
    shutil.copy2(os.path.join(workspace, "validate_lab_record.py"), os.path.join(jw_record, "validate_lab_record.py"))
    
    # Update page home links inside JAVA RECORD/pages
    update_page_home_links(os.path.join(jw_record, "pages"))
    
    # Create 24EU08161.html inside workspace
    jw_index = os.path.join(workspace, "24EU08161.html")
    create_24eu08161_html(os.path.join(workspace, "index.html"), jw_index, "JAVA RECORD/")
    
    # Also create copy without extension just in case
    shutil.copy2(jw_index, os.path.join(workspace, "24EU08161"))

    # 2. Target inside Downloads\KARTHIK
    parent_record = os.path.join(parent_dir, "JAVA RECORD")
    if os.path.exists(parent_record):
        shutil.rmtree(parent_record)
    
    print(f"Copying to {parent_record}...")
    shutil.copytree(jw_record, parent_record)
    
    parent_index = os.path.join(parent_dir, "24EU08161.html")
    create_24eu08161_html(os.path.join(workspace, "index.html"), parent_index, "JAVA RECORD/")
    shutil.copy2(parent_index, os.path.join(parent_dir, "24EU08161"))
    
    # 3. Create a clean zip for submission in Downloads\KARTHIK
    zip_path = os.path.join(parent_dir, "JAVA_RECORD_24EU08161.zip")
    print(f"Creating zip at {zip_path}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add 24EU08161.html at root of zip
        zipf.write(parent_index, arcname="24EU08161.html")
        zipf.write(os.path.join(parent_dir, "24EU08161"), arcname="24EU08161")
        # Add JAVA RECORD folder
        for root, dirs, files in os.walk(parent_record):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, parent_dir)
                zipf.write(full_path, arcname=rel_path)

    print("Package creation finished successfully!")

if __name__ == "__main__":
    build_package()

