from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("QTextEdit")
        self.displayWidgets()

    def displayWidgets(self):
        self.btn_borrar = QPushButton("Borrar", self)
        self.btn_ontener = QPushButton("Obtener Texto", self)
        self.btn_borrar.move(215, 20)

        #QTextEdit
        self.editor = QTextEdit(self)
        self.editor.resize(300, 300)
        self.editor.move(100, 100)

        self.btn_borrar.clicked.connect(self.borrar)
        self.btn_ontener.clicked.connect(self.obtenerTexto)

    def borrar(self):
        self.editor.clear()

    def obtenerTexto(self):
        print(self.editor.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())