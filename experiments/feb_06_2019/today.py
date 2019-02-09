from PIL import Image
import secrets

im = Image.open('a.png')

print(im.size)
width, height = im.size

pic_width = 4
pic_height = 5

# for x in range(pic_width):
#     for y in range(pic_height):
#         print("Coordinates: ", (x, y))
#         print("Pixel : ", im.getpixel((x, y)))

for x in range(width):
    for y in range(height):
        rgb_val = (
            secrets.choice(range(40, 200)),
            secrets.choice(range(150, 170)),
            secrets.choice(range(50, 200))
            )
        im.putpixel((x,y), rgb_val)
        im.save("new_a.png")
