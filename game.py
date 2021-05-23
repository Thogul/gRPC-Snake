import engine_revised
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtMultimedia import *
import sys
from client import Client
from threading import Thread
import protobuffer_pb2 as game
from time import sleep


selectedColor = QtGui.QColor(255, 85, 255)
userName = str


class Mainwindow(QMainWindow):

    def __init__(self, name):
        super(Mainwindow, self).__init__()

        self.name = name

        self.setupUi(self)


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 750)
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.board.setObjectName("board")
        self.board.start()
        self.scoreboard = QtWidgets.QTextEdit(self.board)
        self.scoreboard.setGeometry(QtCore.QRect(10, 10, 200, 300))
        self.scoreboard.setFont(QFont("Arial", 12))
        self.scoreboard.setStyleSheet("background: rgba(247, 247, 247, .5); color: black")
        self.scoreboard.setObjectName("scoreboard")
        self.scoreboard.setEnabled(False)
        #self.scoreboard.setVerticalScrollBar()
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
        self.radioButton.setText(_translate("MainWindow", "Music"))
        self.statusbar.setStyleSheet(_translate("Statusbar", "Font: 10pt"))

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
        self.quitButton.setGeometry(QRect(0, 170, 110, 28))
        self.quitButton.setStyleSheet("background:rgb(255, 85, 0)")
        self.quitButton.clicked.connect(self.quitGame)
        self.playButton = QtWidgets.QPushButton(QWidget)
        self.playButton.setObjectName("playButton")
        self.playButton.setGeometry(QRect(116, 170, 110, 28))
        self.playButton.setStyleSheet("background:rgb(85, 170, 255)")
        self.playButton.clicked.connect(self.playAgian)
        self.scoreButton = QtWidgets.QPushButton(QWidget)
        self.scoreButton.setObjectName("scoreButton")
        self.scoreButton.setGeometry(QRect(232, 170, 110, 28))
        self.scoreButton.setStyleSheet("background:rgb(245, 252, 36)")
        self.scoreButton.clicked.connect(self.showScores)
        self.quitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.playButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.scoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gameOver = QtWidgets.QLabel(QWidget)
        self.gameOver.setObjectName("gameOver")
        self.gameOver.setGeometry(QRect(120, 30, 201, 61))
        self.gameOver.setStyleSheet("font: 12pt \"8514oem\";")
        self.label = QtWidgets.QLabel(QWidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(100, 90, 201, 41))
        self.label.setStyleSheet("font: 12pt \"8514oem\";")
        

        self.retranslateUi(QWidget)
        QMetaObject.connectSlotsByName(QWidget)

    def quitGame(self):
        QApplication.instance().quit()

    def playAgian(self):
        self.parent.start()
        self.close()

    def showScores(self):
       self.highscore = HighScoreWidget()
       self.highscore.show()
         
    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate

        QWidget.setWindowTitle(_translate("Widget", "Game Over!"))
        self.quitButton.setText(_translate("Widget", "Quit"))
        self.playButton.setText(_translate("Widget", "Play Again"))
        self.scoreButton.setText(_translate("Widget", "Show Highscores"))
        self.gameOver.setText(_translate("Widget", "GAME OVER"))
        self.label.setText(_translate("Widget", "Final Score : "+final_score))

class Board(QFrame):
    
    snok_score =[]
    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.WIDTHINBLOCKS = 105
        self.HEIGHTINBLOCKS = 75
        self.SPEED = 17
        self.parent = parent
        self.screen_width = int(self.parent.width())
        self.screen_height = int(self.parent.height())
        self.setFocusPolicy(Qt.StrongFocus)
        self.engine = engine_revised.Engine()
        self.client = Client(userName, self.engine)
        self.client.send_action("w")
        self.timer = QBasicTimer()

        self.direction = "w"

        self.food = []

        self.board = []

        self.snakes_score = []

        self.data = game.Data()
        self.data.alive = False
        self.data_thread = Thread(target=self.game_data_loop, daemon=True)
        self.data_thread.start()
        while not self.data.alive:
            sleep(0.5)


    def game_data_loop(self):
        while True:
            self.data = self.client.gotten_data.get()

    def rec_width(self):
        return self.contentsRect().width() / self.WIDTHINBLOCKS
    
    def rec_height(self):
        return self.contentsRect().height() / self.HEIGHTINBLOCKS
    
    def start(self):
        self.timer.start(self.SPEED, self)
        if not self.data_thread.is_alive():
            self.data_thread.start()
        self.client.send_action("w")
        self.data.alive = False

        while not self.data.alive:
            sleep(0.5)


    def paintEvent(self, event): 
        
        painter = QPainter(self)
        rect = self.contentsRect()
        
        global selectedColor

        boardtop = rect.bottom() - self.HEIGHTINBLOCKS * self.rec_height()
        #data = self.client.gotten_data.get()

        #self.data.snakes[:]

        mini_data = game.Data()
        mini_data.snakes.extend(self.data.snakes)
        mini_data.foods.extend(self.data.foods)
        mini_data.walls.extend(self.data.walls)
        self.items = self.engine.get_items_on_screen(userName, mini_data, self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        #print('Getting moves: ', self.items)

        for item in self.items:
            if item.skin == '@':
                self.draw_square(painter,rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height(), selectedColor)
            elif item.skin == 'O':
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height(), selectedColor)
            elif item.skin == 'A':
                color = QColor(255, 0, 0)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height(),color )
            elif item.skin == '%':
                color = QColor(255, 214, 0)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height() ,color )
            elif item.skin == '#':
                color = QColor(0, 0, 0)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height() ,color )
            #Other Snake
            elif item.skin == '¤':
                color = QColor(0, 0, 255)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height() ,color )
            elif item.skin == '§':
                color = QColor(0, 0, 139)
                self.draw_square(painter, rect.left() + item.x * self.rec_width(), boardtop + item.y * self.rec_height() ,color )

            
                

    def draw_square(self, painter, x, y, QColor):

        painter.fillRect(int(x) , int(y) , int(self.rec_width()) -2 , int(self.rec_height()) -2 , QColor)
    
    
    def timerEvent(self, event):
        
        if event.timerId() == self.timer.timerId():
            scores = []
            for snake in self.data.snakes:
                scores.append((snake.id, snake.score))
                if userName == snake.id:
                   global final_score
                   final_score = str(snake.score)
            scores.sort(key=lambda x : x[1], reverse=True)
            score_string = ""
            for i, (id, score) in enumerate(scores):
                if i == 20:
                    break
                score_string += f"{id}: {score}\n"
            self.parent.scoreboard.setPlainText(score_string)
            
            if not self.data.alive:
                self.gameover()
                self.timer.stop()
            
            self.update()

    def gameover(self):
        self.gameoverWidget = Ui_Form(self)
        self.gameoverWidget.show()
   
    def keyPressEvent(self, event):

        key = event.key()
        if key == Qt.Key_W or key == Qt.Key_Up:
            self.client.send_action("w")
            self.direction = 'w'
            print('you pressed w')

        if key == Qt.Key_A or key == Qt.Key_Left:
            self.client.send_action("a")
            self.direction = 'a'
            print("you pressed a")
        
        if key == Qt.Key_D or key == Qt.Key_Right:
            self.client.send_action("d")
            self.direction = 'd'
            print("you pressed d")

        if key == Qt.Key_S or key == Qt.Key_Down:
            self.client.send_action("s")
            self.direction = 's'
            print("you pressed s")

class HighScoreWidget(QWidget):

    def __init__(self, ):
        super(HighScoreWidget, self).__init__()
        self.setUp(self)

    def setUp(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(600, 500)
        Widget.setStyleSheet("background: rgb(255,255,224)")
        self.titlelabel = QtWidgets.QLabel(Widget)
        self.titlelabel.setObjectName("title")
        self.titlelabel.setGeometry(QtCore.QRect(230, 20, 150, 20))
        self.titlelabel.setStyleSheet("Font: 15pt")
        self.top = QtWidgets.QLabel(Widget)
        self.top.setObjectName("top")
        self.top.setGeometry(QtCore.QRect(250, 70, 150, 25))
        self.top.setStyleSheet("Font: 12pt")
        self.scoreboard = QtWidgets.QTextEdit(Widget)
        self.scoreboard.setEnabled(False)
        self.scoreboard.setGeometry(QtCore.QRect(160, 120, 250, 300))
        self.scoreboard.setFont(QFont("Arial", 12))
        self.scoreboard.setStyleSheet("background: rgba(247, 247, 247, .5); color: black")
        self.scoreboard.setObjectName("scoreboard")
        
        self.engine = engine_revised.Engine()
        self.client = Client(userName, self.engine)
        self.scorelist = self.client.get_high_scores()

        stringscore = ''
        for highscore in self.scorelist.scores:
            stringscore += (str(highscore.id)+' : '+str(highscore.score)+ '\n')

        self.scoreboard.setPlainText(stringscore)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)     

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Highscore"))
        self.titlelabel.setText(_translate("Widget", "Leaderboard"))
        self.top.setText(_translate("Widget", "Top 10"))


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
        self.userLabel.setStyleSheet("Font: 8pt")
        self.pick = QtWidgets.QLabel(Dialog)
        self.pick.setGeometry(QtCore.QRect(10,50, 241, 22))
        self.pick.setObjectName("pick_color")
        self.pick.setStyleSheet("Font: 8pt")
        self.userName = QtWidgets.QLineEdit(Dialog)
        self.userName.setGeometry(QtCore.QRect(125, 20, 241, 22))
        self.userName.setObjectName("userName")
        self.userName.setStyleSheet("background: rgb(255, 255, 255)")
        self.userName.setMaxLength(7)
        self.userName.setPlaceholderText("can only use up to 7 letters :)")
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
        self.instructions.setStyleSheet("Font: 8pt")
        self.framecolor.setStyleSheet("QWidget { background-color: %s}" %selectedColor.name())
      
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def colorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.framecolor.setStyleSheet("QWidget { background-color: %s}" %color.name())
            global selectedColor
            selectedColor = color
    
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
