from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QTextEdit, QFontDialog, QColorDialog, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Aplication(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog")

        self.txted_texto = QTextEdit(self)

        self.btn_presioname = QPushButton("Presioname", self)
        self.btn_presioname.clicked.connect(self.presionado)

        self.btn_color = QPushButton("Escoge tu color", self)
        self.btn_color.clicked.connect(self.escoger_color)

        hlyt_botones = QHBoxLayout()
        hlyt_botones.addWidget(self.btn_presioname)
        hlyt_botones.addWidget(self.btn_color)


        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(self.txted_texto)
        vlyt_principal.addLayout(hlyt_botones)

    def presionado(self):
        fondo, ok = QFontDialog.getFont()
        self.txted_texto.setCurrentFont(fondo)

    def escoger_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.txted_texto.setTextColor(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()

    sys.exit(app.exec_())