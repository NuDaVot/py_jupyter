from tqdm.auto import tqdm, trange

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys
from PyQt6 import QtCore
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QCursor, QRegularExpressionValidator
from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QGridLayout, QPushButton
WINDOW_SIZE = 235
from PyQt6.QtCore import Qt
DISPLAY_HEIGHT = int(35)

class MainWindow(QMainWindow):
    # def __init__(self):
    #     super().__init__()
    #
    #     self.setWindowTitle("Test 2")
    #     self.geometry = self.setGeometry(200, 100, 500, 450)
    #     button = QPushButton("click me")
    #     # button.width(100)
    #     button.clicked.connect(self.the_window_title_changed)
    #
    #     self.setCentralWidget(button)
    #
    # def the_window_title_changed(self, window_title):
    #     print("Window title changed: %s" % window_title)
    #     self.setWindowTitle("2")
    #     if window_title == 'Something went wrong':
    #         self.button.setDisabled(True)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Calculator")
        self.setBaseSize(WINDOW_SIZE, WINDOW_SIZE)
        self.__generalLayout = QVBoxLayout()

        centralWidget = QWidget()
        centralWidget.setLayout(self.__generalLayout)
        self.setCentralWidget(centralWidget)

        self.__create_display()
        self.__create_button()

    def __create_display(self):
        self.__display = QLineEdit()
        self.__display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.__display.setReadOnly(True)

        self.__generalLayout.addWidget(self.__display)

    def __create_button(self):
        list_buttons = []
        list_keyboard = [["7", "8", "9", "/", "C"],
                         ["4", "5", "6", "*", "("],
                         ["1", "2", "3", "-", ")"],
                         ["0", "00", ".", "+", "="]]

        button_layout = QGridLayout()

        row = 0
        col = 0

        for list_row in list_keyboard:
            for column in list_row:
                key_text = column
                key = QPushButton(key_text)
                key.clicked.connect(self.clik_button)
                button_layout.addWidget(key, row, col)
                list_buttons.append(key)

                col = col + 1
            row = row + 1
            col = 0
        self.__generalLayout.addLayout(button_layout)

    def clik_button(self):
        self.__display.setText()
    # def show(self):
    #     self.show()


def main_window():
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.setWindowTitle("test 3")
    window.show()

    app.exec()


def print_hi(name):
    print(f'Hi, {name}')

def look_process_bar(n):
    sum = 0
    for i in tqdm(range(n)):
        sum +=i
    return sum


if __name__ == '__main__':
    main_window()

