import os
import shutil

src_git = os.path.abspath("scratch/remote_repo/.git")
dst_git = os.path.abspath(".git")

if os.path.exists(src_git):
    if os.path.exists(dst_git):
        shutil.rmtree(dst_git)
    shutil.move(src_git, dst_git)
    print("Moved .git to workspace root successfully.")

if os.path.exists("scratch/remote_repo"):
    shutil.rmtree("scratch/remote_repo")
    print("Removed scratch/remote_repo.")

