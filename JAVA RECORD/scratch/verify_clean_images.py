from PIL import Image

# Check week-2 step-04
im2 = Image.open('assets/images/week-2/task-1/step-04.png')
# Check top-left pixel colors
print("im2 size:", im2.size)
# The background of ubuntu terminal is #300a24 -> rgb(48, 10, 36)
# Previously the title bar was #200015 -> rgb(32, 0, 21)
top_px = im2.getpixel((10, 10))
print("im2 pixel at (10, 10):", top_px)

# Check week-3 step-01
im3 = Image.open('assets/images/week-3/task-1/step-01.png')
print("im3 size:", im3.size)
top_px3 = im3.getpixel((10, 10))
print("im3 pixel at (10, 10):", top_px3)

