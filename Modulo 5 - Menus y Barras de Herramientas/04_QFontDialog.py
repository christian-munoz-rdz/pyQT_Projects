from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QTextEdit, QFontDialog
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

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(self.txted_texto)
        vlyt_principal.addWidget(self.btn_presioname)

    def presionado(self):
        fondo, ok = QFontDialog.getFont()
        self.txted_texto.setCurrentFont(fondo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()

    sys.exit(app.exec_())