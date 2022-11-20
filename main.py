from random import choice
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys

class EllipseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
        qp.setBrush(QColor(255, 255, 0))
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
