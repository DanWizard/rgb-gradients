from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPoint, QEvent
from random import randint as rint
import threading 

class Window(QMainWindow):
    def __init__(self, app):
        super().__init__()
 
        self.title = "PyQt5 Conical Gradient"
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
        self.app.primaryScreen().grabWindow(self.winId()).save("2.jpg", "jpg")

    def paintEvent(self, event):
        self.app.primaryScreen().grabWindow(self.winId()).save("2.jpg", "jpg")
        print('hello')
        painter = QPainter(self)

        angles = [0,45, 90, 135, 180, 225, 270]

        ratios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ]
 
        conicalGradient = QConicalGradient(QPoint(250,250), angles[rint(0,6)])
 
        conicalGradient.setColorAt(ratios[rint(0,9)], QColor(rint(0,255), rint(0,255), rint(0,255), rint(0,255)))
        conicalGradient.setColorAt(ratios[rint(0,9)], QColor(rint(0,255),rint(0,255), rint(0,255), rint(0,255)))
        conicalGradient.setColorAt(ratios[rint(0,9)], QColor(rint(0,255), rint(0,255), rint(0,255), rint(0,255)))
        painter.setBrush(QBrush(conicalGradient))
 
        this =  painter.drawRect(-2,-2, 502,502)
        print(this)
        self.app.primaryScreen().grabWindow(self.winId()).save("2.jpg", "jpg")
        # self.app.quit()

def saveIt(app, winId):
    app.primaryScreen().grabWindow(winId).save("2.jpg", "jpg")
    app.quit()


App = QApplication(sys.argv)
window = Window(app=App)
timer = threading.Timer(0.1, saveIt,[App, window.winId()])
timer.start()
# event = QEvent(QEvent.WindowActivate)
# App.sendEvent(window, event)
sys.exit(App.exec())