from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QFont
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("Minimizar")
        self.displayWidgets()

    def displayWidgets(self):
        self.boton = QPushButton("-", self)
        self.boton.setFont(QFont("Arial", 20))
        self.boton.resize(50, 40)
        self.boton.move(40, 40)

        self.btn_maximizar = QPushButton("Maximizar", self)
        self.btn_maximizar.move(100, 100)

        self.boton.clicked.connect(self.minimizado)
        self.btn_maximizar.clicked.connect(self.maximizado)



    def minimizado(self):
        self.showMinimized()

    def maximizado(self):
        #self.showFullScreen() #Pantalla completa
        self.showMaximized() #Maximizar pantalla



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())