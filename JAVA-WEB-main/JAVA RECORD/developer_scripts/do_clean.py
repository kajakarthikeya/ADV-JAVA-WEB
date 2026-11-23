import os
import shutil
import glob

def clean_root_directory():
    root = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main"
    java_record = os.path.join(root, "JAVA RECORD")
    
    os.makedirs(java_record, exist_ok=True)
    scripts_dir = os.path.join(java_record, "developer_scripts")
    ref_dir = os.path.join(java_record, "reference_files")
    os.makedirs(scripts_dir, exist_ok=True)
    os.makedirs(ref_dir, exist_ok=True)

    # 1. Remove extensionless 24EU08161 duplicate from root
    ext_file = os.path.join(root, "24EU08161")
    if os.path.exists(ext_file):
        os.remove(ext_file)

    # 2. Move all python scripts into JAVA RECORD/developer_scripts
    for py_file in glob.glob(os.path.join(root, "*.py")):
        fname = os.path.basename(py_file)
        dest = os.path.join(scripts_dir, fname)
        shutil.move(py_file, dest)

    # 3. Move all ref_* files into JAVA RECORD/reference_files
    for ref_file in glob.glob(os.path.join(root, "ref_*")):
        fname = os.path.basename(ref_file)
        dest = os.path.join(ref_dir, fname)
        shutil.move(ref_file, dest)

    # 4. Move scratch, test_img, __pycache__, JAVA-WEB-main inner into JAVA RECORD
    for folder_name in ["scratch", "test_img", "__pycache__", "JAVA-WEB-main"]:
        src_path = os.path.join(root, folder_name)
        if os.path.exists(src_path):
            dest_path = os.path.join(java_record, folder_name)
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            shutil.move(src_path, dest_path)

    # 5. Remove loose assets and pages from root (since they are safely in JAVA RECORD)
    loose_assets = os.path.join(root, "assets")
    if os.path.exists(loose_assets):
        shutil.rmtree(loose_assets)

    loose_pages = os.path.join(root, "pages")
    if os.path.exists(loose_pages):
        shutil.rmtree(loose_pages)

    # 6. Remove loose style.css, script.js, index.html, README.md, .gitignore from root
    for f in ["style.css", "script.js", "index.html", "README.md", ".gitignore"]:
        fpath = os.path.join(root, f)
        if os.path.exists(fpath):
            # Already inside JAVA RECORD
            os.remove(fpath)

    # Also clean up extensionless 24EU08161 in parent Downloads\KARTHIK
    parent_ext = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\24EU08161"
    if os.path.exists(parent_ext):
        os.remove(parent_ext)

    print("Cleanup completed successfully!")

if __name__ == '__main__':
    clean_root_directory()
