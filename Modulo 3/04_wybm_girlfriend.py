from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QEvent, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from random import randint

import sys


class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()
        self.player = QMediaPlayer()
        self.startMusic()

    def initialize(self):
        self.setGeometry(500, 500, 350, 400)
        self.setWindowTitle("??????????")
        self.displayWidgets()

    def startMusic(self):
        url = 'cancion.mp3'
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(url)))
        self.player.play()
        self.player.mediaStatusChanged.connect(self.repeatMusic)

    def repeatMusic(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()

    def displayWidgets(self):
        self.lbl_pregunta = QLabel("¿Quieres ser mi novia?", self)
        self.lbl_pregunta.resize(350, 50)
        self.lbl_pregunta.setAlignment(Qt.AlignCenter)
        fondo = QFont("Arial", 17)
        fondo.setBold(True)
        fondo.setItalic(True)
        self.lbl_pregunta.setFont(fondo)
        self.lbl_pregunta.move(0, 50)
        self.lbl_pregunta.close()

        perrito = "perrito.jpg"

        try:
            with open(perrito):
                self.lbl_perrito = QLabel(self)
                pixmap = QPixmap(perrito)
                self.lbl_perrito.setPixmap(pixmap)
                self.lbl_perrito.setScaledContents(True)
                self.lbl_perrito.resize(200, 200)
                self.lbl_perrito.move(75, 0)
        except FileNotFoundError:
            print("No se encontró la imagen")

        self.btn_si = QPushButton("Sí", self)
        self.btn_si.resize(100, 40)
        self.btn_si.move(50, 200)

        self.btn_no = QPushButton("No", self)
        self.btn_no.resize(100, 40)
        self.btn_no.move(200, 200)
        self.btn_no.installEventFilter(self)

        self.btn_no.clicked.connect(self.no)
        self.btn_si.clicked.connect(self.si)

        bola = "bola_amarilla.jpg"

        try:
            with open(bola):
                self.lbl_bola_amarilla = QLabel(self)
                pixmap = QPixmap(bola)
                self.lbl_bola_amarilla.setPixmap(pixmap)
                self.lbl_bola_amarilla.move(75, 120)
                self.lbl_bola_amarilla.setScaledContents(True)
                self.lbl_bola_amarilla.resize(200, 200)
        except FileNotFoundError:
            print("No se encontró la imagen")

        self.lbl_bola_amarilla.close()

        self.presionado = False

    def no(self):
        QMessageBox.warning(self, "No tienes de otra", "Ha ocurrido un erro, este botón no funciona", QMessageBox.Ok)

    def si(self):
        self.btn_no.close()
        self.btn_si.close()
        self.lbl_perrito.close()

        self.lbl_pregunta.show()
        self.lbl_pregunta.setText("Bienvenida al mundo de la dependencia emocional!!!")
        self.lbl_pregunta.setWordWrap(True)
        fondo = QFont("Arial", 13)
        fondo.setBold(True)
        fondo.setItalic(True)
        self.lbl_pregunta.setFont(fondo)
        self.lbl_bola_amarilla.show()

        self.presionado = True

    def eventFilter(self, object, event):
        if event.type() == QEvent.HoverMove:
            x = randint(0, 250)
            y = randint(0, 360)
            self.btn_no.move(x, y)
        return False

    def closeEvent(self, event):
        if self.presionado:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())
