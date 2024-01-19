from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
import sys

class Examples(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        lned = QLineEdit(self)
        lned.resize(150, 80)
        lned.setStyleSheet("""
            background-color: blue;
            color: white;
            border-style: double;
            border-width: 7px;
            border-radius: 5px;
            font: bold 24px 'Times New Roman';
            qproperty-alignment: AlignCenter;
        """)

        lned.move((self.width()- lned.width())//2, (self.height() - lned.height())//2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Examples()
    window.show()
    sys.exit(app.exec_())
