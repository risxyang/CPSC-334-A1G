import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel, QLineEdit,
                             QHBoxLayout, QVBoxLayout)

class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Resize This Window")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.setWindowTitle("Resize This Window")

        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("START", self)
        self.pushButton.resize(200,50)
        self.pushButton.move(220, 300)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")

        self.pushButton.clicked.connect(self.window2)              # <===

        #NEW CODE
        self.lineEntry1 = QLineEdit(self) #Projector number textbox
        self.lineEntry1.move(285, 150)
        self.lineEntry1.resize(100,20)
        number = lineEntry1.text()

        self.lineEntry2 = QLineEdit(self) #Orientation textbox
        self.lineEntry2.move(285, 200)
        self.lineEntry2.resize(100,20)

        self.pushButton = QPushButton() 
        self.pushButton.setObjectName("set") 
        self.pushButton.resize(100,50)
        self.pushButton.move(430, 160)
        self.pushButton.clicked.connect(self.button_clicked)

        self.main_window()

    def main_window(self):
        self.label = QLabel("Input Projector Number:", self)
        self.label.resize(300,20)
        self.label.move(120, 150)

        self.label = QLabel("Input Orientation:", self)
        self.label.resize(300,20)
        self.label.move(120, 200)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        #self.hide()

    #def print_LineEdit(self, text):
        #line = lineEntry1.text()
        #print(text)

    def button_clicked(self):
        value = self.lineEntry1.text()
        print(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())