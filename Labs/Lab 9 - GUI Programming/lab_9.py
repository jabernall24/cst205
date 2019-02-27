#! /usr/bin/env python3

from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
import sys

"""
Task 2
"""


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Michael Avalos-Garcia, Jesus Andres Bernal Lopez, Paul Whipp")
#         self.resize(500, 300)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     status = app.exec_()
#     sys.exit(status)


"""
Task 3
"""
# class Menu(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Title")
#
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)
#         lay = QVBoxLayout(self.central_widget)
#
#         label = QLabel(self)
#         pixmap1 = QPixmap('img/sanders.jpg')
#         self.pixmap = pixmap1.scaled(self.width(), self.height())
#         label.setPixmap(self.pixmap)
#         self.resize(self.pixmap.width(), self.pixmap.height())
#
#         lay.addWidget(label)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Menu()
#     sys.exit(app.exec_())

"""
Task 4
"""


class MainWindow(QWidget):
    """Expanding the QWidget class"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Michael Avalos-Garcia, Jesus Andres Bernal Lopez, Paul Whipp")
        self.resize(500, 300)

        vbox = QVBoxLayout()

        # Make 3 buttons and label
        self.michael_btn = QPushButton("Michael", self)
        self.michael_lbl = QLabel('Michael', self)
        self.michael_btn.clicked.connect(self.michael_clicked)

        self.jesus_btn = QPushButton("Jesus", self)
        self.jesus_lbl = QLabel('Jesus', self)
        self.jesus_btn.clicked.connect(self.jesus_clicked)

        self.paul_btn = QPushButton("Paul", self)
        self.paul_lbl = QLabel('Paul', self)
        self.paul_btn.clicked.connect(self.paul_clicked)

        # Add the buttons and labels to the layout
        vbox.addWidget(self.michael_btn)
        vbox.addWidget(self.michael_lbl)
        vbox.addWidget(self.jesus_btn)
        vbox.addWidget(self.jesus_lbl)
        vbox.addWidget(self.paul_btn)
        vbox.addWidget(self.paul_lbl)

        # Setting the layout to our created layout
        self.setLayout(vbox)

    @pyqtSlot()
    def michael_clicked(self):
        """Handles the action when this button is clicked"""
        self.__set_default__()
        self.michael_lbl.setText("You have clicked on Michael")

    @pyqtSlot()
    def jesus_clicked(self):
        """Handles the action when this button is clicked"""
        self.__set_default__()
        self.jesus_lbl.setText('You have clicked on Jesus')

    @pyqtSlot()
    def paul_clicked(self):
        """Handles the action when this button is clicked"""
        self.__set_default__()
        self.paul_lbl.setText('You have clicked on Paul')

    def __set_default__(self):
        """Updates the labels to their original message"""
        self.michael_lbl.setText('Michael')
        self.jesus_lbl.setText('Jesus')
        self.paul_lbl.setText('Paul')
        self.paul_lbl.adjustSize()
        self.jesus_lbl.adjustSize()
        self.michael_lbl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    status = app.exec_()
    sys.exit(status)
