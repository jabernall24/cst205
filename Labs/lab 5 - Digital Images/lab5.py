"""
File: lab5.py
Contributors: Jesus A. Bernal Lopez - jebernal@csumb.edu
              Sat in front of mirror: zepoL lanreB .A suseJ - ude.bmusc@lanrebej
Description: opened up a file, then put the numbers onto a list, created an image from the list then showed it.
Last Modified: 02/09/2019
Due Date: 02/11/2019
"""

from PIL import Image

# opened sample file
fin = open('sample', 'r')

# from stackoverflow:
# https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python

# traversed throught the file and took away unnessary space and semicolon, took in the integers and added them to a list of int
mona = [int(x) for x in fin.read().replace(';', '').replace('\n', ' ').split(' ')]

# closed the file
fin.close()

# changed list of int's to raw data
mona = Image.frombytes('L', (18,29), bytes(mona))


mona.show()


# 18, 29 came from their being 19 columns and 29 rows in the data

"""
Summary: 
Overall it was not difficult, however I did have to look up how to change a str to an int while reading from
a file all in one swoop
"""
