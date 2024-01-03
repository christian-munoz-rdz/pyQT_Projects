import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QButtonGroup, QCheckBox

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        box = QHBoxLayout(self)
        grupo = QButtonGroup(self)

        btn1 = QCheckBox('1', self)
        btn2 = QCheckBox('2', self)

        box.addWidget(btn1)
        box.addWidget(btn2)

        grupo.addButton(btn1)
        grupo.addButton(btn2)

        grupo.buttonClicked.connect(self.onClicked)

    def onClicked(self, btn):
        print('Presionado:', btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())