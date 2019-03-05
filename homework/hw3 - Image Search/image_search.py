#! /usr/bin/env python3

"""
Contributors: Jesus A. Bernal Lopez
              Michael Avalos-Garcia
              Paul Whipp
File: image_search.py
Due Date: March 11, 2019
Description:
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QComboBox, QPushButton, \
    QVBoxLayout, QLabel, QDial
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtCore import pyqtSlot
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        combo_items = ["Select One", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

        # layouts
        hbox = QHBoxLayout()
        sepia_hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        # window items
        self.line_edit = QLineEdit()
        self.img_manip = QComboBox()
        self.img_manip.addItems(combo_items)
        self.img_manip.currentTextChanged.connect(self.hide_show_manip)
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_clicked)
        self.image_label = QLabel(self)

        self.r_spin_dial = QDial()
        self.r_spin_dial.setNotchesVisible(True)
        self.r_spin_dial.setMaximum(10)
        self.r_spin_dial.sliderReleased.connect(self.update_label)
        self.r_sepia_label = QLabel("Red: ")
        self.r_spin_dial.hide()
        self.r_sepia_label.hide()

        self.g_spin_dial = QDial()
        self.g_spin_dial.setNotchesVisible(True)
        self.g_spin_dial.setMaximum(10)
        self.g_spin_dial.sliderReleased.connect(self.update_label)
        self.g_sepia_label = QLabel("Green: ")
        self.g_spin_dial.hide()
        self.g_sepia_label.hide()

        self.b_spin_dial = QDial()
        self.b_spin_dial.setNotchesVisible(True)
        self.b_spin_dial.setMaximum(10)
        self.b_spin_dial.sliderReleased.connect(self.update_label)
        self.b_sepia_label = QLabel("Blue: ")
        self.b_spin_dial.hide()
        self.b_sepia_label.hide()

        # add items to layouts
        hbox.addWidget(self.line_edit)
        hbox.addWidget(self.img_manip)
        hbox.addWidget(search_btn)
        vbox.addLayout(hbox)
        sepia_hbox.addWidget(self.r_spin_dial)
        sepia_hbox.addWidget(self.r_sepia_label)
        sepia_hbox.addWidget(self.g_spin_dial)
        sepia_hbox.addWidget(self.g_sepia_label)
        sepia_hbox.addWidget(self.b_spin_dial)
        sepia_hbox.addWidget(self.b_sepia_label)
        vbox.addLayout(sepia_hbox)
        vbox.addWidget(self.image_label)

        self.setLayout(vbox)
        self.show()

    @pyqtSlot()
    def hide_show_manip(self):
        """Hides and shows the spin dial box and respective labels as needed"""
        if self.img_manip.currentText() == "Sepia":
            self.r_spin_dial.show()
            self.r_sepia_label.show()
            self.g_spin_dial.show()
            self.g_sepia_label.show()
            self.b_spin_dial.show()
            self.b_sepia_label.show()
        else:
            self.r_spin_dial.hide()
            self.r_sepia_label.hide()
            self.g_spin_dial.hide()
            self.g_sepia_label.hide()
            self.b_spin_dial.hide()
            self.b_sepia_label.hide()

    @pyqtSlot()
    def update_label(self):
        """update spin box value to be shown in their respective label"""
        self.r_sepia_label.setText(f'Red: {round(self.r_spin_dial.value() * 0.1, 1)}')
        self.g_sepia_label.setText(f'Green: {round(self.g_spin_dial.value() * 0.1, 1)}')
        self.b_sepia_label.setText(f'Blue: {round(self.b_spin_dial.value() * 0.1, 1)}')

    @pyqtSlot()
    def search_clicked(self):
        """When user searches for image, it displays it on the window"""
        # when user searches for image it sends of the work to other functions then comes back to show the image
        width, height = self.manipulate_image(self.search_image(self.line_edit.text()), self.img_manip.currentText())
        pm = QPixmap('show.jpg')
        pixmap = pm.scaled(width, height)
        if (width is not 0) and (height is not 0):
            self.image_label.setPixmap(pixmap)
            self.image_label.adjustSize()

    def search_image(self, img):
        """Takes in a string and searches for the image that matches an image in the list the most"""
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
                "flickr_user": "Mónica Pinheiro",
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

        # puts title and tags of the dictionaries into a list of list
        key_words = map(lambda x: x['title'].lower().split() + [y.lower() for y in x['tags']], image_info)
        img = img.lower().split()
        most_val = 0
        most_index = []

        # gets the index(indexes) with the most matches
        for i, word in enumerate(key_words):
            val = sum(x in word for x in img)
            if val > most_val:
                most_val = val
                most_index.clear()
                most_index.append(i)
            elif val == most_val:
                most_index.append(i)

        if len(most_index) == 1:
            return f"images/{image_info[most_index[0]]['id']}.jpg"
        else:
            # puts title and index in a tuple, adds them to a list, sorts the list making the 0th index the one we
            # choose
            most_matches = []
            for x in most_index:
                tup = (image_info[x]['title'], x)
                most_matches.append(tup)

            most_matches.sort()
            return f"images/{image_info[most_matches[0][1]]['id']}.jpg"

    def manipulate_image(self, img, manip):
        """Takes image and form of manipulation and sends it to the correct function to manipulate"""
        image = Image.open(img)
        if manip == 'Sepia':
            self.sepia(image)
        elif manip == 'Negative':
            self.negative(image)
        elif manip == 'Grayscale':
            self.grayscale(image)
        elif manip == 'Thumbnail':
            self.none(image)
            return image.width / 2, image.height / 2
        elif manip == 'None':
            self.none(image)
        else:
            self.image_label.setText('You must select an option')
            self.image_label.adjustSize()
            return 0, 0
        return image.width, image.height

    def sepia(self, img):
        """Takes users values from the spin box and does Sepia to them"""
        r, g, b = self.r_spin_dial.value() * 0.1, self.g_spin_dial.value() * 0.1, self.b_spin_dial.value() * 0.1
        new_list = map(lambda x: (int(x[0] * r), int(x[1] * g), int(x[2] * b)), img.getdata())
        img.putdata(list(new_list))
        img.save('show.jpg')

    def negative(self, img):
        """Takes an image, converts it to negative and then saves it"""
        new_list = map(lambda x: (255 - x[0], 255 - x[1], 255 - x[2]), img.getdata())
        img.putdata(list(new_list))
        img.save('show.jpg')

    def grayscale(self, img):
        """Takes an image, converts it to a grayscale image and then saves it"""
        new_list = map(lambda x: (int((x[0] * 0.299 + x[1] * 0.587 + x[2] * 0.114) / 3),) * 3, img.getdata())
        img.putdata(list(new_list))
        img.save('show.jpg')

    def none(self, img):
        """Takes an image and saves it"""
        img.save('show.jpg')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
