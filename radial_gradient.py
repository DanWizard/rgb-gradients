from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import sys
# from PyQt5.QtGui import QPainter, QBrush, QPen, QRadialGradient
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPoint
import threading 
from random import randint as rint

 
 
class Window(QMainWindow):
    def __init__(self, app):
        super().__init__()
 
        self.title = "PyQt5 Radial Gradient"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 500
        self.app = app
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.app.primaryScreen().grabWindow(self.winId()).save("3.png", "png")

    
    # def createLevels(self, count):
 
 
    def paintEvent(self, event):
        self.app.primaryScreen().grabWindow(self.winId()).save("3.png", "png")

        painter = QPainter(self)

        levels = [2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
 
        radialGradient = QRadialGradient(QPoint(250,250), 300)
 

        complexity = levels[rint(0, len(levels) - 1)]
        increment = float(1/complexity)
        current = 0

        while current < 1:
            radialGradient.setColorAt(current, QColor(rint(0,255), rint(0,255), rint(0,255), rint(0,255)))
            current += increment
        painter.setBrush(QBrush(radialGradient))
 
        painter.drawRect(-2,-2, 504,504)
        self.app.primaryScreen().grabWindow(self.winId()).save("3.png", "png")

def saveIt(app, winId):
    app.primaryScreen().grabWindow(winId).save("3.png", "png")
    app.quit()
 
 
 
 
App = QApplication(sys.argv)
window = Window(app=App)
timer = threading.Timer(.1, saveIt,[App, window.winId()])
timer.start()
# event = QEvent(QEvent.WindowActivate)
# App.sendEvent(window, event)
sys.exit(App.exec())