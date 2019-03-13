"""
Contributers: Jesus Andres Bernal Lopez, Paul Whipp, Michael Avalos-Garcia
File: lab12.py
Date: 03/13/2019
Description:
"""

import requests
from dotenv import load_dotenv
import os
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSlot
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clash Royale Chest Cycle")

        vbox = QVBoxLayout()

        label = QLabel("Enter your player tag(without the #)")
        self.user_input = QLineEdit()
        self.my_button = QPushButton("Get Chest Cycle")
        self.my_button.clicked.connect(self.button_clicked)
        self.chest_label = QLabel()
        self.chest_label.isHidden()

        vbox.addWidget(label)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.my_button)
        vbox.addWidget(self.chest_label)

        self.setLayout(vbox)

    @pyqtSlot()
    def button_clicked(self):
        url = f"https://api.royaleapi.com/player/{self.user_input.text().upper()}/chests"

        headers = {
            'auth': my_key
        }

        response = requests.request("GET", url, headers=headers)

        data = response.json()
        self.chest_label.setText(f"""
        Mega Lightning: {data['megaLightning']}\n
        Magical: {data['magical']}\n
        Legendary: {data['legendary']}\n
        Epic: {data['epic']}\n
        Giant: {data['giant']}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Window()
    main_win.show()
    # loads the .env file and stores the API Key in variable
    load_dotenv()
    my_key = os.getenv("API_KEY")
    sys.exit(app.exec_())
