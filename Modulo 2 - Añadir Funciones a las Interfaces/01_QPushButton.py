from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
import sys

class VentanaBoton(QWidget):
    def __init__(self):
        super(VentanaBoton,self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Ventana con botón')
        self.mostrarBotones()

    def mostrarBotones(self):
        label = QLabel(self)
        label.setText('Presiona el botón')
        label.move(100, 20)

        boton = QPushButton('Presioname', self)
        boton.move(105, 50)
        boton.clicked.connect(self.botonPresionado)

    def botonPresionado(self):
        print("Se ha cerrado la ventana")
        self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ventana = VentanaBoton()
    ventana.show()
    sys.exit(app.exec_())



