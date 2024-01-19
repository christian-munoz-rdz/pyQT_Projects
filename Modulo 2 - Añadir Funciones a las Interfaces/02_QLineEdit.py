from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.Initialize()

    def Initialize(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Widget QLineEdit")
        self.mostrarWidgets()

    def mostrarWidgets(self):
        QLabel("Por favor, escribe tu nombre", self).move(100, 10)
        nombre = QLabel(self)
        nombre.setText("Nombre")
        nombre.move(70, 50)

        self.nombreEntrada = QLineEdit(self)
        self.nombreEntrada.move(130, 50)
        self.nombreEntrada.resize(200, 20)
        self.nombreEntrada.setAlignment(Qt.AlignLeft)

        self.boton = QPushButton(self)
        self.boton.move(160, 110)
        self.boton.setText("Limpiar")
        self.boton.clicked.connect(self.limpiarLineEdit)

    def limpiarLineEdit(self):
        sender = self.sender()
        if sender.text() == "Limpiar":
            self.nombreEntrada.clear()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())


