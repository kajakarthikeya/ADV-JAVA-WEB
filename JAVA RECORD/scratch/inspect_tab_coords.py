from PIL import Image

im = Image.open('C:/Users/Vineeth Akkinapalli/.gemini/antigravity/brain/a42cb241-3a22-454c-98c5-085a0e293b02/.user_uploaded/media_1794621013891_ce23636b.jpg')

# Let's inspect the tab region (y=0 to 25, x=245 to 800)
# Let's find where GetPostServlet tab is located
for x in range(500, 750, 20):
    print(f"x={x}, y=12: {im.getpixel((x, 12))}")

