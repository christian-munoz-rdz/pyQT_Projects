from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import QEvent
from random import randint
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(200, 200)
        self.setWindowTitle("Event Filter")
        self.displayWidgets()

    def displayWidgets(self):
        self.boton = QPushButton("XD", self)
        self.boton.resize(50, 50)
        self.boton.installEventFilter(self)

    def eventFilter(self, object, event):
        if event.type() == QEvent.HoverMove:
            x = randint(0, 150)
            y = randint( 0, 150)
            self.boton.move(x, y)
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())