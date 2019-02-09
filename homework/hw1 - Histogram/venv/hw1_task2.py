import hw1_hist_plotter as hp
import pickle

"""
File: hw1_task2.py
Contributors: Jesus A. Bernal Lopez - jebernal@csumb.edu
              Ashleigh Adams - asadams@csumb.edu
Last Modified: Feb 08, 2019
Due Date: Feb 11, 2019
Description: Takes in a list of list and returns a list of each rgb value in 
the list of list then returns each rgb list as an individual svg file
"""


def task2(the_list):
    """
    Takes in a list of list and returns a list of each rgb value in the list of list
    """
    red = []
    green = []
    blue = []
    for value in the_list:
        for the_tuple in value:
            red.append(the_tuple[0])
            green.append(the_tuple[1])
            blue.append(the_tuple[2])
    return [red, green, blue]


def main():
    my_pickle = open('image_matrix.dms', 'rb')
    data = pickle.load(my_pickle)
    my_pickle.close()

    hp.hist_plotter(task2(data))


if __name__ == '__main__':
    main()
