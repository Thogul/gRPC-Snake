import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog, QColorDialog



class Mainwindow(QMainWindow):

    def __init__(self, name):#, color):
        super().__init__()

        self.name = name
        #self.color = color

        self.setupUi(self)




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
        self.scoreboard.setEnabled(False)
        self.scoreboard.setGeometry(QtCore.QRect(825, 10, 171, 241))
        self.scoreboard.setStyleSheet("background: rgb(247, 247, 247, .5)")
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
        self.login = LoginDialog()
        MainWindow.setWindowTitle(_translate("MainWindow", "Snok"))
        self.scoreboard.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.statusbar.showMessage(_translate("statusbar", self.name))
        #self.statusbar.showMessage(_translate("statusbar", self.color))



class LoginDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 200)
        Dialog.setStyleSheet("background: rgb(172, 172, 172)")
        self.userLabel = QtWidgets.QLabel(Dialog)
        self.userLabel.setGeometry(QtCore.QRect(10,20, 241, 22))
        self.userLabel.setObjectName("enter_nickname")
        self.pick = QtWidgets.QLabel(Dialog)
        self.pick.setGeometry(QtCore.QRect(10,50, 241, 22))
        self.pick.setObjectName("pick_color")
        self.userName = QtWidgets.QLineEdit(Dialog)
        self.userName.setGeometry(QtCore.QRect(125, 20, 241, 22))
        self.userName.setObjectName("userName")
        self.userName.setStyleSheet("background: rgb(255, 255, 255)")
        self.enterGame = QtWidgets.QPushButton(Dialog)
        self.enterGame.setGeometry(QtCore.QRect(170, 125, 175, 50))
        self.enterGame.setObjectName("enterGame")
        self.enterGame.clicked.connect(self.enter_game)
        self.enterGame.setStyleSheet("background: rgb(130, 255, 127)")
        self.pickcolor = QtWidgets.QPushButton(Dialog)
        self.pickcolor.setGeometry(QtCore.QRect(125, 50, 241, 28))
        self.pickcolor.setObjectName("pickcolor")
        self.pickcolor.setStyleSheet("background: rgb(255, 255, 255)")
        self.pickcolor.clicked.connect(self.colorDialog)
        self.framecolor = QtWidgets.QFrame(Dialog)
        self.framecolor.setGeometry(QtCore.QRect(390, 30, 100, 75))
        color = QtGui.QColor(0, 0, 255)
        self.framecolor.setStyleSheet("QWidget { background-color: %s}" %color.name())
      
    

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def colorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.framecolor.setStyleSheet("QWidget { background-color: %s}" %color.name())
    
    def enter_game(self):
        user = self.userName.text()
        #color = self.
        self.main = Mainwindow(user)# color)  
        self.main.show()
        self.hide()
    
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Get ready to play Snok!"))

        self.enterGame.setText(_translate("Dialog", "Enter Game"))
        self.enterGame.setText(_translate("Dialog", "Enter Game"))
        self.pickcolor.setText(_translate("Dialog", "Pick Color"))
        self.userLabel.setText(_translate("Dialog", "Enter nickname: "))
        self.pick.setText(_translate("Dialog", "Choose your color: "))


    

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    login = LoginDialog()
    login.show()
    sys.exit(app.exec_())
    
    


if __name__ == '__main__':
    main()
