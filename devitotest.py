import sys
import csv
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel, QLineEdit,
                             QHBoxLayout, QVBoxLayout)

class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.installEventFilter(self)
        self.setWindowTitle("Resize This Window")

        #labels
        self.label1 = QLabel("Top-Left Corner", self)
        self.label1.move(50, 50)
        self.label2 = QLabel("(~~~ : ~~~)", self)
        self.label2.move(150, 50)
        self.label3 = QLabel("Bottom-Right\n Corner", self)
        self.label3.move(50, 100)
        self.label4 = QLabel("(~~~ : ~~~)", self)
        self.label4.move(150, 100)
        self.label5 = QLabel("Resolution: ", self)
        self.label5.move(50, 150)
        self.label6 = QLabel("(~~~ x ~~~)", self)
        self.label6.move(150, 150)
    
        self.label = QLabel("^Up on Desktop^", self)
        self.pushButton = QPushButton("<", self)
        self.pushButton.resize(200,50)
        self.pushButton.clicked.connect(self.left_up)

        self.pushButton.move(0, 0)
        self.pushButton = QPushButton(">", self)
        self.pushButton.clicked.connect(self.right_up)

        self.pushButton.resize(200,50)
        self.pushButton.move(0, 50)
        self.pushButton = QPushButton("^", self)
        self.pushButton.clicked.connect(self.up_up)

        self.pushButton.resize(0,100)
        self.pushButton = QPushButton("V", self)
        self.pushButton.resize(0,150)
        self.pushButton.clicked.connect(self.down_up)

    def right_up(self):
        print("Desktop-Right is Projector-Space-Up")

    def left_up(self):
        print("Desktop-Left is Projector-Space-Up")

    def up_up(self):
        print("Desktop-Up is Projector-Space-Up")

    def down_up(self):
        print("Desktop-Down is Projector-Space-Up")

    def eventFilter(self, obj, event):
        if event.type() in {QtCore.QEvent.Resize, QtCore.QEvent.Move}:
            #Store useful variables
            width = self.frameGeometry().width()
            height = self.frameGeometry().height()
            p = self.mapToGlobal(QtCore.QPoint(0, 0))
            q = self.mapToGlobal(QtCore.QPoint(width, height))

            #Refresh Labels
            self.label2.setText((str(p)[19:]))
            self.label4.setText((str(q)[19:]))
            self.label6.setText(str(width) + " x " + str(height))
        return super().eventFilter(obj, event)   


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.setWindowTitle("Resize This Window")

        c = csv.writer(output)
        c.writerow(['Monitor', 'Projector', 'Orientation', 'Resolution'
            'Top Left Coordinate', 'Bottom Right Coordinate'])
        monitors = ['1A', '1B', '1C', '2A', '2B', '2C']
        for monitor in monitors:
            c.writerow([monitor])


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

        self.lineEntry2 = QLineEdit(self) #Orientation textbox
        self.lineEntry2.move(285, 200)
        self.lineEntry2.resize(100,20)

        self.pushButton = QPushButton("Set", self) 
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
        projector = self.lineEntry1.text()
        orientation = self.lineEntry2.text()
        print(projector + ", " + orientation)

        #monitors = ['1A', '1B', '1C', '2A', '2B', '2C']

        #output = open('output.csv', 'w')
        #c = csv.writer(output)
        #c.writerow(monitors[currentRow], projector, orientation, 0, 0, 0)
        #currentRow = currentRow + 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    output = open('output.csv', 'w')
    window = Window()
    sys.exit(app.exec())
