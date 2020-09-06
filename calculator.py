print('Python code starting...')

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,\
    QMessageBox
from PyQt5.QtCore import Qt

def dialog():
    mbox = QMessageBox()
    
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a fucking idiot")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle('calculator')

    label = QLabel(w)
    label.setText("Hello")
    #label.setAlignment(Qt.AlignCenter)
    label.move(110, 130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110, 150)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    app.exec_()
