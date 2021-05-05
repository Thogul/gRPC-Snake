import random
import sys

from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication

class Snok(QMainWindow):

    def __init__(self):
        super().__init__()

        self.GUI()

    def GUI(self):

        self.gameBoard = Board(self)
        #self.setCentralWidget(self.gameBoard)

        self.msgBar = self.statusBar()
        self.gameBoard.msgScoreBar[str].connect(self.msgBar.showMessage)

        self.msgBar.showMessage("Hello")

        

        self.setGeometry(100, 100, 1000, 800)

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
    




def main():

    app = QApplication([])
    snok = Snok()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
