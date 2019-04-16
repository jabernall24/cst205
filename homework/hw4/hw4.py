# Names: Paul Whipp, Jesus Andres Bernal Lopez, Michael Avalos-Garcia
# Date: 3/31/2019
# Course Name: CST 205
# Abstract: This program renders three unique images on a website
#           and has clickable links to the pictures.

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from random import randint
from PIL import Image

# storing image data in images_info
image_info = [
    {
        "id": "34694102243_3370955cf9_z",
        "title": "Eastern",
        "flickr_user": "Sean Davis",
        "tags": ["Los Angeles", "California", "building"]
    },
    {
        "id": "37198655640_b64940bd52_z",
        "title": "Spreetunnel",
        "flickr_user": "Jens-Olaf Walter",
        "tags": ["Berlin", "Germany", "tunnel", "ceiling"]
    },
    {
        "id": "36909037971_884bd535b1_z",
        "title": "East Side Gallery",
        "flickr_user": "Pieter van der Velden",
        "tags": ["Berlin", "wall", "mosaic", "sky", "clouds"]
    },
    {
        "id": "36604481574_c9f5817172_z",
        "title": "Lombardia, september 2017",
        "flickr_user": "Monica Pinheiro",
        "tags": ["Italy", "Lombardia", "alley", "building", "wall"]
    },
    {
        "id": "36885467710_124f3d1e5d_z",
        "title": "Palazzo Madama",
        "flickr_user": "Kevin Kimtis",
        "tags": ["Rome", "Italy", "window", "road", "building"]
    },
    {
        "id": "37246779151_f26641d17f_z",
        "title": "Rijksmuseum library",
        "flickr_user": "John Keogh",
        "tags": ["Amsterdam", "Netherlands", "book", "library", "museum"]
    },
    {
        "id": "36523127054_763afc5ed0_z",
        "title": "Canoeing in Amsterdam",
        "flickr_user": "bdodane",
        "tags": ["Amsterdam", "Netherlands", "canal", "boat"]
    },
    {
        "id": "35889114281_85553fed76_z",
        "title": "Quiet at dawn, Cabo San Lucas",
        "flickr_user": "Erin Johnson",
        "tags": ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
    },
    {
        "id": "34944112220_de5c2684e7_z",
        "title": "View from our rental",
        "flickr_user": "Doug Finney",
        "tags": ["Mexico", "ocean", "beach", "palm"]
    },
    {
        "id": "36140096743_df8ef41874_z",
        "title": "Someday",
        "flickr_user": "Thomas Hawk",
        "tags": ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
    }
]

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():

    # three random images; pass here and then for loop in template
    # selecting random images from the images package
    index1 = randint(0, 9)
    index2 = randint(0, 9)
    index3 = randint(0, 9)

    # getting first picture info
    name1 = image_info[index1]['id']
    title1 = image_info[index1]['title']

    # select another picture if this picture matches another one that
    # is already rendered
    while index2 == index1 or index2 == index3:
        index2 = randint(0, 9)

    # getting second picture info
    name2 = image_info[index2]['id']
    title2 = image_info[index2]['title']

    # select another picture if this picture matches another one that
    # is already rendered
    while index3 == index1 or index3 == index2:
        index3 = randint(0, 9)

    # getting third picture info
    name3 = image_info[index3]['id']
    title3 = image_info[index3]['title']

    return render_template('landing.html', name1=name1 + ".jpg", name2=name2 + ".jpg", name3=name3 + ".jpg",
                           title1=title1, title2=title2, title3=title3, index1=index1, index2=index2, index3=index3)


@app.route('/image/<index>')
def show_image(index):
    index = int(index)
    # get image info
    name = image_info[index]['id']
    title = image_info[index]['title']
    # get metadata
    im = Image.open('static/' + name + '.jpg')
    mode = im.mode
    format = im.format
    width = im.width
    height = im.height
    # cleanup
    im.close()
    # render
    return render_template('imagepage.html', name=name + ".jpg", title=title,
                            mode=mode, format=format, width=width, height=height)


if __name__ == '__main__':
    app.run(debug=True)
