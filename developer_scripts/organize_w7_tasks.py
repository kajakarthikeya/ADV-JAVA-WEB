import os
import shutil

w7_base = "assets/images/week-7"

task_map = {
    "task-1": [("w7_web_app_setup.png", "step-01.png"), ("w7_web_app_ide.jpg", "step-02.png")],
    "task-2": [
        ("w7_newservlet_code_24EU08161.png", "step-01.png"),
        ("w7_newservlet_browser_24EU08161.png", "step-02.png"),
        ("w7_newservlet_netbeans_ide.jpg", "step-03.png"),
        ("w7_newservlet2_code.jpg", "step-04.png"),
        ("w7_newservlet2_browser.png", "step-05.png")
    ],
    "task-3": [
        ("w7_get_post_html_form.png", "step-01.png"),
        ("w7_get_post_servlet_code.png", "step-02.png"),
        ("w7_get_request_output.png", "step-03.png"),
        ("w7_post_request_output.png", "step-04.png")
    ],
    "task-4": [
        ("w7_generic_servlet_code.png", "step-01.png"),
        ("w7_generic_servlet_output.png", "step-02.png")
    ],
    "task-5": [
        ("w7_lifecycle_servlet_code.png", "step-01.png"),
        ("w7_lifecycle_servlet_output.png", "step-02.png")
    ],
    "task-6": [
        ("w7_student_form_html_code.png", "step-01.png"),
        ("w7_student_form_browser_input.png", "step-02.png"),
        ("w7_student_form_servlet_code.png", "step-03.png"),
        ("w7_student_form_browser_output.png", "step-04.png")
    ]
}

for tdir, files in task_map.items():
    dest_dir = os.path.join(w7_base, tdir)
    os.makedirs(dest_dir, exist_ok=True)
    for src, dst in files:
        src_path = os.path.join(w7_base, src)
        if os.path.exists(src_path):
            shutil.copy2(src_path, os.path.join(dest_dir, dst))

print("Week 7 task subfolders organized.")

