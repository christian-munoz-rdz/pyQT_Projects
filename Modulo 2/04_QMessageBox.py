from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys

class MostrarCuadroDialogo(QWidget):
    def __init__(self):
        super(MostrarCuadroDialogo, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 340, 200)
        self.setWindowTitle('QMessageBox')
        self.mostrarWidgets()

    def mostrarWidgets(self):
        label_Catalogo = QLabel('Catalogo de Peliculas', self)
        label_Catalogo.move(20, 20)
        label_Catalogo.setFont(QFont('Arial', 20))

        label_Pelicula = QLabel('Ingrese el nombre de la pelicula que está buscando', self)
        label_Pelicula.move(20, 60)

        label_Nombre = QLabel('Nombre' , self)
        label_Nombre.move(20, 90)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Nombre de la pelicula")
        self.lineEdit.move(80, 90)
        self.lineEdit.resize(240, 20)

        self.boton = QPushButton('Buscar', self)
        self.boton.move(95, 130)
        self.boton.resize(150, 40)
        self.boton.clicked.connect(self.mostrarCuadroDialogo)

    def mostrarCuadroDialogo(self):
        try:
            with open('peliculas.txt', ) as f:
                peliculas = [linea.rstrip('\n') for linea in f]
        except FileNotFoundError:
            print('El archivo no existe')

        if self.lineEdit.text() in peliculas:
            QMessageBox.information(self, 'Película Encontrada', 'La pelicula se encuentra en el catalogo', QMessageBox.Ok, QMessageBox.Ok)
        else:
            peliculaNoEncontrada = QMessageBox.question(self, 'Película No Encontrada', 'La pelicula no se encuentra en el catalogo, \n¿Desea continuar?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if peliculaNoEncontrada == QMessageBox.No:
                print("Cerrando la Ventana")
                self.close()
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MostrarCuadroDialogo()
    ventana.show()
    sys.exit(app.exec_())





