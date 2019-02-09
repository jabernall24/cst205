import pickle

"""
File: hw1_task1.py
Contributors: Jesus A. Bernal Lopez - jebernal@csumb.edu
              Ashleigh Adams - asadams@csumb.edu
Last Modified: Feb 08, 2019
Due Date: Feb 11, 2019
Description: Read in a file using pickle and sending that list to task1 function and 
printing out a dictionary of rgb with their respective bins.
"""


image = [
    [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
    [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
    [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
    [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
]


def task1(the_list):
    """
    Takes in a list and returns a dictionary representing the bin count for each color
    """

    color_task = {
        'red': [0, 0, 0, 0],
        'green': [0, 0, 0, 0],
        'blue': [0, 0, 0, 0]
    }

    for pixel in the_list:
        for rgb in pixel:
            color_task['red'][too_many_numbers(rgb[0])] += 1
            color_task['green'][too_many_numbers(rgb[1])] += 1
            color_task['blue'][too_many_numbers(rgb[2])] += 1
    print(color_task)


def too_many_numbers(val):
    """
    Takes in a number and returns it's bin index
    """
    if (val >= 0) and (val <= 63):
        return 0
    elif(val >= 64) and (val <= 127):
        return 1
    elif (val >= 128) and (val <= 191):
        return 2
    elif (val >= 192) and (val <= 255):
        return 3


def main():
    my_pickle = open('image_matrix.dms', 'rb')
    data = pickle.load(my_pickle)
    my_pickle.close()
    task1(data)


if __name__ == '__main__':
    main()
