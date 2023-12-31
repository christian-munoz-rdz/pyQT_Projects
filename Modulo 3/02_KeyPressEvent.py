from PyQt5.QtWidgets import  QApplication, QWidget, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.fullscreen = False
        self.lned_1 = QLineEdit(self)
        self.lned_1.keyPressEvent = self.keyPressEvent
        self.lned_2 = QLineEdit(self)
        self.lned_2.move(0, 80)
    def keyPressEvent(self, event):
        if self.lned_1.hasFocus():
            if event.text() != "a":
                print("La tecla presionada en el line edit 1 es diferente a 'a'")
                return QLineEdit.keyPressEvent(self.lned_1, event)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())