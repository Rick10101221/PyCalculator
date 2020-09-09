import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets

class Window(QMainWindow):

    def __init__(self):
        super(Window , self).__init__()
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('This is the Title, bitch')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My first label!')
        self.label.move(50,50)
        
        #createButtons(self, buttonNumber, buttonText)
        #self.button = QtWidgets.QPushButton(self)
        #self.button.setText("Click Me")
        #self.button.move(100,100)
        #self.button.clicked.connect(self.clicked)
    
    def createButtons(self, buttonNumber, buttonText):
        d = {}
        for _ in range(buttonNumber):
            d[f"button{_}"] = QtWidgets.QPushButton(self)

        i = 0   
        for key in d.keys():
            self.key = d[key]
            self.key.setText(buttonText)
            self.key.move(100, i * 100)
            self.key.clicked.connect(self.clicked)
            i = i + 1

    def clicked(self):
        self.label.setText('changed')
        self.update()

    def update(self):
        self.label.adjustSize()
        self.label.move(50,59)
          

def main():
    buttonNumber, buttonText = 3, 'Click Me'
    app = QApplication(sys.argv)
    win = Window()
    win.createButtons(buttonNumber, buttonText)
    win.show()
    sys.exit(app.exec_())

main()

print("SAD :(")