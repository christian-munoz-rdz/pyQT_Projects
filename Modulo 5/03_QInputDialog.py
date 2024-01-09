from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QInputDialog
from PyQt5.QtCore import Qt
import sys

class Aplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(250, 250)

        self.label_ingreso = QLabel("Ingrese", self)
        self.label_ingreso.setAlignment(Qt.AlignCenter)

        self.boton_ingreso = QPushButton("Ingresar", self)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(self.label_ingreso)
        vlyt_principal.addWidget(self.boton_ingreso)

        self.boton_ingreso.clicked.connect(self.presionado)

    def presionado(self):
        datos, valor = QInputDialog.getText(self, "Ingreso", "Porfavor ingrese la tarjeta")

        if datos == "3173711316":
            self.label_ingreso.setText("Bienvenido")
        else:
            self.label_ingreso.setText("Tarjeta incorrecta")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Aplication()
    ventana.show()

    sys.exit(app.exec_())