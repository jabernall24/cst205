"""
Michael Avalos-Garcia
Jesus Bernal Lopez
Paul Whipp

Date: 2/23/2019
Course: CST 205
Description: HW 2 - Using glob and sorting to filter pixels from multiple images
                    that were taken of the same location but at different times.
"""

from PIL import Image
import glob

# Needed variables
all_imgs = glob.glob("img/*")
img_data = []
two_d_array = []
finished_img = []

# Does necessary calculations to be able filter multiple
# pictures into one.


def picture_modification():
    # Create list of PIL image objects
    for img in all_imgs:
        img_data.append(Image.open(img).getdata())

    print("Images turned into PIL objects.")

    # # calc median value
    median_idx = ((len(img_data)) // 2)
    print(f"Median index will be {median_idx}.")

    # Add empty lists for each pixel
    for i in range(len(img_data[0])):
        two_d_array.append([])

    print("Pixel arrays initialized.")

    # Add each pixel to appropriate sub-list
    i = 0
    for img in img_data:
        for pixel in img:
            two_d_array[i].append(pixel)
            i += 1
        i = 0

    print("Pixel arrays filled.")

    # Sort sub-lists
    for pix_list in two_d_array:
        pix_list.sort()

    print("More than 1.4 million arrays sorted...")

    # Build image from medians
    for i in range(len(two_d_array)):
        finished_img.append(two_d_array[i][median_idx])

    print("Image data built.")


picture_modification()
# Convert, save, show image
width, height = img_data[0].size
im = Image.new('RGB', (width, height))
im.putdata(finished_img)
im.save("final.png")
im.show()