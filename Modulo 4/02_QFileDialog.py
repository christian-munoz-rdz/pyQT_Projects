from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500, 500)
        self.setWindowTitle("QFileDialog")
        self.displayWidgets()

    def displayWidgets(self):
        self.btn_abrir = QPushButton("Abrir", self)
        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.move(0, 50)

        self.btn_abrir.clicked.connect(self.open)
        self.btn_guardar.clicked.connect(self.save)

    def open(self):
        file_name = QFileDialog.getOpenFileName(self,"Abrir archivos", "../", "AllFiles(*);; Archivos de texto (*.txt)")

    def save(self):
        file_name = QFileDialog.getSaveFileName(self,"Guardar archivos", "../", "AllFiles(*);; Archivos de texto (*.txt)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())