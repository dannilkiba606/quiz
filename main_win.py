from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from space_quest import *
from text import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(main_text)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):

        self.question_mark1, self.question_mark2 = QLabel("?"), QLabel("?")
        self.question_mark1.setStyleSheet("color : red")
        self.question_mark2.setStyleSheet("color : red")
        self.question_mark1.setFont(QFont(font1, font_size + 10))
        self.question_mark2.setFont(QFont(font1, font_size + 10))

        self.main_txt = QLabel(main_text)
        self.main_txt.setFont(QFont(font1, main_font_size))

        self.welcome_txt = QLabel(welcome_text)
        self.welcome_txt.setFont(QFont(font1, font_size, QFont.StyleItalic))

        self.topics_txt = QLabel(vic_topics)
        self.topics_txt.setFont(QFont(font1, font_size + 5, QFont.Bold))
        self.topics_txt.setStyleSheet("color : rgb(255,140,0);")

        self.rules_button = QPushButton(rules_text)
        self.rules_button.setFont(QFont(font1, font_size + 2))

        self.space_button = QPushButton(space_text)
        self.space_button.setStyleSheet("color : rgb(255, 0, 255);"
                                        "background-image : url(space_image.png);")
        self.space_button.setFont(QFont(font1, font_size + 5))

        self.h_line = QHBoxLayout()
        self.v1_line = QVBoxLayout()
        self.v2_line = QVBoxLayout()
        self.v3_line = QVBoxLayout()

        self.v2_line.addWidget(self.main_txt, alignment = Qt.AlignCenter | Qt.AlignTop)
        self.v1_line.addWidget(self.question_mark1, alignment = Qt.AlignTop | Qt.AlignLeft)
        self.v3_line.addWidget(self.question_mark2, alignment = Qt.AlignTop | Qt.AlignRight)
        self.v3_line.addWidget(self.rules_button, alignment = Qt.AlignCenter | Qt.AlignBottom)
        self.v2_line.addWidget(self.welcome_txt, alignment = Qt.AlignCenter | Qt.AlignTop)
        self.v2_line.addWidget(self.topics_txt, alignment = Qt.AlignTop)
        self.v2_line.addWidget(self.space_button, alignment = Qt.AlignCenter | Qt.AlignTop)

        self.h_line.addLayout(self.v1_line)
        self.h_line.addLayout(self.v2_line)
        self.h_line.addLayout(self.v3_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.space_button.clicked.connect(self.space_click)
        self.rules_button.clicked.connect(self.rules_click)

    def space_click(self):
        self.hide()
        self.space_win = SpaceQuest()

    def rules_click(self):
        self.rules_box = QMessageBox()
        self.rules_box.setIcon(QMessageBox.Information)
        self.rules_box.setWindowTitle(rules_text)
        self.rules_box.setText(rules)
        self.rules_box.exec_()

app = QApplication([])
main_win = MainWin()
app.exec_()


    
        