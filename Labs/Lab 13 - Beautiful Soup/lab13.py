"""
Name: Jesus Andres Bernal Lopez, Michael Avalos-Garcia, Paul Whipp
File: lab13.py
Date: 03/25/2019
Description: In this lab we scraped the first image from pixabay website and then showed the image
"""

import requests
from bs4 import BeautifulSoup as bs4
from PIL import Image

# get the content of website
website = requests.get('https://pixabay.com/').text

# parse the content of website to html
html = bs4(website, "html.parser")

# get the url of the image
img_url = html.find('img')['src']

# store image in variable then show it
img = Image.open(requests.get(img_url, stream=True).raw)
img.show()

