from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from text import *
from space_answer import *

class Answers():
    def __init__(self, answ1, answ2, answ3, answ4, answ5, answ6):
        self.answ1 = answ1
        self.answ2 = answ2
        self.answ3 = answ3
        self.answ4 = answ4
        self.answ5 = answ5
        self.answ6 = answ6

class SpaceQuest(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle("space_text")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.q1_txt = QLabel(q1)
        self.q2_txt = QLabel(q2)
        self.q3_txt = QLabel(q3)
        self.q4_txt = QLabel(q4)
        self.q5_txt = QLabel(q5)
        self.q6_txt = QLabel(q6)

        self.l_q1 = QLineEdit(answer_txt)
        self.l_q2 = QLineEdit(answer_txt)
        self.l_q3 = QLineEdit(answer_txt)
        self.l_q4 = QLineEdit(answer_txt)
        self.l_q5 = QLineEdit(answer_txt)
        self.l_q6 = QLineEdit(answer_txt)

        self.check_button = QPushButton(check_text)

        self.l_v = QVBoxLayout()

        self.l_v.addWidget(self.q1_txt, alignment = Qt.AlignTop | Qt.AlignLeft)
        self.l_v.addWidget(self.l_q1, alignment = Qt.AlignTop | Qt.AlignCenter)
        self.l_v.addWidget(self.q2_txt, alignment = Qt.AlignTop | Qt.AlignLeft)
        self.l_v.addWidget(self.l_q2, alignment = Qt.AlignTop | Qt.AlignCenter)
        self.l_v.addWidget(self.q3_txt, alignment = Qt.AlignTop  | Qt.AlignLeft)
        self.l_v.addWidget(self.l_q3, alignment = Qt.AlignTop | Qt.AlignCenter)
        self.l_v.addWidget(self.q4_txt, alignment = Qt.AlignTop  | Qt.AlignLeft)
        self.l_v.addWidget(self.l_q4, alignment = Qt.AlignTop | Qt.AlignCenter)
        self.l_v.addWidget(self.q5_txt, alignment = Qt.AlignTop  | Qt.AlignLeft)
        self.l_v.addWidget(self.l_q5, alignment = Qt.AlignTop | Qt.AlignCenter)
        self.l_v.addWidget(self.q6_txt, alignment = Qt.AlignTop  | Qt.AlignLeft)
        self.l_v.addWidget(self.l_q6, alignment = Qt.AlignTop | Qt.AlignCenter)
        self.l_v.addWidget(self.check_button, alignment = Qt.AlignTop | Qt.AlignCenter)

        self.setLayout(self.l_v)

    def check_click(self):
        self.hide()
        self.answ = Answers(self.l_q1.text(), self.l_q2.text(), self.l_q3.text(), self.l_q4.text(), self.l_q5.text(), self.l_q6.text())
        self.check_win = SpaceCheck(self.answ)

    def connects(self):
        self.check_button.clicked.connect(self.check_click)
    

    
