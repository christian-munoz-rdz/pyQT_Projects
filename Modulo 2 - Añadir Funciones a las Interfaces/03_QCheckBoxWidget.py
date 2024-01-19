from PyQt5.QtWidgets import QCheckBox, QLabel, QApplication, QWidget
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle('Ventana QCheckBox')
        self.mostrarWidgets()

    def mostrarWidgets(self):
        label = QLabel('¿Qué tipo de helado quieres?',self)
        label.resize(250, 60)
        label.setAlignment(Qt.AlignCenter)

        self.vainilla = QCheckBox('Vainilla', self)
        self.vainilla.move(20, 80)

        self.chocolate = QCheckBox('Chocolate', self)
        self.chocolate.move(20, 100)

        self.fresa = QCheckBox('Fresa', self)
        self.fresa.move(20, 120)

        self.vainilla.stateChanged.connect(self.imprimirTerminal)
        self.chocolate.stateChanged.connect(self.imprimirTerminal)
        self.fresa.stateChanged.connect(self.imprimirTerminal)

    def imprimirTerminal(self, estado):
        sender = self.sender()

        if estado == Qt.Checked:
            print(f'La casilla {sender.text()} está seleccionada')
        else:
            print(f'La casilla {sender.text()} está deseleccionada')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())



