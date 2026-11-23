import shutil
import os

src = "C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794622806575_128a6fbf.jpg"
dst1 = "assets/images/student_photo.jpg"
dst2 = "JAVA-WEB-main/assets/images/student_photo.jpg"

os.makedirs(os.path.dirname(dst1), exist_ok=True)
os.makedirs(os.path.dirname(dst2), exist_ok=True)

shutil.copyfile(src, dst1)
shutil.copyfile(src, dst2)

print(f"Copied student photo to {dst1} ({os.path.getsize(dst1)} bytes)")
print(f"Copied student photo to {dst2} ({os.path.getsize(dst2)} bytes)")

