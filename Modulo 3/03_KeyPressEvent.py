from PyQt5.QtWidgets import  QApplication, QWidget, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.fullscreen = False
        self.lned_1 = QLineEdit(self)
        self.lned_1.keyPressEvent = self.keyPressEvent()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11 and self.fullscreen == False:
            self.showFullScreen()
            self.fullscreen = True
        else:
            self.fullscreen = False
            self.showNormal()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())