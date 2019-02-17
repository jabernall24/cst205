# Jesus Andres Bernal
# Michael Avalos-Garcia
# Paul Whipp

# Task one: Max Red pixel

from PIL import Image
import math
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
import colormath.color_diff as cm_cd # delta_e_cie2000

im = Image.open('img/preyer.jpg')


def de(color_1, color_2):
    return cm_cd.delta_e_cie2000(color_1, color_2)


# turn scaled RGB pixel
def l_c(pixel):
    rgb = sRGBColor(pixel[0], pixel[1], pixel[2], True)
    return convert_color(rgb, LabColor)


def find_max_red(im):
    # get data as flat list, assign names
    pixel_list = list(im.getdata())
    max_red = -1
    curr_max_tup = None
    pos = 0
    # find max routine
    for p in pixel_list:
        if(p[0] > max_red):
            curr_max_tup = p
            max_red = p[0]
        if(max_red == 255):
            break;
        pos += 1
    # get image dimensions
    width, height = im.size
    # calculate coordinates
    y_coord = pos // width
    x_coord = pos % width
    # return all values
    return curr_max_tup, x_coord, y_coord


def blank_canvas(width, height, color):
    store_list = []
    for p in range(width*height):
        store_list.append(color)
    im = Image.new('RGB', (width,height))
    im.putdata(store_list)
    im.show()

# blank_canvas(3000,3000,(255,2,100))

"""
# Color mode, dimen tuple (may be switched?), base color
# From ~ 22 min mark in lecture 7
new_im = Image.new('RGB', (width, height), 'salmon')
"""


# Task 4, Chroma Key Mania
def distance_2(color_1, color_2):
    red_diff = math.pow((color_1[0] - color_2[0]), 2)
    green_diff = math.pow((color_1[1] - color_2[1]), 2)
    blue_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)


def swatch_sample(start_x, start_y, size, im):
    rgb = [0, 0, 0]
    pixel = None
    for x in range(start_x, start_x + size):
        for y in range(start_y, start_y + size):
            px = im.getpixel((x, y))
            rgb[0] += px[0]
            rgb[1] += px[1]
            rgb[2] += px[2]
    size_sq = size*size
    rgb[0] /= size_sq
    rgb[1] /= size_sq
    rgb[2] /= size_sq
    return tuple(rgb)


def chromakey_de(source, bg, offset_x, offset_y):
    #source size plus offset must be less than bg size
    green = (0, 147, 34)
    perc_done = .1
    for x in range(source.width):
        for y in range(source.height):
            coord = (x, y)
            curr_pix = source.getpixel(coord)
            if de(l_c(curr_pix), l_c(green)) < 24.0:
                source.putpixel(coord, bg.getpixel((offset_x + x, offset_y + y)))
        if x == int(source.width * perc_done):
            print(f"Chromakey is {int(perc_done * 100)}% done.")
            perc_done += .1
    source.save('img/chromakeyed.png')


# task 3
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
    max_tup, x_c, y_c = find_max_red(im)
    print(f"tuple: {max_tup} xcoord: {x_c} ycoord: {y_c}")
    img = Image.open("img/one.jpg")
    bg = Image.open("img/bg.jpg")
    save_loc = "img/result.png"
    green = (0, 255, 0)
    chrome_key(img, bg, green, save_loc)
