from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import random
import sys

class Aplication(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Icono')
        self.setWindowIcon(QIcon('images/lemon.png'))

        lbl_etiqueta = QLabel("Presiona el boton")
        lbl_etiqueta.setAlignment(Qt.AlignCenter)

        self.imagenes = ["images/lemon.png", "images/mango.png",
                         "images/orange.png", "images/strawberry.png", "images/tomato.png"]

        self.btn_icono = QPushButton(self)
        self.btn_icono.setIcon(QIcon(random.choice(self.imagenes)))
        self.btn_icono.setIconSize(QSize(60, 60))
        self.btn_icono.clicked.connect(self.cambiar_icono)

        vbox = QVBoxLayout(self)
        vbox.addWidget(lbl_etiqueta)
        vbox.addWidget(self.btn_icono)

    def cambiar_icono(self):
        self.btn_icono.setIcon(QIcon(random.choice(self.imagenes)))
        self.btn_icono.setIconSize(QSize(60, 60))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplication()
    ventana.show()

    sys.exit(app.exec_())

