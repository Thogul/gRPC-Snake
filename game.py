import random
import sys

from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QFormLayout, QPushButton, QLineEdit, QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 788)
        MainWindow.setStyleSheet("background: rgb(170, 255, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.board = QtWidgets.QFrame(self.centralwidget)
        self.board.setGeometry(QtCore.QRect(0, 0, 1021, 741))
        self.board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.board.setObjectName("board")
        self.scoreboard = QtWidgets.QTextBrowser(self.board)
        self.scoreboard.setEnabled(True)
        self.scoreboard.setGeometry(QtCore.QRect(825, 10, 171, 241))
        self.scoreboard.setAutoFillBackground(False)
        self.scoreboard.setStyleSheet("background: rgb(247, 247, 247, .5);\n"
"")
        self.scoreboard.setObjectName("scoreboard")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 26))
        self.menubar.setStyleSheet("background: rgb(238, 238, 238)")
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background: rgb(240, 240, 240)")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Snok"))
        self.scoreboard.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))


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
    deleteWid.close()
    #deleteWid.setParent(None)
    deleteWid.deleteLater()
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    lg = LogIn()
    lg.setAttribute(Qt.WA_DeleteOnClose)
    sys.exit(app.exec_())
    
    
   


if __name__ == '__main__':
    main()
