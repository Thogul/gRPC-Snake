import random
import sys
import engine_revised
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog, QColorDialog
from PyQt5.QtCore import QBasicTimer 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtMultimedia import *
import random
import sys
from client import Client


selectedColor = QtGui.QColor(0, 0, 255)
userName = str

#score = str(engine.Snake().score)
gameover = False

class Mainwindow(QMainWindow):

    def __init__(self, name):
        super(Mainwindow, self).__init__()

        self.name = name

        self.setupUi(self)


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 750)
        #self.setGeometry(100, 100, 1050, 750)
        #MainWindow.setStyleSheet("background: rgb(170, 255, 127)")
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")


        self.board = Board(self)
        self.setCentralWidget(self.board)
        #self.board.setGeometry(QtCore.QRect(0, 0, 1021, 741))
  #self.board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.board.setObjectName("board")
        self.board.start()
        self.scoreboard = QtWidgets.QTextBrowser(self.board)
        self.scoreboard.setEnabled(False)
        self.scoreboard.setGeometry(QtCore.QRect(10, 10, 170, 241))
        self.scoreboard.setFont(QFont("Arial", 12))
        self.scoreboard.setStyleSheet("background: rgba(247, 247, 247, .5)")
        self.scoreboard.setObjectName("scoreboard")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background: rgb(240, 240, 240)")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.soundeffect = QSoundEffect(MainWindow)
        self.soundeffect.setSource(QUrl.fromLocalFile("gamemusic.wav"))
        self.soundeffect.setVolume(0.25)
        self.soundeffect.setObjectName("soundeffect")
        self.soundeffect.setLoopCount(100)
        self.radioButton = QtWidgets.QRadioButton(self.board)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setGeometry(QtCore.QRect(10, 650, 61, 20))
        self.radioButton.toggled.connect(lambda:self.btnstate(self.radioButton))
        self.radioButton.setChecked(False)
        
        
        self.label = QLabel(MainWindow)
        self.label.setObjectName("label")
        
        self.label.setGeometry(QRect(140, -47, 201, 200))
        self.label.setStyleSheet("font: 20pt \"8514oem\";")
        self.board.score[str].connect(self.label.setText)
        
       
       

        self.board.score[str].connect(self.statusbar.showMessage)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def btnstate(self, radioButton):
        if radioButton.isChecked() == True:
            self.soundeffect.play()
        else:
            self.soundeffect.stop()        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Snok"))
        self.scoreboard.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.statusbar.showMessage(_translate("statusbar", self.name))
        self.scoreboard.append(_translate("scoreboard", self.name + ' Score : '))
        self.radioButton.setText(_translate("MainWindow", "Music"))

class Ui_Form(QWidget):

    def __init__(self, parent):

        super(Ui_Form, self).__init__(parent)
        self.parent = parent

        self.setupUi(self)


    def setupUi(self, QWidget):

        QWidget.setObjectName("Widget")
        QWidget.resize(346, 268)
        QWidget.setGeometry(350,100,346,268)
        self.quitButton = QtWidgets.QPushButton(QWidget)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.setGeometry(QRect(50, 170, 93, 28))
        self.quitButton.setStyleSheet("background:rgb(255, 85, 0)")
        self.quitButton.clicked.connect(self.quitGame)
        self.playButton = QtWidgets.QPushButton(QWidget)
        self.playButton.setObjectName("playButton")
        self.playButton.setGeometry(QRect(200, 170, 93, 28))
        self.playButton.setStyleSheet("background:rgb(85, 170, 255)")
        self.playButton.clicked.connect(self.playAgian)
        self.quitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.playButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gameOver = QtWidgets.QLabel(QWidget)
        self.gameOver.setObjectName("gameOver")
        self.gameOver.setGeometry(QRect(120, 30, 111, 61))
        self.gameOver.setStyleSheet("font: 20pt \"8514oem\";")
        self.label = QtWidgets.QLabel(QWidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(80, 90, 201, 41))
        self.label.setStyleSheet("font: 20pt \"8514oem\";")
        

        self.retranslateUi(QWidget)

        QMetaObject.connectSlotsByName(QWidget)
    # setupUi

    def quitGame(self):
        QApplication.instance().quit()

    def playAgian(self):
        #borad = Board(Mainwindow)
        self.parent.engine = engine_revised.Engine()
        self.parent.client = Client(userName, self.parent.engine)
        self.parent.client.send_action("w")
        self.parent.start()
        self.close()
        

    

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate

        QWidget.setWindowTitle(_translate("Widget", "Game over!"))
        self.quitButton.setText(_translate("Widget", "Quit"))
        self.playButton.setText(_translate("Widget", "Play Again"))
        self.gameOver.setText(_translate("Widget", "GAME OVER"))
        self.label.setText(_translate("Widget", "Quit or play again?"))
    # retranslateUi

class Board(QFrame):
    
    score = pyqtSignal(str)
    def __init__(self, parent):
        super(Board, self).__init__(parent)

        
        self.WIDTHINBLOCKS = 105
        self.HEIGHTINBLOCKS = 75
        
        self.SPEED = 17
        self.parent = parent
        self.screen_width = int(self.parent.width())
        self.screen_height = int(self.parent.height())
        self.setFocusPolicy(Qt.StrongFocus)
  
     
        #self.engine = engine.Engine(self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        self.engine = engine_revised.Engine()
        self.client = Client(userName, self.engine)
        self.client.send_action("w")


        ##self.engine.generate_outer_walls(100,150)
        #self.items = self.engine.get_items_on_screen(self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        #self.items = self.engine.get_items_on_screen()
        self.timer = QBasicTimer()

        self.direction = "w"





        self.food = []

        self.board = []

        self.snakes = []
        #print(str(self.items))

        



       


    def rec_width(self):
        return self.contentsRect().width() / self.WIDTHINBLOCKS
    
    def rec_height(self):
        return self.contentsRect().height() / self.HEIGHTINBLOCKS
    
    def start(self):
        self.timer.start(self.SPEED, self)
        #self.engine.generate_outer_walls(100, 150)

    def paintEvent(self, event): 
        
        painter = QPainter(self)
        rect = self.contentsRect()
        
        global selectedColor

        boardtop = rect.bottom() - self.HEIGHTINBLOCKS * self.rec_height()
        data = self.client.gotten_data.get()

        data.snakes[:]

        for snake in data.snakes:

            print(snake.score)
            self.score.emit(str(snake.score))
        self.items = self.engine.get_items_on_screen(userName, data, self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        
       

        

        #print('Getting moves: ', self.items)

        for item in self.items:
            if item.skin == '@':
              
                self.draw_square(painter,rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height(), selectedColor)
             
            elif item.skin == 'O':
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height(), selectedColor)
                #print('drawing new item at:', end=' ')
                #print(item.x ,item.y )
            
            elif item.skin == 'A':
                color = QColor(255, 0, 0)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height(),color )
            elif item.skin == '%':
                color = QColor(255, 214, 0)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height() ,color )
            elif item.skin == '#':
                color = QColor(0, 0, 0)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height() ,color )

            
                

    def draw_square(self, painter, x, y, QColor):

        painter.fillRect(int(x) , int(y) , int(self.rec_width()) -2 , int(self.rec_height()) -2 , QColor)
    
    
    def timerEvent(self, event):
        
        if event.timerId() == self.timer.timerId():
            #self.paintEvent(event)
            #print('Moving')
            #self.engine.snake.move(self.direction)
           # self.client.send_action(self.direction)
    
            if len(self.items)==0:
                self.gameover()
                self.timer.stop()
                

  
                
                
            #self.paintEvent(event)
            #print("okey")
            #self.length.emit(str(len(self.engine.snake.body)+1))
            
           

            self.update()

    def gameover(self):

        
        self.gameoverWidget = Ui_Form(self)
        self.gameoverWidget.show()

           

  
   
    def keyPressEvent(self, event):

        
        #print('noe')

        key = event.key()
        if key == Qt.Key_W or key == Qt.Key_Up:
            #self.engine.snake.move(key)
            self.client.send_action("w")
            self.direction = 'w'
            print('you pressed w')

        if key == Qt.Key_A or key == Qt.Key_Left:
            #self.engine.snake.move(key)
            self.client.send_action("a")
            self.direction = 'a'
            print("you pressed a")
        
        if key == Qt.Key_D or key == Qt.Key_Right:
            #self.engine.snake.move(key)
            self.client.send_action("d")
            self.direction = 'd'
            print("you pressed d")

        if key == Qt.Key_S or key == Qt.Key_Down:
            #self.engine.snake.move(key)
            self.client.send_action("s")
            self.direction = 's'
            print("you pressed s")

        
        

class LoginDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 200)
        Dialog.setStyleSheet("background: rgb(172, 172, 172)")
        self.userLabel = QtWidgets.QLabel(Dialog)
        self.userLabel.setGeometry(QtCore.QRect(10, 20, 241, 22))
        self.userLabel.setObjectName("enter_nickname")
        self.pick = QtWidgets.QLabel(Dialog)
        self.pick.setGeometry(QtCore.QRect(10,50, 241, 22))
        self.pick.setObjectName("pick_color")
        self.userName = QtWidgets.QLineEdit(Dialog)
        self.userName.setGeometry(QtCore.QRect(125, 20, 241, 22))
        self.userName.setObjectName("userName")
        self.userName.setStyleSheet("background: rgb(255, 255, 255)")
        self.userName.setMaxLength(6)
        self.enterGame = QtWidgets.QPushButton(Dialog)
        self.enterGame.setGeometry(QtCore.QRect(170, 125, 175, 50))
        self.enterGame.setObjectName("enterGame")
        self.enterGame.clicked.connect(self.enter_game)
        self.enterGame.setStyleSheet("background: rgb(130, 255, 127)")
        self.enterGame.setCursor(QCursor(Qt.PointingHandCursor))
        self.pickcolor = QtWidgets.QPushButton(Dialog)
        self.pickcolor.setGeometry(QtCore.QRect(125, 50, 241, 28))
        self.pickcolor.setObjectName("pickcolor")
        self.pickcolor.setStyleSheet("background: rgb(255, 255, 255)")
        self.pickcolor.clicked.connect(self.colorDialog)
        self.pickcolor.setCursor(QCursor(Qt.PointingHandCursor))
        self.framecolor = QtWidgets.QFrame(Dialog)
        self.framecolor.setGeometry(QtCore.QRect(390, 30, 100, 75))
        self.instructions = QtWidgets.QLabel(Dialog)
        self.instructions.setGeometry(QtCore.QRect(140, 90, 241, 22))
        self.instructions.setObjectName("instructions")

        
        #color = QtGui.QColor(0, 0, 255)
        self.framecolor.setStyleSheet("QWidget { background-color: %s}" %selectedColor.name())
      
    

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def colorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.framecolor.setStyleSheet("QWidget { background-color: %s}" %color.name())
            global selectedColor
            selectedColor = color
            #print (selectedColor)
    
    def enter_game(self):
        name = self.userName.text()
        global userName
        userName=name
        self.main = Mainwindow(name)
        self.main.show()
        self.deleteLater()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Get ready to play Snok!"))

        self.enterGame.setText(_translate("Dialog", "Enter Game"))
        self.enterGame.setText(_translate("Dialog", "Enter Game"))
        self.pickcolor.setText(_translate("Dialog", "Pick Color"))
        self.userLabel.setText(_translate("Dialog", "Enter nickname: "))
        self.pick.setText(_translate("Dialog", "Choose your color: "))
        self.instructions.setText(_translate("Dialog", 'Move with "WASD" or the arrowkeys!'))


    

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    login = LoginDialog()
    login.setWindowFlags(Qt.Window)
    login.show()
    sys.exit(app.exec_())
    
    


if __name__ == '__main__':
    main()
