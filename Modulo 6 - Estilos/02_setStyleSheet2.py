from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
import sys

estilo = """QPushButton{background-color: black; color: white;}
             QPushButton:pressed{background-color: yellow; color: black;}
             QPushButton#diferente{background-color: skyblue; color: red; font: bold 30px "Calibri";}
             QPushButton#diferente:hover{background-color: yellow; color: black; font: bold 40px "Calibri";}"""

class Examples(QWidget):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("1", self)
        btn2 = QPushButton("2", self)
        btn3 = QPushButton("3", self)
        btn1.setMinimumSize(100, 100)
        btn2.setMinimumSize(100, 100)
        btn3.setMinimumSize(100, 100)
        btn3.setObjectName("diferente")

        hlyt_principal = QHBoxLayout(self)
        hlyt_principal.addWidget(btn1)
        hlyt_principal.addWidget(btn2)
        hlyt_principal.addWidget(btn3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(estilo)
    window = Examples()
    window.show()
    sys.exit(app.exec_())
