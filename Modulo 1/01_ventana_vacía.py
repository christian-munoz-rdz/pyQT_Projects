from PyQt5.QtWidgets import QApplication, QWidget
import sys

class VentanaVacia(QWidget):

    def __init__(self):
        super(VentanaVacia, self).__init__()
        self.initializeUi()

    def initializeUi(self):
        #Definir el tamaño de la ventana
        self.setGeometry(100, 100, 400, 600)
        #Definir el título de la ventana
        self.setWindowTitle('Mi primera ventana en PyQt5')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = VentanaVacia()
    window.show()

    sys.exit(app.exec_())

