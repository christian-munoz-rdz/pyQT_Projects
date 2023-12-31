from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys

class Esqueleto(QWidget):
    def __init__(self):
        super(Esqueleto, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(500, 500, 200, 200)
        self.setWindowTitle("Esqueleto animado")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.mostrarEsqueleto()

    def mostrarEsqueleto(self):
        esqueleto = "esqueleto.gif"

        try:
            with open(esqueleto):
                lbl_esqueleto = QLabel(self)
                movie = QMovie(esqueleto)
                lbl_esqueleto.setMovie(movie)
                movie.start()
        except FileNotFoundError:
            print("No se encontró la imagen")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Esqueleto()
    window.show()

    sys.exit(app.exec_())