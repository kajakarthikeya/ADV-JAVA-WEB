from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/images", exist_ok=True)

# Generate a high-resolution 256x256 circular-friendly student avatar
size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Circle background with emerald gradient
for y in range(size):
    # gradient from #059669 to #047857
    ratio = y / size
    r = int(5 * (1 - ratio) + 4 * ratio)
    g = int(150 * (1 - ratio) + 120 * ratio)
    b = int(105 * (1 - ratio) + 87 * ratio)
    draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

# Create a circular mask
mask = Image.new("L", (size, size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, size, size), fill=255)

# Apply mask
circle_img = Image.new("RGBA", (size, size))
circle_img.paste(img, (0, 0), mask)
draw = ImageDraw.Draw(circle_img)

# Draw elegant white inner border
draw.ellipse((6, 6, size - 7, size - 7), outline=(209, 250, 229, 220), width=4)

# Try loading font
try:
    font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 92)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)
except:
    font = font_sub = ImageFont.load_default()

# Draw Monogram "VK"
draw.text((size // 2, size // 2 - 20), "VK", fill=(255, 255, 255, 255), font=font, anchor="mm")
draw.text((size // 2, size // 2 + 55), "24EU08161", fill=(209, 250, 229, 255), font=font_sub, anchor="mm")

circle_img.save("assets/images/profile.png")
print("Saved assets/images/profile.png successfully!")

