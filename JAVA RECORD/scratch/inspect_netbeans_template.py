from PIL import Image

im = Image.open('C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794621013891_ce23636b.jpg')
print("Image size:", im.size)

# Let's inspect vertical and horizontal boundaries
# The editor starts after the left sidebar
# Let's find where the left sidebar ends:
# Look along a horizontal line around y=100
for x in range(200, 350):
    px = im.getpixel((x, 100))
    # print pixel to find sidebar border
    # sidebar is grey/white, divider is grey line

print("Sample pixels across x at y=100:")
for x in [220, 230, 240, 241, 242, 245, 250, 260, 270, 280]:
    print(f"x={x}: {im.getpixel((x, 100))}")

# Check top bar
print("Sample pixels down y at x=400:")
for y in [5, 10, 20, 25, 30, 40, 50, 60]:
    print(f"y={y}: {im.getpixel((400, y))}")

