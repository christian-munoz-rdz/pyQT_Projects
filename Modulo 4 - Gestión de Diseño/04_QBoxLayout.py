import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        box = QVBoxLayout(self)
        boton = QPushButton('Press', self)

        box.addStretch()
        box.addWidget(boton)
        box.addStretch()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())