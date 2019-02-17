from PIL import Image

"""
File: lab6.py
Name: Jesus A. Bernal Lopez - jebernal@csumb.edu
Due Date: 02/14/2019
Description: Exaplain what happens when we negate a negative image and change the green and
blue channel values by reducing them by 30%.
"""


"""
===== Task 1 =====
To negate a negative we simply do the same thing we do to get the negative of an image. I passed the negative
image to the code that gets the negative of an image and I got the original image.
"""

"""
===== Task 2 =====
Change the green and blue channel values by reducing them by 30%.
"""


def task2(image):
    im = Image.open(image)
    new_list = [(int(a[0]), int(a[1] * 0.7), int(a[2] * 0.7)) for a in im.getdata()]
    im.putdata(list(new_list))
    im.save("img/dog2.png")


if __name__ == "__main__":
    task2("img/dog.png")


"""
Summary: The lab was pretty easy, the only troubling thing was that I tried to use the lambda
approach to get the new_list but was not able to figure it out so reverted to using
list comprehension to get it done
"""
