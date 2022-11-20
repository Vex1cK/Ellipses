from random import choice
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(280, 230, 201, 71))
        self.button.setObjectName("button")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Нажми =3"))


class EllipseWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.ellipse)
        self.Xes = list(range(600))
        self.Yes = list(range(400))
        self.WHes = list(range(40, 199))
        self.values = [self.Xes, self.Yes, self.WHes]

    def ellipse(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = [choice(range(255)) for _ in range(3)]
        qp.setBrush(QColor(*color))
        a = [choice(i) for i in self.values]
        qp.drawEllipse(a[0], a[1], a[2], a[2])
        qp.end()


def main():
    app = QApplication(sys.argv)
    window = EllipseWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
