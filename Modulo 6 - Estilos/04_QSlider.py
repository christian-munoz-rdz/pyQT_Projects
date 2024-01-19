from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)

        #Diseño vertical
        self.vlyt = QVBoxLayout(self)

        #Creación de los widgets
        self.slider = QSlider(self)
        self.slider.setRange(0, 1001)
        self.slider.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self)

        #Agregamos los widgets al diseño vertical
        self.vlyt.addWidget(self.frame)
        self.vlyt.addWidget(self.slider)

        self.slider.valueChanged.connect(self.actualizar)

    def actualizar(self):
        valor = self.slider.value()/1000
        self.frame.setStyleSheet(f'''background: qconicalgradient(cx:0.5, cy:0.5, angle:90,
        stop: {valor-0.001} rgb(255, 0, 0),
        stop:{valor} rgb(255, 255, 255))''')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())