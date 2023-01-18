import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import pyqtSlot

import game

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: orange")
        self.title = 'Time Waster'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 300
        self.initUI()
        
    
    def initUI(self):
        
        self.label_1 = QLabel("You want to waste some time??", self)
        self.label_1.resize(200,60)
        self.label_1.setFont(QFont('Times', 13))
        self.label_1.move(150, 60)
        
        self.label_1 = QLabel("GO click that button", self)
        self.label_1.resize(200,60)
        self.label_1.setFont(QFont('Times', 15))
        self.label_1.move(170, 100)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create a button in the window
        self.button = QPushButton(f"CLICK", self)
        self.button.resize(200,60)
        self.button.move(150,160)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    @pyqtSlot()
    def on_click(self):
        score = game.start()
        score = round(score)
        QMessageBox.question(self, '',f"You just wasted {score} seconds of your life :) ", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
