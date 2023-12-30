from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("Forma Alternativa")
        self.displayWidgets()

    def displayWidgets(self):
        self.boton = QPushButton("Presioname", self)
        self.boton.move(80, 100)
        self.boton.clicked.connect(self.displayCuadroDialogo)

    def displayCuadroDialogo(self):
        cuadro = QMessageBox(self)
        cuadro.setIcon(QMessageBox.Warning)
        cuadro.setWindowTitle("Forma Alternativa")
        cuadro.setText("Este es el texto del cuadro de dialogo")
        cuadro.setInformativeText("Este es un texto informativo")
        cuadro.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        cuadro.setDefaultButton(QMessageBox.Cancel)
        cuadro.setDetailedText("Esta es una información detallada para nuestro cuadro de dialogo")
        boton = cuadro.exec_()

        if boton == QMessageBox.Save:
            print("Presionaste el boton Guardar")
        elif boton == QMessageBox.Cancel:
            print("Presionaste el boton Cancelar")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_()).exit(app.exec_())
