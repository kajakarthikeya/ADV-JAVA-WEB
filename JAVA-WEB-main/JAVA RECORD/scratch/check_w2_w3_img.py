from PIL import Image

# Check top 30 pixels of week-2/task-1/step-01.png and week-3/task-1/step-01.png
img2 = Image.open('assets/images/week-2/task-1/step-01.png')
print("Week 2 step 1 size:", img2.size)

img3 = Image.open('assets/images/week-3/task-1/step-01.png')
print("Week 3 step 1 size:", img3.size)

