from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys

class AplicacionHolaMundo(QWidget):
    def __init__(self):
        super().__init__()
        self.emptyWindow()

    def emptyWindow(self):
        self.setGeometry(100, 100, 600, 1000)
        self.setWindowTitle('Aplicacion Hola Mundo')
        self.displayLabels()

    def displayLabels(self):
        texto = QLabel(self)
        texto.setText('Hola Mundo')
        texto.move(500, 15)

        image = r"C:\Users\itzel\OneDrive\Documentos\Christian\pyQT_Projects\resources\IMGCURSO\SECCION 2\World.png"

        try :
            with open(image):
                labelImage = QLabel(self)
                pixmap = QPixmap(image)
                labelImage.setPixmap(pixmap)
                labelImage.move(30, 30)
        except FileNotFoundError:
            print('Image not found')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AplicacionHolaMundo()
    window.show()

    sys.exit(app.exec_())



