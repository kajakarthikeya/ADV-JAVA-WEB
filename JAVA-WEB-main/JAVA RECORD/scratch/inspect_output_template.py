from PIL import Image

im = Image.open('C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794587213550_0970eda3.jpg')
print("Image size:", im.size)

# Check horizontal layout around y=100
# Left sidebar: x=0 to ~244
# Output pane: x=~245 to ?
# Code editor: x=? to 1024
for x in [240, 250, 300, 350, 380, 390, 400, 410, 420, 450]:
    print(f"x={x}: {im.getpixel((x, 100))}")

