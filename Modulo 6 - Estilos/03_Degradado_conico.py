from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
import sys

class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.frame = QFrame(self)

        self.frame.setStyleSheet('''background: qconicalgradient(cx:0.5, cy:0.5, angle:0,
        stop:0 rgb(255, 0, 0),
        stop:0.666 rgb(0, 255, 0),
        stop:1 rgb(0,0,255))''')

        self.setCentralWidget(self.frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())
