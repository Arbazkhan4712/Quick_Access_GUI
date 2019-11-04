from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate, QTime,Qt , QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
import os
import webbrowser as wb
import ctypes
from DigitalClock import DigitalClock
import pyautogui

def Ss():
    img = pyautogui.screenshot()
    img.save('D:\screenshot.png')

def CODE():
    codePath = "C:\\Users\\HACKER47\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#ADD THE PATH OF THE PROGEM HERE
    os.startfile(codePath)
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "stackoverflow.com", 
        "github.com/Arbazkhan4712", 
        "gmail.com"
        )
    # wb.get(chrome_path).open('stackoverflow.com')
    # wb.get(chrome_path).open('github.com/Arbazkhan4712')
    # wb.get(chrome_path).open('gmail.com')
    for url in URLS:
        wb.get(chrome_path).open(url)


def Resarch():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "stackoverflow.com", 
        "github.com/Arbazkhan4712", 
        "google.com",
        "gmail.com",
        "youtube.com"
        )
    # wb.get(chrome_path).open('youtube.com')
    # wb.get(chrome_path).open('google.com')
    # wb.get(chrome_path).open('gmail.com')
    for url in URLS:
        wb.get(chrome_path).open(url)

def chill():
    music_dir = 'D:\\Music'
    songs = os.listdir(music_dir)
    print(songs)    
    os.startfile(os.path.join(music_dir, songs[0]))

def lock():
    ctypes.windll.user32.LockWorkStation()
date = QDateTime.currentDateTime()
# print(date.toString())
# print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))
def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('hh:mm:ss')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 761)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Clock = QtWidgets.QWidget(self.centralwidget)
        self.Clock.setGeometry(QtCore.QRect(60, 420, 120, 80))
        self.Clock.setObjectName("Clock")
        self.DigitalClock = DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(0, 10, 100, 23))
        self.DigitalClock.setDigitCount(8)
        self.DigitalClock.setObjectName("DigitalClock")
        self.Clock.setObjectName("Clock")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 62, 141, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 70, 141, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 70, 141, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 240, 141, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 250, 151, 101))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 250, 151, 101))
        self.pushButton_6.setObjectName("pushButton_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(860, 0, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(860, 290, 311, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Access"))
        self.pushButton.setText(_translate("MainWindow", "CODE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESEARCH"))
        self.pushButton_3.setText(_translate("MainWindow", "CHILL"))
        self.pushButton_4.setText(_translate("MainWindow", "VIDEO EDITING"))
        self.pushButton_5.setText(_translate("MainWindow", "Screen-Shot"))
        self.pushButton_6.setText(_translate("MainWindow", "Lock System"))
        self.pushButton.clicked.connect(CODE)
        self.pushButton_2.clicked.connect(Resarch)
        self.pushButton_3.clicked.connect(chill)
        self.pushButton_5.clicked.connect(Ss)
        self.pushButton_6.clicked.connect(lock)

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

