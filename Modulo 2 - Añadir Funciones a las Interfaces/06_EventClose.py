from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys


class Evento(QWidget):
    def __init__(self):
        super(Evento, self).__init__()

    def closeEvent(self, event):
        cuadro = QMessageBox.warning(self, "Cerrar", "¿Estas seguro de cerrar la ventana?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if cuadro == QMessageBox.Yes:
            event.accept()
        elif cuadro == QMessageBox.No:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Evento()
    window.show()

    sys.exit(app.exec_())
