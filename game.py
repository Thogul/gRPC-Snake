from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication

import grpc;

class SnakeGUI (QMainWindow):
    
    def __init__(self):
        super().__init__()
