from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from text import *

class SpaceCheck(QWidget):
    def __init__(self, answ):
        super().__init__()
        self.answ = answ

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(answers_text)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def Check_result(self):
        self.result = 0
        if self.answ.answ1 == answer1:
            self.result += 1
        if self.answ.answ2 == answer2:
            self.result += 1
        if self.answ.answ3 == answer3:
            self.result += 1
        if self.answ.answ4 == answer4:
            self.result += 1
        if self.answ.answ5 == answer5:
            self.result += 1
        if self.answ.answ6 == answer6:
            self.result += 1
        return self.result


    def initUI(self):
        self.check1_txt = QLabel(check + str(self.Check_result()) + '/6')
        self.check1_txt.setStyleSheet("color : rgb(62, 0, 167);")
        self.check1_txt.setFont(QFont(font1, font_size + 6))

        if self.Check_result() >= 5:
            self.check2_txt = QLabel(illation1)
        elif self.Check_result() >= 3:
            self.check2_txt = QLabel(illation2)
        else:
            self.check2_txt = QLabel(illation3)
        self.check2_txt.setStyleSheet("color : rgb(62, 0, 167);")
        self.check2_txt.setFont(QFont(font1, font_size + 4))

        self.answers_button = QPushButton(answers_text)
        self.main_button = QPushButton(menu_text)

        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.check1_txt, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.check2_txt, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.answers_button, alignment = Qt.AlignBottom | Qt.AlignLeft)

        self.setLayout(self.v_line)

    def answers_click(self):
        self.answers_box = QMessageBox()
        self.answers_box.setWindowTitle(answers_text)
        self.answers_box.setIcon(QMessageBox.Information)
        self.answers_box.setText(all_answers)
        self.answers_box.resize(win_width - 300, win_height - 500)
        self.answers_box.exec_()

    def connects(self):
        self.answers_button.clicked.connect(self.answers_click)



         