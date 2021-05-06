import random
import sys

from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QFormLayout, QPushButton, QLineEdit, QColorDialog


class Snok(QMainWindow):

    def __init__(self):
        super().__init__()

        self.GUI()

    def GUI(self):

        self.gameBoard = Board(self)
        self.setCentralWidget(self.gameBoard)

        self.msgBar = self.statusBar()
        self.gameBoard.msgScoreBar[str].connect(self.msgBar.showMessage)

        self.msgBar.showMessage("Hello")

        

        self.setGeometry(100, 100, 1000, 800)
        self.setStyleSheet("background: lightgreen;")
        self.msgBar.setStyleSheet("background: #CD96CD;")
        self.gameBoard.setStyleSheet("border: 10px dotted black;")

    

        #Center
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))
    
        self.setWindowTitle('Snok')
        self.show()

class Board(QFrame):

    msgScoreBar = pyqtSignal(str)
    Speed = 80

    def __init__(self, parent):
        super().__init__(parent)

        self.boardGUI()

    def boardGUI(self):
        

        self.timer = QBasicTimer()
        self.timer.start(Board.Speed, self)
        self.msgScoreBar.emit("Hello")
        self.direction = 1

    

    def keyPressEvent(self, event):

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key_Left:
            if self.direction != 2:
                self.direction = 1
        elif key == Qt.Key_Right:
            if self.direction != 1:
                self.direction = 2
        elif key == Qt.Key_Down:
            if self.direction != 4:
                self.direction = 3
        elif key == Qt.Key_Up:
            if self.direction != 3:
                self.direction = 4
        
        


        else:
            super(Board, self).keyPressEvent(event)
    
class LogIn(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Choose your player")
        layout = QFormLayout()
        layout.addRow('Enter your Nickname: ', QLineEdit())
        layout.addRow('Choose your color: ', QColorDialog())
        btn = QPushButton('Enter Game!')
        btn.clicked.connect(onClicked)
        layout.addWidget(btn)
        self.setLayout(layout)
        self.show()

def onClicked(self):
    deleteWid = LogIn()
    #deleteWid.close()
    #deleteWid.setParent(None)
    deleteWid.deleteLater()
def main():

    app = QApplication([])
    lg = LogIn()
    lg.setAttribute(Qt.WA_DeleteOnClose)
    #snok = Snok()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
