import os
import re

def verify_file(html_path, base_dir):
    print(f"\n--- Verifying {html_path} ---")
    if not os.path.exists(html_path):
        print(f"ERROR: {html_path} does not exist!")
        return False
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all src and href
    matches = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    errors = 0
    checked = 0
    for m in matches:
        if m.startswith('http') or m.startswith('#') or m.startswith('data:') or m.startswith('javascript:'):
            continue
        # Split anchor
        clean_path = m.split('#')[0]
        if not clean_path:
            continue
        full_path = os.path.normpath(os.path.join(base_dir, clean_path))
        checked += 1
        if not os.path.exists(full_path):
            print(f"Missing file: {m} -> resolved to {full_path}")
            errors += 1

    print(f"Total checked links/images: {checked}, Errors: {errors}")
    return errors == 0

def run_all_checks():
    karthik_dir = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK"
    jw_dir = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main"
    
    v1 = verify_file(os.path.join(karthik_dir, "24EU08161.html"), karthik_dir)
    v2 = verify_file(os.path.join(jw_dir, "24EU08161.html"), jw_dir)
    v3 = verify_file(os.path.join(karthik_dir, "JAVA RECORD", "index.html"), os.path.join(karthik_dir, "JAVA RECORD"))
    v4 = verify_file(os.path.join(karthik_dir, "JAVA RECORD", "pages", "week-0.html"), os.path.join(karthik_dir, "JAVA RECORD", "pages"))
    v5 = verify_file(os.path.join(karthik_dir, "JAVA RECORD", "pages", "week-7.html"), os.path.join(karthik_dir, "JAVA RECORD", "pages"))

    if v1 and v2 and v3 and v4 and v5:
        print("\nALL VERIFICATION CHECKS PASSED WITH 0 ERRORS!")
    else:
        print("\nSOME CHECKS FAILED!")

if __name__ == '__main__':
    run_all_checks()

