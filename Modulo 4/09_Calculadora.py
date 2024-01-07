from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(450, 400)
        self.setWindowTitle("Calculadora")
        self.displayWidgets()

    def displayWidgets(self):
        lbl_calculadora = QLabel("Calculadora", self)
        lbl_calculadora.setFont(QFont("Arial", 20))
        lbl_calculadora.setAlignment(Qt.AlignCenter)

        self.lbl_operaciones = QLabel("", self)
        self.lbl_operaciones.setAlignment(Qt.AlignRight)

        glyt_botonera = QGridLayout()
        self.btn_0 = QPushButton("0", self)
        self.btn_1 = QPushButton("1", self)
        self.btn_2 = QPushButton("2", self)
        self.btn_3 = QPushButton("3", self)
        self.btn_4 = QPushButton("4", self)
        self.btn_5 = QPushButton("5", self)
        self.btn_6 = QPushButton("6", self)
        self.btn_7 = QPushButton("7", self)
        self.btn_8 = QPushButton("8", self)
        self.btn_9 = QPushButton("9", self)
        self.btn_punto = QPushButton(".", self)
        self.btn_igual = QPushButton("=", self)
        self.btn_suma = QPushButton("+", self)
        self.btn_resta = QPushButton("-", self)
        self.btn_multiplicacion = QPushButton("X", self)
        self.btn_division = QPushButton("/", self)
        self.btn_borrar = QPushButton("C", self)

        glyt_botonera.addWidget(self.btn_borrar, 0, 0)
        glyt_botonera.addWidget(self.btn_division, 0, 1)
        glyt_botonera.addWidget(self.btn_multiplicacion, 0, 2)
        glyt_botonera.addWidget(self.btn_resta, 0, 3)
        glyt_botonera.addWidget(self.btn_7, 1, 0)
        glyt_botonera.addWidget(self.btn_8, 1, 1)
        glyt_botonera.addWidget(self.btn_9, 1, 2)
        glyt_botonera.addWidget(self.btn_4, 2, 0)
        glyt_botonera.addWidget(self.btn_5, 2, 1)
        glyt_botonera.addWidget(self.btn_6, 2, 2)
        glyt_botonera.addWidget(self.btn_1, 3, 0)
        glyt_botonera.addWidget(self.btn_2, 3, 1)
        glyt_botonera.addWidget(self.btn_3, 3, 2)
        glyt_botonera.addWidget(self.btn_suma, 1, 3, 2, 1)
        glyt_botonera.addWidget(self.btn_igual, 3, 3, 2, 1)
        glyt_botonera.addWidget(self.btn_0, 4, 0, 1, 2)
        glyt_botonera.addWidget(self.btn_punto, 4, 2)

        lbl_historial = QLabel("Historial", self)
        lbl_historial.setFont(QFont("Arial", 18))

        self.txt_edit = QTextEdit(self)

        self.lbl_resultado = QLabel("resultado", self)
        self.lbl_resultado.setAlignment(Qt.AlignRight)

        glyt_principal = QGridLayout(self)
        glyt_principal.addWidget(lbl_calculadora, 0, 0, 1, 2)
        glyt_principal.addWidget(self.lbl_operaciones, 1, 0, 1, 1)
        glyt_principal.addWidget(lbl_historial, 1, 1, 1, 1)
        glyt_principal.addWidget(self.txt_edit, 2, 1, 3, 1)
        glyt_principal.addWidget(self.lbl_resultado, 2, 0, 2, 1)
        glyt_principal.addLayout(glyt_botonera, 4, 0)

        self.btn_0.clicked.connect(self.numero)
        self.btn_1.clicked.connect(self.numero)
        self.btn_2.clicked.connect(self.numero)
        self.btn_3.clicked.connect(self.numero)
        self.btn_4.clicked.connect(self.numero)
        self.btn_5.clicked.connect(self.numero)
        self.btn_6.clicked.connect(self.numero)
        self.btn_7.clicked.connect(self.numero)
        self.btn_8.clicked.connect(self.numero)
        self.btn_9.clicked.connect(self.numero)
        self.btn_suma.clicked.connect(self.numero)
        self.btn_division.clicked.connect(self.numero)
        self.btn_multiplicacion.clicked.connect(self.numero)
        self.btn_resta.clicked.connect(self.numero)
        self.btn_punto.clicked.connect(self.numero)

        self.btn_igual.clicked.connect(self.resultado)
        self.btn_borrar.clicked.connect(self.borrar)

    def keyPressEvent(self, event):
        if event.text().isnumeric()or event.key() in [47, 42, 45, 43, 46, 40, 41]:
            self.operacion(event.text())
        elif event.key() in [16777220, 16777221]:
            self.resultado()
        elif event.key() == 16777219:
            self.borrar()


    def operacion(self, letra):
        texto = self.lbl_operaciones.text()
        self.lbl_operaciones.setText(texto + letra)

    def numero(self):
        sender = self.sender()
        texto = self.lbl_operaciones.text()
        if sender.text() == "X":
            sender.setText("*")
        self.lbl_operaciones.setText(texto + sender.text())

    def resultado(self):
        resultado = eval(self.lbl_operaciones.text())
        self.lbl_resultado.setText(str(resultado))
        self.historial()

    def borrar(self):
        self.lbl_operaciones.setText(self.lbl_operaciones.text()[:-1])

    def historial(self):
        self.txt_edit.append(f"{self.lbl_operaciones.text()} = {self.lbl_resultado.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()

    sys.exit(app.exec_())