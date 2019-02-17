from PIL import Image
import math


def distance(one, two):
    dist = 0
    for i in range(3):
        dist += math.pow(one[i] - two[i], 2)
    return math.sqrt(dist)


def chrome_key(img, bg, color_to_replace, save_loc):
    width = min(img.width, bg.width)
    height = min(img.height, bg.height)
    for x in range(width):
        for y in range(height):
            pix = img.getpixel((x, y))
            if distance(pix, color_to_replace) < 180:
                img.putpixel((x, y), bg.getpixel((x, y)))
    img.save(save_loc)


if __name__ == "__main__":
    img = Image.open("img/one.jpg")
    bg = Image.open("img/bg.jpg")
    save_loc = "img/result.png"
    green = (0, 255, 0)
    chrome_key(img, bg, green, save_loc)
